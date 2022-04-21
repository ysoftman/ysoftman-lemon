def print_lemon_name(a: int):
    if a<0:
        print("bad lemon")
    elif a<10:
        print("normal lemon")
    elif a<100:
        print("high lemon")
    else:
        print("GOD lemon")


if __name__ == "__main__":
    print_lemon_name(-1)
    print_lemon_name(5)
    print_lemon_name(20)
    print_lemon_name(100)
