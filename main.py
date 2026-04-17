#region IMPORTS
import sys
from welcome import welcome_text
from menu import MENU,CATEGORIES
from colorama import Fore,Style,init
#endregion

#region UNICODE KARAKTERLERİNİN DÜZGÜN BİR ŞEKİLDE ENCODE EDİLEBİLMESİ İÇİN KULLANDIK
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")
#endregion

init(autoreset=True)
print(welcome_text)

cart={}, total=0, cat_counts=len(CATEGORIES)

