import json
from dataclasses import dataclass

@dataclass
class Activity:
    activity: str
    activity_type: str
    environment:str
    cost: float
    people: int

def load_activity() -> list[Activity]:
    activities: list[Activity] = []
    with open(file= 'activities.json', mode='r' ) as f:
        for activity in json.load(fp = f):
            activities.append(
                Activity(
                    activity = activity['activity'],
                    activity_type = activity['type'],
                    environment=activity['environment'].lower(),
                    cost = activity['cost'],
                    people = activity['people']

                )
            )

    return activities

def generate_activities(activities: list[Activity]) -> None:
    try:
        people: int = int(input("Enter number of people: "))
        cost: float = float(input("Enter the maximum amount you are willing to pay: "))


        weather_choice = input("Choose activity environment (indoor/outdoor/any): ").strip().lower()

        if weather_choice not in ("indoor", "outdoor", "any"):
            print("Invalid choice. Defaulting to 'any'.")
            weather_choice = "any"


    except ValueError:
        print("Please enter a numeric value")
        return

    matched_activities: list[Activity] = []

    for activity in activities:
        activity_people = activity.people
        activity_cost = activity.cost

        if (

        activity_people >= people and
        activity_cost < cost and
        (weather_choice == "any" or activity.environment == weather_choice)

        ):
            matched_activities.append(activity)

    if matched_activities:
        for i, matched in enumerate(matched_activities, start = 1):
            print(f"{i}: {matched.activity}: ₹{matched.cost} per person ₹[{people}p: {people*matched.cost}] ")

    else:
        print("No activities matched your criteria..")


def main() ->None:
    activities: list[Activity] =load_activity()
    generate_activities(activities)

if __name__=='__main__':
    main()
