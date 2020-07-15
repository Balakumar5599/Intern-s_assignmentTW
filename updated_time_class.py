class Time:

    def __init__(self,hours,mins):
        
        self.hours=hours
        self.mins=mins        

def add_two_time():
    tot_time=(time1.hours*60+time1.mins)+(time2.hours*60+time2.mins)
    print("The Addition of two time is:")
    print(tot_time//60,"hrs",tot_time%60,"minutes\n")
    
def diff_of_time():
    diff_time=(time1.hours*60+time1.mins)-(time2.hours*60+time2.mins)
    print("The Difference of two two time is:")
    print(abs(diff_time//60),"hrs",abs(diff_time%60),"minutes\n")
    
def time_in_mins():
    tot_mins=(time1.hours*60+time1.mins)+(time2.hours*60+time2.mins)
    print("Total time in minutes is:")
    print(tot_mins,"minutes")
    
time1=Time(5,60)
time2=Time(2,15)

if time1.mins>60 or time2.mins>60:
    print("Enter the proper minutes and it should not more than 60 mins")
else:
    add_two_time()
    diff_of_time()
    time_in_mins()
