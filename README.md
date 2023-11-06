# Currency conversion rate app


## How to run the app
### Running the database
1. Make sure that you don't have PostgresQL running localy and TCP port 5432 is available
2. Run this command in project directory terminal:
    ```
    docker-compose -f docker-compose-pg-only.yml up
    ```
3. You should see 'database system is ready to accept connections' at the end of the log. Keep this terminal running.

### Running the app

#### Requirements
**You need to have installed following Python modules to run this app**<br>

_psycopg2_
```
pip install psycopg2
```

_requests_
```
pip install requests
```


_python-dotenv_
```
pip install python-dotenv
```
#### Starting the app
1. In a new tab or a window of the terminal, run the app using command:
    ```
    python3 main.py
    ```
2. Follow the instructions in the terminal
