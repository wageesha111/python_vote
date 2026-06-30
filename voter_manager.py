import validator as vld
import file_manager as fm

def add_voter():

    print("\n Add Voter ")
    voters = fm.load_voters()

#voter ID
    voter_id = input("Enter voter ID (10 digits): ").strip()
    if not vld.is_valid_voter_id(voter_id):
        print("Invalid voter ID. Voter ID must be 10 digits.")
        return

    for v in voters:
        if v[0] == voter_id:
            print("Voter ID already exists.")
            return

#district

    district = input ("Enter District name: ").strip()
    if not vld.is_valid_district(district):
        print("District must be one of the 25 districts in Sri Lanka.")
        return

#age

    age = input("Enter Age (minimun 18): ").strip()
    if not vld.is_valid_age(age):
        print("Age must be a number and at least 18.")
        return

    voters.append([voter_id,district,age])
    fm.save_voters(voters)
    print("Voter added successfully.")


def edit_voter():

    print("\n Edit Voter ")
    voters = fm.load_voters()

    voter_id =input("Enter voter ID: ").strip()
    found = False

    for v in voters:
        if v[0] == voter_id:
            found = True
            break

    if found == False:
        print("Voter ID not found")
        return

    print("Current Details")
    print("Voter ID: ", v[0])
    print("District: ", v[1])
    print("Age: ", v[2])


    district = input("Enter new District name: ").strip()
    if not vld.is_valid_district(district):
        print("District must be one of the 25 districts in Sri Lanka.")
        return
    v[1] = district

    age = input("Enter new Age: ").strip()
    if not vld.is_valid_age(age):
        print("Age must be a number and at least 18.")
        return
    v[2] = age
    fm.save_voters(voters)
    print("Voter updated successfully")


def search_voter():

    print("\n Search Voter ")
    voters = fm.load_voters()

    voter_id =input("Enter voter ID to search:").strip()
    for v in voters:
        if v[0] == voter_id:
            print("Voter found")
            print("Voter ID:", v[0])
            print("District:", v[1])
            print("Age:", v[2])
            return
    print("Voter ID not found")


def delete_voter():

    print("\n Delete Voter ")
    voters = fm.load_voters()
    ballots = fm.load_ballots()

    voter_id =input("Enter voter ID to delete:").strip()

    found = False
    for v in voters:
        if v[0] == voter_id:
            found = True
            break

    if not found:
        print("Voter ID not found")
        return

    for b in ballots:
        if b[1] == voter_id:
            print("Cannot delete voter with an active ballot. Delete the ballot first")
            return

    voters = [v for v in voters if v[0] != voter_id]
    fm.save_voters(voters)
    print("Voter deleted successfully")


def voter_menu():

    while True:
        print("\n Voter Management ")
        print("1. Add Voter")
        print("2. Edit Voter")
        print("3. Search Voter")
        print("4. Delete Voter")
        print("5. Back to Main Menu")

        choice = input("Select option: ").strip()
        if choice == "1":
            add_voter()
        elif choice == "2":
            edit_voter()
        elif choice == "3":
            search_voter()
        elif choice == "4":
            delete_voter()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please enter 1-5")








