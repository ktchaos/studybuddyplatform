from presentation import test
import http.server

# Configura um manipulador simples para as solicitações GET
class HttpServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        # Define o cabeçalho de resposta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Define o corpo da resposta
        self.wfile.write(b'Study Buddy API rodando!')