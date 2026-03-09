  import sys
   import os
   
   PROJECT_ROOT = '/home/xenohuru/main'
   
   if PROJECT_ROOT not in sys.path:
       sys.path.insert(0, PROJECT_ROOT)
   
   env_file = os.path.join(PROJECT_ROOT, '.env')
   if os.path.exists(env_file):
       with open(env_file) as f:
           for line in f:
               line = line.strip()
               if line and not line.startswith('#') and '=' in line:
                   key, _, value = line.partition('=')
                   os.environ.setdefault(key.strip(), value.strip())
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'cofig.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
