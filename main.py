def decode_morse_code(morse_code):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
        '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'
    }
    decoded_message = ''
    morse_words = morse_code.split(' ')
    for word in morse_words:
        if word == '':
            decoded_message += ' '
        elif word in morse_dict:
            decoded_message += morse_dict[word]
        else:
            decoded_message += '?'
    return decoded_message

morse_input = input("Enter Morse code (use '-' for dots and '.' for dashes): ")
decoded_message = decode_morse_code(morse_input)
print("Decoded message:", decoded_message)
