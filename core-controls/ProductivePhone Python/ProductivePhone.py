import pyaudio
import wave
import serial
import webbrowser
import random
import openai
import pyttsx3
import time
import dotenv
import os
import cv2

# Introduction
print("===== ProductivePhone MySimpleOS M0 ====")


# Functions
class ProductivePhone:
    def call_app(self, name, number):
  
        contact_list = []
        contact_list.append(name)
        contact_list.append(number)
        print(contact_list)

    
        p = pyaudio.PyAudio()
        stream = p.open(
            rate=44100,
            channels=1, 
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=1024
        )

        print("* Call record started.")
        frames = []
        for i in range(int(44100 * 10 / 1024)):
            data = stream.read(1024)
            frames.append(data)
        
        print("* Call record ended.")
        
        wf = wave.open('output.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        # Call signal to antenna tower
        try:
            ser = serial.Serial(port='/dev/cu.usbserial-1420', baudrate=9600, timeout=1)

            def send_at(command, delay=1):
                ser.write((command + '\r\n').encode())
                time.sleep(delay)
                response = ser.read_all().decode(errors='ignore')
                print(">>", command)
                print(response)
                return response

            send_at(f"ATD{number};", 2)  # dial
            time.sleep(5)
            send_at("ATH", 1)  # hang up
            ser.close()
            print("✅ Call signal sent to GSM module.")
        except Exception as e:
            print("⚠️ GSM module error:", e)

    
    def quran_app(self, quran="https://quran.com"):
        try:
            open_quran = webbrowser.get("safari")
            open_quran.open(quran)
        except webbrowser.Error:
            print("Sorry.")
    
    def game(self, number, secret = random.randint(1, 100)):
        self.number = number
        self.secret = secret

        if number != secret:
            print("Ooops.")
    
    def tts(self, text):
        engine = pyttsx3.init()
        pyttsx3.speak(text)
        engine.runAndWait()
    
    def gpt(self, prompt):
        print("\n🤖 Connecting to GPT...")
        dotenv.load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            print("⚠️ OPENAI_API_KEY missing in .env file.")
            return

        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
            print("GPT:", reply)
            return reply
        except Exception as e:
            print("❌ GPT Error:", e)

    
    def video_player(self, video_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Video failed.")
            return
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Video finished.")
                break
            cv2.imshow("Productive Video Player", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                print("Stopped.")
        
        cap.release()
        cv2.destroyAllWindows()
    
    def browser(self, where_to_go):
        try:
            safari = webbrowser.get("safari")
            safari.open(where_to_go)
        except webbrowser.Error:
            print("Ooops.")



def main():
    while True:
        print("Menu: \n1. Call App\n2. Quran App\n3. Game App\n4. TTS App\n5. GPT App\n6. Video Player\n7. Browser App")
        choice = str(input("Enter your choice (1-7):  "))
        phone = ProductivePhone()
        if choice == '1':
            name = str(input("Enter name of the contact:  "))
            number = str(input("Enter the mobile no.:  "))
            phone.call_app(name, number)
        elif choice == '2':
            phone.quran_app()
        elif choice == '3':
            phone.game()
        elif choice == '4':
            text = str(input("Enter text:  "))
            phone.tts(text)
        elif choice == '5':
            prompt = str(input("Enter prompt:  "))
            phone.gpt(prompt)
        elif choice == '6':
            video = str(input("Enter a video:  "))
            constructed_name = f"{video}.mp4"
            phone.video_player(constructed_name)
        elif choice == '7':
            browser = str(input("Enter a browser name:  "))
            constructed_name_browser = f"{browser}.com"
            phone.browser(constructed_name_browser)

        re_operation = str(input("Wanna do operations again? (yes/no):  "))
        if re_operation.lower() == "no":
            print("== ProductivePhone is leaving ==")
            time.sleep(2)
            print("Closed operation.")
            break

if __name__ == "__main__":
    main()

# *This project is encrypted. This file is encrypted. No change without the permission of writer. * #
# *Or, the copyrights can break even if police step isn't taken.* #
