# Currency conversion rate app

> :warning: **If you are using mobile browser**: Be very careful here!

## How to run the app
### Running the database
1. Make sure that you don't have PostgresQL running localy and TCP port 5432 is available
2. Run this command in project directory terminal:
    ```
    docker-compose -f docker-compose-pg-only.yml up
    ```
3. You should see database system is ready to accept connections' at the end of the log. Keep this terminal running.
    > Running the database is neccessary for app to store history of user's queries

### Running the app
1. In a new tab or a window of the terminal, run the app using command:
    ```
    python3 main.py
    ```
2. Follow the instructions in the terminal