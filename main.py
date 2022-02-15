from word import Word

""" Core of the App.
  So far only testing happens here.
"""

w1 = Word("Sicherheit", 0)
w2 = Word("security", 1)
w3 = Word("safety", 1)


print("TESTING")
print(w1)
w1.increment_box()
print(f"incremented: {w1}")
w1.reset_box()
print(f"reseted: {w1}")


print("German words:")
Word.print_all_instances(0)
print("English words:")
Word.print_all_instances(1)