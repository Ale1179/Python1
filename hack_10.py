"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    
    replacements = {
        "O": "0",
        "I": "1",
        "A": "@"
    }
    for old, new in replacements.items():
        result = result.replace(old, new)
    
    result = list(result)
    return result  