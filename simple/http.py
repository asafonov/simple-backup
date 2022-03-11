from http.server import BaseHTTPRequestHandler
from simple.file import FileHandler

class HTTPHandler(BaseHTTPRequestHandler):
    def __init__():
        super().__init__()
        self.filehandler = FileHandler()

    def _set_headers(self, status = 200, headers = {}):
        self.send_response(status)

        for i in headers:
            self.send_header(i, headers[i])

        self.end_headers();

    def do_GET (self):
        response = ''

        if self.path == '/':
            response = self.main_page()
        elif self.path[0:6] == '/data/':
            response = self.data(self.path[6:])
        else:
            self._set_headers(404)

        self.wfile.write(response.encode('utf-8'))

    def do_OPTIONS (self):
        self._set_headers(200, {"Content-Type": "text/json", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "*"})

    def do_POST (self):
        print('POST request received')
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = post_data.decode('utf-8')
        self.filehandler.save(self.path[1:], data)
        self._set_headers(200, {"Content-Type": "text/json", "Access-Control-Allow-Origin": "*"})

    def data (self, filename):
        print('Data request received')
        self._set_headers(200, {"Content-Type": "text/json", "Access-Control-Allow-Origin": "*"})
        return self.filehandler.load(filename)

    def savefile (self, filename, data):
        return filename

    def loadfile (self, filename):
        return filename

    def main_page (self):
        print('Displaying main page')
        self._set_headers(200, {"Content-Type": "text/html; charset=UTF-8"})
        head = "<html><head></head>"
        body = "<body><h1>Simple backup server</h1></body></html>"
        return head + body
