import re

# --- Network Configuration Auditor ---
# This script reads a configuration file and checks for basic security compliance.

def audit_config(config_file):
    """
    Reads a config file and runs a series of compliance checks.
    
    Args:
        config_file (str): The path to the configuration file to audit.
    """
    print(f"--- Starting Audit for: {config_file} ---")
    
    try:
        # Open and read the entire configuration file into a string
        with open(config_file, 'r') as f:
            config_text = f.read()

        # --- CHECK 1: Ensure a secure 'enable secret' is used over 'enable password' ---
        # re.search() finds the first occurrence of the pattern in the string.
        # re.MULTILINE allows '^' to match the start of each line, not just the start of the string.
        if re.search(r'^\s*enable secret', config_text, re.MULTILINE):
            print("[PASS] ✅ Secure 'enable secret' is configured.")
        else:
            print("[FAIL] ❌ 'enable secret' is missing. This is a critical security risk.")

        # --- CHECK 2: Ensure a warning banner is present to deter unauthorized access ---
        if re.search(r'^\s*banner motd', config_text, re.MULTILINE):
            print("[PASS] ✅ A warning banner (MOTD) is configured.")
        else:
            print("[FAIL] ❌ A warning banner is missing.")

        # --- CHECK 3: Ensure console line does not have an insecure password ---
        # This regex looks for 'password' under 'line con 0' which is insecure.
        if re.search(r'line con 0\n\s*password', config_text):
             print("[FAIL] ❌ Insecure password found on console line. Use 'login local'.")
        else:
             print("[PASS] ✅ Console line appears secure.")

        print("\n--- Audit Complete ---")

    except FileNotFoundError:
        print(f"\n[ERROR] The file '{config_file}' was not found. Please check the file path.")

# --- Main execution ---
if __name__ == "__main__":
    # The name of the configuration file to check.
    # Make sure this file is in the same directory as the script.
    config_filename = 'config.txt'
    audit_config(config_filename)
