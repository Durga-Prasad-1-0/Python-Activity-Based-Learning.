text = input("Enter a string: ")

compressed = ""
i = 0

while i < len(text):
    count = 1

    while i + count < len(text) and text[i] == text[i + count]:
        count += 1

    compressed += text[i] + str(count)
    i += count

print("Original text:", text)
print("Compressed text:", compressed)
print("Original length:", len(text))
print("Compressed length:", len(compressed))

if len(compressed) < len(text):
    print("Compression is beneficial")
else:
    print("Compression is not beneficial")
