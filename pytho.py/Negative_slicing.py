log=list(map(int,input('Enter the logs : ').split()))
last_5_logs=log[-5:]
print(f"Last 5 logs: {last_5_logs} |Critical error Found:{True if 500 in last_5_logs else False}")