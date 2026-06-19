import voter_manager     as vm
import candidate_manager as cm
import ballot_manager    as bm
import trend_graph       as tg

def print_banner():
    print("  Voter Management System (VMS)")
    print("  Student Union President Election")

def main_menu():
    print_banner()

    while True:
        print("\nMani Menu")
        print("1. Voter Management")
        print("2. Candidate Management")
        print("3. Cast / Delete Vote")
        print("4. Show Vote Trend Graph")
        print("5. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            vm.voter_menu()
        elif choice == "2":
            cm.candidate_menu()
        elif choice == "3":
            bm.ballot_menu()
        elif choice == "4":
            tg.show_trend_graph()
        elif choice == "5":
            print("Exiting VMS. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1-5")

if __name__ == "__main__":
    main_menu()


