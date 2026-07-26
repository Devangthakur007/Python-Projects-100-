import datetime
import time
import sys

def set_alarm():
    print("=== ⏰ Python Alarm Clock ===")
    
    # Get target time from user
    alarm_time = input("Enter alarm time in 24-hour format (HH:MM:SS), e.g., 07:30:00: ").strip()
    
    # Validate user input format
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("❌ Invalid time format! Please use HH:MM:SS (24-hour clock).")
        return

    print(f"\n✅ Alarm set for {alarm_time}. Keep this window open!")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\rCurrent Time: {current_time}", end="", flush=True)
        
        if current_time == alarm_time:
            print("\n\n🔔 WAKE UP! ALARM IS RINGING! 🔔")
            # Plays system beep 5 times
            for _ in range(5):
                print("\a")  # System beep sound
                time.sleep(0.5)
            break
            
        time.sleep(1)

if __name__ == "__main__":
    set_alarm()