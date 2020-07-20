"""Classes for melon orders."""
import random
from datetime import datetime, timezone
from datetime import date
import time

class TooManyMelonsError(ValueError):
    def __init__(self):
        self.message = "No more than 100 melons!"


class AbstractMelonOrder():
    """ An abstract base class that other Melon Orders inherit from. """
   

    def __init__(self, species, qty, tax, order_type, country_code=None):
        """Initialize melon order attributes."""
        self.country_code = country_code
        self.species = species
        self.qty = int(qty)
        self.shipped = False
        self.base_price = int(5)
        self.tax = float(tax)
        self.order_type = order_type

        if self.qty > 100:
            raise TooManyMelonsError
          

    def get_total(self):
        """Calculate price, including tax."""
        fee = 0
        # get a random surge prices integer between 5-9
        self.base_price = self.get_base_price()

        # get datetime and get another surge pricing free
        fee += self.get_date_time_surge_fee()

        if self.species == "christmas":
            self.base_price = 1.5 * self.base_price

        if self.order_type == 'international' and self.qty <10:
            fee = 3
        
        total = (1 + self.tax) * self.qty * self.base_price + fee
        return total + self.get_date_time_surge_fee
    
    def get_date_time_surge_fee(self):
        now = today.ctime()
        # print(now, today, today.hour, today.min)
        # print(now.hour - 7, now.min)
        if (str(now).split()[0] in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri' ]
        and "15:00:00"<= str(now).split()[3] < "22:00:00"): 

            return 4
        
        return(0)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

    def get_base_price(self):
        return random.randint(5, 9)



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, 0.08, "domestic")


class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super().__init__(species, qty, 0.0, "government")
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        self.pass_inspection = passed



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, 0.17, "international")
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



if __name__ == '__main__':
    order0 = InternationalMelonOrder("watermelon", 6, "AUS")
    order1 = DomesticMelonOrder("cantaloupe", 8)
    order2 = DomesticMelonOrder("christmas", 10)
    order3 = DomesticMelonOrder("crenshaw", 10)
    # order4 = InternationalMelonOrder("Cantaloupe", 105, "MEX")
