import re

def is_palindrome(phrase):
    string1 = ''.join(re.findall(r'[a-z]', phrase.lower()))
    #print(string1)
    def backwards(string1):
        return string1[::-1]
    #print(backwards(string1))
    if string1 == backwards(string1):
        return True
    else:
        return False

# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome("A roza upala na lapu Azora"))
    print(is_palindrome('te .  n, e t'))
