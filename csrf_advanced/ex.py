from hashlib import md5
import requests

admin_csrf_token = md5('admin127.0.0.1'.encode()).hexdigest()


