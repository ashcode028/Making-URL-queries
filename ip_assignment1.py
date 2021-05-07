#Name:Ashita boyina
#Rollno:2019028
#Group no:01


from datetime import *
from urllib.request import *
from dateutil.parser import parse


def getLatestRates():
    """Returns: a JSON string that is a response to a latest rates query.
The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
"""
    url=urlopen("https://api.exchangeratesapi.io/latest")
    data=url.read()
    return data



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
        
printAsending(getLatestRates())   
changeBase

        
        
    
    

     

