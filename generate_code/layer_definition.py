#/usr/bin/env python
layers = range(0,12)
for i in layers:
    layers[i] = range(0,8)
    for j in layers[i]:
        layers[i][j] = range(0,5)
        for k in layers[i][j]:
            layers[i][j][k] = (0,0)
            # layers[i][j][k] = i * 8 * 5 + j * 5 + k

#test purpose
print layers
