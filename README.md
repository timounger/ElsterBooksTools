[![GitHub release (latest by date)](https://img.shields.io/github/v/release/timounger/ElsterBooksTools)](https://github.com/timounger/ElsterBooksTools/releases/latest)
![GitHub Repo stars](https://img.shields.io/github/stars/timounger/ElsterBooksTools)

# ElsterBooksTools

Dieses Repository stellt portable Tools zur Verfügung, die für ElsterBooks benötigt werden.

## Tools Sammlung

Folgende Tools werden zur Verfügung gestellt:

### LibreOfficePortable

Konvertiert Excel Dokumente nach PDFA-3b.

- Download: http://download.documentfoundation.org/libreoffice/portable/25.2.3/LibreOfficePortable_25.2.3_MultilingualStandard.paf.exe
- Version: 25.2.3

Modifikationen:

- Installation mit: Remove Extra Languages
- Automatische Aktualisierung deaktiviert
- Export-Einstellungen in `LibreOffice Calc`:
  - Verlustfreie Komprimierung
  - Archiv PDF/A-Version: PDFA-3b
  - keine Gliederung exportieren
- nicht verwendete Dateien entfernt

### Git

CMD Befehle zur revisionssicheren Dokumentenablage.

- Download: https://github.com/git-for-windows/git/releases/download/v2.51.0.windows.1/PortableGit-2.51.0-64-bit.7z.exe
- Version: v2.51.0

### PLZ

JSON Export mit Ortschaftsdaten um aus der PLZ den Ortsnamen zu generieren.

- Download: https://dev.ratopi.de/opengeodb/DE.tab.json
- Version: Stand 10/2024

### Tesseract

Tesseract analysiert Bilder und erkennt Buchstaben, Zahlen und Symbole, um daraus lesbaren Text zu generieren.

- Repo: https://github.com/tesseract-ocr/tesseract
- Version: 5.5.0

## Credits

Besonderen Dank an alle Mitwirkenden:
<br><br>
<a href="https://github.com/timounger/ElsterBooksTools/graphs/contributors">
<img src="https://contrib.rocks/image?repo=timounger/ElsterBooksTools" />
</a>
