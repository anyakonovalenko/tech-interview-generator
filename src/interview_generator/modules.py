"""
DSPy Modules for Tech Interview Generation

Modules in DSPy are composable building blocks that use signatures
and prompting techniques to solve tasks.
"""

import dspy
from typing import List, Dict
from .signatures import (
    GenerateQuestion,
    GenerateFollowUp,
    AssessDifficulty,
    GenerateCodingQuestion,
    GenerateMLQuestion
)


class QuestionGenerator(dspy.Module):
    """
    Generates technical interview questions using DSPy's ChainOfThought.

    This demonstrates DSPy's core concept: instead of writing prompts,
    we declare signatures and let DSPy optimize the prompting strategy.
    """

    def __init__(self):
        super().__init__()
        # ChainOfThought makes the LLM explain its reasoning before answering
        self.generate = dspy.ChainOfThought(GenerateQuestion)

    def forward(self, topic: str, question_type: str, difficulty: str):
        """Generate a question with the given parameters."""
        result = self.generate(
            topic=topic,
            question_type=question_type,
            difficulty=difficulty
        )
        return result


class CodingQuestionGenerator(dspy.Module):
    """Specialized generator for coding/algorithm questions."""

    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(GenerateCodingQuestion)

    def forward(self, topic: str, difficulty: str):
        """Generate a structured coding question."""
        result = self.generate(topic=topic, difficulty=difficulty)
        return result


class MLQuestionGenerator(dspy.Module):
    """Specialized generator for ML scientist interview questions."""

    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(GenerateMLQuestion)

    def forward(self, topic: str, difficulty: str, question_style: str = "mixed"):
        """Generate an ML question."""
        result = self.generate(
            topic=topic,
            difficulty=difficulty,
            question_style=question_style
        )
        return result


class FollowUpGenerator(dspy.Module):
    """Generates relevant follow-up questions."""

    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(GenerateFollowUp)

    def forward(self, original_question: str, topic: str, num_followups: int = 3):
        """Generate follow-up questions."""
        result = self.generate(
            original_question=original_question,
            topic=topic,
            num_followups=num_followups
        )
        return result


class InterviewPipeline(dspy.Module):
    """
    Complete pipeline that generates a question and follow-ups.

    This demonstrates DSPy's composability: we can chain multiple
    modules together to create complex workflows.
    """

    def __init__(self):
        super().__init__()
        self.question_gen = QuestionGenerator()
        self.followup_gen = FollowUpGenerator()
        self.difficulty_assessor = dspy.ChainOfThought(AssessDifficulty)

    def forward(self, topic: str, question_type: str, difficulty: str, num_followups: int = 3):
        """
        Generate a complete interview question set.

        Returns:
            dict with 'question', 'explanation', 'followups', and 'difficulty_check'
        """
        # Generate main question
        question_result = self.question_gen(
            topic=topic,
            question_type=question_type,
            difficulty=difficulty
        )

        # Generate follow-ups
        followup_result = self.followup_gen(
            original_question=question_result.question,
            topic=topic,
            num_followups=num_followups
        )

        # Assess difficulty to validate our generation
        difficulty_result = self.difficulty_assessor(
            question=question_result.question,
            topic=topic
        )

        return {
            'question': question_result.question,
            'explanation': question_result.explanation,
            'requested_difficulty': difficulty,
            'assessed_difficulty': difficulty_result.assessed_difficulty,
            'difficulty_reasoning': difficulty_result.reasoning,
            'followup_questions': followup_result.followup_questions
        }


class CompleteInterviewGenerator(dspy.Module):
    """
    Advanced pipeline that can generate different types of questions
    with specialized generators.
    """

    def __init__(self):
        super().__init__()
        self.coding_gen = CodingQuestionGenerator()
        self.ml_gen = MLQuestionGenerator()
        self.followup_gen = FollowUpGenerator()

    def forward(self, topic: str, question_type: str, difficulty: str, num_followups: int = 3):
        """Generate appropriate question based on type."""

        if question_type == "coding":
            result = self.coding_gen(topic=topic, difficulty=difficulty)
            main_question = f"{result.question_title}\n\n{result.question_description}\n\nInput: {result.input_format}\nOutput: {result.output_format}\n\nConstraints: {result.constraints}\n\nExample:\n{result.example}"

        elif question_type == "ml_theory":
            ml_result = self.ml_gen(topic=topic, difficulty=difficulty, question_style="theoretical")
            main_question = ml_result.question
            result = ml_result

        elif question_type == "ml_practical":
            ml_result = self.ml_gen(topic=topic, difficulty=difficulty, question_style="practical")
            main_question = ml_result.question
            result = ml_result

        else:
            raise ValueError(f"Unknown question type: {question_type}")

        # Generate follow-ups
        followup_result = self.followup_gen(
            original_question=main_question,
            topic=topic,
            num_followups=num_followups
        )

        return {
            'question': main_question,
            'details': result,
            'difficulty': difficulty,
            'followup_questions': followup_result.followup_questions
        }
