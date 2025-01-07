import os
import sys

sys.path.insert(0, '/home/Leokaique10/Htliving/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')  # Ajuste aqui
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
