#!/bin/bash
# One-time setup script for PythonAnywhere
# Run this in the PythonAnywhere bash console ONCE to set up the project.
#
# This links the existing /home/xenohuru/main directory to the GitHub repo,
# replacing the old default Django project with the xenohuru-api codebase.
#
# Usage: paste these commands in the PA Bash console

set -e
PA_USERNAME="xenohuru"
PROJECT_DIR="/home/${PA_USERNAME}/main"
VENV_DIR="/home/${PA_USERNAME}/.virtualenvs/xenohuru-venv"
REPO_URL="https://github.com/xenohuru/xenohuru-api.git"

echo "=== Step 1: Link existing directory to GitHub repo ==="
cd "$PROJECT_DIR"
if [ -d ".git" ]; then
  echo "Git already initialized, pulling latest..."
  git pull origin main
else
  git init
  git remote add origin "$REPO_URL"
  git fetch origin main
  git reset --hard origin/main
fi

echo "=== Step 2: Create virtual environment ==="
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"

echo "=== Step 3: Install dependencies ==="
pip install -r "$PROJECT_DIR/requirements.txt" --quiet

echo "=== Step 4: Check .env file ==="
if [ ! -f "$PROJECT_DIR/src/.env" ]; then
  echo ""
  echo "⚠️  .env file missing! Upload it to: $PROJECT_DIR/src/.env"
  echo "    Use the PA Files tab or: nano $PROJECT_DIR/src/.env"
  echo "    Reference: $PROJECT_DIR/src/.env.example"
  echo ""
else
  echo ".env found ✓"
fi

echo "=== Step 5: Run migrations ==="
cd "$PROJECT_DIR"
python src/manage.py migrate --no-input

echo "=== Step 6: Collect static files ==="
python src/manage.py collectstatic --no-input --clear

echo ""
echo "✅ Setup complete!"
echo ""
echo "=== Next steps in PythonAnywhere dashboard ==="
echo "1. Go to Web tab → your web app"
echo "2. Set Source code: $PROJECT_DIR"
echo "3. Set Virtualenv: $VENV_DIR"
echo "4. Edit WSGI file — replace contents with the wsgi_config.py snippet:"
echo "   cat $PROJECT_DIR/wsgi_config.py"
echo "5. Set Static files: URL=/static/  Dir=$PROJECT_DIR/src/staticfiles"
echo "6. Reload the web app"
