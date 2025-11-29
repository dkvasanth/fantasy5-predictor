#!/usr/bin/env python3
"""
Test email configuration before running the full lottery script
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# UPDATE THESE SETTINGS
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'vasanthishere@gmail.com'
SENDER_PASSWORD = 'hwnpwxydkmatjjnj'
RECIPIENT_EMAIL = 'dkvasanth@gmail.com'

def test_email():
    """Send a test email"""
    print("="*60)
    print("📧 Email Configuration Test")
    print("="*60)
    print(f"SMTP Server: {SMTP_SERVER}:{SMTP_PORT}")
    print(f"From: {SENDER_EMAIL}")
    print(f"To: {RECIPIENT_EMAIL}")
    print()

    try:
        # Create test message
        msg = MIMEMultipart()
        msg['Subject'] = '✅ Fantasy 5 Email Test - SUCCESS'
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL

        body = """
        <html>
          <body style="font-family: Arial, sans-serif; padding: 20px;">
            <div style="background: #4CAF50; color: white; padding: 20px; border-radius: 10px;">
              <h1>✅ Email Test Successful!</h1>
              <p>Your email configuration is working correctly.</p>
            </div>
            <div style="margin-top: 20px; padding: 15px; background: #f0f0f0; border-radius: 5px;">
              <h3>Configuration Details:</h3>
              <ul>
                <li><strong>SMTP Server:</strong> {}</li>
                <li><strong>Port:</strong> {}</li>
                <li><strong>Sender:</strong> {}</li>
                <li><strong>Recipient:</strong> {}</li>
              </ul>
            </div>
            <div style="margin-top: 20px;">
              <p>You're ready to run the Fantasy 5 auto-predictor!</p>
              <p style="color: #666; font-size: 12px;">
                Next step: Run <code>python3 fantasy5_auto.py</code>
              </p>
            </div>
          </body>
        </html>
        """.format(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, RECIPIENT_EMAIL)

        msg.attach(MIMEText(body, 'html'))

        # Send email
        print("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
            print("Starting TLS encryption...")
            server.starttls()

            print("Logging in...")
            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            print("Sending test email...")
            server.send_message(msg)

        print()
        print("="*60)
        print("✅ SUCCESS! Email sent successfully!")
        print("="*60)
        print()
        print("Check your inbox at:", RECIPIENT_EMAIL)
        print()
        print("Next steps:")
        print("1. Verify you received the test email")
        print("2. Update fantasy5_auto.py with same settings")
        print("3. Run: python3 fantasy5_auto.py")
        print()
        return True

    except smtplib.SMTPAuthenticationError:
        print()
        print("="*60)
        print("❌ AUTHENTICATION FAILED")
        print("="*60)
        print()
        print("Common causes:")
        print("1. Wrong email/password")
        print("2. Using regular password instead of app password")
        print("3. App passwords not enabled")
        print()
        print("For Gmail:")
        print("- Generate app password: https://myaccount.google.com/apppasswords")
        print("- Use the 16-character code (remove spaces)")
        print()
        return False

    except smtplib.SMTPException as e:
        print()
        print("="*60)
        print(f"❌ SMTP ERROR: {e}")
        print("="*60)
        print()
        print("Check your SMTP settings:")
        print(f"- Server: {SMTP_SERVER}")
        print(f"- Port: {SMTP_PORT}")
        print()
        return False

    except Exception as e:
        print()
        print("="*60)
        print(f"❌ ERROR: {e}")
        print("="*60)
        print()
        print("Possible issues:")
        print("- Internet connection")
        print("- Firewall blocking port", SMTP_PORT)
        print("- Invalid email address")
        print()
        return False

if __name__ == '__main__':
    # Check if settings were updated
    if SENDER_EMAIL == 'your_email@gmail.com':
        print()
        print("⚠️  WARNING: You need to update the email settings in this file!")
        print()
        print("Edit test_email.py and update:")
        print("  SENDER_EMAIL = 'your_actual_email@gmail.com'")
        print("  SENDER_PASSWORD = 'your_16_char_app_password'")
        print("  RECIPIENT_EMAIL = 'recipient@example.com'")
        print()
        exit(1)

    test_email()
