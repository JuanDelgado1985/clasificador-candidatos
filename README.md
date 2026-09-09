# Clasificador de Candidatos

Script en Python que clasifica candidatos de un proceso de selección según su nota técnica y disponibilidad, generando un listado de recomendados y un conteo por categoría.

## Problema que resuelve

En un proceso de selección con muchos postulantes, un reclutador pierde tiempo revisando manualmente candidato por candidato para identificar quiénes cumplen los criterios mínimos y están disponibles para ser contactados. Este script automatiza esa clasificación, entregando directamente una lista de candidatos recomendados y disponibles, junto con un conteo total por categoría (recomendados, a revisar, no recomendados, y recomendados no disponibles).

## Objetivo

Reducir el tiempo de revisión manual de candidatos y priorizar automáticamente a quiénes contactar primero.

## Tecnologías utilizadas

- Python 3

## Cómo funciona

Cada candidato se representa como un diccionario con los siguientes datos: nombre, nota, disponibilidad y años de experiencia. El script aplica las siguientes reglas:

- Nota ≥ 80 y disponible → Recomendado
- Nota ≥ 80 y no disponible → Recomendado, pero no disponible
- Nota entre 50 y 79 → A revisar
- Nota < 50 → No recomendado

## Cómo ejecutarlo

1. Tener Python 3 instalado.
2. Descargar o clonar este repositorio.
3. Ejecutar desde la terminal:

\`\`\`bash
python candidatos.py
\`\`\`

## Ejemplo de uso

Con la lista de candidatos incluida en el archivo, el script imprime:

\`\`\`
[lista de diccionarios de los candidatos recomendados y disponibles]
cantidad de recomendados = 2, cantidad de no recomendados = 1, cantidad de candidatos a revisar = 1
Cantidad de candidatos que tienen una buena nota pero no están disponibles = 1
\`\`\`

## Mejoras futuras

- Leer la lista de candidatos desde un archivo externo (CSV o base de datos), en vez de tenerla fija en el código, para poder actualizarla sin modificar el script.
- Agregar clasificación por perfil (técnico, comercial, customer), idiomas y estudios.
- Incorporar una interfaz o formulario de carga de candidatos.
- Exportar el reporte final a un archivo (CSV o Excel) en vez de solo imprimirlo en pantalla.