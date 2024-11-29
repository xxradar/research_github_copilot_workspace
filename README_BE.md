# research_github_copilot_workspace

## Hoe de Flask-app te draaien

1. Installeer Flask als je dat nog niet hebt gedaan:
   ```
   pip install Flask
   ```

2. Sla de volgende code op in een bestand genaamd `app.py`:
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

3. Draai de Flask-app:
   ```
   python app.py
   ```

## Hoe de 'hello world' API te gebruiken

### GET-verzoek

Om een eenvoudige 'hello world'-reactie te krijgen, stuur een GET-verzoek naar:
```
http://localhost:8888/hello
```

### POST-verzoek

Om een gepersonaliseerde 'hello world'-reactie te krijgen, stuur een POST-verzoek naar:
```
http://localhost:8888/hello
```
met een JSON-body die de naam bevat, zoals dit:
```json
{
    "name": "YourName"
}
```
