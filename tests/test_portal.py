"""Tests fonctionnels simples ; ils ne remplacent pas un scan SAST."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from app.portal import compter_fichiers


class TestMarocDocs(unittest.TestCase):
    def test_deux_fichiers(self):
        with TemporaryDirectory() as dossier:
            Path(dossier, "rapport.txt").write_text("bonjour", encoding="utf-8")
            sous_dossier = Path(dossier, "docs")
            sous_dossier.mkdir()
            (sous_dossier / "note.txt").write_text("note", encoding="utf-8")
            self.assertEqual(compter_fichiers(dossier), 2)

    def test_dossier_vide(self):
        with TemporaryDirectory() as dossier:
            self.assertEqual(compter_fichiers(dossier), 0)

    def test_dossier_absent(self):
        with TemporaryDirectory() as dossier:
            absent = str(Path(dossier, "inexistant"))
            with self.assertRaises(ValueError):
                compter_fichiers(absent)


if __name__ == "__main__":
    unittest.main()
