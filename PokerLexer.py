# Generated from Poker.g by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\t")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\6\7G\n\7\r\7\16\7H\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\3\2\3\3\2\62;L\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\3\21\3\2\2\2\59\3\2\2\2\7?\3\2\2\2\tA\3\2\2\2")
        buf.write("\13C\3\2\2\2\rF\3\2\2\2\17J\3\2\2\2\21\22\78\2\2\22\23")
        buf.write("\7\60\2\2\23\24\7U\2\2\24\25\7;\2\2\25\26\7\63\2\2\26")
        buf.write("\27\7\64\2\2\27\30\7\"\2\2\30\31\7O\2\2\31\32\7K\2\2\32")
        buf.write("\33\7V\2\2\33\34\7\"\2\2\34\35\7R\2\2\35\36\7q\2\2\36")
        buf.write("\37\7m\2\2\37 \7g\2\2 !\7t\2\2!\"\7d\2\2\"#\7q\2\2#$\7")
        buf.write("v\2\2$%\7u\2\2%&\7\"\2\2&\'\7/\2\2\'(\7\"\2\2()\7R\2\2")
        buf.write(")*\7\63\2\2*+\7\"\2\2+,\7x\2\2,-\7u\2\2-.\7\"\2\2./\7")
        buf.write("R\2\2/\60\7\64\2\2\60\61\7\"\2\2\61\62\7*\2\2\62\63\7")
        buf.write("u\2\2\63\64\7v\2\2\64\65\7c\2\2\65\66\7e\2\2\66\67\7m")
        buf.write("\2\2\678\7?\2\28\4\3\2\2\29:\7.\2\2:;\7\"\2\2;<\7d\2\2")
        buf.write("<=\7d\2\2=>\7?\2\2>\6\3\2\2\2?@\7+\2\2@\b\3\2\2\2AB\5")
        buf.write("\r\7\2B\n\3\2\2\2CD\5\r\7\2D\f\3\2\2\2EG\5\17\b\2FE\3")
        buf.write("\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\16\3\2\2\2JK\t\2")
        buf.write("\2\2K\20\3\2\2\2\4\2H\2")
        return buf.getvalue()


class PokerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    STACK = 4
    BB = 5
    DIGITS = 6
    DIGIT = 7

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'6.S912 MIT Pokerbots - P1 vs P2 (stack='", "', bb='", "')'" ]

    symbolicNames = [ "<INVALID>",
            "STACK", "BB", "DIGITS", "DIGIT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "STACK", "BB", "DIGITS", "DIGIT" ]

    grammarFileName = "Poker.g"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


