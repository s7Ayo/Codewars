def to_camel_case(text):
    text=[str(f) for f in str(text)]
    for i in  range(len(text)):
        if text[i] == '-' or text[i] == '_':
            text[i+1]=text[i+1].upper()
    text = [text.replace('-','') for text in text]
    text = [text.replace('_','') for text in text]
    return("".join(text))
