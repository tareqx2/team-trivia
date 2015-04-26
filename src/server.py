import SimpleHTTPServer
import SocketServer
import query

if __name__ == '__main__':
    query.app.run(port=8080,debug=True,host='0.0.0.0')