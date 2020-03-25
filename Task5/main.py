input_str = input("input main string: ")
pos_arr = input("input pos array: ")
neg_arr = input("input negative array: ")

pos_score = 0
for pos in pos_arr:
    pos_score += input_str.count(pos)

neg_score = 0
for neg in neg_arr:
    neg_score += input_str.count(neg)

print(pos_score - neg_score)
