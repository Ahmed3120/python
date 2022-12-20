array = [["sunny", "overcast", "rainy", "sunny", "sunny", "overcast", "rainy", "rainy", "sunny", "rainy", "sunny", "overcast", "overcast", "rainy"], 
         ["no", "yes", "yes", "yes", "yes", "yes", "no", "no", "yes", "yes", "no", "yes", "yes", "no"]]

#حساب اعداد ال yes و no
yes = 0
for i in array[1]:
    if i == "yes":
        yes += 1

#حساب احتماليت ال yes مقسوم عدد ال yes
pYes = yes / len(array[1]) 
print("p(yes) = ", pYes)

#حساب عدد الاجواء المتكررة 
nf = 0
for i in range(len(array[0])):
    if array[0][i] == "rainy" and array[1][i] == "yes":
        nf += 1

#حساب احتماليت الجو  = الجو تقسم احتماليت العب
pRainyYes = nf / yes

print("p(rainy / yes) = ", pRainyYes)

# حساب احتماليت الجو = عدد تكزاز الجو مقسم على حجم الجدول
pRainy = 0
for i in array[0]:
    if i == "rainy":
        pRainy += 1
pRainy = pRainy / len(array[0])
print("p(rainy) = ", pRainy)

# اخيرا معادلة استخراج الاحتمالية 
pyesRainy = (pYes * pRainyYes) / pRainy
print("p(yes/rainy)", pyesRainy)

