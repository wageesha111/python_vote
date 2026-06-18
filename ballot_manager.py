import file_manager as fm
import validator as vld


def cast_vote():

    print("\nCast Vote")

    voters = fm.load_voters()
    candidates = fm.load_candidates()
    ballots = fm.load_ballots()

#date
    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not vld.is_valid_date(date):
        print("Invalid date. Please enter YYYY-MM-DD")
        return

#voter ID

    voter_id = input("Enter voter ID: ").strip()
    voter_record = None
    for v in voters:
        if v[0] == voter_id:
            voter_record = v
            break
    if voter_record is None:
        print("Invalid Voter ID. Voter not registered.")
        return

    for b in ballots:
        if b[1] == voter_id:
            print("Vote already cast by this voter. Multiple votes are not allowed.")


#seat

    seat = input("Enter candidate seat number: ").strip()
    candidate_record = None
    for c in candidates:
        if c[2] == seat:
            candidate_record = c
            break
    if candidate_record is None:
        print("Invalid candidate seat number. No candidate registered for that seat.")
        return

    new_ballot = [
        date,
        voter_record[0],
        candidate_record[0],
        candidate_record[2],
        voter_record[2],
        voter_record[1]
    ]
    ballots.append(new_ballot)
    fm.save_ballots(ballots)
    print("Vote cast successfully for Seat", seat, "on", date + ".")


def delete_vote():

    print("\nDelete Vote")
    ballots = fm.load_ballots()

    voter_id = input("Enter voter ID to delete vote: ").strip()

    if not vld.is_valid_voter_id(voter_id):
        print("Invalid voter ID")
        return

    found = False
    for b in ballots:
        if b[1] == voter_id:
            found = True
            break

    if not found:
        print("Vote does not exist for this Voter ID")
        return

    ballots = [b for b in ballots if b[1] != voter_id]
    fm.save_ballots(ballots)
    print("Vote deletion successful.The voter may now cast a new vote")

def ballot_menu():

    while True:
        print("\nVote Management")
        print("1. Cast Vote")
        print("2. Delete Vote")
        print("3. Back to Main Menu")

        choice = input("Select option: ").strip()
        if choice == "1":
            cast_vote()
        elif choice == "2":
            delete_vote()
        elif choice == "3":
            break
        else:
            print("ERROR: Invalid option. Please enter 1-3")
