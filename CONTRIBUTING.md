# 🤝 Contributing to ML Switzerland

Welcome! This guide explains how to contribute code and how the automated review system helps you learn.

---

## 🔄 Pull Request Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

**Naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation
- `experiment/` - Learning experiments

### 2. Make Changes
- Follow TODO comments in source files
- Write tests for new code
- Add docstrings to all functions
- Use type hints

### 3. Commit Changes
```bash
git add .
git commit -m "feat: implement data loader for accident data"
```

**Commit message format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance

### 4. Push & Create PR
```bash
git push origin feature/your-feature-name
```

Then create PR on GitHub.

---

## 🧠 Automated PR Review

**Every PR automatically gets reviewed!** No action needed from you.

### What the Bot Checks:

#### ✅ Positive Feedback
- Error handling implemented
- Type hints present
- Good comments
- Tests included

#### 💡 Learning Suggestions
- Missing type hints
- Missing docstrings
- TODO tracking
- Code smells (long functions, magic numbers)
- Security issues

#### 🎨 Style Issues
- PEP 8 violations
- Line length
- Import order
- Naming conventions

#### 🔍 Type Issues
- Missing type annotations
- Type mismatches
- Return type issues

### Example Review Output:

```markdown
# 🧠 Automated PR Review - ML Switzerland

**Files Changed:** 2

---
## 📄 `src/data/data_loader.py`

🎉 Great Job:
   ✅ Error handling implemented
   ✅ Type hints present
   ✅ Code is commented

💡 Suggestions for Improvement
🎯 Type Hints Missing:
   - Add return type to: load_csv (line 23)
   - Add return type to: load_accident_data (line 45)

💡 Learning: Type hints help catch bugs early!
   Resource: https://realpython.com/python-type-checking/

📝 Found 3 TODO(s):
   - Line 12: TODO: Set self.base_dir = base_dir or Path('.')
   - Line 25: TODO: Build full path
   - Line 30: TODO: Handle FileNotFoundError

💡 Tip: Track TODO progress in docs/weekly_progress.md

---
## 📊 Summary

- **Style Issues:** 5
- **Suggestions:** 8

### 📚 Helpful Resources
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Python Type Checking](https://realpython.com/python-type-checking/)

---
*This review is automated to help you learn! Feel free to ask questions.*
```

---

## 📋 PR Checklist

Before creating PR, check:

- [ ] Code follows TODO comments
- [ ] Type hints added to functions
- [ ] Docstrings written for all functions
- [ ] Tests created/updated
- [ ] No hardcoded credentials
- [ ] Commit message follows format
- [ ] Branch name is descriptive

---

## 🎓 Learning Focus

This project is about **learning**, not perfection!

### What Matters:
1. **Understanding** - Can you explain your code?
2. **Progress** - Are you improving each PR?
3. **Questions** - Ask when stuck!
4. **Documentation** - Write learnings in comments

### What Doesn't Matter:
- Perfect code on first try
- Following every suggestion immediately
- Speed of progress

---

## 🤖 Bot Commands (Future)

Comment on PR to trigger bot actions:

- `@bot review` - Re-run review
- `@bot explain <line>` - Explain specific code
- `@bot suggest` - Get improvement suggestions
- `@bot resources <topic>` - Get learning resources

---

## 📞 Getting Help

If review suggestions are unclear:

1. **Ask in PR comments** - I'll respond with explanations
2. **Check learning resources** - See `docs/learning_resources.md`
3. **Review examples** - Look at completed code in repo
4. **Weekly check-in** - Update `docs/weekly_progress.md`

---

## 🎯 Review Labels

PRs get auto-labeled:

- `📚 learning` - Active learning PR
- `🔍 needs-review` - Awaiting human review
- `✅ approved` - Ready to merge
- `🐛 has-issues` - Needs fixes before merge

---

## 🚀 Merge Criteria

PRs are merged when:

1. ✅ Automated review completed
2. ✅ Critical issues fixed
3. ✅ Tests passing
4. ✅ Learning goal achieved

**Note:** Code doesn't need to be perfect, just show learning progress!

---

## 📈 Progress Tracking

After each PR:

1. Update `docs/weekly_progress.md`
2. Note what you learned
3. Track challenges overcome
4. Plan next steps

---

**Remember:** Every PR is a learning opportunity. The bot is here to help, not criticize! 🎉

*Last Updated: 2026-03-28*
