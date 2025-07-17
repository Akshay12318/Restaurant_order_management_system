rn = 'Halidram'
rm = {'pav bhaji': 200, 'chai': 150, 'pani puri': 120}
import time


class RMS:
    def __init__(self, user_restaurant_name, user_restaurant_menu):
        self.rest_name = user_restaurant_name
        self.menu = user_restaurant_menu
        self.user_order = ''
        # self.neworder= ''
        self.user_bill = 0.0
        self.user_pay = 0.0
        self.list1=[]

    def welcome_user(self):
        print('Welcome to', self.rest_name)

    def display_menu(self):
        for i in self.menu:
            print(i.title(), self.menu[i])

    def take_order(self):
        self.user_order = input('Please place your order here:').lower()
        if self.user_order in rm:
            self.list1.append(self.user_order)
            print('Your Order:', self.user_order.title())
            # self.list1.append(self.user_order)
        else:
            print("Invalid order,order again")
            self.take_order()

    def preparing_order(self):
        print('Your order is preparing')
        time.sleep(3)

    def serve_order(self):
        print('Your Order is Ready!')

    def reorder(self):
        self.neworder=input("Would you want to place new order ('Yes/No') :").title()
        if self.neworder=="Yes":
            self.order_process()
        else:
            self.bill()


    def display_bill(self):
        for i in self.list1:
            self.user_bill += self.menu[i]
        # self.user_bill = self.menu[self.user_order.lower()]
        # self.user_bill+=self.menu[self.user_order.lower()]
        print('Your Total Bill:', self.user_bill)

    def take_payment(self):
        self.user_pay = float(input('Please pay your bill here:'))
        if self.user_pay > self.user_bill:
            print('Paymnet Successful! Here is your remaininng', self.user_pay - self.user_bill)
        elif self.user_bill > self.user_pay:
            print('Payment Unsuccessful! Please pay remaining', self.user_bill - self.user_pay)
        else:
            pass

    def thank_user(self):
        print('Thank you for visiting Mcdonalds')

    def order_process(self):
        self.welcome_user()
        self.display_menu()
        self.take_order()
        self.preparing_order()
        self.serve_order()
        self.reorder()

    def bill(self):
        self.display_bill()
        self.take_payment()
        print(self.list1)
        self.thank_user()

mcd=RMS(rn,rm)
# hd=RMS(rn,rm)
# hd.order_process()
mcd.order_process()
