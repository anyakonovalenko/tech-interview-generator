"""
Basic Usage Example: Getting Started with DSPy Interview Generator

This example demonstrates the fundamentals of using DSPy to generate
technical interview questions.
"""

import os
import dspy
from dotenv import load_dotenv
from interview_generator import QuestionGenerator, FollowUpGenerator

# Load environment variables
load_dotenv()

# Step 1: Configure DSPy with your LLM
# DSPy supports multiple LLM providers. Here we use OpenAI.
def setup_dspy():
    """Initialize DSPy with an LLM backend."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY in your .env file")

    # Configure DSPy to use GPT-4 (you can also use gpt-3.5-turbo for lower cost)
    lm = dspy.LM('openai/gpt-4o-mini', api_key=api_key)
    dspy.configure(lm=lm)
    print("✓ DSPy configured with OpenAI GPT-4o-mini\n")


def generate_simple_question():
    """Example 1: Generate a single interview question."""
    print("=" * 60)
    print("Example 1: Generating a Simple Question")
    print("=" * 60)

    # Create a question generator module
    generator = QuestionGenerator()

    # Generate a coding question
    result = generator(
        topic="binary search trees",
        question_type="coding",
        difficulty="medium"
    )

    print(f"\nQuestion:\n{result.question}\n")
    print(f"What it tests:\n{result.explanation}\n")


def generate_ml_question():
    """Example 2: Generate an ML-focused question."""
    print("=" * 60)
    print("Example 2: Generating an ML Question")
    print("=" * 60)

    generator = QuestionGenerator()

    result = generator(
        topic="backpropagation and gradient descent",
        question_type="ml_theory",
        difficulty="medium"
    )

    print(f"\nML Question:\n{result.question}\n")
    print(f"What it tests:\n{result.explanation}\n")


def generate_with_followups():
    """Example 3: Generate question with follow-ups."""
    print("=" * 60)
    print("Example 3: Question with Follow-ups")
    print("=" * 60)

    # Generate main question
    question_gen = QuestionGenerator()
    question_result = question_gen(
        topic="convolutional neural networks",
        question_type="ml_theory",
        difficulty="hard"
    )

    print(f"\nMain Question:\n{question_result.question}\n")

    # Generate follow-ups
    followup_gen = FollowUpGenerator()
    followup_result = followup_gen(
        original_question=question_result.question,
        topic="convolutional neural networks",
        num_followups=3
    )

    print(f"Follow-up Questions:\n{followup_result.followup_questions}\n")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("DSPy Tech Interview Generator - Basic Examples")
    print("=" * 60 + "\n")

    # Setup
    setup_dspy()

    # Run examples
    generate_simple_question()
    print("\n")

    generate_ml_question()
    print("\n")

    generate_with_followups()

    print("\n" + "=" * 60)
    print("Examples completed! Try modifying the topics and difficulty.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
