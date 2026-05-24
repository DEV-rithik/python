l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 35, 40, 50]
def find_diff(l1, l2):
    for i in range(min(len(l1), len(l2))):
        if l1[i] != l2[i]:
            print("first difference at index", i)
            return

    


find_diff(l1, l2)
                