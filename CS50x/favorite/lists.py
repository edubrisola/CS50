list1 = [0, 1, 2, 3, 5, 1]
list2 = [-1, 1, 3]

def main():
    sort_list(list1)
    sort_list(list2)

    len1 = len_list(list1)
    len2 = len_list(list2)

    listnew = list1 + list2
    listnew2 = []

    for numbers in listnew:
        if numbers not in listnew2:
            listnew2.append(numbers)

    print(sorted(listnew2))


def sort_list(list):
    list = sorted(list)

def len_list(list):
    return (len(list))

if __name__ == "__main__":
    main()

