
# Git Bash Commands with Short Explanations

# 1. Initialize a new Git repository
git init  # Creates a new Git repository in the current directory

# 2. Clone an existing repository
git clone <repository-url>  # Clones a remote repository to your local machine

# 3. Check the status of the working directory
git status  # Shows the current status of files (staged, modified, untracked)

# 4. Add changes to the staging area
git add <filename>  # Adds a file to the staging area
git add .  # Adds all changes to the staging area

# 5. Commit changes with a message
git commit -m "Commit message"  # Commits the staged changes with a description

# 6. Push changes to a remote repository
git push origin <branch-name>  # Pushes the local branch to the remote repository

# 7. Pull changes from a remote repository
git pull origin <branch-name>  # Fetches and merges changes from the remote branch

# 8. Create or list branches
git branch <new-branch-name>  # Creates a new branch
git branch  # Lists all branches

# 9. Switch branches or create and switch to a new branch
git checkout <branch-name>  # Switches to the specified branch
git checkout -b <new-branch-name>  # Creates and switches to a new branch

# 10. Merge changes from another branch
git merge <branch-name>  # Merges the specified branch into the current branch

# 11. Show commit history
git log  # Displays the commit history of the current branch

# 12. Add or view remote repositories
git remote add origin <repository-url>  # Adds a new remote repository
git remote -v  # Shows the URLs of the remote repositories

# 13. Stash uncommitted changes
git stash  # Temporarily saves changes that haven't been committed
git stash pop  # Restores the stashed changes

# 14. Unstage changes
git reset <file>  # Removes a file from the staging area without deleting it

# 15. Rebase changes onto another branch
git rebase <branch-name>  # Reapplies commits on top of another branch

# 16. Show differences between commits or branches
git diff  # Displays the differences between files or commits

# 17. Remove a file from the repository
git rm <filename>  # Deletes a file from both the repository and the file system

# 18. Fetch changes without merging them
git fetch origin  # Downloads changes from the remote repository without merging

# 19. Tag a commit
git tag <tag-name>  # Creates a tag for the current commit

# 20. Set Git configuration values
git config --global user.name "Your Name"  # Sets the global username for Git commits
git config --global user.email "your.email@example.com"  # Sets the global email for Git commits
