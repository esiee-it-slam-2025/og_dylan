from datas_variables import *
from functions import *


# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  MAIN
# ****************************************************************************************************************************************************************

# Main function to run the ticket machine program
def main():
    while True:
        os.system("cls")

        # Display the welcome message and available actions
        print("\n                      ////////////                                                 ////////////    ///////")
        print("                         ///      //   //////    //  //    //////  ///////            ///       //       // ")
        print("                       ///      //   ///        //  //    //___     //               //       //       //   ")
        print("                     ///       //   //         ////      //        //         //   //        //       //    ")
        print("                    ///       //     //////   //   //   //////    //          ////            ///////       ")
        print("\n\nWelcome to the Ticket Machine.")
        show_actions()
        
        # Prompt the user to choose an action
        action = verif_int("├─> ", 4)

        # Perform the selected action based on user input
        if action == 1:
            clear_folder()
            generate_tickets()
        elif action == 2:
            create_ticket()
        elif action == 3:
            display_available_tickets()
        elif action == 4:
            print("Program exit..\nGoodbye !")
            break

if __name__ == "__main__":
    main()

