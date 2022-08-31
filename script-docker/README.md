# How to dockerize a simple python script.

1. create your directory. mine was **script-docker**

2. create your file. I created a **main.py**.

3. create a **Dockerfile**. Just read my comments. Thanks.

4. In your terminal, CD to your directory and type

    ```docker build -t python-imdb .```

5. then....

    ```docker run python-imdb```

6. You will see that it will crash because a part of the main.py requires user input from a terminal.

7. instead, type....

    ```docker run -t -i python-imdb```

    - -t is for us to have a pseudo terminal

    - -i is for interactive

8. In case you made some changes in your main.py or any file, you need to rebuild first before hitting docker run. 
