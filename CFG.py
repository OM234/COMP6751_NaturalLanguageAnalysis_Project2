import nltk


# This class is used to parse sentences
class CFGParser:

    def __init__(self):
        self.parser = nltk.EarleyChartParser(buildCFG())  # parser used
        self.tokens = None

    def print_trees(self, tokens):
        self.tokens = tokens
        printParsedTrees(self.parser, self.tokens)


# we build the representation of our CFG
def buildCFG():
    stringCFG = (

            "S -> NP VP PONCT\n" +
            "NP -> PRO | PPN | DET NOM\n" +
            "VP -> VERB | VERB NP | VERB NP PP | VERB PP\n" +
            "PP -> PREP NP\n" +
            "NOM -> NOUN\n" +
            "VERB -> 'ate'\n" +
            "PPN -> 'john' | 'mary'\n" +
            "DET -> 'the' | 'an'\n" +
            "NOUN -> 'apple'\n" +
            "PONCT -> '.'"

        # "DATE -> YEAR SEP MONTHDIG SEP DAYDIG\n" +  # 1990/01/30
        #
        # "DATE -> DAYDIG SEP MONTHDIG SEP YEAR\n" +  # 03/01/1990
        #
        # "DATE -> FULLYEAR\n" +  # 2050
        #
        # "DATE -> MONTH DAY\n" +  # february 5th
        #
        # "DATE -> MONTH\n" +  # june
        #
        # "DATE -> ORDINAL OF MONTH\n"  # second of may
        #
        # "DATE -> DAY OF MONTH\n"  # 9th of january
        #
        # "DATE -> ORDINAL OF MONTH\n"  # fourth of january
        #
        # "MONTH -> 'january' | 'february' | 'march' | 'april' | 'may' | 'june' | 'july' | 'august' | "
        # "'september' | 'october' | 'november' | 'december'\n" +
        #
        # "MONTHDIG -> '01' | '02' | '03' | '04' | '05' | '06' | '07' | '08' | '09' | '10' | '11' | '12'\n" +
        #
        # "ORDINAL -> SMALLORDINAL | LARGEORDINAL SMALLORDINAL\n"  # first, twenty-third (dashes removed in tokenizer)
        #
        # "SMALLORDINAL -> 'first' | 'second' | 'third' | 'fourth' | 'fifth' | 'sixth' | 'seventh' | 'eighth' | "
        # "'ninth' | 'tenth' | 'eleventh' | 'twelfth' | 'thirteenth' | 'fourteenth' | 'fifteenth' | 'sixteenth' | "
        # "'seventeenth' | 'eighteenth' | 'nineteenth'\n" +
        #
        # "LARGEORDINAL -> 'twenty' | 'twentieth' | 'thirty' | 'thirtieth' \n"
        #
        # "SEP -> '/'\n" +
        #
        # "OF -> 'of'\n"
    )

    return nltk.CFG.fromstring(stringCFG)


# if there are any trees found, print them
def printParsedTrees(parser, tokens):
    for tree in parser.parse(tokens):
        print(tree)
