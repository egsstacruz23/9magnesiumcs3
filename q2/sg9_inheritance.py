# Class defintion of "Publication"
class Publication:
  def __init__(self, title, author): 
    self.title = title
    self.author = author

  # Getter and Setter functions for class "Publication"
  @property # To make it look like a attribute
  def get_title(self):
    return self.title # Returns the value of the title

  @property # To make it look like a attribute
  def get_author(self): 
    return self.author # Returns the value of the author

  def set_title(self, title):
    self.title = title

  def set_author(self, author):
    self.author = author

# Class definition of "Book"
class Book(Publication):
  def __init__(self, title, author, numberpages):
    super().__init__(title, author)
    self.numberpages = numberpages

  # Setter and getter function for page number
  @property # To make it look like a attribute
  def get_numberpages(self):
    return self.numberpages # Returns the value of the page number

  def set_numberpages(self, numberpages):
    if numberpages > 0: # To prevent the user from inputing impossible page numbers
      self.numberpages = numberpages
    else:
      print("Invalid page") # To state the integer given is not possible for a page

# Class definition of "Magazine"
class Magazine(Publication):
  def __init__(self, title, author, issueno): #
    super().__init__(title, author)
    self.issueno = issueno

  # Setter and getter function for issue number
  @property # To make it look like a attribute
  def get_issueno(self):
    return self.issueno

  def set_issueno(self, issueno):
    self.issueno = issueno

# Printing the information
print("Publication Information:")
a1 = Book("Games of Thrones", "J.R.R Totelkein", 65)
print("Title:", a1.get_title)
print("Author:", a1.get_author)
print("Number of pages:", a1.get_numberpages())
m1 = Magazine("New York Times", "Wall Street", 34)
print("Title:", m1.get_title)
print("Author:", m1.get_author)
print("Issue Number:", m1.get_issueno())
