class Time:

    def __init__(self,time1,time2):
        
        self.time1=time1
        self.time2=time2

    def set_time(self):
        
        time1_list = [int(i) for i in self.time1.split() if i.isdigit()]
        time2_list = [int(i) for i in self.time2.split() if i.isdigit()]
        if len(time1_list)==2:
            total_min_time1 = time1_list[0]*60+time1_list[1]
        else:
            total_min_time1 = time1_list[0]*60
            
        if len(time2_list)==2:
            total_min_time2 = time2_list[0]*60+time2_list[1]
        else:
            total_min_time2 = time2_list[0]*60            
        self.total_minutes = total_min_time1+total_min_time2
        self.diff_time = total_min_time1-total_min_time2

    def add_two_time(self):

        print()
        print("Addition of time1 and time2:")
        print("{} hours and {} minutes\n".format(self.total_minutes//60,self.total_minutes%60))
        
    def diff_of_time(self):

        print("Difference between time1 and time2:")
        print("{} hours and {} minutes\n".format(self.diff_time//60,self.diff_time%60))

    def time_in_mins(self):

        print("Total Time in minutes")
        print("{} minutes".format(self.total_minutes))

time1=input("Enter the time1: ")
time2=input("Enter the time2: ")
time_obj=Time(time1,time2)

try:
    time_obj.set_time()
    time_obj.add_two_time()
    time_obj.diff_of_time()
    time_obj.time_in_mins()
except:
    print("Enter the input in correct format")
    print("Eg: x hours and y minutes")
