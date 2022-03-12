"""

Creator: Jamshid Ahmadov\
    github.com\jamshid-python\

"""

def card(card_number):
    """Karta raqamini yashiruvchi dastur"""
    if len(card_number) <= 4:
        return card_number
    
    else:
        a = card_number[:-4]
        b = card_number[-4:]
        ans = len(a)*"*"
        ans += b
        return ans
    
card_number = input("Enter your card number: ")
print(card(card_number))

"""
pass

"""
