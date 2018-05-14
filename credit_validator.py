card = input("Enter Card Number: ")
card_type = ""

card_len = len(card)
if (int(card[0:2]) == 34 or int(card[0:2]) == 37) and card_len == 15:
    card_type = "AMX"
elif 51 <= int(card[0:2]) <= 55 and card_len == 16:
    card_type = "Master"
elif int(card[0]) == 4 and (card_len == 16 or card_len == 13):
    card_type = "Visa"
else:
    exit()
sum_val = 0
tmp = ""
count = 0
while count < card_len:
    if count % 2 == 0:
        sum_val += int(card[card_len - count - 1]) * 1
    else:
        tmp += str((int(card[card_len - count - 1]) * 2))
        x = int(card[card_len - count - 1]) * 2
        if x < 10:
            sum_val += x
        else:
            sum_val += x % 10
            sum_val += 1
    count += 1
'''

'''
print (sum_val)
if sum_val % 10 == 0:
    print (card_type)
else:
    print ("invalid")
