def foo():
    print("Hello")
print("Hello 2")
print("Hello 3")
x = 5
def bar():
    print("bar")
foo()
print("We do not want to do this!!!")

def main():
    foo()
if __name__ == "__main__":
    main()
    
import functions
functions.add5(x)
