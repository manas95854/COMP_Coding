str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")

if sorted(str1) == sorted(str2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")