import string
user_text = input("Enter your text for hashtag: ")
hash_text = user_text.title()
_text = "".join(char for char in hash_text if char not in string.punctuation and char != " ")
result = f"#{_text}" [:140]
print(result)