# TIMG 5301 F24: ASSIGNMENT 3
# Group 1
# ======================

from swarm import Swarm, Agent
from swarm.repl import run_demo_loop
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Ensure REMOVED_API_KEY is set in the environment
#os.environ["REMOVED_API_KEY"] = os.getenv("REMOVED_API_KEY", "REMOVED_API_KEY")
# Initialize Swarm
client = Swarm()  # Swarm will use the API key from the environment

# Define Tools
def collect_more_information():
    """Collect more details about the customer's requirements."""
    print("Apology, I need more details to assist you. Please answer the following questions:")
    # Collect customer inputs
    usage_type = input("Is your internet need for Residential or Business use? (Residential/Business): ").strip().lower()
    if usage_type == "exit":
        return "Exit"
    # Package the information into a dictionary
    collected_info = {
        "usage_type": usage_type
    }
    # Logic to decide routing
    if usage_type == "residential":
        print(f"Transfer to Residential Sales.")
        route = "Residential Sales"
    elif usage_type == "business":
        print(f"Transfer to Business Sales.")
        route = "Business Sales"
    else:
        print("Unable to determine routing. Please provide clear usage information.")
        route = "Unknown"
    # Return the collected information and routing decision
    return {"collected_info": collected_info, "route": route}


def choose_residential_plan(number_of_user: int):
    """Choose a suitable residential services plan based on the number of users."""
    if str(number_of_user).lower() == "exit":
        return "Exit"
    # Plan information based on the provided data
    plans = {
        1: {"name": "Freedom 6 DSL", "price": 39.95, "speed": "6 Mbps / 0.8 Mbps"},
        2: {"name": "Freedom 15 DSL", "price": 48.95, "speed": "15 Mbps / 10 Mbps"},
        3: {"name": "Freedom 25 DSL", "price": 55.95, "speed": "25 Mbps / 10 Mbps"},
        4: {"name": "Freedom 30 Cable", "price": 59.95, "speed": "30 Mbps / 5 Mbps"},
        5: {"name": "Freedom 50 DSL", "price": 58.95, "speed": "50 Mbps / 10 Mbps"},
        6: {"name": "Freedom 100 Cable", "price": 68.95, "speed": "100 Mbps / 30 Mbps"},
    }

    # Determine the recommended plan based on number of users
    if number_of_user <= 2:
        recommended_plan = 1  # Freedom 6 DSL
    elif 3 <= number_of_user <= 4:
        recommended_plan = 2  # Freedom 15 DSL
    elif 5 <= number_of_user <= 7:
        recommended_plan = 3  # Freedom 25 DSL
    elif 8 <= number_of_user <= 10:
        recommended_plan = 4  # Freedom 30 Cable
    elif 11 <= number_of_user <= 15:
        recommended_plan = 5  # Freedom 50 DSL
    else:
        recommended_plan = 6  # Freedom 100 Cable

    # Display recommended plan
    print(f"\nRecommended Plan for {number_of_user} users:")
    print(
        f"{plans[recommended_plan]['name']}: ${plans[recommended_plan]['price']}/month, "
        f"Speed: {plans[recommended_plan]['speed']}"
    )

    # Display all available plans
    print("\nHere are all the available plans:")
    for key, plan in plans.items():
        print(
            f"{key}. {plan['name']}: ${plan['price']}/month, Speed: {plan['speed']}"
        )

    # Allow user to choose a plan
    try:
        choice = input("\nEnter the number of your chosen plan (1-6) or type 'Exit' to quit: ").strip()
        if choice.lower() == "exit":
            return "Exit"
        choice = int(choice)
        if choice in plans:
            selected_plan = plans[choice]
            return (
                f"You selected {selected_plan['name']} for ${selected_plan['price']}/month "
                f"with a speed of {selected_plan['speed']}."
            )
        else:
            return "Invalid choice. Please select a valid plan number."
    except ValueError:
        return "Invalid input. Please enter a number between 1 and 6."


def choose_business_plan(number_of_user: int):
    """Choose a suitable business services plan based on the number of users."""
    if str(number_of_user).lower() == "exit":
        return "Exit"
    # Plan information based on the provided data
    plans = {
        1: {"name": "Business 6 DSL", "price": 49.95, "speed": "6 Mbps / 0.8 Mbps"},
        2: {"name": "Business 10 DSL", "price": 49.95, "speed": "10 Mbps / 7 Mbps"},
        3: {"name": "Business 16 DSL", "price": 54.95, "speed": "16 Mbps / 10 Mbps"},
        4: {"name": "Business 25 DSL", "price": 64.95, "speed": "25 Mbps / 10 Mbps"},
        5: {"name": "Business 30 Cable", "price": 59.95, "speed": "30 Mbps / 5 Mbps"},
        6: {"name": "Business 50 DSL", "price": 69.95, "speed": "50 Mbps / 10 Mbps"},
        7: {"name": "Business 100 Cable", "price": 68.95, "speed": "100 Mbps / 30 Mbps"},
    }

    # For users above 31, customer to speak with human agent for custom solution
    if number_of_user > 31:
        return (
            f"For the number of user mentioned we can provide a custom solution. Please contact our Business Agent at +1 613 987 654, Mon - Fri, 9AM - 4PM"
        )

    # Determine the recommended plan based on the number of users
    if number_of_user <= 2:
        recommended_plan = 1  # Business 6 DSL
    elif 3 <= number_of_user <= 5:
        recommended_plan = 2  # Business 10 DSL
    elif 6 <= number_of_user <= 10:
        recommended_plan = 3  # Business 16 DSL
    elif 11 <= number_of_user <= 15:
        recommended_plan = 4  # Business 25 DSL
    elif 16 <= number_of_user <= 20:
        recommended_plan = 5  # Business 30 Cable
    elif 21 <= number_of_user <= 30:
        recommended_plan = 6  # Business 50 DSL
    else:
        recommended_plan = 7  # Business 100 Cable

    # Display recommended plan
    print(f"\nRecommended Plan for {number_of_user} users:")
    print(
        f"{plans[recommended_plan]['name']}: ${plans[recommended_plan]['price']}/month, "
        f"Speed: {plans[recommended_plan]['speed']}"
    )

    # Display all available plans
    print("\nHere are all the available plans:")
    for key, plan in plans.items():
        print(
            f"{key}. {plan['name']}: ${plan['price']}/month, Speed: {plan['speed']}"
        )

    # Allow user to choose a plan
    try:
        choice = int(input("\nEnter the number of your chosen plan (1-7): "))
        if choice in plans:
            selected_plan = plans[choice]
            return (
                f"You selected {selected_plan['name']} for ${selected_plan['price']}/month "
                f"with a speed of {selected_plan['speed']}."
            )
        else:
            return "Invalid choice. Please select a valid plan number."
    except ValueError:
        return "Invalid input. Please enter a number between 1 and 7."


# Improved Interactive Triage System
def interactive_triage_system():
    """Interactive Triage System with an exit condition."""
    print("\nWelcome to the Interactive Triage System!")
    print("Type 'exit' to quit the system.\n")

    while True:
        user_query = input("Enter your query: ").strip()
        # Exit condition
        if user_query.lower() == "exit":
            print("Thank you for using the Triage System. Have a great day!")
            sys.exit(0)  # Use sys.exit() to terminate Python completely

        # Handle the query and continue
        print(f"Triage Agent: Processing your query: {user_query}")

# Define Handoffs
def transfer_to_Residential_Sales():
    """Transfer the customer to Residential Sales."""
    return Residential_Sales
def transfer_to_Business_Sales():
    """Transfer the customer to Business Sales."""
    return Business_Sales
def transfer_back_to_triage():
    """Transfer the customer to triage."""
    return Triage

# Define Triage
Triage = Agent(
    name="Triage",
    instructions="""
    You are a Triage for Internet provider company.
    You responsible for routing customer queries to the appropriate sales agent.
    Steps:
    1. Greet the customer.
    2. Collect detail requirement such as name and internet needs.
    3. Transfer to suitable sales.
    
    If you cannot help, collect more details of requirement.
    """,
    functions=[transfer_to_Residential_Sales, transfer_to_Business_Sales, collect_more_information],
)
# Define a Residential Sales Agent
Residential_Sales = Agent(
    name="Residential Sales",
    instructions="""
    You are a Residential Sales.
    You deal with questions about Home Internet Service.
    Steps:
    1. Collect customer's needs and budget.
    2. Recommend an internet plan options based on residential users users.
    3. Inform customer that the order has been confirmed and sent to the Installation Agents.
    
    If you cannot help, transfer back to triage.
    """,
    functions=[choose_residential_plan, transfer_back_to_triage],
)
# Define a Business Sales Agent
Business_Sales = Agent(
    name="Business Sales",
    instructions="""
    You are a Business Sales.
    You deal with questions about Internet Packages for Small Businesses.
    Steps:
    1. Collect the number of user size in the company.
    2. Recommend an internet plan options based on the number of business services users.

    If you cannot help, transfer back to triage.
    """,
    functions=[choose_business_plan, transfer_back_to_triage],
)
# Start conversation
run_demo_loop(Triage, greeting="Welcome to the Group 1 Bot.")
