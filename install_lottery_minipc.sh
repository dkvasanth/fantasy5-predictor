#!/bin/bash
# Installation script for lottery app on mini PC
# Run this on the mini PC: bash install_lottery_minipc.sh

echo "=================================="
echo "Fantasy 5 Lottery App Installer"
echo "=================================="
echo

# Install dependencies
echo "📦 Installing Python dependencies..."
sudo apt-get update
sudo apt-get install -y python3-pip python3-requests python3-bs4

# Verify installation
echo
echo "✅ Verifying installation..."
python3 -c "import requests; import bs4; print('✅ All dependencies installed successfully!')"

echo
echo "=================================="
echo "✅ Installation Complete!"
echo "=================================="
echo
echo "Next steps:"
echo "1. Edit ~/lottery/fantasy5_auto.py and update email settings (lines 17-24)"
echo "2. Test email: python3 ~/lottery/test_email.py"
echo "3. Run lottery app: python3 ~/lottery/fantasy5_auto.py"
echo "4. Setup cron job (see LOTTERY_SETUP.md)"
echo
