# Insert Validation Schema here
# Reference: https://cerberus-sanhe.readthedocs.io/usage.html

MOVIE_SCHEMA = {
  '_id': {'type': 'string', 'required': False},
  'movie': {'type': 'string', 'required': True},
  'year': {'type': 'string', 'required': True},
  'rating': {'type': 'number', 'required': False},
  'votes': {'type': 'integer', 'required': False},
}
