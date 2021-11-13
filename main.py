from worker import alisa, mainA1
# Powered By Abdurazzoq
print('Assalomu alaykum')
print('Dasturimizga Hush kelibsiz')
print('Men siz bilan gaplasha olaman ')
print('Buyruqlar: lotin_morze, krill_lotin')

while True:
   query = input('... ').lower().strip()

   try:
      if query == 'krill_lotin':
         dns = input(">> ")

         print(mainA1(dns, 'k_l'))

      elif query == 'lotin_morze':
         dns = input(">> ")

         print(mainA1(dns,'l_m','morze'))

      else:
         print(alisa(query, 'asosiy'))
   except:
      print('Dasturda Xatolik Bor, Menimcha Bazada mavjud bo\'lmagan so\'z kiritildi')

