import sys
import argparse
def  _create_parser():
    parser=argparse.ArgumentParser()
    parser.add_argument(
            '--name',
            default='qianyuqiao',
            help='My name!')

    parser.add_argument(
            '--age',
            type = int,
            default= 22,
            help='My name!')

    parser.add_argument(
            '--school',
            default='XJTU',
            help='My school'
            )
    return parser 


def main():
    
    parser = _create_parser()
    options, unparsed = parser.parse_known_args()
    print 'options: ', str(options) , ' unparsed: ', str(unparsed)

if __name__ == '__main__':
    main()

