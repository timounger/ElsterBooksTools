[![GitHub release (latest by date)](https://img.shields.io/github/v/release/timounger/ElsterBooksTools)](https://github.com/timounger/ElsterBooksTools/releases/latest)
![GitHub Repo stars](https://img.shields.io/github/stars/timounger/ElsterBooksTools)

# ElsterBooksTools

Dieses Repository stellt portable Tools zur Verfügung, die für ElsterBooks benötigt werden.

## Tools Sammlung

Folgende Tools werden zur Verfügung gestellt:

### LibreOfficePortable

Konvertiert Excel Dokumente nach PDFA-3b.

- Download: http://download.documentfoundation.org/libreoffice/portable/24.8.2/LibreOfficePortable_24.8.2_MultilingualStandard.paf.exe
- Version: 24.8.2

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

- Download: https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/PortableGit-2.47.1-64-bit.7z.exe
- Version: v2.47.1

### PLZ

JSON Export mit Ortschaftsdaten um aus der PLZ den Ortsnamen zu generieren.

- Download: https://dev.ratopi.de/opengeodb/DE.tab.json
- Version: Stand 10/2024

### Poppler

Poppler rendert PDF-Dokumente in Bild Formate.

- Repo: https://github.com/oschwartz10612/poppler-windows
- Version: Release 24.08.0-0

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
