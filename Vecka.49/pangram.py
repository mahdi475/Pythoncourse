amount_test = 0
def is_pangram(text):
    a_z = "abcdefghijklmnopqrstuvwxyz"
    
    text_konvert = text.lower()

    for i in a_z:
        print(i)
        
        if i not in text_konvert:
            return False

    return True

input_text = "The quick brown fox jumps over the lazy dog."

if is_pangram(input_text): 
    print('The text is a pangram.')  
else:
    print('The text is not a pangram.') 