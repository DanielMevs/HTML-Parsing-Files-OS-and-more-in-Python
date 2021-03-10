from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta #time detla is a span of time


def main():
    #DATE OBJECTS
    #Get today's date from the simple today() method from the date class
    today = date.today()
    print("today's date is ", today)

    #print out the date's individual components
    print("Date components: ", today.day, today.mont, today.year)

    #retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is: ", today.weekday())
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    print("Which is a: ", days[today.weekday()])
    
    ## DATETIME OBJECTS
    ## Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is ", today)

    #Get the current time
    t = datetime.time(datetime.now())
    print(t)

    ## Times and dates can be formatted using a set of predefined string
    ## control codes
    now = datetime.now()

    #Date Formating

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%a, %d %B, %y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    ##Time formatting

    # %I / %H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I: %M: %S %p"))
    print(now.strftime("24-hour time: %H:%M"))

    #construct a basic timedelta and print it
    print(timedelta(days=365, hours=5, minutes=1))

    #print today's date
    now = datetime.now()
    print("today is: " + str(now))

    #print today's date one year from now
    print("one year from now it will be: " + str(now + timedelta(days=365)))

    #create a timedelta that uses more than one argument
    print("In 2 days and 3 weeks, it will be " +
          str(now + timedelta(days=2, weeks=3)))

    #calculate the date 1 week ago, formatted as a string
    t = datetime.now() - timeddelta(weeks=1)
    s = t.strftime("%A %B %d %Y")
    print("One week ago it was: " + s)

    #How many days until April Fools' Day?
    today = date.today()
    afd = date(today.year, 4, 1)

    #use date comparison to see if April Fool's has already gone for this year
    #if it has, use the replace() function to get the date for the next year
    if afd < today:
        print("April Fool's day already went by %d days ago" % ((today-afd).days))
              afd = afd.replace(year = today.year+1)

    #Now calculate the amound of time until April Fool's Day
    time_to_afd = afd - today
    print("It's just ", time_to_afd.days, "days until April Fool's Day")

      
    
    
    
    
    
    

    

    

if __name__ == "__main__":
    main()
