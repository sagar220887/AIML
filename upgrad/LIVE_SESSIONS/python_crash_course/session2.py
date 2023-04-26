

while True:
    try:
        number = int(input("Enter the age"))
        print(f'This is a test message {(number/10) + 2}')

    except Exception as e:
        print(e)
        print("Only numbers are allowed")

    finally:
        print("Next iteration")