"""
DSPy Signatures for Tech Interview Generation

Signatures in DSPy define the input/output behavior of LLM modules.
They're like type hints that declare what task we want to solve.
"""

import dspy


class GenerateQuestion(dspy.Signature):
    """Generate a technical interview question based on the topic and type."""

    topic: str = dspy.InputField(desc="The specific topic or technology (e.g., 'binary trees', 'neural networks')")
    question_type: str = dspy.InputField(desc="Type of question: 'coding' or 'ml_theory'")
    difficulty: str = dspy.InputField(desc="Difficulty level: 'easy', 'medium', or 'hard'")

    question: str = dspy.OutputField(desc="The generated interview question")
    explanation: str = dspy.OutputField(desc="Brief explanation of what this question tests")


class GenerateFollowUp(dspy.Signature):
    """Generate follow-up questions based on the original question."""

    original_question: str = dspy.InputField(desc="The original interview question")
    topic: str = dspy.InputField(desc="The topic area")
    num_followups: int = dspy.InputField(desc="Number of follow-up questions to generate")

    followup_questions: str = dspy.OutputField(desc="List of follow-up questions, numbered")


class AssessDifficulty(dspy.Signature):
    """Assess and validate the difficulty level of a question."""

    question: str = dspy.InputField(desc="The interview question to assess")
    topic: str = dspy.InputField(desc="The topic area")

    assessed_difficulty: str = dspy.OutputField(desc="Assessed difficulty: 'easy', 'medium', or 'hard'")
    reasoning: str = dspy.OutputField(desc="Explanation for the difficulty assessment")


class GenerateCodingQuestion(dspy.Signature):
    """Generate a coding/algorithm question with specific constraints."""

    topic: str = dspy.InputField(desc="Algorithm or data structure topic")
    difficulty: str = dspy.InputField(desc="Difficulty level: 'easy', 'medium', or 'hard'")

    question_title: str = dspy.OutputField(desc="Concise title for the coding problem")
    question_description: str = dspy.OutputField(desc="Detailed problem description")
    input_format: str = dspy.OutputField(desc="Description of input format")
    output_format: str = dspy.OutputField(desc="Description of expected output")
    constraints: str = dspy.OutputField(desc="Time/space complexity constraints")
    example: str = dspy.OutputField(desc="Example input/output")


class GenerateMLQuestion(dspy.Signature):
    """Generate a Machine Learning theory or practical question."""

    topic: str = dspy.InputField(desc="ML topic (e.g., 'gradient descent', 'CNN', 'overfitting')")
    difficulty: str = dspy.InputField(desc="Difficulty level: 'easy', 'medium', or 'hard'")
    question_style: str = dspy.InputField(desc="Style: 'theoretical', 'practical', or 'mixed'")

    question: str = dspy.OutputField(desc="The ML question")
    key_concepts: str = dspy.OutputField(desc="Key concepts being tested")
    expected_depth: str = dspy.OutputField(desc="Expected depth of answer for the difficulty level")
