from Domain.Entities import Customer, Movie, Rental
from Erorrs.Exceptions import RepoError



def mergeSortV2(myList, key):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        #print(left)
        right = myList[mid:]
        #print(right)
    
        mergeSortV2(left, key)
        mergeSortV2(right, key)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if keye(left[i]) > keye(right[j]):
        
                myList[k] = left[i]        
                i += 1
            else:
                myList[k] = right[j]
                j += 1
        
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]   
            j += 1
            k += 1

def keye(elem1):
    return elem1[1]

def bingoSort(listaValues, keye2):
    Max = len(listaValues) - 1
    
    nextValue = listaValues[Max]
    #print(nextValue)
    for i in range(Max-1, -1, -1):
        if keye2(listaValues[i]) < keye2(nextValue):
            nextValue = listaValues[i]
    while (Max > 0) and (keye2(listaValues[Max]) == keye2(nextValue)):
        Max -= 1
        
    while Max > 0 :
        value  = nextValue
        nextValue = listaValues[Max]
        for i in range(Max-1, -1, -1):
            if keye2(listaValues[i]) == keye2(value):
                listaValues[i], listaValues[Max] = listaValues[Max], listaValues[i]
                Max -= 1
            elif keye2(listaValues[i]) < keye2(nextValue) :
                nextValue = listaValues[i]
                
        while (Max > 0) and (keye2(listaValues[Max]) == keye2(nextValue)):
            Max -= 1
            
        

def keye2(elem):
    return elem[1]

    
            

def mergeSortV3(myList, comparator):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSortV3(left, comparator)
        mergeSortV3(right, comparator)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if comparator(left[i], right[j]) == 1:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            elif comparator(left[i], right[j]) == 0 or comparator(left[i], right[j]) == -1:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
            
def comparator(cmp1, cmp2):
    if cmp1[1] == cmp2[1]:
        return 0
    #nu sunt in ordine
    if cmp1[1] < cmp2[1]:
        return -1
    #sunt in ordine
    if cmp1[1] > cmp2[1]:
        return 1 
            

class MovieController:
    
    def __init__(self, validMovie, repoMovie):
        self.__validMovie = validMovie
        self.__repoMovie = repoMovie
        
    def add_movie(self, mid, title, genre, status):
        
        movie = Movie(mid, title, genre, status)
        
        self.__validMovie.validate_movie(movie)
        self.__repoMovie.add(movie)
        
    def get_movies(self):
        return self.__repoMovie.get_all()

    def get_NoMovies(self):
        return self.__repoMovie.size()

    def modify_movie_by_title(self, mid, newTitle):
        movie = Movie(mid, None, None, None)
        valid = Movie(mid, newTitle, "drama", "free")
        self.__validMovie.validate_movie(valid)
        self.__repoMovie.modify_title(movie, newTitle)
            
    def modify_movie_by_genre(self, mid, newGenre):
        movie = Movie(mid, None, None, None)
        valid = Movie(mid, "Joker", newGenre, "free")
        self.__validMovie.validate_movie(valid)
        self.__repoMovie.modify_genre(movie, newGenre)
        
    def modify_movie_by_status(self, mid, newStatus):
        movie = Movie(mid, None, None, None)
        valid = Movie(mid, "Joker", "drama", newStatus)
        self.__validMovie.validate_movie(valid)
        self.__repoMovie.modify_status(movie, newStatus)
        
    def remove_movie(self, mid):
        movie = Movie(mid, None, None, None)
        movie_selected = self.__repoMovie.search(movie)
        self.__repoMovie.delete(movie_selected)
        

    def all_movies_same_title(self, title):
        
        self.list = []
        
        movie = Movie(None, title, None, None)
        
        self.list = self.__repoMovie.get_all_movies_same_title(movie)
        
        return self.list 
    
    def all_movie_same_genre(self, genre):
        
        self.list = []
        
        movie = Movie(None, None, genre, None)
        
        self.list = self.__repoMovie.get_all_movies_same_genre(movie)
        
        return self.list  
    
    def all_movies_same_status(self, status):
        
        self.list = []
        
        movie = Movie(None, None, None , status)
        
        self.list = self.__repoMovie.get_all_movies_same_status(movie)
        
        return self.list     
    
    
class CustomerController:
    
    def __init__(self, validCustomer, repoCustomer):
        self.__validCustomer = validCustomer
        self.__repoCustomer = repoCustomer
        
    def add_customer(self, cid, name, cnp, adress):
        
        customer = Customer(cid, name, cnp, adress)
        
        self.__validCustomer.validate_customer(customer)
        self.__repoCustomer.add(customer)
        
    def get_customers(self):
        return self.__repoCustomer.get_all()
    
    def modify_customer_by_name(self, cid, newName):
        
        customer = Customer(cid, None, None, None)
        valid = Customer(cid, newName, 1, "1")
        self.__validCustomer.validate_customer(valid)
        self.__repoCustomer.modify_name(customer, newName)
               
    def modify_customer_by_cnp(self, cid, newCNP):
        customer = Customer(cid, None, None, None)
        valid = Customer(cid, "Alex", newCNP, "1")
        self.__validCustomer.validate_customer(valid)
        self.__repoCustomer.modify_cnp(customer, newCNP)
        
    def modify_customer_by_adress(self, cid, newAdress):
        customer = Customer(cid, None, None, None)
        valid = Customer(cid, "Alex", 1, newAdress)
        self.__validCustomer.validate_customer(valid)
        self.__repoCustomer.modify_adress(customer, newAdress)
          
    def remove_customer(self, cid):
        customer = Customer(cid, None, None, None)
        #TEMA LAAAB MODIFICA
        customer_selected = self.__repoCustomer.search(customer)
        self.__repoCustomer.delete(customer_selected)
        
    def search_customer_by_name(self, name):
        
        self.list = []
        
        customer = Customer(None, name, None , None)
        
        self.list = self.__repoCustomer.get_all_customers_same_name(customer)
        
        return self.list  
    
    def get_customers_no(self):
        return self.__repoCustomer.size()
        
    
class RentedController:
    
    def __init__(self,validRented, repoRented, repoCustomer, repoMovie):
        self.__validRented = validRented
        self.__repoRented = repoRented
        self.__repoCustomer = repoCustomer
        self.__repoMovie = repoMovie
        
    def add_rental(self, mid, cid, start_date, return_date):
        
        rental = Rental(mid, cid, start_date, return_date)
        
        customer = Customer(cid, None, None, None)

        movie = Movie(mid, None, None, None)
        
        
        
        self.__repoCustomer.search(customer)
        movie_found = self.__repoMovie.search(movie)
        if movie_found.get_status() == "rented":
            raise RepoError("film deja inchiriat!\n")
        
        else:
            self.__validRented.validate_rental(rental)        
            self.__repoRented.add(rental)
                  
    def get_rentals(self):
        return self.__repoRented.get_all()
    
    def return_movie(self, mid):
        
        rental = Rental(mid, None, None, None)
        movie = Movie(mid, None, None, None)
        rental_found = self.__repoRented.search(rental)
        
        self.__repoRented.delete(rental_found)
        

        
    def all_customers_with_movies(self):
        
        rented = self.__repoRented.get_all()
        
        clients_with_movies = []
        
        for i in rented:
            customer = Customer(i.get_rented_cid(), None, None, None)
            customer_found = self.__repoCustomer.search(customer)
            if customer_found not in clients_with_movies:
                clients_with_movies.append(customer_found)
                
        clients_with_movies.sort(key=lambda x:x.get_name(), reverse=False)
        
        return clients_with_movies
    
    def all_customers_with_moviesV2(self, rented, len_rented, clients_with_movies):
        

        if len_rented == 0:
            print(clients_with_movies)
            return clients_with_movies
        else:
            customer = Customer(rented[len_rented-1].get_rented_cid(), None, None, None)
            customer_found = self.__repoCustomer.search(customer)
            if customer_found not in clients_with_movies:
                
                clients_with_movies.append(customer_found)
            return self.all_customers_with_moviesV2(rented, len_rented-1, clients_with_movies)
                
    def all_customrs_with_more_movies(self):
        
        rented = self.__repoRented.get_all()
        
        clients_with_movies = []
        
        rented_list = {}
        
        for i in rented:
            if i.get_rented_cid() not in rented_list:
                rented_list[i.get_rented_cid()] = 0
            else :
                rented_list[i.get_rented_cid()] += 1
        
        
        #sortate = sorted(rented_list.items(), key = lambda x:(x[1], x[0]), reverse = True)
        
        #listaValues = list(rented_list.values())
        #listaKeys = list(rented_list.keys())
        
        #print(listaValues)
        #print(listaKeys)
        
        '''
        bingo sort
        ''' 
        dictlist = []

        for key, value in rented_list.items():
            temp = [key,value]
            dictlist.append(temp)
        
        #print(dictlist)
        
        bingoSort(dictlist, keye2 = keye2)
                    
        
        '''
        sortate = True
        
        while sortate == True:# best case = O(n) cand toate elementele sunt sortate
            sortate = False # worst case = O(n^2) cand elementele sunt in ordine crescatoare
            for i in range(0, len(listaValues)-1):# nr cazuri totale = n(n-1)
                if listaValues[i] < listaValues[i+1]:# caz mediu = caiet ( O(n^2) )
                    sortate = True
                    listaKeys[i], listaKeys[i+1] = listaKeys[i+1], listaKeys[i]
                    listaValues[i], listaValues[i+1] = listaValues[i+1], listaValues[i]
        '''
        for i in dictlist:
            customer = Customer(i[0], None, None, None)
            customer_found = self.__repoCustomer.search(customer)
            clients_with_movies.append(customer_found)

        return clients_with_movies
    
    
    def all_customrs_with_more_moviesV2(self):
        
        rented = self.__repoRented.get_all()                    # O(n)
        
        clients_with_movies = []                                # O(1)
        
        rented_list = {}                                        # O(1)
        
        for i in rented:                                        # O(n) / Theta(n)
            if i.get_rented_cid() not in rented_list:
                rented_list[i.get_rented_cid()] = 0
            else :
                rented_list[i.get_rented_cid()] += 1
        
        
        #sortate = sorted(rented_list.items(), key = lambda x:(x[1], x[0]), reverse = True)
        
        listaValues = list(rented_list.values())
        listaKeys = list(rented_list.keys())
        
        #print(listaValues)
        #print(listaKeys)
        
        
        sortate = True
        
        while sortate == True:# best case = O(n) cand toate elementele sunt sortate
            sortate = False # worst case = O(n^2) cand elementele sunt in ordine crescatoare
            for i in range(0, len(listaValues)-1):# nr cazuri totale = n(n-1)
                if listaValues[i] < listaValues[i+1]:# caz mediu = caiet ( O(n^2) )
                    sortate = True
                    listaKeys[i], listaKeys[i+1] = listaKeys[i+1], listaKeys[i]
                    listaValues[i], listaValues[i+1] = listaValues[i+1], listaValues[i]
        
        for i in listaKeys:                                             # O(n)
            customer = Customer(i, None, None, None)
            customer_found = self.__repoCustomer.search(customer)
            clients_with_movies.append(customer_found)

        return clients_with_movies
    
    def top_5_rented_movies(self):
        
        movies = self.__repoMovie.get_all()
        
        
        
        count_list = {}
        
        movies_title = []
        
        for i in movies:
            if i.get_status() == "rented":           
                if i.get_title() not in count_list:
                    count_list[i.get_title()] = 0
                else:
                    count_list[i.get_title()] += 1
                    
            
        sortare = sorted(count_list.items(), key = lambda x:(x[1], x[0]), reverse = True)
            
        for i in sortare:
            movies_title.append(i[0])
                
        return movies_title[:5]
    
    
    
    
            
    def top_5_rented_moviesV2(self):
        
        # Theta(1)
        movies = self.__repoMovie.get_all() 
                
        # Theta(1)
        count_list = {}
        
        # Theta(1)
        movies_title = []
        
        
        # Theta(n)
        for i in movies:
            if i.get_status() == "rented":           
                if i.get_title() not in count_list:
                    count_list[i.get_title()] = 1
                else:
                    count_list[i.get_title()] += 1
                    
        dictlist = []

        # Theta(n)
        for key, value in count_list.items():
            temp = [key,value]
            dictlist.append(temp)
                    
        #sortare = sorted(count_list.items(), key = lambda x:(x[1], x[0]), reverse = True)
        
        
        '''
        merge sort
        '''
        # merge sort complexity : best case = worst case = average case = Theta(n log n)
        mergeSortV3(dictlist, comparator = comparator)
        
        #mergeSortV2(dictlist, key = keye)
       
        # Theta(n)
        for i in dictlist:
            movies_title.append(i[0])
            
        return movies_title[:5]
    
        # Overall complexity : Theta(n log n)
    
                
        '''
        for i in range(1, len(listaValues)): 
      
            key = listaValues[i]
            key2 = listaKeys[i] 
             
            j = i-1
            while j >=0 and key > listaValues[j] : 
                    listaValues[j+1]  = listaValues[j]
                    listaKeys[j+1] = listaKeys[j] 
                    j -= 1
            listaValues[j+1] = key 
            listaKeys[j+1] = key2
        '''
        
    def top_30procent_customers_most_movies(self):
        
        rented = self.__repoRented.get_all()
        
        clients_with_movies = []
        
        rented_list = {}
        
        for i in rented:
            if i.get_rented_cid() not in rented_list:
                rented_list[i.get_rented_cid()] = 0
            else :
                rented_list[i.get_rented_cid()] += 1
        
        
        sortate = sorted(rented_list.items(), key = lambda x:(x[1], x[0]), reverse = True)
        
        for i in sortate:
            customer = Customer(i[0], None, None, None)
            customer_found = self.__repoCustomer.search(customer)
            clients_with_movies.append(customer_found)

        count = int((len(clients_with_movies * 3) / 10))

        return clients_with_movies[:count]
    
    def top_genre_rented(self):
        
        movies = self.__repoMovie.get_all() # O(1)
        
        count_list = {}                     # O(1)
        
        movies_genre = []                   # O(1)
        
        for i in movies:                                #__
            if i.get_status() == "rented":              # nr de pasi = suma de la i = 1 pana la n de 1 = n  
                if i.get_genre() not in count_list:     # worst case = best case = average
                    count_list[i.get_genre()] = 0       # nu luam in cosiderare if/ else deoarece face acelasi numar de pasi
                else:                                   #__
                    count_list[i.get_genre()] += 1      #__
        
        sortare = sorted(count_list.items(), key = lambda x:(x[1], x[0]), reverse = True) # O(n log n ) ( worst case = O(n^2) ) 
        
        for i in sortare:                   # O(n)
            movies_genre.append(i[0])       
            
        return movies_genre[:]              # O(1)
    
        # Complexitatea = O(1) + O(1) + O(1) + O(n) + O (n log n) + O(n) + O(1) = O(n log n) - best case
        #               = O(n^2) - worst case din cauza la functia sorted
