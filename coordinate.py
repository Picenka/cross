# генерация вариантов завершения игры
import numpy as np
coordinate=[]

field = np.arange(100).reshape(10, 10)
diags = [field[::-1, :].diagonal(i) for i in range(-field.shape[0] + 1, field.shape[1])]
diags.extend(field.diagonal(i) for i in range(field.shape[1] - 1, -field.shape[0], -1))


for x in range (len(field)):
    coordinate.append(field[:, x].tolist())
    coordinate.append(field[x, :].tolist())
# отбрасываем короткие диагонали
for n in diags:
    if len(n.tolist())>=5:
        coordinate.append(n.tolist())





