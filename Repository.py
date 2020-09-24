from Erorrs.Exceptions import RepoError

class CustomerRepository:
    
    def __init__(self):
        self._listCustomers = []
        
    def add(self, cust):
        if cust in self._listCustomers:
            raise RepoError("id existent!\n")
        
        self._listCustomers.append(cust)
        
                
    def get_all(self):
        return self._listCustomers[:]
    
    def size(self):
        return len(self._listCustomers)
    
    def search(self, key):
        if key not in self._listCustomers:
            raise RepoError("id inexistent!\n")
        for x in self._listCustomers:
            if x == key:
                return x
            
    def delete(self, x):
        self._listCustomers.remove(x)
        
    def modify_name(self, key, newName):
        x = self.search(key)
        x.set_name(newName)
        
    def modify_cnp(self, key, newCNP):
        x = self.search(key)
        x.set_cnp(newCNP)
        
    def modify_adress(self, key, newAdress):
        x = self.search(key)
        x.set_adress(newAdress)
    def get_all_customers_same_name(self, key):
        list_same_name = []
        
        for x in self._listCustomers:
            if x.same_name(key):
                list_same_name.append(x)
                
        if len(list_same_name) == 0 :
            raise  RepoError("Nu exista acest nume")
        else:
            return list_same_name        


class MovieRepository:
    
    def __init__(self):
        self._listMovies = []
        
    def size(self):
        '''
        Function returns the number of elements included in the movie list
        '''
        return len(self._listMovies)
    
    def add(self, movie):
        if movie in self._listMovies:
            raise RepoError("id existent!\n")
        
        self._listMovies.append(movie)

    def search(self, key):
        if key not in self._listMovies:
            raise RepoError("id inexistent!\n")
        
        for x in self._listMovies:
            if x == key:
                return x
            
    def get_all_movies_same_title(self, key):
        list_same_title = []
        for x in self._listMovies:
            if x.same_title(key):
                list_same_title.append(x)
                
        if len(list_same_title) == 0:
            raise RepoError("Nu exista acest titlu")
        else :
            return list_same_title
        
    def get_all_movies_same_genre(self, key):
        list_same_genre = []
        
        for x in self._listMovies:
            if x.same_genre(key):
                list_same_genre.append(x)
                
        if len(list_same_genre) == 0:
            raise RepoError("Nu exista acest gen")
        else :
            return list_same_genre
        
    def get_all_movies_same_status(self, key):
        list_same_status = []
        
        for x in self._listMovies:
            if x.same_status(key):
                list_same_status.append(x)
                
        if len(list_same_status) == 0:
            raise RepoError("Nu exista acest status")
        else :
            return list_same_status
        
    '''
    ---------------------mai corect
    def sterge(self, key):
        if key not in self.___listMovies:
            raise RepoError("id inexistent!\n")
        
        for i in range(self.___listMovies):
            if key == self.___listMovies[i]:
                del.self.___listMovies[i]
    '''            
            
    def get_all(self):
        return self._listMovies[:]
    
    def delete(self, x):
        self._listMovies.remove(x)
    
    def modify_title(self, key, newTitle):
        x = self.search(key)
        x.set_title(newTitle)
        
    def modify_genre(self, key, newGenre):
        x = self.search(key)
        x.set_genre(newGenre)
        
    def modify_status(self, key, newStatus):
        x = self.search(key)
        x.set_status(newStatus)
            
class RentedRepository:
    
    def __init__(self):
        self._listRented = []
        
    def add(self, rental):
        if rental in self._listRented:
            raise RepoError("film deja inchiriat!\n")
        
        self._listRented.append(rental)
    
    def size(self):
        return len(self._listRented)
    
    def search(self, key):
        if key not in self._listRented:
            raise RepoError("filmul nu este inchiriat!\n")
        
        for x in self._listRented:
            if x == key:
                return x
            
    def get_all(self):
        return self._listRented[:]
    
    def delete(self, key):
        if key not in self._listRented:
            raise RepoError("filmul nu este inchiriat!\n")
        
        for x in self._listRented:
            if x == key:
                self._listRented.remove(key)
          
        
        
class FileRepoCustomer(CustomerRepository):
    
    def __init__(self, filename, read_customer, write_customer):
        self.__filename = filename
        self.__read_customer = read_customer
        self.__write_customer = write_customer
        
    def __read_all_from_file(self):
        self._listCustomers = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            
            for line in lines:
                line = line.strip()
                if line != "":
                    customer = self.__read_customer(line)
                    self._listCustomers.append(customer)
                    
    def __write_all_to_file(self):
        with open(self.__filename, "w") as f:
            for customer in self._listCustomers:
                line = self.__write_customer(customer)
                f.write(line + "\n")
    
    def add(self, customer):
        self.__read_all_from_file()
        CustomerRepository.add(self, customer)
        self.__write_all_to_file()
        
    def delete(self, customer):
        self.__read_all_from_file()
        CustomerRepository.delete(self, customer)
        self.__write_all_to_file()
        
    def get_all(self):
        self.__read_all_from_file()
        return self._listCustomers[:]
        
    def size(self):
        self.__read_all_from_file()
        return CustomerRepository.size(self)
    
    def get_all_customers_same_name(self, key):
        self.__read_all_from_file()
        return CustomerRepository.get_all_customers_same_name(self, key)
    
    def search(self, key):
        self.__read_all_from_file()
        return CustomerRepository.search(self, key)
    
    def modify_name(self, key, newName):
        self.__read_all_from_file()
        CustomerRepository.modify_name(self, key, newName)
        self.__write_all_to_file()
        
    def modify_cnp(self, key, newCNP):
        self.__read_all_from_file()
        CustomerRepository.modify_cnp(self, key, newCNP)
        self.__write_all_to_file()
        
    def modify_adress(self, key, newAdress):
        self.__read_all_from_file()
        CustomerRepository.modify_adress(self, key, newAdress)
        self.__write_all_to_file()
        
class FileRepoMovie(MovieRepository):
    
    def __init__(self, filename, read_movie, write_movie):
        self.__filename = filename
        self.__read_movie = read_movie
        self.__write_movie = write_movie
        
    def __read_all_from_file(self):
        self._listMovies = []
        
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            
        for line in lines:
            line = line.strip()
            if line != "":
                movie = self.__read_movie(line)
                self._listMovies.append(movie)
                
    def __write_all_to_file(self):
        
        with open(self.__filename, "w") as f:
            for movie in self._listMovies:
                line = self.__write_movie(movie)
                f.write(line + "\n")
                
    def add(self, movie):
        self.__read_all_from_file()
        MovieRepository.add(self, movie)
        self.__write_all_to_file()
        
    def delete(self, x):
        self.__read_all_from_file()
        MovieRepository.delete(self, x)
        self.__write_all_to_file()
        
    def get_all(self):
        self.__read_all_from_file()
        return MovieRepository.get_all(self)
        self.__write_all_to_file()
        
    def search(self, key):
        self.__read_all_from_file()
        return MovieRepository.search(self, key)
    
    def get_all_movies_same_title(self, key):
        self.__read_all_from_file()
        return MovieRepository.get_all_movies_same_title(self, key)
    
    def get_all_movies_same_genre(self, key):
        self.__read_all_from_file()
        return MovieRepository.get_all_movies_same_genre(self, key)
    
    def get_all_movies_same_status(self, key):
        self.__read_all_from_file()
        return MovieRepository.get_all_movies_same_status(self, key)
    
    def modify_title(self, key, newTitle):
        self.__read_all_from_file()
        MovieRepository.modify_title(self, key, newTitle)
        self.__write_all_to_file()
        
    def modify_genre(self, key, newGenre):
        self.__read_all_from_file()
        MovieRepository.modify_genre(self, key, newGenre)
        self.__write_all_to_file()
        
    def modify_status(self, key, newStatus):
        self.__read_all_from_file()
        MovieRepository.modify_status(self, key, newStatus)
        self.__write_all_to_file()
        
class FileRepoRented(RentedRepository):
    
    def __init__(self, filename, read_rental, write_rental):
        self.__filename = filename
        self.__read_rental = read_rental
        self.__write_rental = write_rental
        
    def __read_all_from_file(self):
        self._listRented = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    rented = self.__read_rental(line)
                    self._listRented.append(rented)
                    
    def __write_all_to_file(self):
        
        with open(self.__filename, "w") as f:
            for movie in self._listRented:
                line = self.__write_rental(movie)
                f.write(line + "\n")
                
    def add(self, rental):
        self.__read_all_from_file()
        RentedRepository.add(self, rental)
        self.__write_all_to_file()
    
    def search(self, key):
        self.__read_all_from_file()
        return RentedRepository.search(self, key)
    
    def get_all(self):
        self.__read_all_from_file()
        return RentedRepository.get_all(self)

    def delete(self, x):
        self.__read_all_from_file()
        RentedRepository.delete(self, x)
        self.__write_all_to_file()
    
    def size(self):
        self.__read_all_from_file()
        return RentedRepository.size(self)    
'''   
class RepoCustomerTemaLab11():
    
    def __init__(self, filename, filenameAUX, read_customer, write_customer):
        self.__filename = filename
        self.__filenameAUX = filenameAUX
        self.__read_customer = read_customer
        self.__write_customer = write_customer
        
    def __read_all_from_file(self):
        self._listCustomers = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            
            for line in lines:
                line = line.strip()
                if line != "":
                    customer = self.__read_customer(line)
                    self._listCustomers.append(customer)
                    
    def __write_all_to_file(self):
        with open(self.__filename, "w") as f:
            for customer in self._listCustomers:
                line = self.__write_customer(customer)
                f.write(line + "\n")
    
    def add(self, newCustomer):
        
        self.OK = 1
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    customer = self.__read_customer(line)
                    if customer == newCustomer:
                        self.OK = 0
                        raise RepoError("id existent!\n")
                        
        if self.OK == 1:
            with open(self.__filename, "a") as f:
                    line = self.__write_customer(newCustomer)
                    f.write(line + "\n")
            
    def delete(self, newCustomer):
        self.OK = 1
        g = open(self.__filenameAUX, "w")
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    customer = self.__read_customer(line)
                    if customer.get_cid() == newCustomer.get_cid():
                        self.OK = 0
                    else:
                        line = self.__write_customer(customer)
                        print(line)
                        g.write(line + '\n')
                        g.flush        if self.OK == 1:
            raise RepoError("id inexistent!\n")
        
        g.close()
        
        with open(self.__filenameAUX) as f:
            lines = f.readlines()
            lines = [l for l in lines if "ROW" in l]
            with open(self.__filename, "w") as f1:
                f1.writelines(lines)         
             
    def search(self, key):
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    customer = self.__read_customer(line)
                    if customer == key:
                        return customer
    
    
    def get_all(self):
        self.lista = []
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    customer = self.__read_customer(line)
                    self.lista.append(customer)
                    
        return self.lista
       
    def size(self):
        self.count = 0
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    self.count += 1
                    
        return self.count
    
    
    def modify_name(self, key, newName):
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    x = self.search(key)
                    x.set_name(newName)             
    
    def modify_cnp(self, key, newCNP):
        self.__read_all_from_file()
        CustomerRepository.modify_cnp(self, key, newCNP)
        self.__write_all_to_file()
        
    def modify_adress(self, key, newAdress):
        self.__read_all_from_file()
        CustomerRepository.modify_adress(self, key, newAdress)
        self.__write_all_to_file()
        
    def get_all_customers_same_name(self, key):
        self.__read_all_from_file()
        return CustomerRepository.get_all_customers_same_name(self, key)
    '''