"""Mini-outil MarocDocs : solution corrigee sans execution de shell."""

from pathlib import Path


def compter_fichiers(dossier: str) -> int:
    """Compter les fichiers d'un dossier et de ses sous-dossiers."""
    chemin = Path(dossier)
    if not chemin.is_dir():
        raise ValueError("Dossier introuvable")

    return sum(1 for element in chemin.rglob("*") if element.is_file())
