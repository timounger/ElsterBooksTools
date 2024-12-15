[![GitHub release (latest by date)](https://img.shields.io/github/v/release/timounger/ElsterBooksTools)](https://github.com/timounger/ElsterBooksTools/releases/latest)

# ElsterBooksTools

Externe Tools Sammlung für ElsterBooks

## Libre Office

[Libre Office Portable v24.8.2 MultilingualStandard](http://download.documentfoundation.org/libreoffice/portable/24.8.2/LibreOfficePortable_24.8.2_MultilingualStandard.paf.exe)

Modifikationen:
- Installation mit: Remove Extra Languages
- Online Update to v24.8.3.2
- LibreOfficePortable.exe → Extras → Optionen → LibreOffice → Online-Aktualisierunge → Automatisch auf Aktualsierungen prüfen und Autoamtische Aktualisierung deaktiviert
- Export-Einstellungen in `LibreOffice Calc` vornehmen:
  - Programm öffnen.
  - Datei → Als PDF exportieren
  - Verlustfreie Komprimierung
  - Archiv PDF/A-Version: PDFA-3b
  - Gliederung exportieren NICHT setzen
- PDF Export über CMD ausgeführt

Gelöscht:
- LibreOfficePortable\App\AppInfo
- LibreOfficePortable\App\DefaultData
- LibreOfficePortable\App\Fonts
- LibreOfficePortable\App\Java
- LibreOfficePortable\App\Readme.txt
- LibreOfficePortable\App\Manual
- LibreOfficePortable\App\libreoffice\help
- LibreOfficePortable\App\libreoffice\readmes
- LibreOfficePortable\App\libreoffice\share\autocorr
- LibreOfficePortable\App\libreoffice\share\extensions
- LibreOfficePortable\App\libreoffice\share\template
- LibreOfficePortable\App\libreoffice\share\gallery
- LibreOfficePortable\App\libreoffice\share\autotext
- LibreOfficePortable\App\libreoffice\share\Scripts\python
- LibreOfficePortable\App\libreoffice\share\basic\Template
- LibreOfficePortable\App\libreoffice\share\basic\Tutorials
- LibreOfficePortable\App\libreoffice\share\config
- LibreOfficePortable\App\libreoffice\share\theme_definitions
- LibreOfficePortable\App\libreoffice\share\filter
- LibreOfficePortable\App\libreoffice\program\shell
- LibreOfficePortable\App\libreoffice\program\python-core-3.9.20
- LibreOfficePortable\App\libreoffice\program\classes
- LibreOfficePortable\App\libreoffice\program\resource
- LibreOfficePortable\App\libreoffice\LibreOffice_24.8.3.2_Win_x86.msi
- LibreOfficePortable\App\libreoffice\CREDITS.fodt
- LibreOfficePortable\App\libreoffice\extra_languages_removed.txt
- LibreOfficePortable\Data\settings\LibreOfficePortableSettings.ini
- LibreOfficePortable\Data\fonts
- LibreOfficePortable\Other
- LibreOfficePortable\help.html
- Alle Daten im Format: *.log, .status, *.py, *.png, *.svg
- Ordner: updates, tmp, temp, cache
- Inhalte mit Pfad angabe: git_data, C:/Users/Timo/Downloads
- Hier nur noch Ordner App und Data: ElsterBooksTools\LibreOfficePortable
- Alle EXE delete bis auf soffice.exe in `LibreOfficePortable\App\libreoffice\program`
- Alle Ordner in LibreOfficePortable\Data\settings\user bis auf registrymodifications.xcu

Geänderte User Setting in: `LibreOfficePortable\Data\settings\user\registrymodifications.xcu`

``` ini
<item oor:path="/org.openoffice.Office.Common/Filter/PDF/Export"><prop oor:name="ExportBookmarks" oor:op="fuse"><value>false</value></prop></item>
<item oor:path="/org.openoffice.Office.Common/Filter/PDF/Export"><prop oor:name="SelectPdfVersion" oor:op="fuse"><value>3</value></prop></item>
<item oor:path="/org.openoffice.Office.Common/Filter/PDF/Export"><prop oor:name="UseLosslessCompression" oor:op="fuse"><value>true</value></prop></item>
```

Update Check deaktivieren
``` ini
<item oor:path="/org.openoffice.Office.Jobs/Jobs/org.openoffice.Office.Jobs:Job['UpdateCheck']/Arguments"><prop oor:name="AutoCheckEnabled" oor:op="fuse" oor:type="xs:boolean"><value>false</value></prop></item>
```

Auto Update deaktiviert
``` ini
<item oor:path="/org.openoffice.Office.Update/Update"><prop oor:name="Enabled" oor:op="fuse"><value>false</value></prop></item>
```

## Git

https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/PortableGit-2.47.1-64-bit.7z.exe

## PLZ
