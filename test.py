def foo(to_add:list, item={}):
    for items in to_add:
        item[items] = items
    print(item)

foo(['one','two'])
foo(['three','four'])
