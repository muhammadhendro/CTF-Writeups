https://www.mehmetfatih.com/CTFd-template-kurulumu/<br>
https://medium.com/csictf/self-hosting-a-ctf-platform-ctfd-90f3f1611587

 ```
limit_req_zone  $binary_remote_addr zone=mylimit:10m rate=10r/s;
limit_conn_zone $binary_remote_addr zone=addr:10m;
server {
	server_name mydomain.com;
	limit_req zone=mylimit burst=15;
	limit_conn addr 10;
	limit_req_status 429;
	client_max_body_size 8M;
	location / {
    		proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
  }
}
 ```

sudo apt-get install nginx<br>
 sudo nano /etc/nginx/sites-available/ctfd_app.conf<br>
 
 ```
 server {
	listen 80;
	server_name makineniziz_ip_adresi;
	
	location / {
		include proxy_params;
		proxy_pass http://localhost:4000;
	}
}
```

sudo ln -s /etc/nginx/sites-available/ctfd_app.conf /etc/nginx/sites-enabled/<br>

 sudo nginx -t<br>
sudo systemctl restart nginx<br>

gunicorn --bind "0.0.0.0:4000" -w 4 "CTFd:create_app()"<br>
