# Class defintion of "Publication"
class Publication:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  # Getter and Setter methods for class "Publication"
  @property # To make it look like a attribute
  def get_title(self, title):
    return self.title

  @property # To make it look like a attribute
  def get_author(self, author):
    return self.author

  def set_title(self, title):
    self.title = title

  def set_title(self, author):
    self.author = author

# Class definition of "Book"
class Book(Publication):
  def __init__(self, title, author, numberpages):
    super().__init__(title, author)
    self.numberpages = numberpages
  
  def get_numberpages():
    return self.numberpages

class Magazine(Publication):
  def __init__(self, title, author, issueno):
    super().__init__(title, author)
    self.issueno = issueno

# Printing the information
print("Publication Information:")
a1 = Book("hell" , "auth" , 20)
print("Title:", a1.get_title)
