# Git & GitHub Cheatsheet
> Built command-by-command as I learn. Each section = one lesson.

---

## LESSON 1 — Setting Up Git

### `git config`
Configure your identity (done once per machine).

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list                        # view all config values
git config --global core.editor "code --wait"  # set VS Code as default editor
```

**Why it matters:** Every commit is stamped with this name + email. Without it, Git won't let you commit.

---

## LESSON 2 — Creating a Repository

### `git init`
Turn any folder into a Git repository.

```bash
git init                    # init in current folder
git init my-project         # create + init a new folder
```

**What it does:** Creates a hidden `.git/` folder that tracks everything. Don't delete it.

---

## LESSON 3 — Checking Status

### `git status`
See what's going on in your working directory.

```bash
git status                  # full status
git status -s               # short/compact view
```

**Output colors:**
- Red = untracked or modified (not staged)
- Green = staged (ready to commit)

---

## LESSON 4 — Staging Changes

### `git add`
Move changes from your working directory → staging area (the "draft" before committing).

```bash
git add filename.txt        # stage one file
git add .                   # stage everything in current folder
git add *.js                # stage all .js files
git add -p                  # interactively choose what to stage (patch mode)
```

**Mental model:** Think of staging like packing a box before shipping. `git add` puts things in the box. `git commit` ships it.

---

## LESSON 5 — Committing

### `git commit`
Save a snapshot of everything in the staging area.

```bash
git commit -m "your message here"      # commit with inline message
git commit                             # opens editor for longer message
git commit -am "message"               # stage tracked files + commit in one step
```

**Good commit message format:**
```
Short summary (max 72 chars)

Optional longer explanation of WHY this change was made,
not just what was changed.
```

---

## LESSON 6 — Viewing History

### `git log`
Browse the commit history.

```bash
git log                         # full log
git log --oneline               # one line per commit
git log --oneline --graph       # visual branch tree
git log --oneline -5            # last 5 commits
git log --author="Name"         # filter by author
git log -- filename.txt         # history of a specific file
```

---

## LESSON 7 — Seeing What Changed

### `git diff`
See exactly what lines changed, before staging or committing.

```bash
git diff                    # unstaged changes (working dir vs last commit)
git diff --staged           # staged changes (staging area vs last commit)
git diff HEAD               # all changes since last commit (staged + unstaged)
git diff abc123 def456      # diff between two specific commits
```

**Reading the output:**
- `-` red lines = what was removed
- `+` green lines = what was added
- `@@` header = which line number the change is near

**Gotcha:** `git diff` goes silent after `git add` — use `git diff --staged` to see staged changes.

---

## LESSON 8 — Undoing Mistakes

### `git restore`
Discard changes in working directory or unstage files.

```bash
git restore filename.txt            # throw away unstaged changes (can't undo this!)
git restore --staged filename.txt   # unstage a file (change stays in your file)
git restore --staged .              # unstage everything
```

### `git reset`
Undo commits (local only — don't use on pushed commits).

```bash
git reset --soft HEAD~1     # undo last commit, keep changes staged
git reset --mixed HEAD~1    # undo last commit, keep changes unstaged (default)
git reset --hard HEAD~1     # undo last commit AND discard all changes (destructive)
```

### `git revert`
Safely undo a commit by creating a new "undo" commit. Use this after pushing.

```bash
git revert HEAD             # undo the last commit (safe, keeps history intact)
git revert abc123           # undo a specific commit by hash
```

**Which to use:**
| Situation | Command |
|---|---|
| Bad edit, not staged yet | `git restore filename` |
| Staged but not committed | `git restore --staged filename` |
| Committed, not pushed yet | `git reset --soft HEAD~1` |
| Committed and pushed | `git revert HEAD` |

---

<!-- NEW LESSONS WILL BE ADDED HERE -->
