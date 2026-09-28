# deployment_settings.py
from draw.env_settings import *

# Do NOT rewrite "/app.js" -> "/app.js/"
APPEND_SLASH = False

# Serve static at the site root so /app.js, /app.css, /index.html work
STATIC_URL = "/"

# Allow Django to serve static files for local/dev
SERVE_FILES = True