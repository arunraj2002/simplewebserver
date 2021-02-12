from http.server import HTTPServer,BaseHTTPRequestHandler

Content="""
<!doctype html>
<html lang="en">
<head>
<title>my webserver</title>
</head>
<body>
<h1>MULTIPLICATION TABLES OF 6</h1>
6×0=0<br>
6×1=6<br>
6×2=12<br>
6×3=18<br>
6×4=24<br>
6×5=30<br>
6×6=36<br>
6×7=42<br>
6×8=48<br>
6×9=54<br>
6×10=60<br>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request recived")

        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')             
        self.end_headers()

     #to send the responce
        self.wfile.write(Content.encode())

 #to create server address     
server_address=('',80)

#to listen at the specified port
httpd = HTTPServer(server_address,myhandler)
print("MY WEBSERVER IS RUNNING...")
httpd.serve_forever()