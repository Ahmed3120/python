def numOf(table, item):
    num_item = 0
    for ite in table:
        if ite == item:
            num_item += 1
    return num_item

def numberOfy(data, word, data2, word2): 
    number = 0
    for i in range(len(data[0])):
        if data[i] == word and data2[i] == word2:
            number += 1
    return number

def probablaty(data, data2, item, num_yes, num_no):
    pro_data_yes = []
    pro_data_no = []
    
    for i in range(len(data)):
        num_item_yes = numberOfy(data[i], item, data2[i], "yes")
        num_item_no =  numberOfy(data[i], item, data2[i],  "no")
        
        data_yes = num_item_yes / num_yes
        data_no  = num_item_no / num_no
    
        pro_data_yes.append(data_yes)
        pro_data_no.append(data_no)
    
    pro_data_yes.append(pro_data_no)
    
    return pro_data_yes

    
    

data = [
    
    ["youth", "youth", "middle", "old", "old", "old", "middle", "youth", "youth", "old", "youth", "middle", "middle", "old"],
    ["high",  "high", "high", "mid", "low", "low", "low", "mid", "low", "mid", "mid", "mid", "high", "mid"],
    ["no", "no", "no", "no", "yes", "yes", "yes", "no" , "yes", "yes", "yes", "no", "yes", "no"],
    ["fair", "excellent", "fair", "fair", "fair", "excellent", "excellent", "fair", "fair", "fair", "excellent", "excellent", "fair", "excellent"],
    ["no", "no", "yes", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no"]
    
]



# p_forcast = input("choose one forcast to calc probablaty: ")
# p_play    = input("play or no (select yes or no): ")

buy_yes = numOf(data[4], "yes")
buy_no  = len(data[4]) - buy_yes

p_buy_yes = buy_yes / len(data[4])
p_buy_no  = buy_no / len(data[4])

print(p_buy_no, p_buy_yes)

# data.append()

for i in range(len(data[0])):
    print(probablaty(data[i], data[4], 'youth', buy_yes, buy_no))

# pro_age_yes, pro_age_no  = probablaty(data[0], data[4], "youth", buy_yes, buy_no)
# pro_income_yes, pro_income_no  = probablaty(data[1], data[4], "mid", buy_yes, buy_no)
# pro_student_yes, pro_student_no  = probablaty(data[2], data[4], "yes", buy_yes, buy_no)
# pro_credit_yes, pro_credit_no  = probablaty(data[3], data[4], "fair", buy_yes, buy_no)

# print(round(pro_age_yes, 1), round(pro_age_no, 1))
# print(round(pro_income_yes, 1), round(pro_income_no, 1))
# print(round(pro_student_yes, 1), round(pro_student_no, 1))
# print(round(pro_credit_yes, 1), round(pro_credit_no, 1))


# p_x_buy_yes = pro_age_yes * pro_income_yes * pro_student_yes * pro_credit_yes
# p_x_buy_no = pro_age_no * pro_income_no * pro_student_no * pro_credit_no

# print(p_x_buy_yes * p_buy_yes)
# print(p_x_buy_no * p_buy_no)



