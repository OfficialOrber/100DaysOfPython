import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# list_of_all_items = []
list_of_all_items = [
    {'name':'iPad Pro', 'description':'Apple tablet computer.', 'reserve_price':500 },
    {'name':'iPhone 15 Pro', 'description':'Apple computer phone.', 'reserve_price': 600 },
    {'name':'iMac 23', 'description':'Apple all in one desktop.', 'reserve_price': 900 }
    ]
    
def add_new_auction_item(name, description, reserve_price):
    try:
        new_auction_item = {}
        new_auction_item['name'] = name
        new_auction_item['description'] = description
        new_auction_item['reserve_price'] = reserve_price
        list_of_all_items.append(new_auction_item)
    except:
      print('Something went wrong when creating the new item')
    finally:
      print('New item added successcully!')

def item_name_is_correct(item_name):
    for item in list_of_all_items:
        if item['name'] == item_name:
          return item
    return False

def start_auction(item_being_auctioned):
    print(f'Auction will begin for "{item_being_auctioned}"')

def main():    
    continue_program = True
    while(continue_program): 
        print('Here are your options:\n')
        print('"1" or "new": to add a new item\n')
        print('"2" or "start": to start auction\n')
        selection = input()

        if(selection == '1' or selection == 'new'):
            print('Add the details for your new item:')
            item_name = input('Add new item name.')
            item_description = input('Add new item description.')
            item_reserve_price = int(input('Add new item reserve price (minimum you would like it to sell for).'))
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
                
                item_to_auct = input('What item will you like to start the bidding for?\nType the item name, and watchout for typos.\n')

                if():
                    start_auction(item_to_auct)
                    continue_program = False
                else:
                    cls()
                    print(f'Item "{item_to_auct}" couldn\'t be found please pay attention to the name and avoid typos.')

        else:
            print('That\'s not a valid input!')

print('Welcome to the Silent Auction')
main()