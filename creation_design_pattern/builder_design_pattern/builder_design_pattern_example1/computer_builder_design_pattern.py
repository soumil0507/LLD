"""
Problem Statement:
You own a computer shop
You make computers as per demand and requirements.

1. Gaming Computer
2. Office Computer
3. Foldable Computer

building blocks of computer are - 
1. CPU/Processor - mandatory
2. RAM - mandatory
3. GPU
4. SSD 
5. HDD - mandatory
6. Fingerprint


"""
from abc import ABC, abstractmethod

class Computer:

    def __init__(self, cpu, ram, hdd) -> None:
        self.cpu:str = cpu
        self.ram:str = ram
        self.hdd:str = hdd
        self.ssd:str = "Not Installed"
        self.gpu:str = "Not Installed"
        self.fingerprint:bool = False 
    
    def show_computer(self):
        print(f"Your computer is ready with following specifications: \ncpu={self.cpu}\nram={self.ram}\nhdd={self.hdd}\nssd={self.ssd}\ngpu={self.gpu}\nfingerprint={self.fingerprint}\n")

# abstractclass
class IComputerBuilder(ABC):
    
    @abstractmethod
    def set_ssd(self) -> None:
        pass

    @abstractmethod
    def set_gpu(self) -> None:
        pass

    @abstractmethod
    def set_fingerprint(self) -> None:
        pass

# concrete class for building computers
class ComputerBuilder(IComputerBuilder):

    def __init__(self, computer:Computer):
        
        self.computer = computer

        print("We are building a gaming computer for you!!")
    
    def set_ssd(self):
        
        _ssd = input("Enter SSD -> ")
        
        self.computer.ssd = _ssd

        return self

    def set_gpu(self) -> None:
        
        _gpu = input("Enter GPU -> ")

        self.computer.gpu = _gpu

        return self
    
    def set_fingerprint(self) -> None:

        self.computer.fingerprint = True

        return self

    def get_product(self):

        return self.computer
    
# So till now we have a computer builder to which after we provide basic details like cpu, ram, hdd we can opt to add ssd, gpu and fingerprint
    
# for that we need a computer technician 
    
class ComputerShop:
    
    def __init__(self, computerBuilder:IComputerBuilder) -> None:

        self.computerBuilder = computerBuilder

    def buildGamingComputer(self):

        return self.computerBuilder.set_ssd().set_gpu().get_product()
    
    def buildOfficeComputer(self):

        return self.computerBuilder.set_ssd().set_fingerprint().get_product()
    

# The Customer
    
while(1):
    
    print("Shopkeeper : Welcome to Computer Shop\n What kind of computer are you looking for?")
    
    customer_choice = int(input("1.Gaming Computer\n2.Office Computer\n3.Exit Computer Shop\nEnter your choice -> "))

    if customer_choice == 1:
        
        print("Shopkeeper : So you wish to build a gaming computer\nFor that I need some basic info like ram, cpu, hdd !! ")
        
        ram = input("Enter Ram -> ")
        cpu = input("Enter CPU -> ")
        hdd = input("Enter HDD -> ")

        computerBuilder = ComputerBuilder(Computer(cpu=cpu, ram=ram, hdd=hdd))
        
        print("Shopkeeper : Your Basic computer is ready now lets add GPU and SSD for better performance !!")

        computerShop = ComputerShop(computerBuilder)
        
        gamingComputer = computerShop.buildGamingComputer()

        gamingComputer.show_computer()

    elif customer_choice == 2:

        print("Shopkeeper : So you wish to build a office computer\nFor that I need some basic info like ram, cpu, hdd !! ")
        
        ram = input("Enter Ram -> ")
        cpu = input("Enter CPU -> ")
        hdd = input("Enter HDD -> ")

        computerBuilder = ComputerBuilder(Computer(cpu=cpu, ram=ram, hdd=hdd))
        
        print("Shopkeeper : Your Basic computer is ready now lets add SSD and fingerprint for better performance and safety!!")

        computerShop = ComputerShop(computerBuilder)
        
        officeComputer = computerShop.buildOfficeComputer()
        
        officeComputer.show_computer()

    elif customer_choice == 3:

        print("Thank you for visiting the shop!!\nI hope you are happy with your purchase!!")
        break








