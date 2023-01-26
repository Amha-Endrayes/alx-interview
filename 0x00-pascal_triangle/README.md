# 0x00-pascal_triangle

## Technical Interview Preparation

### Description:
A python module that returns a list of lists of integers representing a Pascal’s Triangle of
size n.

* Takes only integer arguments
* Returns an empty list if n <= 0

### Usage:
- Import the module in your application:

```
root@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

- Have fun drawing Pascal's Triangel!

```
root@ubuntu:~/0x00$ 

root@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]

root@ubuntu:~/0x00$ 
```
