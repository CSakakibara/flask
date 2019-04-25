class Product:
    __id = None
    __description = None    
    __price = None

    def __init__(self, id, description, price):
        self.__id = id
        self.__description = description        
        self.__price = price

    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

