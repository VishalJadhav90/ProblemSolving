def breakWord(s, swords, pointer, result):
    if pointer >= len(s):
        result['total'] += 1
    subs = ""
    slot = 0
    while pointer < len(s):
        subs += s[pointer]
        pointer += 1
        if subs in swords:
            slot = slot + 1
            breakWord(s, swords, pointer, result)

result = {'total': 0}
s = "catsanddog"
swords = set(["cat", "cats", "and", "sand", "dog"])
breakWord(s, swords, 0, result)
print("result...", result)
