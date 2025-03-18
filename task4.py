contacts = {}

def main():
    """Main function to run the assistant bot with a command loop"""
    print("Welcome to the assistant bot!")

    commands = {
        "hello": greet,
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "close": goodbye,
        "exit": goodbye
    }

    while True: 
        user_input = input("Enter a command: ")
        try:
            cmd, *args = parse_input(user_input)
            if cmd in commands:
                print(commands[cmd](*args))
                if cmd in ["close", "exit"]:
                    break
            else:
                print("Invalid command. Available commands:", ", ".join(commands.keys()))
        except Exception as e:
            print(f"Error: {e}")

def input_error(func):
    """Decorator to handle common input errors in bot commands"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Please enter a valid key."
        except IndexError:
            return "Give me name please."

    return inner

def parse_input(user_input):
    """Parse user input into command and arguments"""
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args

@input_error
def add_contact(*args):
    """Add a new contact to the contacts dictionary"""
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(*args):
    """Update an existing contact's phone number"""
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(*args):
    """Show the phone number for a specific contact"""
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

def show_all():
    """Show all contacts in the address book"""
    return "\n".join([f"{name} - {phone}" for name, phone in contacts.items()]) or "No contacts found."

def greet():
    """Return a greeting message"""
    return "How can I help you?"

def goodbye():
    """Return a farewell message"""
    return "Goodbye!"

if __name__ == "__main__":
    main()
