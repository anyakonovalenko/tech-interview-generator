# Tech Interview Generator with DSPy

An open-source project to learn and understand **DSPy** (Declarative Self-improving Python) by building a practical technical interview question generator.

## What is DSPy?

DSPy is a framework for **programming** language models, not **prompting** them. Instead of manually writing and tuning prompts, you declare what you want using signatures, and DSPy automatically optimizes the prompts and LLM interactions.

Key concepts:
- **Signatures**: Declarative specifications of input/output behavior (like type hints for LLM tasks)
- **Modules**: Reusable components that combine signatures with prompting strategies
- **Composition**: Build complex pipelines by chaining simple modules together
- **Optimization**: DSPy can automatically tune prompts and weights for better performance

## Project Goals

This project serves two purposes:
1. **Learn DSPy** through hands-on implementation
2. **Build a useful tool** for generating technical interview questions

## Features

Generate technical interview questions for:
- Coding problems (algorithms & data structures)
- ML scientist positions (theory & practical)
- Multiple difficulty levels (easy, medium, hard)
- Automatic follow-up question generation
- Difficulty validation and assessment

## Project Structure

```
tech-interview-generator/
├── src/
│   └── interview_generator/
│       ├── __init__.py          # Main exports
│       ├── signatures.py        # DSPy signatures (task declarations)
│       └── modules.py           # DSPy modules (reusable components)
├── examples/
│   ├── basic_usage.py           # Start here: simple examples
│   ├── advanced_pipeline.py    # Complete interview pipelines
│   └── understanding_dspy.py   # Learn DSPy concepts
├── requirements.txt
├── .env.example
└── README.md
```

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/anyakonovalenko/tech-interview-generator.git
cd tech-interview-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your_key_here
```

### 3. Run Examples

```bash
# Start with basic examples
python examples/basic_usage.py

# Learn DSPy concepts
python examples/understanding_dspy.py

# Try advanced pipelines
python examples/advanced_pipeline.py
```

## Usage Examples

### Basic Question Generation

```python
import dspy
from interview_generator import QuestionGenerator

# Configure DSPy
lm = dspy.LM('openai/gpt-4o-mini', api_key='your-key')
dspy.configure(lm=lm)

# Generate a question
generator = QuestionGenerator()
result = generator(
    topic="binary search trees",
    question_type="coding",
    difficulty="medium"
)

print(result.question)
```

### Complete Interview Pipeline

```python
from interview_generator import InterviewPipeline

pipeline = InterviewPipeline()
result = pipeline(
    topic="neural networks",
    question_type="ml_theory",
    difficulty="hard",
    num_followups=3
)

print(f"Question: {result['question']}")
print(f"Follow-ups: {result['followup_questions']}")
```

## Understanding DSPy Through This Project

### 1. Signatures (signatures.py)

Signatures declare what you want the LLM to do:

```python
class GenerateQuestion(dspy.Signature):
    """Generate a technical interview question."""
    topic: str = dspy.InputField(desc="The topic")
    difficulty: str = dspy.InputField(desc="easy/medium/hard")
    question: str = dspy.OutputField(desc="The generated question")
```

### 2. Modules (modules.py)

Modules combine signatures with prompting techniques:

```python
class QuestionGenerator(dspy.Module):
    def __init__(self):
        super().__init__()
        # ChainOfThought makes the model reason first
        self.generate = dspy.ChainOfThought(GenerateQuestion)

    def forward(self, topic, question_type, difficulty):
        return self.generate(topic=topic, ...)
```

### 3. Composition

Build complex workflows by chaining modules:

```python
class InterviewPipeline(dspy.Module):
    def __init__(self):
        self.question_gen = QuestionGenerator()
        self.followup_gen = FollowUpGenerator()

    def forward(self, ...):
        question = self.question_gen(...)
        followups = self.followup_gen(question, ...)
        return {'question': question, 'followups': followups}
```

## Learn More About DSPy

- [Official DSPy Documentation](https://dspy.ai/)
- [DSPy GitHub Repository](https://github.com/stanfordnlp/dspy)
- [DSPy Learning Resources](https://dspy.ai/learn/)

## Contributing

This is a learning project! Contributions are welcome:
- Add new question types
- Improve existing modules
- Add optimization examples
- Enhance documentation

## License

MIT License - feel free to use this project for learning and building your own tools.

## Acknowledgments

- Built with [DSPy](https://github.com/stanfordnlp/dspy) by Stanford NLP
- Inspired by the need for better technical interview preparation tools
