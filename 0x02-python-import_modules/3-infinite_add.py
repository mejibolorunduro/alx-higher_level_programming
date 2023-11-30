#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        q = 1
        add = 0
        while q <= n:
            add += int(argv[q])
            q += 1
            print("{:d}".format(add))


            if __name__ == "__main__":
                import sys
                add_arg(sys.argv)
