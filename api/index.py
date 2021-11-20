from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import sys

sys.path.append('solutions')

def run_day(day):
    module_name = 'day' + day
    module = __import__(module_name)
    print(module)
    part1 = getattr(module, 'part1')
    part2 = getattr(module, 'part2')
    return f'{part1()},{part2()}'


def send_error(handler, message):
    handler.send_error(400)
    handler.wfile.write(message.encode())


def send_json(handler, content):
    handler.send_response(200)
    handler.send_header('Content-type', 'text/json')
    handler.end_headers()
    handler.wfile.write(content.encode())


def send_text(handler, content):
    handler.send_response(200)
    handler.send_header('Content-type', 'text/plain')
    handler.end_headers()
    handler.wfile.write(content.encode())


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        if self.path.startswith('/api?'):
            query = parse_qs(self.path[5:])
            print(query)
            if 'day' in query:
                day = query['day']
                if len(day) <= 0:
                    send_error('Could not parse query')
                try:
                    day = query['day'][0]
                    result = run_day(day)
                    send_text(self, result)
                except Exception:
                    send_error(self, 'Requested day not found')
            else:
                send_error(self, 'Invalid query')
        else:
            send_error(self, 'Unhandled endpoint')
