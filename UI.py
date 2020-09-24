from Erorrs.Exceptions import ValidError, RepoError
from random import randint

class Console:
    
    def __init__(self, ctrlMovie, ctrlCustomer, ctrlRented):
        self.__ctrlMovie = ctrlMovie
        self.__ctrlCustomer = ctrlCustomer
        self.__ctrlRented = ctrlRented
        
    def ui_main_show(self):
        #se afiseaza meniul principal
        print("MENIU")       
        print("1.Clienti")
        print("2.Filme")
        print("3.Inchirieri")
        print("4.Genereaza")
        print("5.Cautari")
        print("6.Rapoarte")
        print("7.Exit")
    
    def ui_customer_show(self):
        #se afiseaza meniul special pentru sectiunea client
        print("1.Adauga client")
        print("2.Modifica client")
        print("3.Sterge client")
        print("4.Arata lista clienti")
        
    def ui_movie_show(self):
        #se afiseaza meniul special pentru sectiunea film
        print("1.Adauga film")
        print("2.Modifica film")
        print("3.Sterge film")
        print("4.Arata lista filme")
        
    def ui_rental_show(self):
        #se afiseaza meniul special pentru sectiunea filme inchiriate
        print("1.Inchiriaza")
        print("2.Returneaza")
        print("3.Arata lista de filme inchiriate")
        
    def ui_customer_modify(self):
        #se afiseaza meniul special din sectiunea client pentru comanda mofidica client
        print("1.Modifica nume")
        print("2.Modifica cnp")
        print("3.Modifica adresa")
        
    def ui_movie_modify(self):
        #se afiseaza meniul special din sectiunea film pentru comanda modifica film
        print("1.Modifica titlu")
        print("2.Modifica genul")
        print("3.Modifica status")
    
    def ui_raport_show(self):
        #se afiseaza meniul special sectiuni rapoarte
        print("1.Afiseaza clienti cu filme inchiriate")
        print("2.Top 5 cele mai inchiriate filme")
        print("3.Primi 30% clienti cu cele mai multe filme")
        print("4.Cele mai inchiriate genuri")
    
    def ui_search(self):
        #se afiseazaa meniul special din sectiunea cautare 
        print("1.Afiseaza toate filmele cu acelasi titlu")
        print("2.Afiseaza toate filmele cu acelasi gen")
        print("3.Afiseaza toate filmele cu acelasi status")
        print("4.Cauta client dupa nume")
            
    def validate_keyboard(self, menu):
        '''
        Validator comenzi pentru meniu
        input : menu - indica comenzile specifice meniului curent
        output : x - comanda valida
        '''
        
        if menu == "customer" or menu == "movie" or menu == "search":
            while True:
                try:
                    x = int(input())
                        
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        break
                    else:
                        print("comanda invalida!\n")        
                except:
                    print("comanda invalida!\n")
                

    
        if  menu == "modify" or menu == "rental":
            while True:
                try:
                    x = int(input())
                        
                    if x == 1 or x == 2 or x == 3:
                        break
                    else:
                        print("comanda invalida!\n")        
                except:
                    print("comanda invalida!\n")
        
        if menu == "main":
            while True:
                try:
                    x = int(input())
                    
                    if x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7:
                        break
                    else:
                        print("comanda invalida!\n")
                except:
                    print("comanda invalida!\n")
                    
        if menu == "generate":
            while True:
                try:
                    x = int(input())
                    
                    if x == 1 or x == 2:
                        break
                    else:
                        print("comanda invalida!\n")
                except:
                    print("comanda invalida!\n")
                
        return x
    
    def __ui_add_customer(self):
        '''
        Se citesc datele necesare pentru adaugarea unui client
        '''
        try:
            cid = int(input("ID:"))
            name = input("Nume:")
            cnp = int(input("CNP:"))
            adress = input("Adresa:")
            self.__ctrlCustomer.add_customer(cid, name, cnp, adress)
        #in cazul in care datele introduse nu corespund cerintelor cerute
        except:
            print("date invalide!")
        
    def __ui_add_movie(self):
        '''
        Se citesc datele necesare pentru adaugarea unui film
        '''
        try:
            mid = int(input("ID:"))
            title = input("Titlu:")
            genre = input("Gen:")
            status = input("Status:")
            self.__ctrlMovie.add_movie(mid, title, genre, status)
        except:
            print("date invalide!")

    def __ui_add_rental(self):
        '''
        Se citesc datele necesare pentru adaugarea unui film inchiriat
        '''
        print("Alegi id-ul clientului care inchiriaza filmul")
        #se afiseaza lista tuturor clientilor
        self.__ui_print_customers()
        cid = input()
        #se afiseaza lista tuturor filmelor
        self.__ui_print_movies()
        print("Alegi filmul care va fi inchiriat")
        mid = input()
        start_date = input("Data inchirieri(DD.MM.YYYY):")
        return_date = input("Data returnari(DD.MM.YYYY):")
        
        self.__ctrlRented.add_rental(int(mid), int(cid), start_date, return_date)
        #dupa ce adaugam un film in lista rented, filmul devine indisponibil
        self.__ctrlMovie.modify_movie_by_status(int(mid), "rented")
           
    def __ui_modify_customer_by_name(self, key):
        '''
        Se modifica numele clientului 
        input : key - este id-ul clientului
        '''
        #se citeste noul nume
        newName = input("Nume nou:")
        
        self.__ctrlCustomer.modify_customer_by_name(key, newName)
        
    def __ui_modify_movie_by_title(self, key):
        '''
        Se modifica titlul unui film
        input : key - este id-ul filmului
        '''
        
        #se citeste noul titlu
        newTitle = input("Titlu nou:")
        
        self.__ctrlMovie.modify_movie_by_title(key, newTitle)
    
    def __ui_modify_customer_by_cnp(self, key):
        '''
        Se modifica cnp-ul clientului
        input : key - id-ul clientului
        '''
        #se citeste noul cnp
        try:
            newCNP = int(input("CNP nou:"))
            self.__ctrlCustomer.modify_customer_by_cnp(key, newCNP)
        except:
            print("CNP invalid!")
        
    def __ui_modify_movie_by_genre(self, key):
        '''
        Se modifica genul filmului
        input : key - id-ul filmului
        '''
        #se citeste noul gen
        newGenre = input("Gen nou:")
        
        self.__ctrlMovie.modify_movie_by_genre(key, newGenre)
        
    def __ui_modify_customer_by_adress(self, key):
        '''
        Se modifica adresa clientului
        input : key - id-ul clientului
        '''
        #se citeste noua adresa
        newAdress = input("Adresa noua:")
        
        self.__ctrlCustomer.modify_customer_by_adress(key, newAdress)
        
    def __ui_modify_movie_by_status(self, key):
        '''
        Se modifica statusul filmului
        input : key - id-ul filmului
        '''
        
        #se citeste noul status
        newStatus = input("Staus:")
        
        self.__ctrlMovie.modify_movie_by_status(key, newStatus)
        
    def __ui_delete_customer(self):
        
        #key reprezinta id-ul dupa care se va cauta clientul ce trebuie sters        
        key = input("Alege dupa id clientul care sa fie sters:")
        
        self.__ctrlCustomer.remove_customer(int(key))
        
    def __ui_delete_movie(self):
        
        key = input("Alege dupa id filmul care sa fie sters:")
        
        self.__ctrlMovie.remove_movie(int(key))
        
    def __ui_print_customers(self):
        
        customers = self.__ctrlCustomer.get_customers()
        
        for i in customers:
            print(i)
            
    def __ui_print_movies(self):        
        movies = self.__ctrlMovie.get_movies()
        
        for i in movies:
            print(i)
            
    def __ui_print_rentals(self):
        rentals = self.__ctrlRented.get_rentals()
        
        for i in rentals:
            print(i)
            
    def __ui_return_movie(self):
        key = input("Scrieti id ul filmului ce va fi returnat:")
        
        self.__ctrlRented.return_movie(int(key))
        self.__ctrlMovie.modify_movie_by_status(int(key), "free")
    '''
    TEMA LAB ITERATIA 2
    '''
    def __ui_genereaza_clienti(self):
        
        nr_clienti = int(input("Cati clienti sa se genere :"))
        
        lista_prenume = ["Alex", "Mircea", "Dan", "Ion", "Cristi", "George", "Mihai", "Paul"]
        
        lista_nume = ["Gane", "Suciu", "Cimpeanu", "Bijec", "Borcan", "Tren", "Patinuar", "Restaurant"]
        
        lista_adrese = ["Miercurea Ciuc", "Brasov", "Cluj-Napoca", "Bucuresti", "Iasi", "Timisoara", "Bacau"]
        i = 0
        
        while i < nr_clienti:
            
            cid = randint(1,100)
            
            name = lista_prenume[randint(0,7)] + " " + lista_nume[randint(0,7)]
            
            cnp = randint(10000000,99999999)
            
            adress = lista_adrese[randint(0,6)]
            
            try :
                self.__ctrlCustomer.add_customer(cid, name, cnp, adress)
            except RepoError : i -= 1
            
            i += 1
            
    def __ui_genereaza_filme(self, nr_filme):
        
        lista_filme = ["Joker", "Fast and Furious", "Lion King", "Fury", "Matrix", "Shrek", "Titanic", "A MOVIE"]
        
        lista_genuri = ["actiune", "drama", "aventura", "politist", "sf", "dragoste"]
        
        if nr_filme > 0:
            
            mid = randint(1,100)
            
            title = lista_filme[randint(0,7)]
            
            genre = lista_genuri[randint(0,5)]
            
            status = "free"
            
            try:
                self.__ctrlMovie.add_movie(mid, title, genre, status)
            except RepoError : nr_filme+= 1
            
            self.__ui_genereaza_filme(nr_filme - 1)
            
    def __ui_print_all_movies_same_title(self):
        
        search_title = input("Introduceti titlul:")
        
        self.list = []
        
        self.list = self.__ctrlMovie.all_movies_same_title(search_title)
            
        for i in self.list:
            print(i)
            
    def __ui_print_all_movies_same_genre(self):
        
        search_genre = input("Introduceti genul:")
        
        self.list = []
        
        self.list = self.__ctrlMovie.all_movie_same_genre(search_genre)
        
        for i in self.list:
            print(i)
            
    def __ui_print_all_movies_same_status(self):
        
        search_status = input("Introduceti status:")
        
        self.list = []
        
        self.list = self.__ctrlMovie.all_movies_same_status(search_status)
        
        for i in self.list:
            print(i)
            
    def __ui_print_all_customers_same_name(self):
        
        search_name = input("Introduceti numele:")
        
        self.list = []
        
        self.list = self.__ctrlCustomer.search_customer_by_name(search_name)
        
        for i in self.list:
            print(i)
            
    def __ui_print_customers_with_movies_sortName(self):
        
        rented = self.__ctrlRented.get_rentals()
        
        self.clients_with_movies = []
        
        len_rented = len(rented)
        
        #self.list = []
        
        self.clients_with_movies = self.__ctrlRented.all_customers_with_moviesV2(rented, len_rented, self.clients_with_movies)
        
        self.clients_with_movies.sort(key=lambda x:x.get_name(), reverse=False)
        
        for i in self.clients_with_movies:
            print(i)
            
    def __ui_print_customers_with_movies_sortOwnedMovies(self):
        
        self.list = []
        
        self.list = self.__ctrlRented.all_customrs_with_more_movies()
        
        for i in self.list:
            print(i)
    
    def __ui_top_5_rented_movies(self):
        
        self.list = []
        
        self.list = self.__ctrlRented.top_5_rented_moviesV2()
        
        for i in self.list:
            print(i)
        
    def __ui_30procent(self):
        
        self.list = []
        
        self.list = self.__ctrlRented.top_30procent_customers_most_movies()
        
        for i in self.list:
            print(i)
            
    def __ui_top_genre(self):
        
        self.list = []
        
        self.list = self.__ctrlRented.top_genre_rented()
        
        for i in self.list:
            print(i)
    def run(self):
        while True:
            
            #se afiseaza meniul principal
            self.ui_main_show()
            
            #se citeste comanda pentru meniul principal
            keyboard = self.validate_keyboard("main")
            
            #afiseaza meniul principal pentru clienti
            if keyboard == 1:
                self.ui_customer_show()
                
                #se citeste comanda speciala pentru sectiunea clienti
                keyboard = self.validate_keyboard("customer")
                
                #1- se adauga client
                if keyboard == 1:
                    try:
                        self.__ui_add_customer()
                    except ValidError as ve:
                        print (str(ve))
                    except RepoError as re:
                        print(str(re))
                
                #2- se modifica client
                elif keyboard == 2:
                    self.__ui_print_customers()
                    print("Introduceti id client pe care doriti sa-l modificati")
                    
                    aux = int(input())
                    
                    self.ui_customer_modify()
                    
                    keyboard = self.validate_keyboard("modify")
                    
                    if keyboard == 1:
                        try:                        
                            self.__ui_modify_customer_by_name(aux)
                        except RepoError as re:
                            print(str(re))
                        except ValidError as ve:
                            print(str(ve))
                    
                    elif keyboard == 2:
                        try:
                            self.__ui_modify_customer_by_cnp(aux)
                        except RepoError as re:
                            print(str(re))
                        except ValueError as ve:
                            print(str(ve))
                            
                    elif keyboard == 3:
                        try:
                            self.__ui_modify_customer_by_adress(aux)
                        except RepoError as re:
                            print(str(re))
                        except ValidError as ve:
                            print(str(ve))
                        
                elif keyboard == 3:
                    #self.__ui_print_customers()
                    try:
                        self.__ui_delete_customer()
                    except RepoError as re:
                        print(str(re))
                    
                elif keyboard == 4:
                    
                    self.__ui_print_customers()
                
            elif keyboard == 2:
                
                self.ui_movie_show()  
                
                keyboard = self.validate_keyboard("movie")  
                
                if keyboard == 1:
                    
                    try:
                        self.__ui_add_movie()
                    except ValidError as ve:
                        print (str(ve))
                    except RepoError as re:
                        print(str(re))
                        
                elif keyboard == 2:
                    self.__ui_print_customers()
                    print("Introduceti id client pe care doriti sa-l modificati")
                    
                    aux = int(input())
                    
                    self.ui_movie_modify()
                    
                    keyboard = self.validate_keyboard("modify")
                    
                    if keyboard == 1:
                        try:                        
                            self.__ui_modify_movie_by_title(aux)
                        except RepoError as re:
                            print(str(re))
                        except ValidError as ve:
                            print(str(ve))
                    
                    elif keyboard == 2:
                        try:
                            self.__ui_modify_movie_by_genre(aux)
                        except RepoError as re:
                            print(str(re))
                        except ValidError as ve:
                            print(str(ve))
                            
                    elif keyboard == 3:
                        try:
                            self.__ui_modify_movie_by_status(aux)
                        except RepoError as re:
                            print(str(re))
                        except ValidError as ve:
                            print(str(ve))
                        
                    
                elif keyboard == 3:
                    self.__ui_print_movies()
                    try:
                        self.__ui_delete_movie()
                    except RepoError as re:
                        print(str(re))
                        
                elif keyboard == 4:
                
                    self.__ui_print_movies()
            
            elif keyboard == 3:
                
                self.ui_rental_show()
                
                keyboard = self.validate_keyboard("rental")
                
                if keyboard == 1:
                    try:
                        self.__ui_add_rental()
                    except ValidError as ve:
                        print(str(ve))
                    except RepoError as re:
                        print(str(re))
                elif keyboard == 2:
                    try:
                        self.__ui_return_movie()
                    except RepoError as re:
                        print(str(re))
                
                elif keyboard == 3:
                    self.__ui_print_rentals()
            
         
            elif keyboard == 4:
            
                print("1.Genereaza filme")
                print("2.Genereaza clienti")
                
                keyboard = self.validate_keyboard("generate")
                
                if keyboard == 1:
                    nr_filme = int(input("Cate filme sa se genereze"))
                    try:
                        self.__ui_genereaza_filme(nr_filme)
                    except RepoError as re:
                        print(str(re))
                elif keyboard == 2:
                    try:
                        self.__ui_genereaza_clienti()
                    except RepoError as re:
                        print(str(re))    
            
            elif keyboard == 5:
                
                self.ui_search()
                
                keyboard = self.validate_keyboard("search")
                
                if keyboard == 1:
                    try:
                        self.__ui_print_all_movies_same_title()
                    except RepoError as re:
                        print(str(re))
                        
                elif keyboard == 2:
                    try:
                        self.__ui_print_all_movies_same_genre()
                    except RepoError as re:
                        print(str(re))
                
                elif keyboard == 3:
                    try:
                        self.__ui_print_all_movies_same_status()
                    except RepoError as re:
                        print(str(re))
                        
                elif keyboard == 4 :
                    try:
                        self.__ui_print_all_customers_same_name()
                    except RepoError as re:
                        print(str(re))
                    
            elif keyboard == 6:
                
                self.ui_raport_show()
                
                keyboard = self.validate_keyboard("customer")    
                
                if keyboard == 1:
                    
                    print("1.Dupa nume")
                    print("2.Dupa numarul de filme inchiriate(descrescator)")
                    
                    keyboard = self.validate_keyboard("generate")
                    
                    if keyboard == 1:
                        
                        self.__ui_print_customers_with_movies_sortName()
                    
                    if keyboard == 2:
                        
                        self.__ui_print_customers_with_movies_sortOwnedMovies()
                        
                elif keyboard == 2:
                    
                    self.__ui_top_5_rented_movies() 
                    
                elif keyboard == 3:
                    
                    self.__ui_30procent()
                    
                elif keyboard == 4:
                    
                    self.__ui_top_genre()
            elif keyboard == 7:
                break       