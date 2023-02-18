
from collections import Counter
import statistics
from random import randint
import random

'''
PEOGRAM WRITTEN BY EGOBA KELVIN
DEVELOPED WITH PYTHON 3

Dear Code reviewer,

Note: I could not use the color(data) given to me on the website to provide solution as i could 
not use string to calculate the mean, media and mode, hence wrote a reuseble
fuction that can help in making the decision once the analysis is availiable.
This is as a result of trying to meet the deadline to submit the task.
Kindly note that i am more competent than this.
'''
#Self define vairable
nums = [10, 20, 30, 30, 40, 40, 40, 50, 50,5, 60]
target = 5

colors =[
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE","PINK", 
    "BLUE", "YELLOW", "ORANGE", "CREAM","ORANGE", "RED", 
    "WHITE", "BLUE", "WHITE", "BLUE","BLUE", "BLUE", "GREEN"
    ]

# QUESTION 1:   Which color of shirt is the mean color?
def MeanFun(param):
    length_of_frequence = len(param)
    sum_of_frequence = sum(param)
    mean = sum_of_frequence / length_of_frequence
    #print (mean)
    return mean


# QUESTION 2 : Which color is mostly worn throughout the week?

def Mostly_won_color(param):
     data = statistics.mode(param)
     #print(data)
     return data



# QUESTION 3 : Which color is the median?

def Median (param):
    result = statistics.median(param)
    #clsprint(result)
    return result


#QUESTON 4: Get the variance of the colors
def Variance (param):
    result = statistics.variance(param)
    #print(result)
    return result


#QUESTION 5 :  BONUS if a colour is chosen at random, what is the probability that the color is red?

#QUESTION 6 :       Save the colours and their frequencies in postgresql database

#QUESTION 7 BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.

def Search_algorithm(arr, key, low, high):
    if low > high:
        return (False, "Number Not Found")
    mid = (low + high)//2
    if arr[mid] == key:
        return (True, "Number Found")
    elif arr[mid] < key:
        return Search_algorithm(arr, key, mid + 1, high)
    else:
        return Search_algorithm(arr, key, low, mid - 1)
    return (False, "Number Not Found")


def Searching_method(arr, key):
    return Search_algorithm(arr, key, 0, len(arr) - 1)

#QUESTION 8: Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
def Generate_random_number(num=4):
    generated_binary_num = ""
    for i in range(num):
        temp = str(random.randint(0, 1))
        generated_binary_num += temp
        #converting it to base 10
        base_10 = int(generated_binary_num, 2)
    return base_10


#QUESTION 9 :Write a program to sum the first 50 fibonacci sequence
def Fibonacci(param):
    counters = [0, 1]
    #iterate over the fibonacci numbers
    for i in range(2, param+1):
        counters.append(counters[-1] + counters[-2])
    #add up the series
    result = sum(counters)
    return result






#Test for Output
print("QUESTION 1: MeanFun output for a given frequence=>", MeanFun(nums))
print("QUESTION 2: Mostly_won_color output for a given frequence=>", Mostly_won_color(nums))
print("QUESTION 3: Median output for a given frequence=>", Median(nums))
print("QUESTION 4: Variance output for a given frequence=>", Variance(nums))
number_to_search_for= int(input("please enter a valid number to search : "))
print('QUESTION 7: SEARCH RESULT : => ',Searching_method(sorted(nums), number_to_search_for))
print("QUESTION 9 OUTPUT: base 10=> ", Generate_random_number())
print("QUESTION 9 OUTPUT : The sum of first 50 fibonacci =>", Fibonacci(50))

