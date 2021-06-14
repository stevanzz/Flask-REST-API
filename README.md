# Flask-REST-API

This application is made using Python 3.8.0 & Flask library.
Sample data is fetched from [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/).


## Installation

requirements.txt file which contains all libraries used within the app.
Virtualenv is used to ensure clean environment before starting the app. (Not necessary)

```bash
# Install virtualenv, if not installed yet
pip install virtualenv

# Activate virtualenv
venv\Scripts\activate

# Install requirements.txt
pip3 install -r requirements.txt
```

## Usage

```bash
# Execute this command and application will run on http://localhost:5000/
python app.py
```

## Endpoints
1. Get top posts based on total number of comments
[http://localhost:5000/top-posts](http://localhost:5000/top-posts)

2. Find specific comments based on query parameters
[http://localhost:5000/comments?email=Eliseo@gardner.biz](http://localhost:5000/comments?email=Eliseo@gardner.biz)
[http://localhost:5000/comments?email=Eliseo@gardner.biz&id=1](http://localhost:5000/comments?email=Eliseo@gardner.biz&id=1)
[http://localhost:5000/comments?email=Eliseo@gardner.biz&id=1&postId=1](http://localhost:5000/comments?email=Eliseo@gardner.biz&id=1&postId=1)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


