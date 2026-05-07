Logs= ["ERROR DISK FULL",
       "INFO STARTED",
       "ERROR FILE MISSING",
       "WARNING MEMORY LOW"]

counts = {}
for log in Logs:
    x = log.split()[0].upper()
    if x in counts:
        counts[x]+=1
    else:
        counts[x] = 1

print("--- Logtypes ---")
for key, values in counts.items():
    print(key,":",values)
most_frequent=max(counts , key = counts.get)
print("\nMost frequent log type is : ",most_frequent)