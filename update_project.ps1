# ===== PowerShell script to update GitHub repo =====

# 1. Check git status
Write-Host "Checking git status..."
git status

# 2. Stage all changes
Write-Host "Staging all changes..."
git add .

# 3. Commit changes
$commitMessage = Read-Host "Enter commit message"
git commit -m "$commitMessage"

# 4. Pull latest changes from remote (rebase to avoid conflicts)
Write-Host "Pulling latest changes from GitHub..."
git pull origin main --rebase

# 5. Push changes to remote
Write-Host "Pushing changes to GitHub..."
git push origin main

Write-Host "✅ Project successfully updated on GitHub!"
