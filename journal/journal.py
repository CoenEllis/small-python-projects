import json
import datetime

"""
Super cool journal program
"""


# Class for the journal
class Journal:
    # Constructor
    def __init__(self, filename: str = "journal.json"):
        self.filename = filename
        self.entries = self.load_entries()

    # Load entries from JSON
    def load_entries(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError, IOError, OSError):
            return []

    # Save the new entries to the JSON
    def save_entries(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.entries, f, indent=4)
        except (IOError, OSError) as e:
            print(f"Error saving entries: {e}")

    # Add a new entry to the JSON
    def add_entry(self, title: str, content: str):
        timestamp = datetime.datetime.now()
        if not title:
            title = str(timestamp)
        self.entries.append({
            "title": title,
            "content": content,
            "timestamp": timestamp.isoformat(),
            "edited_timestamp": None
        })
        self.save_entries()

    # Check if a specific element exists in the JSON
    def has_entry(self, key: str, value) -> bool:
        return any(entry.get(key) == value for entry in self.entries)

    # Edits an entry
    def edit_entry(self, title: str, new_title: str, content: str):
        for entry in self.entries[:]:
            if entry["title"] == title:
                timestamp = datetime.datetime.now()
                entry["title"] = new_title if new_title else str(timestamp)
                entry["content"] = content
                entry["edited_timestamp"] = timestamp.isoformat()
                self.save_entries()
                return True
        return False

    # Deletes an entry
    def delete_entry(self, title: str):
        for entry in self.entries[:]:
            if entry["title"] == title:
                self.entries.remove(entry)
                self.save_entries()
                return True
        return False

    # Returns the entry with the given title
    def return_by_title(self, title: str):
        for entry in self.entries[:]:
            if entry["title"] == title:
                return entry
        return None

    # Returns the entry with the given timestamp
    def return_by_timestamp(self, timestamp: str):
        for entry in self.entries[:]:
            if entry["timestamp"] == timestamp:
                return entry
        return None

    # Returns the entry with the given edited timestamp
    def return_by_edited_timestamp(self, timestamp: str):
        for entry in self.entries[:]:
            if entry["edited_timestamp"] == timestamp:
                return entry
        return None


choice = None  # Initialize choice at none
journal = Journal()  # Instantiates the journal object
print("--- Journal Program ---")
while choice != '0':  # Continue until 0 is typed
    print("")
    print("0: Exit")
    print("1: New entry")
    print("2: Edit entry")
    print("3: Find")
    print("4: Slice")
    print("5: Delete")
    choice = input("Choice: ")

    if choice == '1':  # New entry
        title = input("Title (if none, date will be title): ")
        content = input("")
        journal.add_entry(title, content)
    elif choice == '2':  # Edit entry
        title = input("Title: ")
        if journal.has_entry("title", title):
            new_title = input("New title: ")
            content = input("Content: ")
            journal.edit_entry(title, new_title, content)
        else:
            print("Not found.")
    elif choice == '3':  # Find
        print("1: Search by title")
        print("2: Search by timestamp")
        print("3: Search by timestamp edited")
        choice = input("Choice: ")
        if choice == '1':
            title = input("Title: ")
            if journal.has_entry("title", title):
                entry = journal.return_by_title(title)
                print("")
                print(entry["content"])
                print(f"\n-----\nTimestamp: {entry['timestamp']}")
                if entry["edited_timestamp"] is not None:
                    print(f"Edited timestamp: {entry['edited_timestamp']}")
            else:
                print("Not found.")
        elif choice == '2':
            timestamp = input("Timestamp: ")
            if journal.has_entry("timestamp", timestamp):
                entry = journal.return_by_timestamp(timestamp)
                print("")
                print(entry["title"])
                print("\n---\n")
                print(entry["content"])
                if entry["edited_timestamp"] is not None:
                    print(f"\n--- Edited: {entry['edited_timestamp']}")
            else:
                print("Not found.")
        elif choice == '3':
            timestamp = input("Timestamp: ")
            if journal.has_entry("edited_timestamp", timestamp):
                entry = journal.return_by_edited_timestamp(timestamp)
                print("")
                print(entry["title"])
                print("\n---\n")
                print(entry["content"])
                print(f"\n-----\nTimestamp: {entry['timestamp']}")
            else:
                print("Not found.")
        else:
            print("???")
    elif choice == '4':  # Slice
        slice_input = input("Slice (without brackets): ")
        entries = journal.entries
        try:
            parts = slice_input.split(':')
            start = int(parts[0]) if parts[0] else None
            stop = int(parts[1]) if len(parts) > 1 and parts[1] else None
            step = int(parts[2]) if len(parts) > 2 and parts[2] else None
            sliced_entries = entries[start:stop:step]
            for entry in sliced_entries:
                print("")
                print(entry["title"])
                print("\n---\n")
                print(entry["content"])
                print(f"\n-----\nTimestamp: {entry['timestamp']}")
                if entry["edited_timestamp"] is not None:
                    print(f"Edited timestamp: {entry['edited_timestamp']}")
        except (ValueError, IndexError):
            print("Bad slicing.")
    elif choice == '5':  # Delete
        title = input("Title: ")
        if journal.delete_entry(title):
            print("Deleted.")
        else:
            print("Not found.")
    else:  # Bad input
        print("???")
