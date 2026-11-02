import menu


def main():

    students_list = []
    while True:
        print("### Students Management System (SMS) ###")
        print("======= MENU =======")
        menu.view_menu_options()
        picked_option = menu.ask_for_menu_option()
        
        #Check if the user wants to exit
        if picked_option == 0:
            print("Exiting program. Goodbye!")
            break
            
        #Execute the chosen action
        menu.handle_menu_choice(picked_option, students_list)
        print("\n" + "="*40 + "\n")


if __name__ == '__main__':
    main()