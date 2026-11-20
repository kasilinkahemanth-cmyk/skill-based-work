text = input("Enter text to compress: ")
if text == "":
    print("Empty text")
else:
    encoded = ""
    i = 0
    while i < len(text):
        count = 1
        while i + count < len(text) and text[i] == text[i + count]:
            count = count + 1
        encoded = encoded + text[i] + str(count)
        i = i + count
    print("Original text:", text)
    print("Encoded text:", encoded)
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))
    if len(encoded) >= len(text):
        print("Encoding is not beneficial")
    else:
        print("Encoding saves space")