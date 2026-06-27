import streamlit as st
import uuid
from langchain_core.messages import HumanMessage
from agent import app
import os

st.set_page_config(page_title="TravelMind", page_icon="✈️")

st.title("✈️ Travel Agent Chatbot")
st.write("Plan your trip using AI.")
if st.button("New Trip"):
    st.session_state.messages = []
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.last_result = None
    st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "last_result" not in st.session_state:
    st.session_state.last_result = None
    
def get_city_image(city):
    city = city.lower().strip()

    image_path = f"assets/{city}.jpg"

    if os.path.exists(image_path):
        return image_path

    return "assets/default.jpg"        

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask me about your trip...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }

    result = app.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config=config
    )
    
    st.session_state.last_result = result

    assistant_reply = result["messages"][-1].content

    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_reply
    })
    
    
    with st.chat_message("assistant"):
        st.write(assistant_reply)

if st.session_state.last_result:
    result = st.session_state.last_result

    flights = result.get("flights", [])
    hotels = result.get("hotels", [])

    if flights and hotels and result.get("package_ready") and not result.get("approved"):
        st.subheader("Choose Your Package")

        cols = st.columns(3)

        for i in range(min(3, len(flights), len(hotels))):
            flight = flights[i]
            hotel = hotels[i]

            with cols[i]:
                with st.container(border=True):

                    image_path = get_city_image(
                        hotel.get("location", "")
                    )

                    st.image(
                        image_path,
                        use_container_width=True
                    )

                    st.subheader(f"Package {i + 1}")

                    st.write("✈️ Flight")
                    st.write(f"Airline: {flight.get('airline')}")
                    st.write(f"Route: {flight.get('origin')} to {flight.get('destination')}")
                    st.write(f"Price: {flight.get('price')}")

                    st.write("🏨 Hotel")
                    st.write(f"Hotel: {hotel.get('name')}")
                    st.write(f"Location: {hotel.get('location')}")
                    st.write(f"Price: {hotel.get('price')}")

                    if st.button(f"Select Package {i + 1}", key=f"package_{i+1}"):
                        selected_package = f"Package {i + 1}"

                        config = {
                            "configurable": {
                                "thread_id": st.session_state.thread_id
                            }
                        }

                        result = app.invoke(
                            {"messages": [HumanMessage(content=selected_package)]},
                            config=config
                        )

                        st.session_state.last_result = result

                        assistant_reply = result["messages"][-1].content

                        st.session_state.messages.append({
                            "role": "user",
                            "content": selected_package
                        })

                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": assistant_reply
                        })

                        st.rerun()