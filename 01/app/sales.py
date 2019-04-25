class Sales:
    __id = None
    __customer_id = None    
    __product_id = None

    def __init__(self, id, customer_id, product_id):
        self.__id = id
        self.__costumer_id = customer_id        
        self.__product_id = product_id

    def get_id(self):
        return self.__id

    def get_customer_id(self):
        return self.__costumer_id

    def get_product_id(self):
        return self.__product_id
