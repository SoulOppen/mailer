# Skills del proyecto

Esta carpeta contiene skills reutilizables para agentes y subagentes.

## Objetivo
Definir bloques de conocimiento accionables para tareas recurrentes:
- exploracion del codigo,
- refactor y estandarizacion,
- testing automatizado,
- documentacion y CI.

## Convencion
- Un skill por carpeta: `skills/<nombre-skill>/SKILL.md`
- Nombre corto, orientado a accion.
- Incluir contexto, pasos, criterios de salida y anti-patrones.

## Uso con subagentes
Se recomienda combinar skills segun el tipo de tarea:
1. Skill de analisis + subagente de exploracion.
2. Skill de implementacion + subagente de cambios de codigo.
3. Skill de validacion + subagente de testing/CI.

## Plantilla
Usa `skills/_template/SKILL.md` como base para nuevos skills.
