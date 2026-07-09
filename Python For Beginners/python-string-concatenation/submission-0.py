def concatenate(s1: str, s2: str) -> str:
    concat = s1+s2
    len_concat = len(concat)
    
    if len_concat > 10:
        return "Too long!"
    else:
        return concat
        
# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
