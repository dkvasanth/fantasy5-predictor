#!/bin/bash
# Quick script to update lottery data on mini PC

echo "=================================="
echo "Lottery Data Updater"
echo "=================================="
echo

# Check if CSV file exists in Downloads
CSV_FILE="$HOME/Downloads/california-fantasy-5.csv"

if [ ! -f "$CSV_FILE" ]; then
    echo "❌ CSV file not found: $CSV_FILE"
    echo
    echo "Steps:"
    echo "1. Go to: https://www.lotteryusa.com/california/fantasy-5/year"
    echo "2. Click 'CSV' button"
    echo "3. Download will save to ~/Downloads/"
    echo "4. Run this script again"
    exit 1
fi

# Get file info
FILE_SIZE=$(ls -lh "$CSV_FILE" | awk '{print $5}')
FILE_DATE=$(ls -l "$CSV_FILE" | awk '{print $6, $7, $8}')

echo "Found CSV file:"
echo "  Location: $CSV_FILE"
echo "  Size: $FILE_SIZE"
echo "  Modified: $FILE_DATE"
echo

# Upload to mini PC
echo "📤 Uploading to mini PC..."
scp "$CSV_FILE" dkvasanth@10.0.0.21:~/lottery/fantasy5_data.csv

if [ $? -eq 0 ]; then
    echo
    echo "=================================="
    echo "✅ Success!"
    echo "=================================="
    echo
    echo "Lottery data updated on mini PC!"
    echo "Next predictions will use this data."
    echo

    # Optional: Archive the file
    ARCHIVE_DIR="$HOME/Documents/lottery_backups"
    mkdir -p "$ARCHIVE_DIR"
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    cp "$CSV_FILE" "$ARCHIVE_DIR/fantasy5_$TIMESTAMP.csv"
    echo "📁 Backup saved: $ARCHIVE_DIR/fantasy5_$TIMESTAMP.csv"
else
    echo
    echo "❌ Upload failed!"
    echo "Check your connection to mini PC"
fi
