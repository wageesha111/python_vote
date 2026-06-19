import os

VOTER_FILE     = "../data/voter.csv"
CANDIDATE_FILE = "../data/candidate.csv"
BALLOT_FILE    = "../data/ballots.csv"

VOTER_HEADER     = ["voter_id", "district", "age"]
CANDIDATE_HEADER = ["candidate_id", "first_name", "seat_number"]
BALLOT_HEADER    = ["date", "voter_id", "candidate_id", "candidate_seat", "voter_age", "district"]


def read_csv(filename):
    rows =[]
    if not os.path.exists(filename):
        return rows
    with open(filename) as f:
        first_line =True
        for line in f:
            line = line.strip()
            if first_line:
                first_line = False
                continue
            if line:
                rows.append(line.split(","))
    return rows

def write_csv(filename,header, rows):
    with open(filename, 'w') as f:
        f.write(",".join(header) +"\n")
        for row in rows:
            f.write(",".join(row) +"\n")

# voters
def load_voters():
    return read_csv(VOTER_FILE)

def save_voters(voters):
    write_csv(VOTER_FILE, VOTER_HEADER, voters)

# candidates

def load_candidates():
    return read_csv(CANDIDATE_FILE)

def save_candidates(candidates):
    write_csv(CANDIDATE_FILE, CANDIDATE_HEADER, candidates)

#ballots

def load_ballots():
    return read_csv(BALLOT_FILE)

def save_ballots(ballots):
    write_csv(BALLOT_FILE, BALLOT_HEADER, ballots)

