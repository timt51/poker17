# Generated from Poker.g by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\t")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\t")
        buf.write("\2\4\3\2\2\2\4\5\7\3\2\2\5\6\7\6\2\2\6\7\7\4\2\2\7\b\7")
        buf.write("\7\2\2\b\t\7\5\2\2\t\3\3\2\2\2\2")
        return buf.getvalue()


class PokerParser ( Parser ):

    grammarFileName = "Poker.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'6.S912 MIT Pokerbots - P1 vs P2 (stack='", 
                     "', bb='", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STACK", "BB", "DIGITS", "DIGIT" ]

    RULE_header = 0

    ruleNames =  [ "header" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    STACK=4
    BB=5
    DIGITS=6
    DIGIT=7

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class HeaderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STACK(self):
            return self.getToken(PokerParser.STACK, 0)

        def BB(self):
            return self.getToken(PokerParser.BB, 0)

        def getRuleIndex(self):
            return PokerParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)




    def header(self):

        localctx = PokerParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(PokerParser.T__0)
            self.state = 3
            self.match(PokerParser.STACK)
            self.state = 4
            self.match(PokerParser.T__1)
            self.state = 5
            self.match(PokerParser.BB)
            self.state = 6
            self.match(PokerParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





