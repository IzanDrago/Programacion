import random
from edeninfinity import (
    TODOS_LOS_PAISES, PAISES_POR_REGION, BANCO_NOMBRES_POR_REGION,
    determinar_grupo_sanguineo, determinar_rh_hijo, heredar_genoma,
    evaluar_mutaciones, determinar_rasgos_hijo, quitar_nombres_duplicados,
    obtener_nombre_poder, determinar_variantes_especiales, formatear_pais
)

APELLIDOS_COMUNES_POR_REGION = {
    'Africa': 'Mohamed Ali Ahmed Ibrahim Hassan Abdullahi Abdi Diallo Traore Toure Kone Diop Ndiaye Sow Fall Camara Keita Barry Sissoko Coulibaly Mensah Owusu Boateng Osei Asare Ndlovu Dlamini Nkosi Khumalo Mokoena Mthembu Zulu Banda Phiri Chirwa Mwangi Ochieng Otieno Wanjiku Kiplagat Abebe Bekele Tadesse Tesfaye Alemu Gebre Mulugeta Maseko Molefe Botha Naidoo Pillay Kamau Njoroge'.split(),
    'Asia': 'Wang Li Zhang Liu Chen Yang Huang Zhao Wu Zhou Xu Sun Ma Zhu Hu Guo He Gao Lin Luo Kim Lee Park Choi Jung Kang Cho Yoon Tanaka Suzuki Takahashi Watanabe Ito Yamamoto Nakamura Kobayashi Sato Kato Yoshida Yamada Sasaki Yamaguchi Matsumoto Nguyen Tran Le Pham Hoang Huynh Phan Bui Dang Patel Singh Kumar Sharma Gupta Khan Das'.split(),
    'Europe': 'Smith Jones Williams Taylor Brown Davies Evans Wilson Thomas Johnson Roberts Robinson Wright Thompson Walker White Edwards Hughes Green Hall Lewis Harris Clarke Patel Jackson Wood Turner Martin Cooper Hill Ward Morris Moore King Baker Harrison Morgan Allen Mitchell Scott Young Campbell Adams Phillips Watson Richardson Cox Gray Bennett Carter Reed Bailey Bell Murphy Kelly Walsh Ryan O’Brien'.split(),
    'North America': 'Smith Johnson Williams Brown Jones Garcia Miller Davis Rodriguez Martinez Hernandez Lopez Gonzalez Wilson Anderson Thomas Taylor Moore Jackson Martin Lee Perez Thompson White Harris Sanchez Clark Ramirez Lewis Robinson Walker Young Allen King Wright Scott Torres Nguyen Hill Flores Green Adams Nelson Baker Hall Rivera Campbell Mitchell Carter Roberts Gomez Phillips Evans Turner Diaz Parker Cruz Edwards Collins Stewart Morris Morales'.split(),
    'South America': 'Silva Santos Oliveira Souza Pereira Costa Rodrigues Almeida Nascimento Lima Araújo Fernandes Carvalho Gomes Martins Rocha Ribeiro Alves Monteiro Mendes Barbosa Cardoso Soares Teixeira Correia Moreira Ferreira Castro Sánchez González Rodríguez Gómez Fernández López Martínez Pérez García Romero Torres Flores Ramírez Díaz Vargas Rojas Muñoz Contreras Herrera Medina Morales Jiménez Gutiérrez Castillo Ortiz Reyes Cruz Mendoza Vargas'.split(),
    'Oceania': 'Smith Williams Brown Jones Taylor Wilson Davies Evans Thomas Johnson White Martin Anderson Thompson Walker Robinson Wright Thompson Hall Lewis Harris Clarke Young King Baker Mitchell Campbell Scott Roberts Kelly Ryan Murphy Martin Turner Cooper Hill Ward Morris Moore Allen Green Jackson Wright Morgan Bell Hughes Bennett Carter Reed Bailey Parker Stewart Collins Phillips Campbell Gray Richardson Foster Cook Ward'.split(),
}

APELLIDOS_COMUNES_POR_PAIS = {
    'AR': 'González Rodríguez Gómez Fernández López Martínez Pérez García Sánchez Romero'.split(),
    'BR': 'Silva Santos Oliveira Souza Pereira Costa Rodrigues Almeida Nascimento Lima'.split(),
    'CA': 'Smith Brown Tremblay Martin Roy Wilson MacDonald Gagnon Johnson Lee'.split(),
    'CL': 'González Muñoz Rojas Díaz Pérez Soto Contreras Silva Martínez Sepúlveda'.split(),
    'CN': 'Wang Li Zhang Liu Chen Yang Huang Zhao Wu Zhou'.split(),
    'CO': 'Rodríguez Gómez González Martínez García López Hernández Sánchez Ramírez Pérez'.split(),
    'DE': 'Müller Schmidt Schneider Fischer Weber Meyer Wagner Becker Schulz Hoffmann'.split(),
    'ES': 'García Rodríguez González Fernández López Martínez Sánchez Pérez Gómez Martín'.split(),
    'FR': 'Martin Bernard Thomas Petit Robert Richard Durand Dubois Moreau Laurent Simon'.split(),
    'GB': 'Smith Jones Taylor Brown Williams Wilson Johnson Davies Patel Robinson Wright'.split(),
    'IN': 'Devi Singh Kumar Das Kaur Sharma Patel Shah Gupta Khan Verma'.split(),
    'IT': 'Rossi Russo Ferrari Esposito Bianchi Romano Colombo Bruno Ricci Marino'.split(),
    'JP': 'Sato Suzuki Takahashi Tanaka Watanabe Ito Yamamoto Nakamura Kobayashi Kato'.split(),
    'KR': 'Kim Lee Park Choi Jung Kang Cho Yoon Jang Lim'.split(),
    'MX': 'Hernández García Martínez López González Pérez Rodríguez Sánchez Ramírez Cruz'.split(),
    'PE': 'Quispe Flores Sánchez García Rodríguez Rojas Huamán Mamani López Pérez'.split(),
    'PT': 'Silva Santos Ferreira Pereira Oliveira Costa Rodrigues Martins Sousa Fernandes'.split(),
    'RU': 'Ivanov Smirnov Kuznetsov Popov Vasiliev Petrov Sokolov Mikhailov Novikov Fedorov'.split(),
    'US': 'Smith Johnson Williams Brown Jones Garcia Miller Davis Rodriguez Martinez'.split(),
    'ZA': 'Nkosi Ndlovu Khumalo Dlamini Mokoena Mthembu Zulu Botha Van der Merwe Naidoo'.split(),
}

APELLIDOS_ESPECIALES = ('Todo', 'Bonestone', 'Belial')
APELLIDOS_ESPECIALES_POR_PAIS = {
    'ES': ('Drago', 'Morato', 'Nieto', 'Santiago', 'Franco', 'DelHoyo'),
    'AT': ('Hitler',),
    'AR': ('Wybie',),
    'US': ('WiFi', 'McMillen'),
    'ZA': ('Musk',),
}
APELLIDOS_ATLANTIS = ('Nimbus', 'Poseidón', 'Neptuno', 'Olimpus', 'Torappu', 'Nobi')
APELLIDOS_VINCULADOS_POR_PAIS = {
    'ES': {'South America': 3},
    'GB': {'US': 3},
    'US': {'GB': 2},
    'CA': {'GB': 2},
    'AU': {'GB': 2},
    'NZ': {'GB': 2},
    'BR': {'PT': 1},
    'PT': {'BR': 2},
    'AT': {'DE': 1},
    'CH': {'DE': 1},
}


def generar_apellido(pais):
    """Elige un apellido de un banco local según el país del personaje."""
    region = next((r for r, paises in PAISES_POR_REGION.items() if pais in paises), 'Europe')
    if region == 'Fictional':
        region = 'Europe'
    apellidos_region = APELLIDOS_COMUNES_POR_REGION.get(
        region, APELLIDOS_COMUNES_POR_REGION['Europe']
    )
    apellidos_pais = APELLIDOS_COMUNES_POR_PAIS.get(pais, ())
    apellidos_comunes = list(dict.fromkeys((*apellidos_pais, *apellidos_region)))[:50]
    apellidos = [*apellidos_comunes, *APELLIDOS_ESPECIALES]
    for codigo_vinculado, peso in APELLIDOS_VINCULADOS_POR_PAIS.get(pais, {}).items():
        apellidos_vinculados = (
            APELLIDOS_COMUNES_POR_REGION[codigo_vinculado]
            if codigo_vinculado in APELLIDOS_COMUNES_POR_REGION
            else APELLIDOS_COMUNES_POR_PAIS.get(codigo_vinculado, ())
        )
        apellidos.extend(apellido for apellido in apellidos_vinculados for _ in range(peso))
    apellidos.extend(APELLIDOS_ESPECIALES_POR_PAIS.get(pais, ()))

    if pais == 'ATL':
        apellidos.extend(
            apellido for apellido in APELLIDOS_ATLANTIS if apellido not in apellidos
        )

    return random.choice(apellidos)


class Personaje:
    _id_counter = 1

    def __init__(
        self, nombre=None, genero=None, padre=None, madre=None, pais=None,
        generacion=None, probabilidad_adicional=0.0
    ):
        self.id = Personaje._id_counter
        Personaje._id_counter += 1
        
        self.padre = padre
        self.madre = madre
        self.genero = genero if genero else random.choice(['M', 'F'])
        
        # 1. GENERACIÓN DE ADN
        if padre is None or madre is None:
            # Fundador (Totalmente Aleatorio)
            self.pais = pais if pais else random.choice(tuple(TODOS_LOS_PAISES))
            self.generacion = 0 if generacion is None else generacion
            self._generar_adn_fundador()
        else:
            # Hijo heredado mediante reglas de edeninfinity
            self.pais = pais if pais else padre.pais
            self.generacion = (
                max(padre.generacion, madre.generacion) + 1
                if generacion is None else generacion
            )
            self._heredar_adn(padre, madre, probabilidad_adicional)

        if padre is None or madre is None:
            self.apellido_paterno = generar_apellido(self.pais)
            self.apellido_materno = None
        else:
            self.apellido_paterno = padre.apellido_paterno
            self.apellido_materno = madre.apellido_paterno

        # 2. GENERACIÓN DE NOMBRE
        if nombre:
            self.nombre = nombre
        else:
            self.nombre = self._generar_nombre()

        self.edad = 0
        self.vivo = True

    def _generar_adn_fundador(self):
        """Crea un personaje completamente nuevo con 50% de probabilidad de gen/poder positivo."""
        self.sangre = {
            'grupo': random.choice(['A', 'B', 'O', 'AB']),
            'rh': random.choice(['+', '-', 'Neutro'])
        }
        
        self.cromosomas = {}
        self.poderes_activos = set()
        self.poderes_naturales = []
        
        # Cromosomas 1 al 22 (50% de ser positivo)
        for i in range(1, 23):
            tiene_poder = random.random() < 0.5
            genes = random.choice(['AB', 'Ab', 'aB', 'ab']) if not tiene_poder else 'AB'
            
            self.cromosomas[i] = {
                'genes': genes,
                'poder': 1 if tiene_poder else 0
            }
            if tiene_poder:
                self.poderes_activos.add(i)
                self.poderes_naturales.append(f"Cromosoma {i}: {obtener_nombre_poder(i, self.genero)}")
                
        # Cromosoma 23 (Género)
        self.cromosomas[23] = {
            'genes': 'AB' if self.genero == 'M' else 'ab',
            'poder': 1 if self.genero == 'M' else 0
        }
        self.poderes_naturales.append(f"Cromosoma 23: {obtener_nombre_poder(23, self.genero)}")

        # Fenotipos
        self.fenotipo = {
            'pelo': random.choice(['Castaño', 'Rubio', 'Negro', 'Blanco', 'Rojo', 'Naranja']),
            'piel': random.choice(['Blanco', 'Crema', 'Mestizo', 'Marron', 'Oscuro', 'Albino']),
            'ojos': random.choice(['Rojo', 'Marron oscuro', 'Miel', 'Azul', 'Verde', 'Pardo', 'Blancos'])
        }

        # Mutaciones y Variantes de edeninfinity
        self.sindromes, self.poderes_mutantes = evaluar_mutaciones(self.genero, factor_sindrome=False)
        self.mutaciones = list(self.sindromes)
        self.variantes = {
            'neurovariantes': [v for v in ('TEA', 'TDA', 'TDH') if random.random() < 0.05],
            'ludopathy': random.random() < 0.02,
            'diabetes': random.choice([None, 'A', 'B', 'Otros tipos']) if random.random() < 0.05 else None,
            'dioptria': random.randint(1, 10) if random.random() < 0.2 else None,
            'gafas': random.random() < 0.3,
            'omnisciencia': self.genero == 'M' and random.randint(1, 7**77) == 777
        }

    def _heredar_adn(self, padre, madre, probabilidad_adicional=0.0):
        """Hereda el genoma usando las funciones reales de edeninfinity.py."""
        self.sangre = {
            'grupo': determinar_grupo_sanguineo(padre.sangre['grupo'], madre.sangre['grupo']),
            'rh': determinar_rh_hijo(padre.sangre['rh'], madre.sangre['rh'])
        }
        
        # Herencia de genoma de edeninfinity
        genoma_hijo, _ = heredar_genoma(padre.cromosomas, madre.cromosomas, self.genero)
        
        # Fenotipos parentales
        pelo, piel, ojos = determinar_rasgos_hijo(
            {'fenotipo': padre.fenotipo}, 
            {'fenotipo': madre.fenotipo}
        )
        self.fenotipo = {'pelo': pelo, 'piel': piel, 'ojos': ojos}
        
        # Evaluación de mutaciones
        tiene_sindrome_padres = len(getattr(padre, 'sindromes', [])) > 0 or len(getattr(madre, 'sindromes', [])) > 0
        muts, pod_muts = evaluar_mutaciones(
            self.genero, tiene_sindrome_padres, probabilidad_adicional
        )
        
        self.cromosomas = {i: {'genes': genoma_hijo[i], 'poder': 0} for i in range(1, 24)}
        self.sindromes = muts
        self.mutaciones = muts
        self.poderes_mutantes = pod_muts
        self.poderes_activos = set()
        self.poderes_naturales = []
        self.variantes = {'neurovariantes': [], 'ludopathy': False, 'diabetes': None, 'dioptria': None, 'gafas': False, 'omnisciencia': False}

    def _generar_nombre(self):
        region = next((r for r, p in PAISES_POR_REGION.items() if self.pais in p), 'Europe')
        banco = BANCO_NOMBRES_POR_REGION.get(region, BANCO_NOMBRES_POR_REGION['Europe'])
        nombres = quitar_nombres_duplicados((*banco[self.genero], *banco['N']))
        if not nombres:
            banco = BANCO_NOMBRES_POR_REGION['Europe']
            nombres = quitar_nombres_duplicados((*banco[self.genero], *banco['N']))
        
        nombre_pila = random.choice(nombres)
        return f"{nombre_pila} {self.apellidos}"

    @property
    def apellidos(self):
        return ' '.join(
            apellido for apellido in (self.apellido_paterno, self.apellido_materno)
            if apellido
        )

    def reproducir(
        self, pareja, *, generacion=None, probabilidad_adicional=0.0
    ):
        if self.genero == pareja.genero:
            raise ValueError("No se pueden reproducir personajes del mismo género.")
        
        padre = self if self.genero == 'M' else pareja
        madre = self if self.genero == 'F' else pareja
        
        return Personaje(
            padre=padre, madre=madre, generacion=generacion,
            probabilidad_adicional=probabilidad_adicional
        )

    def mostrar_ficha(self):
        print(f"\n--- FICHA: {self.nombre} (ID: {self.id}) ---")
        print(
            f"Género: {self.genero} | Edad: {self.edad} | "
            f"País: {formatear_pais(self.pais)}"
        )
        print(f"Sangre: {self.sangre['grupo']}({self.sangre['rh']})")
        print(f"Fenotipo: Pelo {self.fenotipo['pelo']} | Piel {self.fenotipo['piel']} | Ojos {self.fenotipo['ojos']}")
        print(f"Poderes Activos ({len(self.poderes_activos)}):")
        for p in self.poderes_naturales:
            print(f"  * {p}")
        if self.poderes_mutantes:
            print(f"Poderes Mutantes Despiertos: {', '.join(self.poderes_mutantes)}")
        if self.mutaciones:
            print(f"Mutaciones/Síndromes: {', '.join(self.mutaciones)}")