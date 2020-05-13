# Introduce
this is a simple table manager. 
- view data
- pagination
- list tables
- filter



# images

![dd](img/1.jpg)


Nginx Config

```yaml

    server {
        listen       80;
        server_name xx.abc.com;
        root         /usr/share/nginx/html;

        include /etc/nginx/default.d/*.conf;
        location / {
           proxy_pass http://127.0.0.1:8081;
           proxy_set_header host $http_host;
           proxy_set_header x-real-ip $remote_addr;
           proxy_set_header x-forwarded-for $proxy_add_x_forwarded_for;
        }
        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

```