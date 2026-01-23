def move_to_waitlist(student_id):
    print(f"⏳ Student {student_id} moved to waitlist")
    return {
        "status": "waitlisted",
        "student_id": student_id
    }
