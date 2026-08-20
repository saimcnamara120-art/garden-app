# This function checks the season entered by the user and returns
# the appropriate gardening advice.
def get_season_advice(season):
    """Return gardening advice based on the season."""

    # Check if the user entered summer.
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"

    # Check if the user entered winter.
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"

    # Return a message if the season is not recognized.
    else:
        return "No advice for this season.\n"


# This function checks the plant type entered by the user and returns
# the appropriate gardening advice.
def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""

    # Give advice for flowers.
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."

    # Give advice for vegetables.
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"

    # Return a message if the plant type is not recognized.
    else:
        return "No advice for this type of plant."


# This function controls the main flow of the program.
def main():
    """Get user input and display the appropriate gardening advice."""

    # Ask the user to enter the current season.
    # lower() converts the input to lowercase for easier comparison.
    season = input("Enter the season (summer/winter): ").lower()

    # Ask the user to enter the type of plant.
    plant_type = input(
        "Enter the plant type (flower/vegetable): "
    ).lower()

    # Call both advice functions and combine their returned messages.
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Display the completed gardening advice to the user.
    print("\nGardening Advice:")
    print(advice)


# Run the main function only when this file is executed directly.
if __name__ == "__main__":
    main()