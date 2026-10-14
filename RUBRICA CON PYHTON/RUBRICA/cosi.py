#pascal


def triangle(n):
    # Primo caso base
    if n == 0:
        return []
    # Secondo caso base
    elif n == 1:
        return [ [1] ]
    # Caso ricorsivo
    else:
        # Costruisci la tua riga del triangolo
        new_row = [1]
        # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        result = triangle(n-1)
        last_row = result[-1] # [1, 3, 3, 1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row.appen