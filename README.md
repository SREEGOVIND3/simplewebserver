# EX01 Developing a Simple Webserver
## Date:11-04-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
            <th>PROTOCOLS</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>APPLICATION</td>
            <td>HTTP,FTP,DNS,Telent,SSH</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>TRANSPORT</td>
            <td>TCP & UDP</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>PRESENTATION</td>
            <td>SSL,SSH,IMAP,FTP,MPEG,JPEG</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>NETWORK ACCESS LAYER</td>
            <td>MAC/ETHERNET</td>
        </tr>
        <tr>
            <td>5.</td>
            <td>SESSION</td>
            <td>API'S,SOCKETS,WINSOCK</td>
        </tr>
        <tr>
            <td>6.</td>
            <td>DATA LINK </td>
            <td>ETHERNET,PPP,BRIDGE</td>
        </tr>
        <tr>
            <td>7.</td>
            <td>PHYSICAL</td>
            <td>COAX,FIBER,WIRELESS,HUBS,REPEATERS</td>
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
server_address = ('',5000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running on port 6000...")
httpd.serve_forever()

```
## OUTPUT:
![Screenshot 2025-04-15 143855](https://github.com/user-attachments/assets/7a82d363-641c-4f75-9827-436f19f1461b)

![Screenshot 2025-04-17 111613](https://github.com/user-attachments/assets/e4953858-58a3-4a43-ac2e-beb44d77151b)

## RESULT:
The program for implementing simple webserver is executed successfully.
