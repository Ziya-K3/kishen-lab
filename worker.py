"""Cloudflare Workers entrypoint. Local development still uses app.py."""

from app import app
from workers import wsgi

Default = wsgi.entrypoint(app)
