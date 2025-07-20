from planner import interpret_goal
from restaurant_search import search_restaurants
from calendar_api import get_team_availability, create_event

def main():
    goal = input("Enter your high-level goal: ")
    plan = interpret_goal(goal)

    print("\n[Step 1] Interpreting goal...")
    print(plan)

    print("\n[Step 2] Searching restaurants...")
    options = search_restaurants(plan)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option['name']} - {option['address']} - {option['rating']} stars")

    choice = int(input("\nEnter the option number to proceed with: ")) - 1
    chosen = options[choice]

    print("\n[Step 3] Checking availability...")
    slot = get_team_availability(plan['team_members'], plan['date_range'])

    print(f"Available Slot Found: {slot}")
    create_event(plan['team_members'], slot, chosen)

    print("✅ Invitation sent via Google Calendar!")

if __name__ == "__main__":
    main()