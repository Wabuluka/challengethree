# challengethree
challenge three andela
# CRUD API - Andela

In this API, I have put together a simple way in which you can create, retrieve, update and delete data from a list
## Getting Started
To get start with this API, you will need to set up a few prerequists as I am going to guide below.
### Prerequisites
This api must work on any operating system with minimal requirements

```
Windows
```
```
Mac
```
```
Linux
```
Make sure you have python version 
```
python 2.7 and above
```

### Installing


create a virtual environment with (virtualenv yourEnv).

Activate the virtual environment. (source yourEnv/bin/activate)

```
install python (pip install python)
```

```
Install Flask (pip install flask)
```
```
Install Flask (pip install flask_restful)
```

```
Install requirements (pip freeze > requirements.txt)
```

## Endpoints in the API
|REQUEST TYPE| URL | DESCRIPTION |
|------------|-----|-------------|
|POST| /api/v1/order/<int:orderId>|Place a new order|
|GET| /api/v1/orders |Get all orders|
|GET| /api/v1/order/<int:orderId> |Get specific order by orderId|
|PUT| /api/v1/order/<int:orderId> |Update a specified order by orderId|
|DELETE| /api/v1/order/<int:orderId> |Delete order|

## Running the tests

It only needs one code statement to run the test for this simple application

Run the following command in your terminal or cmd
Although at the moment my tests are not fully functional, am still learning how to make them better

```
python -m unittest
```
