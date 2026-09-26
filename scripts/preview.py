"""Local clean-URL preview; binds to localhost and mirrors Vercel 404 behavior."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import os

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        if path in ('/products', '/contact'):
            self.send_response(307)
            self.send_header('Location', '/#apps' if path == '/products' else '/#contact')
            self.end_headers()
            return
        if path != '/' and not Path(path).suffix and (ROOT / (path.lstrip('/') + '.html')).is_file():
            self.path = path + '.html'
        return super().do_GET()

ThreadingHTTPServer(('127.0.0.1', 8767), Handler).serve_forever()
