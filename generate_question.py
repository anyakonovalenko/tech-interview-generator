#!/usr/bin/env python3
"""
Simple CLI tool to generate technical interview questions.
Usage: python generate_question.py
"""

import os
import sys
import dspy
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from interview_generator import CompleteInterviewGenerator, InterviewPipeline


def setup_dspy():
    """Setup DSPy with OpenAI."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY not found!")
        print("\nSetup instructions:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to .env")
        print("3. Run this script again")
        sys.exit(1)

    lm = dspy.LM('openai/gpt-4o-mini', api_key=api_key)
    dspy.configure(lm=lm)


def print_banner():
    """Print welcome banner."""
    print("\n" + "=" * 60)
    print("       TECH INTERVIEW QUESTION GENERATOR")
    print("=" * 60 + "\n")


def get_user_choice(prompt, options):
    """Get user choice from options."""
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = input("\nEnter number: ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
            print("Invalid choice. Try again.")
        except (ValueError, KeyboardInterrupt):
            print("\nExiting...")
            sys.exit(0)


def get_text_input(prompt):
    """Get text input from user."""
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            print("Please enter a value.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)


def generate_question_interactive():
    """Interactive question generation."""
    print_banner()

    # Question type
    question_type = get_user_choice(
        "What type of question do you want?",
        ["Coding/Algorithms", "ML Theory", "ML Practical"]
    )

    type_mapping = {
        "Coding/Algorithms": "coding",
        "ML Theory": "ml_theory",
        "ML Practical": "ml_practical"
    }
    question_type = type_mapping[question_type]

    # Topic
    print("\nWhat topic? (e.g., 'binary trees', 'neural networks', 'gradient descent')")
    topic = get_text_input("Topic: ")

    # Difficulty
    difficulty = get_user_choice(
        "\nDifficulty level?",
        ["easy", "medium", "hard"]
    )

    # Number of follow-ups
    num_followups = int(get_user_choice(
        "\nHow many follow-up questions?",
        ["1", "2", "3", "4"]
    ))

    # Generate
    print("\n" + "=" * 60)
    print("Generating question... (this may take a few seconds)")
    print("=" * 60 + "\n")

    generator = CompleteInterviewGenerator()
    result = generator(
        topic=topic,
        question_type=question_type,
        difficulty=difficulty,
        num_followups=num_followups
    )

    # Display results
    print("\n" + "=" * 60)
    print("GENERATED INTERVIEW QUESTION")
    print("=" * 60 + "\n")
    print(f"Topic: {topic}")
    print(f"Type: {question_type}")
    print(f"Difficulty: {difficulty}\n")
    print("-" * 60)
    print(result['question'])
    print("-" * 60)
    print("\nFOLLOW-UP QUESTIONS:")
    print(result['followup_questions'])
    print("\n" + "=" * 60 + "\n")


def generate_question_quick(topic, question_type="coding", difficulty="medium"):
    """Quick generation without interaction."""
    print_banner()
    print(f"Generating {difficulty} {question_type} question on: {topic}\n")

    generator = CompleteInterviewGenerator()
    result = generator(
        topic=topic,
        question_type=question_type,
        difficulty=difficulty,
        num_followups=2
    )

    print("=" * 60)
    print(result['question'])
    print("=" * 60)
    print("\nFollow-ups:")
    print(result['followup_questions'])
    print("\n")


def main():
    """Main entry point."""
    setup_dspy()

    # Check if arguments provided
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
        generate_question_quick(topic)
    else:
        generate_question_interactive()


if __name__ == "__main__":
    main()
