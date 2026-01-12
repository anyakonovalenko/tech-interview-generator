"""
Advanced Usage: Complete Interview Pipeline

This example shows how to use DSPy's module composition to create
a complete interview generation pipeline.
"""

import os
import dspy
from dotenv import load_dotenv
from interview_generator import InterviewPipeline, CompleteInterviewGenerator

load_dotenv()


def setup_dspy():
    """Initialize DSPy."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY in your .env file")

    lm = dspy.LM('openai/gpt-4o-mini', api_key=api_key)
    dspy.configure(lm=lm)
    print("✓ DSPy configured\n")


def generate_complete_interview_set():
    """Generate a complete interview question with validation and follow-ups."""
    print("=" * 60)
    print("Complete Interview Pipeline")
    print("=" * 60)

    # Use the complete pipeline
    pipeline = InterviewPipeline()

    result = pipeline(
        topic="dynamic programming",
        question_type="coding",
        difficulty="hard",
        num_followups=3
    )

    print(f"\nMain Question:\n{result['question']}\n")
    print(f"Explanation:\n{result['explanation']}\n")
    print(f"Requested Difficulty: {result['requested_difficulty']}")
    print(f"Assessed Difficulty: {result['assessed_difficulty']}")
    print(f"Reasoning: {result['difficulty_reasoning']}\n")
    print(f"Follow-ups:\n{result['followup_questions']}\n")


def generate_specialized_questions():
    """Use specialized generators for different question types."""
    print("=" * 60)
    print("Specialized Question Generators")
    print("=" * 60)

    generator = CompleteInterviewGenerator()

    # Generate coding question
    print("\n--- CODING QUESTION ---")
    coding_result = generator(
        topic="graph algorithms - shortest path",
        question_type="coding",
        difficulty="medium",
        num_followups=2
    )
    print(f"\n{coding_result['question']}\n")
    print(f"Follow-ups:\n{coding_result['followup_questions']}\n")

    # Generate ML theoretical question
    print("\n--- ML THEORY QUESTION ---")
    ml_theory_result = generator(
        topic="bias-variance tradeoff",
        question_type="ml_theory",
        difficulty="medium",
        num_followups=2
    )
    print(f"\n{ml_theory_result['question']}\n")
    print(f"Follow-ups:\n{ml_theory_result['followup_questions']}\n")

    # Generate ML practical question
    print("\n--- ML PRACTICAL QUESTION ---")
    ml_practical_result = generator(
        topic="model evaluation and cross-validation",
        question_type="ml_practical",
        difficulty="hard",
        num_followups=2
    )
    print(f"\n{ml_practical_result['question']}\n")
    print(f"Follow-ups:\n{ml_practical_result['followup_questions']}\n")


def main():
    """Run advanced examples."""
    print("\n" + "=" * 60)
    print("DSPy Tech Interview Generator - Advanced Pipeline")
    print("=" * 60 + "\n")

    setup_dspy()

    generate_complete_interview_set()
    print("\n")

    generate_specialized_questions()

    print("\n" + "=" * 60)
    print("Pipeline examples completed!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
