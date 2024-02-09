"Builder Concept Sample Code"

from abc import ABC, abstractmethod

class Product():
    
    def __init__(self) -> None:
        self.parts = []
    
    def show_parts(self) -> None:
        print(self.parts)

# abstract builder class
class IBuilder(ABC):
    
    @abstractmethod
    def build_part_a(self):
        pass
    
    @abstractmethod
    def build_part_b(self):
        pass
    
    @abstractmethod
    def build_part_c(self):
        pass

    @abstractmethod
    def get_final_product(self):
        pass
    
# Concrete builder class
class BuilderA(IBuilder):

    def __init__(self) -> None:
        
        self.product = Product()
    
    def build_part_a(self):
        
        self.product.parts.append("a")
        
        return self
    
    def build_part_b(self):
        
        self.product.parts.append("b")
        
        return self
    
    def build_part_c(self):
        
        self.product.parts.append("c")
        
        return self
    
    def get_final_product(self):
        
        return self.product
    
class Director:

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def __init__(self, builder:IBuilder) -> None:
        
        self.builder = builder

    def build_minimum_viable_product(self) -> None:
        
        return self.builder.build_part_a().get_final_product()
    
    def build_full_featured_product(self) -> None:

        return self.builder.build_part_a().build_part_b().build_part_c().get_final_product()
    

# The Client
    
builder = BuilderA()

director = Director(builder)

product1 = director.build_minimum_viable_product()

product1.show_parts()

# ----------------------------------------------------------------

builder = BuilderA()

director = Director(builder)

product2 = director.build_full_featured_product()

product2.show_parts()
    

    

