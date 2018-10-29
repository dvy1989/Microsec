from os.path import join
from socketserver import ThreadingMixIn, TCPServer, BaseRequestHandler
from subprocess import Popen, PIPE


class ThreadedTCPRequestHandler(BaseRequestHandler):
    """
    This handler is used to handle each client in separate thread
    """

    def handle(self):
        try:
            command = ['./script.sh'] + self.request.recv(1024).decode().split(' ')
            print(command)
            # Run te process and get access to stdout and stderr
            process = Popen(command, stdout=PIPE, stderr=PIPE, cwd=join('..', 'Question1'))
            # print(process.stdout)
            for line in process.stdout:
                print(line)
                self.request.sendall(line)
        except Exception as e:
            print(e)


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


if __name__ == '__main__':
    HOST, PORT = 'localhost', 2999
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server.serve_forever()
