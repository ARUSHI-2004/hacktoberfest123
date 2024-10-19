function RabinKarp(text, pattern):
    m = length(pattern)
    n = length(text)
    h_pattern = hash(pattern)
    h_text = hash(text[0..m-1])
    
    for i from 0 to n - m:
        if h_text == h_pattern:
            if text[i..i+m-1] == pattern:
                return i
        if i < n - m:
            h_text = update_hash(h_text, text[i], text[i + m])
    return "not found"
