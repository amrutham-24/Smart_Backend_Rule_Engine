from actions.hall_ticket import block_hall_ticket
from actions.waitlist import move_to_waitlist
from actions.notifications import send_notification


def execute_action(action: str, context: dict):
    """
    Executes action based on rule output.
    """

    if action == "block_hall_ticket":
        return block_hall_ticket(context.get("student_id"))

    elif action == "move_to_waitlist":
        return move_to_waitlist(context.get("student_id"))

    elif action == "send_notification":
        return send_notification(context.get("message"))

    else:
        print(f"⚠ Unknown action: {action}")
        return None
