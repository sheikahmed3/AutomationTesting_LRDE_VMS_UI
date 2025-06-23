import random
import string
import re

def generate_department_name():
    # Allowed characters: letters + digits
    letters = string.ascii_letters
    digits = string.digits
    allowed = letters + digits

    # Generate a clean random name, e.g., 'DevTeam123'
    base = ''.join(random.choices(allowed, k=10))

    # Capitalize first letter
    base = base[0].upper() + base[1:]

    # Replace spaces with underscore (just in case)
    base = base.replace(" ", "_")

    # Final clean: allow only alphanumeric and underscore
    return re.sub(r'[^a-zA-Z0-9_]', '', base)
