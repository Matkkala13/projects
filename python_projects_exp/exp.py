string = "Mary had a little lamb Little lamb, little Lamb Mary had a little lamb. " \
"Its fleece was white as show And everywhere that Mary went Mary went, Mary went everywhere that Mary went the lamb was sure to go"
words = string.split()
total_little_count = 0 
for i in range(0, len(words)):
    if words[i].lower() == "little":
        total_little_count += 1  
    else:
        pass
print("Total count of the word 'little' is: ", total_little_count)

list1 = [1, 5, 9, 6, 3]
list2 = sorted(list1)

print(list2)


