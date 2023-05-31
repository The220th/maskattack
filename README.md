# maskattack

maskattack help to generate string combination by mask.

# Usage

## Get all posible combinations

``` python
# import templates
from maskattack import (MaskDigit, MaskAlphaLower, MaskAlphaUpper, MaskSpecialSymbols, MaskAll)
# import functions
from maskattack import (maskattack_get_toucheds, maskattack_look_current, maskattack_one_iterate, maskattack_get_list)

# init mask.
# Trying to brute: Super?password?, where:
#                              first ? is special symbol (or empty);
#                              second ? is digit (or empty);
#        Super   ?                      password   ?
MASK = ["Super", MaskSpecialSymbols(), "password", MaskDigit()]
# special_symbols=" !?\"\'@#$;:.,/\\()<>{}+=-_*&^%" # space included

# get list of all possible by mask string combinations
combs = maskattack_get_list(MASK)

# look:
print(combs)

# output:
# ['Superpassword', 'Superpassword0', 'Superpassword1', 'Superpassword2', 'Superpassword3', 'Superpassword4', 'Superpassword5', 'Superpassword6', 'Superpassword7', 'Superpassword8', 'Superpassword9', 'Super password', 'Super password0', 'Super password1', 'Super password2', 'Super password3', 'Super password4', 'Super password5', 'Super password6', 'Super password7', 'Super password8', 'Super password9', 'Super!password', 'Super!password0', 'Super!password1', 'Super!password2', 'Super!password3', 'Super!password4', 'Super!password5', 'Super!password6', 'Super!password7', 'Super!password8', 'Super!password9', 'Super?password', 'Super?password0', 'Super?password1', 'Super?password2', 'Super?password3', 'Super?password4', ..., 'Super%password7', 'Super%password8', 'Super%password9']
```

## Dinamic iterate

``` python
# import templates
from maskattack import (MaskDigit, MaskAlphaLower, MaskAlphaUpper, MaskSpecialSymbols, MaskAll)
# import functions
from maskattack import (maskattack_get_toucheds, maskattack_look_current, maskattack_one_iterate, maskattack_get_list)

def your_password_func(password: str) -> bool:
    """
    Return True, if the password fits
    """
    if(password == "Super_paSSword38"):
        return True
    else:
        return False

# init mask.
# Trying to brute: Super_paSSword38 <-> Super_paS?word??, where:
#                                                        first ? is letter (or empty);
#                                                        second ? is digit (or empty);
#                                                        third ? is digit too (or empty);
#        Super_paS                   ?                   word   ?            ?
MASK = ["Super_paS", MaskAlphaLower()+MaskAlphaUpper(), "word", MaskDigit(), MaskDigit()]
# init toucheds:
toucheds = maskattack_get_toucheds(MASK)


# Dinamic iterate
while(True):
    one_password = maskattack_look_current(MASK)
    print(one_password)
    if(your_password_func(one_password) == True):
        break
    if(maskattack_one_iterate(MASK, toucheds) == False):
        break
print("END")

# output:
# Super_paSword
# Super_paSword0
# Super_paSword1
# ...
# Super_paSword7
# Super_paSword8
# Super_paSword9
# Super_paSword0
# Super_paSword00
# Super_paSword01
# Super_paSword02
# ...
# Super_paSword06
# Super_paSword07
# Super_paSword08
# Super_paSword09
# Super_paSword1
# Super_paSword10
# Super_paSword11
# ...
# Super_paSword95
# Super_paSword96
# Super_paSword97
# Super_paSword98
# Super_paSword99
# Super_paSAword
# Super_paSAword0
# Super_paSAword1
# ...
# Super_paSAword8
# Super_paSAword9
# Super_paSAword0
# Super_paSAword00
# Super_paSAword01
# ...
# Super_paSAword08
# Super_paSAword09
# Super_paSAword1
# Super_paSAword10
# Super_paSAword11
# ...
# Super_paSAword18
# Super_paSAword19
# Super_paSAword2
# ...
# Super_paSAword95
# Super_paSAword96
# Super_paSAword97
# Super_paSAword98
# Super_paSAword99
# Super_paSBword
# Super_paSBword0
# Super_paSBword1
# Super_paSBword2
# Super_paSBword3
# Super_paSBword4
# ...
# Super_paSDword97
# Super_paSDword98
# Super_paSDword99
# Super_paSEword
# Super_paSEword0
# Super_paSEword1
# Super_paSEword2
# ...
# Super_paSSword28
# Super_paSSword29
# Super_paSSword3
# Super_paSSword30
# ...
# Super_paSSword35
# Super_paSSword36
# Super_paSSword37
# Super_paSSword38
# END
```

# User defined MASK-class

``` python
# import templates
from maskattack import (MaskDigit, MaskAlphaLower, MaskAlphaUpper, MaskSpecialSymbols, MaskAll)
# import functions
from maskattack import (maskattack_get_toucheds, maskattack_look_current, maskattack_one_iterate, maskattack_get_list)
# and import maskattack-interface
from maskattack import MaskI

# define user mask-class:
class UserMaskItem(MaskI):

    letters = [""] + ["your combination 1", "your_combination_two"] + list("kexalo")

    def __init__(self):
        super().__init__()
        self.COMBS = type(self).letters
        self.N = len(self.COMBS)
        self.cur_i = 0

# init mask with user defined mask-class:
MASK = ["Super_user: ", UserMaskItem(), " word", MaskDigit()]

# get list of all possible by mask string combinations
combs = maskattack_get_list(MASK)

# look:
print(combs)

# output:
# ['Super_user:  word', 'Super_user:  word0', 'Super_user:  word1', 'Super_user:  word2', 'Super_user:  word3', 'Super_user:  word4', 'Super_user:  word5', 'Super_user:  word6', 'Super_user:  word7', 'Super_user:  word8', 'Super_user:  word9', 'Super_user: your combination 1 word', 'Super_user: your combination 1 word0', 'Super_user: your combination 1 word1', 'Super_user: your combination 1 word2', 'Super_user: your combination 1 word3', 'Super_user: your combination 1 word4', 'Super_user: your combination 1 word5', 'Super_user: your combination 1 word6', 'Super_user: your combination 1 word7', 'Super_user: your combination 1 word8', 'Super_user: your combination 1 word9', 'Super_user: your_combination_two word', 'Super_user: your_combination_two word0', 'Super_user: your_combination_two word1', 'Super_user: your_combination_two word2', 'Super_user: your_combination_two word3', 'Super_user: your_combination_two word4', 'Super_user: your_combination_two word5', 'Super_user: your_combination_two word6', 'Super_user: your_combination_two word7', 'Super_user: your_combination_two word8', 'Super_user: your_combination_two word9', 'Super_user: k word', 'Super_user: k word0', 'Super_user: k word1', 'Super_user: k word2', 'Super_user: k word3', 'Super_user: k word4', 'Super_user: k word5', 'Super_user: k word6', 'Super_user: k word7', 'Super_user: k word8', 'Super_user: k word9', 'Super_user: e word', 'Super_user: e word0', 'Super_user: e word1', 'Super_user: e word2', 'Super_user: e word3', 'Super_user: e word4', 'Super_user: e word5', 'Super_user: e word6', 'Super_user: e word7', 'Super_user: e word8', 'Super_user: e word9', 'Super_user: x word', 'Super_user: x word0', 'Super_user: x word1', 'Super_user: x word2', 'Super_user: x word3', 'Super_user: x word4', 'Super_user: x word5', 'Super_user: x word6', 'Super_user: x word7', 'Super_user: x word8', 'Super_user: x word9', 'Super_user: a word', 'Super_user: a word0', 'Super_user: a word1', 'Super_user: a word2', 'Super_user: a word3', 'Super_user: a word4', 'Super_user: a word5', 'Super_user: a word6', 'Super_user: a word7', 'Super_user: a word8', 'Super_user: a word9', 'Super_user: l word', 'Super_user: l word0', 'Super_user: l word1', 'Super_user: l word2', 'Super_user: l word3', 'Super_user: l word4', 'Super_user: l word5', 'Super_user: l word6', 'Super_user: l word7', 'Super_user: l word8', 'Super_user: l word9', 'Super_user: o word', 'Super_user: o word0', 'Super_user: o word1', 'Super_user: o word2', 'Super_user: o word3', 'Super_user: o word4', 'Super_user: o word5', 'Super_user: o word6', 'Super_user: o word7', 'Super_user: o word8', 'Super_user: o word9']
```

# Inbuild mask-class discription

- MaskDigit - substitutes all numbers instead of itself: ``.

- MaskAlphaLower - substitutes all lowercase letters instead of itself: ``.

- MaskAlphaUpper - substitutes all uppercase letters instead of itself: ``.

- MaskSpecialSymbols - substitutes special symbols instead of itself: ``.

- MaskAll - all of the above

Also, these classes can be combined with each other using the operator +. For example: `maskAll = MaskDigit() + MaskAlphaLower() + MaskAlphaUpper() + MaskSpecialSymbols()`.

