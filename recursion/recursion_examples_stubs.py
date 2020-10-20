"""
PROGRAM:........... recursion examples
AUTHOR:............ <LastName>, <FirstName>
"""

def factorial_iterative(n):
    """
    Compute and return n! n factorial)
    """
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


def factorial(n):
    """
    Compute and return n! n factorial)
    """
    pass


def is_palindrome_iterative(s):
    """
    Returns True if s is a palindrome, False otherwise
    """
    first = 0
    last = len(s) - 1
    while last >= first:
        if s[first] != s[last]:
            return False
        first += 1
        last -= 1
    return True


def is_palindrome(s):
    """
    Returns True if s is a palindrome, False otherwise
    """
    pass


def binary_search_iterative(target, a_list):
    """
    perform an iterative binary search
    :param target: the target to look for
    :param a_list: the list to search
    :return: True if target is in a_list, False otherwise
    """
    found = False
    first = 0
    last = len(a_list) - 1

    while first <= last and not found:
        mid = (first + last) // 2
        if target < a_list[mid]:
            last = mid - 1
        elif target > a_list[mid]:
            first = mid + 1
        else:
            return True

    return False


def binary_search(target, a_list):
    """
    perform a recursive binary search
    :param target: the target to look for
    :param a_list: the list to search
    :return: True if target is in a_list, False otherwise
    """
    pass


def power(n, p):
    """
    compute and return n^p
    """
    pass


def list_sum(a_list):
    """
    Returns the sum of all the numbers in a_list
    """
    pass


def length(a_list):
    """
    Returns the number of items in, i.e. length of, a_list
    """
    pass


def reverse(s):
    """
    Returns the reverse of string s
    """
    pass


def find_max(a_list):
    """
    find and return the largest item in a list
    """
    pass


def contains(target, a_list):
    """
    Returns True if a_list contains target, False otherwise
    """
    pass


def count(a_list, a_value):
    """
    Return count of how many times a_value appears in a_list
    """
    pass


def range_list(num):
    """
    Returns a list containing values 0..num, both inclusive
    Examples:
        range_list(10) returns [0,1,2,3,4,5,6,7,8,9,10]
        range_list(5) returns [0,1,2,3,4,5]
    """
    pass


def deep_sum(a_list):
    """
    Returns sum of items in a_list even if a_list contains lists which contain
    other lists which contain other lists....
    Examples:
        deep_sum([1,2,[3,4,[5,6,7]],8]) returns 36
        deep_sum([1,2,[3,4],5]) returns 15
        deep_sum([1,2,3,4]) returns 10
    """
    pass


def equals(s1, s2):
    """
    Returns True if strings s1 and s2 contain exactly the same characters in the same order, False otherwise
    """
    pass


def prefix(s1, s2):
    """
    Returns true if s2 is a prefix for s1, i.e. s1 starts with s2, False otherwise
    Examples:
        prefix("apple", "app") returns True
        prefix("python", "py") returns True
        prefix("python", "pytx") returns False 
    """
    pass


def substring(s1, s2):
    """
    Returns True if string s1 contains string s2, False otherwise
    Examples:
        substring("photograph", "photo") returns True
        substring("photograph", "graph") returns True
        substring("photographer", "graph") returns True
        substring("photograph", "hot") returns True
        substring("photograph", "gruph") returns False
    """
    pass
