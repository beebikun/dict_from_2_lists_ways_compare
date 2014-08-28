import timeit


def tests():
    keys = range(100)
    values = range(50)

    def m1():
        return dict(map(None, keys, values))

    def m2():
        l = len(values)
        return dict([(k, values[i] if i < l else None)
                     for i, k in enumerate(keys)])

    def m2_1():
        values.extend([None]*(len(keys)-len(values)))
        return dict([(k, values[i]) for i, k in enumerate(keys)])

    def m3():
        l = len(values)
        return {k: values[i] if i < l else None for i, k in enumerate(keys)}

    def m3_1():
        values.extend([None]*(len(keys)-len(values)))
        return {k: values[i] for i, k in enumerate(keys)}

    def m4():
        d = dict()
        l = len(values)
        for i, k in enumerate(keys):
            d[k] = values[i] if i < l else None
        return d

    def m4_1():
        values.extend([None]*(len(keys)-len(values)))
        d = dict()
        for i, k in enumerate(keys):
            d[k] = values[i]
        return d

    print '1: ', timeit.timeit(m1)
    print '2: ', timeit.timeit(m2)
    print '2_1: ', timeit.timeit(m2_1)
    print '3: ', timeit.timeit(m3)
    print '3_1: ', timeit.timeit(m3_1)
    print '4: ', timeit.timeit(m4)
    print '4_1: ', timeit.timeit(m4_1)

tests()
