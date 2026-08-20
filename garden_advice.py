# This function returns gardening advice based on the season.
def get_season_advice(season):
    """Return gardening advice for the entered season."""

    # Check if the user entered summer.
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"

    # Check if the user entered winter.
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"

    # Return this message if the season is not recognized.
    else:
        return "No advice for this season.\n"


# This function returns gardening advice based on the plant type.
def get_plant_advice(plant_type):
    """Return gardening advice for the entered plant type."""

    # Give advice for flowers.
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."

    # Give advice for vegetables.
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"

    # Return this message if the plant type is not recognized.
    else:
        return "No advice for this type of plant."


# This function controls the main flow of the program.
def main():
    """Run the gardening advice program."""

    # Ask the user to enter the current season.
    # lower() makes the input easier to compare.
    season = input("Enter the season (summer/winter): ").lower()

    # Ask the user to enter the type of plant.
    plant_type = input(
        "Enter the plant type (flower/vegetable): "
    ).lower()

    # Get the advice for the season.
    season_advice = get_season_advice(season)

    # Get the advice for the plant type.
    plant_advice = get_plant_advice(plant_type)

    # Combine both pieces of advice.
    advice = season_advice + plant_advice

    # Display the completed gardening advice.
    print("\nGardening Advice:")
    print(advice)


# Run the main function when the program is started.
if __name__ == "__main__":
    main()


# Change History / TODO List:
# [Completed] Added detailed comments explaining each block of code.
# [Completed] Refactored the code into functions for better readability
# and modularity.
#
# TODO: Store advice in a dictionary for multiple plants and seasons.
# TODO: Recommend plants based on the entered season.
# Hardcoded values for the season and plant type
season = "summer"  # TODO: Replace with input() to allow user interaction.
plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
