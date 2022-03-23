# Use the standard Nginx image from Docker Hub
FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
ENV HOME=/opt/repo