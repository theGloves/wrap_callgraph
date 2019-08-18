def get_pkg_name(path):
    if path is None or not isinstance(path, str):
        return ""
    if "/" in path:
        return path.split("/")[-1]
    return path


def match_pkg(s, pattern):
    pattern_list = []
    if not isinstance(pattern, list):
        pattern_list.append(pattern)
    else:
        pattern_list += pattern
        
    for pattern in pattern_list:
        if s.find(pattern) != -1:
            return True
    return False