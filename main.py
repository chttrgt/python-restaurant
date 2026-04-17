#region IMPORTS
import sys
import msvcrt
from colorama import Fore,Style,init
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
print(welcome_text)

cart,total={},0 
print_categories(30)

while True:
    print("Lütfen kategori seçimi yapınız (1-6 | e): ", end="")
    select_category= msvcrt.getch().decode("utf-8").strip().lower()
    print()
    
    if select_category =="e":
        break

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
        select_product= msvcrt.getch().decode("utf-8").strip().lower()

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
        print(f"Eklendi: {product_name}")
        print(Fore.CYAN + f"Güncel toplam: {total} TL" + Style.RESET_ALL)
        print()

    