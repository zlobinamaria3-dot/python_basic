import string
user_text = input("Enter your text for hashtag: ")
_text = user_text.title()
hashtag = "".join(char for char in user_text if char not in string.punctuation and char != " ")
result = f"#{_text}" [:140]
print(result)