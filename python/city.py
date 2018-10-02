city = (1,3,1,3,1)

cur_sum = 0
sum_ = 0
elem = 0
count = 0
for i in range(len(city)):
    e = city[i]
    if elem < e:
       cur_sum += sum_
       sum_ = 0
       count = 0
       elem = e
    elif elem > e:
        count+=1
        sum_+=elem-e
        if i == (len(city)-1):
            val_tmp = sum_-(elem-e)*count
            if val_tmp > 0:
                cur_sum+=val_tmp
    else:
       cur_sum += sum_
       sum_ = 0
       count = 0
       
       
print(cur_sum)
