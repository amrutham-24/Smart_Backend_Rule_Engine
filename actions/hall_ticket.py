def block_hall_ticket(student_id):
    print(f"🚫 Hall ticket blocked for student {student_id}")
    return {
        "status": "blocked",
        "student_id": student_id
    }
