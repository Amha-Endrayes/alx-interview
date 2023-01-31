# 0x01-lockboxes

# Box Unlocker
A Python 3 script that determines if all boxes can be unlocked.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
```
Python 3
```

## Function Signature

python
```
def can_unlock_all(boxes: List[List[int]]) -> bool:
```

## Installation and Usage
* Clone or download the repository to your local machine.
* Excute the script as follows:
```
root@root: python3 box_unlocker.py
```

## Arguments
@boxes: A list of lists where each sublist represents a box and contains keys to other boxes. A key with the same number as a box opens that box.

Returns:
A boolean value indicating if all boxes can be unlocked.

Examples:

```
>>> can_unlock_all([[1], [0, 2], [3]])
True

>>> can_unlock_all([[1, 3], [0, 2], [1]])
False
```
