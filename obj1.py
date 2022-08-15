from abc import ABC ,abstractmethod
class Book(ABC):
    def __init__(self,title,quantity,author,price):
        self.title = title
        self.quantity = quantity
        self.author = author 
        self.__price = price
        self.__discount = None
    
    #discount funtion
    def set_discount(self,discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price*(1- self.__discount) 
        return self.__price
    
    @abstractmethod
    def __repr__(self):
        return f"Book:{self.title}, Quantity:{ self.quantity}, Author:{self.author},Price:{self.get_price()}"


class Novel(Book):
    def __init__(self,title,quantity,author,price,pages):
        super().__init__(title,quantity,author,price)
        self.pages = pages
    def __repr__(self):
        return f"Book:{self.title}, Quantity:{ self.quantity}, Author:{self.author},Price:{self.get_price()}"


class Academic(Book):
    def __init__(self,title,quantity,author,price,branch):
        super().__init__(title,quantity,author,price)
        self.branch = branch
    
    def __repr__(self):
        return f"Book:{self.title}, Quantity:{ self.quantity}, Author:{self.author},Price:{self.get_price()}"


novel1 = Novel('Two States',1,"Chetan Bhagat",200,187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundation',12,"PSF",655,'IT')

print(novel1)
print(academic1)

# single_book = Book('Two States',1,"Chetan Bhagat",200)
# 
# bulk_books = Book('Two States',25,"Chetan Bhagat",200)
# 
# bulk_books.set_discount(0.20)
# 
# print(single_book.get_price())
# 
# print(bulk_books.get_price())
# 
# print(novel1.get_price())