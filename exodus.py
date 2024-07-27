import base64
import os
from colorama import init, Fore, Style

def obfuscate_python(program, key):
    obfuscated_program = "".join(chr(ord(c) ^ key) for c in program)
    
    encoded = base64.b64encode(obfuscated_program.encode()).decode()
    
    obfuscated_code = '__31c050682f2f7368682f62696e89e3505389e1b00bcd80___31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__ = ""\n'
    for i in range(0, len(encoded), 10):
        chunk = encoded[i:i+10]
        hex_chunk = ''.join(['\\x{:02x}'.format(ord(c)) for c in chunk])
        obfuscated_code += '__31c050682f2f7368682f62696e89e3505389e1b00bcd80___31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__ += "{}"\n'.format(hex_chunk)
    
    obfuscated_code += 'exec("".join(chr(ord(c) ^ {}) for c in __import__("base64").b64decode(__31c050682f2f7368682f62696e89e3505389e1b00bcd80___31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__31c050682f2f7368682f62696e89e3505389e1b00bcd80__).decode()))'.format(key)
    return obfuscated_code


def main():
    try:
        init(autoreset=True)
        
        pink_color = "\033[38;2;255;69;172m"
        reset = "\033[0m"
        banner = f'''
{pink_color}    
 ____  _  _______  ____ _ ____  _ __ 
| ____\ \/ / _ \|  _ \| | | / ___| 
|  _|  \  / | | | | | | | | \___ \ 
| |___ /  \ |_| | |_| | |_| |___) |
|_____/_/\_\___/|____/ \___/|____/            
     
                                                
             Author: Nathaneal Meththananda
             Handle: APT0xSnowdox 
{reset}'''
        print(banner)
        
        print(Fore.CYAN + "PROGRAM EXECUTION BEGIN")
        
        python_code = input(Fore.YELLOW + "Enter the path for the python program (press enter to type the program path): " + Style.RESET_ALL)
        if not python_code:
            program_path = input(Fore.YELLOW + "Enter your python program path: " + Style.RESET_ALL)
            while not os.path.exists(program_path):
                print(Fore.RED + "Invalid path. Please try again.")
                program_path = input(Fore.YELLOW + "Enter your python program path: " + Style.RESET_ALL)
            with open(program_path, 'r') as file:
                python_code = file.read()
        
        obfuscated_program_name = input(Fore.YELLOW + "Enter your obfuscated program name (default obfuscate.py): " + Style.RESET_ALL)
        if not obfuscated_program_name:
            obfuscated_program_name = "obfuscate.py"
        
        key = 0x7F
        
        obfuscated_code = obfuscate_python(python_code, key)
        
        with open(obfuscated_program_name, 'w') as file:
            file.write(obfuscated_code)
        
        print(Fore.GREEN + f"Obfuscated program has been saved as {obfuscated_program_name}")

    except KeyboardInterrupt:
        print(Fore.RED + "\nOperation cancelled by user. Exiting...")

if __name__ == "__main__":
    main()
