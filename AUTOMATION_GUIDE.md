# Fantasy 5 Lottery - Full Automation Guide

You now have **TWO versions** of the lottery predictor:

## 📊 Version Comparison

| Feature | **Manual CSV** | **Fully Automated** |
|---------|---------------|---------------------|
| **Data Source** | You download CSV manually | Auto-downloads via browser |
| **Setup Complexity** | Simple ✅ | Complex ⚠️ |
| **Dependencies** | requests, bs4 | + playwright, chromium |
| **Resource Usage** | Low | Higher (browser required) |
| **Reliability** | Very High ✅ | May break if site changes |
| **Currently Working** | ✅ YES | ⚠️ Requires setup |

---

## 🎯 **RECOMMENDED: Manual CSV Version** (Currently Deployed)

### Why it's better:
- ✅ Simple and reliable
- ✅ Already working on mini PC
- ✅ Low resource usage
- ✅ Easy to troubleshoot
- ✅ Update CSV weekly/monthly is enough

### Current Setup:
```bash
# On mini PC - ALREADY CONFIGURED ✅
0 19 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_auto.py >> lottery.log 2>&1
```

### To Update Data:
```bash
# 1. Download CSV from website (once a week/month)
#    https://www.lotteryusa.com/california/fantasy-5/year
#    Click "CSV" button

# 2. Upload to mini PC
scp ~/Downloads/california-fantasy-5.csv dkvasanth@10.0.0.21:~/lottery/fantasy5_data.csv

# Or use the update script:
./update_lottery.sh
```

---

## 🤖 **ADVANCED: Fully Automated Version** (Optional)

### When to use:
- You want 100% automation
- You don't mind extra complexity
- You're comfortable troubleshooting browser issues

### Setup on Mini PC:

#### Step 1: SSH to Mini PC
```bash
ssh dkvasanth@10.0.0.21
cd ~/lottery
```

#### Step 2: Install Playwright
```bash
bash install_automated.sh
```

This installs:
- playwright Python package
- Chromium browser
- Browser dependencies

**Expected time:** 5-10 minutes
**Disk space:** ~300 MB

#### Step 3: Test Automated Version
```bash
python3 fantasy5_automated.py
```

Expected output:
```
🌐 Launching browser automation...
📥 Navigating to https://www.lotteryusa.com/...
🔍 Looking for CSV download button...
✅ Found CSV button
🖱️  Clicked CSV download button
💾 Downloaded to: fantasy5_data.csv
✅ Loaded 50+ draws from CSV
🎯 TODAY'S PREDICTIONS
📧 Sending email...
✅ Email sent successfully!
```

#### Step 4: Update Cron Job
```bash
crontab -e

# REPLACE the existing line with:
0 19 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_automated.py >> lottery_auto.log 2>&1
```

---

## ⚠️ Troubleshooting Automated Version

### "CSV button not found"
- Website structure changed
- Try taking a screenshot: check `debug_screenshot.png`
- Fallback to manual CSV version

### "Browser launch failed"
```bash
# Reinstall browser
python3 -m playwright install chromium
python3 -m playwright install-deps
```

### "Memory issues"
- Mini PC might not have enough RAM for browser
- Use manual CSV version instead

### Check logs:
```bash
tail -f ~/lottery/lottery_auto.log
```

---

## 🎯 My Recommendation

**Stick with the Manual CSV version** because:

1. **It's already working** ✅
2. **More reliable** - no browser dependencies
3. **Lower resource usage** - important for mini PC
4. **Easier to maintain**
5. **Updating CSV once a week is fine** - patterns don't change daily

---

## 📁 File Structure

```
~/lottery/
├── fantasy5_auto.py          # Manual CSV version (CURRENT) ✅
├── fantasy5_automated.py     # Browser automation version
├── fantasy5_data.csv          # Data file (50 draws)
├── fantasy5_history.json     # Cached analysis
├── install_automated.sh       # Playwright installer
├── test_email.py             # Email tester
└── lottery.log               # Current execution log
```

---

## 🔄 Switching Between Versions

### Use Manual CSV (Current):
```bash
# Cron job:
0 19 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_auto.py >> lottery.log 2>&1
```

### Use Automated:
```bash
# After installing Playwright:
0 19 * * * cd /home/dkvasanth/lottery && /usr/bin/python3 fantasy5_automated.py >> lottery_auto.log 2>&1
```

---

## 💡 Best Practice

**Use Manual CSV version** and update data:
- Weekly: After major winning streaks
- Monthly: General maintenance
- As needed: When you remember 😊

The statistical patterns don't change significantly day-to-day, so weekly/monthly updates are perfectly fine!

---

## ✅ Summary

**Current Status:**
- ✅ Manual CSV version **WORKING** and sending daily emails
- ✅ Automated version **READY** for installation (optional)
- ✅ Email configuration **COMPLETE**
- ✅ Cron job **ACTIVE** (runs daily at 7 PM)

**Your email:** dkvasanth@gmail.com
**Daily predictions:** 7:00 PM PT
**Next email:** Tonight! 🎰

---

**Questions?** Both versions are ready - use whichever you prefer!
