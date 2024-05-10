import re

pattern = r'(\w+)\s(\w+)'

with open('input.txt') as file:
    text = file.read()

def get_matches(string, char) -> int:
    count = 0
    for i in range(len(string)):
        if char == string[i]:
            count += 1
    return count

def classify(cards:dict[str:int]):
    count = 0
    pairs = 0
    jcount = 0
    higher = ''
    
    if cards.__contains__('J'):
        jcount += cards.pop('J')
    
    if not cards:
        return 6    
    
    for card in cards:
        if cards[card] > count:
            count = cards[card]
            pairs = 1
            higher = card
        elif count == cards[card]:
            pairs += 1
            
    cards[higher] += jcount
    count = cards[higher]
    # five of a kind
    if count == 5:
        return 6
    # four of a kind
    elif count == 4:
        return 5
    
    elif count == 3:
        for element in cards:
        # full house
            if cards[element] == 2:
                return 4
        # three of a kind
        else:
            return 3
    elif count == 2 and pairs == 2:
        return 2
    elif count == 2:
        return 1
    else:
        return 0
                
def compare(str1:str,str2:str):
   n = len(str1)
   decode = {
            'A':13,
            'K':12,
            'Q':11,
            'T':10,
            '9':9,
            '8':8,
            '7':7,
            '6':6,
            '5':5,
            '4':4,
            '3':3,
            '2':2,
            'J':1
        }
   
   if str1 == str2: return 0
   
   for i in range(n):
       a = decode[str1[i]]
       b = decode[str2[i]]
       if a == b:
           continue
       elif a > b: 
           return 1
       elif a < b:
           return -1
       
def sort(cards:list[tuple[str,int]]):
    for i in range(len(cards) - 1):
        for j in range(i + 1, len(cards)):
            if compare(cards[i][0], cards[j][0]) == 1:
                cards[i], cards[j] = cards[j], cards[i]
                
                
cards_and_bids = re.findall(pattern,text)
hands_lists = [[],[],[],[],[],[],[]]

for card_and_bid in cards_and_bids:
    cards = {}
    for card_label in card_and_bid:
        for label in card_label:
            if cards.__contains__(label):
                continue
            else:
                cards[label] = get_matches(card_label,label)
        # print(cards)
        set = classify(cards)
        hands_lists[set].append((card_and_bid[0],card_and_bid[1]))
        
        break

for hand_list in hands_lists:
    sort(hand_list)
    # print(hand_list)

result = []
for hand_list in hands_lists:
    result += hand_list
ans = 0

# print(result)

for i in range(len(result)):
    ans += int(result[i][1]) * (i+1)
    
print(len(result))
print(ans)