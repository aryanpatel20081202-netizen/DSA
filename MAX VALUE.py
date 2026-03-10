arr=[10,20,30,40,95,100]

if arr:  
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    print("Max value:", max_val) 
else:
    print("Array is empty")