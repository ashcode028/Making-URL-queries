# Making-URL-queries
This was done as part of my course 'Introduction to Programming'.It was a stepping stone to what I knew about programming done in high school.\
Here, I will cover what I learnt and all the necessary resources required on the way.

## Learning Objectives:
- Currency Exchange Services
- String operations in python.
- Basic knowledge about JSON. 
- Making URL queries and reading their output.
- Testing using unittest

For this assignment, we will access the data of __currency exchange rates__ from the
open source website https://exchangeratesapi.io/. You can access the data using the
APIs (Application Programming Interfaces) given on the website.
<br/>
Following are the __APIs used__ for this assignment<br/>
1. https://api.exchangeratesapi.io/latest <br/>
2. https://api.exchangeratesapi.io/2010-01-12 <br/>
3. https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01 <br/>

### JSON Basics:
- The data received will be in the form of JSON representation as shown below:\
{\
"base": "EUR",\
"date": "2018-04-08",\
"rates": {\
"CAD": 1.565,\
"CHF": 1.1798,\
"GBP": 0.87295,\
"SEK": 10.2983,\
"EUR": 1.092,\
"USD": 1.2234,\
...\
}\
}
- In case you want to learn more about JSON data type you can refer to the guide on
using json module to process the data encoded in JSON.
http://docs.pythonguide.org/en/latest/scenarios/json/<br/>
__Note: We will process the response using only string operation. Module json is not used in this assignment.__
### Error Handling
Note: Date Format : yyyy-mm-dd
If an invalid query is entered,following response pops up:
```
{"error":"time data 'message' does not match format '%Y-%m-%d'"}
```
## Queries for Getting the data
- Python provides us with various sets of pre-defined functions which we can directly call
to perform tasks. Such a set of functions is called a module. In order to use these
functions, you will have to import it’s corresponding module first.
- To get the data from the given APIs through __python script__, we use __urllib.request module__
of python. You can use the following functions:
1. __urlopen()__ : Opens the given api as an object. It takes URL of the webpage as an
argument as string. It returns a network object for reading purposes.
2. __read()__ : Reads the network object and returns the data as a string.\
Example:
```
url = urllib.request.urlopen(​ "https://api.exchangeratesapi.io/latest"​ )
data = url.read()
```
#### Latest Currency Exchange Rates Query
This function is responsible to get latest current exchange rates.
```
def getLatestRates():
    """Returns: a JSON string that is a response to a latest rates query.
       The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
    """
    url=urlopen("https://api.exchangeratesapi.io/latest")
    data=url.read()
    return data
```
## Queries for Processing Data 

Once we have implemented getLatestRates() correctly, we have the currency
exchange data in the form of a string. 
Now we will process it and apply __String module functions__ (you don’t need to import any modules for this) to perform the following queries.
 #### Original currency to Desired currency change query
 
