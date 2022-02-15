from datetime import datetime as dt

class Word:
  """
    Instances of Word build the backbone of the App.

    They are connected to others as front and back of cards.
    They contain information about their language, box, history, nextUp and translation (the connection to other Words).
  """

  # until we have a database, we need to keep track of the instances
  instances = []

  # creates a new instance of the class Word
  #
  # takes a value (String) and a lanugage (Int: 0 = German, 1 = English, 2 = Spanish, 3 = Japanese, etc)
  # Initialises box to be 0, history and translations to None and next_up to datetime.now
  def __init__(self, value, language):
    self.value = value
    self.language = language
    self.box = 0
    self.history = None
    self.next_up = dt.now()
    self.translations = None
    self.instances.append(self)

  # used when print is called on an instance of Word
  def __str__(self):
    return f"value: {self.value}, language: {self.language}, box: {self.box}, history: {self.history}, next up: {self.next_up}"

  # when a Word is answered correctly it is put in the next box
  def increment_box(self):
    self.box += 1
    # TODO: increment box of any Word that is connected to this one

  # when a Word is answered wrongly it is be put in the first box
  # this should also be true for any Word that is connected to this one
  def reset_box(self):
    self.box = 0
    # TODO: reset box of any Word that is connected to this one

  # returns all instances of the Class Word that fit to the language
  #
  # A Word instance fits, when the language argument is the same as the Word's language
  # If no language argument is provided every instance fits.
  #
  # @params: language [Int], defaults to None
  # @return: Word [Array]
  @classmethod
  def get_all_instances(cls, language = None):
    if language is None:
      return cls.instances
    inst = []
    for instance in cls.instances:
      if instance.language == language: inst.append(instance)
    return inst

  # prints all instances of the Class Word that fit to the language
  #
  # This of course only needed until we have a database
  #
  # calls get_all_instances, so the condition for a word to be considered to be fitting are the same:
  # A Word instance fits, when the language argument is the same as the Word's language
  # If no language argument is provided every instance fits.
  #
  # @params language [Int], defaults to None
  # @return: None
  @classmethod
  def print_all_instances(cls, language):
    for instance in cls.get_all_instances(language):
      print(instance)

