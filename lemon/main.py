import sys
from lemon.lemon_name import print_lemon_name
from lemon.lemon_cost import print_lemon_cost as plc

def main():
    print_lemon_name(-1)
    print_lemon_name(5)
    print_lemon_name(20)
    print_lemon_name(100)

    plc(-1)
    plc(5)
    plc(20)
    plc(100)

    args = sys.argv[1:]
    # print(args)
    for i in range(len(args)):
        print(f"args[{i}]:{args[i]}")
        print_lemon_name(int(args[i]))
        plc(int(args[0]))


if __name__ == "__main__":
    main()