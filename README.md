# CarSalesManage

collect static files
```python
python manage.py collectstatic
```

uwsgi.ini
```ini
[uwsgi]
http		= 127.0.0.1:8002
chdir           = /var/www/CarSalesManage
wsgi-file	= CarSalesManage/wsgi.py
master          = true
pidfile		= %(chdir)/master.pid
processes       = 1 
threads		= 2 
max-requests	= 6000
daemonize 	= %(chdir)/run.log
py-autoreload   = 1
static-map	= /static=$(chdir)/static
```