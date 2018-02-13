import ast

astCode = ast.parse(open('test.py').read())
print(ast.dump(astCode))
print("---")
print (astCode.body[0])
print (astCode.body[0].lineno)
print("---")

astInsert = ast.parse("print('Inserted')") 
print (ast.dump(astInsert))

#astCode.body.insert(1, astInsert.body)
#astCode.body[1].lineno = astCode.body[0].lineno

astCode.body[0].body[1].lineno = astCode.body[0].body[0].lineno
ast.increment_lineno(astCode.body[0].body[1], n=-1)

#astCode.body[0].body[1].value.lineno = astCode.body[0].body[0].lineno
#astCode.body[0].body[1].value.left.lineno = astCode.body[0].body[0].lineno
#astCode.body[0].body[1].value.right.lineno = astCode.body[0].body[0].lineno

print(ast.dump(astCode, include_attributes = True))

exec(compile(astCode, filename="fake.py", mode="exec"))




print(ast.dump(ast.parse("print('hello world')")))