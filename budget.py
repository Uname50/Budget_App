class Category:

    # this should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. this class should also have a list called "ledger"
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # the class should contain the following methods: 
    # - a deposit that accepts an amount and description. of no description is given, it should default to an empty string. the method should append an object to the ledger list in the form of 
    # {"amount": amount, "description": description}
    def deposit(self, amount, description = ""):
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)

    # - a withdraw method, similar to the deposit, but the amount passed in should be stored in the ledger as a negative number. if there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise
    def withdraw(self, amount, description = ""):
        transaction = {"amount": -amount, "description": description}
        if self.check_funds():
            self.ledger.append(transaction)
            return True

    # - a get_balance method that returns the current balance of the budget or category, based on the deposits that have occured 
    def get_balance(self):
        balance = sum(transaction["amount"] for transaction in self.ledger)
        return balance

    # - a transfer method that accepts an amount and another category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". This method should return True if the transfer took place, and False otherwise
    def transfer(amount, from_category, to_category):
        pass

    # - a check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method
    def check_funds(self, amount):
        total = sum(transaction["amount"] for transaction in self.ledger)
        if total < amount:
            return False

    # when the budget object is printed it should display:
    # - a title line of 30 characters where the name of the category is centered in a line of * characters
    # - a list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    # - a line displaying the category total.

    # *************Food*************
    # initial deposit        1000.00
    # groceries               -10.15
    # restaurant and more foo -15.89
    # Transfer to Clothing    -50.00
    # Total: 923.96


    