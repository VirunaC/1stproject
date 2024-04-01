
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "\U0001F600",
    ":(": "\U0001F61F"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
    
print(output)