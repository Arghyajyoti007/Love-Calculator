# def greet(name):
#     print(f"Hi {name}")
#
#
# greet("Arghya")
#
#
# # Function with more than one input
# def greet(name, location):
#     print(f"Hi {name}")
#     print(f"You are from {location}")
#
#
# # Postional Argument
# greet("Arghya", "Noida")
# # Keyword Argument
# greet(location="Kolkata", name="Arghya")


def count(test_word, name1, name2):
    new_name = name1 + name2
    new_name = new_name.lower()
    test_word = test_word.lower()
    count_num = 0
    list_of_num = []
    for i in range(len(test_word)):
        print(f"i : {i}")
        for j in range(len(new_name)):
            print(f"j : {j}")
            print('test word: ' + test_word[i])
            print("new name : " + new_name[j])

            if test_word[i] == new_name[j]:
                count_num += 1
            print(f"count : {count_num}")
        list_of_num.append(count_num)
        count_num = 0
    print(list_of_num)
    print()
    return list_of_num


def calculate_love_score(name1, name2):
    check_count1 = count("TRUE", name1, name2)
    check_count2 = count("LOVE", name1, name2)

    a = sum(check_count1)
    b = sum(check_count2)

    return str(a) + str(b)


print(calculate_love_score("Kanye West", "Kim Kardashian"))
