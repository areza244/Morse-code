from re import I
import sys

morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  '$': ' ', ' ': '$'
        }

translate = []
text = []
t = []
cond = True

while True:
    try:
        selection = int(input("Enter '1' for Text to Morse, '2' for Morse to Text: "))
    except ValueError:
        print("Sorry, wrong input!")
        continue
    if selection == 2:
        break
    if selection == 1:
        break
    if selection != 1 and selection != 2:
        print("Sorry, wrong input!")
        continue

def remove_space(string):
    return "".join(string.split())

if selection == 1:
    input = input("Enter the sentence (for space enter $): ")
    input_list = list(input)
    for i in input_list:
        if i in morse:
            translate.append(morse.get(i))
        else:
            print('Error: Character not found')
            sys.exit()
    result =' '.join(map(str, translate))

    print(result)

if selection == 2:
    input = input(str("Enter the morse code with space between letters and end the input with double space: "))
    input_list = list(input)
    for i in input_list:
        if i == ' ':
            input_list[input_list.index(i)] = '/'
    if input_list[-2] == '/':
        for m in input_list:
            if cond == True:
                if m != '/':
                    text.append(m)
                elif m == '/':
                    if text == []:
                        temp =' '.join(map(str, translate))
                        t.append(remove_space(temp))
                        translate = []
                    elif text != []:
                        temp_str =' '.join(map(str, text))
                        temp_str_nospace = remove_space(temp_str)
                        for key, value in morse.items():
                            cond = False
                            if value == temp_str_nospace:
                                cond = True
                                translate.append(key)
                                text = []
                                break   
            elif cond == False:
                print('Error: Character not found!')
                sys.exit()        
    elif input_list[-2] != '/':
        print('Error: the input needs to end with double space!')
        sys.exit()

    result =' '.join(map(str, t)) 

    print("Result: " + result)


