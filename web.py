from http.server import HTTPServer, BaseHTTPRequestHandler

# Define the HTML content
content = """
<!DOCTYPE html>
<html>
<head>
    <title>WEB APPLICATION</title>
</head>
<body>
    <table border="6" bgcolor="lightyellow">
        <caption><strong>TCP/IP MODEL LAYERS</strong></caption>
        <tr bgcolor="lightgreen">
            <th>S.no</th>
            <th>Layer</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>Application</td>
            <td>HTTP</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>Presentation</td>
            <td>Data translation, encryption, and compression</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>Session</td>
            <td>Controls dialogues (connections) between computers</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>Transport</td>
            <td>Reliable data transfer (TCP/UDP)</td>
        </tr>
        <tr>
            <td>5.</td>
            <td>Network</td>
            <td>Path determination and logical addressing</td>
        </tr>
        <tr>
            <td>6.</td>
            <td>Data Link</td>
            <td>Physical addressing and error detection</td>
        </tr>
        <tr>
            <td>7.</td>
            <td>Physical</td>
            <td>Transmission of raw bit stream over physical medium</td>
        </tr>
    </table>
</body>
</html>
"""

# Define request handler
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

# Start server
server_address = ('', 5000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running on port 8000...")
httpd.serve_forever()
