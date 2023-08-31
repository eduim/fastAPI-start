# Start project

If you don't install `poetry` package manager

- 1 Start the project with `poetry new <project_name>`

- 2 Start the virtual env with `poetry shell`

- 3 Install dependencies with `poetry add fastapi "uvicorn[standard]" pydantic`

  > FastAPI is the BE framework, uvicorn the web server and pydantic for data validation.

- 4 Create basic server in the `fapi/__init__.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
  return {'message': 'Hello World!'}
```

And run the script uvicorn fapi:app (location:variable/module), add the flag `--reload` for hot reloading

It should appear the url if you go to `/docs` you should see the documentation of you api.
