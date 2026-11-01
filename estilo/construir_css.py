"""Escribe `datascience.css`: la hoja de estilo con los íconos de sección incrustados como SVG.

Uso: `python estilo/construir_css.py` (después de cambiar `estilo.css` o un ícono de `iconos/`).
Las secciones del sidebar son carpetas sin página: cada ícono se asocia al elemento cuyo `title` es el nombre de la
sección en el `toc` de `myst.yml`.
"""
from pathlib import Path
from urllib.parse import quote

AQUI = Path(__file__).parent

# título de la sección en myst.yml -> archivo del ícono
ICONOS = {
    "Google Colab": "colab",
    "VS Code": "vscode",
    "MyST Markdown": "myst",
    "Hugging Face": "huggingface",
    "Google Earth Engine": "gee",
    "QGIS": "qgis",
}


def uri_svg(ruta: Path) -> str:
    svg = " ".join(ruta.read_text(encoding="utf-8").split())
    return "data:image/svg+xml," + quote(svg, safe=" =:/,';()-.")


def _sel(titulo: str) -> str:
    return f".myst-primary-sidebar .myst-toc-item > [title='{titulo}']"


def reglas() -> str:
    lineas = [", ".join(_sel(t) for t in ICONOS) + " {\n  display: flex;\n  align-items: center;\n  gap: 0.5rem;\n}"]
    lineas.append(
        ", ".join(f"{_sel(t)}::before" for t in ICONOS)
        + " {\n  content: \"\";\n  flex: none;\n  width: 1.45em;\n  height: 1.45em;\n"
        "  background: no-repeat center / contain;\n}"
    )
    for titulo, archivo in ICONOS.items():
        lineas.append(f"{_sel(titulo)}::before {{ background-image: url(\"{uri_svg(AQUI / 'iconos' / f'{archivo}.svg')}\"); }}")
    return "\n".join(lineas) + "\n"


if __name__ == "__main__":
    base = (AQUI / "estilo.css").read_text(encoding="utf-8")
    (AQUI / "datascience.css").write_text(base.replace("/* ICONOS */", reglas()), encoding="utf-8")
    print("escrito", AQUI / "datascience.css")
