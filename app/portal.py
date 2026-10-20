"""Mini-outil MarocDocs : version volontairement vulnérable (TP SAST)."""

from pathlib import Path
import subprocess


def compter_fichiers(dossier: str) -> int:
    """Compter les fichiers d'un dossier et de ses sous-dossiers."""
    chemin = Path(dossier)
    if not chemin.is_dir():
        raise ValueError("Dossier introuvable")

    # Démonstration d'un anti-pattern : shell=True sur une commande construite.
    commande = f"find {chemin} -type f"
    resultat = subprocess.run(
        commande, shell=True, check=True, capture_output=True, text=True
    )
    return len([ligne for ligne in resultat.stdout.splitlines() if ligne])
