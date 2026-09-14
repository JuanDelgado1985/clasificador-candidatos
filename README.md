# Clasificador de Candidatos

Script en Python que clasifica candidatos de un proceso de selección según su nota técnica y disponibilidad, generando un listado de recomendados y un conteo por categoría.

## Problema que resuelve

En un proceso de selección con muchos postulantes, un reclutador pierde tiempo revisando manualmente candidato por candidato para identificar quiénes cumplen los criterios mínimos y están disponibles para ser contactados. Este script automatiza esa clasificación, entregando directamente una lista de candidatos recomendados y disponibles, junto con un conteo total por categoría (recomendados, a revisar, no recomendados, y recomendados no disponibles).

## Objetivo

Reducir el tiempo de revisión manual de candidatos y priorizar automáticamente a quiénes contactar primero.

## Tecnologías utilizadas

- Python 3

## Cómo funciona

El script toma la información de un archivo `candidatos.csv`, con los encabezados `nombre, nota, disponible, anios_experiencia`. Aplica las siguientes reglas de clasificación:

- Nota ≥ 80 y disponible → Recomendado
- Nota ≥ 80 y no disponible → Recomendado, pero no disponible
- Nota entre 50 y 79 → A revisar
- Nota < 50 → No recomendado

## Manejo de errores

El script está preparado para manejar dos situaciones comunes sin interrumpir su ejecución:

- **Archivo no encontrado:** si `candidatos.csv` no existe o el nombre no coincide, se muestra un mensaje indicándolo y el programa finaliza de forma controlada.
- **Datos inválidos en una fila:** si una fila tiene un valor que no puede convertirse al tipo de dato esperado (por ejemplo, texto en la columna `nota`), se muestra un mensaje indicando qué fila tiene el problema, esa fila se omite, y el resto de los candidatos se procesa con normalidad.

## Cómo ejecutarlo

1. Tener Python 3 instalado.
2. Descargar o clonar este repositorio.
3. Asegurarse de tener un archivo `candidatos.csv` en la misma carpeta que `candidatos.py`, con los encabezados `nombre, nota, disponible, anios_experiencia`.
4. Ejecutar desde la terminal:

\`\`\`bash
python candidatos.py
\`\`\`

## Ejemplo de uso

Con el archivo `candidatos.csv` incluido en el repositorio, el script imprime:

\`\`\`
[lista de diccionarios de los candidatos recomendados y disponibles]
cantidad de recomendados = 2, cantidad de no recomendados = 1, cantidad de candidatos a revisar = 1
Cantidad de candidatos que tienen una buena nota pero no están disponibles = 1
\`\`\`

## Mejoras futuras

- Agregar clasificación por perfil (técnico, comercial, customer), idiomas y estudios.
- Incorporar una interfaz o formulario de carga de candidatos.
- Exportar el reporte final a un archivo (CSV o Excel) en vez de solo imprimirlo en pantalla.
- Guardar en un archivo de log las filas con errores, en vez de solo mostrarlas en consola.