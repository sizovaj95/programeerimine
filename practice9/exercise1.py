list_ = [1,2,3,4,5]

print(f"List before sorting: {list_}")

need_swap = True
while need_swap:
    need_swap = False
    for i in range(len(list_)):
        if i != len(list_) - 1:
            current = list_[i]
            next_ = list_[i+1]
            if current < next_:
                need_swap = True
                list_[i] = next_
                list_[i+1] = current


print(f"List after sorting: {list_}")
