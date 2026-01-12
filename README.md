# Tech Interview Generator

[![Built with DSPy](https://img.shields.io/badge/built%20with-DSPy-blue)](https://github.com/stanfordnlp/dspy)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Generate high-quality technical interview questions instantly using AI. Perfect for hiring managers, interviewers, and anyone preparing for technical interviews.

Built with [DSPy](https://github.com/stanfordnlp/dspy) - a framework for programming (not prompting) language models.

## Quick Start (2 minutes)

```bash
# 1. Clone and setup
git clone https://github.com/anyakonovalenko/tech-interview-generator.git
cd tech-interview-generator
bash setup.sh

# 2. Add your OpenAI API key to .env file
# Get one at: https://platform.openai.com/api-keys

# 3. Generate questions!
python generate_question.py
```

## Usage

### Interactive Mode (Easiest)

```bash
python generate_question.py
```

Follow the prompts to select:
- Question type (Coding, ML Theory, ML Practical)
- Topic (e.g., "binary trees", "neural networks")
- Difficulty (easy, medium, hard)
- Number of follow-up questions

### Quick Mode

```bash
# Generate question on a specific topic
python generate_question.py "dynamic programming"
python generate_question.py "convolutional neural networks"
python generate_question.py "graph algorithms"
```

## Features

- **Multiple Question Types**: Coding/algorithms, ML theory, ML practical
- **Smart Difficulty Levels**: Easy, medium, hard with automatic validation
- **Follow-up Questions**: Get 1-4 related follow-ups automatically
- **Instant Generation**: Powered by GPT-4o-mini for fast results
- **No Prompt Engineering**: Built with DSPy for robust, reliable outputs

## Example Output

```
==================================================
       TECH INTERVIEW QUESTION GENERATOR
==================================================

Topic: binary search trees
Type: coding
Difficulty: medium

------------------------------------------------------------
Design and implement a function to find the kth smallest
element in a Binary Search Tree (BST).

Input: Root node of BST and integer k
Output: The kth smallest element

Example:
    BST:     5
           /   \
          3     7
         / \   / \
        2   4 6   8

    k = 3 → Output: 4

Constraints:
- Time complexity should be O(k) on average
- Space complexity should be O(h) where h is tree height
------------------------------------------------------------

FOLLOW-UP QUESTIONS:
1. How would you modify your solution to handle frequent
   queries for different k values on the same BST?
2. What changes are needed if the BST is modified frequently
   with insertions and deletions?
3. Can you solve this without using extra space?
```

## Use Cases

- **Hiring Managers**: Generate diverse questions for technical interviews
- **Interview Prep**: Practice with realistic interview questions
- **Educators**: Create assignments and exam questions
- **Self-Study**: Test your knowledge on specific topics

## For Developers: Learning DSPy

This project is built with [DSPy](https://dspy.ai/), a framework for programming (not prompting) language models. If you want to understand or extend the code:

**Project Structure:**
```
tech-interview-generator/
├── generate_question.py     # Main CLI tool (start here!)
├── setup.sh                 # Quick setup script
├── src/interview_generator/
│   ├── signatures.py        # DSPy task declarations
│   └── modules.py           # Question generation logic
└── examples/                # Learning examples
    ├── basic_usage.py
    ├── advanced_pipeline.py
    └── understanding_dspy.py
```

**Run the examples to learn DSPy:**
```bash
python examples/understanding_dspy.py  # Learn DSPy concepts
python examples/basic_usage.py         # Simple usage
python examples/advanced_pipeline.py   # Advanced patterns
```

**Resources:**
- [DSPy Documentation](https://dspy.ai/)
- [DSPy GitHub](https://github.com/stanfordnlp/dspy)
- [Why DSPy?](https://dspy.ai/learn/) - No more prompt engineering!

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
