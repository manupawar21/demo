elements = [20,51,31,58,59,54,89,23,64,32,65,34,10,50,32,69,99]
print("Before Sorting :",elements)

for i in range(len(elements)):
    for j in range((i+1),len(elements)):
        if (elements[i] > elements[j]):

            temp = elements[i]
            elements[i] = elements[j]
            elements[j] = temp

print("After Sorting :", elements)


# Time complexity
