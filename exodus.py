import argparse
import base64
import os
from colorama import init, Fore

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

def print_banner():
    pink_color = "\033[38;2;255;69;172m"
    reset = "\033[0m"
    banner = rf'''
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

def get_python_code(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return file.read()
    else:
        raise FileNotFoundError(f"File not found: {filepath}")

def save_obfuscated_code(obfuscated_code, filename):
    with open(filename, 'w') as file:
        file.write(obfuscated_code)
    print(Fore.GREEN + f"Obfuscated program has been saved as {filename}")

def verify_xor_key(key):
    if 0 <= key <= 255:
        return key
    else:
        raise argparse.ArgumentTypeError(f"Invalid XOR key: {key}. Must be an integer between 0 and 255.")

def main():
    try:
        init(autoreset=True)
        
        parser = argparse.ArgumentParser(description='Python Code Obfuscation Tool')
        parser.add_argument('-i', '--input', required=True, help='Path to the input Python file')
        parser.add_argument('-o', '--output', default='obfuscate.py', help='Path to save the obfuscated Python file (default: obfuscate.py)')
        parser.add_argument('-k', '--key', type=verify_xor_key, default=127, help='XOR key for obfuscation (default: 127)')
        args = parser.parse_args()

        print_banner()
        
        print(Fore.CYAN + "PROGRAM EXECUTION BEGIN")
        
        python_code = get_python_code(args.input)
        obfuscated_code = obfuscate_python(python_code, args.key)
        save_obfuscated_code(obfuscated_code, args.output)

    except KeyboardInterrupt:
        print(Fore.RED + "\nOperation cancelled by user. Exiting...")
    except FileNotFoundError as e:
        print(Fore.RED + f"Error: {e}")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    main()
