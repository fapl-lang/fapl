def is_blank_line(content):
    for character in content:
        if character != " ":
            return False
    return True