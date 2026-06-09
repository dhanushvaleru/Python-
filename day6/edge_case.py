scores=list(map(len,input("Enter the scores:").split()))
print(f"avearege npd score: {sum(scores)/len(scores)} | nps score is:{True if sum(scores)>=9 else False}")