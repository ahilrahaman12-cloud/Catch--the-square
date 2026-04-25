import tkinter as tk
import random

class CatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Square!")
        self.score = 0
        
        # UI Elements: Score Label
        self.label = tk.Label(root, text="Score: 0", font=("Arial", 16))
        self.label.pack(pady=10)
        
        # Game Canvas
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white", highlightthickness=2, highlightbackground="black")
        self.canvas.pack(padx=20, pady=20)
        
        # The Target (Red Square)
        self.target = self.canvas.create_rectangle(0, 0, 30, 30, fill="red")
        
        # Bind a left-click event to the target
        self.canvas.tag_bind(self.target, "<Button-1>", self.handle_click)
        
        # Start the movement loop
        self.move_target()

    def move_target(self):
        # Generate random coordinates within the 400x400 canvas
        x = random.randint(0, 370)
        y = random.randint(0, 370)
        self.canvas.coords(self.target, x, y, x + 30, y + 30)
        
        # Move the square every 1.2 seconds automatically
        self.root.after(1200, self.move_target)

    def handle_click(self, event):
        # Update score and display
        self.score += 1
        self.label.config(text=f"Score: {self.score}")
        
        # Instantly move the target once clicked
        self.move_target()

# Standard boilerplate to start the GUI
if __name__ == "__main__":
    window = tk.Tk()
    game = CatchGame(window)
    window.mainloop()
