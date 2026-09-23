## GitHub — Fork, Push & Pull Request Guide

A quick guide for submitting your work to the official Solarpunk Corps repository.

**Example**

- Official repository: `SPC/Day-1`
- Team: `Team-01`
- Member: Bob
- GitHub account: Bob

---

## 1. Open the Official Repository

Open the repository provided by Solarpunk Corps.

```text
SPC/Day-1
├── README.md
├── starter-codes/
├── Team-01/
├── Team-02/
├── Team-03/
└── ...
```

**Do not edit the official repository directly.**

---

## 2. Fork the Repository

Click:

**Fork → Create fork**

Choose your own GitHub account.

You will now have:

```text
SPC/Day-1
    ↓
Bob/Day-1
```

Work on your **own fork**.

---

## 3. Clone Your Fork

Open your fork and select:

**Code → HTTPS**

Copy the URL and run:

```bash
git clone https://github.com/Bob/Day-1.git
cd Day-1
```

Open the folder in VS Code.

---

## 4. Work in Your Team Folder

If Bob is in Team-01:

```text
Team-01/
└── bob.py
```

If Alice is also in Team-01:

```text
Team-01/
├── alice.py
└── bob.py
```

**Work only inside your assigned team folder.**

Do not:

- Modify another team's folder.
- Delete another member's files.
- Modify `starter-codes/` unless instructed.
- Change the repository structure unnecessarily.

---

## 5. Write and Test Your Code

Example:

```python
print("Hello from Bob!")
```

Save and test your code before submitting.

---

# Git Commands

## Check Your Changes

```bash
git status
```

## Get Latest Changes

```bash
git pull
```

## Add Your Changes

```bash
git add .
```

## Commit

```bash
git commit -m "Add Bob's Team-01 work"
```

## Push

```bash
git push
```

Your changes will now appear on your GitHub fork.

---

## Complete Git Workflow

```text
git pull
    ↓
Make / edit files
    ↓
git status
    ↓
git add .
    ↓
git commit -m "Your message"
    ↓
git push
    ↓
Create Pull Request
```

### Remember

**`git pull`** → Get changes from GitHub  
**`git add .`** → Prepare your changes  
**`git commit`** → Save your changes locally  
**`git push`** → Upload your changes to GitHub  

---

## 6. Create a Pull Request

After pushing, open your fork on GitHub.

Click:

**Compare & pull request**

Make sure the Pull Request is:

```text
Bob/Day-1
    ↓
Pull Request
    ↓
SPC/Day-1
```

The **base repository must be the official Solarpunk Corps repository**.

---

## 7. Pull Request Title

Use a clear title:

```text
Team-01 — Bob's Submission
```

Example description:

```text
Team: Team-01
Member: Bob

Added my Python work for Day 1.
```

Click:

**Create pull request**

---

## 8. Review & Merge

The Solarpunk Corps maintainers will review your Pull Request.

If everything is correct, it will be merged into the official repository.

Final result:

```text
SPC/Day-1
│
├── Team-01/
│   ├── alice.py
│   └── bob.py
│
├── Team-02/
├── Team-03/
└── ...
```

---

## If a Teammate Has Already Submitted

Suppose Alice has already submitted:

```text
Team-01/alice.py
```

Bob can still submit:

```text
Team-01/bob.py
```

If the files are separate, they can normally be merged without a conflict.

---

## If GitHub Shows a Merge Conflict

**Do not delete files or force changes.**

Contact the club coordinator/maintainer or follow the additional Git instructions provided by the club.

---

# Quick Git Cheat Sheet

```bash
# Clone
git clone https://github.com/USERNAME/Day-1.git

# Enter repository
cd Day-1

# Check status
git status

# Pull latest changes
git pull

# Add changes
git add .

# Commit
git commit -m "Your message"

# Push
git push

# View commits
git log --oneline

# Check remote
git remote -v
```

### Important

**Pull Request is created on GitHub, not with a Git command.**

**Do not push directly to the official Solarpunk Corps repository.**

---

# The 3 Things to Remember

**1. Fork the official repository.**

**2. Work only inside your assigned team folder.**

**3. Push to your fork → Create a Pull Request → Wait for review and merge.**