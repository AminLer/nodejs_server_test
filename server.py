from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = 'public/index.html'
        try:
            file_to_open = open(self.path).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        print("in post method")
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(self.headers)

        self.send_response(200)
        self.end_headers()
        print("{}".format(data))
        return


print("START SERVER")
httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
print("CLOSE SERVER")