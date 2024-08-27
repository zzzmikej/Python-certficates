import sys
import io
from config.config import bank

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

name_bank = bank

def show_menu():
    print("""
╔═════════════════════════════════════════════╗
║           Bem Vindo ao Banco {}           ║
╠═════════════════════════════════════════════╣
║   Selecione a função que deseja realizar!   ║
║                                             ║
╟ 1. Abrir a conta                            ║
╟ 2. Acesso a Conta                           ║
╟ 3. Acesso com Biometria                     ║
╟ 4. Saque                                    ║
╟ 5. Deposito                                 ║
╟ 6. Transferência                            ║
╟ 7. Encerrar                                 ║
╚═════════════════════════════════════════════╝
""".format(name_bank))