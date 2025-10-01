import sys

# 패키지명은 문자(a-z, A-Z), 숫자(0-9), 밑줄(_)만 가능
from ysoftman_lemon.lemon_cost import print_lemon_cost as plc
from ysoftman_lemon.lemon_name import print_lemon_name


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
