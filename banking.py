import string

def is_palindrome(s):
    translator = str.maketrans('', '', string.punctuation)
    s = s.translate(translator).replace(" ", "").lower()
    return s == s[::-1]

# Example usage:
input_string = "A man, a plan, a canal, Panama"
print(f"Is the string a palindrome? {is_palindrome(input_string)}")


