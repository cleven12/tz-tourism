#!/bin/bash

# Quick Commit Script (30 seconds delay for testing)

DELAY_SECONDS=30

echo "🚀 Starting QUICK commits (30s delay)..."
echo ""

commit_with_delay() {
    local files="$1"
    local message="$2"
    local delay="$3"
    
    git add $files 2>/dev/null
    
    if git diff --cached --quiet; then
        echo "⏭️  Skip: $(echo "$message" | head -n1)"
        return
    fi
    
    git commit -m "$message"
    
    if [ $? -eq 0 ]; then
        echo "✅ $(echo "$message" | head -n1)"
        if [ "$delay" = "true" ]; then
            echo "⏳ Waiting ${DELAY_SECONDS}s..."
            sleep ${DELAY_SECONDS}
        fi
    fi
}

commit_with_delay "src/attractions src/regions src/weather src/tour_api" \
"refactor: remove old app structure from src root

- Remove apps from src/ root directory
- Prepare for new src/app/ structure
- Clean up old migrations and cache files" \
true

commit_with_delay "src/app/attractions/" \
"feat: enhance attractions app with full implementation

- Add detailed Attraction model with all fields
- Implement serializers for API responses
- Add viewsets with CRUD operations
- Create URL routing for attractions
- Add initial database migration
- Configure admin interface" \
true

commit_with_delay "src/app/regions/" \
"feat: enhance regions app with full implementation

- Add comprehensive Region model
- Implement region serializers
- Add viewsets for region management
- Create URL patterns for regions API
- Add database migrations
- Configure admin panel" \
true

commit_with_delay "src/app/weather/" \
"feat: implement weather integration app

- Create weather service for Open-Meteo API
- Add real-time weather fetching
- Implement caching for weather data
- Add seasonal pattern analysis
- Create weather API endpoints" \
true

commit_with_delay "src/app/accounts/" \
"feat: add user accounts and authentication

- Create custom user model
- Implement JWT authentication
- Add user registration and login
- Create user profile management
- Add permission classes" \
true

commit_with_delay "src/cofig/" \
"feat: update Django configuration and routing

- Update settings for all apps
- Configure API routing with versioning
- Add CORS and security middleware
- Set up static files handling
- Configure database settings" \
true

commit_with_delay "src/app/*/serializers.py" \
"feat: implement comprehensive API serializers

- Add AttractionSerializer with validation
- Create RegionSerializer with nested data
- Implement WeatherSerializer
- Add custom field validators
- Include read-only computed fields" \
true

commit_with_delay "src/app/*/urls.py" \
"feat: configure URL routing for all apps

- Set up DRF router for viewsets
- Add custom action endpoints
- Configure nested URL patterns
- Include API documentation URLs" \
true

commit_with_delay "src/app/*/migrations/" \
"feat: add database migrations for all models

- Initial migration for attractions
- Initial migration for regions
- Initial migration for weather
- Add indexes for performance
- Set up foreign key relationships" \
true

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
echo "🎉 Done! Recent commits:"
git log --oneline -10
