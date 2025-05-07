import streamlit as st
import phonenumbers
from phonenumbers import geocoder, carrier
from models import init_db, get_user_name, save_user

init_db()

st.title("📱 Phone Number Identifier (Truecaller Lite)")

number_input = st.text_input("Enter phone number (with country code):", "+234")

if st.button("Identify"):
    try:
        phone_number = phonenumbers.parse(number_input)
        
        # Debugging: Print parsed phone number
        st.write(phone_number)  # Check parsed phone number

        # Get location and carrier
        location = geocoder.description_for_number(phone_number, "en") or "Location not found"
        service = carrier.name_for_number(phone_number, "en") or "Carrier not found"
        
        # Get name if available
        name = get_user_name(number_input)

        st.success("✅ Result Found")
        st.write(f"**📍 Location:** {location}")
        st.write(f"**📞 Carrier:** {service}")

        if name:
            st.write(f"**🙋 Name:** {name}")
        else:
            st.warning("No name found. Add one below 👇")
            with st.form("add_name"):
                new_name = st.text_input("Name")
                email = st.text_input("Email (optional)")
                submitted = st.form_submit_button("Submit Name")
                if submitted:
                    save_user(number_input, new_name, email)
                    st.success("Name added successfully!")

    except Exception as e:
        st.error(f"Error: {e}")
        
# Add a footer
st.markdown(
    """
    ---
    Made with ❤️ by Adejoke Ogundipe
    """
)
