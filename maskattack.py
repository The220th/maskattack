# -*- coding: utf-8 -*-

def maskattack_get_toucheds(MASK: list) -> list:
    return list(filter(lambda x: x != None, [i if(isinstance(el_i, MaskI)) else None for i, el_i in enumerate(MASK)]))

def maskattack_look_current(MASK: list) -> str:
    res = ""
    for el_i in MASK:
        if(isinstance(el_i, MaskI) == True):
            res += el_i.keek()
        else:
            res += el_i
    return res

def maskattack_one_iterate(MASK: list, toucheds: list) -> bool:
    '''
    Return True, if not stop, else False
    '''
    touched_i = len(toucheds)-1

    while(MASK[toucheds[touched_i]].kext() == None):
        MASK[toucheds[touched_i]].keset()
        touched_i-=1
        if(touched_i < 0):
            return False
    return True

def maskattack_get_list(MASK: list) -> list:
    toucheds = maskattack_get_toucheds(MASK)
    res = []
    res.append(maskattack_look_current(MASK))
    while(maskattack_one_iterate(MASK, toucheds)):
         res.append(maskattack_look_current(MASK))
    return res



class MaskI():

    def __init__(self):
        self.COMBS = None
        self.N = -1

    def kext(self) -> str:
        '''
        Return next symbol/comb or None, if end
        '''
        if(self.cur_i < self.N-1):
            self.cur_i += 1
            return self.cur_i
        else:
            return None

    def keek(self) -> str:
        '''
        Return current symbol/comb without iterate or None, if end
        '''
        if(self.cur_i < self.N):
            return self.COMBS[self.cur_i]
        else:
            return None

    def keset(self):
        '''
        Reset kext
        '''
        self.cur_i = 0

    def __add__(self, o):
        self.COMBS += o.COMBS
        self.COMBS = sorted(list(set(self.COMBS)))
                          # list(set(...)) for exclude repeats
        self.N = len(self.COMBS)
        return self

class MaskDigit(MaskI):

    letters = [""] + list("0123456789")

    def __init__(self):
        super().__init__()

        self.COMBS = type(self).letters
        self.N = len(self.COMBS)
        self.cur_i = 0

class MaskAlphaLower(MaskI):

    letters = [""] + list("abcdefghijklmnopqrstuvwxyz")

    def __init__(self):
        super().__init__()

        self.COMBS = type(self).letters
        self.N = len(self.COMBS)
        self.cur_i = 0

class MaskAlphaUpper(MaskI):

    letters = [""] + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def __init__(self):
        super().__init__()

        self.COMBS = type(self).letters
        self.N = len(self.COMBS)
        self.cur_i = 0

class MaskSpecialSymbols(MaskI):

    letters = [""] + list(" !?\"\'@#$;:.,/\\()<>{}+=-_*&^%")

    def __init__(self):
        super().__init__()

        self.COMBS = type(self).letters
        self.N = len(self.COMBS)
        self.cur_i = 0

class MaskAll(MaskI):

    letters = [""] + list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?\"\'@#$;:.,/\\()<>{}+=-_*&^%")

    def __init__(self):
        super().__init__()

        self.COMBS = type(self).letters
        self.N = len(self.COMBS)
        self.cur_i = 0































