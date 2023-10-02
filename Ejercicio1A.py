def mejor_corte(S, A, ΔM):
    mejor_par = None
    mejor_ganancia = 0

    for a in A:
        valores_A = sacarRepetidosMasDeDos(S[a]) #Esta funcion le saca los atributos que se repitan más de 2 veces.

        valores_A.sort()

        for i in range(len(valores_unicos) - 1):
            c = (valores_A[i] + valores_A[i+1]) / 2
            S_menor = S[S[a] <= c]
            S_mayor = S[S[a] > c]

            ganancia = ΔM(S, S_menor, S_mayor)  # Calcular la ganancia usando la función ΔM

            if ganancia > mejor_ganancia:
                mejor_ganancia = ganancia
                mejor_par = (atributo, corte)

    return mejor_par
