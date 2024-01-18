with open("Games Played.txt", "r", encoding='utf-8') as fh:
    new_text = []
    for line in fh:
        line.strip()
        if not line.startswith(":"):
            new_text.append(line)
            
text = "\n".join(new_text)
print(text)

with open("Games Played.txt", "w", encoding='utf-8') as fh:
    fh.write(text)
        