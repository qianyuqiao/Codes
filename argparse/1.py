import argparse
def main():
    parser= argparse.ArgumentParser()
    parser.add_argument('--name',
            metavar='NAME',
            help='name')
    parser.add_argument('--height',
            type=int,
            help='height of me')

    data=parser.parse_args()
    print data

if __name__ == '__main__':
    main()

