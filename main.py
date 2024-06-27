def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    """
    result = False
    
    if email[0].isalpha():
        
        if 5 < len(email) < 30:
            # Checks 'if' there is an '@' in email
            if "@" in email:
                at_index = email.find("@")
            
                if "." in email[at_index:]:
                
                    result = True
                
                print(result)
                
    
    
    
    
    """
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
