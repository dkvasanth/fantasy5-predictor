#!/usr/bin/env python3
"""
Fantasy 5 Lottery Analysis - 3 Statistical Approaches
WARNING: This is for entertainment only. Lottery is random - past results don't predict future.
"""

import csv
from collections import Counter, defaultdict
import random

# Read the data
draws = []
with open('/Users/vasanth/Downloads/CA Fantasy 5 numbers from LotteryUSA.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Result']:
            numbers = [int(n.strip()) for n in row['Result'].split(',')]
            draws.append(numbers)

print(f"Analyzing {len(draws)} draws...\n")
print("="*80)

# Flatten all numbers for frequency analysis
all_numbers = [num for draw in draws for num in draw]
frequency = Counter(all_numbers)

print("\n📊 APPROACH 1: FREQUENCY ANALYSIS (Hot Numbers)")
print("-" * 80)
print("Strategy: Pick the most frequently appearing numbers")
print("\nTop 20 Most Frequent Numbers:")
for num, count in frequency.most_common(20):
    print(f"  {num:2d}: appeared {count:2d} times ({count/len(draws)*100:.1f}%)")

hot_numbers = [num for num, _ in frequency.most_common(10)]
prediction_1 = sorted(random.sample(hot_numbers, 5))
print(f"\n🎯 PREDICTION 1 (Hot Numbers): {prediction_1}")

print("\n" + "="*80)

# Gap Analysis - find overdue numbers
print("\n📈 APPROACH 2: GAP ANALYSIS (Overdue Numbers)")
print("-" * 80)
print("Strategy: Find numbers that haven't appeared recently")

last_seen = {}
for i, draw in enumerate(reversed(draws)):
    for num in draw:
        if num not in last_seen:
            last_seen[num] = i

# Find numbers that haven't appeared or appeared long ago
overdue = sorted([(num, gap) for num, gap in last_seen.items()], key=lambda x: x[1], reverse=True)

print("\nTop 15 Most Overdue Numbers:")
for num, gap in overdue[:15]:
    print(f"  {num:2d}: last seen {gap} draws ago")

# Check for numbers never seen
all_possible = set(range(1, 40))
never_seen = all_possible - set(all_numbers)
if never_seen:
    print(f"\n⚠️  Numbers NEVER appeared in these 50 draws: {sorted(never_seen)}")

overdue_numbers = [num for num, _ in overdue[:10]]
prediction_2 = sorted(random.sample(overdue_numbers, 5))
print(f"\n🎯 PREDICTION 2 (Overdue): {prediction_2}")

print("\n" + "="*80)

# Distribution Analysis - balanced approach
print("\n⚖️  APPROACH 3: DISTRIBUTION ANALYSIS (Balanced)")
print("-" * 80)
print("Strategy: Balance odd/even, high/low, and sum range")

# Analyze patterns
odd_count = sum(1 for num in all_numbers if num % 2 == 1)
even_count = len(all_numbers) - odd_count
low_count = sum(1 for num in all_numbers if num <= 19)
high_count = len(all_numbers) - low_count

print(f"\nHistorical Patterns:")
print(f"  Odd numbers:  {odd_count} ({odd_count/len(all_numbers)*100:.1f}%)")
print(f"  Even numbers: {even_count} ({even_count/len(all_numbers)*100:.1f}%)")
print(f"  Low (1-19):   {low_count} ({low_count/len(all_numbers)*100:.1f}%)")
print(f"  High (20-39): {high_count} ({high_count/len(all_numbers)*100:.1f}%)")

# Calculate sum ranges
sums = [sum(draw) for draw in draws]
avg_sum = sum(sums) / len(sums)
print(f"\n  Average sum of winning numbers: {avg_sum:.1f}")
print(f"  Sum range: {min(sums)} - {max(sums)}")

# Generate balanced prediction
# Aim for 3 odd, 2 even OR 2 odd, 3 even
# Aim for 2-3 low, 2-3 high
# Target sum around 100

def generate_balanced():
    while True:
        nums = random.sample(range(1, 40), 5)
        odd = sum(1 for n in nums if n % 2 == 1)
        low = sum(1 for n in nums if n <= 19)
        total = sum(nums)

        # Check balance criteria
        if odd in [2, 3] and low in [2, 3] and 80 <= total <= 120:
            return sorted(nums)

prediction_3 = generate_balanced()
odd_3 = sum(1 for n in prediction_3 if n % 2 == 1)
low_3 = sum(1 for n in prediction_3 if n <= 19)
print(f"\n🎯 PREDICTION 3 (Balanced): {prediction_3}")
print(f"   Odd/Even: {odd_3}/{5-odd_3}, Low/High: {low_3}/{5-low_3}, Sum: {sum(prediction_3)}")

print("\n" + "="*80)
print("\n🎲 SUMMARY - YOUR 3 PREDICTIONS")
print("="*80)
print(f"1. Hot Numbers (Frequency):  {prediction_1}")
print(f"2. Overdue (Gap Analysis):   {prediction_2}")
print(f"3. Balanced (Distribution):  {prediction_3}")
print("\n⚠️  REMINDER: These predictions are based on statistical patterns in random data.")
print("    Your odds remain 1 in 575,757 regardless of which numbers you choose!")
print("="*80)
