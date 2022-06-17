# my-store-app

https://www.youtube.com/watch?v=v8nYbiUw7RA

## What is my-store-app:

It's a virtual store where you can: 
- Create your account, log in, search for certain type of tech products, add and remove products from your cart and "Buy" the products you selected.

## Requirements and dependences:

- python3
- sqlite3
- pip3 and libraries of requirements.txt

### Docker container:

The project also comes with a dockerfile and a docker-compose. To create the container you need to:
- Have docker installed.
- Go to the project director and run:
- <code>docker-compose up -d</code>
- Then run:
- <code>docker exec -it <container_id> bash</code>
- Inside the container all need to do is run: 
- <code>python3 app.py</code>

#### Explaining the files and folders:

- The static folder comes with the css and the javascript files to give the project a nice style and more user interactions with the page.
- The templates folder comes with all the html pages of the project.
- The layout.html file is the main template wich all the others extens from, it also has the connection with bootstrap library.
- app.py is where the back-end of the application is located, with all the routes and the connection to the database.
- helpers.py is another python files with some functions that complements the app.py file and make the connection with an external api.
- store.db is the database with all the tables the project needs to work
- tables.sqlite is just where the code to create the tables are located, in case you need it.
- The requeriments.txt comes with a list of what libraries the flask project depends on

