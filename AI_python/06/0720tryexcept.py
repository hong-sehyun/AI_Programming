def func1():
    try:
        print('func1')
    except AttributeError as e:
        print(e)

def func2():
    try:
        print('func2')
        func1()

    except ZeroDivisionError as e:
        print(e)


def main():
    try:
        # func1()
        func2()

    except AttributeError as e:
        print(e)

main()
