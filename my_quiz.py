#!/usr/bin/env python

import random
import os


def check_multiplication_answer(a, b, answer):
    ''' 
    Description: 
        Check to see if a x b is equal to answer. 
        Return True if a x b == answer. Otherwise return False
    Input:
        a - integer, first multiplier
        b - integer, second multiplier
        answer - integer, check this number is equal to a multiply by b.
    Return:
        True or False
    '''
    if a*b == answer:
        return True
    else:
        return False    

# Hint: Use random.randint(1, max_multiplier)
def generate_multiplication_question(max_multiplier):
    '''
    Description:
        Generates the two multipliers of a multiplication question.
    Input:
        max_multiplier - integer, the maximum integer of a multiplier.
        For example, if max_multiplier = 12, then the maximum multiplier will be 12
    Return:
        A tuple that represents the two multipliers. For example, (2,5) represents 2 x 5
    '''
    x = random.randint(1, max_multiplier)
    y = random.randint(1, max_multiplier)
    return x, y

def calculate_total_time(start_time, end_time):
    '''
    Description:
        Calculates the time difference between a start time and an end time.
    Input:
        start_time - A Python time object representing a start time.
        end_time - A Python time object representing an end time.
    Return:
        A time object representing the total time.
    '''
    total_time = end_time - start_time
    return total_time

def log_assessment_result(records, name = ""):
    fname = "default.csv"
    if name !="":
        fname = name+".csv"
    with open(fname, "a") as f:
        for record in records:
            update = ""
            line = ""            
            for field in record:
                if line != "":
                    line = line + "," + str(field)
                else:
                    line = str(field)
            line = line + "\n"
            update = update + line
        f.write(update)



