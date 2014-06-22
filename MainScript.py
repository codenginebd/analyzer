#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Codengine'


import datetime
import csv


class FileHandler:
    def __init__(self):
        pass
    @staticmethod
    def read_csv(file_name):
        lines = []
        with open(file_name,'r') as f:
            lines = f.readlines()

        contents = []
        for line in lines:
            contents += [[i.strip() for i in line.split(',')]]

        return contents

    @staticmethod
    def write_output(file1_contents,output_data,file_name='output.txt'):
        contents = []
        for f1_data,o_data in zip(file1_contents,output_data):
            line = f1_data+[o_data['status']]
            contents += [line]

        #First write the data to csv file using .txt extension with csv module.
        with open(file_name, 'w') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(contents)

        #To remove all whitespaces read the contents and remove all whitespaces and write back to the file.
        contents = []
        with open(file_name,'r') as f:
            contents = f.readlines()

        temp_contents = [line.rstrip() if i == len(contents) - 1 else line.rstrip()+'\n' for i,line in enumerate(contents)]
        contents = temp_contents

        with open(file_name,'w') as f:
            for line in contents:
                f.write(line)


def get_day_of_the_week():
    DayL = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
    date = DayL[datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day).weekday()] + 'day'
    return date

class Main:
    def __init__(self):
        self.static_header = ["Sunday", "stime", "Monday", "mtime","Tuesday", "ttime","Wednesday", "wtime","Thursday", "thtime", "Friday", "ftime", "Saturday","satime"]

    def get_row_index(self):
        #Get today's day name like: Saturday
        today_day = get_day_of_the_week()
        #Now check for matching value in static list and return the index.
        for i,val in enumerate(self.static_header):
            if val == today_day:
                return i

    def check_and_return(self):
        """ This function read data from all the three files, process the data and return list of output. """
        file1_name,file2_name,file3_name = 'file1.txt','file2.txt','file3.txt'

        ### First read file1.txt,file2.txt and file3.txt. The program assumes that the contents of the file will be
        # comma separated. FileHandler.read_csv file will return a list of list where each inner list is a data row
        #like [[server1,windows,0,120,running,BAD0], [server2,linux,1,250,offline,NOK1], .....]
        file1_data = FileHandler.read_csv(file1_name)
        file2_data = FileHandler.read_csv(file2_name)
        file3_data = FileHandler.read_csv(file3_name)

        chances = []

        for file1_val,file2_val,file3_val in zip(file1_data,file2_data,file3_data):

            #This method find the column index using today's day name.
            r_index = self.get_row_index()

            #file1.txt data may be either string or int. So the comparison should be in string.
            f1_val = file1_val[2]
            #Convert the value to int. Get column value for this row using the r_index we got earlier by today's day name.
            f2_val = int(file2_val[r_index])
            f3_val = int(file3_val[r_index])

            chance = "ERROR"
            if ( f2_val > 0 and f3_val == 0 and f1_val == '1'):
                chance = "OK1"
            elif ( f2_val == 0 and f3_val > 0 and f1_val == '1'):
                chance = "NOK1"
            elif ( f2_val > 0 and f3_val > 0 and f1_val == '1'):
                chance = "NULL1"
            elif ( f2_val == 0 and f3_val == 0 and f1_val == '1'):
                chance = "BAD1"
            elif ( f2_val > 0 and f3_val == 0 and f1_val == '0'):
                chance = "OK0"
            elif ( f2_val == 0 and f3_val > 0 and f1_val == '0'):
                chance = "NOK0"
            elif ( f2_val > 0 and f3_val > 0 and f1_val == '0'):
                chance = "NULL0"
            elif ( f2_val == 0 and f3_val == 0 and f1_val == '0'):
                chance = "BAD0"
            else:
                chance = "ERROR:"

            #Append the result in a list.
            chances += [{'Server':file1_val[0],'ServerType':file1_val[1],'status':chance}]

        #return file1.txt file contents and resulted data list.
        return file1_data,chances


    def run(self):
        print 'Starting program...'
        file1_data,output_data =  self.check_and_return()

        #We have the data. So we now need to write it to out file.
        FileHandler.write_output(file1_data,output_data)
        print 'Done.'

if __name__ == "__main__":
    Main().run()



