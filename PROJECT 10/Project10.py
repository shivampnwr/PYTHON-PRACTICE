LOGS = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMROY LOW"
]
count = {}
for logs in LOGS:
    x = logs.split()[0].upper()
    if x in count:
        count[x]+= 1
    else:
        count[x] = 1
print("--COUNT OF LOGS--")
for key,values in count.items():
    print(key, ":" ,values )

# for most frequent in the logs
most_frequent = max(count,key=count.get)
print("\nMost frequent :",most_frequent)
