from os.path import join
from socketserver import ThreadingMixIn, TCPServer, BaseRequestHandler
from subprocess import run, PIPE


class ThreadedTCPRequestHandler(BaseRequestHandler):
    def handle(self):
        command = ['./script.sh'] + self.request.recv(1024).decode().split(' ')
        print(command)
        process = run(command, stdout=PIPE, cwd=join('..','Question1'))
        # print(process.stdout)   
	while True:
            for line in process.stdout:
                print(line)
                self.request.sendall(line.encode())


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


if __name__ == '__main__':
    HOST, PORT = 'localhost', 2999
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server.serve_forever()
