# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:25:23 2022

@author: shilaaa
"""

while True:
    
 # Meminta input umur
 age = int(input("Masukkan umur: "))
 
 # Menghitung harga tiket
 if age < 3:
  price = 0
 elif age < 12:
  price = 14
 elif age < 65:
  price = 23
 else:
  price = 18
  
 # Menampilkan harga tiket
 print("Harga tiket: $" + str(price))
 
 # Menanyakan apakah pengunjung ingin menambahkan data lagi
 answer = input("Apakah anda ingin menambahkan data lagi? (Y/T) ").lower()
 
 # Jika iya, maka program akan meminta input umur lagi
 if answer == "y":
  continue

 # Jika tidak, maka program akan menampilkan total harga tiket
 elif answer == "t":
  print("Total harga tiket: $" + str(price))
  
 # Meminta input jumlah uang yang dibayarkan
 money = int(input("Masukkan jumlah uang yang dibayarkan: $"))
 
 # Jika uang yang dibayarkan kurang dari total harga tiket, maka program akan menampilkan "Uang anda kurang"
 if money < price:
  print("Uang anda kurang")
  
 # Jika uang yang dibayarkan lebih dari total harga tiket, maka program akan menampilkan "Uang anda lebih" dan "Silahkan ambil kembalian: $[jumlah uang yang lebih]"
 elif money > price:
  print("Uang anda lebih")
  print("Silahkan ambil kembalian: $" + str(money - price))
  
 # Jika uang yang dibayarkan pas dengan total harga tiket, maka program akan menampilkan "Uang anda pas"
 elif money == price:
  print("Uang anda pas")
 break

 # Jika input tidak sesuai, maka program akan menampilkan "Input tidak valid"
else:
 print("Input tidak valid")