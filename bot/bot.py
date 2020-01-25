class Bot():
    
    def __init__(self):
        pass

    def compare(self, card1, card2, trump):  # card1 пытается побить card2, trump - козырная масть
        if card1['type'] != card2['type'] and card1['type'] != trump:
            return False
        else:
            if card1['type'] == card2['type'] and card1['value'] > card2['value']:
                return True
            elif card1['type'] == trump and card2['type'] != trump:
                return True
            elif card1['type'] == trump and card2['type'] == trump:
                if card1['value'] > card2['value']:
                    return True
                else:
                    return False

    def minn(self, cards):
        m = cards[0]['value']
        j = 0
        for i in range(len(cards)):
            if cards[i]['value'] < m:
                m = cards[i]['value']
                j = i
        return cards[j]

    def attack(self, mycards):
        return minn(mycards)

    def defend(self, mycards, acard, trump):
        while len(mycards) > 0:
            if compare(minn(mycards), acard, trump):
                return minn(mycards)
            else:
                mycards.remove(minn(mycards))
        return False
