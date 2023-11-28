def remove_char_at(s, n):
    if 0 <= n < len(s):
        result = s[:n] + s[n+1:]
        return result
    else:
        return s
