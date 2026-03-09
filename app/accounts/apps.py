import os
import threading
import time
from django.apps import AppConfig


class accountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.accounts'

    def ready(self):
        # Self-ping keep-alive — only runs on Render to prevent free tier sleep
        if not os.environ.get('RENDER'):
            return

        def keep_alive():
            time.sleep(90)  # Wait for server to fully start
            from django.conf import settings
            url = getattr(settings, 'RENDER_EXTERNAL_URL', '')
            if not url:
                return
            ping_url = f'{url}/api/health/'
            while True:
                try:
                    import requests
                    requests.get(ping_url, timeout=10)
                except Exception:
                    pass
                time.sleep(14 * 60)  # Ping every 14 minutes (Render sleeps at 15)

        t = threading.Thread(target=keep_alive, daemon=True)
        t.start()
