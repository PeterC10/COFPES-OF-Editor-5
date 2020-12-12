from editor.option_file import OptionFile

# Put PES 5 Option File in the same folder as this script
of_file_location = "KONAMI-WIN32PES5OPT"

# Load/decrypt the option file
print("Loading option file...")
of = OptionFile(of_file_location)
print("Option file loaded.")

# Select the 1st club (by index number)
club = of.clubs[0]
print(f"Old Club Name: {club.name}")
# Change club name
club.update_name("EVOWEB FC")
print(f"New Club Name: {club.name}")

# Save/encrypt the option file
print("Saving option file...")
of.save_option_file()
print("Option file saved.")
