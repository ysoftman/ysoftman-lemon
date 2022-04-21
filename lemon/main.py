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


if __name__ == "__main__":
    main()