
def two_list_in_one(list_1, list_2):
    big_list = []
    len_lists = len(list_1)
    for i in range(len_lists):
        small_list = []
        small_list.append(list_1[i])
        small_list.append(list_2[i])
        big_list.append(small_list)

    return big_list
