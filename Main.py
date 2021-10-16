from Pipeline import Pipeline
from CFG import CFGParser


def main():

    sentences_file = open('sentences.txt')
    file_contents = sentences_file.read()
    sentences = file_contents.splitlines()

    parser = CFGParser()

    for sentence in sentences:
        pipeline = Pipeline(parser, sentence)  # create pipeline
        pipeline.preprocess()  # preprocess text
        pipeline.print_trees()
        # pipeline.print_tokens()  # print values from pipeline
        # pipeline.print_sentences()
        # pipeline.print_pos_tags()


if __name__ == "__main__":
    main()
