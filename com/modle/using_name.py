__author__ = 'renfei'
print(__name__)

def moduleName():
    print(__name__)
    if __name__ == "__main__":
        print("This program is being run by itself")
    else:
        print("I am being imported form another module")

moduleName()
