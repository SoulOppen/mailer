# Git Workflow - Buenas practicas

## Cuando usarlo
Usa este skill para trabajo local con Git:
- creacion de ramas,
- commits atomicos,
- historial claro y trazable.

## Objetivo
Mantener un flujo de versionado limpio, seguro y facil de revisar.

## Reglas obligatorias
1. Nunca incluir secretos en commits (`.env`, tokens, credenciales).
2. Un commit debe tener un objetivo unico y verificable.
3. Evitar commits gigantes que mezclen refactor, feature y fix.

## Flujo recomendado
1. Crear rama descriptiva:
   - `feat/<tema>`
   - `fix/<tema>`
   - `chore/<tema>`
2. Implementar cambios en bloques pequenos.
3. Ejecutar pruebas locales antes de commit.
4. Commitear con mensaje claro del por que.

## Convenciones de commit
- `feat: add ...`
- `fix: correct ...`
- `test: cover ...`
- `docs: update ...`
- `refactor: simplify ...`

## Checklist
- [ ] Cambios acotados y coherentes.
- [ ] Mensaje de commit claro.
- [ ] Tests locales ejecutados.
- [ ] Sin archivos sensibles.
