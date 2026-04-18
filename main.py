#region IMPORTS
import sys
import msvcrt
from colorama import Back,Fore,Style,init
from welcome import welcome_text
from tools import clear_console
from menu import MENU,CATEGORIES,print_categories,print_products
#endregion

#region UNICODE KARAKTERLERİNİN DÜZGÜN BİR ŞEKİLDE ENCODE EDİLEBİLMESİ İÇİN KULLANDIK
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")
#endregion

init(autoreset=True)
UNDERLINE = "\033[4m"

print(welcome_text)

cart,total={},0 
print_categories(30)

while True:
    print("Lütfen kategori seçimi yapınız (1-6 | e): ", end="", flush=True)
    select_category = msvcrt.getwch().lower()
    if select_category == "e":
        print("\r\033[2K", end="")
        break
    print()

    if select_category.isdigit() == False:
        print(f"{Fore.RED} Hatalı seçim yatpınız! Kategori seçimi için (1-6) arasında bir tuşa basmalısınız. {Style.RESET_ALL}")
        continue

    cat_no=int(select_category)    
    if not (1<=cat_no<=len(CATEGORIES)):
        print(f"{Fore.RED} Hatalı seçim yatpınız! Kategori seçimi için (1-6) arasında bir tuşa basmalısınız. {Style.RESET_ALL}")
        continue

    cat_name=CATEGORIES[cat_no - 1]
    cat_of_products=MENU[cat_name]
    products=list(cat_of_products.items())
 
    print_products(30,cat_name,products)    

    while True:
        print("Lütfen ürün seçimi yapınız (1-5 | q): ", end="")
        select_product = msvcrt.getwch().strip().lower()

        if select_product=="q":
          clear_console()
          print_categories(30)
          break

        if select_product.isdigit() == False:
            print(f"{Fore.RED} Hatalı seçim yatpınız! Ürün seçimi için (1-5) arasında bir tuşa basmalısınız. {Style.RESET_ALL}")
            continue

        pro_no=int(select_product)
        if not (1<=pro_no<=len(products)):
            print(f"{Fore.RED} Hatalı seçim yatpınız! Ürün seçimi için (1-5) arasında bir tuşa basmalısınız. {Style.RESET_ALL}")
            continue

        product_name,product_price=products[pro_no - 1]

        if product_name in cart:
            cart[product_name]["adet"] += 1
        else:
            cart[product_name]={"adet":1,"fiyat":product_price,"kategori":cat_name}

        total += product_price
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + f"{product_name} {Style.RESET_ALL} ürünü eklendi." + Style.RESET_ALL)
        print(Back.CYAN + Fore.BLACK + Style.BRIGHT + f"Güncel toplam: {total} TL" + Style.RESET_ALL)
        print()

print()

if total == 0:
    print("Sipariş vermeden çıkış yaptınız. Yine bekleriz!")
else:
    cart_count = len(cart)
    print( Style.BRIGHT + UNDERLINE  + f"🍴 {"Siparişleriniz" if cart_count > 1 else "Siparişiniz"} " + Style.RESET_ALL)

    for category in CATEGORIES:
        products_in_category = [
            pname for pname in cart
            if cart[pname]["kategori"] == category
        ]

        if products_in_category:
            print(f"\n  {Back.YELLOW + Fore.BLACK + Style.BRIGHT + category + Style.RESET_ALL}")

            for pname in products_in_category:
                quantity = cart[pname]["adet"]
                price = cart[pname]["fiyat"]
                if products_in_category.index(pname) % 2 == 0:
                    print(Back.BLACK + Fore.WHITE + Style.BRIGHT + f"  - {pname} ({quantity} x {price} = {quantity * price} TL)" + Style.RESET_ALL)
                else:
                    print(Back.WHITE + Fore.BLACK + Style.BRIGHT + f"  - {pname} ({quantity} x {price} = {quantity * price} TL)" + Style.RESET_ALL)
                
    print()
    print(Back.CYAN + Fore.BLACK + Style.BRIGHT + f"Ödemeniz gereken toplam tutar: {total} TL" + Style.RESET_ALL)
    print()


    while True:
        payment = input("Lütfen ödeme yapmak istediğiniz tutarı giriniz: ").strip()

        if payment.isdigit() == False:
            print(f"{Fore.RED} Hatalı giriş yatpınız! Ödeme yapmak istediğiniz tutarı bir sayı olarak giriniz. {Style.RESET_ALL}")
            continue
        
        paid_amount = int(payment)

        if paid_amount < total:
            print(Fore.RED +"Ödeme yapmak istediğiniz tutar toplam tutardan düşük olamaz."+ Style.RESET_ALL)
            print(Style.BRIGHT + Fore.WHITE + Back.RED + f"Eksik bakiye: {total - paid_amount} TL" + Style.RESET_ALL)
            continue
        else:
           change = paid_amount - total
           print()
           print(Fore.GREEN + f"Ödeme alındı: {paid_amount} TL" + Style.RESET_ALL)
           print(Fore.GREEN + f"Para üstü: {change} TL" + Style.RESET_ALL)
           print()
           print(Back.GREEN + Fore.BLACK + Style.BRIGHT + f"❤️ TEŞEKKÜRLER! YİNE BEKLERİZ!❤️" + Style.RESET_ALL)
           break
  