# Simple Probability Calculator (with full 52-card deck)
# Author: (Your Name)

def calculate_probability(favorable, total):
    """Calculate probability = favorable outcomes / total outcomes"""
    if total == 0:
        return 0
    return favorable / total


# ---- Step 0: Create full 52-card deck ----
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

deck_52 = [f"{rank} of {suit}" for rank in ranks for suit in suits]


print("🎯 Simple Probability Calculator 🎯\n")
print("Choose an example:")
print("1. Using playing cards (full 52-card deck)")
print("2. Rolling a die (1 to 6)")
print("3. Tossing a coin (Heads or Tails)")

# Step 1: Ask user to choose
choice = input("\nEnter your choice (1-3): ").strip()

# Step 2: Set up the sample space
if choice == "1":
    sample_space = deck_52
    description = "Full 52-card deck"
elif choice == "2":
    sample_space = ["1", "2", "3", "4", "5", "6"]
    description = "Rolling a die"
elif choice == "3":
    sample_space = ["Heads", "Tails"]
    description = "Coin toss"
else:
    print("Invalid choice! Please restart the program.")
    exit()

# Step 3: Show sample space info
total_outcomes = len(sample_space)
print(f"\n✅ Example selected: {description}")
print(f"Total outcomes (n(S)) = {total_outcomes}\n")

# Step 4: Define an event
event_name = input("Enter a name for your event (e.g., Face cards, Even, Heads): ")

print("\nEnter outcomes for your event.")
if choice == "1":
    print("Example inputs:")
    print(" --> A of Hearts")
    print(" --> 10 of Spades")
    print(" --> K of Diamonds")
    print(" --> J of Clubs\n")

event_items = input(f"Enter outcomes for '{event_name}' (comma-separated): ")

# Keep only valid outcomes that are part of the sample space
event_outcomes = [x.strip() for x in event_items.split(",") if x.strip() in sample_space]

# Step 5: Calculate probability
favorable = len(event_outcomes)
probability = calculate_probability(favorable, total_outcomes)

# Step 6: Display result
print(f"\nEvent '{event_name}': {event_outcomes}")
print(f"n(E) = {favorable}")
print(f"P({event_name}) = {favorable}/{total_outcomes} = {probability:.4f}")

print("\n🎉 Program finished! Thanks for using the Probability Calculator.")
