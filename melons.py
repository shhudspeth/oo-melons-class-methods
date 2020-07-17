"""Classes for melon orders."""

class AbstractMelonOrder():
    """ An abstract base class that other Melon Orders inherit from. """
    tax = None
    order_type = None

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""
        self.country_code = country_code
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 5

    def get_total(self):
        """Calculate price, including tax."""
        fee = 0

        if self.species.lower() == "christmas":
            self.base_price = 1.5 * self.base_price
        else: 
            base_price = 5

        if self.order_type == 'international' and self.qty <10:
            fee = 3

        total = (1 + self.tax) * self.qty * self.base_price + fee
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"
    
    
   
   


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
       
    order_type = "international"
    tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code



if __name__ == '__main__':
    order0 = InternationalMelonOrder("watermelon", 6, "AUS")
    order1 = DomesticMelonOrder("cantaloupe", 8)
    order2 = DomesticMelonOrder("christmas", 10)
    order3 = DomesticMelonOrder("crenshaw", 10)
