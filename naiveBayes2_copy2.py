
data = [
    
    ["youth", "youth", "middle", "old", "old", "old", "middle", "youth", "youth", "old", "youth", "middle", "middle", "old"],
    ["high",  "high", "high", "mid", "low", "low", "low", "mid", "low", "mid", "mid", "mid", "high", "mid"],
    ["no", "no", "no", "no", "yes", "yes", "yes", "no" , "yes", "yes", "yes", "no", "yes", "no"],
    ["fair", "excellent", "fair", "fair", "fair", "excellent", "excellent", "fair", "fair", "fair", "excellent", "excellent", "fair", "excellent"],
    ["no", "no", "yes", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no"]
    
]
x = []

x.append(input("age: "))
x.append(input("income: "))
x.append(input("student: "))
x.append(input("credits: "))


def numberOfy(data, word, data2, word2): 
    number = 0
    for i in range(len(data)):
        if data[i] == word and data2[i] == word2:
            number += 1
    return number

def probablaty(data, data2, item, num_yes, num_no):

    num_item_yes = numberOfy(data, item, data2, "yes")
    num_item_no =  numberOfy(data, item, data2,  "no")
    data_yes = num_item_yes / num_yes
    data_no  = num_item_no / num_no
        
    return data_yes, data_no

#get how many yes and no in the list
number_of_yes = 0

for ite in data[4]:
    if ite == "yes":
        number_of_yes += 1

# number of no in question
number_of_no  = abs(len(data[4]) - number_of_yes)
print("number of no and yes", number_of_no, number_of_yes)

#probablty of yes and no
prob_of_yes = number_of_yes / len(data[4])
prob_of_no = number_of_no  / len(data[4])


print("probablaty of no and yes", prob_of_no, prob_of_yes)

prob_x_yes = 1
prob_x_no  = 1

for i in range(len(x)):
    
    prob_of_yes, prob_of_no = probablaty(data[i], data[4], x[i], number_of_yes, number_of_no)
    print(f"probablaty of {i}", prob_of_yes, prob_of_no)
    prob_x_yes *= prob_of_yes
    prob_x_no  *= prob_of_no

prob_y_yes = prob_x_yes * prob_of_yes
prob_y_no  = prob_x_no  * prob_of_no
print("P(X|Ci)P(Ci) yes =", prob_y_yes)
print("P(X|Ci)P(Ci) no = ", prob_y_no)

if prob_of_yes > prob_of_no:
    print("yes")
else:
    print("NO")