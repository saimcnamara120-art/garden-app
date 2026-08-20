# Ask the user to enter the current season.
# The lower() method converts the input to lowercase so that entries
# such as "Summer" and "SUMMER" will still match "summer".
season = input("Enter the season (summer/winter): ").lower()

# Ask the user to enter the type of plant.
# The input is also converted to lowercase for easier comparison.
plant_type = input(
    "Enter the plant type (flower/vegetable): "
).lower()

# Create an empty string that will store the gardening advice.
# Advice for the season and plant type will be added to this variable.
advice = ""

# Check the season entered by the user and add the appropriate advice.
if season == "summer":
    # Summer plants may need more water and protection from the sun.
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    # Winter plants may need protection from cold temperatures and frost.
    advice += "Protect your plants from frost with covers.\n"
else:
    # Display this message if the entered season is not recognized.
    advice += "No advice for this season.\n"

# Check the plant type entered by the user and add appropriate advice.
if plant_type == "flower":
    # Fertiliser can help flowers grow and produce healthy blooms.
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    # Vegetable plants should be regularly checked for garden pests.
    advice += "Keep an eye out for pests!"
else:
    # Display this message if the plant type is not recognized.
    advice += "No advice for this type of plant."

# Display the completed gardening advice to the user.
print("\nGardening Advice:")
print(advice)


# Change History / TODO List:
# [Completed] Added detailed comments explaining each block of code.
#
# TODO: Refactor the code into functions for better readability
# and modularity.
# TODO: Store advice in a dictionary for multiple plants and seasons.
# TODO: Recommend plants based on the entered season.