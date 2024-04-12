def read_input():
    return open('','r')

def calculate_score(file):
    score_dict = {'A X': 1, 'A Y': 4, 'A Z': 7, 'B X': 2, 'B Y': 5, 'B Z': 8, 'C X': 3, 'C Y': 6, 'C Z': 9} 
    total_value = 0
    for line in file:
        value = line.strip()
        if value in score_dict:
            total_value += score_dict[value]
    print("total value: ",total_value)
calculate_score(read_input())

def calculate_score(file):
    score_dict = {'A X': 1, 'A Y': 4, 'A Z': 7, 'B X': 2, 'B Y': 5, 'B Z': 8, 'C X': 3, 'C Y': 6, 'C Z': 9}
    total_value = 0  
    for line in file:
        value = line.strip()
        value_from_dict = score_dict.get(value, None)
        if value_from_dict is not None:
            total_value += value_from_dict
    print("Total value:", total_value)

calculate_score(read_input())