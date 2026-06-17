import file_manager as fm
import validator as vld


def add_candidate():

    print("\n Add candidate")
    candidates = fm.load_candidates()

#candidate ID
    cid = input("Enter candidate ID (10 digits): ").strip()
    if not vld.is_valid_candidate_id(cid):
        print("Candidate ID must be exactly 10 digits")
        return
    for c in candidates:
        if c[0] == cid:
            print("Candidate ID already exists")
            return

#first name

    name = input("Enter first name (max 10 chars): ").strip()
    if not vld.is_valid_first_name(name):
        print("First name must contain letters only and be at most 10 characters")
        return

#seat number

    seat = input("Enter candidate seat number (2 digits): ").strip()
    if not vld.is_valid_seat_number(seat):
        print("Seat number must be exactly 2 digits")
        return
    for c in candidates:
        if c[2] == seat:
            print("Seat number already taken by another candidate")
            return

    candidates.append([cid, name, seat])
    fm.save_candidates(candidates)
    print("Candidate added successfully")

def view_candidates():

    print("\n View candidates")
    candidates = fm.load_candidates()

    if not candidates:
        print("No candidates registered")
        return

    print ("{:<15} {:<15} {:<10}".format("Candidate ID", "First Name", "Seat No"))
    print("-" * 45)
    for c in candidates:
        print("{:<15} {:<15} {:<10}".format(c[0], c[1], c[2]))


def candidate_menu():

    while True:
        print("\nCandidate Management")
        print("1. Add Candidate")
        print("2. View Candidates")
        print("3. Back to Main Menu")

        choice = input("Select option: ").strip()
        if choice == "1":
            add_candidate()
        elif choice == "2":
            view_candidates()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please enter 1-3.")