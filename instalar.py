import json
import zipfile

package_json = {
    "name": "wybie-lang",
    "displayName": "WYBIE Language Support",
    "description": "Soporte oficial de sintaxis para archivos .wybie",
    "version": "1.0.0",
    "publisher": "izan",
    "engines": {"vscode": "^1.60.0"},
    "categories": ["Programming Languages"],
    "contributes": {
        "languages": [
            {
                "id": "wybie",
                "aliases": ["WYBIE", "wybie"],
                "extensions": [".wybie"],
                "configuration": "./language-configuration.json",
            }
        ],
        "grammars": [
            {
                "language": "wybie",
                "scopeName": "source.wybie",
                "path": "./syntaxes/wybie.tmLanguage.json",
            }
        ],
    },
}

lang_config = {
    "comments": {"lineComment": "#"},
    "brackets": [["{", "}"], ["(", ")"]],
    "autoClosingPairs": [
        {"open": "{", "close": "}"},
        {"open": "(", "close": ")"},
        {"open": '"', "close": '"'},
    ],
    "surroundingPairs": [
        ["{", "}"],
        ["(", ")"],
        ['"', '"'],
    ],
}

tm_language = {
    "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
    "name": "WYBIE",
    "patterns": [
        {"name": "keyword.other.header.wybie", "match": "<WYBIE.*?>"},
        {"name": "punctuation.definition.tag.wybie", "match": "\\(|\\)"},
        {
            "name": "entity.name.tag.wybie",
            "match": "(?<=\\()[^)]+(?=\\))",
        },
        {"name": "keyword.operator.assignment.wybie", "match": "="},
        {"name": "punctuation.section.block.wybie", "match": "\\{|\\}"},
        {"name": "string.quoted.double.wybie", "begin": '"', "end": '"'},
        {"name": "constant.numeric.wybie", "match": "\\b\\d+(\\.\\d+)?\\b"},
    ],
    "scopeName": "source.wybie",
}

content_types = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="application/json"/>
  <Default Extension="vsixmanifest" ContentType="text/xml"/>
</Types>"""

vsix_manifest = """<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.openxmlformats.org/package/2010/07/manifest">
  <Metadata>
    <Identity Id="wybie-lang" Version="1.0.0" Publisher="izan"/>
    <DisplayName>WYBIE Language Support</DisplayName>
    <Description>Soporte para .wybie</Description>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
  </Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json"/>
  </Assets>
</PackageManifest>"""

vsix_path = "/workspaces/Programacion/wybie.vsix"

with zipfile.ZipFile(vsix_path, "w") as z:
    z.writestr("extension/package.json", json.dumps(package_json, indent=2))
    z.writestr(
        "extension/language-configuration.json",
        json.dumps(lang_config, indent=2),
    )
    z.writestr(
        "extension/syntaxes/wybie.tmLanguage.json",
        json.dumps(tm_language, indent=2),
    )
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("extension.vsixmanifest", vsix_manifest)

print("📦 ¡Paquete wybie.vsix creado con éxito!")