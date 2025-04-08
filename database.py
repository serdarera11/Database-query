import time

print("Welcome to database")
site = input("Database sitesi(https/http/www/.com eklemeyin örn:eray): ")
time.sleep(2)
print(f"[*]{site}_setah1234")
print("[*]information_shema")
time.sleep(1)
input("Hangisini çekmek istiyorsunuz(sonuna --tables ekleyin): ")
time.sleep(2)

# Tablo ismi
print("""
+----+----------+ 
| users   |            
+----+----------+
""")
print("User bilgileri alınıyor..")
time.sleep(5)

# Column bilgileri
print("""
+----+----------+   | 
|    id      |  
| password   |
| username   |
+----+----------+
""")
print("Bilgiler alınıyor..")
# Veritabanı içeriği
print("""
# Veritabanı içeriği burada
+----+----------+-------------+---------------------+
| id | username | password    | email               |
+----+----------+-------------+---------------------+
| 1  | admin    | admin123    | admin@gmail.com   |
| 2  | eray     | kralserdar123 | eray@gmail.com   |
| 3  | ahmet      | gizli123    | ahmet@gmail.com    |
+----+----------+-------------+---------------------+
""")
