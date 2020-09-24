from Tests.Tests import Tests
from Validators.Validators import ValidateMovie, ValidateCustomer, ValidateRented
from Infrastructure.Repository import FileRepoCustomer, FileRepoMovie, FileRepoRented
from Business.Controller import MovieController, CustomerController, RentedController
from Presentation.UI import Console
from Domain.Entities import Customer, Movie, Rental

tests = Tests()
tests.run_all_tests()
validMovie = ValidateMovie()
validCustomer = ValidateCustomer()
validRented = ValidateRented()
repoMovie = FileRepoMovie("movies.txt", Movie.read_movie, Movie.write_movie)
repoCustomer = FileRepoCustomer("customers.txt", Customer.read_customer, Customer.write_customer)
repoRented = FileRepoRented("rentals.txt", Rental.read_rental, Rental.write_rental)
ctrlCustomer = CustomerController(validCustomer, repoCustomer)
ctrlMovie = MovieController(validMovie, repoMovie)
ctrlRented = RentedController(validRented, repoRented, repoCustomer, repoMovie)
ui = Console(ctrlMovie, ctrlCustomer, ctrlRented)

ui.run()