# Question 2

## How to use these scripts

These scripts are written with Python 3.7.1 so this version of Python should be installed (the solution was not tested with
other Python 3 versions). They are not Python 2 compatible. Depending on your system you should use either *python* or *python3* command.
First, it is required to run the server.

```bash
python3 server.py
```

Server will listen port 2999. Clients are instructed to use this port so it should not be provided anywhere. Client should be started in the following way:

```bash
python3 server.py HOST URL WORD
```

The scripts takes the following set of parameters. First, there is *HOST*, which is a name of the host where server resides. URL is an URL of starting page and WORD is a word to search.
Server is going to block terminal, so either a client should be launched in another terminal, or the server should be started in background mode. Word appearances will be shown in
client's console output. There might be multiple clients working with the same server simultaneously.

## Assumptions, limitations and future work

It is assumed, that the server will be using port 2999. So a user is not expected to explicitly provide it.

