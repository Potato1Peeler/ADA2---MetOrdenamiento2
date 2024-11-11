class Shell:
    def ordenamientoDeShell(self, lista):
        lista = lista.copy()
        contadorSublistas = len(lista) // 2
        while contadorSublistas > 0:
            for posicionInicio in range(contadorSublistas):
                self.brechaOrdenamientoPorInsercion(lista, posicionInicio, contadorSublistas)
            print(f"Después del incremento de tamaño {contadorSublistas}, la lista es: {lista}")
            contadorSublistas = contadorSublistas // 2

        print("Lista ordenada con Shell Sort:", lista)

    def brechaOrdenamientoPorInsercion(self, unaLista, inicio, brecha):
        for i in range(inicio + brecha, len(unaLista), brecha):
            valorActual = unaLista[i]
            posicion = i
            while posicion >= brecha and unaLista[posicion - brecha] > valorActual:
                unaLista[posicion] = unaLista[posicion - brecha]
                posicion = posicion - brecha
            unaLista[posicion] = valorActual


class Quick:
    def ordenamientoRapido(self, lista):
        lista = lista.copy()
        self.ordenamientoRapidoAuxiliar(lista, 0, len(lista) - 1)
        print("Lista ordenada con Quick Sort:", lista)

    def ordenamientoRapidoAuxiliar(self, unaLista, primero, ultimo):
        if primero < ultimo:
            puntoDivision = self.particion(unaLista, primero, ultimo)
            self.ordenamientoRapidoAuxiliar(unaLista, primero, puntoDivision - 1)
            self.ordenamientoRapidoAuxiliar(unaLista, puntoDivision + 1, ultimo)

    def particion(self, lista, primero, ultimo):
        valorPivote = lista[primero]
        marcaIzq = primero + 1
        marcaDer = ultimo
        hecho = False
        while not hecho:
            while marcaIzq <= marcaDer and lista[marcaIzq] <= valorPivote:
                marcaIzq += 1
            while lista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
                marcaDer -= 1
            if marcaDer < marcaIzq:
                hecho = True
            else:
                lista[marcaIzq], lista[marcaDer] = lista[marcaDer], lista[marcaIzq]
        lista[primero], lista[marcaDer] = lista[marcaDer], lista[primero]
        print(f"Lista después de partición: {lista}")
        return marcaDer


class Radix:
    def counting_sort(self, lista, exp):
        n = len(lista)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = lista[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = lista[i] // exp
            output[count[index % 10] - 1] = lista[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            lista[i] = output[i]

    def radix_sort(self, lista):
        lista = lista.copy()
        max_num = max(lista)
        exp = 1
        while max_num // exp > 0:
            self.counting_sort(lista, exp)
            exp *= 10
            print(f"Lista después de ordenar por dígitos de orden {exp}: {lista}")
        print("Lista ordenada con Radix Sort:", lista)


class Heap:
    def construir_monticulo(self, lista):
        lista = lista.copy()
        N = len(lista) - 1
        for i in range(N // 2, -1, -1):
            self.heapify(lista, N, i)
        print(f"Lista construida como montículo: {lista}")
        self.heapSort(lista)

    def heapify(self, lista, N, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left <= N and lista[left] > lista[largest]:
            largest = left
        if right <= N and lista[right] > lista[largest]:
            largest = right
        if largest != i:
            lista[i], lista[largest] = lista[largest], lista[i]
            self.heapify(lista, N, largest)

    def heapSort(self, lista):
        N = len(lista) - 1
        for i in range(N, 0, -1):
            lista[0], lista[i] = lista[i], lista[0]
            self.heapify(lista, i - 1, 0)
            print(f"Lista después de intercambiar el primer elemento: {lista}")
        print(f"Lista ordenada con Heap Sort: {lista}")


def menu():
    tamaño = int(input("Ingresa el tamaño de la lista: "))
    lista = []
    for i in range(tamaño):
        num = int(input(f"Ingresa el número {i+1} de la lista: "))
        lista.append(num)

    listaopciones = [
        "1. Quicksort",
        "2. Shell Sort",
        "3. Radix Sort",
        "4. Heap Sort",
        "5. Salir"
    ]
    print("\n".join(listaopciones))

    while True:
        respuesta = int(input("Ingresa la opción que desees (1-4) o 5 para salir: "))
        if respuesta == 5:
            break
        elif respuesta == 1:
            quick = Quick()
            quick.ordenamientoRapido(lista)
        elif respuesta == 2:
            shell = Shell()
            shell.ordenamientoDeShell(lista)
        elif respuesta == 3:
            radix = Radix()
            radix.radix_sort(lista)
        elif respuesta == 4:
            heap = Heap()
            heap.construir_monticulo(lista)
        else:
            print("Opción no válida, intente de nuevo.")

menu()
