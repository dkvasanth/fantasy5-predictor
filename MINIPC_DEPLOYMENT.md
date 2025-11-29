# Fantasy 5 Lottery App - Mini PC Deployment

## ✅ What's Been Deployed:

All lottery app files have been copied to your mini PC at:
```
/home/dkvasanth/lottery/
```

**Files deployed:**
- ✅ `fantasy5_auto.py` - Main lottery prediction script
- ✅ `test_email.py` - Email configuration tester
- ✅ `requirements_lottery.txt` - Python dependencies
- ✅ `LOTTERY_SETUP.md` - Full setup guide
- ✅ `fantasy5_config.example.py` - Configuration example
- ✅ `install_lottery_minipc.sh` - Installation script

---

## 🔧 Complete the Setup (Run on Mini PC):

### Step 1: SSH into Mini PC
```bash
ssh dkvasanth@10.0.0.21
```

### Step 2: Install Python Dependencies
```bash
cd ~/lottery
bash install_lottery_minipc.sh
```

**What this does:**
- Installs pip3
- Installs requests library (for web scraping)
- Installs beautifulsoup4 (for HTML parsing)
- Verifies everything works

### Step 3: Configure Email Settings

Edit the main script:
```bash
nano ~/lottery/fantasy5_auto.py
```

Update these lines (around line 17-24):
```python
'sender_email': 'YOUR_EMAIL@gmail.com',      # Your Gmail address
'sender_password': 'YOUR_APP_PASSWORD',       # 16-char app password
'recipient_email': 'WHERE_TO_SEND@gmail.com', # Where to receive predictions
```

**Save:** Ctrl+O, Enter, Ctrl+X

**Get Gmail App Password:**
1. Go to: https://myaccount.google.com/apppasswords
2. Create password for "Mail" → "Other (Custom name)"
3. Copy the 16-character code (no spaces)

### Step 4: Test Email Configuration
```bash
# First update test_email.py with same settings
nano ~/lottery/test_email.py

# Then test
python3 ~/lottery/test_email.py
```

You should see: `✅ Email sent successfully!`

### Step 5: Run the Lottery App
```bash
python3 ~/lottery/fantasy5_auto.py
```

**Expected output:**
```
📥 Fetching data from https://www.lotteryusa.com/california/fantasy-5/year...
✅ Scraped 50+ draws
💾 Saved data to fantasy5_history.json
🎯 TODAY'S PREDICTIONS
1. Hot Numbers:    [7, 13, 21, 35, 38]
2. Overdue:        [3, 5, 11, 25, 28]
3. Balanced:       [13, 16, 20, 21, 31]
📧 Sending email...
✅ Email sent successfully!
```

### Step 6: Setup Daily Auto-Run (Cron Job)
```bash
# Open crontab editor
crontab -e

# Add this line (runs daily at 7:00 PM):
0 19 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_auto.py >> lottery.log 2>&1

# Save and exit
```

**Verify cron job:**
```bash
crontab -l
```

---

## 📧 What You'll Receive Daily:

Every day at 7:00 PM (after the 6:30 PM draw), you'll get an email with:

- **3 Prediction Sets:**
  - Hot Numbers (most frequent)
  - Overdue Numbers (haven't appeared recently)
  - Balanced Numbers (optimized distribution)

- **Statistics:**
  - Top 5 hottest numbers
  - Top 5 most overdue numbers
  - Analysis details

- **Beautiful HTML formatting** with colors and styling

---

## 🔍 Verify Everything Works:

### Check if cron job is running:
```bash
# View recent logs
tail ~/lottery/lottery.log

# Watch for new predictions (wait until 7 PM)
tail -f ~/lottery/lottery.log
```

### Manual run anytime:
```bash
python3 ~/lottery/fantasy5_auto.py
```

### View cached data:
```bash
cat ~/lottery/fantasy5_history.json
```

---

## 📅 Cron Schedule Options:

```bash
# Daily at 7:00 PM (recommended - after 6:30 PM draw)
0 19 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_auto.py >> lottery.log 2>&1

# Daily at 8:00 PM
0 20 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_auto.py >> lottery.log 2>&1

# Daily at 9:00 AM (morning predictions)
0 9 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_auto.py >> lottery.log 2>&1

# Twice daily (9 AM and 7 PM)
0 9,19 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_auto.py >> lottery.log 2>&1
```

---

## 🆘 Troubleshooting:

### Dependencies not installing?
```bash
# Try manual install
sudo apt-get update
sudo apt-get install python3-pip python3-requests python3-bs4
```

### Email not working?
1. Verify settings in `fantasy5_auto.py`
2. Test with `python3 test_email.py`
3. Check if using app password (not regular password)
4. Check spam folder for first email

### Cron not running?
```bash
# Check cron service
sudo systemctl status cron

# View cron logs
grep CRON /var/log/syslog | tail -20

# Use full path to python
which python3  # Use this path in crontab
```

### Script errors?
```bash
# View detailed error log
cat ~/lottery/lottery.log

# Run manually to see errors
python3 ~/lottery/fantasy5_auto.py
```

---

## 📊 File Locations:

```
/home/dkvasanth/lottery/
├── fantasy5_auto.py           # Main script
├── test_email.py              # Email tester
├── install_lottery_minipc.sh  # Installer
├── LOTTERY_SETUP.md          # Full guide
├── fantasy5_history.json     # Cached data (auto-generated)
└── lottery.log               # Execution log (auto-generated)
```

---

## ⚠️ Important Notes:

1. **First time:** Email might go to spam - mark as "Not Spam"
2. **Privacy:** Never share your app password
3. **Lottery:** This doesn't improve your odds - it's for fun!
4. **Data:** Script caches data to avoid excessive web requests
5. **Updates:** Script auto-updates data each run

---

## 🎯 Quick Commands:

```bash
# SSH to mini PC
ssh dkvasanth@10.0.0.21

# Run lottery app manually
python3 ~/lottery/fantasy5_auto.py

# View logs
tail -f ~/lottery/lottery.log

# Edit email settings
nano ~/lottery/fantasy5_auto.py

# Test email
python3 ~/lottery/test_email.py

# Edit cron schedule
crontab -e
```

---

**All set! 🎰 Good luck!** 🍀
