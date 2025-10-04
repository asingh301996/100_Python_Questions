'''write a function to validate password which meets below criteria '
1. pwd min length 8
2. max lenghth 
3. must include upper case lower case or number 
'''

def validate_password_criteria(password):
    if 8  <= len(password) <= 15 :
      if hasUpperCase(password) and hasLowerCase(password) or hasNumber(password) and not hasSpecialChar(password):
        return "Password testing passed"
      else:
          return "Password testing failed for upper case lower case or number criteria"
    else:
        return "Password testing failed for length criteria"
    
def hasUpperCase(password):
    for char in password:
        if char.isupper():
            return True
        else:
            pass
    return False

def hasLowerCase(password):
    for char in password:
        if char.islower():
            return True
        else:
            pass
    return False  
def hasNumber(password):
    for char in password:
        if char.isdigit():
            return True
        else:
            pass
    return False

def hasSpecialChar(password):
    
    for char in password:
        if char in special_characters:
            return True
        else:
            pass
    return False

password = input("Enter the password for login")
print (validate_password_criteria(password)) 


    
    