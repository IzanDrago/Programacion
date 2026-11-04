import os
import random
from edeninfinity import formatear_pais
from generador import Personaje


class MotorSimulacion:
    def __init__(self):
        self.poblacion = []
        self.generacion = 0
        self.historial_generaciones = []  # Guarda listas de personajes por generación
        self.registro_parejas = []        # Guarda tuplas: (padre, madre, hijo)

    def inicializar_mundo(self):
        """Crea la Generación 0 con 128 personajes de género aleatorio."""
        print("=== INICIALIZANDO SIMULADOR EN EDEN INFINITY ===")
        
        pj_principal = Personaje()
        self.poblacion.append(pj_principal)
        
        for _ in range(127):
            self.poblacion.append(Personaje())

        self.historial_generaciones.append(list(self.poblacion))
        print(f"\n¡Población inicial fundada! ({len(self.poblacion)} integrantes)")
        self.mostrar_poblacion(self.poblacion)

    @staticmethod
    def ordenar_por_genero(personajes):
        return sorted(personajes, key=lambda personaje: (personaje.genero, personaje.id))

    @staticmethod
    def mostrar_poblacion(personajes):
        for indice, personaje in enumerate(
            MotorSimulacion.ordenar_por_genero(personajes), 1
        ):
            genero = 'Masculino' if personaje.genero == 'M' else 'Femenino'
            print(
                f"  [{indice:03d}] {genero} | {personaje.nombre} | "
                f"País: {formatear_pais(personaje.pais)}"
            )

    def obtener_candidatos_anteriores(self):
        """Incluye con un 10% de probabilidad mayores sin descendencia."""
        progenitores_con_descendencia = {
            progenitor.id
            for padre, madre, _ in self.registro_parejas
            for progenitor in (padre, madre)
        }
        personajes_conocidos = {
            personaje.id: personaje
            for generacion in self.historial_generaciones
            for personaje in generacion
        }
        candidatos = []

        for personaje in personajes_conocidos.values():
            if (
                personaje.generacion <= self.generacion - 2
                and personaje.id not in progenitores_con_descendencia
                and personaje.vivo
                and random.random() < 0.1
            ):
                candidatos.append(personaje)

        return candidatos

    def crear_descendiente(self, padre, madre):
        generacion_antigua = min(padre.generacion, madre.generacion)
        probabilidad_adicional = (
            0.05 if self.generacion - generacion_antigua >= 2 else 0.0
        )
        hijo = padre.reproducir(
            madre, generacion=self.generacion,
            probabilidad_adicional=probabilidad_adicional
        )
        self.registro_parejas.append((padre, madre, hijo))
        return hijo

    def elegir_pareja_interactiva(self, jugador, opciones_totales):
        """Muestra a todos los integrantes de la generación y gestiona la elección de pareja."""
        print(f"\n==================================================")
        print(
            f" TÚ ERES: {jugador.nombre} | ID: {jugador.id} | "
            f"Género: {jugador.genero} | País: {formatear_pais(jugador.pais)}"
        )
        print(f"==================================================")
        print("Integrantes disponibles (ordenados por género):")
        
        candidatos_lista = [
            p for p in self.ordenar_por_genero(opciones_totales)
            if p.id != jugador.id
        ]
        
        for idx, p in enumerate(candidatos_lista, 1):
            es_mismo_genero = " (Mismo género)" if p.genero == jugador.genero else ""
            print(
                f"  [{idx}] Gen. {p.generacion} | {p.nombre} | "
                f"País: {formatear_pais(p.pais)}{es_mismo_genero}"
            )

        while True:
            try:
                eleccion = int(input(f"\nSelecciona el número del personaje con el que deseas estar (1-{len(candidatos_lista)}): "))
                if 1 <= eleccion <= len(candidatos_lista):
                    seleccionado = candidatos_lista[eleccion - 1]
                    
                    # Validar género
                    if seleccionado.genero == jugador.genero:
                        print(f"\n❌ No puedes elegir a {seleccionado.nombre}. No se puede tener descendencia con tu propio género ({jugador.genero}). Por favor, escoge a alguien del género opuesto.")
                    else:
                        print(f"\n¡Has elegido a {seleccionado.nombre} como pareja!")
                        return seleccionado
                else:
                    print("Número fuera de rango. Inténtalo de nuevo.")
            except ValueError:
                print("Por favor, introduce un número entero válido.")

    def ejecutar_simulacion(self):
        """Avanza las generaciones hasta que no queden parejas posibles de distinto género."""
        jugador_actual = self.poblacion[0]
        poblacion_actual = list(self.poblacion)

        while len(poblacion_actual) > 1:
            self.generacion += 1
            print(f"\n==================================================")
            print(f"       GENERACIÓN {self.generacion - 1} -> Creando Generación {self.generacion}")
            print(f"==================================================")

            participantes = {
                personaje.id: personaje
                for personaje in (
                    *poblacion_actual, *self.obtener_candidatos_anteriores()
                )
                if personaje.vivo
            }
            hombres = [
                p for p in participantes.values() if p.genero == 'M'
            ]
            mujeres = [
                p for p in participantes.values() if p.genero == 'F'
            ]

            if not hombres or not mujeres:
                print("\n⚠️ Ya no hay integrantes de ambos géneros para continuar la reproducción.")
                break

            siguiente_generacion = []
            
            # --- TURNO DEL JUGADOR ---
            if jugador_actual.id in participantes:
                pareja_jugador = self.elegir_pareja_interactiva(
                    jugador_actual, list(participantes.values())
                )
                
                # Remover a ambos de las listas de emparejamiento
                if jugador_actual.genero == 'M':
                    hombres.remove(jugador_actual)
                    mujeres.remove(pareja_jugador)
                    padre, madre = jugador_actual, pareja_jugador
                else:
                    mujeres.remove(jugador_actual)
                    hombres.remove(pareja_jugador)
                    padre, madre = pareja_jugador, jugador_actual

                hijo_jugador = self.crear_descendiente(padre, madre)
                siguiente_generacion.append(hijo_jugador)
                
                print(
                    f"✨ ¡Ha nacido tu descendiente!: {hijo_jugador.nombre} "
                    f"({hijo_jugador.genero}) | "
                    f"País: {formatear_pais(hijo_jugador.pais)}"
                )
                if hijo_jugador.mutaciones:
                    print(
                        f"  Mutaciones/condiciones: "
                        f"{', '.join(hijo_jugador.mutaciones)}"
                    )
                jugador_actual = hijo_jugador

            # --- EMPAREJAMIENTO AUTOMÁTICO DE OTRAS PAREJAS ---
            random.shuffle(hombres)
            random.shuffle(mujeres)
            parejas_restantes = min(len(hombres), len(mujeres))

            for i in range(parejas_restantes):
                p_m = hombres[i]
                p_f = mujeres[i]
                hijo_bot = self.crear_descendiente(p_m, p_f)
                siguiente_generacion.append(hijo_bot)
                print(f"\nPareja automática: {p_m.nombre} + {p_f.nombre}")
                print(
                    f"  Descendencia: {hijo_bot.nombre} "
                    f"({hijo_bot.genero}) | País: {formatear_pais(hijo_bot.pais)}"
                )
                if hijo_bot.mutaciones:
                    print(f"  Mutaciones/condiciones: {', '.join(hijo_bot.mutaciones)}")

            poblacion_actual = siguiente_generacion
            self.historial_generaciones.append(
                self.ordenar_por_genero(siguiente_generacion)
            )

        self.guardar_informe_completo()

    def generar_arbol_ascii(self):
        """Construye el esquema en árbol genealógico conectando cada pareja con su descendiente."""
        lineas_arbol = []
        lineas_arbol.append("\n=========================================================================")
        lineas_arbol.append("                       ESQUEMA DEL ÁRBOL GENEALÓGICO")
        lineas_arbol.append("=========================================================================\n")

        for idx, (padre, madre, hijo) in enumerate(self.registro_parejas, 1):
            lineas_arbol.append(f"  {padre.nombre} ({padre.genero})  <--->  {madre.nombre} ({madre.genero})")
            lineas_arbol.append(f"                                 |")
            lineas_arbol.append(f"                                 v")
            lineas_arbol.append(f"                      [Hijo/a]: {hijo.nombre} ({hijo.genero})\n")
            lineas_arbol.append("-------------------------------------------------------------------------")

        return lineas_arbol

    def guardar_informe_completo(self):
        """Escribe las fichas genéticas desglosadas por generación y el árbol genealógico final."""
        ruta_home = os.path.expanduser('~')
        ruta_escritorio = os.path.join(ruta_home, 'Desktop', 'genoma_familiar_completo.txt')

        contenido = []
        contenido.append("=========================================================================")
        contenido.append("         REGISTRO GENÉTICO DE LA FAMILIA Y DESCENDENCIA (EDEN INFINITY)")
        contenido.append("=========================================================================\n")

        # Mapeo rápido de hijos por padre/madre
        hijos_por_padre = {p.id: h for p, m, h in self.registro_parejas}
        hijos_por_madre = {m.id: h for p, m, h in self.registro_parejas}

        # 1. FICHAS DESGLOSADAS POR GENERACIONES
        for gen_num, integrantes in enumerate(self.historial_generaciones):
            contenido.append(f"\n=========================================================================")
            contenido.append(f"   GENERACIÓN {gen_num} ({len(integrantes)} Integrantes)")
            contenido.append(f"=========================================================================\n")

            for p in self.ordenar_por_genero(integrantes):
                contenido.append(f"FICHA GENÉTICA: {p.nombre} (ID: {p.id})")
                contenido.append(f"Apellidos: {p.apellidos}")
                contenido.append(f"Género: {('Masculino' if p.genero == 'M' else 'Femenino')}")
                contenido.append(f"País: {formatear_pais(p.pais)}")
                contenido.append(f"Padre: {p.padre.nombre if p.padre else 'Ancestral / Fundador'}")
                contenido.append(f"Madre: {p.madre.nombre if p.madre else 'Origen / Fundadora'}")
                
                # Verificar descendencia
                hijo_asociado = hijos_por_padre.get(p.id) or hijos_por_madre.get(p.id)
                if hijo_asociado:
                    contenido.append(f"Descendiente engendrado: {hijo_asociado.nombre} (ID: {hijo_asociado.id})")
                else:
                    contenido.append("Descendiente engendrado: Ninguno / Sin pareja")

                contenido.append(f"Sangre: {p.sangre['grupo']} ({p.sangre['rh']})")
                contenido.append(f"Fenotipo: Pelo={p.fenotipo['pelo']} | Piel={p.fenotipo['piel']} | Ojos={p.fenotipo['ojos']}")
                contenido.append(
                    f"Mutaciones/condiciones: {', '.join(p.mutaciones) if p.mutaciones else 'Ninguna'}"
                )
                
                contenido.append("\n[PODERES Y AFINIDADES NATURALES]")
                if getattr(p, 'poderes_naturales', None):
                    for poder in p.poderes_naturales:
                        contenido.append(f"  - [ACTIVO] {poder}")
                else:
                    contenido.append("  - [NINGUNO]")

                if getattr(p, 'poderes_mutantes', None):
                    contenido.append("\n[PODERES MUTANTES DESPERTADOS]")
                    for pm in p.poderes_mutantes:
                        contenido.append(f"  - [DESPIERTO] {pm}")

                contenido.append("\n[DESGLOSE COMPLETO DE CROMOSOMAS Y GENES]")
                for cr, datos in sorted(p.cromosomas.items()):
                    contenido.append(f"  Cr {cr:02d}: Genes=[{datos['genes']}] | Poder=[{datos['poder']}]")

                contenido.append("\n-------------------------------------------------------------------------\n")

        # 2. ANEXAR ÁRBOL GENEALÓGICO FINAL
        contenido.extend(self.generar_arbol_ascii())

        # Guardar en archivo
        try:
            os.makedirs(os.path.dirname(ruta_escritorio), exist_ok=True)
            with open(ruta_escritorio, 'w', encoding='utf-8') as f:
                f.write('\n'.join(contenido))
            
            print(f"\n📄 Archivo con todas las generaciones y el árbol genealógico guardado con éxito.")
            print(f"Ruta completa: '{ruta_escritorio}'")
        except OSError as e:
            print(f"\n Error al guardar el archivo en el Escritorio: {e}")

if __name__ == '__main__':
    motor = MotorSimulacion()
    motor.inicializar_mundo()
    motor.ejecutar_simulacion()