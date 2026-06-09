Score=list(map(int,input("Enter the scores:").split()))
print(f"Rnaked:{sorted(Score,reverse=True)} | Top Scorer: {max(Score)} ")