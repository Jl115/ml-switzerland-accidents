#!/usr/bin/env python3
"""
🧠 ML Switzerland - Automated PR Review Bot

This bot reviews your code and provides educational feedback.
It's designed to help you learn, not to criticize!

Features:
- Code style checks (PEP 8)
- Type hint validation
- TODO detection
- Learning suggestions
- Best practices guidance
- Security checks
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple
import subprocess


# =============================================================================
# Code Analysis Functions
# =============================================================================

def run_linter(filepath: str) -> List[str]:
    """
    Run flake8 linter on file.
    
    Returns list of style issues found.
    """
    try:
        result = subprocess.run(
            ['flake8', '--max-line-length=100', '--extend-ignore=E203,W503', filepath],
            capture_output=True,
            text=True
        )
        return result.stdout.split('\n') if result.stdout else []
    except FileNotFoundError:
        return ["⚠️  flake8 not installed. Run: pip install flake8"]


def run_type_checker(filepath: str) -> List[str]:
    """
    Run mypy type checker on file.
    
    Returns list of type issues found.
    """
    try:
        result = subprocess.run(
            ['mypy', '--ignore-missing-imports', filepath],
            capture_output=True,
            text=True
        )
        return result.stdout.split('\n') if result.stdout else []
    except FileNotFoundError:
        return ["⚠️  mypy not installed. Run: pip install mypy"]


def check_todo_comments(filepath: str, content: str) -> List[str]:
    """
    Check for TODO comments and their status.
    
    Returns suggestions about TODOs.
    """
    todos = []
    for i, line in enumerate(content.split('\n'), 1):
        if 'TODO' in line:
            todos.append(f"Line {i}: {line.strip()}")
    
    suggestions = []
    if todos:
        suggestions.append(f"📝 Found {len(todos)} TODO(s):")
        for todo in todos[:5]:  # Show first 5
            suggestions.append(f"   - {todo}")
        
        if len(todos) > 5:
            suggestions.append(f"   ... and {len(todos) - 5} more")
        
        suggestions.append("\n💡 Tip: Track TODO progress in docs/weekly_progress.md")
    
    return suggestions


def check_type_hints(filepath: str, content: str) -> List[str]:
    """
    Check if functions have type hints.
    
    Returns suggestions about type hinting.
    """
    suggestions = []
    
    # Find function definitions
    func_pattern = r'def\s+(\w+)\s*\([^)]*\)\s*(?:->\s*[\w\[\],\s]+)?\s*:'
    functions = re.finditer(func_pattern, content)
    
    missing_hints = []
    for match in functions:
        func_name = match.group(1)
        line = content[:match.start()].count('\n') + 1
        func_line = content.split('\n')[line - 1]
        
        # Check if function has return type hint
        if '->' not in func_line:
            missing_hints.append(f"{func_name} (line {line})")
    
    if missing_hints:
        suggestions.append("🎯 Type Hints Missing:")
        for func in missing_hints[:5]:
            suggestions.append(f"   - Add return type to: {func}")
        suggestions.append("\n💡 Learning: Type hints help catch bugs early!")
        suggestions.append("   Resource: https://realpython.com/python-type-checking/")
    
    return suggestions


def check_docstrings(filepath: str, content: str) -> List[str]:
    """
    Check if functions have docstrings.
    
    Returns suggestions about documentation.
    """
    suggestions = []
    
    # Simple check: look for def followed by """ within next few lines
    lines = content.split('\n')
    missing_docstrings = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('def ') and not line.strip().startswith('class '):
            # Check next 3 lines for docstring
            has_docstring = False
            for j in range(i+1, min(i+4, len(lines))):
                if '"""' in lines[j] or "'''" in lines[j]:
                    has_docstring = True
                    break
            
            if not has_docstring:
                missing_docstrings.append(f"{line.strip()} (line {i+1})")
    
    if missing_docstrings:
        suggestions.append("📖 Docstrings Missing:")
        for func in missing_docstrings[:5]:
            suggestions.append(f"   - Add docstring to: {func}")
        suggestions.append("\n💡 Learning: Good docstrings explain 'why', not just 'what'")
        suggestions.append("   Example: See src/models/base_model.py for template")
    
    return suggestions


def check_learning_patterns(filepath: str, content: str) -> List[str]:
    """
    Check for good learning practices.
    
    Returns positive feedback and suggestions.
    """
    suggestions = []
    
    # Positive checks
    has_error_handling = 'try:' in content and 'except' in content
    has_type_hints = '->' in content or ': str' in content or ': int' in content
    has_comments = content.count('#') > 5
    has_tests = 'test_' in filepath.lower() or 'assert' in content
    
    positives = []
    if has_error_handling:
        positives.append("✅ Error handling implemented")
    if has_type_hints:
        positives.append("✅ Type hints present")
    if has_comments:
        positives.append("✅ Code is commented")
    if has_tests:
        positives.append("✅ Tests included")
    
    if positives:
        suggestions.append("🎉 Great Job:")
        suggestions.extend([f"   {p}" for p in positives])
    
    return suggestions


def check_code_smells(filepath: str, content: str) -> List[str]:
    """
    Check for common code smells and anti-patterns.
    
    Returns suggestions for improvement.
    """
    suggestions = []
    
    # Check for long functions (>50 lines)
    lines = content.split('\n')
    in_function = False
    function_start = 0
    function_name = ""
    
    for i, line in enumerate(lines):
        if line.strip().startswith('def '):
            if in_function and (i - function_start) > 50:
                suggestions.append(f"⚠️  Function '{function_name}' is {i - function_start} lines")
                suggestions.append("   💡 Consider breaking into smaller functions")
            in_function = True
            function_start = i
            function_name = line.split('def ')[1].split('(')[0]
    
    # Check for magic numbers
    magic_numbers = re.findall(r'(?<!\w)(\d{2,})(?!\w)', content)
    if len(magic_numbers) > 3:
        suggestions.append(f"⚠️  Found {len(magic_numbers)} magic numbers")
        suggestions.append("   💡 Define as named constants at top of file")
    
    # Check for repeated code patterns
    if content.count('\n    ') > content.count('\n        '):
        # Lots of single indentation, might be copy-paste
        pass  # Could add more sophisticated check
    
    return suggestions


def check_security_issues(filepath: str, content: str) -> List[str]:
    """
    Check for common security issues.
    
    Returns security warnings.
    """
    suggestions = []
    
    # Check for hardcoded credentials
    if 'password' in content.lower() and '=' in content:
        if 'os.environ' not in content and 'getenv' not in content:
            suggestions.append("🔒 Security: Avoid hardcoded passwords")
            suggestions.append("   💡 Use environment variables: os.environ.get('PASSWORD')")
    
    # Check for eval/exec usage
    if 'eval(' in content or 'exec(' in content:
        suggestions.append("🔒 Security: eval/exec can be dangerous")
        suggestions.append("   💡 Find safer alternatives when possible")
    
    return suggestions


# =============================================================================
# Review Generation
# =============================================================================

def generate_review(changed_files: List[str]) -> str:
    """
    Generate comprehensive PR review comment.
    
    Args:
        changed_files: List of file paths that changed
        
    Returns:
        Formatted review comment
    """
    review = []
    review.append("# 🧠 Automated PR Review - ML Switzerland")
    review.append("")
    review.append(f"**Files Changed:** {len(changed_files)}")
    review.append("")
    
    total_issues = 0
    total_suggestions = 0
    
    for filepath in changed_files:
        if not filepath.endswith('.py'):
            continue
        
        review.append(f"---")
        review.append(f"## 📄 `{filepath}`")
        review.append("")
        
        # Read file content
        try:
            with open(filepath, 'r') as f:
                content = f.read()
        except Exception as e:
            review.append(f"❌ Could not read file: {e}")
            continue
        
        # Run checks
        linter_issues = run_linter(filepath)
        type_issues = run_type_checker(filepath)
        todo_suggestions = check_todo_comments(filepath, content)
        type_hint_suggestions = check_type_hints(filepath, content)
        docstring_suggestions = check_docstrings(filepath, content)
        learning_feedback = check_learning_patterns(filepath, content)
        code_smells = check_code_smells(filepath, content)
        security_issues = check_security_issues(filepath, content)
        
        # Add positive feedback first
        if learning_feedback:
            review.extend(learning_feedback)
            review.append("")
        
        # Add suggestions
        all_suggestions = (
            type_hint_suggestions + 
            docstring_suggestions + 
            todo_suggestions + 
            code_smells +
            security_issues
        )
        
        if all_suggestions:
            review.append("### 💡 Suggestions for Improvement")
            review.extend(all_suggestions)
            review.append("")
            total_suggestions += len(all_suggestions)
        
        # Add linter issues
        if linter_issues and linter_issues[0]:
            review.append("### 🎨 Style Issues (flake8)")
            review.extend(linter_issues[:10])  # Show first 10
            review.append("")
            total_issues += len(linter_issues)
        
        # Add type checker issues
        if type_issues and type_issues[0]:
            review.append("### 🔍 Type Issues (mypy)")
            review.extend(type_issues[:10])  # Show first 10
            review.append("")
            total_issues += len(type_issues)
    
    # Add summary
    review.append("---")
    review.append("## 📊 Summary")
    review.append("")
    review.append(f"- **Style Issues:** {total_issues}")
    review.append(f"- **Suggestions:** {total_suggestions}")
    review.append("")
    
    # Add learning resources
    if total_suggestions > 0:
        review.append("### 📚 Helpful Resources")
        review.append("- [Python Style Guide (PEP 8)](https://pep8.org/)")
        review.append("- [Python Type Checking](https://realpython.com/python-type-checking/)")
        review.append("- [Writing Good Docstrings](https://www.python.org/dev/peps/pep-0257/)")
        review.append("")
    
    review.append("---")
    review.append("*This review is automated to help you learn! Feel free to ask questions in the PR comments.*")
    review.append("")
    review.append("**Remember:** The goal is learning, not perfection! 🚀")
    
    return '\n'.join(review)


# =============================================================================
# Main
# =============================================================================

def main():
    """Main entry point for PR review bot."""
    # Get changed files from environment
    changed_files_str = os.environ.get('CHANGED_FILES', '')
    changed_files = changed_files_str.split() if changed_files_str else []
    
    if not changed_files:
        print("No Python files changed")
        return
    
    print(f"Reviewing {len(changed_files)} file(s)...")
    
    # Generate review
    review = generate_review(changed_files)
    
    # Print review (will be captured by GitHub Actions)
    print(review)
    
    # Save review to file for GitHub Actions to use
    with open('/tmp/pr_review.md', 'w') as f:
        f.write(review)
    
    # Post review as comment (using GitHub CLI)
    github_token = os.environ.get('GITHUB_TOKEN', '')
    pr_number = os.environ.get('PR_NUMBER', '')
    
    if github_token and pr_number:
        try:
            subprocess.run([
                'gh', 'api',
                f'/repos/{os.environ.get("GITHUB_REPOSITORY")}/issues/{pr_number}/comments',
                '-X', 'POST',
                '-H', f'Authorization: token {github_token}',
                '-F', f'body=@/tmp/pr_review.md'
            ], check=True)
            print(f"\n✅ Review posted to PR #{pr_number}")
        except Exception as e:
            print(f"\n⚠️  Could not post review: {e}")


if __name__ == '__main__':
    main()
