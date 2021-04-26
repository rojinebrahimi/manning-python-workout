def url_encode(url):
    encoded_url = []
    for char in url:
        if char.isalnum():
           encoded_url.append(char)
        else:
            asc_char = ord(char)
            encoded_url.append(f"%{asc_char}")
    return "".join(encoded_url)


print(url_encode('@solutions/*of#Manning_Book/!exercises/(by rojin)'))