"""
Understanding DSPy: Core Concepts Explained

This file demonstrates DSPy's key concepts through practical examples.
Use this to understand HOW DSPy works, not just what it does.
"""

import os
import dspy
from dotenv import load_dotenv

load_dotenv()


def concept_1_signatures():
    """
    Concept 1: SIGNATURES

    In DSPy, a Signature is a declarative specification of what you want
    the LLM to do. It's like a function signature but for LLM tasks.

    Instead of writing: "Given a topic, generate a question..."
    You declare: topic -> question
    """
    print("=" * 60)
    print("CONCEPT 1: Signatures (Declarative Task Definition)")
    print("=" * 60)

    # Define a simple signature
    class SimpleQuestionGen(dspy.Signature):
        """Generate a technical question."""
        topic: str = dspy.InputField()
        question: str = dspy.OutputField()

    print("\nSignature defined:")
    print("  Input: topic (string)")
    print("  Output: question (string)")
    print("  Task: Generate a technical question")

    # Use it with ChainOfThought
    generator = dspy.ChainOfThought(SimpleQuestionGen)

    api_key = os.getenv("OPENAI_API_KEY")
    lm = dspy.LM('openai/gpt-4o-mini', api_key=api_key)
    dspy.configure(lm=lm)

    result = generator(topic="recursion")
    print(f"\nGenerated: {result.question}")
    print("\nKey Insight: We didn't write any prompts! DSPy generates them.")


def concept_2_modules():
    """
    Concept 2: MODULES

    Modules are reusable components that combine signatures with
    prompting strategies (ChainOfThought, ReAct, etc.)
    """
    print("\n" + "=" * 60)
    print("CONCEPT 2: Modules (Reusable Components)")
    print("=" * 60)

    class QuestionSignature(dspy.Signature):
        """Generate a question with difficulty."""
        topic: str = dspy.InputField()
        difficulty: str = dspy.InputField()
        question: str = dspy.OutputField()

    # Create a module that encapsulates logic
    class QuestionModule(dspy.Module):
        def __init__(self):
            super().__init__()
            # ChainOfThought makes the model reason before answering
            self.generate = dspy.ChainOfThought(QuestionSignature)

        def forward(self, topic, difficulty="medium"):
            return self.generate(topic=topic, difficulty=difficulty)

    api_key = os.getenv("OPENAI_API_KEY")
    lm = dspy.LM('openai/gpt-4o-mini', api_key=api_key)
    dspy.configure(lm=lm)

    module = QuestionModule()
    result = module(topic="hash tables", difficulty="easy")

    print(f"\nGenerated: {result.question}")
    print("\nKey Insight: Modules are composable and reusable building blocks.")


def concept_3_composition():
    """
    Concept 3: COMPOSITION

    DSPy's power comes from composing modules into pipelines.
    Each module can call other modules.
    """
    print("\n" + "=" * 60)
    print("CONCEPT 3: Composition (Building Pipelines)")
    print("=" * 60)

    # Define signatures
    class GenQuestion(dspy.Signature):
        """Generate a question."""
        topic: str = dspy.InputField()
        question: str = dspy.OutputField()

    class AssessQuality(dspy.Signature):
        """Assess if question is good."""
        question: str = dspy.InputField()
        is_good: str = dspy.OutputField(desc="'yes' or 'no'")
        reason: str = dspy.OutputField()

    # Compose them into a pipeline
    class QualityCheckedGenerator(dspy.Module):
        def __init__(self):
            super().__init__()
            self.generate = dspy.ChainOfThought(GenQuestion)
            self.assess = dspy.ChainOfThought(AssessQuality)

        def forward(self, topic):
            # Generate question
            result = self.generate(topic=topic)

            # Check quality
            quality = self.assess(question=result.question)

            return {
                'question': result.question,
                'quality_check': quality.is_good,
                'reason': quality.reason
            }

    api_key = os.getenv("OPENAI_API_KEY")
    lm = dspy.LM('openai/gpt-4o-mini', api_key=api_key)
    dspy.configure(lm=lm)

    pipeline = QualityCheckedGenerator()
    result = pipeline(topic="sorting algorithms")

    print(f"\nQuestion: {result['question']}")
    print(f"Quality Check: {result['quality_check']}")
    print(f"Reason: {result['reason']}")
    print("\nKey Insight: Complex workflows emerge from simple compositions.")


def concept_4_no_prompts():
    """
    Concept 4: PROGRAMMING, NOT PROMPTING

    Traditional approach: Write and tune prompts manually
    DSPy approach: Declare what you want, let DSPy handle the prompting
    """
    print("\n" + "=" * 60)
    print("CONCEPT 4: Programming, NOT Prompting")
    print("=" * 60)

    print("\nTraditional Approach (Manual Prompting):")
    print("  prompt = '''You are an expert interviewer.")
    print("  Generate a {difficulty} question about {topic}.")
    print("  Make it practical and relevant...'''")
    print("  response = llm(prompt.format(...))")
    print("\n  Problems:")
    print("  - Fragile: small changes break it")
    print("  - Hard to optimize")
    print("  - Doesn't compose well")

    print("\n\nDSPy Approach (Declarative):")
    print("  class GenQ(dspy.Signature):")
    print("    topic: str = dspy.InputField()")
    print("    difficulty: str = dspy.InputField()")
    print("    question: str = dspy.OutputField()")
    print("\n  generator = dspy.ChainOfThought(GenQ)")
    print("  result = generator(topic='...', difficulty='...')")
    print("\n  Benefits:")
    print("  - Robust: DSPy optimizes prompts automatically")
    print("  - Composable: modules chain together")
    print("  - Portable: works across different LLMs")

    print("\nKey Insight: DSPy treats LLMs as first-class programming constructs.")


def main():
    """Run all concept demonstrations."""
    print("\n" + "=" * 60)
    print("Understanding DSPy: Core Concepts")
    print("=" * 60 + "\n")

    concept_1_signatures()
    concept_2_modules()
    concept_3_composition()
    concept_4_no_prompts()

    print("\n" + "=" * 60)
    print("Concepts completed! You now understand DSPy fundamentals.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
