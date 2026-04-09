def readTxt(path: str) -> set[str]:
    """Lee un TXT y devuelve sus lineas (sin encabezado) como conjunto.

    Args:
        path: Ruta del archivo a leer.

    Returns:
        Conjunto de lineas unicas no vacias. Si no existe, retorna set().
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            next(f, None)  # skip first line safely
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()


def writeTxt(path: str, lines: set[str], head: str) -> None:
    """Escribe un TXT con encabezado y una linea por elemento.

    Args:
        path: Ruta del archivo de salida.
        lines: Coleccion de lineas a persistir.
        head: Encabezado a escribir en la primera linea.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{head}\n")
        for line in lines:
            f.write(line + "\n")
