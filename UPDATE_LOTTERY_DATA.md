# How to Update Lottery Data

The website uses JavaScript to generate CSV downloads, so we can't automate it directly. Here's the simple manual process:

## 📥 Quick Update (Once a Week or Month)

### Step 1: Download Latest Data
1. Go to: https://www.lotteryusa.com/california/fantasy-5/year
2. Click the **"CSV"** button (above the results table)
3. Save the file (usually downloads as `california-fantasy-5.csv`)

### Step 2: Upload to Mini PC
```bash
# From your Mac:
scp ~/Downloads/california-fantasy-5.csv dkvasanth@10.0.0.21:~/lottery/fantasy5_data.csv
```

### Step 3: Done!
The lottery app will automatically use the updated data for next predictions.

---

## 🤖 Semi-Automated Alternative

Create an alias for quick updates:

```bash
# Add to your Mac's ~/.zshrc or ~/.bashrc:
alias update-lottery="scp ~/Downloads/california-fantasy-5.csv dkvasanth@10.0.0.21:~/lottery/fantasy5_data.csv && echo '✅ Lottery data updated!'"

# Then just run:
update-lottery
```

---

## 📊 How Often to Update?

- **Daily:** For most current analysis (download after each draw)
- **Weekly:** Sufficient for pattern analysis
- **Monthly:** Acceptable for long-term trends

**Current data:** 50 draws (Oct-Nov 2025)

---

## 🔄 Full Automation Option (Advanced)

If you want full automation, we'd need to use browser automation (Selenium/Playwright):

**Pros:**
- Fully automated, no manual steps
- Can run on schedule

**Cons:**
- Requires Chrome/Firefox installation on mini PC
- More complex setup
- Higher resource usage
- May break if website changes

**Let me know if you want me to create the browser automation version!**

---

## ✅ Current Setup Works Great

The current setup:
- ✅ Uses cached CSV data (50 draws)
- ✅ Generates daily predictions
- ✅ Emails results automatically
- ✅ Updates needed only occasionally

You can update the CSV file whenever you want fresh data, but the current 50 draws are sufficient for accurate statistical analysis.
