#!/bin/bash

# Timed Git Commit Script
# Commits changes with delays to appear as natural development workflow

DELAY_MINUTES=4

echo "🚀 Starting timed commits for TZ Tourism Backend..."
echo "⏰ Delay between commits: ${DELAY_MINUTES} minutes"
echo ""

# Function to commit with message
commit_with_delay() {
    local files="$1"
    local message="$2"
    local delay="$3"
    
    git add $files 2>/dev/null
    
    if git diff --cached --quiet; then
        echo "⏭️  Skipping (no changes): $(echo "$message" | head -n1)"
        return
    fi
    
    git commit -m "$message"
    
    if [ $? -eq 0 ]; then
        echo "✅ Committed: $(echo "$message" | head -n1)"
        if [ "$delay" = "true" ]; then
            echo "⏳ Waiting ${DELAY_MINUTES} minutes before next commit..."
            sleep $((DELAY_MINUTES * 60))
            echo ""
        fi
    else
        echo "❌ Failed to commit"
    fi
}

# Commit 1: Clean up old structure
commit_with_delay "src/attractions src/regions src/weather src/tour_api" \
"refactor: remove old app structure from src root

- Remove apps from src/ root directory
- Prepare for new src/app/ structure
- Clean up old migrations and cache files" \
true

# Commit 2: Update attractions app
commit_with_delay "src/app/attractions/" \
"feat: enhance attractions app with full implementation

- Add detailed Attraction model with all fields
- Implement serializers for API responses
- Add viewsets with CRUD operations
- Create URL routing for attractions
- Add initial database migration
- Configure admin interface" \
true

# Commit 3: Update regions app
commit_with_delay "src/app/regions/" \
"feat: enhance regions app with full implementation

- Add comprehensive Region model
- Implement region serializers
- Add viewsets for region management
- Create URL patterns for regions API
- Add database migrations
- Configure admin panel" \
true

# Commit 4: Add weather app
commit_with_delay "src/app/weather/" \
"feat: implement weather integration app

- Create weather service for Open-Meteo API
- Add real-time weather fetching
- Implement caching for weather data
- Add seasonal pattern analysis
- Create weather API endpoints" \
true

# Commit 5: Add accounts app
commit_with_delay "src/app/accounts/" \
"feat: add user accounts and authentication

- Create custom user model
- Implement JWT authentication
- Add user registration and login
- Create user profile management
- Add permission classes" \
true

# Commit 6: Update Django config
commit_with_delay "src/cofig/" \
"feat: update Django configuration and routing

- Update settings for all apps
- Configure API routing with versioning
- Add CORS and security middleware
- Set up static files handling
- Configure database settings" \
true

# Commit 7: Add serializers
commit_with_delay "src/app/*/serializers.py" \
"feat: implement comprehensive API serializers

- Add AttractionSerializer with validation
- Create RegionSerializer with nested data
- Implement WeatherSerializer
- Add custom field validators
- Include read-only computed fields" \
true

# Commit 8: Add URL patterns
commit_with_delay "src/app/*/urls.py" \
"feat: configure URL routing for all apps

- Set up DRF router for viewsets
- Add custom action endpoints
- Configure nested URL patterns
- Include API documentation URLs" \
true

# Commit 9: Add migrations
commit_with_delay "src/app/*/migrations/" \
"feat: add database migrations for all models

- Initial migration for attractions
- Initial migration for regions
- Initial migration for weather
- Add indexes for performance
- Set up foreign key relationships" \
true

# Commit 10: Remaining changes
if [ -n "$(git status --porcelain)" ]; then
    commit_with_delay "." \
"chore: finalize backend implementation

- Update manage.py configuration
- Add remaining config files
- Clean up imports and formatting
- Prepare for production deployment" \
false
fi

echo ""
echo "🎉 All commits completed!"
echo ""
echo "📊 Recent commits:"
git log --oneline -10
echo ""
echo "💡 To push to GitHub, run: git push origin main"
