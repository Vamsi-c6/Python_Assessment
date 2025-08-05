print("📌 Q4: .txt Files in Current Directory")
txt_files = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]

if txt_files:
    for file in txt_files:
        print(file)
else:
    print("No .txt files found.")
print()
