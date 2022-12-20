forcastData = ["sunny", "overcast", "rainy", "sunny", "sunny", "overcast", "rainy", "rainy", "sunny", "rainy", "sunny", "overcast", "overcast", "rainy"]
playData    = ["no", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "no", "yes", "yes", "no"]

p_forcast = input("(sunny or rainy or overcast): ")
p_play    = input("(select yes or no): ")

def calcItems(list_of_data, items):
    sam = 0
    for i in list_of_data:
        if i == items:
            sam += 1
    return sam

def calcMultiItems(list1, first_Item, list2, second_item):
    sam = 0
    i = 0
    while i != len(list1):
        if list1[i] == first_Item and list2[i] == second_item:
            sam += 1
        i += 1
    return sam

num_p_play = calcItems(playData, p_play)
num_not_p_play = len(playData) - num_p_play

pro_num_p_play = num_p_play / len(playData) 
pro_num_not_p_play  = num_not_p_play / len(playData)

print("p(H) = ", round(pro_num_p_play, 2))

num_forcast = calcMultiItems(forcastData, p_forcast, playData, p_play)
p_forcast_play = num_forcast / num_p_play
print("p(E/H) = ", round(p_forcast_play, 3))


pro_p_forcast = calcItems(forcastData, p_forcast) / len(playData)
print("P(E) = ", round(pro_p_forcast, 2))


p_play_forcast = (pro_num_p_play * p_forcast_play) / pro_p_forcast
print("p(H/E) = ", round(p_play_forcast, 3))


