def isPalindrome(string: str, n: int):
    if n <= 1:
        return True

    if(string[0] == string[n - 1]):
        return isPalindrome(string[1:n-1], n - 2)
    else:
        return False


if __name__ == "__main__":
    string = "civic"
    print(isPalindrome(string, 5))
