import json
import os
import re
import time


def parse_wybie_v2(codigo_wybie):
    codigo = re.sub(r"<WYBIE.*?>", "", codigo_wybie, flags=re.IGNORECASE)
    codigo = re.sub(r"\.\.\.", "", codigo)

    raiz = {}
    pila = [raiz]
    clave_actual = None

    patron = r"\((.*?)\)|=\s*([^\n{},]+)|(\{|\})|(,)"

    for coincidencia in re.finditer(patron, codigo):
        contenido_parentesis, valor, delimitador, coma = coincidencia.groups()

        if contenido_parentesis is not None:
            contenido = contenido_parentesis.strip()

            if clave_actual:
                pila[-1][clave_actual] = True
                clave_actual = None

            partes = contenido.split(maxsplit=1)
            if len(partes) == 2 and "=" not in contenido:
                val = partes[1]
                if val.isdigit():
                    pila[-1][partes[0]] = int(val)
                else:
                    try:
                        pila[-1][partes[0]] = float(val)
                    except ValueError:
                        pila[-1][partes[0]] = val
            else:
                clave_actual = contenido

        elif valor is not None:
            if clave_actual:
                val_str = valor.strip().strip('"')
                if val_str.isdigit():
                    val_str = int(val_str)
                pila[-1][clave_actual] = val_str
                clave_actual = None

        elif delimitador == "{":
            nuevo_bloque = {}
            if clave_actual:
                pila[-1][clave_actual] = nuevo_bloque
                clave_actual = None
            pila.append(nuevo_bloque)

        elif delimitador == "}":
            if clave_actual:
                pila[-1][clave_actual] = True
                clave_actual = None
            if len(pila) > 1:
                pila.pop()

        elif coma is not None:
            if clave_actual:
                pila[-1][clave_actual] = True
                clave_actual = None

    if clave_actual and len(pila) > 0:
        pila[-1][clave_actual] = True

    return raiz


def wybie_a_markdown(datos):
    md = "# Wiki de Objetos y Entidades\n\n"

    wiki = datos.get("Wiki") or datos.get("wiki") or datos

    def procesar_nodo(nodo, nivel=2):
        nonlocal md
        if not isinstance(nodo, dict):
            return

        for clave, valor in nodo.items():
            if isinstance(valor, dict):
                # Generar encabezados según el nivel de profundidad (#, ##, ###...)
                md += f"{'#' * min(nivel, 6)} {clave}\n\n"

                atributos_simples = []
                subbloques = {}

                for k, v in valor.items():
                    if isinstance(v, dict):
                        subbloques[k] = v
                    elif v is True:
                        atributos_simples.append(f"`{k}`")
                    else:
                        atributos_simples.append(f"**{k}:** {v}")

                if atributos_simples:
                    md += " | ".join(atributos_simples) + "\n\n"

                if subbloques:
                    procesar_nodo(subbloques, nivel + 1)

                if nivel == 4:
                    md += "---\n\n"

            elif valor is not True:
                md += f"* **{clave}:** {valor}\n"
            else:
                md += f"* `{clave}`\n"

    procesar_nodo(wiki)
    return md


def procesar_y_guardar(ruta_origen, ruta_destino):
    try:
        with open(ruta_origen, "r", encoding="utf-8") as archivo:
            contenido_wybie = archivo.read()

        resultado = parse_wybie_v2(contenido_wybie)
        markdown_texto = wybie_a_markdown(resultado)

        with open(ruta_destino, "w", encoding="utf-8") as f:
            f.write(markdown_texto)

        return True
    except Exception as e:
        print(f"⚠️ Error al procesar el archivo: {e}")
        return False


directorio = os.path.dirname(os.path.abspath(__file__))
ruta_wybie = os.path.join(directorio, "wiki.wybie")
ruta_md = os.path.join(directorio, "wiki.md")

if procesar_y_guardar(ruta_wybie, ruta_md):
    print("¡Wiki generada con éxito en 'wiki.md'!")

print("\n👀 Escuchando cambios en 'wiki.wybie'...")
print("   (Presiona Ctrl + C para detener)\n")

ultima_modificacion = os.path.getmtime(ruta_wybie)

try:
    while True:
        time.sleep(1)
        if os.path.exists(ruta_wybie):
            mtime_actual = os.path.getmtime(ruta_wybie)
            if mtime_actual != ultima_modificacion:
                ultima_modificacion = mtime_actual
                if procesar_y_guardar(ruta_wybie, ruta_md):
                    print("⚡ ¡Cambio detectado! 'wiki.md' actualizado con éxito.")
except KeyboardInterrupt:
    print("\n👋 Modo observador detenido.")