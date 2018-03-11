Concept sandbox
=================

[Lexing, Parsing and Inerpreting the code](http://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1)
A simple interpreter from scratch in Python (part 1)


Lexing
--------------------------

Purpose of Lexing is to find kauboy-specific keywords (statements) inside the source code and generate list of lexing tokens as follows:

(STATEMENT, value, lineNo, charNo)

e.g.
(EXPECT_STM, "expect", 10, 2)


#### PLY module
[Documentation](http://www.dabeaz.com/ply/ply.html#ply_nn36)

External references:
- Introduction:  [Writing Parsers and Compilers with PLY](http://www.dabeaz.com/ply/PLYTalk.pdf)
- ZLexer: [example of Python code PLY based lexer](https://github.com/woshifyz/zlang/blob/master/zlexer.py)

Normalizing code
--------------------------
ToDo

In-placing
--------------------------
includes following steps

- conversion of normalized code to AST tree
- place-in the code performing the function of individual kauboy-statements

#### AST module
[Documentation](https://docs.python.org/3/library/ast.html)

External references:
- use example:  [Testing Code Submissions With Python AST](https://www.codeschool.com/blog/2016/03/23/testing-code-submissions-with-python-ast/)
- ZLexer: [example of Python code PLY based lexer](https://github.com/woshifyz/zlang/blob/master/zlexer.py)


Compile and Execute
--------------------------
- compilation of modified (kauboy-enriched) AST tree
- execution of the compiled code

External references:

- compile & run example:  [Getting to and from ASTs](http://greentreesnakes.readthedocs.io/en/latest/tofrom.html)
