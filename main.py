from datetime import datetime
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import GridLayout


from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
#from utils import Dabloons, Transactions

"""
TODO:
- Add a way to delete transactions
- Add a way to remove dabloons
- Add a way to show inventory
- Add a way to show item info in inventory
- Add a way to edit items in inventory
- Add a way to add items to inventory

"""

class MainApp(MDApp):
    def build(self):
        self.dabloons = 0#Dabloons()
        self.transaction_history = []#Transactions()
        self.show_history_page = 1
        self.PAGE_LIMIT = 8

        screen = MDScreen()
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"

        self.main_text = Label(text=f"Your dabloons: {self.dabloons}", font_size=50, pos_hint={"center_x": 0.5, "center_y": 0.7})
        screen.add_widget(self.main_text)

        btn = MDRectangleFlatButton(text="Add dabloons", pos_hint={"center_x": 0.5, "center_y": 0.6})
        btn.bind(on_press=self.add_button)
        screen.add_widget(btn)

        btn2 = MDRectangleFlatButton(text="Purchase", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn2.bind(on_press=self.purchase)
        screen.add_widget(btn2)

        btn3 = MDRectangleFlatButton(text="History", pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.show_history)
        screen.add_widget(btn3)

        return screen

    def show_error(self, text, on_press=None):
        if on_press is None:
            on_press = self.dismiss_popup

        self.box = BoxLayout(orientation="vertical", padding=10)
        self.box.add_widget(Label(text=text, font_size=20))
        self.box.add_widget(MDRectangleFlatButton(text="Close", on_press=on_press, pos_hint={"center_x": 0.5}))

        self.popup = Popup(title="Error", content=self.box, size_hint=(None, None), size=(300, 175))
        self.popup.open()

    def add_transaction(self, action, price, name=""):
        self.transaction_history.append({
            "id": len(self.transaction_history) + 1,
            "action": action,
            "name": name,
            "price": int(price),
            "date": datetime.now().strftime("%d.%m.%Y"),
            "time": datetime.now().strftime("%H:%M:%S")
        })

    def add_button(self, obj):
        self.box = MDBoxLayout(orientation="vertical", adaptive_height=True)
        self.box.add_widget(MDTextField(text="", multiline=False, font_size=20, size_hint=(0.5, 0.8), pos_hint={"center_x": 0.5}, hint_text="Amount", helper_text="Enter amount of dabloons to add", helper_text_mode="on_focus"))
        self.box.add_widget(MDRectangleFlatButton(text="Add", on_press=self.add_dabloons, pos_hint={"center_x": 0.5}))

        self.popup = Popup(title="Add dabloons", content=self.box, size_hint=(None, None), size=(300, 175))
        self.popup.open()
    
    def add_dabloons(self, obj):
        self.popup.dismiss()
        dep_text= self.box.children[1].text

        if not dep_text.isdigit():
            self.box = BoxLayout(orientation="vertical", padding=10)
            self.box.add_widget(MDLabel(text=f"Please enter a valid amount!", font_size=20))
            self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))

        elif int(dep_text) > 1_000_000:
            self.box = BoxLayout(orientation="vertical", padding=10)
            self.box.add_widget(MDLabel(text=f"You can't add 1m+ dabloons at once", font_size=20))
            self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))

        else:
            self.deposit = int(dep_text)

            if self.deposit > 0:
                self.dabloons += self.deposit
                #print(self.dabloons)
                #print(self.dabloons.credits)
                self.main_text.text = f"Your dabloons: {self.dabloons}"
                self.add_transaction("deposit", price=self.box.children[1].text)

                self.box = BoxLayout(orientation="vertical", padding=10)
                self.box.add_widget(MDLabel(text=f"Succesfully deposited {self.deposit} dabloons!", font_size=20, on_press=self.dismiss_popup))
                self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))

            else:
                self.box = BoxLayout(orientation="vertical", padding=10)
                self.box.add_widget(MDLabel(text="Please enter a valid amount!", font_size=20, pos_hint={"center_x": 0.5, "center_y": 0.5}))
                self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))


        self.popup = Popup(title="Add dabloons", content=self.box, size_hint=(None, None), size=(300, 175))
        self.popup.open()



    def purchase(self, obj):
        self.box = BoxLayout(orientation="vertical", padding=10)
        #self.box.add_widget(MDLabel(text="Input item price:", font_size=20))
        self.box.add_widget(MDTextField(text="", multiline=False, font_size=20, size_hint=(0.5, 0.8), pos_hint={"center_x": 0.5}, hint_text="Price", helper_text="Enter price of item", helper_text_mode="on_focus"))
        self.box.add_widget(MDRectangleFlatButton(text="Purchase", on_press=self.purchase_for_dabloons, pos_hint={"center_x": 0.5}))

        self.popup = Popup(title="Purchase", content=self.box, size_hint=(None, None), size=(300, 175))
        self.popup.open()
    
    def purchase_for_dabloons(self, obj):
        self.popup.dismiss()

        price_text= self.box.children[1].text

        if not price_text.isdigit():
            self.box = BoxLayout(orientation="vertical", padding=10)
            self.box.add_widget(MDLabel(text=f"Please enter a valid amount!", font_size=20))
            self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))
        else:

            self.item_price = int(price_text) # global variable for last purchase price

            if self.dabloons >= self.item_price and self.item_price > 0:

                self.box = BoxLayout(orientation="vertical", padding=10)
                #self.box.add_widget(MDLabel(text="Input item name:", font_size=20))
                self.box.add_widget(MDTextField(text="", multiline=False, font_size=20, size_hint=(0.5, 0.8), pos_hint={"center_x": 0.5}, hint_text="Name", helper_text="Enter name of item", helper_text_mode="on_focus"))
                self.box.add_widget(MDRectangleFlatButton(text="Purchase", on_press=self.purchase_input_item, pos_hint={"center_x": 0.5}))

            elif self.item_price <= 0:
                self.box = BoxLayout(orientation="vertical", padding=10)
                self.box.add_widget(MDLabel(text="Item price must be greater than 0", font_size=20))
                self.box.add_widget(MDRectangleFlatButton(text="Dismiss", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))

            else:
                self.box = BoxLayout(orientation="vertical", padding=10)
                self.box.add_widget(MDLabel(text="You don't have enough dabloons!", font_size=20, pos_hint={"center_x": 0.5}))
                self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))

            self.popup = Popup(title="Purchase", content=self.box, size_hint=(None, None), size=(300, 175))
            self.popup.open()


    def purchase_input_item(self, obj):
        self.popup.dismiss()
        self.item_name = self.box.children[1].text # global variable for last purchase item name

        if not self.item_name:
            self.box = BoxLayout(orientation="vertical", padding=10)
            self.box.add_widget(MDLabel(text="Please enter a valid item name!", font_size=20))
            self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))
        else:
            self.dabloons -= self.item_price
            self.main_text.text = f"Your dabloons: {self.dabloons}"

            self.add_transaction("purchase", name=self.item_name, price=self.item_price)

            self.box = BoxLayout(orientation="vertical", padding=10)

            self.box.add_widget(MDLabel(text=f"You purchased {self.item_name} for a {self.item_price} dabloons!", font_size=20))
            self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.dismiss_popup, pos_hint={"center_x": 0.5}))

        self.popup = Popup(title="Purchase", content=self.box, size_hint=(None, None), size=(300, 175))
        self.popup.open()


    def history_max_page(self):
        return len(self.transaction_history) // self.PAGE_LIMIT + (1 if len(self.transaction_history) % self.PAGE_LIMIT != 0 or len(self.transaction_history) == 0 else 0)

    def show_history(self, obj):
        self.box = MDBoxLayout(orientation="vertical", padding=2)
        self.show_history_page_max = self.history_max_page()


        if self.transaction_history:
            page_transactions = self.transaction_history[(self.show_history_page - 1) * self.PAGE_LIMIT if self.show_history_page != 1 else 0:self.show_history_page * self.PAGE_LIMIT]
            while len(page_transactions) < self.PAGE_LIMIT:
                page_transactions.append({"action": "", "name": "", "price": "", "date": "", "time": "", "id": ""})
            
            LINELIMIT = 40
            dep_color = "#50C878"
            pur_color = "#B80000"
            lbtext = ""
            for transaction in page_transactions:
                if transaction["action"] == "deposit":
                    lbtext += f"{transaction['id']}." + f" [ref={transaction['id']}] [color={dep_color}]+{transaction['price']} dabloons[/color][/ref]".center(LINELIMIT, " ") + "\n"
                elif transaction["action"] == "purchase":
                    lbtext += f"{transaction['id']}."
                    main_ = f" [ref={transaction['id']}] [color={pur_color}]-{transaction['price']} dabloons for {transaction['name']}[/color][/ref]".center(LINELIMIT, " ")
                    if len(main_) - 30 > LINELIMIT:
                        main_ = main_[:LINELIMIT + 15].replace('[/ref]', '') + "...[/color][/ref]"
                    lbtext += main_ + "\n"
                else:
                    lbtext += f"\n"


            self.box.add_widget(Label(text=lbtext, font_size=20, pos_hint={"center_x": 0.5, "center_y": 0.5}, markup=True, on_ref_press=self.edit_transaction))

        else:
            self.box.add_widget(Label(text="No transactions yet", font_size=20))

        self.gridline = GridLayout(cols=3, size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.8})

        btn_size = (0.1, 0.02)

        self.gridline.add_widget(MDRectangleFlatButton(text="<<", on_press=self.show_history_left, size_hint=btn_size, pos_hint={"center_x": 0.5}))
        self.gridline.add_widget(Label(text=f"{self.show_history_page}/{self.show_history_page_max}", font_size=12, pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint=btn_size))
        self.gridline.add_widget(MDRectangleFlatButton(text=">>", on_press=self.show_history_right, size_hint=btn_size, pos_hint={"center_x": 0.5}))

        self.box.add_widget(self.gridline)

        self.box.add_widget(MDRectangleFlatButton(text="Ok", on_press=self.close_history, size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.9}))

        self.popup = Popup(title="History", content=self.box, size_hint=(None, None), size=(400, 400))
        self.popup.open()

    def close_history(self, obj):
        self.dismiss_popup(obj)
        self.show_history_page = 1

    def show_history_left(self, obj):
        if self.show_history_page > 1:
            self.dismiss_popup(obj)
            self.show_history_page -= 1
            self.show_history(obj)

    def show_history_right(self, obj):
        if self.show_history_page < self.history_max_page():
            self.show_history_page += 1
            self.dismiss_popup(obj)
            self.show_history(obj)

    def edit_transaction(self, obj, ref):
        self.popup.dismiss()

        self.last_ref = ref
        tx = self.transaction_history[int(ref) - 1]

        self.box = MDBoxLayout(orientation="vertical", padding=10)

        if tx['action'] == 'deposit':
            lbtext = f"TransactionId: {tx['id']}\nType: {tx['action']}\nAmount: {tx['price']}\nDate: {tx['date']}\nTime: {tx['time']}"
            btns = [
                MDTextField(text=str(tx['price']), multiline=False, font_size=20, size_hint=(0.5, 0.8), pos_hint={"center_x": 0.5}, hint_text="Amout", helper_text="Enter dabloons amount", helper_text_mode="on_focus"),
            ]
        else:
            lbtext = f"TransactionId: {tx['id']}\nType: {tx['action']}\nItem: {tx['name']}\nPrice: {tx['price']}\nDate: {tx['date']}\nTime: {tx['time']}"
            btns = [
                MDTextField(text=str(tx['price']), multiline=False, font_size=20, size_hint=(0.5, 0.8), pos_hint={"center_x": 0.5}, hint_text="Price", helper_text="Enter item price", helper_text_mode="on_focus"),
                MDTextField(text=tx['name'], multiline=False, font_size=20, size_hint=(0.5, 0.8), pos_hint={"center_x": 0.5}, hint_text="Item name", helper_text="Enter item name", helper_text_mode="on_focus"),
            ]

        self.box.add_widget(MDLabel(text=lbtext, font_size=20))
        for btn in btns:
            self.box.add_widget(btn)

        btngrid = GridLayout(cols=2, size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.8})

        btngrid.add_widget(MDRectangleFlatButton(text="Save", on_press=self.save_edited_transaction, pos_hint={"center_x": 0}, size_hint=(0.2, 0.2)))
        btngrid.add_widget(MDRectangleFlatButton(text="Cancel", on_press=self.dismiss_popup, pos_hint={"center_x": 1}, size_hint=(0.2, 0.2)))

        self.box.add_widget(btngrid)

        self.popup = Popup(title="Edit transaction", content=self.box, size_hint=(None, None), size=(400, 400))
        self.popup.open()

    def save_edited_transaction(self, obj):
        self.popup.dismiss()

        tx = self.transaction_history[int(self.last_ref) - 1]

        if tx['action'] == 'deposit':
            new_price = self.box.children[1].text
            new_name = ""
        else:
            print(self.box.children)
            new_price = self.box.children[2].text
            new_name = self.box.children[1].text


        if new_price == "" or (new_name == "" and tx['action'] == 'purchase'):
            self.show_error("Please fill in all fields")
            return
        
        if not new_price.isdigit():
            print(new_price, new_price.isdigit())
            self.show_error("Price must be a number")
            return
        
        new_price = int(new_price)

        if new_price > 1_000_000 and tx['action'] == 'deposit':
            self.show_error("You can't add 1m+ dabloons at once")
            return
        
        if tx['action'] == 'purchase':
            oldbal = self.dabloons + tx['price']
            newbal = oldbal - new_price
            if newbal < 0:
                self.show_error("You don't have enough dabloons")
                return

        elif tx['action'] == 'deposit':
            oldbal = self.dabloons - tx['price']
            newbal = oldbal + new_price

        self.dabloons = newbal#.data['dabloons']['credits'] = newbal
        self.main_text.text = f"Your dabloons: {self.dabloons}"


        self.transaction_history.edit(int(self.last_ref) - 1, "price", new_price)
        self.transaction_history.edit(int(self.last_ref) - 1, "name", new_name)

        self.show_history(obj)



    def dismiss_popup(self, obj):
        self.popup.dismiss()


MainApp().run()