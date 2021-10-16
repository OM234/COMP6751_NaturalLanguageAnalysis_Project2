import nltk


# Pipeline used to preprocess and print relevant values



class Pipeline:
    def __init__(self, parser, text):
        self.text = text
        self.parser = parser
        self.tokens = None
        self.number_parser = None
        self.sentences = None
        self.pos_tags = None
        self.date_parser = None

    def preprocess(self):
        print_preprocessing(self.text)  # print current text
        self.tokens = tokenize(self.text)
        self.sentences = split_sentences(self.text)
        self.pos_tags = pos_tagging(self.tokens)

    def print_tokens(self):
        print_tokens(self.tokens)

    def print_sentences(self):
        print_sentences(self.sentences)

    def print_pos_tags(self):
        print_pos_tags(self.pos_tags)

    def print_trees(self):
        print_trees(self.parser, self.tokens)


# print file id
def print_preprocessing(text):
    print("\n\n\n\n\npreprocessing: ***{}***\n".format(text))


def tokenize(raw_text):
    tokens = nltk.word_tokenize(raw_text)  # use nltk to tokenize
    tokenizeToLowerCase(tokens)  # convert tokens to lower case
    return tokens


def tokenizeToLowerCase(tokens):
    for i in range(0, len(tokens)):
        lower_case_token = tokens[i].lower()
        tokens[i] = lower_case_token


# nltk is used to tokenize sentences
def split_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences


# nltk is used to tokenize POS tags
def pos_tagging(tokens):
    pos_tags = nltk.pos_tag(tokens)
    return pos_tags


def print_tokens(tokens):
    print("********** tokens **********")
    for i in range(len(tokens)):
        if i % 10 == 9:
            print('|')
        print('|', tokens[i], end=' ')


def print_sentences(sentences):
    print("\n\n********** sentences **********")
    for i in range(0, len(sentences)):
        print('{}) {}'.format(i + 1, sentences[i]))


def print_pos_tags(pos_tags):
    print("\n********** POS tags **********")
    for i in range(len(pos_tags)):
        if i % 6 == 5:
            print()
        print(pos_tags[i], end=' ')


def print_trees(parser, tokens):
    parser.print_trees(tokens)