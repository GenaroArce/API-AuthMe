
# API AuthMe - Security

The AuthMe API is a simple and secure authentication API that uses hashed passwords to ensure the security of user credentials. This API provides endpoints for user registration and login, using a secure password.
## Features

**User Registration**: Allows users to register by providing their email, username and password. The password is stored securely.

**Login**: Users can log in using their registered username and password. The API verifies the provided credentials and returns an authentication token on success.
## Requirements

You can start the application by running the provided `start.bat` file. This will automatically install the required dependencies and start the Flask server.

```bash
start.bat
```

O In order to use the API you must install the requirements.

```bash
pip install -r requirements.txt
```
## Database Configuration

To configure the connection to your own MongoDB database and specify the name of the database and the collection in which you want to store the data, follow these steps:

1. Open the `app.py` file in your text editor or IDE.

2. Find the lines of code that establish the connection to the database, the name of the database, and the collection. These lines are usually found at the beginning of the `app.py` file.

```python
client = pymongo.MongoClient("MONGO_DB_URL")
db = client["MONGO_DB_NAME"]
collection = db["MONGO_DB_COLLECTION"]
```
## Usage

First, make sure you have Python 3.x and all necessary dependencies installed. Then, you can run the `app.py` file to start the API server.

```
  python app.py
```

Then in a new console execute:

```
  python main.py
```
## Examples

NOTE: Once the server is up and running, you can send HTTP requests to the provided endpoints using tools like curl or requests. Here are some usage examples:

**User registration**:
```
curl -X POST -H "Content-Type: application/json" -d '{"email": "example@example.com", "username": "usuario1", "password": "contrasena"}' http://localhost:5050/users
```

**Login**:
```
curl -X GET -H "Content-Type: application/json" -d '{"username": "usuario1", "password": "contrasena"}' http://localhost:5050/users
```
## Support

For help or a suggestion, email genaroarcee@gmail.com
