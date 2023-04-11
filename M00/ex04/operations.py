from curses.ascii import isdigit
import sys

def main():
    assert len(sys.argv) == 3, "Too many arguments"
    assert sys.argv[1].isdigit() and sys.argv[2].isdigit(), "only integers"
    print('Sum:', int(sys.argv[1]) + int(sys.argv[2]))
    print('Difference:', int(sys.argv[1]) - int(sys.argv[2]))
    print('Product:', int(sys.argv[1]) * int(sys.argv[2]))
    if int(sys.argv[2]) != 0:
        print('Qutient:', int(sys.argv[1]) / int(sys.argv[2]))
        print('Reminder:', int(sys.argv[1]) % int(sys.argv[2]))
    else:
        print('Qutient:', 'ERROR (division by zero)')
        print('Reminder:', "ERROR (modulo by zero)")

if __name__ == "__main__":
    main()