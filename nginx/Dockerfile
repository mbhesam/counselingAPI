
FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY moshavereAPI.nginx.conf /etc/nginx/sites-available/moshavereAPI.nginx.conf
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/moshavereAPI.nginx.conf /etc/nginx/sites-enabled/
CMD ["nginx", "-g", "daemon off;"]