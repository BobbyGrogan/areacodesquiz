import random

def read_layered_list(filename):
    layered_list = []
    with open(filename, 'r') as file:
        for line in file:
            # Clean and format the line
            line = line.strip().strip('[]').strip()
            if line:
                # Split based on the first occurrence of ', '
                parts = line.split("', '")
                if len(parts) == 2:
                    number = parts[0].strip("'")
                    location = parts[1].strip("'")
                    layered_list.append([number, location])
    return layered_list

def deliver_quiz(layered_list, quiz_type, num_questions):
    score = 0
    total_questions = min(num_questions, len(layered_list))
    
    for number, location in random.sample(layered_list, total_questions):
        if quiz_type == "m":
            # Generate multiple choice options
            options = random.sample(layered_list, 4)
            if [number, location] not in options:
                options[random.randint(0, 3)] = [number, location]
            options_text = "\n".join([f"{i+1}. {opt[1]}" for i, opt in enumerate(options)])
            
            print(f"\nWhat is the location for the code {number}?\n")
            print(options_text)
            answer = input("Your answer (1/2/3/4): ").strip()
            
            try:
                if options[int(answer) - 1][1] == location:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {location}.\n")
            except (IndexError, ValueError):
                print(f"Invalid input! The correct answer is {location}.\n")
                
        elif quiz_type == "f":
            print(f"What is the code for the location {location}?")
            answer = input("Your answer: ").strip()
            
            if answer == number:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {number}.\n")
    
    print(f"\nYour final score is {score} out of {total_questions}.")

def main():
    filename = 'list.txt'
    layered_list = read_layered_list(filename)
    
    quiz_type = input("Choose quiz type: 'm' (multiple choice) or 'f' (free response): ").strip().lower()
    if quiz_type not in ["m", "f"]:
        print("Invalid quiz type selected. Exiting.")
        return

    try:
        num_questions = int(input(f"Enter the number of questions (1 to {len(layered_list)}): ").strip())
        if num_questions < 1 or num_questions > len(layered_list):
            raise ValueError
    except ValueError:
        print("Invalid number of questions. Exiting.")
        return
    
    deliver_quiz(layered_list, quiz_type, num_questions)

if __name__ == "__main__":
    main()
