import random
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
import db_functions as db

import time
import os
from simple_term_menu import TerminalMenu

welcome_to_pi = r'''  
                                 ..;;;;;;;
                               ,;;;;;;;;;'              P
                             ,;;;;;;;\                  I
                           ,;;;;;;;;  \                 
                         ,;;;;;;;;     \                G
                       ,;;;;;;;;        \               A
                     ,;;;;;;;; ,,,,      \              M
                   ,;;;;;;;; '     ',     \             E
                 ,;;;;;;;;            ' . ,\,           S
             .,;;;;;;;;_______________      \ ',        
            /__________I             I__________I
            I__________I_____________I___________I
           [=MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM=]
             { }        { }  III              { }
             { }        { }  III              { }
             { }       [__]  III              { }
            _{ }             III              { }
            [__]            O C O             [__]
'''

pi_2000_string = '''
3
1415926535 8979323846 2643383279 5028841971 6939937510
5820974944 5923078164 0628620899 8628034825 3421170679
8214808651 3282306647 0938446095 5058223172 5359408128
4811174502 8410270193 8521105559 6446229489 5493038196
4428810975 6659334461 2847564823 3786783165 2712019091
4564856692 3460348610 4543266482 1339360726 0249141273
7245870066 0631558817 4881520920 9628292540 9171536436
7892590360 0113305305 4882046652 1384146951 9415116094
3305727036 5759591953 0921861173 8193261179 3105118548
0744623799 6274956735 1885752724 8912279381 8301194912
9833673362 4406566430 8602139494 6395224737 1907021798
6094370277 0539217176 2931767523 8467481846 7669405132
0005681271 4526356082 7785771342 7577896091 7363717872
1468440901 2249534301 4654958537 1050792279 6892589235
4201995611 2129021960 8640344181 5981362977 4771309960
5187072113 4999999837 2978049951 0597317328 1609631859
5024459455 3469083026 4252230825 3344685035 2619311881
7101000313 7838752886 5875332083 8142061717 7669147303
5982534904 2875546873 1159562863 8823537875 9375195778
1857780532 1712268066 1300192787 6611195909 2164201989

3809525720 1065485863 2788659361 5338182796 8230301952
0353018529 6899577362 2599413891 2497217752 8347913151
5574857242 4541506959 5082953311 6861727855 8890750983
8175463746 4939319255 0604009277 0167113900 9848824012
8583616035 6370766010 4710181942 9555961989 4676783744
9448255379 7747268471 0404753464 6208046684 2590694912
9331367702 8989152104 7521620569 6602405803 8150193511
2533824300 3558764024 7496473263 9141992726 0426992279
6782354781 6360093417 2164121992 4586315030 2861829745
5570674983 8505494588 5869269956 9092721079 7509302955
3211653449 8720275596 0236480665 4991198818 3479775356
6369807426 5425278625 5181841757 4672890977 7727938000
8164706001 6145249192 1732172147 7235014144 1973568548
1613611573 5255213347 5741849468 4385233239 0739414333
4547762416 8625189835 6948556209 9219222184 2725502542
5688767179 0494601653 4668049886 2723279178 6085784383
8279679766 8145410095 3883786360 9506800642 2512520511
7392984896 0841284886 2694560424 1965285022 2106611863
0674427862 2039194945 0471237137 8696095636 4371917287
4677646575 7396241389 0865832645 9958133904 7802759009
'''

### Cleaning-up my first 2000 digits of π from whitespace and \n ...
pi_2000_string_clean = pi_2000_string.replace(" ", "").replace("\n", "")

def start_index():

    option1 = "[1] - Which specific digit of PI you want (for example the 473rd!) ?"
    option2 = "[2] - Tell me a randomth digit of π!"
    option3 = "[3] - Study of π in series of 10 digits."
    option4 = "[4] - Study of π in series of 100 digits."
    option5 = "[5] - [T, DB] Write 100 digits of π from the first 2000 and I will check if they are correct."
    option6 = "[6] - [T, DB] I give you 100 digits of π from the first 100.000 and you memorize them :-)"
    options = [ option1, option2, option3, option4, option5, option6]

    terminal_menu = TerminalMenu(options,
    title="Choose your game!",
    show_multi_select_hint=True,
    menu_cursor="π ",
    exit_on_shortcut=False,
    status_bar="[Legend - T = with Timer, DB = with Database]",
    shortcut_key_highlight_style = ("fg_yellow",)
    # accept_keys=("1", "2", "3", "4", "5", "6"),
    )
    menu_entry_index = terminal_menu.show()
    print(Fore.YELLOW + f"You have selected {options[menu_entry_index]}!")
    print()

    user_choice = options[menu_entry_index]

    if user_choice == option1:
        game_1()
    if user_choice == option2:
        game_2()
    if user_choice == option3:
        game_3()
    if user_choice == option4:
        game_4()
    if user_choice == option5:
        game_5()
    if user_choice == option6:
        game_6()

def fix_the_input_for_me(prompt):
    '''
    This function will return you an integer if the user actually wrote a number.
    - If the user inputs B, it will go back to the Index.
    - If the user inputs Y, it will return Y and do nothing else
    - If the user do not input anything, it will return None
    - If the user writes anything else, it will say that it is not a valid option and go back to the Index.'''
    my_input = input(Fore.CYAN + f"{prompt} *** [B to go Back to the Index] *** \n{Style.RESET_ALL}")
    my_input = my_input.upper()
    if my_input == "B":
        start_index()
        exit()
    elif my_input == "Y":
        return "Y"
    elif my_input == "": # Pressing Enter without value
        return None
    else:
        try: 
            my_input = int(my_input)
        except:
            print(Fore.RED + f"{my_input} is not a valid option. Bringing you back to the Index of Games!")
            start_index()
        return my_input

def countdown():
    '''Simple countdown of 3 seconds.'''
    print()
    print(Fore.YELLOW + "READY?")
    time.sleep(1)
    print(f"{Style.RESET_ALL}SET ... ")
    time.sleep(1)
    print(Fore.GREEN + f"GO!{Style.RESET_ALL}")
    print()

def game_1():
    '''### 1st GAME ###
    ### Which specific digit of PI you want (for example the 473rd!) ?###'''

    digit_i_want = 473
    prompt_exc_1 = fix_the_input_for_me("Which specific digit of PI you want [from 1 to 2000] ?")
    digit_i_want = prompt_exc_1

    print(f"The {prompt_exc_1} digit of π is: {pi_2000_string_clean[digit_i_want]}")
    game_1()

def game_2():
    '''### 2nd GAME ###
    ### Tell me a randomth digit of π! ###'''

    random_digit = random.randint(1, 2000)
    prompt_exc_2 = fix_the_input_for_me(f"What is the {random_digit} digit of π?")

    if prompt_exc_2 == int(pi_2000_string_clean[random_digit]):
        print(Fore.GREEN + f"CORRECT! The {random_digit} digit of π is {pi_2000_string_clean[random_digit]}!")
    else:
        print(Fore.RED + f"WRONG! The {random_digit} digit of π is {pi_2000_string_clean[random_digit]} and not {prompt_exc_2}!")
    game_2()

def game_3():
    '''### 3rd GAME ###
    ### Revision of π in series of 10 digits. Which series of 100 digits do you want to revise? (From 1 to 20) ###'''

    prompt_exc_3 = fix_the_input_for_me("Which series of 10 digits do you want to revise? (From 1 to 200)")

    allowed_values = list(range(1, 201))
    if prompt_exc_3 not in allowed_values:
        print(Fore.RED + f"The value {prompt_exc_3} is not allowed. Please use one of the following values: {allowed_values} ")
        game_3()
        
    # Example with 5: If I want the fifth series of 10 numbers, initial index must be the 41st and the final index must be the 50th.
    initial_index = 41
    final_index = 50
    initial_index = (prompt_exc_3 * 10) + 1 - 10
    final_index = (prompt_exc_3 * 10)
    list_of_10_numbers = []
    string_of_10_numbers = ""

    # Populate my list of 10 numbers
    for number in range(initial_index, final_index+1):
        list_of_10_numbers.append(pi_2000_string_clean[number])
    
    # Create String of 10 numbers
    string_of_10_numbers = "".join(list_of_10_numbers)

    print(Fore.GREEN + f'''

πππππππππππππππππππππππππππ
π                         π 
π      {string_of_10_numbers}         π
π                         π
πππππππππππππππππππππππππππ

''')
    
    game_3()

def game_4():
    '''### 4nd GAME ###
    ### Revision of π in series of 100 digits ###'''
    list_of_100_numbers = []
    string_of_100_numbers = ""
    allowed_values = list(range(1, 21))
    prompt_exc_4 = fix_the_input_for_me("Which series of 100 digits do you want to revise? (1 to 20) ")

    # Example with 5: If I want the fifth series of 100 numbers, initial index must be the 401st and the final index must be the 500th.
    initial_index = (prompt_exc_4 * 100) - 99
    final_index = (prompt_exc_4 * 100) 

    # Be sure that prompt4 is only between 1 and 20:
    if prompt_exc_4 not in allowed_values:
        print(Fore.RED + f"The value {prompt_exc_4} is not allowed. Please use one of the following values: {allowed_values} ")
        game_4()
    # Populate my list of 100 numbers
    for number in range(initial_index, final_index+1):
        list_of_100_numbers.append(pi_2000_string_clean[number])
    
    # Create String of 100 numbers
    string_of_100_numbers = "".join(list_of_100_numbers)

    # Add a space every 10 digits for readability
    string_of_100_numbers_with_spaces = ''
    for index, digit in enumerate(string_of_100_numbers):
        index = index+1
        string_of_100_numbers_with_spaces+=digit
        if index % 10 == 0:
            string_of_100_numbers_with_spaces+=" "

    print(Fore.GREEN + f'''

πππππππππππππππππππππππππππ
π                         
π      {string_of_100_numbers_with_spaces}         
π                         
πππππππππππππππππππππππππππ

''')

    game_4()

def game_5():
    '''### 5th GAME ###
    ### 5 - Write 100 digits and I will check if they are correct.###'''

    list_of_100_correct_numbers = []
    string_of_100_correct_numbers = ""
    allowed_values = list(range(1, 21))
    prompt_exc_5 = fix_the_input_for_me("Which series of 100 digits do you want to revise? (1 to 20) ")

    # Example with 5: If I want the fifth series of 100 numbers, initial index must be the 401st and the final index must be the 500th.
    initial_index = (prompt_exc_5 * 100) - 99
    final_index = (prompt_exc_5 * 100) 

    pi_series_used = f"{initial_index}_{final_index}"
    # Be sure that prompt5 is only between 1 and 20:
    if prompt_exc_5 not in allowed_values:
        print(Fore.RED + f"The value {prompt_exc_5} is not allowed. Please use one of the following values: {allowed_values} ")
        game_5()

    # Populate my list of 100 numbers
    for number in range(initial_index, final_index+1):
        list_of_100_correct_numbers.append(pi_2000_string_clean[number])
    
    # Create String of 100 numbers
    string_of_100_correct_numbers = "".join(list_of_100_correct_numbers)

    # Start the countdown
    countdown()

    # Start the clock
    starttime = time.time()

    # Ask for the numbers from (human) memory
    prompt_exc_5B = input("Add here the numbers out of YOUR memory! *** [B to go Back to the Index] *** \n")
    
    # Clean Prompt of all the spaces
    prompt_exc_5B = prompt_exc_5B.replace(" ", "").replace("\n", "")

    # Check the case in which the numbers from memory are more than 100
    while len(prompt_exc_5B) > 100:
        prompt_len = len(prompt_exc_5B)
        prompt_exc_5B = input(f"You gave too many numbers ({prompt_len})! Try to reinsert precisely 100 digits. *** [B to go Back to the Index] *** \n")
    
    # Stop the clock
    totaltime = round((time.time() - starttime), 2)

    # Check the case in which the numbers from memory are less than 100. I will add Xes until i reach 100
    while len(prompt_exc_5B) != 100:
        prompt_exc_5B += "X"

    # Initialize variables for the loop
    fully_colored_string = ""
    no_of_mistakes = 0

    # Let's see how many mistakes were done ... 
    mistakes_dictionary = {}
    for i, num in enumerate(prompt_exc_5B):
        colored_digit_to_add = ""
        if num == string_of_100_correct_numbers[i]:
            colored_digit_to_add = f"{Fore.GREEN}{num}{Style.RESET_ALL}"
        else:
            colored_digit_to_add = f"{Fore.RED}{num}{Style.RESET_ALL}"
            no_of_mistakes += 1

            # Populate the mistakes_dictionary
            mistaken_digit = num
            mistaken_digit_position = initial_index + i
            mistaken_digit_correct = pi_2000_string_clean[mistaken_digit_position]
            mistakes_dictionary[mistaken_digit_position] = [mistaken_digit, mistaken_digit_correct]
        
        fully_colored_string = fully_colored_string + colored_digit_to_add
        
    # Give me the results
    print(f'''

ππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππ
{fully_colored_string}                                                                                
{string_of_100_correct_numbers}                                                                       
Mistakes: {no_of_mistakes}
Total time: {totaltime} seconds                                                                      
ππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππ

''')

### DB OPERATIONS ###
    # Initializing db variables
    conn, c = db.create_database("sessions")
    db.create_table(conn, c, 'sessions')

    mistakes_dictionary = str(mistakes_dictionary)
    # Write in the database
    session_dictionary = {
    "game_no" : 5,
    "date" : time.time(),
    "mistakes_no" : no_of_mistakes,
    "mistakes" : mistakes_dictionary,
    "time" : totaltime,
    "pi_series": pi_series_used
    }

    db.add_new_session(conn, c, session_dictionary)
    db.close_connection(conn)

    game_5()
 
def game_6():

    ### 6th GAME ###
    ### 6 - I give you 100 digits from the first 100.000 digits of π and you memorize them.###

    # Import the Biggie
    from pi_to_100000 import pi_to_100000

    ### Cleaning-up my first 100.000 digits of π from whitespace and \n ...
    pi_to_100000 = pi_to_100000.replace(" ", "").replace("\n", "")
    
    prompt_6A = fix_the_input_for_me('''After you say yes, I will show you 100 digits of π (taken randomly between the first 100.000) and the timer will start. Are you Ready? (Y for Yes)''')
    
    # If input is Yes or None continue
    if prompt_6A != "Y" and prompt_6A != None:
        start_index()
    random_series_of_100_digits_no = random.randint(21, 1000) # I do not want the first 2000 digits of π that I already memorized
    initial_index = (random_series_of_100_digits_no * 100) - 99
    final_index = (random_series_of_100_digits_no * 100)

    # Initialize list
    list_of_numbers_to_show = []

    # Populate my list of 100 numbers
    for number in range(initial_index, final_index+1):
        list_of_numbers_to_show.append(pi_to_100000[number])
    
    # Create String of 100 numbers
    string_of_numbers_to_show = "".join(list_of_numbers_to_show)

    countdown()

    # Start the clock
    starttime = time.time()
    
    print(f"******************* FROM {initial_index} *******************")
    print()
    print(f'{string_of_numbers_to_show}')
    print()
    print(f"*******************  TO {final_index}  *******************")
    print()
    print()
    pi_series_used = f"{initial_index}_{final_index}"
    input("Press Enter when you are done and I will stop the timer.")

    # Clean the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Stop the clock
    totaltime = round((time.time() - starttime), 2)
    print("Total time used to memorize: ", totaltime, "seconds.")

    prompt_6C = input("Insert here the numbers you memorized and press Enter ...\n")

    # Clean Prompt of all the spaces
    prompt_6C = prompt_6C.replace(" ", "").replace("\n", "")

    # Check the case in which the numbers from memory are more than 100
    while len(prompt_6C) > 100:
        prompt_len = len(prompt_6C)
        prompt_6C = input(f"You gave too many numbers ({prompt_len})! Try to reinsert precisely 100 digits. *** [B to go Back to the Index] *** \n")
    
    # Check the case in which the numbers from memory are less than 100. I will add Xes until i reach 100
    while len(prompt_6C) != 100:
        prompt_6C += "X"

    # Initialize variables for the loop
    fully_colored_string = ""
    no_of_mistakes = 0

    # Let's see how many mistakes were done ...  
    mistakes_dictionary = {}
    for i, num in enumerate(prompt_6C):
        colored_digit_to_add = ""
        if num == string_of_numbers_to_show[i]:
            colored_digit_to_add = f"{Fore.GREEN}{num}{Style.RESET_ALL}"
        else:
            colored_digit_to_add = f"{Fore.RED}{num}{Style.RESET_ALL}"
            no_of_mistakes += 1

            # Populate the mistakes_dictionary
            mistaken_digit = num
            mistaken_digit_position = initial_index + i
            mistaken_digit_correct = pi_to_100000[mistaken_digit_position]
            mistakes_dictionary[mistaken_digit_position] = [mistaken_digit, mistaken_digit_correct]

        
        fully_colored_string = fully_colored_string + colored_digit_to_add
        
    # Give me the results
    print(f'''

ππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππ
{fully_colored_string}                                                                                
{string_of_numbers_to_show}                                                                       
Mistakes: {no_of_mistakes}
Total time used to memorize: {totaltime} seconds                                                                      
ππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππππ

''')

    ### DB OPERATIONS ###
    # Initializing db variables
    conn, c = db.create_database("sessions")
    db.create_table(conn, c, 'sessions')

    mistakes_dictionary = str(mistakes_dictionary)
    # Write in the database
    session_dictionary = {
    "game_no" : 6,
    "date" : time.time(),
    "mistakes_no" : no_of_mistakes,
    "mistakes" : mistakes_dictionary,
    "time" : totaltime,
    "pi_series": pi_series_used
    }

    db.add_new_session(conn, c, session_dictionary)
    db.close_connection(conn)

    game_6()

### WELCOME! ###
print(f'''
πππππππππππππππππππππππππππ
{Fore.YELLOW}### WELCOME TO ∏ GAMES! ###{Style.RESET_ALL}
πππππππππππππππππππππππππππ
''')
print(welcome_to_pi)

### INDEX OF GAMES ###
start_index()





