# Emoji Convertor
"""
Created on Fri Mar  8 11:25:47 2024

@author: Imran Nawar
"""
message = input('>')
words = message.split(' ')

emojis = {
    ':)': '😁',
    ':(': '😞'
}

output = ''
for word in words:
    output += emojis.get(word, word) + ' '
    
print(output)