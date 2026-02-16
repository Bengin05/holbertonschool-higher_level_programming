#!/usr/bin/python3
"""
Simple API built using Python's http.server module.

This server:
- Handles GET requests
- Serves plain text and JSON responses
- Manages multiple endpoints
- Returns 404 for undefined routes
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):
    """Custom request handler for the simple API."""

    def do_GET(self):
        """Handle GET requests."""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.end_headers()
            self.wfile.write(
                json.dumps(data).encode("utf-8")
            )

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    """Initialize and start the HTTP server."""
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPI)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
