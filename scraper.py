import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

# -> Get the body of the economic calendar page. 
Target_URL = "https://www.myfxbook.com/forex-economic-calendar"
URL_Result = requests.get ( Target_URL )

# -> Using BeautifulSoup, parse the URL_Result and prepare it for use.
Parsed_URL_Result = BeautifulSoup ( URL_Result.text, "html.parser" )

# -> Target the economic calendar table.
Economic_Calendar_Table = Parsed_URL_Result.find ( id="economicCalendarTable" )

# -> Find scheduled economic event rows within the table.
Economic_Events = Economic_Calendar_Table.find_all ( "tr" )

# -> Declare the variables used to store event data.
Event_Date = ""
Event_Name = ""

# -> Loop through the events and reorganise them.
for Event_Row in Economic_Events:

    # -> Find the event date and event name.
    Event_Date = Event_Row.find ( "div", class_="calendarDateTd" )
    Event_Name = Event_Row.find ( "a", class_="calendar-event-link" )

    # -> Print out the results. Drop a separate line between each event.
    print ( Event_Date )
    print ( Event_Name, end="\n" *2 )