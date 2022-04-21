# info3180-lab7-vuejs-starter

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

## Start Flask API

Remember to always create a virtual environment and install the packages in your requirements file

```bash
$ python -m venv venv (you may need to use python3 instead)
$ source venv/bin/activate (or .\venv\Scripts\activate on Windows)
$ pip install -r requirements.txt 
$ python run.py
```
``` bash

# make the database in postgress sql shell open the psql shell
$ create user "autosales";
$ create database "autosales";
$ #\password autosales  #Password123
$ alter database autosales owner to autosales;


# create a coppy of the .env file with the following:
FLASK_ENV=development
FLASK_RUN_PORT=8080
FLASK_RUN_HOST=0.0.0.0
SECRET_KEY= ak%jh%asd9#!ad8@*^asd%fa$
DATABASE_URL=postgresql://autosales:Password123@localhost/autosales
UPLOAD_FOLDER= 'uploads'

# for migrations folder to be made initiate your virtual env and run the following commands.
$ pip install flask 
$ pip install Flask-Migrate
$ pip install python-dotenv
$ pip install flask_wtf
$ pip install psycopg2
# after those commands are ran check the _init_.py and add 
# from flask_migrate import Migrate
# migrate = Migrate(app, db)
# to initiate the databse
# then to create the migrations file run the following commands
$ falsk db init
$ flask db migrate 
$ flask db upgrade 
# any other changes made to the database after makeing the changes re use the commands above.


# after adding data to the database you can view the data by opening the psql shell and running the following commands after logging in.
$
$ \c autosales #allows you to enter the specific database called autosales
$ \ dt   # shows the tables in the database
$ select * from "insert table name  here";  #to see the data uploaded to the database remove the ("") when typing in the specific table.


https://github.com/FortAwesome/vue-fontawesome