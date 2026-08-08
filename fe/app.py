import streamlit as st
import requests as r
be_loc="http://127.0.0.1:8000"

st.title("🛩️AI TRAVEL PLANNER")

st.subheader("enter all trip data")
# input tags

starting_loc = st.text_input("enter starting location")
destination_loc = st.text_input("enter destination locationn")
no_of_trip_days=st.number_input("enter trip days",min_value=1)
no_of_people=st.number_input("enter people count",min_value=1)
budget=st.number_input("enter budget",min_value=10000,max_value=100000,step=10000)
specifications=st.text_area("enter your specification",
                            placeholder="Example: beaches, temples, party places, adventure, food, etc.")
language = st.selectbox(
    "🌐 Select Travel Plan Language",
    ["English", "తెలుగు (Telugu)", "हिंदी (Hindi)"]
)

btn=st.button("Build Traveling Plan")

if btn:

    # Basic validation
    if not starting_loc or not destination_loc:
        st.warning("Please enter starting location and destination.")

    else:

        # Payload sent to FastAPI
        payload = {
            "starting_loc": starting_loc,
            "destination_loc": destination_loc,
            "no_of_trip_days": no_of_trip_days,
            "no_of_people": no_of_people,
            "budget": budget,
            "specifications": specifications,
            "language": language
        }

        try:

            # Send request to backend
            be_res = r.post(
                f"{be_loc}/plan_trip",
                json=payload
            )

            # Successful response
            if be_res.status_code == 200:

                response_data = be_res.json()

                st.success("Travel plan generated successfully! ✈️")

                st.subheader("Your AI Travel Plan")

                st.write(
                    response_data["travel_plan"]
                )

            else:

                st.error(
                    f"Backend Error: {be_res.status_code}"
                )

                st.write(be_res.text)

        except r.exceptions.ConnectionError:

            st.error(
                "Could not connect to FastAPI backend. "
                "Make sure your FastAPI server is running."
            )

        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )