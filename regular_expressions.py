import re

# %%
assert re.findall("a", "a") == ["a"]
# + is a special character. So it needs to be prefixed with \.
assert re.findall(r"\+", "abc+def") == ["+"]

# %%
# [] denotes character class. It matches any set inside the brackets
# - is a range expression. Ex: a-d indicates a,b,c,d; 0-4 indicates 0,1,2,3,4
assert "".join(re.findall(r"[a-z]", "hello")) == "hello"
# If [] starts with ^, it acts as invert of. It matches with anything not in []
assert "".join(re.findall(r"[^a-z]", "iphone 10")) == " 10"

# %%
assert re.match("four|foor", "ffour") is None
