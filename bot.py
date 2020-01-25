def compare(card1, card2, trump):  # card1 пытается побить card2, trump - козырная масть
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

def choose(mycards, trump, trash, numl, ):
