import sys
import os
from notebook import Notebook, Note

class Menu:
	"""Show the menu when the run function is called..."""
	def __init__(self):
		self.notebook = Notebook()
		self.choices = {
		"1": self.show_notes,
		"2": self.search_notes,
		"3": self.add_note,
		"4": self.modify_note,
		"5": self.quit
		}

	def display_menu(self):
		print("""
			Notebook Menu

			1. Show all Notes
			2. Search Notes
			3. Add Note
			4. Modify Note
			5. Quit

			""")
	def run(self):
		'''Display the menu and respond to choices...'''
		while True:
			os.system("cls")
			self.display_menu()
			choice = input("Enter an option: ")
			action = self.choices.get(choice)
			if action:
				os.system("cls")
				action()
			else:
				os.system("cls")
				print(f"{choice} is not an avaiable choice!")

	def show_notes(self, notes=None):
		if not notes:
			notes = self.notebook.notes

		for note in notes:
			print(f"ID -> {note.id}|| TAGS -> {note.tags}\n NOTE: \n{note.memo}")

		wait = input("Press enter to continue... ")

	def search_notes(self):
		filter = input("Search for: ")
		notes = self.notebook.search(filter)
		self.show_notes(notes)

	def add_note(self):
		memo = input("Enter a memo: ")
		tags = input("Enter tags for your new note: ")
		self.notebook.new_note(memo, tags)
		print("Your note has been added.")

	def modify_note(self):
		id = int(input("Enter a note id: "))
		memo = input("Enter a memo: ")
		tags = input("Enter tags: ")
		if memo:
			self.notebook.modify_memo(id, memo)
		if tags:
			self.notebook.modify_tags(id, tags)

	def quit(self):
		print("Thank you for using your notebook today! ")
		sys.exit(0)

if __name__ == "__main__":
	Menu().run()