import re
import os
def valid_mail(mail):
    """
    Validates the format of an email address using regex.

    Parameters:
    - mail (str): The email address to validate.

    Returns:
    - bool: True if the email has a valid format, False otherwise.
    """
    # Regex pattern explanation:
    # ^            → start of string
    # [a-zA-Z0-9._%+-]+ → one or more allowed characters in the username
    # @            → must contain @
    # [a-zA-Z0-9.-]+   → one or more allowed characters in domain
    # \.           → literal dot
    # [a-zA-Z]{2,}$   → top-level domain (at least 2 letters)
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    return bool(re.match(pattern, mail))

def valid_domain(mail):
    """
    Checks if the domain of an email address is reachable via ping.

    The function extracts the domain part after '@', 
    then tries to ping it. Returns True if the ping succeeds 
    (domain is reachable), otherwise returns False.
    If the email has no '@', returns False.

    Parameters:
    - mail (str): The email address to check.

    Returns:
    - bool: True if the domain is reachable, False otherwise.
    """
    try:
        domain = mail.split("@")[1]
    except IndexError:
        return False  # invalid email, no '@'

    # Send only 1 ping packet depending on the OS
    param = "-n 1" if os.name == "nt" else "-c 1"
    # Suppress output in the console
    ans = os.system(
        f"ping {param} {domain} >nul 2>&1"
        if os.name == "nt"
        else f"ping {param} {domain} >/dev/null 2>&1"
    )
    return ans == 0