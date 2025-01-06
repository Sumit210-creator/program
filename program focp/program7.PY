def unique_letters(s):
    return sorted(set(c for c in s if c.isalpha()))

print(unique_letters("cheese")) 


def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))


def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))


def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))


print(letters_in_either("cheese", "apple"))  
print(letters_in_both("cheese", "apple"))   
print(letters_in_either_but_not_both("cheese", "apple"))  
