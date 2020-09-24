from Domain.Entities import Customer, Movie, Rental
from Validators.Validators import ValidateCustomer, ValidateMovie,\
    ValidateRented
from Erorrs.Exceptions import ValidError, RepoError
from Infrastructure.Repository import CustomerRepository, MovieRepository, RentedRepository,\
    FileRepoCustomer, FileRepoMovie, FileRepoRented
from Business.Controller import CustomerController, MovieController,\
    RentedController
import unittest




class Tests:
    
    def __init__(self):
        pass
    
    def __test_create_customer(self):
        
        cid = 1
        name = "alex"
        cnp = 123456789
        adress = "Miercurea Ciuc"
        
        customer = Customer(cid, name, cnp, adress)
        
        assert(customer.get_name() == "alex")
        assert(customer.get_cid() == 1)
        assert(customer.get_cnp() == 123456789)
        assert(customer.get_adress() == "Miercurea Ciuc")
        
        customer.set_name("George")
        customer.set_adress("Brasov")
        #customer.set_rentedMovies()
        
        assert(customer.get_name() == "George")
        assert(customer.get_adress() == "Brasov")
        
        self.__customer = customer
        self.__other_customer_same_id = Customer(cid,"Mihai",987654321,"Cluj")
        #assert(self.__other_customer_same_id.get_cid() == 1)
        #assert(self.__customer == self.__other_customer_same_id)
        
    def __test_validate_customer(self):
        
        validCustomer = ValidateCustomer()
        
        #self.__customer = Customer(5,"alex",123456789,"miercurea ciuc",["joker","batman"])
        
        validCustomer.validate_customer(self.__customer)
        
        self.__customer_wrong_cid = Customer (-5, "Alex", 123456789, "Miercurea Ciuc")
        self.__customer_wrong_name = Customer (5, "", 123456789, "Miercurea Ciuc")
        self.__customer_wrong_adress = Customer (5, "Alex", 123456789, "")
        self.__customer_wrong_cnp = Customer (5, "Alex", -50231231, "Miercurea Ciuc")
        self.__customer_wrong = Customer (-5, "", -50231231, "")
        
        try:
            validCustomer.validate_customer(self.__customer_wrong_cid)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "id invalid!\n")
        
        try:
            validCustomer.validate_customer(self.__customer_wrong_name)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "nume invalid!\n")
            
        try:
            validCustomer.validate_customer(self.__customer_wrong_adress)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "adresa invalida!\n")
            
        try:
            validCustomer.validate_customer(self.__customer_wrong_cnp)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "cnp invalid!\n")
            
        try:
            validCustomer.validate_customer(self.__customer_wrong)
            assert(False)
        except ValidError as ve :
            assert(str(ve) == "id invalid!\nnume invalid!\ncnp invalid!\nadresa invalida!\n")
        
    def __test_repo_add_search_customer(self):
        self.__repo_customer = CustomerRepository()
        assert(self.__repo_customer.size() == 0)
        self.__repo_customer.add(self.__customer)
        assert(self.__repo_customer.size() == 1)
        customer_key = Customer(self.__customer.get_cid(), None, None, None)
        customerFound = self.__repo_customer.search(customer_key)
        assert(customerFound.get_name()==self.__customer.get_name())
        try:
            self.__repo_customer.add(self.__other_customer_same_id)
            assert(False)
        except RepoError as re:
            assert(str(re) == "id existent!\n")
        self.__inexisting_customer = Customer(13,"Adrian",123456789,"Iasi")
        try:
            self.__repo_customer.search(self.__inexisting_customer)
            assert(False)
        except RepoError as re:
            assert(str(re) == "id inexistent!\n")
    
    def __test_modify_customer_by_name_cnp_adress(self):
        self.__repo_customer = CustomerRepository()
        self.__valid_customer = ValidateCustomer()
        self.__crtlCustomer = CustomerController(self.__valid_customer, self.__repo_customer)
        self.__customer = Customer(1,"Alex",1234,"Miercurea Ciuc")
        self.__repo_customer.add(self.__customer)
        
        self.__crtlCustomer.modify_customer_by_name(self.__customer.get_cid(), "Mircea")
        self.__crtlCustomer.modify_customer_by_cnp(self.__customer.get_cid(), 5678)
        self.__crtlCustomer.modify_customer_by_adress(self.__customer.get_cid(), "Brasov")
        assert(self.__customer.get_name() == "Mircea")
        assert(self.__customer.get_cnp() == 5678)
        assert(self.__customer.get_adress() == "Brasov")
     
    def __test_ctrl_customer_add(self):
        customer_repo = CustomerRepository()
        self.__ctrl_customer = CustomerController(self.__valid_customer, customer_repo)
        assert (self.__ctrl_customer.get_customers_no() == 0)
        self.__ctrl_customer.add_customer(5, "Alex", 1234, "Cluj")
        assert (self.__ctrl_customer.get_customers_no() == 1)
        try:
            self.__ctrl_customer.add_customer(-5, "Alex", 1234, "Cluj")
            assert(False)
        except ValidError as ve:
            assert(str(ve)=="id invalid!\n")
        try:
            self.__ctrl_customer.add_customer(5, "", 1234, "Cluj")
            assert(False)
        except ValidError as ve:
            assert(str(ve) =="nume invalid!\n")
        try:
            self.__ctrl_customer.add_customer(5, "Alex", -2342, "Cluj")
            assert(False)
        except ValidError as ve:
            assert(str(ve) =="cnp invalid!\n")
        try:
            self.__ctrl_customer.add_customer(5, "Alex", 1234, "")
            assert(False)
        except ValidError as ve:
            assert(str(ve) =="adresa invalida!\n")
            
    def __test_create_movie(self):
        
        mid = 2
        title = "Joker"
        genre = "Drama"
        status = "free"
        
        movie = Movie(mid, title, genre, status)
        
        assert(movie.get_mid() == 2)
        assert(movie.get_title() == "Joker")
        assert(movie.get_genre() == "Drama")
        assert(movie.get_status() == "free")
        
        movie.set_title("Fury")
        movie.set_genre("Actiune")
        movie.set_status("rented")
        
        assert (movie.get_title() == "Fury")
        assert (movie.get_genre() == "Actiune")
        assert (movie.get_status() == "rented")
        
        self.__movie = movie
        self.__other_movie_same_id = Movie(mid, "Joker", "Drama", "free")
         
    def __test_validate_movie(self):
        
        validMovie = ValidateMovie()
        
        validMovie.validate_movie(self.__movie)
        
        self.__movie_wrong_id = Movie(-5, "Joker", "Drama", "free")
        self.__movie_wrong_title = Movie(5, "", "Drama", "free")
        self.__movie_wrong_genre = Movie(5, "Joker", "", "free")
        self.__movie_wrong_status = Movie(5, "Joker", "Drama", "freea")
        
        try:
            validMovie.validate_movie(self.__movie_wrong_id)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "id invalid!\n")
            
        try:
            validMovie.validate_movie(self.__movie_wrong_title)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "titlu invalid!\n")
        
        try:
            validMovie.validate_movie(self.__movie_wrong_genre)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "gen invalid!\n")
            
        try:
            validMovie.validate_movie(self.__movie_wrong_status)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "status invalid!\n")
            
    def __test_repo_add_search_movie(self):
        self.__movie_repo = MovieRepository()
        assert(self.__movie_repo.size() == 0)
        self.__movie_repo.add(self.__movie)
        assert(self.__movie_repo.size() == 1)
        movie_key = Movie(self.__movie.get_mid(), None, None, None)
        movie_found = self.__movie_repo.search(movie_key)
        assert(movie_found.get_title() == self.__movie.get_title())
        try:
            self.__movie_repo.add(self.__other_movie_same_id)
            assert(False)
        except RepoError as re:
            assert(str(re) == "id existent!\n")
        self.__inexisting_movie = Movie(13, "Batman", "Aventura", "Free")
        try:
            self.__movie_repo.search(self.__inexisting_movie)
            assert(False)
        except RepoError as re:
            assert(str(re) == "id inexistent!\n")
        
    def __test_modify_movie_by_title_genre_status(self):
        self.__repo_movie = MovieRepository()
        self.__valid_movie = ValidateMovie()
        self.__ctrl_movie = MovieController(self.__valid_movie, self.__repo_movie)
        self.__movie = Movie(1,"Joker","Drama","free")
        self.__repo_movie.add(self.__movie)
        self.__ctrl_movie.modify_movie_by_title(self.__movie.get_mid(), "Batman")
        self.__ctrl_movie.modify_movie_by_genre(self.__movie.get_mid(), "Actiune")
        self.__ctrl_movie.modify_movie_by_status(self.__movie.get_mid(), "rented")
        assert(self.__movie.get_title() == "Batman")
        assert(self.__movie.get_genre() == "Actiune")
        assert(self.__movie.get_status() == "rented")

    def __test_create_rental(self):
        
        mid = 1
        cid = 2
        start_date = "01.10.2019"
        return_date = "01.10.2020"
        
        rental = Rental(mid, cid, start_date, return_date)
        
        assert(rental.get_rented_mid() == 1)
        assert(rental.get_rented_cid() == 2)
        assert(rental.get_start_date() == "01.10.2019")
        assert(rental.get_return_date() == "01.10.2020")
        
        rental.set_start_date("02.11.2019")
        rental.set_return_date("03.11.2020")
        
        assert(rental.get_start_date() == "02.11.2019")
        assert(rental.get_return_date() == "03.11.2020")

        self.__rental = rental
        self.__already_rented_movie = Rental(mid, 3, "13.06.2000", "13.07.2025")

    def __test_validate_rental(self):
        
        validRental = ValidateRented()
        
        validRental.validate_rental(self.__rental)
        
        self.__rental_wrong_sdate = Rental(1,1,"41.10.2019","12.10.2019")
        self.__rental_wrong_rdate = Rental(1,1,"12.10.2019","12.41.2020")
        self.__rental_wrong_srdate = Rental(1,1,"21321414","16.11")
        
        try:
            validRental.validate_rental(self.__rental_wrong_sdate)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "data start invalid!\n")
            
        try:
            validRental.validate_rental(self.__rental_wrong_rdate)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "data return invalid!\n")
            
        try:
            validRental.validate_rental(self.__rental_wrong_srdate)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "data start invalid!\ndata return invalid!\n")
        
    def __test_add_search_rental(self):
        self.__rental_repo = RentedRepository()
        assert(self.__rental_repo.size() == 0)
        self.__rental_repo.add(self.__rental)
        assert(self.__rental_repo.size() == 1)
        rental_key = Rental(self.__rental.get_rented_mid(), None, None, None)
        rental_found = self.__rental_repo.search(rental_key)
        assert(self.__rental.get_rented_mid() == rental_found.get_rented_mid())
        try:
            self.__rental_repo.add(self.__already_rented_movie)
            assert(False)
        except RepoError as re:
            assert(str(re) == "film deja inchiriat!\n")
        self.__not_rented_movie = Rental(13,14,"01.01.2000","01.01.2000")
        try:
            self.__rental_repo.search(self.__not_rented_movie)
            assert(False)
        except RepoError as re:
            assert(str(re) == "filmul nu este inchiriat!\n")
        
    def __test_delete_customer(self):
        self.__customer_repo = CustomerRepository()
        self.__customer_repo.add(self.__customer)
        assert(self.__customer_repo.size() == 1)
        self.__customer_repo.delete(self.__customer)
        assert(self.__customer_repo.size() == 0)
        
    def __test_delete_movie(self):
        self.__movie_repo = MovieRepository()
        self.__movie_repo.add(self.__movie)
        assert(self.__movie_repo.size() == 1)
        self.__movie_repo.delete(self.__movie)
        assert(self.__movie_repo.size() == 0) 
        
    def __test_delete_rental(self):
        self.__rental_repo = RentedRepository()
        self.__rental_repo.add(self.__rental)
        assert(self.__rental_repo.size() == 1)
        self.__rental_repo.delete(self.__rental)
        assert(self.__rental_repo.size() == 0)   
    
    def __test_filerepo_customer_read_write(self):
        
        self.__file_repo_customer = FileRepoCustomer("test.txt", Customer.read_customer, Customer.write_customer)
        
        #assert (self.__file_repo_customer.size() == 6)
        
        #self.__file_repo_customer.__read_all_from_file()
        
    def __test_all_customers_with_movies(self):
        
        valid_rent = ValidateRented()
        
        repo_rent = RentedRepository()
        
        repo_cust = CustomerRepository()
        
        repo_movie = MovieRepository()
        
        movie1 = Movie(1, "Joker", "drama", "free")
        repo_movie.add(movie1)
        movie2 = Movie(2, "Batman", "actiune", "free")
        repo_movie.add(movie2)
        movie3 = Movie(3, "Lion King", "aventura", "free")
        repo_movie.add(movie3)
        movie4 = Movie(4, "Shrek", "comedie", "free")
        repo_movie.add(movie4)
        movie5 = Movie(5, "Titanic", "dragoste", "free")
        repo_movie.add(movie5)
        
        customer1 = Customer(1, "Alex", 12345, "Cluj")
        repo_cust.add(customer1)
        customer2 = Customer(2, "Dan", 12346, "Cluj")
        repo_cust.add(customer2)
        customer3 = Customer(3, "Cristi", 12347, "Cluj")
        repo_cust.add(customer3)
        customer4 = Customer(4, "Ion", 12348, "Cluj")
        repo_cust.add(customer4)
        customer5 = Customer(5, "Alin", 12349, "Cluj")
        repo_cust.add(customer5)
        
  
        
        self.__ctrl_rental = RentedController(valid_rent, repo_rent, repo_cust, repo_movie)
        
        # 1 - Alex
        self.__ctrl_rental.add_rental(1, 1, "1.1.1", "1.1.1")
        
        # 4 - Ion
        self.__ctrl_rental.add_rental(5, 4, "1.1.1", "1.1.1")
        
        # 2 - Dan
        self.__ctrl_rental.add_rental(3, 2, "1.1.1", "1.1.1")
        
        
        
        lista_corecta = self.__ctrl_rental.all_customers_with_movies()
        
        assert (lista_corecta == [customer1, customer2, customer4])
        
    def __test_all_customers_with_more_movies(self):
        
        valid_rent = ValidateRented()
        
        repo_rent = RentedRepository()
        
        repo_cust = CustomerRepository()
        
        repo_movie = MovieRepository()
        
        movie1 = Movie(1, "Joker", "drama", "free")
        repo_movie.add(movie1)
        movie2 = Movie(2, "Batman", "actiune", "free")
        repo_movie.add(movie2)
        movie3 = Movie(3, "Lion King", "aventura", "free")
        repo_movie.add(movie3)
        movie4 = Movie(4, "Shrek", "comedie", "free")
        repo_movie.add(movie4)
        movie5 = Movie(5, "Titanic", "dragoste", "free")
        repo_movie.add(movie5)
        
        customer1 = Customer(1, "Alex", 12345, "Cluj")
        repo_cust.add(customer1)
        customer2 = Customer(2, "Dan", 12346, "Cluj")
        repo_cust.add(customer2)
        customer3 = Customer(3, "Cristi", 12347, "Cluj")
        repo_cust.add(customer3)
        customer4 = Customer(4, "Ion", 12348, "Cluj")
        repo_cust.add(customer4)
        customer5 = Customer(5, "Alin", 12349, "Cluj")
        repo_cust.add(customer5)
        
  
        
        self.__ctrl_rental = RentedController(valid_rent, repo_rent, repo_cust, repo_movie)
        
        # 2 - Dan
        self.__ctrl_rental.add_rental(2, 2, "1.1.1", "1.1.1")
        
        # 1 - Alex
        self.__ctrl_rental.add_rental(1, 1, "1.1.1", "1.1.1")
        
        # 4 - Ion
        self.__ctrl_rental.add_rental(5, 4, "1.1.1", "1.1.1")
        
        # 2 - Dan
        self.__ctrl_rental.add_rental(3, 2, "1.1.1", "1.1.1")
        
       
        
        
        
        lista_corecta = self.__ctrl_rental.all_customrs_with_more_movies()
        
        assert (lista_corecta == [customer2, customer1, customer4])
    
    
    def __test_top_5_rented_movies(self):
        
        valid_rent = ValidateRented()
        
        repo_rent = RentedRepository()
        
        repo_cust = CustomerRepository()
        
        repo_movie = MovieRepository()
        
        self.__ctrl_rental = RentedController(valid_rent, repo_rent, repo_cust, repo_movie)
        
        movie1 = Movie(1, "Joker", "drama", "rented")
        repo_movie.add(movie1)
        movie2 = Movie(2, "Batman", "actiune", "rented")
        repo_movie.add(movie2)
        movie3 = Movie(3, "Lion King", "aventura", "rented")
        repo_movie.add(movie3)
        movie5 = Movie(5, "Titanic", "dragoste", "rented")
        repo_movie.add(movie5)
        movie6 = Movie(6, "Titanic", "dragoste", "rented")
        repo_movie.add(movie6)
        movie7 = Movie(7, "Lion King", "dragoste", "rented")
        repo_movie.add(movie7)
        movie8 = Movie(8, "Titanic", "dragoste", "rented")
        repo_movie.add(movie8)
        
        
        #Titanic - 3
        #Lion king - 2
        #Batman - 1
        #Joker - 1
        
        #print(repo_movie.get_all())
        
        #print(repo_movie.size())
        
        customer1 = Customer(1, "Alex", 12345, "Cluj")
        repo_cust.add(customer1)
        customer2 = Customer(2, "Dan", 12346, "Cluj")
        repo_cust.add(customer2)
        customer3 = Customer(3, "Cristi", 12347, "Cluj")
        repo_cust.add(customer3)
        customer4 = Customer(4, "Ion", 12348, "Cluj")
        repo_cust.add(customer4)
        customer5 = Customer(5, "Alin", 12349, "Cluj")
        repo_cust.add(customer5)
        
        
        lista_corecta = self.__ctrl_rental.top_5_rented_moviesV2()
        
        #print(lista_corecta)
        
         
        assert (lista_corecta == ["Titanic", "Lion King", "Batman", "Joker"]) 
        
    def __test_top_30procent_customers_most_movies(self):
        
        valid_rent = ValidateRented()
        
        repo_rent = RentedRepository()
        
        repo_cust = CustomerRepository()
        
        repo_movie = MovieRepository()
        
        movie1 = Movie(1, "Joker", "drama", "free")
        repo_movie.add(movie1)
        movie2 = Movie(2, "Batman", "actiune", "free")
        repo_movie.add(movie2)
        movie3 = Movie(3, "Lion King", "aventura", "free")
        repo_movie.add(movie3)
        movie4 = Movie(4, "Shrek", "comedie", "free")
        repo_movie.add(movie4)
        movie5 = Movie(5, "Titanic", "dragoste", "free")
        repo_movie.add(movie5)
        movie6 = Movie(6, "Titanic", "dragoste", "free")
        repo_movie.add(movie6)
        movie7 = Movie(7, "Lion King", "dragoste", "free")
        repo_movie.add(movie7)
        movie8 = Movie(8, "Titanic", "dragoste", "free")
        repo_movie.add(movie8)
        
        #print(repo_movie.get_all())
        
        #print(repo_movie.size())
        
        customer1 = Customer(1, "Alex", 12345, "Cluj")
        repo_cust.add(customer1)
        customer2 = Customer(2, "Dan", 12346, "Cluj")
        repo_cust.add(customer2)
        customer3 = Customer(3, "Cristi", 12347, "Cluj")
        repo_cust.add(customer3)
        customer4 = Customer(4, "Ion", 12348, "Cluj")
        repo_cust.add(customer4)
        customer5 = Customer(5, "Alin", 12349, "Cluj")
        repo_cust.add(customer5)
        
  
        
        self.__ctrl_rental = RentedController(valid_rent, repo_rent, repo_cust, repo_movie)
        
        # 2 - Dan , 8 - Titanic
        self.__ctrl_rental.add_rental(8, 2, "1.1.1", "1.1.1")
        
        # 1 - Alex , 7 - Lion king
        self.__ctrl_rental.add_rental(7, 1, "1.1.1", "1.1.1")
        
        # 4 - Ion , 6 - Titanic
        self.__ctrl_rental.add_rental(6, 4, "1.1.1", "1.1.1")
        
        # 2 - Dan , 3 - Lion King
        self.__ctrl_rental.add_rental(3, 2, "1.1.1", "1.1.1")
        
        # 5 - Titanic
        self.__ctrl_rental.add_rental(5, 2, "1.1.1", "1.1.1")
        
        # 2 - Batman
        self.__ctrl_rental.add_rental(2, 2, "1.1.1", "1.1.1")
        
        
        
        lista_corecta = self.__ctrl_rental.top_5_rented_movies()
        
         
        assert (lista_corecta == ["Titanic", "Lion King", "Batman"])
          
    def run_all_tests(self):
        self.__test_create_customer()
        self.__test_validate_customer()
        self.__test_repo_add_search_customer()
        self.__test_modify_customer_by_name_cnp_adress()
        self.__test_create_movie()
        self.__test_validate_movie()
        self.__test_repo_add_search_movie()
        self.__test_modify_movie_by_title_genre_status()
        self.__test_create_rental()
        self.__test_validate_rental()
        self.__test_add_search_rental()
        self.__test_delete_customer()
        self.__test_delete_movie()
        self.__test_delete_rental()
        self.__test_ctrl_customer_add()
        self.__test_filerepo_customer_read_write()
        self.__test_all_customers_with_movies()
        self.__test_all_customers_with_more_movies()
        self.__test_top_5_rented_movies()
        
class TestCaseMovieController(unittest.TestCase):
    
    def setUp(self):
        validMovie = ValidateMovie()
        self.repoMovie = MovieRepository()
        self.ctrlMovie = MovieController(validMovie, self.repoMovie)
        
    def tearDown(self):
        pass
        
    def testAdd(self):
        self.ctrlMovie.add_movie(1, "Joker", "Drama", "free")
        
        self.assertTrue(self.ctrlMovie.get_NoMovies() == 1)
        #test for invalid movie
        self.assertRaises(ValidError, self.ctrlMovie.add_movie ,-1, "", "", "")
        #test for duplicate id
        self.assertRaises(RepoError, self.ctrlMovie.add_movie,1, "Batman", "Drama", "free")
        
    def testRemove(self):
        self.ctrlMovie.add_movie(2, "Shrek", "Comedy", "free")
        
        self.assertTrue(self.ctrlMovie.get_NoMovies() == 1)
        
        self.ctrlMovie.remove_movie(2)
        
        self.assertTrue(self.ctrlMovie.get_NoMovies() == 0)
        
        self.assertRaises(RepoError, self.ctrlMovie.remove_movie,3)
     
    def testModifyTitle(self):
        movie = Movie(4, "Lion King", "Aventura", "free")
        
        self.repoMovie.add(movie)
        
        self.assertTrue(movie.get_title() == "Lion King")
        
        self.ctrlMovie.modify_movie_by_title(4, "Indiana Jones")
        
        self.assertTrue(movie.get_title() == "Indiana Jones")
        
        self.assertRaises(RepoError, self.ctrlMovie.modify_movie_by_title ,5 , "Indiana Jones")
    
    def testModifyGenre(self):
        movie = Movie(4, "Lion King", "Aventura", "free")
        
        self.repoMovie.add(movie)
        
        self.assertTrue(movie.get_genre() == "Aventura")
        
        self.ctrlMovie.modify_movie_by_genre(4, "Drama")
        
        self.assertTrue(movie.get_genre() == "Drama")
        
        self.assertRaises(RepoError, self.ctrlMovie.modify_movie_by_genre, 5 , "Drama")
        
    def testModifyStatus(self):
        movie = Movie(4, "Lion King", "Aventura", "free")
        
        self.repoMovie.add(movie)
        
        self.assertTrue(movie.get_status() == "free")
        
        self.ctrlMovie.modify_movie_by_status(4, "rented")
        
        self.assertTrue(movie.get_status() == "rented")
        
        self.assertRaises(RepoError, self.ctrlMovie.modify_movie_by_status, 5, "rented")
        
    def testAllMoviesSameTitle(self):
        
        self.ctrlMovie.add_movie(7, "Titanic", "Comedy", "free")
        
        self.ctrlMovie.add_movie(8, "Shrek", "Comedy", "free")
        
        self.ctrlMovie.add_movie(9, "Titanic", "Comedy", "free")
        
        self.ctrlMovie.add_movie(10, "Shrek", "Comedy", "free")
        
        self.ctrlMovie.add_movie(11, "Titanic", "Comedy", "free")
        
        #self.assertTrue(self.ctrlMovie.all_movies_same_title("Titanic") == [Movie(7, "Titanic", "Comedy", "free"), Movie(7, "Titanic", "Comedy", "free"), Movie(11, "Titanic", "Comedy", "free")])
         
        lista = self.ctrlMovie.all_movies_same_title("Titanic")
        
        self.assertTrue(len(lista) == 3)
        
        self.assertTrue(lista[0].get_mid() == 7)
        
        self.assertTrue(lista[1].get_mid() == 9)
        
        self.assertTrue(lista[2].get_mid() == 11)
        
        self.assertTrue(lista[0].get_title() == "Titanic")
        
        self.assertTrue(lista[1].get_title() == "Titanic")
        
        self.assertTrue(lista[2].get_title() == "Titanic")
        
    def testAllMoviesSameGenre(self):
        
        self.ctrlMovie.add_movie(7, "Titanic", "Comedy", "free")
        
        self.ctrlMovie.add_movie(8, "Shrek", "Drama", "free")
        
        self.ctrlMovie.add_movie(9, "Titanic", "Comedy", "free")
        
        self.ctrlMovie.add_movie(10, "Shrek", "Comedy", "free")
        
        self.ctrlMovie.add_movie(11, "Titanic", "Drama", "free")
        
        #self.assertTrue(self.ctrlMovie.all_movies_same_title("Titanic") == [Movie(7, "Titanic", "Comedy", "free"), Movie(7, "Titanic", "Comedy", "free"), Movie(11, "Titanic", "Comedy", "free")])
         
        lista = self.ctrlMovie.all_movie_same_genre("Drama")
        
        self.assertTrue(len(lista) == 2)
        
        self.assertTrue(lista[0].get_mid() == 8)
        
        self.assertTrue(lista[1].get_mid() == 11)
        
        self.assertTrue(lista[0].get_genre() == "Drama")
        
        self.assertTrue(lista[1].get_genre() == "Drama")
        
    def testAllMoviesSameStatus(self):
        
        self.ctrlMovie.add_movie(7, "Titanic", "Comedy", "free")
        
        self.ctrlMovie.add_movie(8, "Shrek", "Drama", "free")
        
        self.ctrlMovie.add_movie(9, "Titanic", "Comedy", "rented")
        
        self.ctrlMovie.add_movie(10, "Shrek", "Comedy", "rented")
        
        self.ctrlMovie.add_movie(11, "Titanic", "Drama", "free")
        
        #self.assertTrue(self.ctrlMovie.all_movies_same_title("Titanic") == [Movie(7, "Titanic", "Comedy", "free"), Movie(7, "Titanic", "Comedy", "free"), Movie(11, "Titanic", "Comedy", "free")])
         
        lista = self.ctrlMovie.all_movies_same_status("rented")
        
        self.assertTrue(len(lista) == 2)
        
        self.assertTrue(lista[0].get_mid() == 9)
        
        self.assertTrue(lista[1].get_mid() == 10)
        
        self.assertTrue(lista[0].get_status() == "rented")
        
        self.assertTrue(lista[1].get_status() == "rented")

class TestCaseMovieRepository(unittest.TestCase):
    
    def setUp(self):
        self.repoMovie = MovieRepository()
        
    def tearDown(self):
        pass
    
    def testAdd(self):
        
        movie = Movie(1, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie)
        
        self.assertTrue(self.repoMovie.size() == 1)
        
        self.assertRaises(RepoError, self.repoMovie.add, movie)
        
    def testGetAll(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista == [movie2, movie3])
    
    def testSize(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        self.assertTrue(self.repoMovie.size() == 2)
        
    def testSearch(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Drama", "free")
        
        self.assertTrue(self.repoMovie.search(movie3) == movie3)
        
        self.assertRaises(RepoError, self.repoMovie.search, movie4)
    
    def testDelete(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie4)
        
        self.assertTrue(self.repoMovie.size() == 3)
        
        self.repoMovie.delete(movie3)
        
        self.assertTrue(self.repoMovie.size() == 2)
        
        self.assertRaises(RepoError , self.repoMovie.search, movie3)
        
    def testModifyTitle(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_title() == "Joker")
        
        self.repoMovie.modify_title(lista[0], "Batman")
        
        self.assertTrue(lista[0].get_title() == "Batman")
        
        self.assertRaises(RepoError, self.repoMovie.modify_title, movie3, "Batman")
        
    def testModifyGenre(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_genre() == "Drama")
        
        self.repoMovie.modify_genre(lista[0], "Comedie")
        
        self.assertTrue(lista[0].get_genre() == "Comedie")
        
        self.assertRaises(RepoError, self.repoMovie.modify_genre, movie3, "Batman")
        
    def testModifyStatus(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_status() == "free")
        
        self.repoMovie.modify_status(lista[0], "rented")
        
        self.assertTrue(lista[0].get_status() == "rented")
        
        self.assertRaises(RepoError, self.repoMovie.modify_status, movie3, "Batman")
        
    def testGetAllMoviesSameTitle(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie4)
        
        movie5 = Movie(5, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie5)
        
        movie6 = Movie(6, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie6)
        
        movie7 = Movie(7, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie7)
        
        lista = self.repoMovie.get_all_movies_same_title(movie3)
        
        self.assertTrue(len(lista) == 3)
        
    def testGetAllMoviesSameGenre(self):
        
        movie2 = Movie(2, "Joker", "Comedy", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Comedy", "free")
        
        self.repoMovie.add(movie4)
        
        movie5 = Movie(5, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie5)
        
        movie6 = Movie(6, "Joker", "Comedy", "free")
        
        self.repoMovie.add(movie6)
        
        movie7 = Movie(7, "Lion King", "Comedy", "free")
        
        self.repoMovie.add(movie7)
        
        lista = self.repoMovie.get_all_movies_same_genre(movie7)
        
        self.assertTrue(len(lista) == 4)
        
    def getAllMoviesSameStatus(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Drama", "rented")
        
        self.repoMovie.add(movie4)
        
        movie5 = Movie(5, "Lion King", "Drama", "rented")
        
        self.repoMovie.add(movie5)
        
        movie6 = Movie(6, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie6)
        
        movie7 = Movie(7, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie7)
        
        lista = self.repoMovie.get_all_movies_same_status(movie5)
        
        self.assertTrue(len(lista) == 2) 
        
class TestCaseMovieValidator(unittest.TestCase):
    
    def setUp(self):
         
        self.validMovie = ValidateMovie()
         
    def tearDown(self):
        pass
    
    def testValidateCustomer(self):
        
        self.assertRaises(ValidError, self.validMovie.validate_movie, Movie(-1, "Joker", "Drama", "free"))
    
        self.assertRaises(ValidError, self.validMovie.validate_movie, Movie(1, "", "Drama", "free"))
        
        self.assertRaises(ValidError, self.validMovie.validate_movie, Movie(1, "Joker", "", "free"))
        
        self.assertRaises(ValidError, self.validMovie.validate_movie, Movie(1, "Joker", "Drama", "freee"))
        
        self.validMovie.validate_movie(Movie(1,"Joker", "Drama", "free"))
        
class TestCaseCustomerRepository(unittest.TestCase):
    
    def setUp(self):
        
        self.custRepo = CustomerRepository()
    
    def tearDown(self):
        pass 
    
    def testAdd(self):
        
        customer = Customer(1, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(customer)
        
        self.assertTrue(self.custRepo.size() == 1)
        
        self.assertRaises(RepoError, self.custRepo.add, customer)
        
    def testGetAll(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust3)
        
        self.assertTrue(self.custRepo.get_all() == [cust2, cust3])
        
    def testSearch(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust3)
        
        cust4 = Customer(4, "Alex", 123456789, "Cluj")
        
        self.assertTrue(self.custRepo.search(cust3) == cust3)
        
        self.assertRaises(RepoError, self.custRepo.search, cust4)
        
    def testDelete(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust3)
        
        cust4 = Customer(4, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust4)
        
        self.assertTrue(self.custRepo.size() == 3)
        
        self.custRepo.delete(cust3)
        
        self.assertTrue(self.custRepo.size() == 2)
        
        self.assertRaises(RepoError, self.custRepo.search, cust3)
        
    def testModifyName(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_name() == "Alex")
        
        self.custRepo.modify_name(lista[0], "Mircea")
        
        self.assertTrue(lista[0].get_name() == "Mircea")
        
        self.assertRaises(RepoError, self.custRepo.modify_name, cust3, "COCO")
        
    def testModifyCNP(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_cnp() == 123456789)
        
        self.custRepo.modify_cnp(lista[0], 987654321)
        
        self.assertTrue(lista[0].get_cnp() == 987654321)
        
        self.assertRaises(RepoError, self.custRepo.modify_cnp, cust3, 42069)
        
    def testModifyAdress(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_adress() == "Cluj")
        
        self.custRepo.modify_adress(lista[0], "Brasov")
        
        self.assertTrue(lista[0].get_adress() == "Brasov")
        
        self.assertRaises(RepoError, self.custRepo.modify_adress, cust3, "Holulu")
        
    def testGetAllCustomersSameName(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Mircea", 123456789, "Cluj")
        
        self.custRepo.add(cust3)
        
        cust4 = Customer(4, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust4)
        
        cust5 = Customer(5, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust5)
        
        cust6 = Customer(6, "Mircea", 123456789, "Cluj")
        
        self.custRepo.add(cust6)
        
        cust7 = Customer(7, "Johnny", 123456789, "Cluj")
         
        lista = self.custRepo.get_all_customers_same_name(cust6)
        
        self.assertTrue(len(lista) == 2)
        
        self.assertTrue(lista[0].get_cid() == 3)
        
        self.assertTrue(lista[1].get_cid() == 6)
        
        self.assertRaises(RepoError, self.custRepo.get_all_customers_same_name, cust7)
    
class TestCaseValidateCustomer(unittest.TestCase):
    
    def setUp(self):
        
        self.validCust = ValidateCustomer()
        
    def tearDown(self):
        pass
    
    def testValidateCustomer(self):
        
        self.assertRaises(ValidError, self.validCust.validate_customer, Customer(-1, "Alex", 123456789, "Cluj"))
        self.assertRaises(ValidError, self.validCust.validate_customer, Customer(1, "", 123456789, "Cluj"))
        self.assertRaises(ValidError, self.validCust.validate_customer, Customer(1, "Alex", -123456789, "Cluj"))
        self.assertRaises(ValidError, self.validCust.validate_customer, Customer(1, "Alex", 123456789, ""))  
        self.validCust.validate_customer(Customer(1, "Alex", 123456789, "Cluj"))  
        
class TestCaseCustomerController(unittest.TestCase):
    
    def setUp(self):
        
        validCust = ValidateCustomer()
        self.repoCust = CustomerRepository()
        self.ctrlCust = CustomerController(validCust, self.repoCust)
        
    def tearDown(self):
        pass
    
    def testAddCustomer(self):
        
        self.assertTrue(self.repoCust.size() == 0)
        
        self.ctrlCust.add_customer(1, "alex", 12345, "cluj")
        
        self.assertTrue(self.repoCust.size() == 1)
        
        self.assertRaises(RepoError, self.ctrlCust.add_customer, 1, "g", 123, "honolulu")
        
        self.assertRaises(ValidError, self.ctrlCust.add_customer, -1, "g", 123, "")
        
    def testGetCustomers(self):
        
        self.ctrlCust.add_customer(1, "alex", 12345, "cluj")
        
        self.ctrlCust.add_customer(2, "dan", 12345, "brasov")
        
        self.ctrlCust.add_customer(3, "cristi", 12345, "mciuc")
        
        lista = self.ctrlCust.get_customers()
        
        self.assertTrue(len(lista) == 3)
        
    def testModifyCustomerByName(self):
        
        self.ctrlCust.add_customer(1, "alex", 12345, "cluj")
        
        lista = self.ctrlCust.get_customers()
        
        self.assertTrue(lista[0].get_name() == "alex")
        
        self.ctrlCust.modify_customer_by_name(1, "dan")
        
        self.assertTrue(lista[0].get_name() == "dan")
        
        self.assertRaises(ValidError, self.ctrlCust.modify_customer_by_name, 1, "")
        
        self.assertRaises(RepoError, self.ctrlCust.modify_customer_by_name, 2, "boss")
        
    def testModifyCustomerByCNP(self):
        
        self.ctrlCust.add_customer(1, "alex", 12345, "cluj")
        
        lista = self.ctrlCust.get_customers()
        
        self.assertTrue(lista[0].get_cnp() == 12345)
        
        self.ctrlCust.modify_customer_by_cnp(1, 54321)
        
        self.assertTrue(lista[0].get_cnp() == 54321)
        
        self.assertRaises(ValidError, self.ctrlCust.modify_customer_by_cnp, 1, -54321)
        
        self.assertRaises(RepoError, self.ctrlCust.modify_customer_by_cnp, 2, 67890)
        
    def testModifyCustomerByAdress(self):
        
        self.ctrlCust.add_customer(1, "alex", 12345, "cluj")
        
        lista = self.ctrlCust.get_customers()
        
        self.assertTrue(lista[0].get_adress() == "cluj")
        
        self.ctrlCust.modify_customer_by_adress(1, "brasov")
        
        self.assertTrue(lista[0].get_adress() == "brasov")
        
        self.assertRaises(ValidError, self.ctrlCust.modify_customer_by_name, 1, "")
        
        self.assertRaises(RepoError, self.ctrlCust.modify_customer_by_name, 2, "boss")
        
    def testRemoveCustomer(self):
        
        self.ctrlCust.add_customer(1, "alex", 12345, "cluj")
        
        self.ctrlCust.add_customer(2, "alex", 12345, "cluj")
        
        self.assertTrue(self.repoCust.size() == 2)
                        
        self.ctrlCust.remove_customer(2)
        
        self.assertTrue(self.repoCust.size() == 1)
        
        self.assertRaises(RepoError, self.ctrlCust.remove_customer, 2)
        
    def testSearchCustomerByName(self):
        
        self.ctrlCust.add_customer(1, "alex", 12345, "cluj")
        
        self.ctrlCust.add_customer(2, "boss", 12345, "cluj")
        
        self.ctrlCust.add_customer(3, "alex", 12345, "cluj")
        
        self.ctrlCust.add_customer(4, "boss", 12345, "cluj")
        
        self.ctrlCust.add_customer(5, "boss", 12345, "cluj")
        
        self.ctrlCust.add_customer(6, "alex", 12345, "cluj")
        
        lista = self.ctrlCust.search_customer_by_name("boss")
        
        self.assertTrue(len(lista) == 3)
        
        self.assertTrue(lista[0].get_cid() == 2)
        
        self.assertTrue(lista[1].get_cid() == 4)
        
        self.assertTrue(lista[2].get_cid() == 5)
        
        self.assertRaises(RepoError, self.ctrlCust.search_customer_by_name, "joker")
        
class TestCaseRentedRepository(unittest.TestCase):
    
    def setUp(self):
        
        self.repoRented = RentedRepository() 
        
    def tearDown(self):
        pass
    
    def testAdd(self):
        
        rental = Rental(1, 1, "1.1.1", "1.1.1")
        
        self.assertTrue(self.repoRented.size() == 0)
        
        self.repoRented.add(rental)   
    
        self.assertTrue(self.repoRented.size() == 1)
        
        self.assertRaises(RepoError, self.repoRented.add, rental)
        
    def testSearch(self):
        
        rental = Rental(1, 1, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental)   
        
        rental2 = Rental(2, 2, "1.1.1", "1.1.1")   
    
        rental3 = Rental(3, 3, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental3)   
        
        self.assertTrue(self.repoRented.search(rental3) == rental3)
        
        self.assertRaises(RepoError, self.repoRented.search, rental2)
        
    def testGetAll(self):
        
        rental = Rental(1, 1, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental)   
        
        rental2 = Rental(2, 2, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental2)   
    
        rental3 = Rental(3, 3, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental3)   
        
        lista = self.repoRented.get_all()
    
        self.assertTrue(len(lista) == 3)
        
        self.assertTrue(lista[1].get_rented_mid() == 2)
        
        self.assertTrue(lista[1].get_rented_cid() == 2)
        
    def testDelete(self):
    
        rental = Rental(1, 1, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental)   
        
        rental2 = Rental(2, 2, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental2)   
    
        rental3 = Rental(3, 3, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental3)   
        
        self.assertTrue(self.repoRented.size() == 3)
        
        self.repoRented.delete(rental2)
        
        self.assertTrue(self.repoRented.size() == 2)
        
        self.assertRaises(RepoError, self.repoRented.search, rental2)
        
        self.assertRaises(RepoError, self.repoRented.delete, rental2)
        
class TestCaseValidateRented(unittest.TestCase):
    
    def setUp(self):
        
        self.validRented = ValidateRented()
    
    def tearDown(self):
        pass
    
    def testValidateRental(self):
        
        self.assertRaises(ValidError, self.validRented.validate_rental, Rental(1,1,"20.09", "1.1.1"))
        self.assertRaises(ValidError, self.validRented.validate_rental, Rental(1,1,"1.1.1","20.09"))
        self.assertRaises(ValidError, self.validRented.validate_rental, Rental(1,1,"1.1.1", "32.13.2000"))
        self.assertRaises(ValidError, self.validRented.validate_rental, Rental(1,1,"20.09.2000", ""))
        self.validRented.validate_rental(Rental(1,1,"1.1.1", "1.11.1"))
        
class TestCaseRentedCotroller(unittest.TestCase):
    
    def setUp(self):
        validRented = ValidateRented()
        self.repoRented = RentedRepository()
        self.repoCust = CustomerRepository()
        self.repoMovie = MovieRepository()
        self.ctrlRented = RentedController(validRented, self.repoRented, self.repoCust, self.repoMovie)
        
    def tearDown(self):
        pass
    
    def testAddRental(self):
        
        cust1 = Customer(1, "alex", 12345, "cluj")
        
        self.repoCust.add(cust1)
        
        cust2 = Customer(2, "alex", 12345, "cluj")
        
        self.repoCust.add(cust2)
        
        cust3 = Customer(3, "alex", 12345, "cluj")
        
        self.repoCust.add(cust3)
        
        movie1 = Movie(1, "joker", "drama", "free")
        
        self.repoMovie.add(movie1)
        
        movie2 = Movie(2, "joker", "drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "joker", "drama", "free")
        
        self.repoMovie.add(movie3)
        
        self.assertTrue(self.repoRented.size() == 0)
        
        self.ctrlRented.add_rental(1, 2, "1.1.1", "1.1.1")
        
        self.assertTrue(self.repoRented.size() == 1)
        
        self.assertRaises(RepoError, self.ctrlRented.add_rental, 1, 3, "1.1.1", "1.1.1")
        self.assertRaises(RepoError, self.ctrlRented.add_rental, 2, 4, "1.1.1", "1.1.1")
        self.assertRaises(RepoError, self.ctrlRented.add_rental, 4, 3, "1.1.1", "1.1.1")
        self.assertRaises(ValidError, self.ctrlRented.add_rental, 1, 3, "11.1", "1.1.1")
        
    def testReturnMovie(self):
        
        cust1 = Customer(1, "alex", 12345, "cluj")
        
        self.repoCust.add(cust1)
        
        cust2 = Customer(2, "alex", 12345, "cluj")
        
        self.repoCust.add(cust2)
        
        cust3 = Customer(3, "alex", 12345, "cluj")
        
        self.repoCust.add(cust3)
        
        movie1 = Movie(1, "joker", "drama", "free")
        
        self.repoMovie.add(movie1)
        
        movie2 = Movie(2, "joker", "drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "joker", "drama", "free")
        
        self.repoMovie.add(movie3)
        
        self.ctrlRented.add_rental(1, 2, "1.1.1", "1.1.1")
        self.ctrlRented.add_rental(3, 2, "1.1.1", "1.1.1")
        self.assertTrue(self.repoRented.size() == 2)
        self.ctrlRented.return_movie(3)
        self.assertTrue(self.repoRented.size() == 1)
        self.assertRaises(RepoError, self.repoRented.search, Rental(3,2,"1.1.1", "1.1.1"))
    
    def testGetRentals(self):
        
        cust1 = Customer(1, "alex", 12345, "cluj")
        
        self.repoCust.add(cust1)
        
        cust2 = Customer(2, "alex", 12345, "cluj")
        
        self.repoCust.add(cust2)
        
        cust3 = Customer(3, "alex", 12345, "cluj")
        
        self.repoCust.add(cust3)
        
        movie1 = Movie(1, "joker", "drama", "free")
        
        self.repoMovie.add(movie1)
        
        movie2 = Movie(2, "joker", "drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "joker", "drama", "free")
        
        self.repoMovie.add(movie3)
        
        self.ctrlRented.add_rental(1, 2, "1.1.1", "1.1.1")
        self.ctrlRented.add_rental(3, 2, "1.1.1", "1.1.1")
        
        lista = self.ctrlRented.get_rentals()
        
        self.assertTrue(len(lista) == 2)
        self.assertTrue(lista[0].get_rented_mid() == 1)
        self.assertTrue(lista[1].get_rented_mid() == 3)
        
    def testAllCustomersWithMovies(self):
        movie1 = Movie(1, "Joker", "drama", "free")
        self.repoMovie.add(movie1)
        movie2 = Movie(2, "Batman", "actiune", "free")
        self.repoMovie.add(movie2)
        movie3 = Movie(3, "Lion King", "aventura", "free")
        self.repoMovie.add(movie3)
        movie4 = Movie(4, "Shrek", "comedie", "free")
        self.repoMovie.add(movie4)
        movie5 = Movie(5, "Titanic", "dragoste", "free")
        self.repoMovie.add(movie5)
        
        customer1 = Customer(1, "Alex", 12345, "Cluj")
        self.repoCust.add(customer1)
        customer2 = Customer(2, "Dan", 12346, "Cluj")
        self.repoCust.add(customer2)
        customer3 = Customer(3, "Cristi", 12347, "Cluj")
        self.repoCust.add(customer3)
        customer4 = Customer(4, "Ion", 12348, "Cluj")
        self.repoCust.add(customer4)
        customer5 = Customer(5, "Alin", 12349, "Cluj")
        self.repoCust.add(customer5)
        
        # 1 - Alex
        self.ctrlRented.add_rental(1, 1, "1.1.1", "1.1.1")
        
        # 4 - Ion
        self.ctrlRented.add_rental(5, 4, "1.1.1", "1.1.1")
        
        # 2 - Dan
        self.ctrlRented.add_rental(3, 2, "1.1.1", "1.1.1")
        
        lista_corecta = self.ctrlRented.all_customers_with_movies()
        
        assert (lista_corecta == [customer1, customer2, customer4])
        
    def testAllCustomersWithMoreMovies(self):
        
        movie1 = Movie(1, "Joker", "drama", "free")
        self.repoMovie.add(movie1)
        movie2 = Movie(2, "Batman", "actiune", "free")
        self.repoMovie.add(movie2)
        movie3 = Movie(3, "Lion King", "aventura", "free")
        self.repoMovie.add(movie3)
        movie4 = Movie(4, "Shrek", "comedie", "free")
        self.repoMovie.add(movie4)
        movie5 = Movie(5, "Titanic", "dragoste", "free")
        self.repoMovie.add(movie5)
        
        customer1 = Customer(1, "Alex", 12345, "Cluj")
        self.repoCust.add(customer1)
        customer2 = Customer(2, "Dan", 12346, "Cluj")
        self.repoCust.add(customer2)
        customer3 = Customer(3, "Cristi", 12347, "Cluj")
        self.repoCust.add(customer3)
        customer4 = Customer(4, "Ion", 12348, "Cluj")
        self.repoCust.add(customer4)
        customer5 = Customer(5, "Alin", 12349, "Cluj")
        self.repoCust.add(customer5)
        
        # 2 - Dan
        self.ctrlRented.add_rental(2, 2, "1.1.1", "1.1.1")
        
        # 1 - Alex
        self.ctrlRented.add_rental(1, 1, "1.1.1", "1.1.1")
        
        # 4 - Ion
        self.ctrlRented.add_rental(5, 4, "1.1.1", "1.1.1")
        
        # 2 - Dan
        self.ctrlRented.add_rental(3, 2, "1.1.1", "1.1.1")
        
        lista_corecta = self.ctrlRented.all_customrs_with_more_movies()
        
        assert (lista_corecta == [customer2, customer4, customer1])
        
    def testTop5RentedMovies(self):
        
        movie1 = Movie(1, "Joker", "drama", "rented")
        self.repoMovie.add(movie1)
        movie2 = Movie(2, "Batman", "actiune", "rented")
        self.repoMovie.add(movie2)
        movie3 = Movie(3, "Lion King", "aventura", "rented")
        self.repoMovie.add(movie3)
        movie5 = Movie(5, "Titanic", "dragoste", "rented")
        self.repoMovie.add(movie5)
        movie6 = Movie(6, "Titanic", "dragoste", "rented")
        self.repoMovie.add(movie6)
        movie7 = Movie(7, "Lion King", "dragoste", "rented")
        self.repoMovie.add(movie7)
        movie8 = Movie(8, "Titanic", "dragoste", "rented")
        self.repoMovie.add(movie8)
        
        customer1 = Customer(1, "Alex", 12345, "Cluj")
        self.repoCust.add(customer1)
        customer2 = Customer(2, "Dan", 12346, "Cluj")
        self.repoCust.add(customer2)
        customer3 = Customer(3, "Cristi", 12347, "Cluj")
        self.repoCust.add(customer3)
        customer4 = Customer(4, "Ion", 12348, "Cluj")
        self.repoCust.add(customer4)
        customer5 = Customer(5, "Alin", 12349, "Cluj")
        self.repoCust.add(customer5)
        
        
        lista_corecta = self.ctrlRented.top_5_rented_movies()
         
        assert (lista_corecta == ["Titanic", "Lion King", "Joker", "Batman"]) 
        
    def testTop30ProcentCustomersMostMovies(self):
        
         
        movie1 = Movie(1, "Joker", "drama", "rented")
        self.repoMovie.add(movie1)
        movie2 = Movie(2, "Batman", "actiune", "rented")
        self.repoMovie.add(movie2)
        movie3 = Movie(3, "Lion King", "aventura", "rented")
        self.repoMovie.add(movie3)
        movie5 = Movie(5, "Titanic", "dragoste", "rented")
        self.repoMovie.add(movie5)
        movie6 = Movie(6, "Titanic", "dragoste", "rented")
        self.repoMovie.add(movie6)
        movie7 = Movie(7, "Lion King", "dragoste", "rented")
        self.repoMovie.add(movie7)
        movie8 = Movie(8, "Titanic", "dragoste", "rented")
        self.repoMovie.add(movie8)
        
        customer1 = Customer(1, "Alex", 12345, "Cluj")
        self.repoCust.add(customer1)
        customer2 = Customer(2, "Dan", 12346, "Cluj")
        self.repoCust.add(customer2)
        customer3 = Customer(3, "Cristi", 12347, "Cluj")
        self.repoCust.add(customer3)
        customer4 = Customer(4, "Ion", 12348, "Cluj")
        self.repoCust.add(customer4)
        customer5 = Customer(5, "Alin", 12349, "Cluj")
        self.repoCust.add(customer5)
        
        
        lista_corecta = self.ctrlRented.top_5_rented_movies()
         
        assert (lista_corecta == ["Titanic", "Lion King", "Joker", "Batman"]) 
        
class TestCaseFileRepoCustomer(unittest.TestCase):
    
    def setUp(self):
        
        self.custRepo = FileRepoCustomer("testcustomer.txt", Customer.read_customer, Customer.write_customer)
    
    def tearDown(self):
        pass 
    
    def testAdd(self):
        
        customer = Customer(1, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(customer)
        
        self.assertTrue(self.custRepo.size() == 1)
        
        self.assertRaises(RepoError, self.custRepo.add, customer)
        
        open('testcustomer.txt', 'w').close()

       
    def testGetAll(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust3)
        
        self.assertTrue(self.custRepo.get_all() == [cust2, cust3])
        
        open('testcustomer.txt', 'w').close()
    
       
    def testSearch(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust3)
        
        cust4 = Customer(4, "Alex", 123456789, "Cluj")
        
        self.assertTrue(self.custRepo.search(cust3) == cust3)
        
        self.assertRaises(RepoError, self.custRepo.search, cust4)
        
        open('testcustomer.txt', 'w').close()
        
    
        
    def testDelete(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust3)
        
        cust4 = Customer(4, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust4)
        
        self.assertTrue(self.custRepo.size() == 3)
        
        self.custRepo.delete(cust3)
        
        self.assertTrue(self.custRepo.size() == 2)
        
        self.assertRaises(RepoError, self.custRepo.search, cust3)
        
        open('testcustomer.txt', 'w').close()
     
    def testModifyName(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_name() == "Alex")
        
        self.custRepo.modify_name(lista[0], "Mircea")
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_name() == "Mircea")
        
        self.assertRaises(RepoError, self.custRepo.modify_name, cust3, "COCO")
        
        f = open('testcustomer.txt', 'r+')
        f.truncate(0)
        f.close()
    
    def testModifyCNP(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_cnp() == 123456789)
        
        self.custRepo.modify_cnp(lista[0], 987654321)
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_cnp() == 987654321)
        
        self.assertRaises(RepoError, self.custRepo.modify_cnp, cust3, 42069)
        
        open('testcustomer.txt', 'w').close()
        
    def testModifyAdress(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Alex", 123456789, "Cluj")
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_adress() == "Cluj")
        
        self.custRepo.modify_adress(lista[0], "Brasov")
        
        lista = self.custRepo.get_all()
        
        self.assertTrue(lista[0].get_adress() == "Brasov")
        
        self.assertRaises(RepoError, self.custRepo.modify_adress, cust3, "Holulu")
        
        open('testcustomer.txt', 'w').close()
     
     
    def testGetAllCustomersSameName(self):
        
        cust2 = Customer(2, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust2)
        
        cust3 = Customer(3, "Mircea", 123456789, "Cluj")
        
        self.custRepo.add(cust3)
        
        cust4 = Customer(4, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust4)
        
        cust5 = Customer(5, "Alex", 123456789, "Cluj")
        
        self.custRepo.add(cust5)
        
        cust6 = Customer(6, "Mircea", 123456789, "Cluj")
        
        self.custRepo.add(cust6)
        
        cust7 = Customer(7, "Johnny", 123456789, "Cluj")
         
        lista = self.custRepo.get_all_customers_same_name(cust6)
        
        self.assertTrue(len(lista) == 2)
        
        self.assertTrue(lista[0].get_cid() == 3)
        
        self.assertTrue(lista[1].get_cid() == 6)
        
        self.assertRaises(RepoError, self.custRepo.get_all_customers_same_name, cust7)
        
        open('testcustomer.txt', 'w').close()

class TestCaseFileRepoMovie(unittest.TestCase):
    
    def setUp(self):
        self.repoMovie = FileRepoMovie("testmovie.txt", Movie.read_movie, Movie.write_movie)
        
    def tearDown(self):
        pass
    
    def testAdd(self):
        
        movie = Movie(1, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie)
        
        self.assertTrue(self.repoMovie.size() == 1)
        
        self.assertRaises(RepoError, self.repoMovie.add, movie)
        
        open('testmovie.txt', 'w').close()
        
    def testGetAll(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista == [movie2, movie3])
        
        open('testmovie.txt', 'w').close()
        
    def testSize(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        self.assertTrue(self.repoMovie.size() == 2)
        
        open('testmovie.txt', 'w').close()
        
    def testSearch(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Drama", "free")
        
        self.assertTrue(self.repoMovie.search(movie3) == movie3)
        
        self.assertRaises(RepoError, self.repoMovie.search, movie4)
    
        open('testmovie.txt', 'w').close()
    
    def testDelete(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie4)
        
        self.assertTrue(self.repoMovie.size() == 3)
        
        self.repoMovie.delete(movie3)
        
        self.assertTrue(self.repoMovie.size() == 2)
        
        self.assertRaises(RepoError , self.repoMovie.search, movie3)
        
        open('testmovie.txt', 'w').close()
        
    def testModifyTitle(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_title() == "Joker")
        
        self.repoMovie.modify_title(lista[0], "Batman")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_title() == "Batman")
        
        self.assertRaises(RepoError, self.repoMovie.modify_title, movie3, "Batman")
        
        open('testmovie.txt', 'w').close()
        
    def testModifyGenre(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_genre() == "Drama")
        
        self.repoMovie.modify_genre(lista[0], "Comedie")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_genre() == "Comedie")
        
        self.assertRaises(RepoError, self.repoMovie.modify_genre, movie3, "Batman")
        
        open('testmovie.txt', 'w').close()
        
    def testModifyStatus(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Joker", "Drama", "free")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_status() == "free")
        
        self.repoMovie.modify_status(lista[0], "rented")
        
        lista = self.repoMovie.get_all()
        
        self.assertTrue(lista[0].get_status() == "rented")
        
        self.assertRaises(RepoError, self.repoMovie.modify_status, movie3, "Batman")
        
        open('testmovie.txt', 'w').close()
        
    def testGetAllMoviesSameTitle(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie4)
        
        movie5 = Movie(5, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie5)
        
        movie6 = Movie(6, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie6)
        
        movie7 = Movie(7, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie7)
        
        lista = self.repoMovie.get_all_movies_same_title(movie3)
        
        self.assertTrue(len(lista) == 3)
        
        open('testmovie.txt', 'w').close()
        
    def testGetAllMoviesSameGenre(self):
        
        movie2 = Movie(2, "Joker", "Comedy", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Comedy", "free")
        
        self.repoMovie.add(movie4)
        
        movie5 = Movie(5, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie5)
        
        movie6 = Movie(6, "Joker", "Comedy", "free")
        
        self.repoMovie.add(movie6)
        
        movie7 = Movie(7, "Lion King", "Comedy", "free")
        
        self.repoMovie.add(movie7)
        
        lista = self.repoMovie.get_all_movies_same_genre(movie7)
        
        self.assertTrue(len(lista) == 4)
        
        open('testmovie.txt', 'w').close()
        
    def getAllMoviesSameStatus(self):
        
        movie2 = Movie(2, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie2)
        
        movie3 = Movie(3, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie3)
        
        movie4 = Movie(4, "Joker", "Drama", "rented")
        
        self.repoMovie.add(movie4)
        
        movie5 = Movie(5, "Lion King", "Drama", "rented")
        
        self.repoMovie.add(movie5)
        
        movie6 = Movie(6, "Joker", "Drama", "free")
        
        self.repoMovie.add(movie6)
        
        movie7 = Movie(7, "Lion King", "Drama", "free")
        
        self.repoMovie.add(movie7)
        
        lista = self.repoMovie.get_all_movies_same_status(movie5)
        
        self.assertTrue(len(lista) == 2) 
        
        open('testmovie.txt', 'w').close()

class TestCaseFileRepoRented(unittest.TestCase):
    
    def setUp(self):
        
        self.repoRented = FileRepoRented("testrented.txt", Rental.read_rental, Rental.write_rental)
        
    def tearDown(self):
        pass
    
    def testAdd(self):
        
        rental = Rental(1, 1, "1.1.1", "1.1.1")
        
        self.assertTrue(self.repoRented.size() == 0)
        
        self.repoRented.add(rental)   
    
        self.assertTrue(self.repoRented.size() == 1)
        
        self.assertRaises(RepoError, self.repoRented.add, rental)
        
        open('testrented.txt', 'w').close()
        
    def testSearch(self):
        
        rental = Rental(1, 1, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental)   
        
        rental2 = Rental(2, 2, "1.1.1", "1.1.1")   
    
        rental3 = Rental(3, 3, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental3)   
        
        self.assertTrue(self.repoRented.search(rental3) == rental3)
        
        self.assertRaises(RepoError, self.repoRented.search, rental2)
        
        open('testrented.txt', 'w').close()
        
    def testGetAll(self):
        
        rental = Rental(1, 1, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental)   
        
        rental2 = Rental(2, 2, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental2)   
    
        rental3 = Rental(3, 3, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental3)   
        
        lista = self.repoRented.get_all()
    
        self.assertTrue(len(lista) == 3)
        
        self.assertTrue(lista[1].get_rented_mid() == 2)
        
        self.assertTrue(lista[1].get_rented_cid() == 2)
        
        open('testrented.txt', 'w').close()
        
    def testDelete(self):
    
        rental = Rental(1, 1, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental)   
        
        rental2 = Rental(2, 2, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental2)   
    
        rental3 = Rental(3, 3, "1.1.1", "1.1.1")
        
        self.repoRented.add(rental3)   
        
        self.assertTrue(self.repoRented.size() == 3)
        
        self.repoRented.delete(rental2)
        
        self.assertTrue(self.repoRented.size() == 2)
        
        self.assertRaises(RepoError, self.repoRented.search, rental2)
        
        self.assertRaises(RepoError, self.repoRented.delete, rental2)
        
        open('testrented.txt', 'w').close()
        
if __name__ == '__main__':
    unittest.main()
