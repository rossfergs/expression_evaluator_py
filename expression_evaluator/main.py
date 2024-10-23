from interpreter import interpret


def main():
    while True:
        user_input = input(">>> ")
        if user_input == "exit":
            exit(0)
        result = interpret(user_input)
        print(f"     = {result}")


main()
