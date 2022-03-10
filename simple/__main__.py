def main():
    from http.server import HTTPServer
    from simple.http import HTTPHandler

    server_address = ('', 9092)
    httpd = HTTPServer(server_address, HTTPHandler)

    try:
        print('Serving HTTP on port ' + str(server_address[1]) + ' ...')
        httpd.serve_forever()
    except Exception:
        pass

    httpd.server_close()

if __name__ == "__main__":
    main()
