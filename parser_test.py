from antlr4 import *
from PokerLexer import PokerLexer
from PokerListener import PokerListener
from PokerParser import PokerParser
import sys

class PokerPrintListener(PokerListener):
    def enterStack(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    txt = "6.S912 MIT Pokerbots - P1 vs P2 (stack=200, bb=2)"
    lexer = PokerLexer(InputStream(txt))
    stream = CommonTokenStream(lexer)
    parser = PokerParser(stream)
    tree = parser.header()
    printer = PokerPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()