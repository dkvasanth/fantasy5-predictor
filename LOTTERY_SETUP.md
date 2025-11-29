# Fantasy 5 Auto-Predictor Setup Guide

Automatically scrape lottery data and email daily predictions.

## 📋 Prerequisites

- Python 3.7+
- Email account (Gmail recommended)
- Mac/Linux/Windows with cron or Task Scheduler

---

## 🚀 Quick Setup

### 1. Install Dependencies

```bash
cd /Users/vasanth/p2p-video-chat
pip3 install -r requirements_lottery.txt
```

### 2. Configure Email Settings

Edit the `fantasy5_auto.py` file and update the CONFIG section (lines 17-24):

```python
CONFIG = {
    'email': {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'sender_email': 'YOUR_EMAIL@gmail.com',      # Change this
        'sender_password': 'YOUR_APP_PASSWORD',       # Change this
        'recipient_email': 'RECIPIENT@example.com',   # Change this
    }
}
```

### 3. Generate Gmail App Password (if using Gmail)

⚠️ **Don't use your regular Gmail password!**

1. Go to: https://myaccount.google.com/apppasswords
2. Sign in to your Google account
3. Click "Select app" → Choose "Mail"
4. Click "Select device" → Choose "Other" → Type "Lottery Script"
5. Click "Generate"
6. Copy the 16-character password
7. Paste it in `sender_password` (remove spaces)

### 4. Test the Script

```bash
python3 fantasy5_auto.py
```

You should see:
```
📥 Fetching data from https://www.lotteryusa.com/california/fantasy-5/year...
✅ Scraped 50+ draws
💾 Saved data to fantasy5_history.json
🎯 TODAY'S PREDICTIONS
...
📧 Sending email...
✅ Email sent successfully!
```

---

## ⏰ Setup Daily Auto-Run

### Option A: Mac/Linux (cron)

1. Open crontab editor:
```bash
crontab -e
```

2. Add this line to run daily at 7:00 PM (after the 6:30 PM draw):
```bash
0 19 * * * cd /Users/vasanth/p2p-video-chat && /usr/bin/python3 fantasy5_auto.py >> lottery.log 2>&1
```

3. Save and exit (Ctrl+O, Enter, Ctrl+X for nano)

4. Verify cron job:
```bash
crontab -l
```

**Cron schedule examples:**
```
0 19 * * *     # Daily at 7:00 PM
0 20 * * *     # Daily at 8:00 PM
30 18 * * *    # Daily at 6:30 PM (right after draw)
0 9 * * *      # Daily at 9:00 AM
0 12 * * 1     # Every Monday at noon
```

### Option B: Windows (Task Scheduler)

1. Open Task Scheduler
2. Create Basic Task
3. Name: "Fantasy 5 Predictions"
4. Trigger: Daily at 7:00 PM
5. Action: Start a program
   - Program: `C:\Python\python.exe`
   - Arguments: `fantasy5_auto.py`
   - Start in: `C:\Users\vasanth\p2p-video-chat`
6. Finish

### Option C: Deploy to Mini PC

```bash
# Copy script to mini PC
scp fantasy5_auto.py requirements_lottery.txt dkvasanth@10.0.0.21:/opt/lottery/

# SSH into mini PC
ssh dkvasanth@10.0.0.21

# Setup
cd /opt/lottery
pip3 install -r requirements_lottery.txt

# Edit config
nano fantasy5_auto.py  # Update email settings

# Add to crontab
crontab -e
# Add: 0 19 * * * cd /opt/lottery && python3 fantasy5_auto.py >> lottery.log 2>&1
```

---

## 📧 Email Preview

Your daily email will include:

- **3 Prediction Sets** (Hot, Overdue, Balanced)
- **Statistics** (Top hot numbers, most overdue)
- **Analysis Info** (Number of draws analyzed)
- **Formatted HTML** with colors and styling
- **Disclaimer** (lottery is random!)

---

## 🔧 Troubleshooting

### "535 Authentication failed"
- Use app-specific password, not regular password
- Enable "Less secure app access" (not recommended)
- Try different email provider

### "No data found"
- Website structure changed - script needs updating
- Using cached data from previous run
- Check internet connection

### Email not sending
- Check SMTP settings for your provider
- Verify firewall isn't blocking port 587
- Test with a simple Python SMTP script first

### Cron job not running
```bash
# Check cron service status
sudo systemctl status cron

# View cron logs
grep CRON /var/log/syslog

# Test absolute paths
which python3  # Use this full path in crontab
```

---

## 📊 Advanced Usage

### Manual Run for Testing
```bash
python3 fantasy5_auto.py
```

### View Log File
```bash
tail -f lottery.log
```

### Update Data Only (no email)
Edit `fantasy5_auto.py` and comment out the email line:
```python
# predictor.send_email(stats)
```

### Change Prediction Time
Edit crontab to run at different time:
```bash
30 18 * * *  # 6:30 PM (right after draw)
0 8 * * *    # 8:00 AM (morning predictions)
```

---

## ⚠️ Important Notes

1. **Lottery is Random** - This script analyzes patterns but doesn't improve odds
2. **Play Responsibly** - Set limits and never spend more than you can afford
3. **Email Security** - Never share your app password
4. **Rate Limiting** - Script respects website by caching data
5. **Legal** - For personal use only; check local regulations

---

## 📝 Files Created

- `fantasy5_auto.py` - Main script
- `requirements_lottery.txt` - Python dependencies
- `fantasy5_history.json` - Cached lottery data (auto-generated)
- `lottery.log` - Execution log (auto-generated)

---

## 🆘 Support

If you encounter issues:
1. Check the log file: `cat lottery.log`
2. Run manually to see errors: `python3 fantasy5_auto.py`
3. Verify email settings are correct
4. Check internet connection
5. Ensure website is accessible

---

**Good luck! 🍀**
