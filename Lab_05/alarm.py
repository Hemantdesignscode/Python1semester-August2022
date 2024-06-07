# CSC 1301 - Python Lab 5
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu
# Section & CRN: Section 014 and CRN 84157
import math

def main():
    alarm_hour= int(input("HOURS: "))                # The hour of the day that Road Runner needs to get out of bed.
    alarm_min = int(input("MINUTES: "))                 # The minute of the day that Road Runner needs to get out of bed.
    wake_min =  int(input("TIME: "))  # The minutes that Road Runner wants to stay in bed awake.
   

    ALARM_hour = 00   #the hour that Road Runner needs set
    ALARM_min = 00    #the minute that Road Runner needs set
    alarm_hour = ((alarm_hour * 60) + alarm_min) - (wake_min) # converts alarm_hour from hours to minutes
    HOURS = int((alarm_hour / 60)) # gets the exact amount of hours by using the type casting of int
    MIN = math.ceil(((alarm_hour / 60) - int((alarm_hour / 60))) * 60) # gets the exact amount of minutes by subtracting the integer value from the float point number and then multiplying it by 60 then using the math.ceil() function to round up to the estimated amount of minutes
    
    print("ALARM TIME: %02d:%02d" % (HOURS,MIN)) # prints the Hours and Minutes with the 00:00 format using %02d:%02d 

main()
