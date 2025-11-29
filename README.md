# Fantasy 5 Lottery Predictor 🎰

Automated California Fantasy 5 lottery number predictor with daily email notifications. Uses statistical analysis (frequency, gap analysis, and distribution balancing) to generate predictions.

## ✨ Features

- 📊 **3 Prediction Algorithms**
  - Hot Numbers (frequency analysis)
  - Overdue Numbers (gap analysis)
  - Balanced Distribution (odd/even, high/low optimization)

- 📧 **Automated Email Notifications**
  - Beautiful HTML-formatted emails
  - Daily predictions at 7:00 PM PT
  - Statistics and analysis included

- 🤖 **Two Versions**
  - **Manual CSV**: Simple, reliable (recommended)
  - **Fully Automated**: Browser automation with Playwright

- ⚙️ **Easy Setup**
  - Runs on Mini PC or any Linux server
  - Cron job for daily automation
  - Comprehensive documentation

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/dkvasanth/fantasy5-predictor.git
cd fantasy5-predictor
```

### 2. Choose Version

#### Option A: Manual CSV (Recommended)
```bash
# Install dependencies
sudo apt-get install -y python3-requests python3-bs4

# Configure email in fantasy5_auto.py
nano fantasy5_auto.py
# Update lines 24-26 with your email settings

# Test
python3 fantasy5_auto.py

# Setup daily cron job (7 PM)
crontab -e
# Add: 0 19 * * * cd /path/to/fantasy5-predictor && python3 fantasy5_auto.py >> lottery.log 2>&1
```

#### Option B: Fully Automated
```bash
# Install Playwright
bash install_automated.sh

# Configure email in fantasy5_automated.py
nano fantasy5_automated.py

# Test
python3 fantasy5_automated.py

# Setup cron job
crontab -e
# Add: 0 19 * * * cd /path/to/fantasy5-predictor && python3 fantasy5_automated.py >> lottery_auto.log 2>&1
```

## 📖 Documentation

- **[LOTTERY_SETUP.md](LOTTERY_SETUP.md)** - Complete setup guide
- **[AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md)** - Version comparison
- **[MINIPC_DEPLOYMENT.md](MINIPC_DEPLOYMENT.md)** - Mini PC deployment
- **[UPDATE_LOTTERY_DATA.md](UPDATE_LOTTERY_DATA.md)** - Data update guide

## 📧 Email Configuration

Requires Gmail app password:
1. Go to https://myaccount.google.com/apppasswords
2. Generate password for "Mail"
3. Update in script configuration

## 🎯 How It Works

1. **Data Collection**: Downloads/loads California Fantasy 5 past results
2. **Statistical Analysis**:
   - Frequency analysis of all numbers
   - Gap analysis (overdue numbers)
   - Distribution balancing (odd/even, high/low)
3. **Prediction Generation**: Creates 3 number sets using different algorithms
4. **Email Delivery**: Sends formatted predictions with statistics

## ⚠️ Important Disclaimer

**This tool is for entertainment purposes only.** Lottery numbers are random and past results do not predict future outcomes. Your odds remain **1 in 575,757** regardless of which numbers you choose. Play responsibly!

## 📊 Statistics

Based on 50+ recent draws:
- Analyzes number frequency patterns
- Tracks gap between appearances
- Balances odd/even and high/low distributions
- Historical sum range analysis

## 🛠️ Technologies

- Python 3.11+
- Playwright (for browser automation)
- BeautifulSoup4 (for web scraping)
- SMTP (for email delivery)
- Cron (for scheduling)

## 📁 Project Structure

```
fantasy5-predictor/
├── fantasy5_auto.py              # Manual CSV version
├── fantasy5_automated.py         # Browser automation version
├── test_email.py                 # Email configuration tester
├── lottery_analysis.py           # Analysis script
├── requirements_lottery.txt      # Dependencies (manual)
├── requirements_automated.txt    # Dependencies (automated)
├── install_lottery_minipc.sh    # Installer (manual)
├── install_automated.sh         # Installer (automated)
├── update_lottery.sh            # CSV update helper
└── *.md                         # Documentation files
```

## 🔧 Troubleshooting

### Email not sending?
- Verify app password is correct
- Check firewall isn't blocking port 587
- Test with `python3 test_email.py`

### Browser automation failing?
- Website structure may have changed
- Use manual CSV version instead
- Check `debug_screenshot.png` for clues

### Dependencies not installing?
```bash
sudo apt-get update
sudo apt-get install python3-pip python3-requests python3-bs4
```

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Contributions welcome! Please open an issue or PR.

## 📮 Contact

For issues or questions, please open a GitHub issue.

---

**Made with ❤️ for lottery enthusiasts** 🍀

*Remember: Play responsibly and never spend more than you can afford to lose!*
