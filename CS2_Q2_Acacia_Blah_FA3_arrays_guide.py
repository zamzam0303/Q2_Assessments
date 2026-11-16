# ==========================================
# Activity 1: Direct Index Access
# ==========================================
video_games = ["Mobile Legends", "Valorant", "Minecraft", "Roblox", "Terraria"]

print("--- Activity 1: Direct Index Access ---")
print("Element at index 0:", video_games[0])
print("Element at index 1:", video_games[1])
print("Element at index 2:", video_games[2])
print("Element at index 3:", video_games[3])
print("Element at index 4:", video_games[4])

print("\n--- Modifying an Element via Index ---")
print("Original index 2 item:", video_games[2])

video_games[2] = "CODM"

print("Updated index 2 item:", video_games[2])
print("Updated Backpack List:", video_games)

# ==========================================
# Activity 2: Process Your Data (Uses Activity 1 List)
# ==========================================
print("\n--- Activity 2: Process Your Data ---")
original_array = video_games
print("Original Array/List:", original_array)

try:
    update_index = int(input("Enter index to update (0 to 4): "))
    new_value = input("Enter New Value: ")
    if 0 <= update_index < len(original_array):
        original_array[update_index] = new_value
        print(f"New Value: {new_value}")
    else:
        print("❌ Invalid index position.")
except ValueError:
    print("❌ Please enter a valid integer for the index.")

try:
    start_idx = int(input("Enter Slice Start Index: "))
    end_idx = int(input("Enter Slice End Index: "))
    sliced_list = original_array[start_idx:end_idx]
    print(f"Sliced ArrayList ({start_idx}:{end_idx}):", sliced_list)
except ValueError:
    print("❌ Please enter valid integers for slicing.")

search_item = input("Enter Search Item: ")
if search_item in sliced_list:
    print(f"Search Result (from sliced array): {search_item} is found in the sliced list.")
else:
    print(f"Search Result (from sliced array): {search_item} is NOT found in the sliced list.")

print("Updated Array/List:", original_array)


# ==========================================
# Activity 3: Data Analysis Mini App
# ==========================================
print("\n--- Activity 3: Data Analysis Mini App ---")
scores_data = [85, 90, 78, 92, 88]

def display_scores(scores):
    print("\n--- Current Student Scores ---")
    if not scores:
        print("No scores recorded.")
        return
    for i, s in enumerate(scores):
        print(f"Student #{i+1} (Index {i}): {s}")

def search_score(scores):
    try:
        target = int(input("Enter the score to search for: "))
        if target in scores:
            idx = scores.index(target)
            print(f"✅ Score {target} found at Student #{idx+1} (Index {idx}).")
        else:
            print(f"❌ Score {target} not found in records.")
    except ValueError:
        print("❌ Please enter a valid numeric score.")

def compute_average_score(scores):
    if not scores:
        print("No scores available to compute.")
        return
    avg = sum(scores) / len(scores)
    print(f"\n--- Score Statistics ---")
    print(f"Total Students: {len(scores)}")
    print(f"Total Sum:      {sum(scores)}")
    print(f"Average Score:  {avg:.2f}")
    print(f"Highest Score:  {max(scores)}")
    print(f"Lowest Score:   {min(scores)}")

def update_score(scores):
    display_scores(scores)
    try:
        index = int(input("Enter the index of the score you want to update: "))
        if 0 <= index < len(scores):
            new_score = int(input(f"Enter the new score for Index {index} (Old: {scores[index]}): "))
            old_val = scores[index]
            scores[index] = new_score
            print(f"✅ Successfully updated Index {index}: {old_val} -> {new_score}")
        else:
            print(f"❌ Invalid index! Must be between 0 and {len(scores)-1}.")
    except ValueError:
        print("❌ Please enter valid numbers for index and score.")

def run_mini_app():
    while True:
        print("\n=== Student Score Analyzer ===")
        print("1. Display Scores")
        print("2. Search Score")
        print("3. Compute Average Score")
        print("4. Update Score")
        print("5. Display Updated Scores")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            display_scores(scores_data)
        elif choice == '2':
            search_score(scores_data)
        elif choice == '3':
            compute_average_score(scores_data)
        elif choice == '4':
            update_score(scores_data)
        elif choice == '5':
            display_scores(scores_data)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice. Choose 1-6.")

run_mini_app()
