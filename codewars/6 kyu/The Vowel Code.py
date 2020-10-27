def encode(st):
    st.lower()
    print(st.maketrans("aeiou", "12345"))
    return st.translate(st.maketrans("aeiou", "12345"))

def decode(st):
    return st.translate(st.maketrans("12345", "aeiou"))

print(encode("hello"))
