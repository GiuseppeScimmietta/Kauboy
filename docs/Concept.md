Concept Sandbox
=================

PreLexing
--------------------------

Purpose of prelexinf is to find kauboy specific keywords (statements) within the source code an generate list of lexing tokens

(STATEMENT, value, lineNo, charNo)

e.g.
(EXPECT_STM, "expect", 10, 2)

Given a Labelled BNF grammar the tool produces:
- an abstract syntax implementation
- a case skeleton for the abstract syntax in the same language
- an Alex, JLex, or Flex lexer generator file
- a Happy, CUP, or Bison parser generator file
- a pretty-printer as a Haskell/Java/C++/C module
- a Latex file containing a readable specification of the language

*More information*: [haskell platform](https://www.haskell.org/platform/)
