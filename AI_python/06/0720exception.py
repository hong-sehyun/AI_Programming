class SHException(Exception):
    def __init__(self) :
        super().__init__("sh's exception")


def main():
    try:
        print("hello")
        raise SHException
    except SHException as e:
        print(e)


main()
