################
# Main Program #
################

import ui

def handle_main_choice(choice):
    '''Handles choice from the main menu'''
    if choice == '1':
        edit_merchandise()
    elif choice == '2':
        edit_events()
    elif choice == '3':
        enter_sales()
    elif choice == '4':
        helpful_info()
    elif choice == 'q':
        quit()
    else:
        ui.message('Please enter a valid selection')

def handle_edit_merch_choice(choice):
    '''Handles choice from the Edit Merchandise menu'''
    if choice == '1':
        ui.display_products()
    elif choice == '2':
        ui.add_product()
    elif choice == '3':
        ui.edit_price()
    elif choice == '4':
        ui.edit_quantity()
    elif choice == '5':
        ui.delete_product()
    elif choice == 'q':
        return
    else:
        ui.message('Please enter a valid selection')

def handle_edit_events_choice(choice):
    '''Handles choice from the Edit Events menu'''
    if choice == '1':
        ui.display_events()
    elif choice == '2':
        ui.add_event()
    elif choice == '3':
        ui.edit_event_date()
    elif choice == '4':
        ui.edit_event_location()
    elif choice == '5':
        ui.delete_event()
    elif choice == 'q':
        return
    else:
        ui.message('Please enter a valid selection')

def handle_enter_sales_choice(choice):
    '''Handles choice from the Enter Sales menu'''
    if choice == '1':
        ui.display_sales()
    elif choice == '2':
        ui.add_sale()
    elif choice == '3':
        ui.edit_sale()
    elif choice == '4':
        ui.delete_sale()
    elif choice == 'q':
        return
    else:
        ui.message('Please enter a valid selection')

def handle_info_choice(choice):
    '''Handles choice from the Sales Info menu'''
    if choice == '1':
        ui.most_sold_product()
    elif choice == '2':
        ui.festival_sold_most_crystals()
    elif choice == '3':
        ui.festival_sold_least_crystals()
    elif choice == '4':
        ui.least_sold_product()
    elif choice == 'q':
        return
    else:
        ui.message('Please enter a valid selection')


def edit_merchandise():
    '''Enter the Edit Merchandise Menu'''
    quit = 'q'
    choice = None
    while choice != quit:
        choice = ui.display_edit_merch_menu()
        handle_edit_merch_choice(choice)

def edit_events():
    '''Enter the Edit Events Menu'''
    quit = 'q'
    choice = None
    while choice != quit:
        choice = ui.display_edit_events_menu()
        handle_edit_events_choice(choice)

def enter_sales():
    '''Enter the Enter Sales Menu'''
    quit = 'q'
    choice = None
    while choice != quit:
        choice = ui.display_enter_sales_menu()
        handle_enter_sales_choice(choice)

def helpful_info():
    '''Enter the Helpful Info Menu'''
    quit = 'q'
    choice = None
    while choice != quit:
        choice = ui.display_info_menu()
        handle_info_choice(choice)

def quit():
    '''Shutdown Program'''
    ui.message("Have a good day!")
    exit()



####################
# Start of Program #
####################
def main():
    print("Merchandise Manager")

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_main_menu_get_choice()
        handle_main_choice(choice)


if __name__ == '__main__':
    main()
