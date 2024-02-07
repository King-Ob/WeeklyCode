from datetime import datetime, timedelta
from os import path, system
from sys import argv as argument

def find_time_range(check_file):
    time_fmt = '%H:%M:%S %m/%d/%Y'
    intervals=[]
    with open (check_file,'r') as file:
        for line in file: 
            parts = line.strip().split()
            start, end = f"{parts[1]} {parts[2]}", f"{parts[-2]} {parts[-1]}"

            start_time = datetime.strptime(start, time_fmt)
            end_time = datetime.strptime(end, time_fmt)

            time_diff = end_time - start_time
            intervals.append(time_diff)

    average_interval = sum(intervals,timedelta())/len(intervals)
    average_interval_fmt = str(average_interval).split('.')[0]
    return average_interval_fmt


if __name__ == "__main__":
    if len(argument) != 2:
        error_message="\nDon't forget to pass in the log file ONLY"
        raise ValueError(f"{error_message}")

    check_file = argument[1]

    if not path.exists(check_file):
        raise FileNotFoundError(f"{check_file} does not exist")

    print(f'The average timespan is: {find_time_range(check_file)}')