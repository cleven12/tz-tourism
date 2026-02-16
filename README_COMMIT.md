# 🚀 Timed Commit Scripts

Two scripts to commit changes with realistic timing:

## Scripts

### 1. `commit_timed.sh` - Production (4 min delay)
```bash
./commit_timed.sh
```
- **4 minutes** between each commit
- Makes ~10 commits over **40 minutes**
- Looks natural on GitHub profile

### 2. `commit_quick.sh` - Testing (30 sec delay)
```bash
./commit_quick.sh
```
- **30 seconds** between commits
- For testing the script
- Makes all commits in ~5 minutes

## What it does

✅ Commits each app separately  
✅ Adds descriptive commit messages  
✅ Delays between commits (appears as different times)  
✅ Skips empty changes  
✅ Shows progress with emojis  

## Commits Made

1. Clean up old structure
2. Enhance attractions app
3. Enhance regions app
4. Add weather app
5. Add accounts app
6. Update Django config
7. Add serializers
8. Add URL patterns
9. Add migrations
10. Finalize implementation

## After Running

```bash
# Check commits
git log --oneline -10

# Push to GitHub
git push origin main
```

## Tips

- Run during work hours for realistic appearance
- Don't interrupt the script
- Check `git status` first to see what will be committed
- Use `commit_quick.sh` first to test

## Time Required

- **Quick:** ~5 minutes (testing)
- **Timed:** ~40 minutes (production)

---

**Note:** These scripts help space out commits naturally, making your contribution graph look more organic! 🌱
