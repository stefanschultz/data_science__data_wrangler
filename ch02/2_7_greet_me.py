def greet_me(a_name):
    print(f"Hello {a_name}!")

author = 'James'
editor = 'John'

greet_me(author)
greet_me(editor)

greet_me('Jane')
greet_me(42)
greet_me(3.14)
greet_me(True)
# greet_me(author, editor) # TypeError: greet_me() takes 1 positional argument but 2 were given
# greet_me() # TypeError: greet_me() missing 1 required positional argument: 'a_name'