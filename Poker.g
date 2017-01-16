grammar Poker;

header : '6.S912 MIT Pokerbots - P1 vs P2 (stack=' STACK ', bb=' BB ')';
STACK : DIGITS;
BB : DIGITS;

DIGITS : [0-9]+;
