import sqlite3 #sqlite kullanmak için öncelikle programımıza sqlite3 paketini import ediyoruz

#veritabanı oluşturmak ve o veritabanına erişmek için con değişkenini oluşturduk
con = sqlite3.connect("kütüphane.db")  #veritabanı uzantısının db olması gerekmekte
#kütüphane adında bir veri tabanı yoksa bu veritabanını oluşturur ve işlem yapabiliriz. ilgili veritabanı varsa doğrudan işlem yapabiliriz.

cursor =con.cursor() #bu veritababnında işlem yapmak için bizim bir tane imlece ihtiyacımız bulunmakta. bunun için de cursor değişkenini oluşturduk.

def tablo_olustur(): #veritabanı içinde tablo oluşturmak için fonksiyon yazacağız
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    #işlem yapmak için cursor'da gömülü olan execute fonksiyonunu kullandık. Text olarak İsim,Yazar,Yayınevi başlıklarını oluştururken Integer formunda da Sayfa_Sayısı başlığını oluşturduk)
    con.commit() #sorguyu çalıştırmak için bu fonksiyonu yazmamız gerekmekte. aksi halde fonksiyonu çalıştıramayız
    # programın oluşturulduğu dosyada db uzantılı, kütüphane isimli boş bir veritabanı oluşturduk.

def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    cursor.execute("Insert into kitaplık Values('İstanbul','Ümit','Everest',569)")
    cursor.execute("Insert into kitaplık Values('Ankara','Ahmet','can',946)")
    cursor.execute("Insert into kitaplık Values('Savaş Ve Barış','Kayahan','sel',946)")
    #büyük harf veya küçük harfle yazmanız bir şeyi değştirmez. sorgu her iki durumda da çalışır.
    #insert into sorgusu ile tabloya veri girişi yapacağız
    con.commit()
def kullanıcıdan_veri_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    #? işaretini kullanmamızın sebebi values komutunun içini sonradan dolduracağımız veriler için atama yapılacak alan oluşturulmasıdır.
    #4 tane soru işaretinin sırasıyla (isim,yazar,yayınevi,sayfa_sayısı) değerlerine denk geleceğini programa işliyoruz
    con.commit()

isim=input("İsim:")
yazar=input("Yazar:")
yayınevi=input("Yayınevi:")
sayfa_sayısı=int(input("Sayfa Sayısı:"))


tablo_olustur() #oluşturduğumuz fonksiyonu çalıştırarak veritabanında ilgili tabloyu oluşturduk
veri_ekle() #kütüphane.db klasörüne gelip Browse Data sekmesine tıkladığımızda oluşturulan veriyi görebiliriz.
kullanıcıdan_veri_ekle(isim,yazar,yayınevi,sayfa_sayısı) #eklenen veriler veritabanında kalıcı olarak durur.
# python dosyası kapansa ve sonradan tekrar çalıştırılsa bile daha önce eklenen veriler kullanıcı tarafından silinmediği sürece veritabanında kalır


con.close() #veritabanındaki işlemlerimiz bittikten sonra veritabanını kapattık

#programın oluşturulduğu dosyada db uzantılı, kütüphane isimli boş bir veritabanı oluşturduk.










