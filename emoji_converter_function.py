def emoji_converter(message):
    emoji_dictionary = {
        ":)": "😊",
        ":(": "😞",
        ";)": "😉"
    }
    words = message.split(" ")
    message_out = ""
    for word in words:
        message_out += emoji_dictionary.get(word, word) + ' '
    return message_out

message = input("> ")
output = emoji_converter(message)
print(output)