"""
Main entry point.
"""
import sys
from new_parser import Parser
from lexer import Lexer
from string import ascii_lowercase


class ParserInit:

    def __init__(self,
                 parsing_table_filename: str = "parsing_table.csv",
                 grammar_table_filename: str = "grammar_table.csv"):
        """

        :param parsing_table_filename:
        :param grammar_table_filename:
        """
        self.parsing_table = parsing_table_filename
        self.grammar_table = grammar_table_filename

    def read_file_as_string(self, filename):
        """
        Reads the provided file as a string.
        @param filename: Name of the file to read.
        @return: A string of the files contents.
        """
        with open(filename, 'r') as file_pointer:
            return file_pointer.read()

    def choose_parsing_table(self, parsing_table_filename: str = "parsing_table.csv"):
        self.parsing_table = parsing_table_filename

    def choose_grammar_table(self, grammar_table_filename: str = "grammar_table.csv"):
        self.grammar_table = grammar_table_filename


initializer = ParserInit()

# Ensure the right amount of arguments are provided.
if len(sys.argv) != 2:
    print("python3 main.py [sourceCode.*]")
    exit(0)

# Extract file names from the program arguments.
source_code_filename = sys.argv[1]

source_code = initializer.read_file_as_string(source_code_filename)

# Manually build the scanning table and token table.
lexical_table = {}

# Le'finite status machinem.
for c in ascii_lowercase:
    lexical_table[(0, c)] = 1
    lexical_table[(1, c)] = 1

lexical_table[(0, '=')] = 3
lexical_table[(0, '+')] = 2
lexical_table[(0, ' ')] = 4
lexical_table[(0, '\n')] = 4
lexical_table[(0, '\r')] = 4
lexical_table[(0, '\t')] = 4
lexical_table[(4, ' ')] = 4
lexical_table[(4, '\n')] = 4
lexical_table[(4, '\r')] = 4
lexical_table[(4, '\t')] = 4

# Table for token classes at accepting states.
token_table = {1: "id",
               2: "+",
               3: "=",
               4: "whitespace"
               }

# Construct the lexer from the parsed file outputs from the parser.
lexer = Lexer(lexical_table, token_table, source_code)
# Perform the lexical analysis.
token_stream = lexer.perform_analysis()

parsing_table_filename = "parsing_table.csv"
grammar_table_filename = "grammar_table.csv"

# Perform the parse.
parser = Parser(token_stream, parsing_table_filename, grammar_table_filename)
parser.parse()

if __name__ == "__main__":
    pass
