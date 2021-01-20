def comma(list):
    if not list:
        print("Your list is empty")
    else:
        for i in range(len(list)):
            if int(i)  == len(list) - 2:
                print(str(list[i]), end = " and ")
            elif int(i) == len(list) - 1:
                print(str(list[i]) + ".")
            else:
                print(str(list[i]), end = ", ")

spam = ["apples", "bananas", "tofu", "cats"]
comma(spam)
bacon = [1,2,3,4,5,6,7,8,9]
comma(bacon)
