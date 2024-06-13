from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database.db_sqlite import Database
from pprint import pprint

baza = Database(path_to_db="main.sqlite3")

result = baza.check_user_order_exists(1664504095,6,300,2)
print(result)


# # import sqlite3
# # con = sqlite3.connect('main.sqlite3')
# # cur = con.cursor()
# # sql = '''DROP TABLE Orders;'''
# # cur.execute(sql)
# # con.commit()
# # con.close()


# # baza.create_category_table()
# # baza.create_users_table()
# # baza.create_products_table()
# # baza.create_orders_table()
# # baza.create_product_types_table()
# # baza.create_locations_table()

# # baza.create_product_types_table()

# # baza.add_category('Lavash', 'images/categories/Lavash.jpg')
# # baza.add_category('Trindwich', 'images/categories/Trindwich.jpg')
# # baza.add_category('Shaurma', 'images/categories/shaurma.jpg')
# # baza.add_category('Burger', 'images/categories/burger.jpg')
# # baza.add_category('Sub', 'images/categories/sub.jpg')
# # baza.add_category('Kartoshka', 'images/categories/kartoshka4.jpg')
# # baza.add_category('Hot Dog', 'images/categories/hot-dog.jpg')
# # baza.add_category('Sneklar', 'images/categories/senki.jpg')
# # baza.add_category('Salat, garnir, non', 'images/categories/salad.jpg')
# # baza.add_category('Souslar', 'images/categories/sause.jpg')
# # baza.add_category('Setlar', 'images/categories/sets.jpg')
# # baza.add_category('Desertlar', 'images/categories/desserts.jpg')
# # baza.add_category('Issiq ichimliklar', 'images/categories/hot drinks.jpg')
# # baza.add_category('Sovuq ichimliklar', 'images/categories/cold drinks.jpg')
# # baza.add_category('Combo', 'images/categories/combo.jpg')

# # baza.add_products("Tovuq go`shtidan lavash", 'images/lavash/Tovuq goshtidan lavash.jpg','Lavash',)
# # baza.add_products("Mol go'shtidan pishloqli lavash", 'images/lavash/Mol goshtidan pishloqli lavash.jpg','Lavash',)
# # baza.add_products("Mol go'shtidan qalampir lavash", 'images/lavash/Mol goshtidan qalampir lavash.jpg','Lavash',)
# # baza.add_products("Tovuq go'shtidan qalampir lavash", 'images/lavash/Tovuq goshtidan qalampir lavash.jpg.','Lavash',)
# # baza.add_products("Tovuq go`shtidan pishloqli lavash", 'images/lavash/Tovuq goshtidan pishloqli lavash.jpg','Lavash',)
# # baza.add_products("Fitter", 'images/lavash/Fitter.jpg','Lavash',)
# # baza.add_products("Mol go`shtidan lavash", 'images/lavash/Mol goshtidan lavash.jpg',category_name='Lavash',)



# # baza.add_product_type('Mini', 25000, "Tovuq go`shtidan pishloqli lavash")
# # baza.add_product_type('Big', 35000, "Tovuq go`shtidan pishloqli lavash")

# # baza.add_product_type('Mini', 20000, "Tovuq go'shtidan qalampir lavash")
# # baza.add_product_type('Big', 30000, "Tovuq go'shtidan qalampir lavash")

# # baza.add_product_type('Mini', 20000, "Mol go'shtidan qalampir lavash")
# # baza.add_product_type('Big', 20000, "Mol go'shtidan qalampir lavash")

# # baza.add_product_type('Mini', 24000, "Mol go'shtidan pishloqli lavash")
# # baza.add_product_type('Big', 36000, "Mol go'shtidan pishloqli lavash")

# # baza.add_product_description("Mol go'shtidan pishloqli lavash", "mol go'shti bo'lakchalaridan ajoyib lavash, yeganingizda yengil tamni xis qiling va ushbu taomdan rohatlaning")
# # result = baza.get_product_types(product_name="Mol go'shtidan pishloqli lavash")

# # data = baza.get_products_by_categories(category_name='Lavash')
# # pprint(data)

# # def sort_user_products(tg_id: int):
# #     data = baza.get_order(tg_id)
# #     for user_id, product_id, quantity in data:
# #         print(
# #             f"{user_id=}"
# #         )
# #         print(
# #             f"product name: {baza.get_product_name(product_id)[0]}"
# #         )
# #         print(
# #             f"{quantity=}"
# #         )

# # sort_user_products(1058730773)







# baza.add_products("Trindwich tovuq go'shtidan", 'images/Trindwich/Trindwich tovuq goshtidan.jpg','Trindwich',)
# baza.add_products("Trindwich mol go'shtidan", 'images/Trindwich/Trindwich mol goshtidan.jpg','Trindwich',)



# baza.add_products("Mol go'shtidan qalampir shaurma", 'images/shaurma/Mol goshtidan qalampir shaurma.jpg','Shaurma',)
# baza.add_product_type("Mini",24000,"Mol go'shtidan qalampir shaurma")
# baza.add_product_type("Big",28000,"Mol go'shtidan qalampir shaurma")
# baza.add_products("Tovuq go'shtidan shaurma", 'images/shaurma/Tovuq goshtidan shaurma.jpg','Shaurma',)
# baza.add_product_type("Mini",23000,"Tovuq go'shtidan shaurma")
# baza.add_product_type("Big",26000,"Tovuq go'shtidan shaurma")
# baza.add_products("Tovuq go'shtidan qalampir shaurma", 'images/shaurma/Tovuq goshtidan qalampir shaurma.jpg','Shaurma',)
# baza.add_product_type("Mini",23000,"Tovuq go'shtidan qalampir shaurma")
# baza.add_product_type("Big",26000,"Tovuq go'shtidan qalampir shaurma")
# baza.add_products("Mol go'shtidan shaurma", 'images/shaurma/Mol goshtidan shaurma.jpg','Shaurma',)
# baza.add_product_type("Mini",24000,"Mol go'shtidan shaurma")
# baza.add_product_type("Big",28000,"Mol go'shtidan shaurma")


# baza.add_products("Gamburger", 'images/Burger/Gamburger.jpg','Burger',)
# baza.add_products("Dablburger", 'images/Burger/Dablburger.jpg','Burger',)
# baza.add_products("Chizburger", 'images/Burger/Chizburger.jpg','Burger',)
# baza.add_products("Dablchizburger", 'images/Burger/Dablchizburger.jpg','Burger',)

# baza.add_products("Tovuq go`shtidan sab", 'images/Sub/Tovuq goshtidan sab.jpg','Sub',)
# baza.add_products("Tovuq go`shtidan pishloqli sab", 'images/Sub/Tovuq goshtidan pishloqli sab.jpg','Sub',)
# baza.add_products("Mol go`shtidan pishloqli sab", 'images/Sub/Mol goshtidan pishloqli sab.jpg','Sub',)
# baza.add_products("Mol go`shtidan sab", 'images/Sub/Mol goshtidan sab.jpg','Sub',)

# baza.add_products("Jaydari kartoshka", 'images/Kartoshka/Jaydari kartoshka.jpg','Kartoshka',)
# baza.add_products("Kartoshka Fri", 'images/Kartoshka/Kartoshka Fri.jpg','Kartoshka',)
# baza.add_products("Naggetslar, 4 dona", 'images/Kartoshka/Naggetslar, 4 dona.jpg','Kartoshka',)
# baza.add_products("Naggetslar, 8 dona", 'images/Kartoshka/Naggetslar, 8 dona.jpg','Kartoshka',)


# baza.add_products("Hot-Dog", 'images\Hot dog\Hot-dog.jpg','Hot Dog',)
# baza.add_products("Hot-Dog-Dabl", 'images/Hot dog/Hot-Dog-Dabl.jpg','Hot Dog',)
# baza.add_products("Bolalar uchun Hot-Dog", 'images/Hot dog/Bolalar uchun Hot-Dog.jpg','Hot Dog',)
# baza.add_products("Hot-Dog Mini", 'images/Hot dog/Hot-Dog Mini.jpg','Hot Dog',)


# baza.add_products("Smayliki", 'images/Sneklar/Smayliki.jpg','Sneklar',)
# baza.add_products("Strips", 'images/Sneklar/Strips.jpg','Sneklar',)


# baza.add_products("Guruch", 'images/Salat, garnir, non/Guruch.jpg','Salat, garnir, non',)
# baza.add_products("Non", 'images/Salat, garnir, non/Non.jpg','Salat, garnir, non',)
# baza.add_products("Salat", 'images/Salat, garnir, non/Salat.jpg','Salat, garnir, non',)
# baza.add_products("Sezar salat", 'images/Salat, garnir, non/Sezar salat.jpg','Salat, garnir, non',)
# baza.add_products("Grecheskiy salat", 'images/Salat, garnir, non/Grecheskiy salat.jpg','Salat, garnir, non',)

# baza.add_products("Ketchup", 'images/Souslar/Ketchup.jpg','Souslar',)
# baza.add_products("Sezar sous", 'images/Souslar/Sezar sous.jpg','Souslar',)
# baza.add_products("Grecheskiy sous", 'images/Souslar/Grecheskiy sous.jpg','Souslar',)
# baza.add_products("Chili sous", 'images/Souslar/Chili sous.jpg','Souslar',)
# baza.add_products("Sarimsoqli sous", 'images/Souslar/Sarimsoqli sous.jpg','Souslar',)
# baza.add_products("Pishloqli sous", 'images/Souslar/Pishloqli sous.jpg','Souslar',)
# baza.add_products("Barbekyu sousi", 'images/Souslar/Barbekyu sousi.jpg','Souslar',)
# baza.add_products("Mayonez", 'images/Souslar/Mayonez.jpg','Souslar',)


# baza.add_products("COMBO PLUS", 'images/Setlar/COMBO PLUS.jpg','Setlar',)
# baza.add_products("COMBO PLUS isituvchan (ko'k choy)", "images/Setlar/COMBO PLUS isituvchan (ko'k choy).jpg",'Setlar',)
# baza.add_products("Mol go'shtidan donar", "images/Setlar/Mol goshtidan donar.jpg",'Setlar',)
# baza.add_products("FitCombo", 'images/Setlar/FitCombo.jpg','Setlar',)
# baza.add_products("Tovuq go'shtidan donar", 'images/Setlar/Tovuq goshtidan donar.jpg','Setlar',)
# baza.add_products("COMBO PLUS isituvchan (qora choy)", 'images/Setlar/COMBO PLUS isituvchan (qora choy).jpg','Setlar',)
# baza.add_products("Bolalar uchun Combo", 'images/Setlar/Bolalar uchun Combo.jpg','Setlar',)
# baza.add_products("Donar-box tovuq go'shtli", 'images/Setlar/Donar-box tovuq goshtli.jpg','Setlar',)
# baza.add_products("Donar-box mol go'shtli", 'images/Setlar/Donar-box mol goshtli.jpg','Setlar',)

# baza.add_products("Karameli donut", 'images/Desertlar/Karameli donut.jpg','Desertlar',)
# baza.add_products("Mevali Donut", 'images/Desertlar/Mevali Donut.jpg','Desertlar',)

# baza.add_products("Limonli kok choy", 'images/Issiq ichimliklar/Limonli kok choy.jpg','Issiq ichimliklar',)
# baza.add_products("Kofe Latte", 'images/Issiq ichimliklar/Kofe Latte.jpg','Issiq ichimliklar',)
# baza.add_products("Limonli qora choy", 'images/Issiq ichimliklar/Limonli qora choy.jpg','Issiq ichimliklar',)
# baza.add_products("Qora choy", 'images/Issiq ichimliklar/Qora choy.jpg','Issiq ichimliklar',)
# baza.add_products("Kok choy", 'images/Issiq ichimliklar/ Kok choy.jpg','Issiq ichimliklar',)
# baza.add_products("Kapuchino", 'images/Issiq ichimliklar/Kapuchino.jpg','Issiq ichimliklar',)
# baza.add_products("Amerikano", 'images/Issiq ichimliklar/Amerikano.jpg','Issiq ichimliklar',)
# baza.add_products("Malina va smorodinali Punsh", 'images/Issiq ichimliklar/Malina va smorodinali Punsh.jpg','Issiq ichimliklar',)

# baza.add_products("Olmali sharbat shakarsiz, 0,33L", 'images/Sovuq ichimliklar/Olmali sharbat shakarsiz, 0,33L.jpg','Sovuq ichimliklar',)
# baza.add_products("Gazlangan suv 0.5L", 'images/Sovuq ichimliklar/Gazlangan suv 0.5L.jpg','Sovuq ichimliklar',)
# baza.add_products("7up razliv", 'images/Sovuq ichimliklar/7up razliv.jpg','Sovuq ichimliklar',)
# baza.add_products("“Chortoq” tozalangan gazsiz ichimlik suvi, 0,5 L", 'images/Sovuq ichimliklar/Chortoq tozalangan gazsiz ichimlik suvi, 0,5 L.jpg','Sovuq ichimliklar',)
# baza.add_products("Olmali sharbat, 1 L", 'images/Sovuq ichimliklar/Olmali sharbat, 1 L.jpg','Sovuq ichimliklar',)
# baza.add_products("Stakan 200ml", 'images/Sovuq ichimliklar/Stakan 200ml.jpg','Sovuq ichimliklar',)
# baza.add_products("Pepsi 0,5L", 'images/Sovuq ichimliklar/Pepsi 0,5L.jpg','Sovuq ichimliklar',)
# baza.add_products("Pepsi 1,5L", 'images/Sovuq ichimliklar/Pepsi 1,5L.jpg','Sovuq ichimliklar',)
# baza.add_products("Pepsi razliv", 'images/Sovuq ichimliklar/Pepsi razliv.jpg','Sovuq ichimliklar',)
# baza.add_products("Moxito", 'images/Sovuq ichimliklar/Moxito.jpg','Sovuq ichimliklar',)
# baza.add_products("Pina colada", 'images/Sovuq ichimliklar/Pina colada.jpg','Sovuq ichimliklar',)
# baza.add_products("Mirinda razliv", 'images/Sovuq ichimliklar/Mirinda razliv.jpg','Sovuq ichimliklar',)
# baza.add_products("Olchali sharbat, 1 L", 'images/Sovuq ichimliklar/Olchali sharbat, 1 L.jpg','Sovuq ichimliklar',)
# baza.add_products("Apelsinli sharbat, 1 L", 'images/Sovuq ichimliklar/Apelsinli sharbat, 1 L.jpg','Sovuq ichimliklar',)


# baza.add_products("Talaba-Combo", 'images/Combo/Talaba-Combo.jpg','Combo',)
# baza.add_products("Sport-Combo", 'images/Combo/Sport-Combo.jpg','Combo',)
# baza.add_products("M-Combo №1", 'images/Combo/M-Combo .jpg','Combo',)
# baza.add_products("M-Combo №2", 'images/Combo/M-Combo .jpg','Combo',)
# baza.add_products("S-Combo №1", 'images/Combo/S-Combo 1.jpg','Combo',)
# baza.add_products("S-Combo №2", 'images/Combo/S-Combo 2.jpg','Combo',)
# baza.add_products("S-Combo №3", 'images/Combo/S-Combo 3.jpg','Combo',)
# baza.add_products("S-Combo №4", 'images/Combo/S-Combo 4.jpg','Combo',)
# baza.add_products("Double - Combo №1", 'images/Combo/Double - Combo 1.jpg','Combo',)
# baza.add_products("Double - Combo  №2", 'images/Combo/Double - Combo  2.jpg','Combo',)
# baza.add_products("Double - Combo №3", 'images/Combo/Double - Combo 3.jpg','Combo',)
# baza.add_products("Double - Combo №4", 'images/Combo/Double - Combo 4.jpg','Combo',)
# baza.add_products("Oilaviy-Combo №1", 'images/Combo/Oilaviy-Combo 1.jpg','Combo',)
# baza.add_products("Oilaviy-Combo №2", 'images/Combo/Oilaviy-Combo 2.jpg','Combo',)
# baza.add_products("Combo Plus 7up", 'images/Combo/Combo Plus 7up.jpg','Combo',)









