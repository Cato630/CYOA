#Import different tools
import time
import sys


#create scrolling rule
def print_scroll(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.02)


def load_story(section_title, file_path="D:\coding\DNDgame\choose_your_own_adventure_story.txt"):
    #I was running into errors with not being able to open this file: Using stack overflow I was able to realize I could encode and by pass those errors
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
#create new lines per section
    sections = content.split('\n\n')
    section_dict = {}
#establish a memory of what desision path we are on
    current_title = None
    current_text = []
#Establish what is happening in each section
    for section in sections:
        section = section.strip()
        if section == '':
            continue
        # Create how to read the text for each section
        if section.startswith(('CHAPTER', 'ENDING', 'INTRODUCTION')):
            if current_title:
                section_dict[current_title] = '\n\n'.join(current_text).strip()
            current_title = section
            current_text = []
        else:
            current_text.append(section)

    # Capture the last section
    if current_title:
        section_dict[current_title] = '\n\n'.join(current_text).strip()

    return section_dict.get(section_title, f"Section '{section_title}' not found.")
#Create the Narative
def introduction():
    intro_text = load_story("INTRODUCTION: ARRIVAL")
    print_scroll(intro_text)

    #create the first choice you could choose that starts the game:
def first_choice():
    print("\nDo you:")
    print("A: Go directly to Eldrin.")
    print("B: Explore the village first.")
    print("C: Chase down the carriage and return to the guild.")

    #Create the Options
    while True:
        choice = input("Enter your choice(A,B,C): ").upper()
        if choice == "A":
            chapter_eldrin()
            break
        if choice == "B":
            chapter_village()
            break
        if choice == "C":
            print_scroll(load_story("INTRODUCTION: THE TRAP"))
            introduction()
            first_choice()
            break
        else:
            print("That is not an option, please try again: (A,B,C)")


  #Create the choices for the chapter  
def chapter_eldrin():
    print_scroll(load_story("CHAPTER 1: INTO THE WOODS"))
    print("\nDo you:")
    print("A: Enter the Circle alone?")
    print("B: Perform the ritual with Eldrin?")
    print("C: Leave Eldrin alone and head to the village? ")

    #Create the Options from this selection
    while True:
        choice = input("Enter your choice(A,B,C,D): ").upper()
        if choice == "A":
            print_scroll(load_story("ENDING A: THE FORGOTTEN ONE"))
            break
        elif choice == "B":
            print_scroll(load_story("ENDING B: THE WARDEN"))
            break
        elif choice == "C":
            print_scroll(load_story("ENDING C: ABBANDON THE RITE"))
            chapter_village()
            break
        else:
            print("That is not an option, please try again: (A,B,C)")
#create the other set of choices
def chapter_village():
     print_scroll(load_story("CHAPTER 2: INTO THE VILLAGE"))
     print("\nDo you:")
     print("A) Visit the baker.")
     print("B) Go to the tavern.")
     print("C) Rally the villagers.")

     #Create the options that happen
     while True:
         choice = input("Enter your choice(A,B,C): ").upper()
         if choice == "A":
             print_scroll(load_story("ENDING VA: THE SEER"))
             break
         elif choice == "B":
             print_scroll(load_story("ENDING VB: THE DRUNKARD"))
             break
         elif choice == "C":
             print_scroll(load_story("ENDING VC: THE DEFFENDERS"))
             break
         else:
            print("That is not an option, please try again: (A,B,C)")

#The Main Game
def main():
    introduction()
    first_choice()

if __name__ == "__main__":
    main()
