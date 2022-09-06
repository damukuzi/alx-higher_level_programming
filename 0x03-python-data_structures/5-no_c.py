#!/usr/bin/python3
def no_c(my_string):
    copy_str = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            copy_str += i
    return (copy_str)
