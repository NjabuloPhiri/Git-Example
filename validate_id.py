# A function to calculate two numbers

id = input("Please enter your id no.: ")
valid_ids_list = ["0123456789123"]

def validate_user_id():
    # Check if id has 13 characters
    id_len = len(id)

    for i in valid_ids_list:
        if id == i:
            valid_ids_list.remove(i)
            print("Id already exists.")

    if id_len == 13:
        valid_ids_list.append(id)
        print("Your id no. is valid")
    elif id_len > 13:
        print("The id chars are more than 13")
    else:
        print("Your id no. is less than 13.")
    
    # Check against valid ids list
    
    

    print(valid_ids_list)

validate_user_id()