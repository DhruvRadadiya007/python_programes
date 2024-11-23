# match case statements

x = input("enter the greeting:-")

match x:
    case "good morning":
        print("very good morning\nradhe radhe")
    case "good afternoon":
        print("very good afternoon\nradhe radhe")
    case "good night":
        print("very good night\nradhe radhe")
    case _:
        print("invalid greeting")
