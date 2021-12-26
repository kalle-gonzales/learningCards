from word import Word

""" Core of the App.
  So far only testing happens here.
"""

w1 = Word("Sicherheit", 1)
w2 = Word("security", 2)
w3 = Word("safety", 2)

print("TESTING")
print(w1)
w1.increment_box()
print(f"incremented: {w1}")
w1.reset_box()
print(f"reseted: {w1}")


print("German words:")
Word.print_all_instances(1)
print("English words:")
Word.print_all_instances(2)