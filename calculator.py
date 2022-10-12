
while True:
    breaker = input(
        "Do you wish to terminate this process? input 'yes' or 'no': ").lower()
    if breaker == "yes":
        break

    f_num = float(input("What's your first number? "))
    operation = input("""*
    /
    +
    -
    Pick an operation: 
    """)
    s_num = float(input("What's the second number? "))

    def calculation():
        """This function returns the calculation between two numbers based
        on the operation given"""
        global answer
        if operation == "*":
            answer = f_num * s_num
        elif operation == "/":
            answer = f_num / s_num
        elif operation == "+":
            answer = f_num + s_num
        elif operation == "-":
            answer = f_num - s_num

        return answer

    print(calculation())

    user_res = ""
    
    while True:
        user_res = input(
            f"Do you want to continue with {answer} or you want to start another calculation? type 'yes' or 'no': ").lower()
        if user_res == "no":
            break

        f_num = answer

        operation = input("""*
        /
        +
        -
        Pick an operation: 
        """)
        s_num = float(input("What's the second number? "))
        print(calculation())
