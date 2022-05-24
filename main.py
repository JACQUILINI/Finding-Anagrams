# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


#Accept string input form user
string1 = input("Enter First Word: ")
string2 = input("Enter Second Word: ")

#fomat inputs
string1uppercase = string1.upper()
string2uppercase = string2.upper()

#create anagram funtion 
def find_anagrams(word1, word2):
    # [assignment] Add your code here
    x = sorted(word1)==sorted(word2)
    return x

#call anagram funtion and print return value
print(find_anagrams(string1uppercase, string2uppercase))

