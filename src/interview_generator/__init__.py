"""
Tech Interview Generator using DSPy
A framework for generating technical interview questions using DSPy's declarative approach
"""

from .signatures import (
    GenerateQuestion,
    GenerateFollowUp,
    AssessDifficulty
)
from .modules import (
    QuestionGenerator,
    FollowUpGenerator,
    InterviewPipeline
)

__all__ = [
    'GenerateQuestion',
    'GenerateFollowUp',
    'AssessDifficulty',
    'QuestionGenerator',
    'FollowUpGenerator',
    'InterviewPipeline'
]
