# ---------------------------------------------
# Update and Push DMS Project to GitHub Script
# ---------------------------------------------

# Set Execution Policy temporarily
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Navigate to project folder (update path if needed)
$projectPath = "C:\Users\HP\Desktop\DMS Project"
Set-Location $projectPath

# GitHub repo URL
$repoURL = "https://github.com/pgadhavi309-rgb/dms-project.git"

# Ensure the correct remote
if ((git remote) -contains "origin") {
    git remote remove origin
}
git remote add origin $repoURL

# Stage all changes
git add .

# Commit changes with a message input from user
$commitMessage = Read-Host "Enter commit message"
git commit -m "$commitMessage"

# Pull latest changes and rebase to avoid non-fast-forward
git pull origin main --rebase

# Push changes to GitHub
git push -u origin main

Write-Host "✅ Project successfully updated on GitHub!"
