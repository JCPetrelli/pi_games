import string
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import random

welcome_to_pi = '''
       _ 
      (_)
 _ __  _ 
| '_ \| |
| |_) | |
| .__/|_|
| |      
|_|   

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
    print('''
πππππππππππππππππππππππππππ
######### INDEX ###########
πππππππππππππππππππππππππππ

1 - Which specific digit of PI you want (for example the 473rd!) ?
2 - Tell me a randomth digit of π!
3 - Revision of π in series of 10 digits. 
4 - Revision of π in series of 100 digits. 
    ''')
    index_prompt = fix_the_input_for_me("Select your π game! [1 to 10]")
    if index_prompt == 1:
        game_1()
    if index_prompt == 2:
        game_2()
    if index_prompt == 3:
        game_3()
    if index_prompt == 4:
        game_4()

def fix_the_input_for_me(prompt):
    '''
    This function will return you an integer if the user actually wrote a number.
    If instead the user wrote B, it will send you back to the Index.
    If the user writes anything else, it will say that it is not a valid option and go back to the Index. 
    '''
    my_input = input(f"{prompt} *** [B to go Back to the Index] *** \n")
    my_input = my_input.upper()
    if my_input == "B":
        start_index()
        exit()
    else:
        try: 
            my_input = int(my_input)
        except:
            print(Fore.RED + f"{my_input} is not a valid option. Bringing you back to the Index of Games!")
            start_index()
        return my_input
    
def game_1():
    ### 1st GAME ###
    ### Which specific digit of PI you want (for example the 473rd!) ?###

    digit_i_want = 473
    prompt_exc_1 = fix_the_input_for_me("Which specific digit of PI you want [from 1 to 2000] ?")
    digit_i_want = prompt_exc_1

    print(f"The {prompt_exc_1} digit of π is: {pi_2000_string_clean[digit_i_want]}")
    game_1()


def game_2():
    ### 2nd GAME ###
    ### Tell me a randomth digit of π! ###

    random_digit = random.randint(1, 2000)
    prompt_exc_2 = fix_the_input_for_me(f"What is the {random_digit} digit of π?")

    if prompt_exc_2 == int(pi_2000_string_clean[random_digit]):
        print(Fore.GREEN + f"CORRECT! The {random_digit} digit of π is {pi_2000_string_clean[random_digit]}!")
    else:
        print(Fore.RED + f"WRONG! The {random_digit} digit of π is {pi_2000_string_clean[random_digit]} and not {prompt_exc_2}!")
    game_2()

def game_3():
    ### 3rd GAME ###
    ### Revision of π in series of 10 digits. Which series of 100 digits do you want to revise? (From 1 to 20) ###

    random_digit = random.randint(1, 2000)
    prompt_exc_3 = fix_the_input_for_me(f"Which series of 10 digits do you want to revise? (From 1 to 200)")

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
    string_of_10_numbers = f"".join(list_of_10_numbers)

    print(Fore.GREEN + f'''

πππππππππππππππππππππππππππ
π                         π 
π      {string_of_10_numbers}         π
π                         π
πππππππππππππππππππππππππππ

''')
    
    game_3()


def game_4():
    ### 4nd GAME ###
    ### Revision of π in series of 100 digits ###

    list_of_100_numbers = []
    string_of_100_numbers = ""
    allowed_values = list(range(1, 21))
    prompt_exc_4 = fix_the_input_for_me(f"Which series of 100 digits do you want to revise? (1 to 20) ")

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
    string_of_100_numbers = f"".join(list_of_100_numbers)

    print(Fore.GREEN + f'''

πππππππππππππππππππππππππππ
π                         
π      {string_of_100_numbers}         
π                         
πππππππππππππππππππππππππππ

''')

    game_4()
### WELCOME! ###
print(Fore.GREEN + f'''

πππππππππππππππππππππππππππ
### WELCOME TO ∏ GAMES! ###
πππππππππππππππππππππππππππ

''')
print(welcome_to_pi)

### INDEX OF GAMES ###
start_index()





