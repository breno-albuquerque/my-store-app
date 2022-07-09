# Tech Store

It's a tech store shopping cart! 

## Links:

* Demo: https://www.youtube.com/watch?v=v8nYbiUw7RA

## Features:

##### Register/Login/Logout:
  - Register an account with valid credentials.
  - Once registered, it is possible to log in and out.

##### Search products by category:
  - Choose between multiple categories
  - Real tech products will be displayed

##### Add/Remove from cart:
  - Add the chosen products to the shopping cart
  - Remove any chosen products from the cart
  - The total value will be displayed
  - "Finish" the order

## Main tech stack:

  * Python
  * Flask
  * sqlite
  
## Running it localy:

#### Requirements:

  - python3
  - sqlite3
  - pip3 and libraries of requirements.txt

##### Clone Repository and run app:

```
$ git clone git@github.com:breno-albuquerque/tech-store.git
$ cd tech-store
$ python3 app.py
```
#### Or clone and run with docker

```
$ git clone git@github.com:breno-albuquerque/tech-store.git
$ cd tech-store
$ docker-compose up -d
$ docker exec -it flask_app bash
$ python3 app.py
```