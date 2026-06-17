scores=[85,90,78,92,99]
for i in range(len(scores)):
    print(f"scores[{i}]={scores[i]}")
    #method 2

for score in scores: print(score)

# method 3(

for idx, val in enumerate(scores):
    print(f"Index {idx} -> {val}")

# method 4
doubled=[x*2 for x in scores]    