available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "HDMI cable"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []
print("Please enter 0 to end.")
while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print(f"Removing {current_choice}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {current_choice}")
            computer_parts.append(chosen_part)
        print(f"Your list for your routine now contains {computer_parts}")
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")
    current_choice = input()
print(f"Your final list is: {computer_parts}")

