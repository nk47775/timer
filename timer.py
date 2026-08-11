import time

print("⏱️ टाइमर टूल")
try:
    sec = int(input("कितने सेकंड का टाइमर लगाना है? (उदा. 60): "))
    while sec:
        m, s = divmod(sec, 60)
        print(f"⏳ बचा हुआ समय: {m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        sec -= 1
    print("\n⏰ समय समाप्त! (Time's up)")
except ValueError:
    print("\n❌ कृपया केवल नंबर डालें।")
  
