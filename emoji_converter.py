emoji_dictionary = {
    ":)":"😊",
    ":(":"😞",
    ";)":"😉"
}

message = input("Message: ")
words = message.split(" ")
message_out = ""
for word in words:
    message_out += emoji_dictionary.get(word, word) + ' '
print(message_out)
