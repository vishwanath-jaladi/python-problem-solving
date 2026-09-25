# Program: Count Vowels
# Description: Takes a string and attempts to count the vowels
# present in the text.
text=input("Enter text:")
def count_vowels(text):
    count=0
    for character in text:
        if character is ("a" or "e" or "i" or "o" or "u"):
            count+=1
    return count
output=count_vowels(text)
print("Output:",output)
