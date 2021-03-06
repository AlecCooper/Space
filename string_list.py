def merge(original, add, remove):

    results = (set(original) | set(add)) - set(remove)

    results = list(results)

    results.sort(key = lambda x: (len(x), x), reverse=True)

    return results


# Test the function! 
print(merge(
    ["one", "two", "three"], 
    ["one", "two", "five", "six"],
    ["two", "five"]))
