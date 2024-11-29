# research_github_copilot_workspace
 
## How to run the Flask app

1. Install Flask if you haven't already:
   ```
   pip install Flask
   ```

2. Save the following code in a file named `app.py`:
   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   @app.route('/hello', methods=['GET'])
   def hello_world():
       return 'Hello, World!'

   @app.route('/hello', methods=['POST'])
   def personalized_hello():
       data = request.get_json()
       name = data.get('name', 'World')
       return f'Hello, {name}!'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=8888)
   ```

3. Run the Flask app:
   ```
   python app.py
   ```

## How to use the 'hello world' API

### GET request

To get a simple 'hello world' response, send a GET request to:
```
http://localhost:8888/hello
```

### POST request

To get a personalized 'hello world' response, send a POST request to:
```
http://localhost:8888/hello
```
with a JSON body containing the name, like this:
```json
{
    "name": "YourName"
}
```
