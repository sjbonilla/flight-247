import time
import json
import re
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_title():
    print("\n***********************************FLIGHT 247**********************************")
    print("This is Flight 247 departing LAX with final destination JFK")
    print("*********************************************************************************")
    print("\nIn this adventure game you will be the Captain of Flight"
          " 247\nYou are in charge of each decision while flying and "
          "are responsible for landing safely the 160 passengers")
    print("\nYou will encounter different scenarios while flying and "
          "need to take different choices that will affect the result")
    input("\nTo start the game please cick [ENTER]")


def captain_credentials():

    while True:

        name = input(f"Please write your Captain Name: ").upper()

        if re.fullmatch(r"[A-Z]+", name):
            print(f"Welcome Captain {name} to Flight 247")
            break
        else:
            print("Please enter a valid name containing only letters.")

    return name


def get_decision():
    while True:
        try:
            user_choice = int(input("\nEnter your decision (1-3): "))

            if user_choice not in (1, 2, 3):
                print("Please select an available decision")
                continue
        except ValueError:
            print("Please enter a number!")
            continue
        break
    return user_choice


def engine_emergency(captain):
    print("\nWARNING: ENGINE 2 HIGH TEMPERATURE\n")
    print(f"Captain {captain}, Engine 2 is overheating quickly")
    print("___________________________________________________")
    print("\n1. Inspect engine parameters")
    print("2. Reduce engine thrust and monitor")
    print("3. Ignore the warning and continue")

    choice = get_decision()

    if choice == 1:
        print("Engine parameters are being inspected...")
        time.sleep(3)
        print("Inspection confirms an abnormal temperature reading on Engine 2.")
        print(f"{captain}, overheating on Engine 2 confirmed. We should evaluate "
              "our diversion options before the situation deteriorates.")
        time.sleep(6)
    elif choice == 2:
        print("Reducing engine thrust...")
        time.sleep(3)
        print("Engine thrust reduced succesfully.")
        print(f"{captain}, the temperature is decreasing, but the main cause of malfunction"
              "have not been identified. We should consider our diversion options. ")
        time.sleep(6)
    elif choice == 3:
        print("Continuing Flight...")
        time.sleep(3)
        print(f"{captain}, the temperature is decreasing, but the main cause of malfunction"
              "have not been identified. We should consider our diversion options. ")
        time.sleep(6)

    return choice


def diversion(name, previous_decision):

    if previous_decision == 1:
        print("\nFIRST OFFICER: Captain, our engine assessment is complete. Engine 2 remains operational, but"
              "the abnormal reading persist. ATC has provided two alternate airports. One is closer, but weather"
              "conditions are deteriorating. The other has better weather but requires a longer flight\n")
        print("1. Divert to the closer airport- Reduce flight time, but face challenging weather.")
        print("2. Divert to the airport with better weather- Take a longer route with more favorable landing conditions..")
        print("3. Continue to JFK- Maintain the original destination despite the unresolved anomaly.")
    elif previous_decision == 2:
        print("\nFIRST OFFICER: Captain, the temperature has stabilized, but Engine 2 is producing less thrust. We are receiving"
              " inconsistent performance readings, and the crew still has not determined the cause. We need to decide how to proceed.\n")
        print("1. Request an engine assessment and diversion- Gather additional information while arrangin a suitable landing.")
        print("2. Maintain reduced thrust and continue- Keep monitoring the engine while proceeding toward JFK.")
        print("3. Increase thrust to recover performance- Attempt to restore performance despite the unresolved temperature anomaly.")
    elif previous_decision == 3:
        print("\nWARNING: POWER LOSS\n")
        print("\nFIRST OFFICER: Captain! We have lost power on Engine 2. ATC is standing by. We need to make a decision immediately!\n")
        print("1. Declare an emergency and request diversion- Coordinate an emergency landing at a suitable airport.")
        print("2. Attempt to restore engine performance- Spend additional time troubleshooting while the situation remains unstable.")
        print("3. Continue toward JFK despite the failure- Reject the immediate diversion recommendation.")

    user_choice = get_decision()
    time.sleep(3)
    return user_choice


def final_approach(name, decision1, decision2, risk):
    if (decision1 == 1 or decision1 == 2) and (decision2 == 1 or decision2 == 2):
        print("\nFINAL APPROACH\n")
        print("We are starting our final approach towards the diverted airport")
        print("Winds are a bit strong, around 20 knots. ATC recommends landing")
        print("\nWe need to make our final decision ASAP!\n")
        print("1. Continue landing in the longer runway. Emergency personnel already on route. Airport is waiting for us.")
        print("2. Land on the shorter runway as is closer to the aiport gate.")
        print("3. ATC ask if we need emergency personel, we decide not need it as we are okay. Continue landing on longer runway.")
    elif (decision1 == 3 or decision1 == 2 or decision1 == 1) and (decision2 == 3):
        print("FINAL APPROACH TOWARDS JFK")
        print("Engine 2 is in pretty bad shape. Temperature is becoming worse.")
        print("Engine 1 have just starte to increse the temperature as well.")
        print("Emergency personnel alreay in runway waiting for us!")
        print("We need to make our final decision ASAP!\n")
        print("1. Land in the longer runway maintaing speed and watching wind gusts.")
        print("2. Decide to land later and do a go around as winds are picking up.")
        print("3. Land on shorter runway as is far from emergency personnel. We not want more causalities in a bad event while landing.")
    user_choice = get_decision()
    time.sleep(3)
    return user_choice


def calculate_risk(decision):

    risk_points = {
        1: 0,
        2: 1,
        3: 2
    }

    points = risk_points[decision]

    return points


def determine_outcome(risk):
    if risk in (0, 1, 2):
        outcome = "Succesful Landing"
    elif risk in (3, 4):
        outcome = "Emergency Landing"
    else:
        outcome = "Aircraft Crash"
    print(f"\n{outcome}")
    print(f"\nLanding Score: {risk}")
    return outcome


def main():
    while True:
        display_title()
        clear_screen()
        name = captain_credentials()
        clear_screen()
        print("Starting Game...")
        time.sleep(3)
        decisions = []
        risk = 0
        clear_screen()
        decision1 = engine_emergency(name)
        decisions.append(decision1)
        risk += calculate_risk(decision1)
        clear_screen()
        decision2 = diversion(name, decision1)
        risk += calculate_risk(decision2)
        decisions.append(decision2)
        clear_screen()
        decision3 = final_approach(name, decision1, decision2, risk)
        risk += calculate_risk(decision3)
        decisions.append(decision3)
        clear_screen()
        outcome = determine_outcome(risk)

        game_data = {
            "captain": name,
            "decisions": decisions,
            "risk": risk,
            "outcome": outcome
        }

        with open("flight247_results.json", "w") as file:
            json.dump(game_data, file, indent=4)

        print("Game Finished")

        while True:
            replay = input(
                "\nWould you like to play again? (Y/N) ").strip().lower()

            if replay in ("y", "n"):

                break

            print("Please chose a valid answer.")
        if replay == "n":
            print("Thanks for playing")
            break


main()
