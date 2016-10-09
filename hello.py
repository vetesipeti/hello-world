import sys

def command_counter():
    lenght = len(sys.argv)
    return lenght

def Hello():
    """ Greets the User """
    return ("Hello " + sys.argv[1] + "!")

if command_counter() > 1:
    print(Hello())
else:
    print("Hello World!")

