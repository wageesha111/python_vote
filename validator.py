import datetime

SRI_LANKA_DISTRICTS = [
    "Ampara", "Anuradhapura", "Badulla", "Batticaloa", "Colombo",
    "Galle", "Gampaha", "Hambantota", "Jaffna", "Kalutara",
    "Kandy", "Kegalle", "Kilinochchi", "Kurunegala", "Mannar",
    "Matale", "Matara", "Monaragala", "Mullaitivu", "Nuwara Eliya",
    "Polonnaruwa", "Puttalam", "Ratnapura", "Trincomalee", "Vavuniya"
]

def is_valid_voter_id(voter_id):
    return voter_id.isdigit() and len(voter_id) == 10


def is_valid_district(district):
    for d in SRI_LANKA_DISTRICTS:
        if d.lower() == district.strip().lower():
            return True
    return False


def is_valid_age(age_str):
    if not age_str.isdigit():
        return False
    return int(age_str) >= 18


def is_valid_candidate_id(cid):
    return cid.isdigit() and len(cid) == 10



def is_valid_first_name(name):
    return name.isalpha() and 1 <= len(name) <= 10


def is_valid_seat_number(seat):
    return seat.isdigit() and len(seat) == 2


def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


