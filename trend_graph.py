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

        if not ballot_df.empty:
            vote_counts = ballot_df.groupby("candidate_seat").size().reset_index(name="votes")
        else:
            vote_counts = pd.DataFrame(columns=["candidate_seat", "votes"])

        merged = candidate_df.merge(vote_counts, left_on="seat_number",
                                    right_on="candidate_seat", how="left")

        merged["votes"] = merged["votes"].fillna(0)

        merged["label"] = merged["first_name"] + " (Seat " + merged["seat_number"] + ")"

        fig = px.bar(
            merged,
            x="label",
            y="votes",
            text="votes",
            title="Votes Received by Each Candidate",
            labels={"label": "Candidate (Seat)", "votes": "Number of Votes"},
    )
        fig.update_traces(textposition="outside", marker_color="lightblue")
        fig.update_layout(coloraxis_showscale=False)
        fig.update_yaxes(dtick=1)
        fig.show()

    except ImportError:
        print("pandas and plotly are required for the trend graph")
