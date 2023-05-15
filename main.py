def choose_swap ():
    swap_array = []
    swaps_done = 1
    swaps_amount = int(input("How many latter swaps do you want to perform?: "))
    while swaps_done <= swaps_amount:
        swap_pair = input(f"Please enter what pair of letter you want to swap? ({swaps_done}/{swaps_amount}) (Remember, you can not mention the same letter twice!): ")
        first_swap_letter = swap_pair[0].upper()
        last_swap_letter = swap_pair[-1].upper()
        #check if the input contains only letters
        if first_swap_letter.isalpha() and last_swap_letter.isalpha():
            print(f"\nThe first letter is {first_swap_letter}, \nThe second one is {last_swap_letter}\n")
            
            #check if the input does not contain duplicates
            if first_swap_letter in swap_array or last_swap_letter in swap_array or first_swap_letter == last_swap_letter:
                print("Error! You can not mention the same letter twice!")
            else:
                swap_array.append(first_swap_letter)
                swap_array.append(last_swap_letter)
                swaps_done += 1
                print(f"These letters will be swapped {swap_array}")
        else: 
            print("At least one of the elements is not a character! Discarding this input. Try again \n")
 
    return swap_array

def choose_rotors ():
    chosen_rotors = []  
    i = 1
    while i <= 3:
        rotor_number = int(input(f"\nPlease, enter a number of the rotor #{i}: "))
        if rotor_number >= 1 and rotor_number <= 5:
            if rotor_number not in chosen_rotors:
                chosen_rotors.append(rotor_number)
                i += 1
            else:
                print("You can not name the same rotor twice")
        else:
            print("Error! You have to chose between 1 to 5")
    print(f"Your rotors are {chosen_rotors}")
    return chosen_rotors

def choose_offsets ():
    offset_array = []      
    i = 1
    while i <= 3:
        offset = int(input(f"\nPlease, enter the offset of the rotor #{i}: "))
        if offset >= 0 and offset <= len(alphabet) - 1:
            offset_array.append(offset)
            i += 1
        else:
            print("You can not use offset bigger than 25")
    print(f"Your offsets are {offset_array}")
    return offset_array

def get_swapped_alphabet (alphabet, swap):
    swap_position = []
    for i in range (0, len(swap)):
        letter_position = alphabet.index(swap[i])
        swap_position.append(letter_position)
    # print(f"swap_position = {swap_position}")
    
    for i in range(0, int(len(swap)/2)):
        j = i*2
        alphabet[swap_position[j]], alphabet[swap_position[j+1]] = alphabet[swap_position[j+1]], alphabet[swap_position[j]] 
    # print(f"Swaped alphabet = {alphabet}")
    return alphabet
    
def get_rotors_with_offset (rotors, offsets):
    """Decides what rotors to pick and what offset to add to them.

    Args:
        rotors (array): Array with numbers of picked rotors in a correct order
        offsets (array): Array with numbers that represent an offset to each rotor

    Returns:
        array: Array that contains 3 rotors in a final order
    """
    final_set_of_rotors = []    # here we should have an array with 3 arrays that contain correct rotors in a correct order with the offset applied
    for i in range(0, 3):
        name_of_chosen_rotor = "rotor" + str(rotors[i]) + "_initial"
        actual_rotor = globals()[name_of_chosen_rotor]
        actual_rotor_with_offset = actual_rotor[offsets[i]:] + actual_rotor[:offsets[i]]
        # print(f"{name_of_chosen_rotor}_with_offset = {actual_rotor_with_offset}")
        final_set_of_rotors.append(actual_rotor_with_offset)
    return final_set_of_rotors
   
def message_to_decimal (message):
    message_decimal = []
    for i in range(0, len(message)):
        letter = message[i]
        letter_index = swaped_alphabet.index(letter)
        message_decimal.append(letter_index)
    # print(f"message_decimal = {message_decimal}")
    return message_decimal

def decimal_to_message (decimal):
    mesage_list = []
    for i in range(0, len(decimal)):
        pos = decimal[i]
        letter = swaped_alphabet[pos]
        mesage_list.append(letter)
    message = "".join(mesage_list)
    # print(f"message = {message}")
    return message

def encrypt (message):  
    #transform message into numbers due to new alphabet
    message_decimal = message_to_decimal(message)
    
    #pass every other letter through wheels
    i = 0
    click0 = 0
    click1 = 0
    click2 = 0
    encrypted_message_decimal = []
    
    # imitating rotation of rotors
    while i < len(message):
        click0 = i % 26
        click1 = i // 26
        click2 = i // 676
        final_position_of_rotors = get_rotors_with_offset(rotors, offsets)
        final_position_of_rotors[0] = final_position_of_rotors[0][click0:] + final_position_of_rotors[0][:click0]
        final_position_of_rotors[1] = final_position_of_rotors[1][click1:] + final_position_of_rotors[1][:click1]
        final_position_of_rotors[2] = final_position_of_rotors[2][click2:] + final_position_of_rotors[2][:click2]
        
        step1 = message_decimal[i]          
        step2 = final_position_of_rotors[0][step1]          
        step3 = final_position_of_rotors[1][step2]          
        step4 = final_position_of_rotors[2][step3]          
        step5 = connector[step4]
        step6 = final_position_of_rotors[2][step5]          
        step7 = final_position_of_rotors[1][step6]          
        step8 = final_position_of_rotors[0][step7]          
        # print(f"step1 = {step1} \nstep2 = {step2}\nstep3 = {step3}\nstep4 = {step4}\nstep5 = {step5}\nstep6 = {step6}\nstep7 = {step7}\nstep8 = {step8}\n")
        encrypted_message_decimal.append(step8)
        i += 1
    print(f"encrypted_mesage_decimal = {encrypted_message_decimal}")
    
                
    # decypher them due to new alphabet
    answer = decimal_to_message(encrypted_message_decimal)
    return answer

def decrypt (messpassage):
    # transform message into numbers due to new alphabet
    message_decimal = message_to_decimal(message)
    
    i = 0
    click0 = 0
    click1 = 0
    click2 = 0
    decrypted_message_decimal = []
    
    # imitating rotation of rotors
    while i < len(message):
        click0 = i % 26
        click1 = i // 26
        click2 = i // 676
        final_position_of_rotors = get_rotors_with_offset(rotors, offsets)
        final_position_of_rotors[0] = final_position_of_rotors[0][click0:] + final_position_of_rotors[0][:click0]
        final_position_of_rotors[1] = final_position_of_rotors[1][click1:] + final_position_of_rotors[1][:click1]
        final_position_of_rotors[2] = final_position_of_rotors[2][click2:] + final_position_of_rotors[2][:click2]
                
        step1 = message_decimal[i]
        step2 = final_position_of_rotors[0].index(step1)
        step3 = final_position_of_rotors[1].index(step2)
        step4 = final_position_of_rotors[2].index(step3)
        step5 = connector.index(step4)
        step6 = final_position_of_rotors[2].index(step5)
        step7 = final_position_of_rotors[1].index(step6)
        step8 = final_position_of_rotors[0].index(step7)
        # print(f"step1 = {step1} \nstep2 = {step2}\nstep3 = {step3}\nstep4 = {step4}\nstep5 = {step5}\nstep6 = {step6}\nstep7 = {step7}\nstep8 = {step8}")
        decrypted_message_decimal.append(step8)
        i += 1
    print(f"decrypted_mesage_decimal = {decrypted_message_decimal}")
    
    # decypher them due to new alphabet 
    answer = decimal_to_message(decrypted_message_decimal)
    return answer
    
# dataset
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
connector = [1, 15, 16, 13, 18, 9, 24, 6, 20, 17, 21, 3, 8, 25, 19, 2, 23, 10, 4, 0, 22, 14, 12, 5, 7, 11]
rotor1_initial = [14, 8, 5, 23, 6, 19, 4, 17, 9, 25, 2, 16, 1, 10, 22, 0, 20, 18, 11, 15, 21, 7, 3, 13, 24, 12]
rotor2_initial = [23, 19, 8, 7, 12, 15, 24, 3, 1, 20, 10, 22, 4, 9, 14, 11, 2, 5, 25, 0, 13, 17, 18, 6, 16, 21]
rotor3_initial = [21, 6, 18, 24, 0, 5, 16, 3, 13, 7, 14, 10, 22, 2, 17, 11, 23, 19, 8, 9, 20, 25, 4, 12, 1, 15]
rotor4_initial = [12, 19, 24, 0, 2, 23, 20, 3, 6, 18, 25, 8, 9, 21, 5, 16, 7, 10, 1, 4, 22, 17, 13, 11, 14, 15]
rotor5_initial = [16, 8, 6, 20, 10, 18, 3, 9, 0, 14, 11, 19, 5, 12, 21, 1, 25, 7, 22, 15, 13, 23, 2, 24, 17, 4]

# start settings
swap = choose_swap()
rotors = choose_rotors()
offsets = choose_offsets()
print(f"\nSetup is complete! \nswap   = {swap}\nrotors = {rotors}\noffsets = {offsets}")

swaped_alphabet = get_swapped_alphabet(alphabet, swap) 
# print(f"Swaped alphabet = {swaped_alphabet}") 

# main
while True:
    process = input("\nEncrypt or decrypt? (e/d): ")
    
    if process.lower() == "encrypt" or process.lower() == "e":
        print("You are in the encription mode!")
        message = input("Enter a message you want to encrypt: ").upper().strip()
        print(f"\nYour original message is: {message}")
        result = encrypt(message)
        print(f"Your encripted mesage is:--------------------------- {result}")
        
    elif process.lower() == "decrypt" or process.lower() == "d":
        print("You are in the decription mode!")    
        message = input("Enter a message you want to decrypt:").upper().strip()
        print(f"Your message is: {message}")
        result = decrypt(message)
        print(f"Your decrypted mesage is:--------------------------- {result}")
        
    else: 
        quit = input("Input is not valid! Do you want to quit? All settings will be discarded... (y/n): ")
        
        if quit.lower() == "y" or quit.lower() == "yes":
            print("\nGoodbye!")
            break
        
        else:
            print("\nAlright, one more time...")

