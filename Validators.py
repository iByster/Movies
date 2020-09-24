from Erorrs.Exceptions import ValidError
class ValidateCustomer:
    
    def __init__(self):
        pass
    def validate_customer(self, customer):
        '''
        Validate customer
        input : object customer
        output : errors if found
        '''
        errors = ""
        
        #id nu poate fi negativ
        if customer.get_cid() < 0:
            errors += "id invalid!\n"
        
        #numele nu poate fi gol/nimic
        if customer.get_name() == "":
            errors += "nume invalid!\n"
        
        #cnp nu poate fi negativ
        if customer.get_cnp() < 0:
            errors += "cnp invalid!\n"
        
        #adresa nu poate fi gol/nimic
        if customer.get_adress() == "":
            errors += "adresa invalida!\n"
        
        if len(errors)>0:
            raise ValidError(errors)
        
class ValidateMovie:
    
    def __init__(self):
        pass
    
    def validate_movie(self, movie):
        '''
        Validate movie
        input : object movie
        output : errors if found
        '''
        errors = ""
        
        #id nu poate fi negativ
        if movie.get_mid() < 0:
            errors += "id invalid!\n"
        
        #titlu nu poate fi gol/nimic    
        if movie.get_title() == "":
            errors += "titlu invalid!\n"
        
        #genul nu poate fi gol/nimic
        if movie.get_genre() == "":
            errors += "gen invalid!\n"
        
        #status poate fi doar <free> sau <rented>  
        if movie.get_status() != "free" and movie.get_status() != "rented":
            errors += "status invalid!\n"
            
        if len(errors) > 0:
            raise ValidError(errors)
        
class ValidateRented:
    
    def __init__(self):
        pass
    
    def validate_rental(self, rental):
        '''
        Validate rental
        input : object rental
        output : errors if found
        '''
        
        errors = ""
        
        #datele de start si return vor fi impartine pe bucati pentru a putea fi evaluata
        #ziua si luna separat
        start_date = rental.get_start_date()
        return_date = rental.get_return_date()
        
        start_date = start_date.split(".")
        return_date = return_date.split(".")
        
        #ca o data sa fie valida trebuie sa aiba urmatoarele propietati :
        #1. trebuie sa fie compus din trei parti : zi, luna, an
        #2. ziua nu poate sa fie negativa si mai mica decat 31
        #3. luna nu poate fi negativa si mai mica decat 12
        if len(start_date) != 3 or (int(start_date[0]) < 0 or int(start_date[0]) > 31) or (int(start_date[1]) < 0 or int(start_date[1]) > 12):
            errors += "data start invalid!\n"
        
        if len(return_date) != 3 or (int(return_date[0]) < 0 or int(return_date[0]) > 31) or (int(return_date[1]) < 0 or int(return_date[1]) > 12):
            errors += "data return invalid!\n"
        
        if len(errors) > 0:
            raise ValidError(errors)
        



