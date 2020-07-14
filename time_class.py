class Time:

    def __init__(self,time1,time2):
        
        self.time1=time1
        self.time2=time2
        self.time1_list = [int(i) for i in self.time1.split() if i.isdigit()]
        self.time2_list = [int(i) for i in self.time2.split() if i.isdigit()]
        
        if len(self.time1_list)==2:
            total_min_time1 = self.time1_list[0]*60+self.time1_list[1]
        else:
            total_min_time1 = self.time1_list[0]*60
            self.time1_list.append(0)
            
        if len(self.time2_list)==2:
            total_min_time2 = self.time2_list[0]*60+self.time2_list[1]
        else:
            total_min_time2 = self.time2_list[0]*60
            self.time2_list.append(0)
            
        self.total_minutes = total_min_time1+total_min_time2
        self.diff_time = total_min_time1-total_min_time2

    def add_two_time(self):

        print()
        if self.time1_list[1]>60 or self.time2_list[1]>60:
            print("Enter the minutes and it should not more than 60 minutes\n")
        else:
            print("Addition of time1 and time2:")
            print("{} hours and {} minutes\n".format(self.total_minutes//60,self.total_minutes%60))
        
    def diff_of_time(self):
        
        if self.time1_list[1]>60 or self.time2_list[1]>60:
            print("Enter the minutes and it should not more than 60 minutes\n")
        else:
            print("Difference between time1 and time2:")
            print("{} hours and {} minutes\n".format(abs(self.diff_time//60),abs(self.diff_time%60)))

    def time_in_mins(self):      
        
        if self.time1_list[1]>60 or self.time2_list[1]>60:
            print("Enter the minutes and it should not more than 60 minutes\n")
        else:
            print("Total Time in minutes")
            print("{} minutes".format(self.total_minutes))

time1=input("Enter the time1: ")
time2=input("Enter the time2: ")
time_obj=Time(time1,time2)

try:
    time_obj.add_two_time()
    time_obj.diff_of_time()
    time_obj.time_in_mins()
except:
    print("Enter the input in correct format")
    print("Eg: x hours and y minutes")
