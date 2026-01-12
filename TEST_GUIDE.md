# Testing Guide

## Quick Test (After Getting API Key)

### 1. Add Your API Key to .env

```bash
# Open .env file
nano .env

# Or use any text editor
code .env
```

Add this line:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

### 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 3. Test Interactive Mode

```bash
python generate_question.py
```

**Expected Flow:**
```
==================================================
       TECH INTERVIEW QUESTION GENERATOR
==================================================

What type of question do you want?
1. Coding/Algorithms
2. ML Theory
3. ML Practical

Enter number: 1

What topic? (e.g., 'binary trees', 'neural networks', 'gradient descent')
Topic: binary trees

Difficulty level?
1. easy
2. medium
3. hard

Enter number: 2

How many follow-up questions?
1. 1
2. 2
3. 3
4. 4

Enter number: 3

==================================================
Generating question... (this may take a few seconds)
==================================================
```

### 4. Test Quick Mode

```bash
# Generate question on a specific topic
python generate_question.py "sorting algorithms"
```

### 5. Test Different Question Types

**Coding Question:**
```bash
python generate_question.py "dynamic programming"
```

**ML Theory:**
```bash
python generate_question.py "backpropagation"
```

**ML Practical:**
```bash
python generate_question.py "cross-validation"
```

## Troubleshooting

### Error: "OPENAI_API_KEY not found"
- Make sure .env file exists in project root
- Check that API key is properly formatted: `OPENAI_API_KEY=sk-...`
- No quotes needed around the key

### Error: "Module not found"
- Make sure virtual environment is activated: `source venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`

### Error: "Invalid API key"
- Check your API key at https://platform.openai.com/api-keys
- Make sure you copied it correctly (no extra spaces)

### Slow Response
- This is normal! GPT-4o-mini takes a few seconds to generate quality questions
- Typical wait time: 5-10 seconds

## What Success Looks Like

You should see output like this:

```
==================================================
GENERATED INTERVIEW QUESTION
==================================================

Topic: binary trees
Type: coding
Difficulty: medium

------------------------------------------------------------
[Detailed question with examples, constraints, etc.]
------------------------------------------------------------

FOLLOW-UP QUESTIONS:
1. [Follow-up 1]
2. [Follow-up 2]
3. [Follow-up 3]

==================================================
```

## Next Steps After Testing

- Try different topics
- Experiment with difficulty levels
- Generate multiple questions for interview prep
- Share with your team!
