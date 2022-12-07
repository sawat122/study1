
"""Kullanıcı girişi yapmak"""




print("""****************************
    Kullanıcı Girişi
****************************""")

username ="zehra"
password = "1234"

user = input("Kullanıcı adınızı giriniz:")

if user == username:
    psw = input("Parolanızı giriniz: ")
    if psw ==password:
        print("Giriş Başarılı Hoşgeldiniz!!")
    else:
        print("Giriş Başarısız Tekrar Deneyiniz!")
else:
    print("Giriş Başarısız Tekrar Deneyiniz!") 
