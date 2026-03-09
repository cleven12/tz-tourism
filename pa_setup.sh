#!/bin/bash
# One-time setup script for PythonAnywhere
# Run these commands in the PA Bash console to link ~/main to the GitHub repo.

set -e
PA_USERNAME="xenohuru"
PROJECT_DIR="/home/${PA_USERNAME}/main"
VENV_DIR="/home/${PA_USERNAME}/.virtualenvs/xenohuru-venv"
REPO_URL="https://github.com/xenohuru/xenohuru-api.git"

echo "=== Step 1: Clean up old Django project files ==="
cd "$PROJECT_DIR"
# Remove old default Django project files (if they exist)
rm -rf main/ manage.py static/ media/ 2>/dev/null || true

echo "=== Step 2: Link to GitHub repo ==="
if [ -d ".git" ]; then
  echo "Git already initialized, pulling latest..."
  git pull origin main
else
  git init
  git remote add origin "$REPO_URL"
  git fetch origin main
  git reset --hard origin/main
fi

echo "=== Step 3: Create virtual environment ==="
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"

echo "=== Step 4: Install dependencies ==="
pip install -r "$PROJECT_DIR/requirements.txt" --quiet

echo "=== Step 5: Check .env file ==="
if [ ! -f "$PROJECT_DIR/.env" ]; then
  echo ""
  echo "⚠️  .env file missing! Upload it to: $PROJECT_DIR/.env"
  echo "    Use the PA Files tab or: nano $PROJECT_DIR/.env"
  echo "    Reference: $PROJECT_DIR/.env.example"
  echo ""
else
  echo ".env found ✓"
fi

echo "=== Step 6: Run migrations ==="
python "$PROJECT_DIR/manage.py" migrate --no-input

echo "=== Step 7: Collect static files ==="
python "$PROJECT_DIR/manage.py" collectstatic --no-input --clear

echo ""
echo "✅ Setup complete!"
echo ""
echo "=== Configure the Web tab in PythonAnywhere ==="
echo "  Source code:  $PROJECT_DIR"
echo "  Virtualenv:   $VENV_DIR"
echo "  WSGI file:    paste contents of $PROJECT_DIR/wsgi_config.py"
echo "  Static files: URL=/static/  Dir=$PROJECT_DIR/staticfiles"
echo "  Reload the web app"
