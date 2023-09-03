import RPi.GPIO as GPIO
import time

# Set mode GPIO (BCM atau BOARD)
GPIO.setmode(GPIO.BCM)

# Tentukan pin GPIO yang akan digunakan
pin_relay = 17

# Konfigurasi pin sebagai OUTPUT
GPIO.setup(pin_relay, GPIO.OUT)

try:
    # Aktifkan relay (aktifkan perangkat yang terhubung ke relay)
    GPIO.output(pin_relay, GPIO.HIGH)
    print("Relay telah dinyalakan")
    
    # Tunggu beberapa detik (misalnya, 5 detik)
    time.sleep(5)
    
    # Matikan relay (nonaktifkan perangkat yang terhubung ke relay)
    GPIO.output(pin_relay, GPIO.LOW)
    print("Relay telah dimatikan")

except KeyboardInterrupt:
    print("Proses dihentikan oleh pengguna")

finally:
    # Matikan relay dan bersihkan pengaturan GPIO
    GPIO.output(pin_relay, GPIO.LOW)
    GPIO.cleanup()

