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
        print("\nMain Menu")
        print("1. Voter Management")
        print("2. Candidate Management")
        print("3. Cast / Delete Vote")
        print("4. Show Vote Trend Graph")
        print("5. Exit")

        choice = input("Select option: ").strip()

        match choice:
            case "1":
                vm.voter_menu()
            case "2":
                cm.candidate_menu()
            case "3":
                bm.ballot_menu()
            case "4":
                tg.show_trend_graph()
            case "5":
                print("Exiting VMS...")
                break
            case _:
                print("Invalid option.Please enter 1-5")


if __name__ == "__main__":
    main_menu()


