from superadmin.database import (create_database,
                                 add_update_or_delete_manager, see_all_managers,
                                 total_sales, total_revenue, sales_per_branch, sales_per_seller)
from client.client import (view_available_cars, buy_car, view_purchase_history)
from seller.seller import (sell_car, view_sales_history, view_available_cars)

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")


def show_super_admin_menu():
    """
    This function shows the main menu of the superadmin menu.
    """
    text = input("""
    1. Create database.   
    2. Manager management.
    3. Statistics.
    4. Go to back

    Choose an option above: """)

    if text == "1":
        if create_database():
            return show_super_admin_menu()
    elif text == "2":
        if show_manger_management_menu():
            return show_super_admin_menu()
    elif text == "3":
        pass
    elif text == "4":
        pass
    else:
        print("Invalid input")
        show_super_admin_menu()


def show_manger_management_menu():
    """
    This function shows the main menu of the manger management menu.
    """
    text = input("""
    1. Add/update/delete manager account.
    2. See all managers.
    3. Go to back.

    Choose an option above: """)

    if text == "1":
        if add_update_or_delete_manager():
            show_manger_management_menu()
    elif text == "2":
        if see_all_managers():
            show_manger_management_menu()
    elif text == "3":
        show_super_admin_menu()
    else:
        print("Invalid input")
        show_manger_management_menu()


def show_statistics_menu():
    """
    This function shows the main menu of the statistics menu.
    """
    text = input("""
    1. Total sales.
    2. Total revenue.
    3. Sales per branch.
    4. Sales per seller. 
    5. Go to back.

    Choose an option above: """)

    if text == "1":
        total_sales()
    elif text == "2":
        total_revenue()
    elif text == "3":
        sales_per_branch()
    elif text == "4":
        sales_per_seller()
    elif text == "5":
        return show_super_admin_menu()
    else:
        print("Invalid input")
        show_statistics_menu()


def branch_manager_menu():
    """
    This function shows the main menu of the branch management menu.
    """
    while True:
        print("\nBranch Manager Menu:")
        print("1. Manage Sellers")
        print("2. Manage Cars")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            manage_sellers_menu()
        elif choice == "2":
            manage_cars_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")


def manage_sellers_menu():
    """
    This function shows the main menu of the sellers menu.
    """
    while True:
        print("\nManage Sellers:")
        print("1. Create seller account")
        print("2. Update seller account")
        print("3. Delete seller account")
        print("4. View all sellers in branch")
        print("5. Back to Branch Manager Menu")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")


def manage_cars_menu():
    """
    This function shows the main menu of the cars menu.
    """
    while True:
        print("\nManage Cars:")
        print("1. Add a new car")
        print("2. Update car details")
        print("3. Delete car")
        print("4. View available cars in branch")
        print("5. Back to Branch Manager Menu")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")


def seller_menu(branch_id):
    while True:
        print("\nSeller Menu:")
        print("1. Sell a Car")
        print("2. View Sales History")
        print("3. View Available Cars")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            sell_car(branch_id)
        elif choice == '2':
            view_sales_history(branch_id)
        elif choice == '3':
            view_available_cars(branch_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def client_menu():
    while True:
        print("\n==== Car Selling System ====")
        print("1. View Available Cars")
        print("2. Buy a Car")
        print("3. View Purchase History")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_available_cars()
        elif choice == '2':
            buy_car()
        elif choice == '3':
            view_purchase_history()
        elif choice == '4':
            print("Thank you for using the Car Selling System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
