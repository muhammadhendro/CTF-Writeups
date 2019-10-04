https://www.mehmetfatih.com/CTFd-template-kurulumu/<br>

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
