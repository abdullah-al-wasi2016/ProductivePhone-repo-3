
import time
def boot():
    print("[Boot] start...")
    time.sleep(2)
    print("""System logs:
    [Components] initializing...
    [Boot] starting...
    """)
    time.sleep(2)

if __name__ == "__main__":
    boot()