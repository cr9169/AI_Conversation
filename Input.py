import enchant

dict = enchant.Dict("en_US")


def check_if_string_word(string, dictionary):
    return dictionary.check(string)


def check_if_sentence_valid(sentence):
    remove_spaces_from_sentence_input(sentence)
    for word in sentence.split():
        if not check_if_string_word(word, dict):
            return False
    return True


def remove_spaces_from_sentence_input(sentence):
    sentence.strip()
    sentence = " ".join(sentence.split())
    return sentence
