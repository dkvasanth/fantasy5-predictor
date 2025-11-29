#!/bin/bash
# Installation script for FULLY AUTOMATED lottery predictor

echo "========================================"
echo "Fantasy 5 Automated Predictor Installer"
echo "========================================"
echo

# Install Python packages
echo "📦 Installing Python dependencies..."
sudo apt-get update
sudo apt-get install -y python3-pip

# Install playwright
pip3 install --user playwright

# Install Playwright browsers
echo
echo "🌐 Installing Chromium browser for automation..."
python3 -m playwright install chromium
python3 -m playwright install-deps

# Verify installation
echo
echo "✅ Verifying installation..."
python3 -c "from playwright.sync_api import sync_playwright; print('✅ Playwright installed successfully!')"

echo
echo "========================================"
echo "✅ Installation Complete!"
echo "========================================"
echo
echo "Next steps:"
echo "1. Test: python3 ~/lottery/fantasy5_automated.py"
echo "2. Setup cron (see instructions below)"
echo
echo "Cron job for daily 7 PM run:"
echo "0 19 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_automated.py >> lottery_auto.log 2>&1"
echo
