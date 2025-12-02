#PASSWORD STRENGTH CHECKER
def is_strong(password):
    """
    Checks if the provided password is strong
    A strong password must :
    - Be at least 8 characters long
    - Contain at least one digit
    - Contain at least one lowercase letter
    - Contain at least one uppercase letter
    - Contain at least one special character 
    """
    special_characters = "!@#$%^&*()_+[]{}|;:',.<>/?"
    if len(password)<8:
        return "password must be 8 characters long "
    if not any(char.isdigit() for char in password):
        return "password must include at least one number"
    if not any(char.islower() for char in password):
        return "password must include at least one lowercase letter"
    if not any(char.isupper() for char in password):
        return "password must include at least one uppercase letter"
    if not any(char in special_characters for char in password):
        return "password must include at least one special character"
    return "password is strong"

pwd = input("enter password : ")
result = is_strong(pwd)
print(result)
    