# Chap1_8. Given 2 strings: s1 and s2, write code to check if s2 is rotation of
# s1 using only one call to isSubstring.


def main():
    s1 = "waterbottle"
    s2 = "erbottlewat"

     # Why you giving me a hard time
    print isRotation(s1, s2)


def isRotation(s1, s2):
    """This is for purpose only"""
    if len(s1) == len(s2) and s1.isSubstring(s2+s2):
        return True

if __name__ == "__main__":
    main()
