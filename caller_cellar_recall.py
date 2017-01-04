with open('words.txt', 'r') as f:
    l = {x: ''.join(sorted(x)) for x in f.read().split('\n')}
out = {}
for key in l:
    if list(l.values()).count(l[key]) > 1 and l[key] not in out:
        for kv in l:
            if l[kv] == l[key]:
                if l[kv] in out:
                    out[l[kv]].append(kv)
                else:
                    out[l[kv]] = [kv]
for key in out:
    print(' '.join(sorted(out[key])))
