items = [3, 4, 1, 2, 6, 5]
print(items)

# Insersion Sort
for i in range(1, len(items)):
    curr_val = items[i]
    if curr_val > items[i-1]:
        continue
    else:
        changed = True
        for l in range(i-1, -1, -1):
            if curr_val <= items[l]:
                continue
            else:
                del items[i]
                items.insert(l+1, curr_val)
                changed = False
                break
        if changed:
            del items[i]
            items.insert(0, curr_val)

print(items)
