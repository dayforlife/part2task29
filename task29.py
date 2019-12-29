def myfunc():
    text = input()
    res1 = text.replace(",", " ")
    res2 = res1.replace("!", " ")
    res3 = res2.replace("#", " ")
    return res3
print(myfunc())
