# Making-URL-queries
This was done as part of my course 'Introduction to Programming'.It was a stepping stone to what I knew about programming done in high school.\
Here, I will cover what I learnt and all the necessary resources required on the way.

## Learning Objectives:
- Currency Exchange Services
- String operations in python.
- Basic knowledge about JSON. 
- Making URL queries and reading their output.
- Testing using unittest
- Basic sorting algorithms

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
## 1. Queries for Getting the data
- Python provides us with various sets of pre-defined functions which we can directly call
to perform tasks. Such a set of functions is called a module. In order to use these
functions, you will have to import it’s corresponding module first.
- To get the data from the given APIs through __python script__, we use __urllib.request module__
of python. You can use the following functions:
1. __urlopen()__ : Opens the given api as an object. It takes URL of the webpage as an
argument as string. It returns a network object for reading purposes.
2. __read()__ : Reads the network object and returns the data as a string.\
__Example:__
```
url = urllib.request.urlopen(​ "https://api.exchangeratesapi.io/latest"​ )
data = url.read()
```
#### 1.1 Latest Currency Exchange Rates Query
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
## 2. Queries for Processing Data 

Once we have implemented getLatestRates() correctly, we have the currency
exchange data in the form of a string. 
Now we will process it and apply __String module functions__ (you don’t need to import any modules for this) to perform the following queries.
 #### 2.1 Original currency to Desired currency change query
- For this task, I have to use the second link to read the JSON and store the result as
a string. 
- Using this string, you have to implement the following function that takes the
amount, original currency, desired currency and date and converts the amount of
original currency to the desired currency on the specified date.
- I also had to __edit the link in order to procure the data for the specified date__.
__Example:__
- If 1 GBP = 100 INR, a function call of changeBase(250, “INR”, “GBP”,
“2010-10-25”) returns 2.5 (since 250 INR was equal to 2.5 GBP on 25th October 2010).
- Similarly, if 1 USD = 80 INR, a function call of changeBase(100, “INR”, “USD”,
“2010-10-25”) returns 1.25.
```
def changeBase(amount,currency,desiredCurrency,date):
    """Outputs: a float value f.
    """
    url=urlopen("https://api.exchangeratesapi.io/"+date)
    data=url.read()
    result=eval(data)    
    a=result["rates"][currency]
    b=result["rates"][desiredCurrency]
    value=(b/a)*amount
    return value
```
#### 2.2 Print ascending order of latest rates query
- For this task, first, we have get the json string of latest rates (using the first link) and
then print them in ascending order based on the rates.
```
def printAsending(json):
    """Output: the sorted order of the Rates 
       You don't have to return anything.
	   Parameter:
       json: a json string to parse
    """
    data=eval(json)#converts string into dictionary
    x=data["rates"]#a dictionary of only rates
    y=sorted(x.items(),key=lambda x:x[1])#sorts according to the values and returns a list of tuples
    x=dict(y)#converts back to dictionary
    for k in x:
        print("1 "+data["base"]+" = "+str(x[k])+" "+k)
```
#### 2.3 Strongest currency on a given Friday query
- For this task, import datetime module of python. Using some functions
of this module, get the day of the week on a particular date.
- With a given startDate and an endDate as strings (a sample date is:
“2019-09-23” which represents 23rd September 2019),edit the third link so as 
to get data ranging from startDate to endDate. 
- Once we have this data, we __find among all the Fridays that are present there, on which of them was a particular currency strongest and on which one was it the weakest__.<br/>
__Example__:
for the function call extremeFridays(“2017-01-01”, “2017-12-31”,“INR”) is:
![](https://github.com/ashcode028/Making-URL-queries/blob/f0043620fe0b2148ec8a9f01f2575db0d9254499/ip.png)
```
def extremeFridays(startDate,endDate,currency):
    """Output: on which friday was currency the strongest and on which was it the weakest.
You don't have to return anything.
		
Parameters: 
stardDate and endDate: strings of the form yyyy-mm-dd
currency: a string representing the currency those extremes you have to determine
"""
    url=urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
    data=eval(url.read())#string to dictionary
    for key in data["rates"].keys():
        y=parse(key).weekday()#converts into date format and weekday returns no of the weekday
        if(y==4):#checks if its friday
            x.update({key:data["rates"][key][currency]})#updates date and currency value on that date in a dictionary
    z=sorted(x.items(),key=lambda x:x[1])#sorting according to values
    x=dict(z)#converts tuples into dictionary
    print(currency+" was strongest on "+x[0])
    print(currency+" was weakest on "+x[-1])
```
#### 2.4 Find Missing Dates of a given range of dates query
- We observe that when we retrieve data from link 2, all the dates in the given range are not
present. Some dates are absent. 
- In this task, I print all the valid dates that are not present in the given range.
```
def findMissingDates(startDate,endDate):
    """Output: the dates that are not present when you do a json query from startDate to endDate
You don't have to return anything.
Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
 """
    url=urlurl=urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
    data=eval(url.read())#string to dictionary
    x=[]
    for key in data["rates"].keys():
        x.append(datetime.strptime(key,'%Y-%m-%d').date())#convets string to date objects
    x.sort()  #sorts the date objects 
    for i in range(len(x)-1):#print missing dates
        a=x[i]
        b=x[i+1]
        c=a+timedelta(1)
        while c!=b:#prints dates till c is equal next date
            print(c)
            c+=timedelta(1)
```
[Sample code consisiting of all queries](ip_assignment1.py)
## 3. Testing the Data
- Once we have correctly implemented the above functions, we can test whether the
code you have written is correct or not.
- We can do that by using the __unittest module__ of python.
- To make things simple, we can start to test the __changeBase function__. 
- A sample code is shown below and you can __add multiple assert statements__ (you can add assertEqual,assertAlmostEqual, assertTrue etc. of your choice) to make sure that your function is
working correctly.
```
        self.assertAlmostEqual(changeBase(782, "SGD", "PLN", "2016-04-18"), 2196.7, delta = 0.1)
		self.assertAlmostEqual(changeBase(314, "INR", "CAD", "2014-05-21"), 5.8, delta = 0.05)
		self.assertAlmostEqual(changeBase(200, "INR", "BRL","2018-02-22"), 10.05, delta = 0.1)
		self.assertAlmostEqual(changeBase(2708, "EEK", "ZAR","2009-12-01"), 1915.3, delta = 0.1)
```
[Sample test code](a1test.py)
