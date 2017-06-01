import SocketServer
import threading
import time


class TCPRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip()
        print(data)

        cur_thread = threading.currentThread()
        print "Current Thread:", cur_thread

        self.wfile.write(data)


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


if __name__ == '__main__':
    HOST, PORT = "localhost", 0
    server = SocketServer.TCPServer((HOST, PORT), TCPRequestHandler)

    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    print("Server loop running in thread: {}".format(server_thread.getName()))
    print("IP: %s" % ip)
    print("Port: %s" % port)

    time.sleep(60)
