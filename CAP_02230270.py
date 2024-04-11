################################
# Your Name: Pravesh Bhandari
# Your Section: 1 ME
# Your Student ID Number: 02230270
################################
# REFERENCES
# Links that you referred while solving
# the problem
# https://www.youtube.com/watch?v=4OX49nLNPEE
# https://realpython.com/read-write-files-python/
################################
# SOLUTION
# Your Solution Score: 50054
# Put your number here: 0
################################
def read_input():
    return open('input_0_cap1.txt','r')

def calculate_score(f):
    score_dict = {'A X': 1, 'A Y': 4, 'A Z': 7, 'B X': 2, 'B Y': 5, 'B Z': 8, 'C X': 3, 'C Y': 6, 'C Z': 9}
    total_value = 0  
    for line in f:
        value = line.strip()
        value_from_dict = score_dict.get(value, None)
        if value_from_dict is not None:
            total_value += value_from_dict
    print("Total value:", total_value)

calculate_score(read_input())




   


    


       