import mimetypes
from urllib.parse import urlparse
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        router = urlparse(self.path).path
        match router:
            case '/':
                self.send_html('index.html')
        
        
    def do_Post(self):
        pass

    def send_html(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as f:
            self.wfile.write(f.read())    
    
def run(server_class=HTTPServer, handler_class=MyServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    
    
    
if __name__ == "__main__":
    run()