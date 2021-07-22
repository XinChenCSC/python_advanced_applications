from datetime import datetime


def run_time(func):
    def print_time():
        
        start_time = datetime.now()
        print("Start Time: %s"%start_time)
        func()
        end_time = datetime.now()
        print("End Time: %s"%end_time)
        total_time =  end_time - start_time
        print("Total Time: %s"%total_time)
    return print_time
@run_time
def my_type():
    print("----type----")
    for i in range(10000):
        type('hello')


my_type()