table = [["sunny", "overcast", "rainy", "sunny", "sunny", "overcast", "rainy", "rainy", "sunny", "rainy", "sunny", "overcast", "overcast", "rainy"], 
         ["no", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "no", "yes", "yes", "no"]]

p_forcast = input("choose one forcast to calc probablaty: ")
p_play    = input("play or no (select yes or no): ")

def numOf(table, item):
    num_item = 0
    for ite in table:
        if ite == item:
            num_item += 1
    return num_item

def numberOfy(data, word, data2, word2):
    number = 0
    for i in range(len(data)):
        if data[i] == word and data2[i] == word2:
            number += 1
    return number

num_p_play = numOf(table[1], p_play)
num_not_p_play = len(table[1]) - num_p_play

print(f"number of {p_play} is ", num_p_play)
print(f"number of other is ", num_not_p_play)

pro_num_p_play = num_p_play / len(table[1]) 
pro_num_not_p_play  = num_not_p_play / len(table[1])

print(f"number of p of {p_play} is ", round(pro_num_p_play, 2))
print(f"number of p of other is  ", round(pro_num_not_p_play, 2))

num_forcast = numberOfy(table[0], p_forcast, table[1], p_play)
p_forcast_play = num_forcast / num_p_play

print(f"probablaty of {p_forcast} / {p_play} is ", p_forcast_play)

prob_forcast = numOf(table[0], p_forcast)

pro_p_forcast = prob_forcast / len(table[1])
print(f"probablaty of {p_forcast} is ", round(pro_p_forcast, 2))
print("probablty of yes", pro_num_p_play)
print("probablty of rainy", p_forcast_play)
print("probablty of forcast", pro_p_forcast)


p_play_forcast = (pro_num_p_play * p_forcast_play) / pro_p_forcast

print(f"probablaty of {p_play} / {p_forcast}", round(p_play_forcast, 2))


if p_play_forcast < 0.5:
    print(p_play_forcast, "which is lower probability which means chances of match played is low.")
else:
    print(p_play_forcast, "which is higher probability which means chances of match played is high.")

