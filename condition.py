import re
import socket
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
        return False  

    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False