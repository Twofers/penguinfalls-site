"""Loopback-only preview of public static routes with Vercel clean URLs."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, unquote
import os
ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = unquote(urlsplit(self.path).path)
        if any(part.startswith('.') for part in Path(path).parts) or path.startswith(('/docs/', '/scripts/')):
            return self.send_error(404)
        if path in ('/products', '/contact'):
            self.send_response(307)
            self.send_header('Location', '/#twofer' if path == '/products' else '/#contact')
            self.end_headers()
            return
        if path != '/' and not Path(path).suffix and (ROOT / (path.lstrip('/') + '.html')).is_file():
            self.path = path + '.html'
        return super().do_GET()
print('Penguin Falls preview: http://127.0.0.1:8768', flush=True)
ThreadingHTTPServer(('127.0.0.1', 8768), Handler).serve_forever()
