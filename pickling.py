import pickle
 
# todo = ['write blog post', 'reply to email', 'read in a book']

# with open("todo.pickle", "wb") as archivo:
#     pickle.dump(todo, archivo)


with open("todo.pickle", "rb") as archivo:
    t = pickle.load(archivo)

print(t)
