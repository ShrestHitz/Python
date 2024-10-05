def main():
    sentence = input("Write a Sentence: ")
    print(sentence)
    sentence = convert(sentence)
    print(sentence)

def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence
main()