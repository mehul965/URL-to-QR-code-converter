import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x500")
        self.root.configure(bg='lightblue')

        self.movies_with_hints = {
            "Dangal": "Maari chhoriyaan chhoro se kam hai ke?",
            "3 IDIOTS": "Aal izz well.",
            "Dabang": "Swagat nahi karoge hamara?",
            "CHENNAI EXPRESS": "Don't underestimate the power of a common man.",
            "SHOLAY": "Kitne Aadmi The"
        }
        self.secret_movie = random.choice(list(self.movies_with_hints.keys()))
        self.hint = self.movies_with_hints[self.secret_movie]
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 24), bg='lightblue')
        self.title_label.pack(pady=20)

        self.hint_label = tk.Label(self.root, text=f"Hint: {self.hint}", font=("Helvetica", 16), bg='lightblue')
        self.hint_label.pack(pady=10)

        self.movie_label = tk.Label(self.root, text=self.get_display_text(), font=("Helvetica", 18), bg='lightblue')
        self.movie_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self.root, text="Guess", font=("Helvetica", 16), command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.status_label = tk.Label(self.root, text=f"Attempts left: {self.max_attempts}", font=("Helvetica", 16), bg='lightblue')
        self.status_label.pack(pady=10)

        self.restart_button = tk.Button(self.root, text="Restart", font=("Helvetica", 16), command=self.restart_game)
        self.restart_button.pack(pady=10)

    def get_display_text(self):
        return " ".join([letter if letter in self.guesses or letter == " " else "_" for letter in self.secret_movie])

    def make_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)
        
        if len(guess) == 0:
            messagebox.showwarning("Invalid Input", "Please enter a letter or the full movie name.")
            return
        
        if len(guess) == 1:
            if not guess.isalpha():
                messagebox.showwarning("Invalid Input", "Please enter a valid letter.")
                return
            
            if guess in self.guesses:
                messagebox.showinfo("Already Guessed", "You've already guessed that letter.")
                return
            
            self.guesses.append(guess)
            if guess not in self.secret_movie:
                self.attempts += 1
        elif len(guess) == len(self.secret_movie) and guess.replace(" ", "") == self.secret_movie.replace(" ", ""):
            self.guesses = list(self.secret_movie)
        else:
            messagebox.showwarning("Incorrect Guess", "The movie name is incorrect.")
            self.attempts += 1

        if self.attempts >= self.max_attempts:
            self.end_game(False)
        elif "_" not in self.get_display_text():
            self.end_game(True)
        else:
            self.update_status()

    def update_status(self):
        self.movie_label.config(text=self.get_display_text())
        self.status_label.config(text=f"Attempts left: {self.max_attempts - self.attempts}")

    def end_game(self, won):
        if won:
            messagebox.showinfo("Congratulations!", f"You've guessed the movie: {self.secret_movie}")
        else:
            messagebox.showerror("Game Over", f"You've lost! The movie was: {self.secret_movie}")
        self.restart_game()

    def restart_game(self):
        self.secret_movie = random.choice(list(self.movies_with_hints.keys()))
        self.hint = self.movies_with_hints[self.secret_movie]
        self.guesses = []
        self.attempts = 0
        self.hint_label.config(text=f"Hint: {self.hint}")
        self.movie_label.config(text=self.get_display_text())
        self.status_label.config(text=f"Attempts left: {self.max_attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
