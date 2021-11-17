## Planck's Tech Assignment

This Assignment written in python 3.9 on windows with FastAPI library

## Swagger Ling

[swagger-api-planck](https://swagger-api-planck.herokuapp.com/docs)


## Installation

```bash
py -m pip install -r requirements.txt
```

## Explanation
Since these are a few API requests, I wrote them in one python file. In case there is more API requests I would divide the routers according to the prefix of the request. For example, each category of food in a different route file.
There is the _Menu class which is a singleton and its created in the startup event. In order to update the menu on a daily basis I used fastapi_utilis library. From the moment you startup the server - the Menu will update every 24 hours according to the 10bis API request.

To demonstrate the service functionality, I would suggest to write unit tests on the _Menu class, although there are functions that use private functions in this class (there to avoid duplicate code) they are still short for using unit tests (you can use stubs but it is no longer a very simple way ). Then I would do write integration tests to the routers (API requests) with the Menu class. Finally I would write stress tests to test the server's durability and scalability



