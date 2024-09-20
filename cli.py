from database import SessionLocal  # Import SessionLocal
from models import Guest, Room, Reservation, Inventory, Task, Staff
from datetime import datetime

# Add a guest to the database
def add_guest(name, email, phone):
    session = SessionLocal()  # Use SessionLocal to create a session
    guest = Guest(name=name, email=email, phone=phone)
    session.add(guest)
    session.commit()
    session.close()
    return guest

# List available rooms for booking (rooms without reservations)
def list_available_rooms():
    session = SessionLocal()  # Use SessionLocal to create a session
    available_rooms = session.query(Room).outerjoin(Reservation).filter(Reservation.id == None).all()
    session.close()

    if available_rooms:
        print("Available Rooms:")
        for room in available_rooms:
            print(f"Room {room.number}, Type: {room.room_type}, Price: {room.price}")
        return available_rooms
    else:
        print("No rooms are available.")
        return []



# Assign an inventory item to a guest
def assign_inventory_item():
    session = SessionLocal()  # Use SessionLocal to create a session

    # List guests to select from
    guests = session.query(Guest).all()
    if not guests:
        print("No guests available.")
        return

    print("Guests:")
    for guest in guests:
        print(f"{guest.id}. {guest.name} (Email: {guest.email})")

    guest_id = int(input("Enter the guest ID to assign an inventory item to: "))
    guest = session.query(Guest).filter_by(id=guest_id).first()

    if not guest:
        print("Guest not found.")
        return

    # Collect inventory item details
    item_name = input("Enter inventory item name: ")
    item_category = input("Enter inventory category: ")
    item_quantity = int(input("Enter quantity: "))

    # Create the inventory item
    inventory_item = Inventory(name=item_name, category=item_category, quantity=item_quantity, guest_id=guest.id)
    session.add(inventory_item)

    session.commit()
    print(f"Inventory item '{item_name}' assigned to {guest.name} successfully.")
    session.close()


# List all guests
def list_guests():
    session = SessionLocal()  # Use SessionLocal to create a session
    guests = session.query(Guest).all()

    print("Guests:")
    for guest in guests:
        print(f"{guest.name}, Email: {guest.email}, Phone: {guest.phone}")

    session.close()

# List all inventory items
def list_inventory():
    session = SessionLocal()  # Use SessionLocal to create a session
    items = session.query(Inventory).all()
    
    print("Inventory Items:")
    for item in items:
        print(f"{item.name}, Category: {item.category}, Quantity: {item.quantity}, Assigned to Guest: {item.guest.name if item.guest else 'None'}")
    
    session.close()


def book_reservation():
    session = SessionLocal()

    # Check if there are available rooms
    available_rooms = list_available_rooms()
    if not available_rooms:
        print("No rooms available to reserve.")
        return

    # Collect guest information
    guest_name = input("Enter guest name: ")
    guest_email = input("Enter guest email: ")
    guest_phone = input("Enter guest phone: ")

    # Check if guest exists, if not create a new guest
    guest = session.query(Guest).filter_by(email=guest_email).first()
    if not guest:
        guest = Guest(name=guest_name, email=guest_email, phone=guest_phone)
        session.add(guest)
        session.commit()  # Commit to assign an ID to the guest

    # Prompt the user to choose a room type
    room_type = input("Enter the room type you want to reserve (e.g., 'ordinary', 'basic', 'first-class'): ")

    # Filter the available rooms by the selected room type
    selected_rooms = [room for room in available_rooms if room.room_type == room_type]
    
    if not selected_rooms:
        print(f"No rooms available for the selected type: {room_type}")
        return

    # Select the first available room of the chosen type
    selected_room = selected_rooms[0]

    # Collect reservation details
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")

    # Create a new reservation
    reservation = Reservation(guest_id=guest.id, room_id=selected_room.id, check_in_date=check_in, check_out_date=check_out)
    session.add(reservation)

    # Commit the reservation to generate the reservation ID
    session.commit()

    print(f"Reservation made successfully for {guest_name} in room {selected_room.number} ({room_type} type)!")
    
    session.close()


# Function to assign a task to a hotel staff member
def assign_task():
    session = SessionLocal()
    staff_members = session.query(Staff).all()

    if not staff_members:
        print("No staff available.")
        return

    print("Available Staff:")
    for staff in staff_members:
        print(f"Staff ID: {staff.id}, Name: {staff.name}")

    staff_id = input("Enter the ID of the staff to assign the task: ")
    task_description = input("Enter task description: ")
    
    staff_member = session.query(Staff).filter(Staff.id == staff_id).first()

    if staff_member:
        new_task = Task(description=task_description, staff_id=staff_member.id)
        session.add(new_task)
        session.commit()
        print(f"Task '{task_description}' has been assigned to {staff_member.name}.")
    else:
        print("Staff member not found.")
    
    session.close()


def checkout_guest():
    session = SessionLocal()
    guest_id = input("Enter the ID of the guest to check out: ")
    guest = session.query(Guest).filter_by(id=guest_id).first()

    if guest:
        # Find the reservation associated with this guest and delete it
        reservation = session.query(Reservation).filter_by(guest_id=guest.id).first()
        if reservation:
            session.delete(reservation)
            session.delete(guest)
            session.commit()
            print(f"Guest {guest.name} has been checked out and reservation removed.")
        else:
            print(f"No reservation found for guest ID: {guest_id}")
    else:
        print(f"No guest found with ID: {guest_id}")

    session.close()
