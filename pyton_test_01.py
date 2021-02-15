import random


class Bill:
    def __init__(self):
        self.num_of_adult = 0
        self.num_of_children = 0
        self.gratuity = 0.2  # 20%
        self.cost = 0
        self.costs = {"a": 25.95,
                      "b": 21.75}
        self.hall_cost = 0
        self.halls = {"a": 1000,
                      "b": 850,
                      "c": 750,
                      "d": 0}
        self.weekend = False
        self.weekend_surcharge = 0.1  # 10%
        self.sales_tax = 0.06875  # 6.875%
        self.invoice_number = 0
        self.speedy_payment = False
        self.speedy_discount = 0
        self.speedy_discounts = {"a": 0.02,  # 2, 4, 5, 7%
                                 "b": 0.04,
                                 "c": 0.05,
                                 "d": 0.07}
        self.deposit = 0

    def main(self):
        self._inputs()
        self._calculations()
        self._print_bill()

    def _inputs(self):
        self.num_of_adult = int(input("Enter the number of adults attending: "))
        self.num_of_children = int(input("Enter the number of children attending: "))
        print("Select menu: ('a' or 'b')\na. Cost for Deluxe meal $25.95,\nb. Cost for Standard meal $21.75.")
        self.cost = self.costs[input()]
        print("Select hall: (from 'a' to 'd')\na. Hall – A $1000.00\n"
              "b. Hall – B $850.00\nc. Hall – C $750.00\nd. Hall – H is home")
        self.hall_cost = self.halls[input()]
        self.weekend = True if input("Is the event held on a weekend? "
                                     "(Yes/No, Y/N)\n") in ("Yes", "y", "Y") else False
        self.speedy_payment = True if input("Will the payment be made in 10 days? "
                                            "(Yes/No, Y/N)\n") in ("Yes", "y", "Y") else False
        self.deposit = float(input("Enter the deposit: "))

    def _calculations(self):
        self.invoice = "".join(random.choices("1234567890", k=3))
        self.total_food_cost = round(self.num_of_adult * self.cost, 2) + round(self.num_of_children * self.cost / 2, 2)
        self.gratuity_payment = round(self.total_food_cost * self.gratuity, 2)
        self.weekend_charge = round(self.total_food_cost * self.weekend_surcharge, 2) if self.weekend else 0
        self.taxes = round((self.total_food_cost + self.hall_cost) * self.sales_tax, 2)
        self.subtotal = round(self.total_food_cost + self.gratuity_payment +
                              self.hall_cost + self.weekend_charge + self.taxes, 2)
        if self.speedy_payment:
            if self.subtotal > 5000:
                key = "d"
            elif self.subtotal > 2000:
                key = "c"
            elif self.subtotal > 1000:
                key = "b"
            else:
                key = "a"
            self.speedy_discount = round(self.speedy_discounts[key] * self.subtotal, 2)
        self.balance_due = round(self.subtotal - self.deposit - self.speedy_discount, 2)

    def _print_bill(self):
        print(f"""
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
                    Caswell Catering and Convention Services
                                  Final Bill                                   Invoice# {self.invoice}
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
            Number of adult:        {str(self.num_of_adult)}
            Number of children:     {str(self.num_of_children)}
            Gratuity:               {int(self.gratuity * 100)}%
            Weekend:                {"Yes" if self.weekend else "No"}
            Cost per standard meal for adult:   {f"${self.cost:.2f}":>10}
            Cost per standard meal for child:   {f"${self.cost * 0.5:.2f}":>10}
            -------------------------------------------------------------------
            Total cost for adult meals:         {f"${self.num_of_adult * self.cost:.2f}":>10}
            Total cost for child meals:         {f"${self.num_of_children * self.cost / 2:.2f}":>10}
            Total food cost:                    {f"${self.total_food_cost:.2f}":>10}
            -------------------------------------------------------------------
            Gratuity:                           {f"${self.gratuity_payment:.2f}":>10}
            Hall C - Room fee                   {f"${self.hall_cost:.2f}":>10}
            Weekend charge:                     {f"${self.weekend_charge:.2f}":>10}
            Taxes:                              {f"${self.taxes:.2f}":>10}
            -------------------------------------------------------------------
            Subtotal:                           {f"${self.subtotal:.2f}":>10}
            Less deposit:                       {f"${self.deposit:.2f}":>10}
            Less Speedy Payment                 {f"${self.speedy_discount:.2f}":>10}
            Balance Due:                        {f"${self.balance_due:.2f}":>10}
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
                        Thank you for using Caswell Catering""")


def main():
    bill = Bill()
    bill.main()


main()
