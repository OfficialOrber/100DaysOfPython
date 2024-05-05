import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# list_of_all_items = []
list_of_all_items = [
    {'name':'iPad Pro', 'description':'Apple tablet computer.', 'reserve_price':500 },
    {'name':'iMac 23', 'description':'Apple all in one desktop.', 'reserve_price': 900 },
    {'name':'iPhone 15 Pro', 'description':'Apple computer phone.', 'reserve_price': 600 }
]
    
def add_new_auction_item(name, description, reserve_price):
    try:
        new_auction_item = {}
        new_auction_item['name'] = name
        new_auction_item['description'] = description
        new_auction_item['reserve_price'] = reserve_price
        list_of_all_items.append(new_auction_item)
        print('New item added successcully!')

    except:
      print('Something went wrong when creating the new item')

def item_name_is_correct(item_name):
    for item in list_of_all_items:
        if item['name'] == item_name:
          return item
    return False

def start_auction(item_being_auctioned):
    print(f'Auction will begin for "{item_being_auctioned["name"]}"')
    item_being_auctioned['bids'] = []
    auction_live = True
    while auction_live:
        if(input('Are there any bids?\n') == 'yes'):
            cls()
            bidder_name = input('Insert Bidder\'s name: ')
            bid_amount = int(input('Insert bid amount: £'))
            item_being_auctioned['bids'].append({'name': bidder_name, 'amount':bid_amount})
        else:
            auction_live = False
            cls()
            print('As there are no more bids, the auction will be closed.')
            print('A winner will be calculated provided the reserve price has been met.')
    
    winning_bid = find_winning_bid(item_being_auctioned['bids'])
    if winning_bid['amount'] >= item_being_auctioned['reserve_price']:
        cls()
        print(f'Congratulations {winning_bid["name"]}, you have won, with a bid of £{winning_bid["amount"]}.')
        close_auction(item_being_auctioned)
    else:
        cls()
        print('There has been no winning bid, as the bids were below the reserve price.')
        
def find_winning_bid(list_of_bids):
    current_winning_bid = {'amount': 0}
    for bid in list_of_bids:
        if bid['amount'] > current_winning_bid['amount']:
          current_winning_bid = bid
    return current_winning_bid

def close_auction(auction_item):
    for item in list_of_all_items:
        if item == auction_item:
            list_of_all_items.remove(item)


def main():    
    continue_program = True
    while(continue_program): 
        print('Here are your options:\n')
        print('"1" or "new": to add a new item\n')
        print('"2" or "start": to start auction\n')
        print('"3" or "stop": to stop the program\n')
        selection = input()

        if(selection == '1' or selection == 'new'):
            print('Add the details for your new item:')
            item_name = input('Add new item name: ')
            item_description = input('Add new item description: ')
            item_reserve_price = int(input('Add new item reserve price (minimum you would like it to sell for): '))
            if(not item_name or not item_description or not item_reserve_price):
                cls()
                print('Something was wrong with your input')
                print('Please provide all 3 values next time')
            else:
                add_new_auction_item(item_name, item_description,item_reserve_price)
            
        
        elif(selection == '2' or selection == 'start'):
            if(not list_of_all_items):
                cls()
                print('The list is empty.')
                print('Please add a new item to the auction list.')
            else:
                item_num = 1
                for item in list_of_all_items:
                    print(f'{item_num}-{item["name"]}: {item["description"]}\n')
                    item_num+=1
                
                item_to_auct_name = input('What item will you like to start the bidding for?\nType the item name, and watchout for typos.\n')
                item_to_auction = item_name_is_correct(item_to_auct_name)
                if(item_to_auction):
                    start_auction(item_to_auction)
                else:
                    cls()
                    print(f'Item "{item_to_auct_name}" couldn\'t be found please pay attention to the name and avoid typos.')
        
        elif selection == 3 or selection == 'stop':
            continue_program = False

        else:
            print('That\'s not a valid input!')

print('Welcome to the Silent Auction')
main()