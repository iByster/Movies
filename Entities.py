class Customer:
    
    def __init__(self, cid, name, cnp, adress):
        '''
        Creating object Customer
        Parameters:
            
            cid = int (unique identifier)
            name = string (customer name)
            cnp = int (customer cnp)
            adress = string (customer adress - city)
        '''
    
        self.__cid = cid
        self.__name = name
        self.__cnp = cnp
        self.__adress = adress
        
    def get_name(self):
        '''
        Getter method
        output : Customer name 
        '''
        return self.__name
    
    def get_cid(self):
        '''
        Getter method
        output : Customer id 
        '''
        return self.__cid
    
    def get_cnp(self):
        '''
        Getter method
        output : Customer cnp 
        '''
        return self.__cnp
    
    def get_adress(self):
        '''
        Getter method
        output : Customer adress 
        '''
        return self.__adress
    
    def set_name(self, newName):
        '''
        Setter method
        output : Customer gets a new name
        '''
        
        self.__name = newName
        
    def set_adress(self, newAdress):
        '''
        Setter method
        output : Customer gets a new adress
        '''
        
        self.__adress = newAdress
        
    def set_cnp(self, newCNP):
        '''
        Setter method
        output : Customer gets a new cnp
        '''
        
        self.__cnp = newCNP
    
    def __eq__(self, other):
        '''
        verify if two customers have the same id
        '''
        return self.__cid == other.__cid
         
    def __str__(self):
        '''
        convers object customer in a string line
        '''
        return str(self.__cid)+":"+self.__name+":"+str(self.__cnp)+":"+self.__adress
    
    def same_name(self, other):
        '''
        verify if two customers have the same name
        '''
        return self.get_name() == other.get_name()
    
    @staticmethod
    def read_customer(line):
        '''
        creates a object customer from a line string
        '''
        parts = line.split(":")
        return Customer(int(parts[0].strip()), parts[1].strip(), int(parts[2].strip()), parts[3].strip())
    
    @staticmethod
    def write_customer(customer):
        '''
        convers a customer in a string line, parts being divided by :
        '''
        return str(customer.get_cid()) + ":" + customer.get_name() + ":" + str(customer.get_cnp()) + ":" + customer.get_adress()

class Movie:
    
    def __init__(self, mid, title, genre, status):
        '''
        Creating object Movie
        Params:
            mid = int (unique identifer)
            title = string (movie title)
            genre = string (movie genre)
            status = string (movie status - free/rented)
        '''
        self.__mid = mid
        self.__title = title
        self.__genre = genre
        self.__status = status
        
    def get_mid(self):
        '''
        Getter method 
        output : movie's id
        '''
        return self.__mid
    
    def get_title(self):
        '''
        Getter method 
        output : movie's title
        '''
        return self.__title
    
    def get_genre(self):
        '''
        Getter method
        output : movie's genre
        '''
        return self.__genre
    
    def get_status(self):
        '''
        Getter method
        output : movie's status
        '''
        return self.__status
    
    def set_title(self, newTitle):
        '''
        Setter method
        input : newTitle - string 
        output : the movie gets a new title
        '''
        self.__title = newTitle
        
    def set_genre(self, newGenre):
        '''
        Setter method 
        input : newGenre - string
        output : the movie gets a new genre
        '''
        self.__genre = newGenre
        
    def set_status(self, newStatus):
        '''
        Setter method 
        input : newStatus 
        output : the movie gets a new status
        '''
        self.__status = newStatus
        
    def same_title(self, other):
        '''
        verify if two movies have the same title
        '''
        return self.get_title() == other.get_title()
    
    def same_genre(self, other):
        '''
        verify if two movies have the same genre
        '''
        return self.get_genre() == other.get_genre()
    
    def same_status(self, other):
        '''
        verify if two movies have the same status
        '''
        return self.get_status() == other.get_status()
        
    def __eq__(self, other):
        '''
        verify if two movies have the same id
        '''
        return self.__mid == other.__mid
    
    def __str__(self):
        '''
        converts object movie into a string line 
        '''
        return str(self.__mid)+":"+self.__title+":"+self.__genre+":"+self.__status
    
    @staticmethod
    def read_movie(line):
        '''
        creates a object movie from a line string
        '''
        parts = line.split(":")
        return Movie(int(parts[0].strip()), parts[1].strip(), parts[2].strip(), parts[3].strip())
    
    @staticmethod
    def write_movie(movie):
        '''
        convers a movie in a string line, parts being divided by :
        '''
        return str(movie.get_mid())+":"+movie.get_title()+":"+movie.get_genre()+":"+movie.get_status()
        
class Rental:
    
    def __init__(self, mid, cid, start_date, return_date):
        '''
        Creating object Rented
        Params:
            mid = int - movie id (unique identifier)
            cid = int - customer id (unique identifier)
            start_date = string (the date when a certain movie was rented)
            return_date string (the date when a certain rented movie most be returned 
        '''
        self.__mid = mid
        self.__cid = cid
        self.__start_date = start_date
        self.__return_date = return_date
        
    def get_rented_cid(self):
        '''
        Getter method 
        output : rented movie's id
        '''
        return self.__cid
        
    def get_rented_mid(self):
        '''
        Getter method
        output : customer's id with the rented movie
        '''
        return self.__mid
        
    def get_start_date(self):
        '''
        Getter method 
        output : rented movie start date
        '''
        return self.__start_date
    
    def get_return_date(self):
        '''
        Getter method 
        output : rented movie return date
        '''
        return self.__return_date
    
    def set_start_date(self, newStartDate):
        '''
        Setter method
        output : rented movie gets a new start date
        '''
        self.__start_date = newStartDate
        
    def set_return_date(self, newReturnDate):
        '''
        Setter method
        output : rented movie gets a new return date
        '''
        self.__return_date = newReturnDate
        
    def __eq__(self, other):
        '''
        verify if two rentals have the same id
        '''
        return self.__mid == other.__mid
    
    def __str__(self):
        '''
        converts object rental into a string dividing each part by :
        '''
        return str(self.__mid)+":"+str(self.__cid)+":"+self.__start_date+":"+self.__return_date

    @staticmethod
    def read_rental(line):
        '''
        creates a object rental from a line string
        '''
        parts = line.split(":")
        return Rental(int(parts[0].strip()), int(parts[1].strip()), parts[2].strip(), parts[3].strip())
    
    @staticmethod
    def write_rental(rental):
        '''
        convers a rental in a string line, parts being divided by :
        '''
        return str(rental.get_rented_mid()) + ":" + str(rental.get_rented_cid()) + ":" + str(rental.get_start_date()) + ":" + str(rental.get_return_date())
        