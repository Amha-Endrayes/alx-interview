#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
                code> <file size>
"""
import sys
stcd = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}
total = 0


def print_stats():
    """
    Function that print stats about log
    """
    global total

    print('File size: {}'.format(total))
    stcdor = sorted(stcd.keys())
    for each in stcdor:
        if stcd[each] > 0:
            print('{}: {}'.format(each, stcd[each]))


if __name__ == "__main__":
    count = 0
    try:
        """ Iter the standar input """
        for data in sys.stdin:
            try:
                fact = data.split(' ')
                """ If there is a status code """
                if fact[-2] in stcd:
                    stcd[fact[-2]] += 1
                """ If there is a lenght """
                total += int(fact[-1])
            except:
                pass
            """ Printing control """
            count += 1
            if count == 10:
                print_stats()
                count = 0
    except KeyboardInterrupt:
        print_stats()
        raise
    else:
        print_stats()
