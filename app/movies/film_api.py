import json
from flask_restx import Resource
from app import api, format_error_response
from app.movies.film import Film

film_ns = api.namespace('movies', description='Movies API')

# Expected input params for GET parser
get_parser = api.parser()
get_parser.add_argument(
    'movie',
    type=str,
    help='Movie name to search. Blank will search all', required=False)

# Expected input params for POST parser
post_parser = api.parser()

post_parser.add_argument(
    'movie',
    type=str,
    help='New movie name to add',
    required=True)

post_parser.add_argument(
    'year',
    type=str,
    help='Production year',
    required=True)

post_parser.add_argument(
    'rating',
    type=float,
    help='Movie rating',
    required=True)

post_parser.add_argument(
    'votes',
    type=int,
    help='Number of votes obtained',
    required=True)

# Expected input params for DELETE parser
delete_parser = api.parser()
delete_parser.add_argument(
    'movie',
    type=str,
    help='Movie name to delete',
    required=True)


@film_ns.route('/')
class FilmApi(Film, Resource):
    def __init__(self, api):
        super().__init__()
        self.api = api

    @api.expect(get_parser)
    @film_ns.response(200, 'succeed in getting all movies')
    def get(self):
        """ GET movies """
        try:
            args = get_parser.parse_args()
            movie = args.get('movie')
            # Returns all movies if filter is empty
            result = self.search_by_name(movie) if movie else self.get_all()
            return result
        except Exception as e:
            return format_error_response(e)

    @api.expect(post_parser)
    @film_ns.response(200, 'succeed in adding new movie')
    def post(self):
        """ POST new movie """
        try:
            args = post_parser.parse_args()
            new_movie = {
              'movie': args.get('movie'),
              'year': args.get('year'),
              'rating': args.get('rating'),
              'votes': args.get('votes'),
            }
            # perform object validation
            result = self.add(new_movie)
            logger.info(f"Added new movie successfully: {json.dumps(result)}")
            return result
        except Exception as e:
            return format_error_response(e)

    @api.expect(delete_parser)
    @film_ns.response(200, 'succeed in deleting')
    def delete(self):
        """ TODO: DELETE movie """
        try:
            args = delete_parser.parse_args()
            self.delete_by_name(args.get('movie'))
        except Exception as e:
            return format_error_response(e)
