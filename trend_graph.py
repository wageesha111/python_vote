import file_manager as fm


def show_trend_graph():

    print("\nVote Trend Graph")
    ballots = fm.load_ballots()
    candidates = fm.load_candidates()

    if not ballots:
        print("No ballots found")
        return

    if not candidates:
        print("No candidates found")
        return

    try:
        import pandas as pd
        import plotly.express as px

        ballot_df = pd.DataFrame(ballots, columns=["date", "voter_id", "candidate_id",
                                               "candidate_seat", "voter_age", "district"])

        candidate_df = pd.DataFrame(candidates, columns=["candidate_id", "first_name", "seat_number"])

        vote_counts = ballot_df.groupby("candidate_seat").size().reset_index(name="votes")

        merged = vote_counts.merge(candidate_df, left_on="candidate_seat",
                               right_on="seat_number", how="left")

        merged["label"] = merged["first_name"] + " (Seat " + merged["candidate_seat"] + ")"

        fig = px.bar(
            merged,
            x="label",
            y="votes",
            text="votes",
            title="Votes Received by Each Candidate",
            labels={"label": "Candidate (Seat)", "votes": "Number of Votes"},
            color="votes",
            color_continuous_scale="Blues"
    )
        fig.update_traces(textposition="outside")
        fig.update_layout(coloraxis_showscale=False)
        fig.show()

    except ImportError:
        print("pandas and plotly are required for the trend graph")
