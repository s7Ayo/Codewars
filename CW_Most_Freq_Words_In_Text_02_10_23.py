import re

def top_3_words(text):
    text = text.lower()
    text = re.sub(r"[^a-z']",' ',text)
    words = text.split()
    highestcount = {}
    for word in words:
        if word in highestcount:
            highestcount[word]+=1
        else:
            highestcount[word] = 1
    sorted_words = sorted(highestcount.items(), key=lambda x: x[1], reverse=True)

    print(sorted_words)
    top3 = sorted_words[:3]
    return

top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack.""")