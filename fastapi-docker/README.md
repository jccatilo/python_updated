# How to dockerize a web app using Fast API and dockerizing it.

1. create a virtual environment  using *python -m venv <virtual-environment-name>*
    ```python -m venv venv```

2. activate the virtual environment by typing *.\virtual-env-name\Scripts\activate* . Note that this might be different on linux-based systems.
    ```.\venv\Scripts\activate ```

3. install dependencies of FASTAPI
    ``` pip install fastapi```

    ``` pip install uvicorn```

4. create /app/main.py

5. Grabe the example code from the [FAST API website](https://fastapi.tiangolo.com/)

    ```
    from typing import Union

    from fastapi import FastAPI

    app = FastAPI()
    import uvicorn

    @app.get("/")
    def read_root():
        return {"Hello": "World"}


    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

    if __name__ == '__main__':
        uvicorn.run(app, port=8000, host = "127.0.0.1")
    ```

6. Test App locally, CD to /app and run main.py
    ```cd app```
    ```cd python main.py```

7. open *http://127.0.0.1:8000/* on your browser and you should see *{"Hello":"World"}*

8. You can shutdown the server by hitting ctrl+c on your terminal

9. Generate requirements.txt using pip freeze
    ```pip freeze > requirements.txt```

10. Create a docker file in the root directory of the project. just follow the *Dockerfile* in the root with comments.

11. ```docker build -t python-fastapi .```

12. ```docker run -p 8000:8000 python-fastapi```

13. on your browser go to http://127.0.0.1:8000/ and you should see the previous hello world web response.