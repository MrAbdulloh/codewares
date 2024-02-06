def row_weights(array):
    # xx = []
    # x = []
    # for i, v in enumerate(array):
    #     if i % 2 == 0:
    #         xx.append(v)
    #     else:
    #         x.append(v)
    # return [sum(xx), sum(x)]
    ## 2 method
    return sum(array[::2]), sum(array[1::2])


print(row_weights([0, 0]))
