#!/usr/bin/env python3
"""
Fantasy 5 Lottery Auto-Predictor with Email Notifications
Scrapes data from LotteryUSA and emails daily predictions
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from collections import Counter
import random
import os

# Configuration
CONFIG = {
    'data_file': 'fantasy5_history.json',
    'email': {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'sender_email': 'vasanthishere@gmail.com',
        'sender_password': 'hwnpwxydkmatjjnj',
        'recipient_email': 'dkvasanth@gmail.com',
    }
}

class Fantasy5Predictor:
    def __init__(self):
        self.draws = []

    def load_from_csv(self, csv_path='fantasy5_data.csv'):
        """Load lottery data from CSV file"""
        if not os.path.exists(csv_path):
            print(f"⚠️  CSV file not found: {csv_path}")
            return False

        try:
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('Result'):
                        try:
                            numbers = [int(n.strip()) for n in row['Result'].split(',')]
                            if len(numbers) == 5:
                                self.draws.append({
                                    'date': row.get('Date', ''),
                                    'numbers': numbers
                                })
                        except:
                            continue

            if self.draws:
                print(f"✅ Loaded {len(self.draws)} draws from CSV")
                self.save_data()
                return True
            return False

        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            return False

    def scrape_data(self, url='https://www.lotteryusa.com/california/fantasy-5/year'):
        """Scrape lottery data from LotteryUSA"""
        print(f"📥 Fetching data from {url}...")

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the results table
            draws = []
            # Look for table rows with lottery results
            rows = soup.find_all('tr', class_=lambda x: x and ('result' in x.lower() if x else False))

            if not rows:
                # Try alternative parsing - look for any table with numbers
                tables = soup.find_all('table')
                for table in tables:
                    for row in table.find_all('tr')[1:]:  # Skip header
                        cells = row.find_all('td')
                        if len(cells) >= 2:
                            date_cell = cells[0].get_text(strip=True)
                            numbers_cell = cells[1].get_text(strip=True)

                            # Try to parse numbers
                            try:
                                numbers = [int(n.strip()) for n in numbers_cell.replace(',', ' ').split() if n.strip().isdigit()]
                                if len(numbers) == 5 and all(1 <= n <= 39 for n in numbers):
                                    draws.append({
                                        'date': date_cell,
                                        'numbers': numbers
                                    })
                            except:
                                continue

            if draws:
                print(f"✅ Scraped {len(draws)} draws")
                self.draws = draws
                self.save_data()
                return True
            else:
                print("⚠️  No data found. Using cached data if available.")
                return self.load_data()

        except Exception as e:
            print(f"❌ Error scraping: {e}")
            return self.load_data()

    def save_data(self):
        """Save draws to JSON file"""
        with open(CONFIG['data_file'], 'w') as f:
            json.dump({
                'last_updated': datetime.now().isoformat(),
                'draws': self.draws
            }, f, indent=2)
        print(f"💾 Saved {len(self.draws)} draws to {CONFIG['data_file']}")

    def load_data(self):
        """Load draws from JSON file"""
        if os.path.exists(CONFIG['data_file']):
            with open(CONFIG['data_file'], 'r') as f:
                data = json.load(f)
                self.draws = data['draws']
                print(f"📂 Loaded {len(self.draws)} draws from cache")
                return True
        return False

    def analyze_and_predict(self):
        """Run 3 prediction algorithms"""
        if not self.draws:
            print("❌ No data available for analysis")
            return None

        all_numbers = [num for draw in self.draws for num in draw['numbers']]
        frequency = Counter(all_numbers)

        # Algorithm 1: Hot Numbers (Frequency)
        hot_numbers = [num for num, _ in frequency.most_common(10)]
        prediction_1 = sorted(random.sample(hot_numbers, 5))

        # Algorithm 2: Overdue Numbers (Gap Analysis)
        last_seen = {}
        for i, draw in enumerate(reversed(self.draws)):
            for num in draw['numbers']:
                if num not in last_seen:
                    last_seen[num] = i

        overdue = sorted([(num, gap) for num, gap in last_seen.items()],
                        key=lambda x: x[1], reverse=True)
        overdue_numbers = [num for num, _ in overdue[:10]]
        prediction_2 = sorted(random.sample(overdue_numbers, 5))

        # Algorithm 3: Balanced Distribution
        def generate_balanced():
            for _ in range(100):  # Max attempts
                nums = random.sample(range(1, 40), 5)
                odd = sum(1 for n in nums if n % 2 == 1)
                low = sum(1 for n in nums if n <= 19)
                total = sum(nums)
                if odd in [2, 3] and low in [2, 3] and 80 <= total <= 120:
                    return sorted(nums)
            return sorted(random.sample(range(1, 40), 5))

        prediction_3 = generate_balanced()

        # Compile statistics
        stats = {
            'total_draws': len(self.draws),
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'top_5_hot': [f"{num} ({count}x)" for num, count in frequency.most_common(5)],
            'top_5_overdue': [f"{num} ({gap} draws)" for num, gap in overdue[:5]],
            'predictions': {
                'hot': prediction_1,
                'overdue': prediction_2,
                'balanced': prediction_3
            }
        }

        return stats

    def send_email(self, stats):
        """Send email with predictions"""
        if not stats:
            print("❌ No stats to send")
            return False

        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"🎰 Fantasy 5 Daily Predictions - {datetime.now().strftime('%B %d, %Y')}"
            msg['From'] = CONFIG['email']['sender_email']
            msg['To'] = CONFIG['email']['recipient_email']

            # HTML email body
            html = f"""
            <html>
              <head>
                <style>
                  body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                  .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                           color: white; padding: 20px; text-align: center; border-radius: 10px; }}
                  .prediction {{ background: #f8f9fa; padding: 15px; margin: 15px 0;
                               border-left: 4px solid #667eea; border-radius: 5px; }}
                  .numbers {{ font-size: 24px; font-weight: bold; color: #667eea;
                            letter-spacing: 3px; margin: 10px 0; }}
                  .stats {{ background: #e9ecef; padding: 10px; border-radius: 5px;
                          margin: 10px 0; font-size: 14px; }}
                  .warning {{ background: #fff3cd; border-left: 4px solid #ffc107;
                            padding: 10px; margin: 15px 0; }}
                  .footer {{ text-align: center; color: #6c757d; font-size: 12px;
                           margin-top: 30px; padding-top: 20px; border-top: 1px solid #dee2e6; }}
                </style>
              </head>
              <body>
                <div class="header">
                  <h1>🎰 California Fantasy 5 Daily Predictions</h1>
                  <p>{datetime.now().strftime('%A, %B %d, %Y')}</p>
                </div>

                <div style="padding: 20px;">
                  <h2>Your 3 Number Sets for Today:</h2>

                  <div class="prediction">
                    <h3>🔥 Prediction #1: Hot Numbers (Frequency)</h3>
                    <div class="numbers">{' - '.join(map(str, stats['predictions']['hot']))}</div>
                    <p><em>Based on most frequently appearing numbers</em></p>
                  </div>

                  <div class="prediction">
                    <h3>⏰ Prediction #2: Overdue Numbers (Gap Analysis)</h3>
                    <div class="numbers">{' - '.join(map(str, stats['predictions']['overdue']))}</div>
                    <p><em>Based on numbers that haven't appeared recently</em></p>
                  </div>

                  <div class="prediction">
                    <h3>⚖️ Prediction #3: Balanced Distribution</h3>
                    <div class="numbers">{' - '.join(map(str, stats['predictions']['balanced']))}</div>
                    <p><em>Optimized balance of odd/even and high/low numbers</em></p>
                  </div>

                  <div class="stats">
                    <h3>📊 Statistics</h3>
                    <p><strong>Analyzed:</strong> {stats['total_draws']} recent draws</p>
                    <p><strong>Hottest Numbers:</strong> {', '.join(stats['top_5_hot'])}</p>
                    <p><strong>Most Overdue:</strong> {', '.join(stats['top_5_overdue'])}</p>
                    <p><strong>Last Updated:</strong> {stats['last_updated']}</p>
                  </div>

                  <div class="warning">
                    <p><strong>⚠️ Important Reminder:</strong></p>
                    <p>These predictions are based on statistical analysis of random data and
                    <strong>will NOT improve your odds of winning</strong>. Each lottery draw is
                    independent and random. Your probability remains 1 in 575,757 regardless of
                    which numbers you choose. Play responsibly!</p>
                  </div>

                  <div style="text-align: center; margin: 30px 0;">
                    <p>🍀 Good Luck! 🍀</p>
                    <p><a href="https://www.calottery.com/en/draw-games/fantasy-5">
                       View Official Results →</a></p>
                  </div>
                </div>

                <div class="footer">
                  <p>Generated by Fantasy 5 Auto-Predictor</p>
                  <p>Drawing time: Daily at 6:30 PM PT</p>
                </div>
              </body>
            </html>
            """

            msg.attach(MIMEText(html, 'html'))

            # Send email
            print(f"📧 Sending email to {CONFIG['email']['recipient_email']}...")
            with smtplib.SMTP(CONFIG['email']['smtp_server'], CONFIG['email']['smtp_port']) as server:
                server.starttls()
                server.login(CONFIG['email']['sender_email'], CONFIG['email']['sender_password'])
                server.send_message(msg)

            print("✅ Email sent successfully!")
            return True

        except Exception as e:
            print(f"❌ Error sending email: {e}")
            return False

def main():
    """Main execution"""
    print("="*80)
    print("🎰 Fantasy 5 Auto-Predictor")
    print("="*80)

    predictor = Fantasy5Predictor()

    # Try CSV first, then web scraping, then cached data
    if not predictor.load_from_csv():
        print("📡 CSV not found, trying web scraping...")
        if not predictor.scrape_data():
            print("⚠️  Web scraping failed, trying cached data...")
            if not predictor.load_data():
                print("❌ No data available. Exiting.")
                return

    # Generate predictions
    stats = predictor.analyze_and_predict()

    if stats:
        print("\n" + "="*80)
        print("🎯 TODAY'S PREDICTIONS")
        print("="*80)
        print(f"1. Hot Numbers:    {stats['predictions']['hot']}")
        print(f"2. Overdue:        {stats['predictions']['overdue']}")
        print(f"3. Balanced:       {stats['predictions']['balanced']}")
        print("="*80)

        # Send email
        predictor.send_email(stats)

    print("\n✅ Done!")

if __name__ == '__main__':
    main()
