# Task 1: Morse Code Decoder

def morse_code_decoder(morse_code):
    morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                  '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                  '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                  '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                  '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                  '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
                  '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
                  '----.': '9'}

    words = morse_code.split('   ')  
    decoded_message = ''

    for word in words:
        letters = word.split(' ')  # Split each word into letters
        for letter in letters:
            # Get the corresponding letter from the dictionary
            decoded_message += morse_dict.get(letter, '')  
        decoded_message += ' ' 
    
    # Remove trailing whitespace
    decoded_message = decoded_message.strip()  
    return decoded_message


morse_code = '.- -   -.. .- .-- -.   .-.. --- --- -.-   - ---   - .... .   . .- ... -'
decoded_message = morse_code_decoder(morse_code)
print(decoded_message)


# Task 2: Sentence Encoder

def encode_sentence(sentence):
    words = sentence.split()
    encoded_words = []

    for word in words:
        if len(word) > 3:
            # Reverse the word if its length exceeds 3
            encoded_words.append(word[::-1])  
        else:
            encoded_words.append(word)

    encoded_sentence = ' '.join(encoded_words)
    return encoded_sentence

input_sentence = "AT DAWN LOOK TO THE EAST"
encoded_result = encode_sentence(input_sentence)
print(encoded_result)