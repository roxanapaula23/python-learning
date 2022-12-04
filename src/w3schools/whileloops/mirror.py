
def is_mirror_word(word: str):
    
    length = len(word)
    last_index = int(length) - 1
    for i in range(int(length/2)):
        print("Front letter: " + word[i] + " Mirror letter: " + word[last_index - i])
        if(word[i] != word[last_index - i]):
            print("False")

is_mirror_word("nooon")



