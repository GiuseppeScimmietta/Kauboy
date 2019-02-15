import traceback
import ast

def clearStamp(codeTxt):
  return print(codeTxt)


#Visit AST nodes----------------------------------------

# class Transformer(ast.NodeTransformer):
#   def visit_FunctionDef(self, node):
#     return node
#
#   def visit_Name(self, node):
#     # if node.id in kwargs and not isinstance(node.ctx, ast.Store):
#     #   replacement = kwargs[node.id]
#     #   if isinstance(replacement, int):
#     #     return ast.copy_location(ast.Num(n=replacement), node)
#     #   else:
#     #     return copy.copy(replacement)
#     # else:
#     #   return node
#     print("Visitor_Begin----------------------------------------")
#     print(node)
#     print("Visitor_End----------------------------------------")
#
#
# Transformer().visit(pyAst)



#---Open Kauboy source file--------------------------------------
kauboyCode = open('test.py').read()
#kauboyCode = open('fake.py').read()

#---Lex and tokenize---------------------------------------------


#---Lint---------------------------------------------------------
# ...Kauboy specific syntax check

#---Transform Kauboy statements----------------------------------
# ...into function calls

#---Parse into AST-----------------------------------------------

#Open and parse code to AST--------------------------------------
print(kauboyCode)
pyAst = ast.parse(kauboyCode)

#Print AST nodes----------------------------------------
#print(ast.dump(pyAst))
#print("---")
#print (pyAst.body[1].body[1])
#print (pyAst.body[0].lineno)
#print("---")


#---Manipulate AST-----------------------------------------------

# Insert
#astInsert = ast.parse("print('Inserted')")
#print (ast.dump(astInsert))
#pyAst.body.insert(1, astInsert.body)
#pyAst.body[1].lineno = pyAst.body[0].lineno

# pyAst.body[1].body[1].lineno = pyAst.body[0].body[0].lineno
# ast.increment_lineno(pyAst.body[1].body[1], n=-1)
# print(ast.dump(pyAst, include_attributes = True))

#---Compile code AST into Code-----------------------------------
pyCode = compile(pyAst, filename="test.py", mode="exec")

#---Execute-------------------------------------
try:
  exec(pyCode)
except Exception as err:
  traceback.print_exc(limit=-1)




    
