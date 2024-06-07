## Laberinto de Tuberías

### Parte 1
Juan, un estudiante de ingeniería mecánica, recibió una llamada urgente de su profesor sobre un problema crítico en el laberinto de tuberías del laboratorio de hidráulica. Había una caída de presión que indicaba un ciclo de flujo problemático.

Ayuda a Juan a encontrar el ciclo de flujo problemático:

Conoces que todo el campo está lleno de tuberías dispuestas en una cuadrícula bidimensional:

  - |  : **tubería vertical** (conecta norte-sur).
  - \- : **tubería horizontal** (conecta este-oeste).
  - L : **arco de 90 grados** (conecta norte-este).
  - J : **arco de 90 grados** (conecta norte-oeste).
  - 7 : **arco de 90 grados** (conecta sur-oeste).
  - F : **arco de 90 grados** (conecta sur-este).
  - .  : **tierra**; no hay tubería.
  - S : **posición inicial de Juan**; hay una tubería pero no se muestra su forma.

Aquí hay un ejemplo de un ciclo cuadrado de tuberías:

```
. . . . .
. F - 7 .
. | . | .
. L - J .
. . . . .
```

Si el Juan entró en la esquina noroeste:

```
. . . . .
. S - 7 .
. | . | .
. L - J .
. . . . .
```
Aquí hay otro ciclo más complejo:

```
. . F 7 .
. F J | .
S J . L 7
| F - - J
L J . . .
```
Tras mucho análisis, Juan se dio cuenta de que **la falla se encuentra en el lugar más lejano alcanzable comenzando en S y siguiendo el camino del laberinto**.

```
. . . . . 
. 0 1 2 . 
. 1 . 3 . 
. 2 3 4 .
. . . . . 
```

El punto más alejado es **4** pasos. 

En el ciclo más complejo:

```
. . 4 5 .
. 2 3 6 .
0 1 . 7 8
1 4 5 6 7
2 3 . . .
```

**¿Cuántos pasos toma llegar desde S al punto más lejano?**

### Parte 2 
el Juan llega rápidamente al punto más alejado del ciclo, pero la falla no se encontraba ahí. Por los sonidos que escucha, ¿quizás esté dentro del área delimitada por el ciclo?

Para determinar si vale la pena dedicar a buscar una falla así, **deberías calcular cuántos componentes están contenidos dentro del ciclo.** Por ejemplo:

```
. . . . . . . . . . .
. S - - - - - - - 7 .
. | F - - - - - 7 | .
. | | . . . . . | | .
. | | . . . . . | | .
. | L - 7 . F - J | .
. | . . | . | . . | .
. L - - J . L - - J .
. . . . . . . . . . .
```
El ciclo anterior encierra apenas cuatro componentes: los dos pares de **.** en el suroeste y sureste (marcados como **1** abajo). Las componentes **.** centrales (marcadas como **0** abajo) no están dentro del ciclo. Aquí está el mismo ciclo nuevamente con esas regiones marcadas:
```
. . . . . . . . . . .
. S - - - - - - - 7 .
. | F - - - - - 7 | .
. | | 0 0 0 0 0 | | .
. | | 0 0 0 0 0 | | .
. | L - 7 0 F - J | .
. | 1 1 | 0 | 1 1 | .
. L - - J 0 L - - J .
. . . . . 0 . . . . .
```
De hecho, ni siquiera necesita haber un camino completo de componentes hacia afuera para que cuenten como fuera del ciclo: ¡también está permitido deslizarse entre las tuberías! Aquí, **1** todavía está dentro del ciclo y **0** todavía está fuera del ciclo:
```
. . . . . . . . . .
. S - - - - - - 7 .
. | F - - - - 7 | .
. | | 0 0 0 0 | | .
. | | 0 0 0 0 | | .
. | L - 7 F - J | .
. | 1 1 | | 1 1 | .
. L - - J L - - J .
. . . . . . . . . .
```
>En ambos ejemplos anteriores, **4** componentes están encerradas por el ciclo.

Aquí tienes un ejemplo más grande:
```
. F - - - - 7 F 7 F 7 F 7 F - 7 . . . .
. | F - - 7 | | | | | | | | F J . . . .
. | | . F J | | | | | | | | L 7 . . . .
F J L 7 L 7 L J L J | | L J . L - 7 . .
L - - J . L 7 . . . L J S 7 F - 7 L 7 .
. . . . F - J . . F 7 F J | L 7 L 7 L 7
. . . . L 7 . F 7 | | L 7 | . L 7 L 7 |
. . . . . | F J L J | F J | F 7 | . L J
. . . . F J L - 7 . | | . | | | | . . .
. . . . L - - - J . L J . L J L J . . .
```

El esbozo anterior tiene muchas partes aleatorias de tierra, algunas de las cuales están dentro del ciclo (**1**) y algunas están fuera de él (**0**):

```
0 F - - - - 7 F 7 F 7 F 7 F - 7 0 0 0 0
0 | F - - 7 | | | | | | | | F J 0 0 0 0
0 | | 0 F J | | | | | | | | L 7 0 0 0 0
F J L 7 L 7 L J L J | | L J 1 L - 7 0 0
L - - J 0 L 7 1 1 1 L J S 7 F - 7 L 7 0
0 0 0 0 F - J 1 1 F 7 F J | L 7 L 7 L 7
0 0 0 0 L 7 1 F 7 | | L 7 | 1 L 7 L 7 |
0 0 0 0 0 | F J L J | F J | F 7 | 0 L J
0 0 0 0 F J L - 7 0 | | 0 | | | | 0 0 0
0 0 0 0 L - - - J 0 L J 0 L J L J 0 0 0
```

>En este ejemplo más grande, **8** componentes están encerradas por el ciclo.

**Cualquier componente que no forme parte del ciclo principal puede contar como si estuviera encerrada por el ciclo**. Aquí tienes otro ejemplo con muchas piezas de tubería chatarra que no están conectadas al ciclo principal en absoluto:

```
F F 7 F S F 7 F 7 F 7 F 7 F 7 F - - - 7
L | L J | | | | | | | | | | | | F - - J
F L - 7 L J L J | | | | | | L J L - 7 7
F - - J F - - 7 | | L J L J 7 F 7 F J -
L - - - J F - J L J . | | - F J L J J 7
| F | F - J F - - - 7 F 7 - L 7 L | 7 |
| F F J F 7 L 7 F - J F 7 | J L - - - 7
7 - L - J L 7 | | F 7 | L 7 F - 7 F 7 |
L . L 7 L F J | | | | | F J L 7 | | L J
L 7 J L J L - J L J L J L - - J L J . L
```

Aquí solo están marcadas con **1** las componentes que están encerradas por el ciclo:
```
F F 7 F S F 7 F 7 F 7 F 7 F 7 F - - - 7
L | L J | | | | | | | | | | | | F - - J
F L - 7 L J L J | | | | | | L J L - 7 7
F - - J F - - 7 | | L J L J 1 F 7 F J -
L - - - J F - J L J 1 1 1 1 F J L J J 7
| F | F - J F - - - 7 1 1 1 L 7 L | 7 |
| F F J F 7 L 7 F - J F 7 1 1 L - - - 7
7 - L - J L 7 | | F 7 | L 7 F - 7 F 7 |
L . L 7 L F J | | | | | F J L 7 | | L J
L 7 J L J L - J L J L J L - - J L J . L
```
>En este último ejemplo, **10** componentes están encerradas por el ciclo.

Descubre si tienes tiempo para buscar la falla calculando el área dentro del ciclo. **¿Cuántos componentes están encerradas por el ciclo?**