def mohasebe(matrix):

    tedad = len(matrix)

    if tedad == 1:
        return matrix[0][0]

    if tedad == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    natije = 0

    for sotun in range(tedad):

        if matrix[0][sotun] == 0:
            continue

        matrix_jadid = []

        for radif in range(1, tedad):

            radif_jadid = []

            for s in range(tedad):

                if s != sotun:
                    radif_jadid.append(matrix[radif][s])

            matrix_jadid.append(radif_jadid)

        alamat = (-1) ** sotun

        natije += alamat * matrix[0][sotun] * mohasebe(matrix_jadid)
    return natije
tedad = 10
matrix = []
print("Enter 10x10 matrix:")
for i in range(tedad):

    while True:

        radif = list(map(float, input().split()))

        if len(radif) == tedad:
            matrix.append(radif)
            break

        print("Please enter exactly 10 numbers!")
print("Determinant =", mohasebe(matrix))