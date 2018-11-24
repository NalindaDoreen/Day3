def list_sort(list1):

    even = []
    odd = []
    characs = []
    dict1 = dict()
    
    if not list1:
        dict1['evens'] = even
        dict1['odds'] = odd
        dict1['chars'] = characters
        return dict1

    for i in list1:

        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)

            else:
                odd.append(i)

        elif isinstance(i, str):
            characs.append(i)

    dict1['evens'] = sorted(even)
    dict1['odds'] = sorted(odd)
    dict1['chars'] = sorted(characs)
    return dict1


print(list_sort([1,2,3,4,5,'a','b','c']))