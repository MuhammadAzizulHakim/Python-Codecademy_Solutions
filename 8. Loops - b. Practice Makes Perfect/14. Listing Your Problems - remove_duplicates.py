def remove_duplicates(dirty_list):
    white_list = []
    for i in dirty_list:
        if i not in white_list:
            white_list.append(i)
    return white_list
    
print remove_duplicates(["apple","pie","pinneaple","apple","pie"])
print remove_duplicates([1,2,3,4,3,2,1,5,6,7,8,7,6,5,9,0,0,9,8])
