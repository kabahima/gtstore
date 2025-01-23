import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from core.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = get_wsgi_application()

app = WhiteNoise(app, root=os.path.join(BASE_DIR, 'staticfiles'))

app.add_files(os.path.join(BASE_DIR, 'static'), prefix='static/')
