def fbgen(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 7 == 0:
            print("Fizz Buzz ", end = "")
        elif i % 3 == 0:
            print("Fizz ",end = "")
        elif i % 7 == 0:
            print("Buzz ",end = "")
        else:
            print(i," ",end = "",)
            
def fbgen_3or5(n):
    for i in range(1,n+1):
        fizz, buzz = [], []
        fizz = ["Fizz" for dig in str(i) if int(dig) == 3]
        buzz = ["Buzz" for dig in str(i) if int(dig) == 5]
        if fizz:
            print("fizz ",end = "",)
        elif buzz:
            print("buzz ",end = "",)
        else:
            print(i, end = " ")
