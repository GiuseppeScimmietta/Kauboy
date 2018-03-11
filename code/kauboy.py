import ast

def clearStamp(codeTxt):
  
  return print(codeTxt)


#------------------------------------------------

codeTxt = open('test.py').read()

clearStamp(codeTxt)

astCode = ast.parse(codeTxt)
print(ast.dump(astCode))
print("---")
print (astCode.body[0])
print (astCode.body[0].lineno)
print("---")

# Insert
#astInsert = ast.parse("print('Inserted')") 
#print (ast.dump(astInsert))
#astCode.body.insert(1, astInsert.body)
#astCode.body[1].lineno = astCode.body[0].lineno

astCode.body[0].body[1].lineno = astCode.body[0].body[0].lineno
ast.increment_lineno(astCode.body[0].body[1], n=-1)


print(ast.dump(astCode, include_attributes = True))

exec(compile(astCode, filename="tes.py", mode="exec"))



    
