    
age_data = ["youth", "youth", "middle", "old", "old", "old", "middle", "youth", "youth", "old", "youth", "middle", "middle", "old"]
income_data = ["high",  "high", "high", "mid", "low", "low", "low", "mid", "low", "mid", "mid", "mid", "high", "mid"]
student_data = ["no", "no", "no", "no", "yes", "yes", "yes", "no" , "yes", "yes", "yes", "no", "yes", "no"]
credit_data = ["fair", "excellent", "fair", "fair", "fair", "excellent", "excellent", "fair", "fair", "fair", "excellent", "excellent", "fair", "excellent"]
buy_computer = ["no", "no", "yes", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no"]
    

age = input("age: ")
income = input("income: ")
isStudent = input("is student: ")
credit = input("credits: ")

def numberOfy(data, word, data2, word2): 
    number = 0
    for i in range(len(data)):
        if data[i] == word and data2[i] == word2:
            number += 1
    return number

def numOf(table, item):
    num_item = 0
    for ite in table:
        if ite == item:
            num_item += 1
    return num_item


#get how many yes and no in the list
number_of_yes = numOf(buy_computer, "yes")
number_of_no  = abs(len(buy_computer) - number_of_yes)

print("number of no ", number_of_no)
print("number of yes", number_of_yes)

#probablty of yes and no
prob_of_yes = number_of_yes / len(buy_computer)
prob_of_no = number_of_no  / len(buy_computer)
print(numberOfy(age_data, age, buy_computer, "yes"))


print("probablaty of no and yes", prob_of_no, prob_of_yes)

prob_of_age_yes = numberOfy(age_data, age, buy_computer, "yes") / number_of_yes
prob_of_age_no = numberOfy(age_data,  age, buy_computer, "no") / number_of_no
print("probablaty of age yes", prob_of_age_yes)
print("probablaty of age no ", prob_of_age_no)

prob_of_income_yes = numberOfy(income_data, income, buy_computer, "yes") / number_of_yes
prob_of_income_no = numberOfy(income_data,  income, buy_computer, "no") / number_of_no
print("probablaty of icome yes", prob_of_income_yes)
print("probablaty of icome no ", prob_of_income_no)

prob_of_student_yes = numberOfy(student_data, isStudent, buy_computer, "yes") / number_of_yes
prob_of_student_no = numberOfy( student_data, isStudent, buy_computer, "no") / number_of_no
print("probablaty of student yes", prob_of_student_yes)
print("probablaty of student no ", prob_of_student_no)


prob_of_credit_yes = numberOfy(credit_data, credit, buy_computer, "yes") / number_of_yes
prob_of_credit_no = numberOfy( credit_data, credit, buy_computer, "no") / number_of_no
print("probablaty of student yes", prob_of_credit_yes)
print("probablaty of student no ", prob_of_credit_no)


prob_x_yes = prob_of_age_yes * prob_of_income_yes * prob_of_student_yes * prob_of_credit_yes
print("PROBABLITY OF X/BUY_COMPUTER = YES", prob_x_yes)

prob_x_no = prob_of_age_no * prob_of_income_no * prob_of_student_no * prob_of_credit_no
print("PROBABLITY OF X/BUY_COMPUTER = no", prob_x_no)

prob_y_yes = prob_x_yes * prob_of_yes
prob_y_no = prob_x_no * prob_of_no
print(prob_y_yes)
print("probablty of ", prob_y_no)


