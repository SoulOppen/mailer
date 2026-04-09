# Python Testing Quality - Buenas practicas

## Cuando usarlo
Usa este skill para cambios de codigo Python:
- nuevas funciones,
- refactors,
- correccion de bugs con pruebas.

## Objetivo
Mantener codigo Python explicito, testeable y estable.

## Reglas obligatorias
1. Toda funcion nueva o modificada debe tener tests.
2. Mantener cobertura minima del proyecto (actual: 80%).
3. Escribir funciones explicitas con docstrings (`Args`, `Returns`, `Raises` si aplica).
4. Centralizar constantes en `constants.py`.

## Flujo recomendado
1. Definir casos de exito, borde y error.
2. Implementar cambios con responsabilidad unica por funcion.
3. Escribir/actualizar tests en `tests/`.
4. Ejecutar:
   - `pytest`
   - `pytest --cov=. --cov-report=term-missing --cov-fail-under=80`
5. Revisar legibilidad y mantenibilidad.

## Anti-patrones
- Tests que solo cubren mocks triviales sin comportamiento real.
- Hardcodes de configuracion en logica de negocio.
- Funciones largas con multiples responsabilidades.

## Checklist
- [ ] Tests agregados/actualizados.
- [ ] Cobertura minima respetada.
- [ ] Docstrings claros.
- [ ] Constantes fuera de la logica.
