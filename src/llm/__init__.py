"""LLM module for task parsing."""

from .openai import parse_task_with_llm, TaskParseResult

__all__ = ["parse_task_with_llm", "TaskParseResult"]
