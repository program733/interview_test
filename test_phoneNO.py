import phonenumbers
from phonenumbers import geocoder



import phonenumbers
from geopy.geocoders import Nominatim

# Function to get location from phone number
def get_location_from_phone_number(phone_number):
    print(phone_number)
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        print(parsed_number)

        # Check if the phone number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            print(' are here')
            return "Invalid phone number"

        print('fetching country code')
        # Get the country and region codes from the phone number
        country_code = 1
        region_code = 6502530000

        print(country_code)
        print(region_code)
        # Get location information using geocoding
        geolocator = Nominatim(user_agent="phone_number_locator")
        location = geolocator.geocode(f"{country_code} {region_code}")

        # Return the location details
        if location:
            return location.address
        else:
            return "Location information not found"
    except Exception as e:
        return str(e)

# Example phone number
phone_number = "+1 650-253-0000"  # Replace this with the desired phone number

# Get and print the location information
location_info = get_location_from_phone_number(phone_number)
print("Location of the phone number:", location_info)
