# AGENT.md

## Objetivo
Este archivo define como los agentes deben trabajar en `quickMail` para mantener calidad, trazabilidad y velocidad de entrega.

## Reglas obligatorias
1. Tests para todas las funciones:
   - Toda funcion nueva debe incluir tests.
   - Las funciones existentes deben permanecer cubiertas por tests.
2. Constantes centralizadas:
   - Ninguna constante de configuracion o estructura debe quedarse hardcodeada dentro de logica.
   - Usar `constants.py` para variables compartidas.
3. Funciones explicitas:
   - Nombres descriptivos y responsabilidad unica.
   - Docstrings obligatorios con `Args`, `Returns` y `Raises` cuando aplique.

## Orquestacion de skills y subagentes
Los agentes pueden crear subagentes y combinarlos con skills para dividir trabajo en paralelo:

- Analisis y mapeo:
  - Subagente de exploracion para localizar archivos, riesgos y dependencias.
  - Skills de dominio para interpretar stack y convenciones.
- Implementacion:
  - Subagentes por modulo (ejemplo: `main.py`, `condition.py`, `tests/`).
  - Combinacion de skills de refactor, testing y documentacion.
- Validacion:
  - Subagente para ejecutar checks locales (tests/lint).
  - Subagente para revisar consistencia de README/AGENT/skills.

## Flujo recomendado
1. Analizar alcance y restricciones.
2. Diseñar cambios minimos y explicitos.
3. Implementar por capas (core -> tests -> docs -> CI).
4. Validar con pruebas automatizadas.
5. Documentar cambios y siguientes pasos.

## Checklist previo a merge
- [ ] Tests en verde.
- [ ] README actualizado y coherente con el codigo.
- [ ] Reglas de `AGENT.md` respetadas.
- [ ] Sin secretos en repo.
