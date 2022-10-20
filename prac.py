import sys

def calling_some_api():
    print("inside calling_some_api ")
    raise Exception("prem chand")


def my_func():
    calling_some_api()
    return


if __name__ == "__main__":
    my_func()
