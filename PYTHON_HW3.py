
#3 Merge Sort
def merge(list1, list2):
    result = []
    new_length = len(list1) + len(list2)
    list1_count = 0
    list2_count = 0
    while len(result) != new_length:
        if len(list1) == list1_count:
            result += list2[list2_count:]
            break
        elif len(list2) == list2_count:
            result += list1[list1_count:]
            break
        elif list1[list1_count] < list2[list2_count]:
            result.append(list1[list1_count])
            list1_count += 1
        else:
            result.append(list2[list2_count])
            list2_count += 1
    return result   

#Test Case
print ("merge([1, 3, 5, 7], [2, 4, 6, 8]):\t", merge([1, 3, 5, 7], [2, 4, 6, 8]))
input("Press Enter to continue...")
