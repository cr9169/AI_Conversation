import enchant

dictionary = enchant.Dict("en_US")


def check_if_string_word(string, d):
    return d.check(string)


def check_if_sentence_valid(sentence):
    """
    :param sentence: string.
    :return: boolean (valid or not).
    """
    remove_spaces_from_sentence_input(sentence)
    for word in sentence.split():
        if not check_if_string_word(word, dictionary):
            return False
    return True


def remove_spaces_from_sentence_input(sentence):
    """
    Ex: (" wds fsd        st          teryterre yt yty  er") =>
    ("wds fsd st teryterre yt yty er")

    :param sentence: string
    :return: string (sentence)
    """

    sentence.strip()
    sentence = " ".join(sentence.split())
    return sentence


def main():
    print("hi")


if __name__ == '__main__':
    main()
