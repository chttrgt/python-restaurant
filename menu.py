from colorama import Back,Fore,Style,init

MENU = {
    "Çorbalar": {
        "Mercimek Çorbası": 60,
        "Domates Çorbası": 55,
        "Tavuk Suyu Çorba": 75,
        "Ezogelin Çorbası": 65,
        "Yayla Çorbası": 65,
    },
    "Ana Yemekler": {
        "Tavuk Şiş": 180,
        "Köfte": 160,
        "Mantı": 150,
        "Karnıyarık": 170,
        "Sebzeli Makarna": 120,
    },
    "Tatlılar": {
        "Sütlaç": 80,
        "Kazandibi": 85,
        "Baklava": 120,
        "Profiterol": 110,
        "Cheesecake": 130,
    },
    "Salatalar": {
        "Çoban Salata": 70,
        "Mevsim Salata": 75,
        "Ton Balıklı Salata": 120,
        "Sezar Salata": 125,
        "Gavurdağı Salata": 95,
    },
    "Sıcak İçecekler": {
        "Türk Kahvesi": 45,
        "Latte": 70,
        "Çay": 20,
        "Sıcak Çikolata": 65,
        "Americano": 55,
    },
    "Soğuk İçecekler": {
        "Su": 10,
        "Ayran": 20,
        "Kola": 35,
        "Limonata": 40,
        "Soğuk Kahve": 75,
    },
}

CATEGORIES = list(MENU.keys())

def print_categories(inner_width):
    print("╔" + "═" * inner_width + "╗")
    print("║" + Back.BLACK + Fore.WHITE + Style.BRIGHT + f"📂 KATEGORİLER".ljust(inner_width - 1) + Style.RESET_ALL + "║")
    print("╠" + "═" * inner_width + "╣")

    i = 0
    while i < len(CATEGORIES):
        if i % 2 == 0:
            print("║" + Back.WHITE + Fore.BLACK + Style.BRIGHT + f"  {i + 1}) {CATEGORIES[i]}".ljust(inner_width) + Style.RESET_ALL + "║")
        else:
            print("║" + Back.BLACK + Fore.WHITE + Style.BRIGHT + f"  {i + 1}) {CATEGORIES[i]}".ljust(inner_width) + Style.RESET_ALL + "║")
        i += 1

    print("╠" + "═" * inner_width + "╣")
    print("║" + "👉 Seçim: 1-6".ljust(inner_width - 1) + "║")
    print("║" + "🛑 Bitir: 'e'".ljust(inner_width - 1) + "║")
    print("╚" + "═" * inner_width + "╝")

def print_products(inner_width,cat_name,products):
    print()
    print("╔" + "═" * inner_width + "╗")
    print("║" + Back.BLACK + Fore.WHITE + Style.BRIGHT  + f"📂 {cat_name}".upper().ljust(inner_width - 1) + Style.RESET_ALL + "║")
    print("╠" + "═" * inner_width + "╣")

    for i in range(0,len(products)):
     product_name,product_price = products[i]
     if i % 2 == 0:
        print("║" + Back.WHITE + Fore.BLACK + Style.BRIGHT + f"  {i + 1}) {product_name} - {product_price} TL".ljust(inner_width) + Style.RESET_ALL + "║")
     else:
        print("║" + Back.BLACK + Fore.WHITE + Style.BRIGHT + f"  {i + 1}) {product_name} - {product_price} TL".ljust(inner_width) + Style.RESET_ALL + "║")
    
     
    print("╠" + "═" * inner_width + "╣")
    print("║" + "👉 Ürün seçimi: 1-5".ljust(inner_width - 1) + "║")
    print("║" + "🛑 Geriye dön: 'q'".ljust(inner_width - 1) + "║")
    print("╚" + "═" * inner_width + "╝")