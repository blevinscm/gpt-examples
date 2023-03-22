import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import random
import openai
import configparser
import os

# Load configuration file
config = configparser.ConfigParser()
config.read("../config.ini")

# Set up your GPT-3 API key
openai.api_key = config.get("openai", "api_key")

# Character class definition
class Character:
    def __init__(self, archetype, name, description, motivation):
        self.archetype = archetype
        self.name = name
        self.description = description
        self.motivation = motivation

# GPT-3.5 Turbo API call function to generate dialogue
def generate_gpt3_dialogue(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a screenplay writer."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content.strip()

# Generate script function
def generate_script(characters, stage_characters, plot):
    script = f"Basic Plot:\n{plot}\n\n"

    monomyth_stages = [
        "1. Ordinary World",
        "2. Call to Adventure",
        "3. Refusal of the Call",
        "4. Meeting the Mentor",
        "5. Crossing the First Threshold",
        "6. Tests, Allies, and Enemies",
        "7. Approach to the Inmost Cave",
        "8. Ordeal",
        "9. Reward",
        "10. The Road Back",
        "11. Resurrection",
        "12. Return with the Elixir"
    ]

    for stage, stage_char in zip(monomyth_stages, stage_characters):
        script += f"{stage}\n"
        script += f"Characters involved: {', '.join([char.name for char in stage_char])}\n"
        script += "Scene description:\n\n"
        script += "Dialogue:\n"
        for character in stage_char:
            prompt = f"In a movie script, {character.name} ({character.archetype}) says something related to the plot: {plot}. Their motivation is {character.motivation}. What would they say?"
            dialogue = generate_gpt3_dialogue(prompt)
            script += f"{character.name}: {dialogue}\n"
        script += "\n\n"

    return script

# Main function with the user interface
def main():
    def on_generate():
        stage_characters = []
        for stage_vars in stage_vars_list:
            stage_char = [characters[i] for i, var in enumerate(stage_vars) if var.get()]
            stage_characters.append(stage_char)
        script = generate_script(characters, stage_characters, plot_text.get("1.0", tk.END))
        # print(script)
        filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save Script", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename:
            with open(filename, "w") as f:
                f.write(script)
        



    archetypes = [
        ("Hero", "The protagonist, who embarks on a journey and undergoes significant change."),
        ("Mentor", "A wise and experienced guide who helps the Hero along their journey."),
        ("Threshold Guardian", "A character who tests the Hero's commitment to the journey."),
        ("Herald", "A character who brings the Call to Adventure, signaling the start of the journey."),
        ("Shapeshifter", "A character with unclear or shifting loyalties, causing uncertainty."),
        ("Shadow", "The antagonist, representing the fears or challenges the Hero must overcome."),
        ("Ally", "A supportive character who helps the Hero during the journey."),
        ("Trickster", "A character who brings humor, mischief, or chaos to the story.")
    ]

    root = tk.Tk()
    root.title("Movie Script Generator")

    characters = []
    for i, (archetype, description) in enumerate(archetypes):
        label = tk.Label(root, text=f"{archetype}: {description}")
        label.grid(row=i, column=0, sticky="w")
        entry = tk.Entry(root)
        entry.grid(row=i, column=1)
        motivation_entry = tk.Entry(root)
        motivation_entry.grid(row=i, column=2)
        characters.append(Character(archetype, entry.get(), description, motivation_entry.get()))

    stage_vars_list = []
    for i, stage in enumerate(range(1, 13)):
        label = tk.Label(root, text=f"Stage {stage}:")
        label.grid(row=i, column=3, sticky="w")
        stage_vars = []
        for j, char in enumerate(characters):
            var = tk.BooleanVar()
            stage_vars.append(var)
            chk = tk.Checkbutton(root, text=char.archetype, variable=var)
            chk.grid(row=i, column=4 + j)
        stage_vars_list.append(stage_vars)

    plot_label = tk.Label(root, text="Basic Plot:")
    plot_label.grid(row=13, column=0, sticky="w")
    plot_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=4)
    plot_text.grid(row=13, column=1, columnspan=len(characters), sticky="w")

    generate_button = tk.Button(root, text="Generate Script", command=on_generate)
    generate_button.grid(row=14, column=0, columnspan=4)

    root.mainloop()

if __name__ == "__main__":
    main()
