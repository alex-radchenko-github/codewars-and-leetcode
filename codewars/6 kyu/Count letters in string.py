import collections
def string_letter_count(s):
    rez = ''
    s1 = sorted(set("".join(s.split()).lower()))
    for i in s1:
        if i.isalpha():
            rez += i + str(s.lower().count(i))
        else:
            continue
    return rez

print(string_letter_count("The quick brown fox jumps over the lazy dog."))#, "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z")
print(string_letter_count("The time you enjoy wasting is not wasted time."))#, "2a1d5e1g1h4i1j2m3n3o3s6t1u2w2y")
print(string_letter_count("./4592#{}()"))#, "")