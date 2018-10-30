# Question 3

## Disclaimer

Well, this works only in debug mode for now.

## Installation

This project requires the following software to be installed:

* Python 3.7.1
* NodeJs 11.0.0

The solution was tested only for the described configurations. Currect work with other configurations is not guaranteed.

Installation includes the fllowing steps:
1. In git repository folder run the following command to initiate virtual environment:

```bash
python3 -m venv venv
```

1. Activate virtual environment by running:

```bash
venv\Scripts\activate
```

1. If everything is done correctly you should see *(venv)* in the beginning of the console line.

1. Install all required Python packages. This requires switching to folder Question3 (it is subfolder of repository folder) and running:

```bash
pip install -r packages.txt
```

1. When the command is finished switch to folder *frontend*. It is in Question3 folder and run:

```bash
npm install -g create-react-app
npm install
```

1. Then you need to return to Question3 folder and configure Django. I.e., run migrations and create superuser:

```bash
python3 manage.py migrate
python3 manage.py createsuperuser
```

1. That's it.

## Running the application

1. First, you should launch websocket "broker". Switch to folder Question3 in repository folder and run:

```bash
python3 ws_server.py
```

1. Then you should start Django app by running:

```bash
python3 manage.py runserver
```

1. Then switch to frontend folder and run:

```bash
npm run start
```

1. Open frontend at address localhost:3000. You will see authorization window:

![Authorization window](/images/auth.png)


