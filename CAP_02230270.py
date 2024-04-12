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
    return open('CSF101CAP/input_0_cap1.txt','r')

def calculate_score(file):
    score_dict = {'A X': 1, 'A Y': 4, 'A Z': 7, 'B X': 2, 'B Y': 5, 'B Z': 8, 'C X': 3, 'C Y': 6, 'C Z': 9} 
    total_value = 0
    for line in file:
        value = line.strip()
        if value in score_dict:
            total_value += score_dict[value]
    print("total value: ",total_value)

calculate_score(read_input())





   


    


       