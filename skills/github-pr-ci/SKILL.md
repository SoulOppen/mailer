# GitHub PR y CI - Buenas practicas

## Cuando usarlo
Usa este skill para publicar cambios en GitHub:
- push a rama remota,
- apertura de Pull Request,
- validacion de CI antes de merge.

## Objetivo
Garantizar PRs merge-ready con evidencia de calidad y riesgo controlado.

## Reglas obligatorias
1. Toda PR debe incluir contexto, impacto y plan de pruebas.
2. No mergear con CI en rojo.
3. Documentar cambios de comportamiento en README/AGENT/skills cuando aplique.

## Flujo recomendado
1. Hacer push de la rama de trabajo.
2. Crear PR con resumen corto y test plan.
3. Esperar CI verde (`.github/workflows/ci.yml`).
4. Resolver comentarios de revision con commits claros.
5. Merge solo cuando checklist de calidad este completo.

## Checklist de PR
- [ ] CI en verde.
- [ ] Descripcion clara del problema y solucion.
- [ ] Riesgos y mitigaciones documentados.
- [ ] Cambios de docs incluidos si aplica.
- [ ] Sin regresiones conocidas.
