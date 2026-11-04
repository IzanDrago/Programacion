# Cabrón, no me copies el código original de ©IzanDragoMorato
# Importa `random` para usar ese módulo en este archivo.
import random
# Importa `unicodedata` para usar ese módulo en este archivo.
import unicodedata
# Importa `os` para usar ese módulo en este archivo.
import os
# Importa `date, datetime, timedelta` desde `datetime`; así se pueden usar directamente esos nombres.
from datetime import date, datetime, timedelta
# Importa `time as hora` desde `datetime`; así se pueden usar directamente esos nombres.
from datetime import time as hora
# Catálogos de entrada del simulador: agrupan países, nombres, localidades y rasgos
# para que la lógica elija opciones válidas sin repetirlas en cada función.
# Define `PAISES_POR_REGION` para relacionar cada región con sus códigos de país válidos.
PAISES_POR_REGION = {'Africa': set('AO BF BI BJ BW CD CF CG CI CM CV DJ DZ EG EH ER ET GA GH GM GN GQ GW KE KM LR LS LY MA MG ML MR MU MW MZ NA NE NG RW SC SD SL SN SO SS ST SZ TD TG TN TZ UG ZA ZM ZW'.split()), 'Asia': set('AE AF AM AZ BD BH BN CN GE ID IL IN IQ IR JO JP KG KH KP KR KW KZ LA LB LK MM MN MV MY NP OM PH PK PS QA SA SG SY TH TJ TL TM TR TW UZ VN YE'.split()), 'Europe': set('AD AL AT AX BA BE BG BY CH CY CZ DE DK EE ES FI FO FR GB GG GI GR HR HU IE IM IS IT JE LI LT LU LV MC MD ME MK MT NL NO PL PT RO RS RU SE SI SJ SK SM UA VA'.split()), 'North America': set('BM BQ CA GL PM US'.split()), 'South America': set('AG AI AN AR AW BB BL BO BR BS BZ CL CO CR CU CW DM DO EC FK GD GF GP GT GY HN HT JM KN KY LC MF MQ MS MX NI PA PE PR PY SR SV SX TC TT UY VC VE VG VI'.split()), 'Oceania': set('AS AU CK FJ FM GU KI MH MP NC NF NR NU NZ PF PG PW SB TK TO TV VU WF WS'.split()), 'Fictional': {'ATL', 'TER'}}
# Define `TODOS_LOS_PAISES` para reunir los códigos que se aceptan al pedir un país o elegir uno al azar.
TODOS_LOS_PAISES = set().union(*PAISES_POR_REGION.values())
# Define `NOMBRES_PAISES` para traducir códigos ISO y ficticios a nombres legibles.
NOMBRES_PAISES = {
    'AD': 'Andorra', 'AE': 'Emiratos Árabes Unidos', 'AF': 'Afganistán',
    'AG': 'Antigua y Barbuda', 'AI': 'Anguila', 'AL': 'Albania',
    'AM': 'Armenia', 'AN': 'Antillas Neerlandesas', 'AO': 'Angola',
    'AR': 'Argentina', 'AS': 'Samoa Americana', 'AT': 'Austria',
    'AU': 'Australia', 'AW': 'Aruba', 'AX': 'Islas Åland',
    'AZ': 'Azerbaiyán', 'BA': 'Bosnia y Herzegovina', 'BB': 'Barbados',
    'BD': 'Bangladés', 'BE': 'Bélgica', 'BF': 'Burkina Faso',
    'BG': 'Bulgaria', 'BH': 'Baréin', 'BI': 'Burundi', 'BJ': 'Benín',
    'BL': 'San Bartolomé', 'BM': 'Bermudas', 'BN': 'Brunéi',
    'BO': 'Bolivia', 'BQ': 'Caribe neerlandés', 'BR': 'Brasil',
    'BS': 'Bahamas', 'BW': 'Botsuana', 'BY': 'Bielorrusia',
    'BZ': 'Belice', 'CA': 'Canadá',
    'CD': 'República Democrática del Congo',
    'CF': 'República Centroafricana', 'CG': 'Congo', 'CH': 'Suiza',
    'CI': 'Costa de Marfil', 'CK': 'Islas Cook', 'CL': 'Chile',
    'CM': 'Camerún', 'CN': 'China', 'CO': 'Colombia',
    'CR': 'Costa Rica', 'CU': 'Cuba', 'CV': 'Cabo Verde',
    'CW': 'Curazao', 'CY': 'Chipre', 'CZ': 'Chequia',
    'DE': 'Alemania', 'DJ': 'Yibuti', 'DK': 'Dinamarca',
    'DM': 'Dominica', 'DO': 'República Dominicana', 'DZ': 'Argelia',
    'EC': 'Ecuador', 'EE': 'Estonia', 'EG': 'Egipto',
    'EH': 'Sáhara Occidental', 'ER': 'Eritrea', 'ES': 'España',
    'ET': 'Etiopía', 'FI': 'Finlandia', 'FJ': 'Fiyi',
    'FK': 'Islas Malvinas', 'FM': 'Micronesia', 'FO': 'Islas Feroe',
    'FR': 'Francia', 'GA': 'Gabón', 'GB': 'Reino Unido',
    'GD': 'Granada', 'GE': 'Georgia', 'GF': 'Guayana Francesa',
    'GG': 'Guernesey', 'GH': 'Ghana', 'GI': 'Gibraltar',
    'GL': 'Groenlandia', 'GM': 'Gambia', 'GN': 'Guinea',
    'GP': 'Guadalupe', 'GQ': 'Guinea Ecuatorial', 'GR': 'Grecia',
    'GT': 'Guatemala', 'GU': 'Guam', 'GW': 'Guinea-Bisáu',
    'GY': 'Guyana', 'HN': 'Honduras', 'HR': 'Croacia',
    'HT': 'Haití', 'HU': 'Hungría', 'ID': 'Indonesia',
    'IE': 'Irlanda', 'IL': 'Israel', 'IM': 'Isla de Man',
    'IN': 'India', 'IQ': 'Irak', 'IR': 'Irán', 'IS': 'Islandia',
    'IT': 'Italia', 'JE': 'Jersey', 'JM': 'Jamaica',
    'JO': 'Jordania', 'JP': 'Japón', 'KE': 'Kenia',
    'KG': 'Kirguistán', 'KH': 'Camboya', 'KI': 'Kiribati',
    'KM': 'Comoras', 'KN': 'San Cristóbal y Nieves',
    'KP': 'Corea del Norte', 'KR': 'Corea del Sur', 'KW': 'Kuwait',
    'KY': 'Islas Caimán', 'KZ': 'Kazajistán', 'LA': 'Laos',
    'LB': 'Líbano', 'LC': 'Santa Lucía', 'LI': 'Liechtenstein',
    'LK': 'Sri Lanka', 'LR': 'Liberia', 'LS': 'Lesoto',
    'LT': 'Lituania', 'LU': 'Luxemburgo', 'LV': 'Letonia',
    'LY': 'Libia', 'MA': 'Marruecos', 'MC': 'Mónaco',
    'MD': 'Moldavia', 'ME': 'Montenegro', 'MF': 'San Martín',
    'MG': 'Madagascar', 'MH': 'Islas Marshall',
    'MK': 'Macedonia del Norte', 'ML': 'Malí',
    'MM': 'Myanmar (Birmania)', 'MN': 'Mongolia',
    'MP': 'Islas Marianas del Norte', 'MQ': 'Martinica',
    'MR': 'Mauritania', 'MS': 'Montserrat', 'MT': 'Malta',
    'MU': 'Mauricio', 'MV': 'Maldivas', 'MW': 'Malaui',
    'MX': 'México', 'MY': 'Malasia', 'MZ': 'Mozambique',
    'NA': 'Namibia', 'NC': 'Nueva Caledonia', 'NE': 'Níger',
    'NF': 'Isla Norfolk', 'NG': 'Nigeria', 'NI': 'Nicaragua',
    'NL': 'Países Bajos', 'NO': 'Noruega', 'NP': 'Nepal',
    'NR': 'Nauru', 'NU': 'Niue', 'NZ': 'Nueva Zelanda',
    'OM': 'Omán', 'PA': 'Panamá', 'PE': 'Perú',
    'PF': 'Polinesia Francesa', 'PG': 'Papúa Nueva Guinea',
    'PH': 'Filipinas', 'PK': 'Pakistán', 'PL': 'Polonia',
    'PM': 'San Pedro y Miquelón', 'PR': 'Puerto Rico',
    'PS': 'Territorios Palestinos', 'PT': 'Portugal',
    'PW': 'Palaos', 'PY': 'Paraguay', 'QA': 'Catar',
    'RO': 'Rumanía', 'RS': 'Serbia', 'RU': 'Rusia', 'RW': 'Ruanda',
    'SA': 'Arabia Saudí', 'SB': 'Islas Salomón', 'SC': 'Seychelles',
    'SD': 'Sudán', 'SE': 'Suecia', 'SG': 'Singapur',
    'SI': 'Eslovenia', 'SJ': 'Svalbard y Jan Mayen',
    'SK': 'Eslovaquia', 'SL': 'Sierra Leona', 'SM': 'San Marino',
    'SN': 'Senegal', 'SO': 'Somalia', 'SR': 'Surinam',
    'SS': 'Sudán del Sur', 'ST': 'Santo Tomé y Príncipe',
    'SV': 'El Salvador', 'SX': 'Sint Maarten', 'SY': 'Siria',
    'SZ': 'Esuatini', 'TC': 'Islas Turcas y Caicos', 'TD': 'Chad',
    'TG': 'Togo', 'TH': 'Tailandia', 'TJ': 'Tayikistán',
    'TK': 'Tokelau', 'TL': 'Timor-Leste', 'TM': 'Turkmenistán',
    'TN': 'Túnez', 'TO': 'Tonga', 'TR': 'Turquía',
    'TT': 'Trinidad y Tobago', 'TV': 'Tuvalu', 'TW': 'Taiwán',
    'TZ': 'Tanzania', 'UA': 'Ucrania', 'UG': 'Uganda',
    'US': 'Estados Unidos', 'UY': 'Uruguay', 'UZ': 'Uzbekistán',
    'VA': 'Ciudad del Vaticano', 'VC': 'San Vicente y las Granadinas',
    'VE': 'Venezuela', 'VG': 'Islas Vírgenes Británicas',
    'VI': 'Islas Vírgenes de EE. UU.', 'VN': 'Vietnam',
    'VU': 'Vanuatu', 'WF': 'Wallis y Futuna', 'WS': 'Samoa',
    'YE': 'Yemen', 'ZA': 'Sudáfrica', 'ZM': 'Zambia',
    'ZW': 'Zimbabue', 'ATL': 'Atlantis', 'TER': 'Terrícola',
}
NOMBRES_PAISES_ESPECIALES = {'ATL': 'Atlantis', 'TER': 'Terrícola'}
# Define `BANCO_NOMBRES_POR_REGION` para ofrecer nombres de ejemplo separados por región y género.
BANCO_NOMBRES_POR_REGION = {'Africa': {'M': 'Omgombo Ayo Kwame Amadou Kofi Moussa Chidi Olu Tendai Thabo Sipho Bongani Mandela Sefu Jelani Zuberi Abasi Bakari Baraka Dakarai Faraji Hasani Idris Jabari Kato Lekan Mandla Nnamdi Obi Rashidi Said Tau Udo Yared Zola Abebe Ade Alemayehu Bamidele Cheikh Demba Femi Gamba Ikenna Kagiso Luthando Mosi Olumide Sadio Taye Mohamed'.split(), 'F': 'Amara Amina Zuri Fatou Nia Adanna Aaliyah Abena Adaeze Aisha Akosua Alaba Anuli Ayana Bolanle Binta Chiamaka Dayo Ebele Efua Eshe Folami Hadiya Imani Jamila Khadija Lulu Makena Malaika Mirembe Nala Ngozi Nkechi Ona Safiya Sade Thandiwe Yewande Zalika Zawadi Abeni Deka Esinam Ifunanya Kesia Lerato Mbali Nandi Sibongile'.split(), 'N': 'Ayo Imani Lesedi Sasha Kaya Kehinde Leke Mosa Neo Tendai Tumi Zola'.split()}, 'Asia': {'M': 'Murasakibara Haruto Yuto Sota Ren Yuki Daiki Akira Hiroshi Takeshi Kenji Riku Kaito Minato Jin Haru Takumi Arjun Aarav Vihaan Ishaan Rohan Dev Kabir Aditya Rahul Sanjay Ananda Budi Dimas Eko Fajar Hendra Indra Joko Surya Wei Ming Jun Tao Chen Liang Jian Seojun Jiho Hyun Minho Taeyang Sang Francisco Paco Ace Donald Mickey Sergio José'.split(), 'F': 'Damai Mei Aiko Yuna Sakura Ananya Hana Sora Aoi Emi Keiko Yui Rin Mio Ayaka Nari Hyejin Minji Soyeon Jiwoo Seoyeon Priya Diya Anika Kavya Isha Aditi Saanvi Meera Lakshmi Nisha Ayu Citra Dewi Intan Kartika Lestari Putri Ratna Sari Thao Linh Mai Ngoc Ying Xia Lan Hui Ning Amaya Mina'.split(), 'N': 'Kai Ren Akira Noa Haruka Hikaru Jun Makoto Min Sora Yuki Yu'.split()}, 'Europe': {'M': 'Antonio Izan Daniel Peter Ethan Santiago Luca Matteo Giovanni Alessandro Enzo Nikolai Milan Lukas Felix Leon Oscar Hugo Gabriel Adrian Mateo Pablo Javier Diego Andres Rafael Tiago Joao Dimitri Andrei Stefan Marek Tomas Jan Kacper Bjorn Soren Magnus Oliver Arthur Louis Theo Hendrik Emil Rasmus Ivo Mihai Viktor Boris Aleksandar Kristian Marcos Marco Cristian'.split(), 'F': 'Sofia Mia Elena Lucia Freya Ines Giulia Francesca Alessia Chiara Isabella Valentina Martina Camila Carmen Irene Clara Alba Marina Laia Ainhoa Catalina Beatriz Leonor Matilde Anais Amelie Celine Margot Louise Chloe Astrid Greta Ingrid Linnea Katarina Zuzana Klara Anja Milena Nadia Tatiana Eliska Dagmar Ewa Maja Zofia Daphne Iris Theodora'.split(), 'N': 'Alex Noa Dani Andrea Ari Cleo Dominique Eden Luca Mika Sasha Teo'.split()}, 'North America': {'M': 'Anthony Noah James Liam Mason Logan Benjamin Elijah Lucas Maverick Jackson Aiden Carter Wyatt Grayson Owen Levi Caleb Isaac Ezra Miles Dylan Hunter Cooper Easton Asher Jaxon Connor Parker Austin Chase Derek Malik Xavier Andre Joaquin Emilio Rafael Tomas Diego Luis Mateo Thiago Ramon Carlos José Cruz Orion Phoenix River'.split(), 'F': 'Olivia Emma Maya Ava Harper Evelyn Abigail Emily Ella Scarlett Grace Chloe Zoey Riley Nora Lily Hannah Layla Ellie Paisley Violet Aurora Savannah Brooklyn Kennedy Skylar Madison Addison Aubrey Claire Naomi Gabriella Aaliyah Jade Amara Mackenzie Sierra Brianna Kiara Mckenna Dakota Sage Peyton Morgan Taylor Avery Quinn Reese Rowan Wren'.split(), 'N': 'Alex Jordan Taylor Noa Avery Cameron Casey Drew Jamie Morgan Parker Quinn'.split()}, 'South America': {'M': 'Santiago Mateo Thiago Joao Pedro Gabriel Davi Heitor Bernardo Lorenzo Enzo Miguel Arthur Theo Benicio Gael Ravi Nicolas Benjamin Samuel Lucas Martin Tomas Felipe Joaquin Agustin Facundo Lautaro Franco Bruno Emiliano Maximo Benjamim Caio Murilo Ruan Leandro Ronaldo Eder Cauã Yago Iker Cristobal Esteban Renato Jorge Manuel Luciano Dante Alonso'.split(), 'F': 'Valentina Camila Isabella Antonella Manuela Isabel Helena Alice Laura Luiza Heloisa Cecilia Luna Aurora Maite Martina Emilia Julieta Renata Bianca Agustina Florencia Catalina Josefina Abril Alma Pilar Milagros Aitana Mariana Daniela Gabriela Fernanda Bruna Leticia Yasmin Larissa Beatriz Vitória Eloá Isadora Manuella Rafaela Talita Noemi Paloma Clarice Catarina Iara Luz'.split(), 'N': 'Alex Dani Noa Ariel Cris Dara Gael Guadalupe Jaci Jules Ren Sol'.split()}, 'Oceania': {'M': 'Kai Manaia Tane Ariki Ari Wiremu Tama Rangi Tawhiri Nikau Koa Ihaia Matiu Rawiri Tui Hemi Tamauri Anaru Hoani Pita Niko Jone Sione Tevita Leka Semisi Manu Iosefa Fetu Malakai Afa Peni Viliami Solomon Lachlan Hamish Angus Callum Rhys Flynn Bodhi Jai Arlo Coen Dane Kieran Marlow Taj Zac'.split(), 'F': 'Moana Anahera Aroha Mere Maia Marama Hine Kiri Ataahua Ria Awhina Hinemoa Kaia Mele Litia Salote Malia Luisa Sina Fia Talia Leilani Alani Kalani Mahana Aulani Mauri Siale Teuila Mereana Kiriana Aniva Isla Matilda Charlotte Harriet Poppy Evie Ruby Mila Willow Indi Tahlia Imogen Freya Zara Elodie Sienna Pippa Clementine'.split(), 'N': 'Ari Kai Noa Riley Aroha Haru Kauri Koa Manu Mika Tui Wai'.split()}, 'Fictional': {'M': ('Izan', 'Ethan', 'Daniel', 'Murasakibara', 'Omgombo'), 'F': ('Amara', 'Mia', 'Sofia', 'Aiko', 'Zuri', 'Noa', 'Damai'), 'N': ('Alex', 'Ari', 'Kai', 'Noa')}}
# Define `NOMBRES_ADICIONALES_POR_REGION` para guardar más nombres que pueden incorporarse a los bancos regionales.
NOMBRES_ADICIONALES_POR_REGION = {'Africa': {'M': 'Abdou Abiola Abiodun Abioye Adewale Afolabi Agyei Akintunde Amare Ashenafi Ayodele Babatunde Bhekizizwe Chike Chisom Dayo Ekon Enoch Fikru Ganiu Gebre Hakeem Kelechi Khamisi Lamine Madu Nkosana Oladipo Olufemi Onyeka Sekou Tafari Ubong Useni Yaw', 'F': 'Abosede Aderonke Afolake Akachi Alaba Alemitu Almaz Anaya Ashanti Bimpe Chidinma Chinwe Dalia Dalmar Eniola Faduma Foluke Gbemisola Halima Ifeoma Kadija Kaltuma Kanyinsola Kikelomo Masego Mojisola Nkiruka Oluchi Omolara Simisola Temitope Uchenna Wanjiku Yaa', 'N': 'Desta Fisayo Kalu Kwezi Nuru Rehema Sanyu Tinashe Zikomo'.split()}, 'Asia': {'M': 'Abdul Akio Akiro Anwar Bao Bảo Byung Chan Chang Daisuke Eiji Faisal Farhan Goku Hakim Hitoshi Isamu Jae Joon Kazuki Kenta Le Minh Nam Naveen Nikhil Pranav Qiang Ramesh Rizwan Ryota San Satoshi Shota Tariq Tenzin Usman Vinh Xiaobo Yao Yash Zain', 'F': 'Aaradhya Akari Amrita Anushka Asma Bảo Bich Chiyo Dawa Eri Farah Fatima Hikari Hoa Indira Jaya Jyoti Kanya Khushi Kyoko Laila Malini Mariam Nandini Noor Parvati Qian Rina Roshni Samira Shreya Sonam Tenzin Usha Vanna Xiu Yasmin Zahra', 'N': 'Ashwin Baek Dae Huan Kiran Lian Nima Pema Qori Sen Umang'.split()}, 'Europe': {'M': 'Alvaro Ander Borja Bruno Carles Caspar Cesc Dario Elio Esteban Ferran Francisco Gorka Guillem Iago Ismael Jacobo Jesús Jon Marc Marcos Mikel Nacho Pau Paco Quim Raul Sergio Unai Xabier Yago Agustin Alistair Alphonse Anselm Bastian Cillian', 'F': 'Adela Aina Alicia Amalia Ana Angela Arantxa Ariadna Blanca Bruna Carlota Covadonga Daniela Elia Elisa Estrella Eva Fiona Gabriela Ines Jimena Joana Leire Lola Mar Marionna Maria Marisol Nuria Olalla Raquel Rocio Salome Teresa Ursula Vega Ximena Yaiza Adriana Almudena Candela', 'N': 'Aimar Aitzol Andrea Eneko Izar Jules Kim Noa Pau Tristan'.split()}, 'North America': {'M': 'Ace Adam Adrian Alan Albert Amos Andy Antonio Archie Arlo August Beau Beckett Bowie Brooks Camden Clark Cody Colt Damian Dean Donald Dustin Edgar Edward Elliot Felix Finn Forrest Frank Frankie George Graham Henry Mickey Nico Oscar Otto Percy Reid Remy Salvador Simon Spencer Victor Wesley', 'F': 'Adeline Alice Amara Amelia Angelica Annabelle Annie Beatrice Bella Bonnie Callie Caroline Cecilia Daisy Delilah Eden Eleanor Eliza Esther Francesca Georgia Hazel Iris Josephine Juliet Katherine Leah Maeve Margot Maria Marionna Matilda Molly Nina Opal Rose Ruby Sadie Stella Thea Vera Winnie', 'N': 'Angel Billie Blair Charlie Darcy Emerson Hollis Indigo Kit Lennon Marlowe'.split()}, 'South America': {'M': 'Alejandro Alexis Alfonso Alvaro Anibal Antonio Armando Bastian Batman Bautista Ciro Claudio Dario Eduardo Ezequiel Fabio Fabricio Francisco Gael Gonzalo Ignacio Ivan Jacinto Javier Jeremias Jesús Leonel Lorenzo Luciano Marcelo Mariano Mario Nicolas Paco Patricio Piero Ramiro Sergio Vicente', 'F': 'Agustina Amparo Ana Antonella Ariadna Aurora Belen Brisa Carolina Constanza Delfina Dolores Emilia Esmeralda Estefania Guadalupe Ines Josefina Juana Juliana Malena Maria Marionna Milena Mora Olivia Paloma Pilar Rocio Rosario Salome Trinidad Violeta Xiomara Zaira Zoe', 'N': 'Amaru Azul Beltran Cruz Inti Jani Lujan Mar Sol Thiago'.split()}, 'Oceania': {'M': 'Aidan Albie Archie Ariki Blake Cooper Darcy Eli Finn George Hamish Harrison Hunter Jack Lachie Lewis Liam Mason Mitchell Ned Oliver Oscar Patrick Quinn Reuben Sam Samuel Sonny Spencer Stanley Thomas Toby Tom Vincent Xavier', 'F': 'Aisha Alice Annabelle Arabella Bonnie Chelsea Ella Elsie Frankie Georgia Grace Harlow Hazel Isla Jemima Jessica Kate Layla Lily Lucy Mackenzie Maisie Matilda Millie Olive Paige Phoebe Piper Quinn Rose Ruby Sadie Sophie Summer Violet Zoe', 'N': 'Ash Billie Charlie Darcy Frankie Jules Kelly Lake Mackenzie Robin'.split()}, 'Fictional': {'M': 'Ace Donald Mickey Paco Francisco José Sergio'.split(), 'F': 'Damai Maria Marionna Pilar'.split(), 'N': 'Alex Ari Kai Noa'.split()}}
# Define `NOMBRES_EXTRA_POR_REGION` para guardar otra colección de nombres regionales usados por el simulador.
NOMBRES_EXTRA_POR_REGION = {'Africa': {'M': 'Abanoub Abayomi Abdi Abiola Abubakar Adisa Akin Akinyi Amadou Amari Amadouba Anas Anwar Babacar Boubacar Cheikh Daouda Diarra El Hadji Fodé Habib Ibrahima Ismail Koffi Mamadou Modibo Oumar Samba Sékou Souleymane Youssouf Abdullahi Biko Chibuzo Dlamini Fikile Gamba Juma Khamisi Lethabo Makhaya Mlungisi Nkosinathi Obinna Olumide Paki Themba Thulani Uche Wekesa', 'F': 'Aïssatou Awa Binta Coumba Diarra Fatoumata Fanta Hawa Khady Kumba Mariama Mame Mounia Ndeye Rokhaya Salimata Sira Sokhna Tenin Yacine Yasmin Zainab Abimbola Abla Adia Afiya Aisha Amondi Asha Bontle Chiamaka Eshe Fikile Gugu Ijeoma Kendi Lindiwe Mpho Nia Nomsa Onika Palesa Rehema', 'N': 'Amari Bayo Kande Sadio Sira Yacine Amani Banele Khotso Lindi'.split()}, 'Asia': {'M': 'Akihiko Akira Arata Asahi Daichi Eren Hiro Hoshi Issei Kiyoshi Kouki Kuro Lee Masaru Naoki Noboru Osamu Ryo Shiro Takashi Taro Tomoya Yoshi Yoshiro Yuma Kintaro Rentarou Akash Amrit Aravind Bharat Chandra Deven Gaurav Harish Jatin Kalyan Manish Om Prakash Suresh Vikas Enrique Coque Josemari Nishio Michael Toñete Isaias Isaac Adolf Izuku Shoto Ywatch Nathan Goku Teseo Mario Rayman Raimond Raimundo Rick Morty Homer Sócrates Leónidas Sukuna Naruto Ali Steve Miguel Morato Benito', 'F': 'Aimi Akane Amaya Asami Chika Etsuko Fumiko Harumi Hitomi Izumi Kaede Koharu Kumi Madoka Nanami Natsuki Nozomi Rei Riko Sayuri Shizuka Sumire Yoko Yukiko Damai Mai Mei Anjali Bhavna Charu Deepa Gauri Indu Kalpana Lalita Neha Pooja Rani Sita Tanvi Uma Mina Laura Ochako Alba Summer Mia Rosa Amparo Nona', 'N': 'Aki Chihiro Honekushi Itsuki Kaoru Kazumi Nao Puppet Aoi Fumi Nori Kyubutsu Sura Tenko Zewhui Pikachu Capi Toad Po Angra Spenta Bobi'.split()}, 'Europe': {'M': 'Alcides Alistair Ambrose Ansel Arthur Bael Belial Basil Benedict Casimir Cedric Jesús Zeus Leviatán Clement Conrad Dorian Edmund Elias Fabian Florian Hugo Ignatius Leopold Lucian Matthias Maximilian Octavian Percival Quentin Raphael Sebastian Tristan Ulysses Valentin Xavier Alaric Ambrosius Arvid Balthazar Cassian Cosmo Evander Hadrian Isidore Lysander Peregrine Stellan Thaddeus Valerian Wolfgang', 'F': 'Adelaide Agnes Antonia Beatrix Celeste Cordelia Delphine Elodie Estelle Evangeline Florence Genevieve Helena Isadora Josephine Lavinia Marguerite Octavia Ophelia Penelope Philippa Seraphina Sylvia Theodora Vivienne Adelina Agatha Anastasia Annika Aurelia Cecily Eleanora Eulalia Gwendolyn Henrietta Isolde Leonora Lucinda Magnolia Mirabel Ottilie Rosalind', 'N': 'Aubrey Camille Dominique Ellis Hollis Jules Noa Remy Robin Arden Bellamy'.split()}, 'North America': {'M': 'Alcides Amos Arthur Atticus Axel Beckett Bennett Brooks Calvin Caspian Cyrus Declan Everett Felix Finn Gideon Jasper Jonah Julian Milo Nathaniel Nolan Percy Quentin Ronan Silas Theodore Wesley Wyatt Zachary Freddy Eduardo Alistair Anderson August Banks Bowen Colson Desmond Everett Franklin Garrett Holden Israel Jett Keaton Lawson Maddox Preston Sterling Thayer', 'F': 'Adeline Annika Aurora Brielle Callista Celeste Delaney Elowen Ember Esme Fiona Freya Gemma Hazel Isla Juniper Liana Maeve Nadia Ophelia Phoebe Quinn Rowan Sloane Tessa Willa Alana Aspen Cassidy Colette Daphne Elodie Felicity Heidi Jocelyn Laurel Mallory Noelle Priscilla Ramona Sabrina Teagan', 'N': 'Auden Bellamy Briar Chus Hollis Indigo Kit Lane Lyric Onyx Scout Shiloh Sidney'.split()}, 'South America': {'M': 'Alcides Baltazar Camilo Dante Elias Facundo Gaspar Isandro Leandro Lorenzo Matias Octavio Ramiro Salvador Teodoro Valentín Xavier Zacarías Ademar Alvaro Amadeo Anselmo Apolo Ciro Damián Elian Estanislao Fabricio Hernan Lisandro Nahuel Rafael Santino Tadeo', 'F': 'Alondra Amalia Anahi Ayelen Bruna Candelaria Delfina Eliana Fiorella Isidora Josefina Luciana Malena Micaela Rocio Selena Tamara Uxia Valeria Ysabel Ailén Anabella Antonina Carmela Delfina Elvira Guillermina Irupé Jimena Luján Maribel Nuria Perla Romina Soledad', 'N': 'Ariel Cielo Irupe Luan Maru Paz Belén Cris Eluney Jasy'.split()}, 'Oceania': {'M': 'Arihi Atarangi Hemi Kahu Kauri Māui Nikau Pounamu Rāwiri Rongo Tāne Tūmatauenga Whakaari Awanui Eruera Haami Kahurangi Makarini Paora Pita Ropata Tame Tāmati', 'F': 'Aroha Atarangi Hinewai Kahurangi Marama Matariki Pounamu Raukura Rongomai Tiare Waiora Anahera Hinerangi Kiriwai Maata Ngaio Parehuia Rereata Te Aroha', 'N': 'Ahi Hoku Kiri Mahi Nalu Awhi Huriwai'.split()}, 'Fictional': {'M': 'Bael Belial Eduardo Freddy Jesús Kintaro Leviatán Zeus Chus Rentarou Honekushi Alcides Elmo', 'F': 'Mai Mei Shizuka Damai'.split(), 'N': 'Alex Chus Puppet'.split()}}
# Crea `NOMBRES_ESPECIALES_POR_GENERO` con los datos u opciones que se procesan después.
NOMBRES_ESPECIALES_POR_GENERO = {'M': 'Alcides Zeus Jesús Bael Belial Leviatán Kintaro Rentarou Freddy Eduardo Gabriel Sergio', 'F': 'Damai Shizuka Mai Mei Marionna Maria Pilar', 'N': 'Chus Alex Puppet Honekushi'}
# Recorre `NOMBRES_ADICIONALES_POR_REGION.items()`; ejecuta el bloque una vez por cada valor asignado a `(region, nombres_por_genero)`.
for region, nombres_por_genero in NOMBRES_ADICIONALES_POR_REGION.items():
    # Recorre `nombres_por_genero.items()`; ejecuta el bloque una vez por cada valor asignado a `(genero_nombre, nombres_adicionales)`.
    for genero_nombre, nombres_adicionales in nombres_por_genero.items():
        # Calcula y guarda en `BANCO_NOMBRES_POR_REGION[region][genero_nombre]` el valor que se necesita en las instrucciones siguientes.
        BANCO_NOMBRES_POR_REGION[region][genero_nombre] = tuple(BANCO_NOMBRES_POR_REGION[region][genero_nombre]) + tuple(nombres_adicionales.split() if isinstance(nombres_adicionales, str) else nombres_adicionales)
# Recorre `NOMBRES_EXTRA_POR_REGION.items()`; ejecuta el bloque una vez por cada valor asignado a `(region, nombres_por_genero)`.
for region, nombres_por_genero in NOMBRES_EXTRA_POR_REGION.items():
    # Recorre `nombres_por_genero.items()`; ejecuta el bloque una vez por cada valor asignado a `(genero_nombre, nombres_adicionales)`.
    for genero_nombre, nombres_adicionales in nombres_por_genero.items():
        # Calcula y guarda en `BANCO_NOMBRES_POR_REGION[region][genero_nombre]` el valor que se necesita en las instrucciones siguientes.
        BANCO_NOMBRES_POR_REGION[region][genero_nombre] = tuple(BANCO_NOMBRES_POR_REGION[region][genero_nombre]) + tuple(nombres_adicionales.split() if isinstance(nombres_adicionales, str) else nombres_adicionales)
# Recorre `NOMBRES_ESPECIALES_POR_GENERO.items()`; ejecuta el bloque una vez por cada valor asignado a `(genero_nombre, nombres_especiales)`.
for genero_nombre, nombres_especiales in NOMBRES_ESPECIALES_POR_GENERO.items():
    # Calcula y guarda en `BANCO_NOMBRES_POR_REGION['Fictional'][genero_nombre]` el valor que se necesita en las instrucciones siguientes.
    BANCO_NOMBRES_POR_REGION['Fictional'][genero_nombre] = tuple(BANCO_NOMBRES_POR_REGION['Fictional'][genero_nombre]) + tuple(nombres_especiales.split())

# Define `clave_normalizada_nombre` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def clave_normalizada_nombre(nombre):
    """Normaliza un nombre para detectar duplicados ignorando acentos y mayúsculas."""
    # Guarda en `nombre_sin_acentos` el resultado de obtener el resultado de `''.join`; se reutiliza en los pasos siguientes.
    nombre_sin_acentos = ''.join((caracter for caracter in unicodedata.normalize('NFKD', nombre) if not unicodedata.combining(caracter)))
    # Devuelve `nombre_sin_acentos.casefold()` al código que llamó a esta función.
    return nombre_sin_acentos.casefold()

# Define `quitar_nombres_duplicados` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def quitar_nombres_duplicados(nombres):
    """Conserva el primer nombre y elimina repeticiones por grafía normalizada."""
    # Crea `unicos` con los datos u opciones que se procesan después.
    unicos = []
    # Guarda en `vistos` el resultado de obtener el resultado de `set`; se reutiliza en los pasos siguientes.
    vistos = set()
    # Recorre `nombres`; ejecuta el bloque una vez por cada valor asignado a `nombre`.
    for nombre in nombres:
        # Guarda en `clave` el resultado de obtener el resultado de `clave_normalizada_nombre`; se reutiliza en los pasos siguientes.
        clave = clave_normalizada_nombre(nombre)
        # Comprueba `clave and clave not in vistos`; solo ejecuta este bloque cuando se cumple la condición.
        if clave and clave not in vistos:
            # Incorpora un elemento al conjunto, evitando duplicados.
            # Incorporar un elemento al conjunto sin crear duplicados.
            vistos.add(clave)
            # Añadir un solo elemento a la lista que se está construyendo.
            unicos.append(nombre)
    # Devuelve `tuple(unicos)` al código que llamó a esta función.
    return tuple(unicos)

# Se normalizan los bancos al arrancar: los nombres repetidos entre géneros pasan
# al conjunto neutro y se evita reutilizar el mismo nombre en distintas regiones.
# Recorre `BANCO_NOMBRES_POR_REGION.values()`; ejecuta el bloque una vez por cada valor asignado a `banco_region`.
for banco_region in BANCO_NOMBRES_POR_REGION.values():
    # Recorre `banco_region.items()`; ejecuta el bloque una vez por cada valor asignado a `(genero_nombre, nombres)`.
    for genero_nombre, nombres in banco_region.items():
        # Guarda en `banco_region[genero_nombre]` el resultado de obtener el resultado de `quitar_nombres_duplicados`; se reutiliza en los pasos siguientes.
        banco_region[genero_nombre] = quitar_nombres_duplicados(nombres)
    # Crea `claves_por_genero` con los datos u opciones que se procesan después.
    claves_por_genero = {genero_nombre: {clave_normalizada_nombre(nombre) for nombre in nombres} for genero_nombre, nombres in banco_region.items()}
    # Calcula y guarda en `claves_compartidas` el valor que se necesita en las instrucciones siguientes.
    claves_compartidas = claves_por_genero['M'] & claves_por_genero['F'] | claves_por_genero['M'] & claves_por_genero['N'] | claves_por_genero['F'] & claves_por_genero['N']
    # Guarda en `nombres_neutros` el resultado de obtener el resultado de `list`; se reutiliza en los pasos siguientes.
    nombres_neutros = list(banco_region['N'])
    # Guarda en `claves_neutras` el resultado de obtener el resultado de `set`; se reutiliza en los pasos siguientes.
    claves_neutras = set(claves_por_genero['N'])
    # Recorre `('M', 'F')`; ejecuta el bloque una vez por cada valor asignado a `genero_nombre`.
    for genero_nombre in ('M', 'F'):
        # Crea `nombres_exclusivos` con los datos u opciones que se procesan después.
        nombres_exclusivos = []
        # Recorre `banco_region[genero_nombre]`; ejecuta el bloque una vez por cada valor asignado a `nombre`.
        for nombre in banco_region[genero_nombre]:
            # Guarda en `clave` el resultado de obtener el resultado de `clave_normalizada_nombre`; se reutiliza en los pasos siguientes.
            clave = clave_normalizada_nombre(nombre)
            # Comprueba `clave in claves_compartidas`; solo ejecuta este bloque cuando se cumple la condición.
            if clave in claves_compartidas:
                # Comprueba `clave not in claves_neutras`; solo ejecuta este bloque cuando se cumple la condición.
                if clave not in claves_neutras:
                    # Añadir un solo elemento a la lista que se está construyendo.
                    nombres_neutros.append(nombre)
                    # Incorpora un elemento al conjunto, evitando duplicados.
                    # Incorporar un elemento al conjunto sin crear duplicados.
                    claves_neutras.add(clave)
            # Si `clave in claves_compartidas` no se cumple, ejecuta esta alternativa.
            else:
                # Añadir un solo elemento a la lista que se está construyendo.
                nombres_exclusivos.append(nombre)
        # Guarda en `banco_region[genero_nombre]` el resultado de obtener el resultado de `tuple`; se reutiliza en los pasos siguientes.
        banco_region[genero_nombre] = tuple(nombres_exclusivos)
    # Guarda en `banco_region['N']` el resultado de obtener el resultado de `quitar_nombres_duplicados`; se reutiliza en los pasos siguientes.
    banco_region['N'] = quitar_nombres_duplicados(nombres_neutros)
# Guarda en `nombres_vistos_globalmente` el resultado de obtener el resultado de `set`; se reutiliza en los pasos siguientes.
nombres_vistos_globalmente = set()
# Recorre `BANCO_NOMBRES_POR_REGION.values()`; ejecuta el bloque una vez por cada valor asignado a `banco_region`.
for banco_region in BANCO_NOMBRES_POR_REGION.values():
    # Recorre `('M', 'F', 'N')`; ejecuta el bloque una vez por cada valor asignado a `genero_nombre`.
    for genero_nombre in ('M', 'F', 'N'):
        # Crea `nombres_unicos` con los datos u opciones que se procesan después.
        nombres_unicos = []
        # Recorre `banco_region[genero_nombre]`; ejecuta el bloque una vez por cada valor asignado a `nombre`.
        for nombre in banco_region[genero_nombre]:
            # Guarda en `clave` el resultado de obtener el resultado de `clave_normalizada_nombre`; se reutiliza en los pasos siguientes.
            clave = clave_normalizada_nombre(nombre)
            # Comprueba `clave not in nombres_vistos_globalmente`; solo ejecuta este bloque cuando se cumple la condición.
            if clave not in nombres_vistos_globalmente:
                # Incorpora un elemento al conjunto, evitando duplicados.
                # Incorporar un elemento al conjunto sin crear duplicados.
                nombres_vistos_globalmente.add(clave)
                # Añadir un solo elemento a la lista que se está construyendo.
                nombres_unicos.append(nombre)
        # Guarda en `banco_region[genero_nombre]` el resultado de obtener el resultado de `tuple`; se reutiliza en los pasos siguientes.
        banco_region[genero_nombre] = tuple(nombres_unicos)
# Define `PROVINCIAS_ESPANA` para asociar provincias con localidades españolas disponibles.
PROVINCIAS_ESPANA = {'A Coruña': ['A Coruña', 'Santiago de Compostela'], 'Albacete': ['Albacete'], 'Alicante': ['Alicante', 'Elche'], 'Almería': ['Almería'], 'Araba/Álava': ['Vitoria-Gasteiz'], 'Asturias': ['Oviedo', 'Gijón'], 'Ávila': ['Ávila'], 'Badajoz': ['Badajoz', 'Mérida'], 'Barcelona': ['Barcelona', 'Montcada i Reixac'], 'Burgos': ['Burgos'], 'Cáceres': ['Cáceres'], 'Cádiz': ['Cádiz', 'San Roque'], 'Cantabria': ['Santander'], 'Castellón': ['Castellón de la Plana'], 'Ciudad Real': ['Ciudad Real'], 'Córdoba': ['Córdoba'], 'Cuenca': ['Cuenca'], 'Girona': ['Girona', 'La Junquera'], 'Granada': ['Granada'], 'Guadalajara': ['Guadalajara'], 'Gipuzkoa': ['San Sebastián'], 'Huelva': ['Huelva'], 'Huesca': ['Huesca'], 'Illes Balears': ['Palma'], 'Jaén': ['Jaén'], 'León': ['León', 'Ponferrada'], 'Lleida': ['Lleida'], 'Lugo': ['Lugo'], 'Madrid': ['Madrid', 'Alcalá de Henares'], 'Málaga': ['Málaga', 'Marbella'], 'Murcia': ['Murcia', 'Cartagena'], 'Navarra': ['Pamplona'], 'Ourense': ['Ourense'], 'Palencia': ['Palencia'], 'Las Palmas': ['Las Palmas de Gran Canaria'], 'Pontevedra': ['Pontevedra', 'Vigo'], 'La Rioja': ['Logroño'], 'Salamanca': ['Salamanca'], 'Santa Cruz de Tenerife': ['Santa Cruz de Tenerife'], 'Segovia': ['Segovia'], 'Sevilla': ['Sevilla'], 'Soria': ['Soria'], 'Tarragona': ['Tarragona'], 'Teruel': ['Teruel'], 'Toledo': ['Toledo'], 'Valencia': ['Valencia'], 'Valladolid': ['Valladolid'], 'Bizkaia': ['Bilbao'], 'Zamora': ['Zamora'], 'Zaragoza': ['Zaragoza'], 'Ceuta': ['Ceuta'], 'Melilla': ['Melilla']}
# Define `ESTADOS_UNIDOS` para listar estados que se ofrecen como localidades estadounidenses.
ESTADOS_UNIDOS = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Carolina del Norte', 'Carolina del Sur', 'Colorado', 'Connecticut', 'Dakota del Norte', 'Dakota del Sur', 'Delaware', 'Florida', 'Georgia', 'Hawái', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Luisiana', 'Maine', 'Maryland', 'Massachusetts', 'Míchigan', 'Minnesota', 'Misisipi', 'Misuri', 'Montana', 'Nebraska', 'Nevada', 'Nueva Jersey', 'Nueva York', 'Nuevo Hampshire', 'Nuevo México', 'Ohio', 'Oklahoma', 'Oregón', 'Pensilvania', 'Rhode Island', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Virginia Occidental', 'Washington', 'Wisconsin', 'Wyoming']
# Define `LOCALIDADES_POR_PAIS` para asociar cada país con localidades posibles para el nacimiento.
LOCALIDADES_POR_PAIS = {'ATL': ['Atlantis'], 'AD': ['Andorra la Vella', 'Escaldes-Engordany'], 'AR': ['Buenos Aires', 'Córdoba', 'Rosario'], 'AU': ['Canberra', 'Sídney', 'Melbourne'], 'AT': ['Viena', 'Graz', 'Salzburgo'], 'BE': ['Bruselas', 'Amberes', 'Gante'], 'BO': ['Sucre', 'La Paz', 'Santa Cruz de la Sierra'], 'BR': ['Brasilia', 'São Paulo', 'Río de Janeiro'], 'CA': ['Ottawa', 'Toronto', 'Vancouver'], 'CL': ['Santiago', 'Valparaíso', 'Concepción'], 'CN': ['Pekín', 'Shanghái', 'Cantón'], 'CO': ['Bogotá', 'Medellín', 'Cali'], 'CU': ['La Habana', 'Santiago de Cuba'], 'CZ': ['Praga', 'Brno', 'Ostrava'], 'DE': ['Berlín', 'Hamburgo', 'Múnich'], 'DK': ['Copenhague', 'Aarhus'], 'EG': ['El Cairo', 'Alejandría'], 'ES': [ciudad for ciudades in PROVINCIAS_ESPANA.values() for ciudad in ciudades], 'FI': ['Helsinki', 'Tampere', 'Turku'], 'FR': ['París', 'Lyon', 'Marsella'], 'GB': ['Londres', 'Manchester', 'Edimburgo'], 'GR': ['Atenas', 'Salónica'], 'HU': ['Budapest', 'Debrecen'], 'ID': ['Yakarta', 'Surabaya', 'Bandung'], 'IE': ['Dublín', 'Cork', 'Galway'], 'IL': ['Jerusalén', 'Tel Aviv'], 'IN': ['Nueva Delhi', 'Bombay', 'Bangalore'], 'IS': ['Reikiavik', 'Akureyri'], 'IT': ['Roma', 'Milán', 'Nápoles'], 'JP': ['Tokio', 'Osaka', 'Kioto'], 'KR': ['Seúl', 'Busan', 'Incheon'], 'MA': ['Rabat', 'Casablanca', 'Marrakech'], 'MX': ['Ciudad de México', 'Guadalajara', 'Monterrey'], 'NG': ['Abuya', 'Lagos', 'Kano'], 'NL': ['Ámsterdam', 'Róterdam', 'La Haya'], 'NO': ['Oslo', 'Bergen', 'Trondheim'], 'NZ': ['Wellington', 'Auckland', 'Christchurch'], 'PE': ['Lima', 'Cusco', 'Arequipa'], 'PH': ['Manila', 'Cebú', 'Dávao'], 'PL': ['Varsovia', 'Cracovia', 'Gdansk'], 'PT': ['Lisboa', 'Oporto', 'Coímbra'], 'RU': ['Moscú', 'San Petersburgo', 'Novosibirsk'], 'SA': ['Riad', 'Yeda', 'La Meca'], 'SE': ['Estocolmo', 'Gotemburgo', 'Malmö'], 'SG': ['Singapur'], 'TH': ['Bangkok', 'Chiang Mai', 'Phuket'], 'TR': ['Ankara', 'Estambul', 'Esmirna'], 'TW': ['Taipéi', 'Kaohsiung'], 'TER': ['Terrícola'], 'UA': ['Kyiv', 'Járkiv', 'Odesa'], 'US': ESTADOS_UNIDOS + ['Washington D. C.', 'Nueva York', 'Los Ángeles'], 'VE': ['Caracas', 'Maracaibo', 'Valencia'], 'VN': ['Hanói', 'Ciudad Ho Chi Minh', 'Da Nang'], 'ZA': ['Pretoria', 'Ciudad del Cabo', 'Johannesburgo']}
# Define `CAPITALES_POR_PAIS` para dar una localidad de respaldo cuando no hay ciudades catalogadas.
CAPITALES_POR_PAIS = {'ATL': 'Atlantis', 'AD': 'Andorra la Vella', 'AE': 'Abu Dhabi', 'AF': 'Kabul', 'AG': "St. John's", 'AI': 'The Valley', 'AL': 'Tirana', 'AM': 'Yerevan', 'AN': 'Willemstad', 'AO': 'Luanda', 'AR': 'Buenos Aires', 'AS': 'Pago Pago', 'AT': 'Viena', 'AU': 'Canberra', 'AW': 'Oranjestad', 'AX': 'Mariehamn', 'AZ': 'Baku', 'BA': 'Sarajevo', 'BB': 'Bridgetown', 'BD': 'Dhaka', 'BE': 'Bruselas', 'BF': 'Ouagadougou', 'BG': 'Sofía', 'BH': 'Manama', 'BI': 'Gitega', 'BJ': 'Porto-Novo', 'BL': 'Gustavia', 'BM': 'Hamilton', 'BN': 'Bandar Seri Begawan', 'BO': 'Sucre', 'BQ': 'Willemstad', 'BR': 'Brasilia', 'BS': 'Nassau', 'BW': 'Gaborone', 'BY': 'Minsk', 'BZ': 'Belmopan', 'CA': 'Ottawa', 'CD': 'Kinshasa', 'CF': 'Bangui', 'CG': 'Brazzaville', 'CH': 'Berna', 'CI': 'Yamoussoukro', 'CK': 'Avarua', 'CL': 'Santiago', 'CM': 'Yaoundé', 'CN': 'Pekín', 'CO': 'Bogotá', 'CR': 'San José', 'CU': 'La Habana', 'CV': 'Praia', 'CW': 'Willemstad', 'CY': 'Nicosia', 'CZ': 'Praga', 'DE': 'Berlín', 'DJ': 'Yibuti', 'DK': 'Copenhague', 'DM': 'Roseau', 'DO': 'Santo Domingo', 'DZ': 'Argel', 'EC': 'Quito', 'EE': 'Tallin', 'EG': 'El Cairo', 'EH': 'El Aaiún', 'ER': 'Asmara', 'ES': 'Madrid', 'ET': 'Adís Abeba', 'FI': 'Helsinki', 'FJ': 'Suva', 'FK': 'Stanley', 'FM': 'Palikir', 'FO': 'Tórshavn', 'FR': 'París', 'GA': 'Libreville', 'GB': 'Londres', 'GD': "St. George's", 'GE': 'Tiflis', 'GF': 'Cayena', 'GG': 'St Peter Port', 'GH': 'Acra', 'GI': 'Gibraltar', 'GL': 'Nuuk', 'GM': 'Banjul', 'GN': 'Conakri', 'GP': 'Basse-Terre', 'GQ': 'Ciudad de la Paz', 'GR': 'Atenas', 'GT': 'Ciudad de Guatemala', 'GU': 'Hagåtña', 'GW': 'Bisáu', 'GY': 'Georgetown', 'HN': 'Tegucigalpa', 'HR': 'Zagreb', 'HT': 'Puerto Príncipe', 'HU': 'Budapest', 'ID': 'Yakarta', 'IE': 'Dublín', 'IL': 'Jerusalén', 'IM': 'Douglas', 'IN': 'Nueva Delhi', 'IQ': 'Bagdad', 'IR': 'Teherán', 'IS': 'Reikiavik', 'IT': 'Roma', 'JE': 'Saint Helier', 'JM': 'Kingston', 'JO': 'Amán', 'JP': 'Tokio', 'KE': 'Nairobi', 'KG': 'Biskek', 'KH': 'Nom Pen', 'KI': 'Tarawa', 'KM': 'Moroni', 'KN': 'Basseterre', 'KP': 'Pionyang', 'KR': 'Seúl', 'KW': 'Kuwait', 'KY': 'George Town', 'KZ': 'Astaná', 'LA': 'Vientián', 'LB': 'Beirut', 'LC': 'Castries', 'LI': 'Vaduz', 'LK': 'Colombo', 'LR': 'Monrovia', 'LS': 'Maseru', 'LT': 'Vilna', 'LU': 'Luxemburgo', 'LV': 'Riga', 'LY': 'Trípoli', 'MA': 'Rabat', 'MC': 'Mónaco', 'MD': 'Chisináu', 'ME': 'Podgorica', 'MF': 'Marigot', 'MG': 'Antananarivo', 'MH': 'Majuro', 'MK': 'Skopie', 'ML': 'Bamako', 'MM': 'Naipyidó', 'MN': 'Ulán Bator', 'MP': 'Saipán', 'MQ': 'Fort-de-France', 'MR': 'Nuakchot', 'MS': 'Plymouth', 'MT': 'La Valeta', 'MU': 'Port Louis', 'MV': 'Malé', 'MW': 'Lilongüe', 'MX': 'Ciudad de México', 'MY': 'Kuala Lumpur', 'MZ': 'Maputo', 'NA': 'Windhoek', 'NC': 'Numea', 'NE': 'Niamey', 'NF': 'Kingston', 'NG': 'Abuya', 'NI': 'Managua', 'NL': 'Ámsterdam', 'NO': 'Oslo', 'NP': 'Katmandú', 'NR': 'Yaren', 'NU': 'Alofi', 'NZ': 'Wellington', 'OM': 'Mascate', 'PA': 'Ciudad de Panamá', 'PE': 'Lima', 'PF': 'Papeete', 'PG': 'Port Moresby', 'PH': 'Manila', 'PK': 'Islamabad', 'PL': 'Varsovia', 'PM': 'Saint-Pierre', 'PR': 'San Juan', 'PS': 'Jerusalén Este', 'PT': 'Lisboa', 'PW': 'Melekeok', 'PY': 'Asunción', 'QA': 'Doha', 'RO': 'Bucarest', 'RS': 'Belgrado', 'RU': 'Moscú', 'RW': 'Kigali', 'SA': 'Riad', 'SB': 'Honiara', 'SC': 'Victoria', 'SD': 'Jartum', 'SS': 'Yuba', 'SE': 'Estocolmo', 'SG': 'Singapur', 'SI': 'Liubliana', 'SJ': 'Longyearbyen', 'SK': 'Bratislava', 'SL': 'Freetown', 'SM': 'San Marino', 'SN': 'Dakar', 'SO': 'Mogadiscio', 'SR': 'Paramaribo', 'ST': 'Santo Tomé', 'SV': 'San Salvador', 'SX': 'Philipsburg', 'SY': 'Damasco', 'SZ': 'Mbabane', 'TC': 'Cockburn Town', 'TD': 'Yamena', 'TG': 'Lomé', 'TH': 'Bangkok', 'TJ': 'Dusambé', 'TK': 'Atafu', 'TL': 'Dili', 'TM': 'Asjabad', 'TN': 'Túnez', 'TO': 'Nukualofa', 'TR': 'Ankara', 'TT': 'Puerto España', 'TV': 'Funafuti', 'TW': 'Taipéi', 'TER': 'Terrícola', 'TZ': 'Dodoma', 'UA': 'Kyiv', 'UG': 'Kampala', 'US': 'Washington D. C.', 'UY': 'Montevideo', 'UZ': 'Taskent', 'VA': 'Ciudad del Vaticano', 'VC': 'Kingstown', 'VE': 'Caracas', 'VG': 'Road Town', 'VI': 'Charlotte Amalie', 'VN': 'Hanói', 'VU': 'Port Vila', 'WF': 'Mata Utu', 'WS': 'Apia', 'YE': 'Saná', 'ZA': 'Pretoria', 'ZM': 'Lusaka', 'ZW': 'Harare'}
# Define `CIUDADES_JAPON` para mantener el catálogo de ciudades japonesas elegibles.
CIUDADES_JAPON = "\nAbashiri\nAbiko, Chiba\nAgano, Niigata\nAgeo\nAioi, Hyōgo\nAira, Kagoshima\nAisai\nAizuwakamatsu\nAkabira\nAkaiwa\nAkashi, Hyōgo\nAki, Kōchi\nAkiruno, Tokyo\nAkishima, Tokyo\nAkita (city)\nAkitakata\nAkune, Kagoshima\nAkō, Hyōgo\nAma, Aichi\nAmagasaki\nAmakusa, Kumamoto\nAmami, Kagoshima\nAnan, Tokushima\nAnjō\nAnnaka, Gunma\nAomori\nArao, Kumamoto\nArida, Wakayama\nAsago, Hyōgo\nAsahi, Chiba\nAsahikawa\nAsaka, Saitama\nAsakuchi\nAsakura, Fukuoka\nAshibetsu\nAshikaga, Tochigi\nAshiya, Hyōgo\nAso, Kumamoto\nAtami\nAtsugi\nAwa, Tokushima\nAwaji, Hyōgo\nAwara, Fukui\nAyabe, Kyoto\nAyase, Kanagawa\nAzumino\nBandō, Ibaraki\nBeppu\nBibai\nBizen, Okayama\nBungo-Ōno\nBungotakada, Ōita\nBuzen, Fukuoka\nChiba (city)\nChichibu, Saitama\nChigasaki, Kanagawa\nChikugo, Fukuoka\nChikuma, Nagano\nChikusei\nChikushino, Fukuoka\nChino, Nagano\nChiryū\nChita, Aichi\nChitose, Hokkaido\nChōfu\nChōshi\nChūō, Yamanashi\nDaisen, Akita\nDaitō, Osaka\nDate, Fukushima\nDate, Hokkaido\nDazaifu, Fukuoka\nEbetsu\nEbina, Kanagawa\nEbino, Miyazaki\nEchizen, Fukui\nEna, Gifu\nEniwa, Hokkaido\nEtajima, Hiroshima\nFuchū, Hiroshima\nFuchū, Tokyo\nFuefuki\nFuji, Shizuoka\nFujieda, Shizuoka\nFujiidera\nFujimi, Saitama\nFujimino, Saitama\nFujinomiya, Shizuoka\nFujioka, Gunma\nFujisawa, Kanagawa\nFujiyoshida\nFukagawa, Hokkaido\nFukaya, Saitama\nFukuchiyama, Kyoto\nFukui (city)\nFukuoka\nFukuroi, Shizuoka\nFukushima (city)\nFukutsu, Fukuoka\nFukuyama, Hiroshima\nFunabashi\nFurano, Hokkaido\nFussa, Tokyo\nFuttsu\nGamagōri\nGero, Gifu\nGifu\nGinowan, Okinawa\nGobō, Wakayama\nGojō, Nara\nGose, Nara\nGosen, Niigata\nGoshogawara\nGotemba, Shizuoka\nGotō, Nagasaki\nGujō, Gifu\nGyōda\nGōtsu, Shimane\nHabikino\nHachimantai, Iwate\nHachinohe\nHachiōji\nHadano, Kanagawa\nHagi, Yamaguchi\nHakodate\nHakui, Ishikawa\nHakusan, Ishikawa\nHamada, Shimane\nHamamatsu\nHamura, Tokyo\nHanamaki, Iwate\nHanda, Aichi\nHannan, Osaka\nHannō\nHanyū, Saitama\nHashima, Gifu\nHashimoto, Wakayama\nHasuda, Saitama\nHatsukaichi\nHekinan\nHida, Gifu\nHidaka, Saitama\nHigashihiroshima\nHigashikagawa, Kagawa\nHigashikurume, Tokyo\nHigashimatsushima\nHigashimatsuyama, Saitama\nHigashimurayama, Tokyo\nHigashine\nHigashiyamato, Tokyo\nHigashiōmi\nHigashiōsaka\nHikari, Yamaguchi\nHikone, Shiga\nHimeji\nHimi, Toyama\nHino, Tokyo\nHioki, Kagoshima\nHirado, Nagasaki\nHirakata\nHirakawa, Aomori\nHiratsuka\nHirosaki\nHiroshima\nHita, Ōita\nHitachi, Ibaraki\nHitachinaka, Ibaraki\nHitachiōmiya\nHitachiōta, Ibaraki\nHitoyoshi, Kumamoto\nHokota, Ibaraki\nHokuto, Hokkaido\nHokuto, Yamanashi\nHonjō, Saitama\nHyūga, Miyazaki\nHōfu\nIbara\nIbaraki, Osaka\nIbusuki\nIchihara, Chiba\nIchikawa, Chiba\nIchikikushikino\nIchinomiya, Aichi\nIchinoseki, Iwate\nIga, Mie\nIida, Nagano\nIiyama, Nagano\nIizuka, Fukuoka\nIkeda, Osaka\nIki, Nagasaki\nIkoma, Nara\nImabari, Ehime\nImari, Saga\nImizu\nIna, Nagano\nInabe\nInagi\nInashiki\nInazawa\nInuyama, Aichi\nInzai\nIruma, Saitama\nIsa, Kagoshima\nIsahaya, Nagasaki\nIse, Mie\nIsehara, Kanagawa\nIsesaki\nIshigaki, Okinawa\nIshikari, Hokkaido\nIshinomaki\nIshioka, Ibaraki\nIsumi\nItako, Ibaraki\nItami\nItoigawa\nItoman, Okinawa\nItoshima, Fukuoka\nItō, Shizuoka\nIwade, Wakayama\nIwaki, Fukushima\nIwakuni\nIwakura, Aichi\nIwamizawa\nIwanuma\nIwata, Shizuoka\nIyo, Ehime\nIzu, Shizuoka\nIzumi, Kagoshima\nIzumi, Osaka\nIzumisano\nIzumiōtsu\nIzumo, Shimane\nIzunokuni\nJōetsu, Niigata\nJōsō\nJōyō, Kyoto\nKadoma, Osaka\nKaga, Ishikawa\nKagoshima\nKahoku, Ishikawa\nKai, Yamanashi\nKainan, Wakayama\nKaizu\nKaizuka, Osaka\nKakamigahara\nKakegawa, Shizuoka\nKakogawa, Hyōgo\nKakuda, Miyagi\nKama, Fukuoka\nKamagaya\nKamaishi, Iwate\nKamakura\nKameoka, Kyoto\nKameyama, Mie\nKami, Kōchi\nKami-Amakusa\nKaminoyama\nKamisu\nKamo, Niigata\nKamogawa, Chiba\nKan'onji, Kagawa\nKanazawa\nKani, Gifu\nKanoya, Kagoshima\nKanuma, Tochigi\nKanzaki, Saga\nKaratsu, Saga\nKariya, Aichi\nKasai, Hyōgo\nKasama, Ibaraki\nKasaoka\nKashiba, Nara\nKashihara, Nara\nKashima, Ibaraki\nKashima, Saga\nKashiwa\nKashiwara\nKashiwazaki, Niigata\nKasuga, Fukuoka\nKasugai, Aichi\nKasukabe, Saitama\nKasumigaura, Ibaraki\nKatagami, Akita\nKatano\nKatori, Chiba\nKatsuragi, Nara\nKatsuura, Chiba\nKatsuyama, Fukui\nKatō, Hyōgo\nKawachinagano\nKawagoe, Saitama\nKawaguchi, Saitama\nKawanishi, Hyōgo\nKawasaki, Kanagawa\nKazo, Saitama\nKazuno, Akita\nKesennuma\nKikuchi, Kumamoto\nKikugawa\nKimitsu\nKinokawa, Wakayama\nKirishima, Kagoshima\nKiryū, Gunma\nKisarazu\nKishiwada, Osaka\nKitaakita\nKitahiroshima, Hokkaido\nKitaibaraki, Ibaraki\nKitakami, Iwate\nKitakata, Fukushima\nKitakyushu\nKitami\nKitamoto, Saitama\nKitanagoya\nKitsuki, Ōita\nKiyose, Tokyo\nKiyosu\nKizugawa, Kyoto\nKobayashi, Miyazaki\nKobe\nKodaira, Tokyo\nKoga, Fukuoka\nKoga, Ibaraki\nKoganei, Tokyo\nKokubunji, Tokyo\nKomae, Tokyo\nKomagane, Nagano\nKomaki\nKomatsu, Ishikawa\nKomatsushima, Tokushima\nKomoro, Nagano\nKonan, Shiga\nKosai, Shizuoka\nKoshigaya\nKudamatsu\nKuji, Iwate\nKuki, Saitama\nKumagaya\nKumamoto\nKumano, Mie\nKunisaki\nKunitachi, Tokyo\nKurashiki\nKurayoshi, Tottori\nKure, Hiroshima\nKurihara, Miyagi\nKurobe, Toyama\nKuroishi, Aomori\nKurume\nKusatsu, Shiga\nKushima, Miyazaki\nKushiro\nKuwana, Mie\nKyoto\nKyōtanabe, Kyoto\nKyōtango\nKōchi, Kōchi\nKōfu\nKōka, Shiga\nKōnan, Aichi\nKōnan, Kōchi\nKōnosu\nKōriyama\nKōshi, Kumamoto\nKōshū, Yamanashi\nMachida, Tokyo\nMaebashi\nMaibara, Shiga\nMaizuru\nMakinohara\nMakurazaki, Kagoshima\nManiwa\nMarugame, Kagawa\nMasuda, Shimane\nMatsubara\nMatsudo\nMatsue\nMatsumoto, Nagano\nMatsusaka\nMatsuura, Nagasaki\nMatsuyama\nMidori, Gunma\nMihara, Hiroshima\nMikasa, Hokkaido\nMiki, Hyōgo\nMima, Tokushima\nMimasaka, Okayama\nMinamata, Kumamoto\nMinami-Alps, Yamanashi\nMinamiashigara, Kanagawa\nMinamiawaji\nMinamibōsō\nMinamikyūshū\nMinamisatsuma\nMinamishimabara\nMinamisōma\nMinamiuonuma\nMine, Yamaguchi\nMino, Gifu\nMinoh\nMinokamo, Gifu\nMisato, Saitama (city)\nMisawa, Aomori\nMishima, Shizuoka\nMitaka, Tokyo\nMito, Ibaraki\nMitoyo, Kagawa\nMitsuke\nMiura, Kanagawa\nMiyako, Iwate\nMiyakojima, Okinawa\nMiyakonojō\nMiyama, Fukuoka\nMiyawaka\nMiyazaki (city)\nMiyazu, Kyoto\nMiyoshi, Aichi\nMiyoshi, Hiroshima\nMiyoshi, Tokushima\nMizuho, Gifu\nMizunami, Gifu\nMobara\nMonbetsu, Hokkaido\nMooka, Tochigi\nMoriguchi, Osaka\nMorioka\nMoriya, Ibaraki\nMoriyama, Shiga\nMotomiya, Fukushima\nMotosu, Gifu\nMukō\nMunakata, Fukuoka\nMurakami, Niigata\nMurayama, Yamagata\nMuroran\nMuroto, Kōchi\nMusashimurayama, Tokyo\nMusashino, Tokyo\nMutsu, Aomori\nMyōkō, Niigata\nNabari, Mie\nNagahama, Shiga\nNagai, Yamagata\nNagakute\nNagano (city)\nNagaoka, Niigata\nNagaokakyō, Kyoto\nNagareyama\nNagasaki\nNagato, Yamaguchi\nNago\nNagoya\nNaha\nNaka, Ibaraki\nNakagawa, Fukuoka\nNakama, Fukuoka\nNakano, Nagano\nNakatsu, Ōita\nNakatsugawa\nNamegata\nNamerikawa, Toyama\nNan'yō, Yamagata\nNanao, Ishikawa\nNanjō\nNankoku, Kōchi\nNantan, Kyoto\nNanto, Toyama\nNara (city)\nNarashino\nNarita, Chiba\nNaruto, Tokushima\nNasukarasuyama\nNasushiobara\nNatori, Miyagi\nNayoro\nNemuro, Hokkaido\nNeyagawa, Osaka\nNichinan, Miyazaki\nNihonmatsu, Fukushima\nNiigata (city)\nNiihama\nNiimi\nNiiza, Saitama\nNikaho, Akita\nNikkō\nNinohe, Iwate\nNirasaki, Yamanashi\nNishinomiya\nNishinoomote, Kagoshima\nNishio\nNishitokyo\nNishiwaki, Hyōgo\nNisshin, Aichi\nNobeoka\nNoboribetsu\nNoda, Chiba\nNomi, Ishikawa\nNonoichi, Ishikawa\nNoshiro, Akita\nNumata, Gunma\nNumazu\nNōgata, Fukuoka\nObama, Fukui\nObanazawa\nObihiro\nOdawara\nOga, Akita\nOgi, Saga\nOgōri, Fukuoka\nOjiya, Niigata\nOkaya, Nagano\nOkayama\nOkazaki, Aichi\nOkegawa, Saitama\nOkinawa (city)\nOmaezaki\nOmitama\nOno, Hyōgo\nOnomichi\nOsaka\nOtaru\nOwariasahi\nOwase\nOyabe, Toyama\nOyama, Tochigi\nRikuzentakata, Iwate\nRittō, Shiga\nRumoi, Hokkaido\nRyūgasaki, Ibaraki\nSabae, Fukui\nSado, Niigata\nSaga (city)\nSagae\nSagamihara\nSaijō, Ehime\nSaikai, Nagasaki\nSaiki, Ōita\nSaitama (city)\nSaito, Miyazaki\nSakado, Saitama\nSakai\nSakai, Fukui\nSakaide, Kagawa\nSakaiminato, Tottori\nSakata, Yamagata\nSaku, Nagano\nSakura, Chiba\nSakura, Tochigi\nSakuragawa, Ibaraki\nSakurai, Nara\nSan'yō-Onoda\nSanda, Hyōgo\nSanjō, Niigata\nSanmu\nSano, Tochigi\nSanuki, Kagawa\nSapporo\nSasebo\nSatsumasendai, Kagoshima\nSatte, Saitama\nSayama\nSeiyo, Ehime\nSeki, Gifu\nSemboku, Akita\nSendai\nSennan, Osaka\nSeto, Aichi\nSetouchi, Okayama\nSettsu, Osaka\nShibata, Niigata\nShibetsu, Hokkaido\nShibukawa, Gunma\nShibushi, Kagoshima\nShijōnawate\nShiki, Saitama\nShikokuchūō\nShima, Mie\nShimabara, Nagasaki\nShimada, Shizuoka\nShimanto, Kōchi (city)\nShimoda, Shizuoka\nShimonoseki\nShimotsuke, Tochigi\nShimotsuma, Ibaraki\nShingū, Wakayama\nShinjō, Yamagata\nShinshiro\nShiogama\nShiojiri, Nagano\nShirakawa, Fukushima\nShiraoka, Saitama\nShiroi\nShiroishi, Miyagi\nShisō, Hyōgo\nShizuoka (city)\nShōbara\nShūnan\nSodegaura\nSoo, Kagoshima\nSuita\nSukagawa, Fukushima\nSukumo, Kōchi\nSumoto, Hyōgo\nSunagawa, Hokkaido\nSusaki, Kōchi\nSusono\nSuwa, Nagano\nSuzaka, Nagano\nSuzu, Ishikawa\nSuzuka, Mie\nSōja\nSōka\nSōma, Fukushima\nSōsa\nTachikawa, Tokyo\nTagajō\nTagawa, Fukuoka\nTahara, Aichi\nTainai\nTajimi\nTakahagi, Ibaraki\nTakahama, Aichi\nTakahashi, Okayama\nTakaishi, Osaka\nTakamatsu\nTakaoka, Toyama\nTakarazuka, Hyōgo\nTakasago, Hyōgo\nTakasaki\nTakashima, Shiga\nTakatsuki\nTakayama, Gifu\nTakehara, Hiroshima\nTakeo, Saga\nTaketa, Ōita\nTakikawa, Hokkaido\nTakizawa, Iwate\nTaku, Saga\nTama, Tokyo\nTamana, Kumamoto\nTamano\nTamba, Hyōgo\nTamba-Sasayama\nTamura, Fukushima\nTanabe, Wakayama\nTarumizu, Kagoshima\nTatebayashi, Gunma\nTateyama, Chiba\nTatsuno, Hyōgo\nTendō, Yamagata\nTenri, Nara\nToba, Mie\nTochigi (city)\nToda, Saitama\nToki, Gifu\nTokoname\nTokorozawa, Saitama\nTokushima (city)\nTokyo\nTomakomai\nTome, Miyagi\nTomigusuku, Okinawa\nTomioka, Gunma\nTomisato\nTomiya, Miyagi\nTonami, Toyama\nTondabayashi\nToride, Ibaraki\nTosa, Kōchi\nTosashimizu, Kōchi\nTosu, Saga\nTottori (city)\nTowada\nToyama (city)\nToyoake\nToyohashi\nToyokawa, Aichi\nToyonaka\nToyooka, Hyōgo\nToyota, Aichi\nTsu, Mie\nTsubame, Niigata\nTsuchiura\nTsugaru, Aomori\nTsukuba\nTsukubamirai, Ibaraki\nTsukumi, Ōita\nTsuru, Yamanashi\nTsuruga, Fukui\nTsurugashima, Saitama\nTsuruoka\nTsushima, Aichi\nTsushima, Nagasaki\nTsuyama\nTōgane\nTōkai, Aichi\nTōkamachi\nTōmi, Nagano\nTōno, Iwate\nTōon, Ehime\nUbe, Yamaguchi\nUda, Nara\nUeda, Nagano\nUenohara\nUji\nUki, Kumamoto\nUkiha, Fukuoka\nUnnan\nUnzen, Nagasaki\nUonuma\nUozu, Toyama\nUrasoe, Okinawa\nUrayasu\nUreshino, Saga\nUruma\nUsa, Ōita\nUshiku, Ibaraki\nUsuki, Ōita\nUtashinai\nUto, Kumamoto\nUtsunomiya\nUwajima, Ehime\nWajima, Ishikawa\nWakayama (city)\nWakkanai\nWakō, Saitama\nWarabi, Saitama\nYabu, Hyōgo\nYachimata\nYachiyo, Chiba\nYaita\nYaizu\nYamaga, Kumamoto\nYamagata (city)\nYamagata, Gifu\nYamaguchi (city)\nYamanashi (city)\nYamato, Kanagawa\nYamatokōriyama\nYamatotakada, Nara\nYame\nYanagawa, Fukuoka\nYanai, Yamaguchi\nYao, Osaka\nYashio, Saitama\nYasu, Shiga\nYasugi, Shimane\nYatomi\nYatsushiro\nYawata\nYawatahama\nYokkaichi\nYokohama\nYokosuka\nYokote, Akita\nYonago\nYonezawa, Yamagata\nYoshikawa, Saitama\nYoshinogawa, Tokushima\nYotsukaidō\nYufu\nYukuhashi, Fukuoka\nYurihonjō\nYuzawa, Akita\nYūbari, Hokkaido\nYūki, Ibaraki\nZama, Kanagawa\nZentsūji, Kagawa\nZushi, Kanagawa\nŌamishirasato\nŌbu\nŌda, Shimane\nŌdate\nŌfunato\nŌgaki\nŌita (city)\nŌkawa, Fukuoka\nŌmachi, Nagano\nŌme, Tokyo\nŌmihachiman\nŌmura, Nagasaki\nŌmuta, Fukuoka\nŌno, Fukui\nŌnojō\nŌsakasayama\nŌsaki, Miyagi\nŌshū, Iwate\nŌta, Gunma\nŌtake, Hiroshima\nŌtawara\nŌtsu\nŌtsuki, Yamanashi\nŌzu, Ehime\n".strip().splitlines()
# Calcula y guarda en `LOCALIDADES_POR_PAIS['JP']` el valor que se necesita en las instrucciones siguientes.
LOCALIDADES_POR_PAIS['JP'] = CIUDADES_JAPON
# Crea `LOCALIDADES_ADICIONALES_POR_PAIS` con los datos u opciones que se procesan después.
LOCALIDADES_ADICIONALES_POR_PAIS = {'AD': ['les Escaldes', 'Encamp', 'Sant Julià de Lòria', 'la Massana', 'Canillo', 'Ordino'], 'AE': ['Dubai', 'Abu Dhabi', 'Sharjah', 'Al Ain City', 'Ajman', 'Dayrah', 'Ras Al Khaimah', 'Musaffah', 'Jebel Ali', 'Business Bay', 'Dubai Investments Park', 'Dubai Marina'], 'AF': ['Kabul', 'Herāt', 'Kandahār', 'Mazār-e Sharīf', 'Jalālābād', 'Kunduz', 'Ghazni', 'Balkh', 'Bagrām', 'Baghlān', 'Gardez', 'Khōst'], 'AG': ['Saint John’s', 'St. Paul Parish', 'St. George Parish', 'St. Mary Parish', 'St. Peter Parish', 'Piggotts', 'Bolands', 'Codrington', 'Parham', 'Freetown', 'Falmouth'], 'AI': ['The Valley', 'Blowing Point Village', 'East End Village', 'Sandy Hill', 'Sandy Ground Village', 'Farrington', 'George Hill', 'Island Harbour', 'North Hill Village', 'North Side', 'South Hill Village', 'Stoney Ground'], 'AL': ['Tirana', 'Durrës', 'Vlorë', 'Elbasan', 'Shkodër', 'Lushnjë', 'Berat', 'Fier-Çifçi', 'Korçë', 'Fier', 'Krujë', 'Pogradec'], 'AM': ['Yerevan', 'Malatia-Sebastia', 'Shengavit', 'Nor Nork', 'Kentron', 'Erebuni', 'Ajapnyak', 'Arabkir', 'Gyumri', 'Vanadzor', 'Kanaker-Zeytun', 'Avan'], 'AN': ['Willemstad', 'Philipsburg', 'Kralendijk'], 'AO': ['Luanda', 'Mulenvos', 'Viana', 'Kikolo', 'Maianga', 'Camama', 'Golfe', 'Calumbo', 'Hoji ya Henda', 'Lubango', 'Huambo', 'Benguela'], 'AR': ['Mar del Plata', 'San Miguel de Tucumán', 'Salta', 'Santa Fe', 'Avellaneda', 'Corrientes', 'Posadas', 'Bahía Blanca', 'Resistencia', 'Merlo', 'Quilmes', 'San Salvador de Jujuy'], 'AS': ['Pago Pago', 'Tāfuna', 'Ta`ū', 'Taulaga'], 'AT': ['Vienna', 'Linz', 'Favoriten', 'Donaustadt', 'Floridsdorf', 'Salzburg', 'Innsbruck', 'Ottakring', 'Simmering', 'Klagenfurt am Wörthersee', 'Landstraße', 'Penzing'], 'AU': ['Sydney', 'Brisbane', 'Perth', 'Adelaide', 'Gold Coast', 'Newcastle', 'Sunshine Coast', 'Central Coast', 'Logan City', 'Geelong', 'Wollongong', 'Hobart'], 'AW': ['Oranjestad', 'Noord', 'Tanki Leendert', 'Santa Cruz', 'Butucu', 'San Nicolas', 'Paradera', 'Savaneta', 'Malmok', 'Palm Beach', 'Pos Chiquito', 'Alto Vista'], 'AX': ['Mariehamn', 'Ytterby', 'Yomala'], 'AZ': ['Baku', 'Sumgayit', 'Ganja', 'Khirdalan', 'Yevlakh', 'Mingachevir', 'Naxçıvan', 'Lankaran', 'Qaraçuxur', 'Lerik', 'Şirvan', 'Sheki'], 'BA': ['Sarajevo', 'Banja Luka', 'Zenica', 'Tuzla', 'Mostar', 'Bihać', 'Ilidža', 'Lukavac', 'Bugojno', 'Brčko', 'Bijeljina', 'Prijedor'], 'BB': ['Bridgetown', 'White Hill', 'Speightstown', 'Oistins', 'Bathsheba', 'Holetown', 'Crane', 'Greenland', 'Checker Hall', 'Four Cross Roads', 'Welchman Hall'], 'BD': ['Dhaka', 'Chattogram', 'Gazipur', 'Khulna', 'Rangpur', 'Rajshahi', 'Comilla', 'Pallabi', 'Mirpur Model Thana', 'Mohammadpur', 'Hāthazāri', 'Shibganj'], 'BE': ['Brussels', 'Antwerp', 'Gent', 'Charleroi', 'Liège', 'Anderlecht', 'Schaerbeek', 'Brugge', 'Namur', 'Leuven', 'Molenbeek-Saint-Jean', 'Mons'], 'BF': ['Ouagadougou', 'Bobo-Dioulasso', 'Koudougou', 'Saaba', 'Ouahigouya', 'Kaya', 'Banfora', 'Pouytenga', 'Houndé', "Fada N'gourma", 'Nioko I', 'Dédougou'], 'BG': ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Stara Zagora', 'Ruse', 'Pleven', 'Sliven', 'Pernik', 'Shumen', 'Dobrich', 'Blagoevgrad'], 'BH': ['Al Muharraq', 'Manama', 'Madīnat Ḩamad', 'Ar Rifā‘', 'Sitrah', 'Jidd Ḩafş', 'Dār Kulayb', 'Madīnat ‘Īsá', 'Al Ḩadd', 'Az Zallāq', 'Sanābis', 'Sār'], 'BI': ['Bujumbura', 'Gitega', 'Ngozi', 'Mpanda', 'Rumonge', 'Cibitoke', 'Kayanza', 'Cendajuru', 'Bubanza', 'Vyanda', 'Zanandore', 'Gatumba'], 'BJ': ['Cotonou', 'Abomey-Calavi', 'Porto-Novo', 'Parakou', 'Godomè', 'Abomey', 'Djougou', 'Bohicon', 'Ekpé', 'Nikki', 'Malanville', 'Kandi'], 'BL': ['Gustavia', 'Saint-Jean', 'Lorient', 'Colombier'], 'BM': ['Pembroke Parish', 'Warwick Parish', 'Sandys Parish', 'Devonshire Parish', 'Southampton Parish', 'Hamilton Parish', 'Paget Parish', "St George's Parish", "Smith's Parish", 'Hamilton'], 'BN': ['Bandar Seri Begawan', 'Sengkurong', 'Mentiri', 'Kuala Belait', 'Tutong', 'Serasa', 'Liang', 'Perumahan Negara Panchor', 'Telamba', 'Telisai', 'Kota Batu', 'Kampung Tanah Jambu'], 'BO': ['Cochabamba', 'Oruro', 'Sacaba', 'Quillacollo', 'Tarija', 'Potosí', 'Riberalta', 'Montero', 'Viacha', 'Trinidad', 'Yacuiba', 'Tiquipaya'], 'BQ': ['Kralendijk', 'Oranjestad', 'The Bottom'], 'BR': ['Belo Horizonte', 'Salvador', 'Fortaleza', 'Manaus', 'Curitiba', 'Recife', 'Goiânia', 'Belém', 'Porto Alegre', 'Guarulhos', 'Maceió', 'Campinas'], 'BS': ['Nassau', 'Lucaya', 'Freeport', 'Killarney', 'West End', 'Cooper’s Town', 'San Andros', 'George Town', 'Marsh Harbour', 'High Rock', 'Clarence Town', 'Spanish Wells'], 'BW': ['Gaborone', 'Francistown', 'Mogoditshane', 'Maun', 'Molepolole', 'Serowe', 'Tlokweng', 'Palapye', 'Mochudi', 'Mahalapye', 'Kanye', 'Selebi-Phikwe'], 'BY': ['Minsk', "Homyel'", 'Hrodna', 'Vitebsk', 'Mahilyow', 'Brest', 'Bobruysk', 'Baranovichi', 'Barysaw', 'Pinsk', 'Mazyr', 'Lida'], 'BZ': ['Belize City', 'San Ignacio', 'San Pedro', 'Orange Walk', 'Belmopan', 'Dangriga', 'Corozal', 'Santa Elena', 'Ladyville', 'Benque Viejo el Carmen', 'Bella Vista', 'Trial Farm'], 'CA': ['Montréal', 'Calgary', 'Edmonton', 'Winnipeg', 'Mississauga', 'Brampton', 'Hamilton', 'Surrey', 'Québec', 'Halifax', 'Laval', 'London'], 'CD': ['Kinshasa', 'Lubumbashi', 'Mbuji-Mayi', 'Kisangani', 'Kananga', 'Bukavu', 'Kolwezi', 'Likasi', 'Tshikapa', 'Kikwit', 'Masina', 'Mbandaka'], 'CF': ['Bangui', 'Bimbo', 'Bégoua', 'Carnot', 'Berbérati', 'Bambari', 'Bouar', 'Bossangoa', 'Kaga-Bandoro', 'Bangassou', 'Paoua', 'Bria'], 'CG': ['Brazzaville', 'Pointe-Noire', 'Dolisie', 'Nkayi', 'Kayes', 'Impfondo', 'Ouesso', 'Owando', 'Sibiti', 'Loutété', 'Bouansa', 'Gamboma'], 'CH': ['Zürich', 'Geneva', 'Basel', 'Lausanne', 'Bern', 'Winterthur', 'Luzern', 'Sankt Gallen', 'Lugano', 'Biel/Bienne', 'Zürich (Kreis 11)', 'Zürich (Kreis 3)'], 'CI': ['Abidjan', 'Abobo', 'Bouaké', 'Korhogo', 'Daloa', 'Koumassi', 'San-Pédro', 'Gagnoa', 'Yamoussoukro', 'Sinfra', 'Man', 'Marcory'], 'CK': ['Avarua', 'Arutanga', 'Amuri', 'Muri'], 'CL': ['Puente Alto', 'Maipú', 'Antofagasta', 'Viña del Mar', 'Ñuñoa', 'San Bernardo', 'Puerto Montt', 'Arica', 'Peñalolén', 'Temuco', 'Rancagua', 'Quilicura'], 'CM': ['Douala', 'Yaoundé', 'Bamenda', 'Bafoussam', 'Maroua', 'Ngaoundéré', 'Kumba', 'Nkongsamba', 'Buea', 'Kousséri', 'Bertoua', 'Limbe'], 'CN': ['Chongqing', 'Chengdu', 'Beijing', 'Guangzhou', 'Shenzhen', 'Tianjin', 'Wuhan', 'Xi’an', 'Hangzhou', 'Harbin', 'Dongguan', 'Hefei'], 'CO': ['Barranquilla', 'Kennedy', 'Cartagena', 'Cúcuta', 'Soacha', 'Bucaramanga', 'Ibagué', 'Santa Marta', 'Montería', 'Valledupar', 'Pereira', 'Manizales'], 'CR': ['San José', 'Limón', 'San Francisco', 'Alajuela', 'Liberia', 'Paraíso', 'Puntarenas', 'San Isidro', 'Curridabat', 'San Vicente', 'San Vicente de Moravia', 'Purral'], 'CU': ['Havana', 'Camagüey', 'Holguín', 'Guantánamo', 'Santa Clara', 'Almendares', 'Diez de Octubre', 'Arroyo Naranjo', 'Mantilla', 'Las Tunas', 'Bayamo', 'Boyeros'], 'CV': ['Praia', 'Mindelo', 'Espargos', 'Assomada', 'Tarrafal', 'Palmarejo', 'Porto Novo', 'Sal Rei', 'Achada Santo Antonio', 'São Filipe', 'Pedra Badejo', 'Santa Cruz'], 'CW': ['Willemstad', 'Bandariba', 'Bandabou', 'St. Michiel', 'Santa Rosa', 'Sint Michiel Liber'], 'CY': ['Nicosia', 'Limassol', 'Larnaca', 'Stróvolos', 'Famagusta', 'Káto Lakatámeia', 'Paphos', 'Kyrenia', 'Mórfou', 'Káto Polemídia', 'Aradíppou', 'Aglantziá'], 'CZ': ['Prague', 'Pilsen', 'Liberec', 'Olomouc', 'České Budějovice', 'Hradec Králové', 'Ústí nad Labem', 'Pardubice', 'Brno střed', 'Havířov', 'Zlín', 'Kladno'], 'DE': ['Hamburg', 'Köln', 'Frankfurt am Main', 'Düsseldorf', 'Stuttgart', 'Essen', 'Dortmund', 'Dresden', 'Bremen', 'Nuremberg', 'Hannover', 'Leipzig'], 'DJ': ['Djibouti', 'Balbala', 'Ali Sabih', 'Dikhil', 'Tadjoura', 'Arta', 'Obock', '‘As ‘Êla', 'Damêrdjôg'], 'DK': ['Copenhagen', 'Århus', 'Odense', 'Aalborg', 'Frederiksberg', 'Esbjerg', 'Randers', 'Kolding', 'Horsens', 'Vejle', 'Hvidovre', 'Avedøre'], 'DM': ['Roseau', 'Portsmouth', 'Marigot', 'Berekua', 'Saint Joseph', 'Wesley', 'Soufrière', 'Pointe Michel', 'Colihaut', 'Rosalie', 'Pont Cassé'], 'DO': ['Santo Domingo', 'Santiago de los Caballeros', 'Santo Domingo Oeste', 'Santo Domingo Este', 'San Pedro de Macorís', 'La Romana', 'Bella Vista', 'San Cristóbal', 'Puerto Plata', 'San Francisco de Macorís', 'Salvaleón de Higüey', 'La Vega'], 'DZ': ['Algiers', 'Oran', 'Constantine', 'Annaba', 'Blida', 'Batna', 'Bab Ezzouar', 'Djelfa', 'Sétif', 'Sidi Bel Abbes', 'Biskra', 'Tébessa'], 'EC': ['Quito', 'Guayaquil', 'Cuenca', 'Santo Domingo de los Colorados', 'Ambato', 'Portoviejo', 'Eloy Alfaro', 'Machala', 'Loja', 'Manta', 'Riobamba', 'Ibarra'], 'EE': ['Tallinn', 'Lasnamäe', 'Tartu', 'Mustamäe', 'Kesklinn', 'Põhja-Tallinn', 'Narva', 'Haabersti', 'Pärnu', 'Nõmme', 'Kohtla-Järve', 'Kristiine'], 'EG': ['Cairo', 'Alexandria', 'Giza', 'Shubrā al Khaymah', 'Port Said', 'Suez', 'Madīnat an Naşr', 'Al Mansurah', 'Al Maḩallah al Kubrá', 'Tanta', 'Assiut', 'Al Fayyum'], 'EH': ['Laayoune', 'Dakhla', 'Boujdour', 'El Marsa', 'Meharrize', 'Tichla', 'El Aargub'], 'ER': ['Asmara', 'Keren', 'Himora', 'Af’abet', 'Massawa', 'Assab', 'Mendefera', 'Barentu', 'Adi Keyh', 'Edd', 'Dek’emhāre', 'Ak’ordat'], 'ES': ['Eixample', 'Gasteiz / Vitoria', "L'Hospitalet de Llobregat", 'Latina', 'Carabanchel', 'Puente de Vallecas', 'Fuencarral', 'Sant Martí', 'Ciudad Lineal', 'Fuencarral-El Pardo', 'Terrassa', 'Badalona'], 'ET': ['Addis Ababa', 'Jijiga', 'Gonder', "Mek'ele", 'Nazrēt', 'Warder', 'Awasa', 'Bahir Dar', 'Dire Dawa', 'Dessie', 'Jimma', 'Shashamane'], 'FI': ['Espoo', 'Vantaa', 'Oulu', 'East Helsinki', 'Jyväskylä', 'Kuopio', 'Lahti', 'Pori', 'Joensuu', 'Kouvola', 'Lappeenranta', 'Vaasa'], 'FJ': ['Nasinu', 'Suva', 'Lautoka', 'Nadi', 'Labasa', 'Lami', 'Sigatoka', 'Ba', 'Tavua', 'Levuka', 'Savusavu', 'Vaileka'], 'FK': ['Stanley', 'Goose Green', 'Port Howard', 'Fox Bay'], 'FM': ['Weno', 'Tofol', 'Colonia', 'Palikir', 'Kolonia', 'Kolonia Town'], 'FO': ['Tórshavn', 'Klaksvík', 'Fuglafjørður', 'Miðvágur', 'Tvøroyri', 'Sandur'], 'FR': ['Marseille', 'Toulouse', 'Nice', 'Nantes', 'Marne La Vallée', 'Strasbourg', 'Bordeaux', 'Montpellier', 'Lille', 'Paris 15 Vaugirard', 'Rennes', 'Reims'], 'GA': ['Libreville', 'Port-Gentil', 'Franceville', 'Owendo', 'Oyem', 'Moanda', 'Ntoum', 'Lambaréné', 'Mouila', 'Akanda', 'Tchibanga', 'Bitam'], 'GB': ['London', 'Birmingham', 'Glasgow', 'Sheffield', 'Leeds', 'Edinburgh', 'Liverpool', 'Bristol', 'Cardiff', 'Leicester', 'Bradford', 'Belfast'], 'GD': ["Saint George's", 'Gouyave', 'Grenville', 'Victoria', 'Saint David’s', 'Sauteurs', 'Hillsborough'], 'GE': ['Tbilisi', 'Batumi', 'Kutaisi', 'Rustavi', 'Sokhumi', 'Gori', 'Poti', 'Zugdidi', 'Ts’khinvali', 'Stantsiya Novyy Afon', 'Marneuli', 'Khashuri'], 'GF': ['Cayenne', 'Matoury', 'Saint-Laurent-du-Maroni', 'Kourou', 'Rémire-Montjoly', 'Apatou', 'Grand-Santi', 'Macouria', 'Maripasoula', 'Mana'], 'GG': ['Saint Peter Port', 'Vale Parish', 'Saint Sampson', 'Saint Pierre du Bois Parish', 'Forest Parish', 'Castel', 'Saint Andrew', 'Saint Saviour', 'St Anne', 'St Martin', 'Torteval'], 'GH': ['Kumasi', 'Accra', 'Tamale', 'Takoradi', 'Sekondi', 'Cape Coast', 'Atsiaman', 'Ashaiman', 'Obuase', 'Tema', 'Koforidua', 'Teshi Old Town'], 'GI': ['Gibraltar', 'Reclamation Areas', 'South District'], 'GL': ['Nuuk', 'Sisimiut', 'Ilulissat', 'Qaqortoq', 'Aasiaat'], 'GM': ['Serekunda', 'Brikama', 'Bununka Kunda', 'Sukuta', 'Talinding', 'Faji Kunda', 'Bakau', 'Banjul', 'Nema Kunku', 'Farafenni', 'Bakau New Town', 'Busumbala'], 'GN': ['Conakry', 'Camayenne', 'Nzérékoré', 'Kankan', 'Manéah', 'Dixinn', 'Dubréka', 'Kindia', 'Siguiri', 'Kamsar', 'Kissidougou', 'Labé'], 'GP': ['Les Abymes', 'Baie-Mahault', 'Le Gosier', 'Petit-Bourg', 'Sainte-Anne', 'Le Moule', 'Sainte-Rose', 'Capesterre-Belle-Eau', 'Pointe-à-Pitre', 'Lamentin', 'Saint-François', 'Basse-Terre'], 'GQ': ['Bata', 'Malabo', 'Ebebiyin', 'Añisoc', 'Aconibe', 'Luba', 'Evinayong', 'Rebola', 'Abaamang', 'Mongomo', 'Aual', 'Mikomeseng'], 'GR': ['Athens', 'Thessaloníki', 'Pátra', 'Piraeus', 'Lárisa', 'Peristéri', 'Irákleion', 'Kallithéa', 'Acharnés', 'Kalamariá', 'Níkaia', 'Glyfáda'], 'GT': ['Guatemala City', 'Villa Nueva', 'Mixco', 'Cobán', 'Quetzaltenango', 'Jalapa', 'Escuintla', 'Villa Canales', 'Jutiapa', 'Chichicastenango', 'San Juan Sacatepéquez', 'Petapa'], 'GU': ['Dededo Village', 'Yigo Village', 'Tamuning', 'Tamuning-Tumon-Harmon Village', 'Mangilao Village', 'Barrigada Village', 'Santa Rita Village', 'Mongmong-Toto-Maite Village', 'Chalan Pago-Ordot Village', 'Yona Village', 'Apotgan', 'Agana Heights Village'], 'GW': ['Bissau', 'Bairro Militar', 'Gabú', 'Contumo', 'Reino de Bandim', 'Missira', 'Bafatá', 'Reino de Antula', 'Quelele', 'Plaque', 'Luanda', 'Sintra-Nema'], 'GY': ['Georgetown', 'Linden', 'New Amsterdam', 'Anna Regina', 'Corriverton', 'Bartica', 'Tuschen', 'Rose Hall', 'Mabaruma', 'Skeldon', 'Rosignol', 'Mahdia'], 'HN': ['Tegucigalpa', 'San Pedro Sula', 'Danlí', 'La Ceiba', 'Puerto Cortez', 'Catacamas', 'Choloma', 'Siguatepeque', 'Olanchito', 'Tocoa', 'El Progreso', 'Santa Cruz de Yojoa'], 'HR': ['Zagreb', 'Split', 'Rijeka', 'Osijek', 'Zadar', 'Sesvete', 'Pula', 'Slavonski Brod', 'Karlovac', 'Centar', 'Varaždin', 'Šibenik'], 'HT': ['Port-au-Prince', 'Carrefour', 'Delmas', 'Pétionville', 'Port-de-Paix', 'Saint-Marc', 'Cité Soleil', 'Croix-des-Bouquets', 'Dessalines', 'Jacmel', 'Cap-Haïtien', 'Léogâne'], 'HU': ['Pest', 'Buda', 'Szeged', 'Miskolc', 'Pécs', 'Budapest XI. kerület', 'Zugló', 'Győr', 'Budapest III. kerület', 'Nyíregyháza', 'Budapest XIII. kerület', 'Kecskemét'], 'ID': ['Jakarta', 'Bekasi', 'Medan', 'Depok', 'Tangerang', 'Palembang', 'Semarang', 'Makassar', 'South Tangerang', 'Batam', 'Jepara', 'Pekanbaru'], 'IE': ['South Dublin', 'Limerick', 'Tallaght', 'Waterford', 'Drogheda', 'Dundalk', 'Swords', 'Navan', 'Bray', 'Dún Laoghaire', 'Ennis', 'Carlow'], 'IL': ['Jerusalem', 'West Jerusalem', 'Haifa', 'Rishon LeTsiyyon', 'Petaẖ Tiqva', 'Netanya', 'Ashdod', 'Bnei Brak', 'H̱olon', 'Beersheba', 'Ramat Gan', 'Reẖovot'], 'IM': ['Douglas', 'Ramsey', 'Peel', 'Port Erin', 'Castletown', 'Laxey', 'Andreas', 'Ballabeg', 'Ballasalla', 'Ballaugh', 'Bride', 'Crosby'], 'IN': ['Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur', 'Kanpur', 'Navi Mumbai'], 'IQ': ['Baghdad', 'Al Mawşil al Jadīdah', 'Mosul', 'Erbil', 'Basrah', 'Karbala', 'Sadr City', 'Kirkuk', 'Abū Ghurayb', 'Sulaymaniyah', 'Nasiriyah', 'Najaf'], 'IR': ['Tehran', 'Mashhad', 'Isfahan', 'Karaj', 'Tabriz', 'Shiraz', 'Qom', 'Ahvaz', 'Kermanshah', 'Rasht', 'Kerman', 'Orūmīyeh'], 'IS': ['Reykjavík', 'Kópavogur', 'Hafnarfjörður', 'Reykjanesbær', 'Keflavík', 'Mosfellsbær', 'Garðabær', 'Selfoss', 'Akranes', 'Ísafjörður', 'Sauðárkrókur', 'Egilsstaðir'], 'IT': ['Rome', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Verona', 'Messina', 'Trieste'], 'JE': ['Saint Helier', 'St Lawrence', 'Le Hocq'], 'JM': ['Kingston', 'New Kingston', 'Spanish Town', 'Portmore', 'Montego Bay', 'Mandeville', 'May Pen', 'Ocho Rios', 'Old Harbour', 'Linstead', 'Half Way Tree', 'Barrett Town'], 'JO': ['Amman', 'Zarqa', 'Irbid', 'Russeifa', 'Ḩayy Khildā', 'Khuraybat as Sūq', 'Wādī as Sīr', 'Ar Ramthā', 'Ṣuwayliḥ', '‘Ajlūn', 'As Salţ', 'Aqaba'], 'JP': ['Kawasaki', 'Saitama', 'Chiba', 'Setagaya', 'Niigata', 'Ōta', 'Aihara', 'Edogawe', 'Adachi', 'Shizuoka', 'Honchō', 'Kawaguchi'], 'KE': ['Nairobi', 'Kakamega', 'Mombasa', 'Nakuru', 'Ruiru', 'Eldoret', 'Kisumu', 'Kikuyu', 'Thika', 'Naivasha', 'Karuri', 'Matuga'], 'KG': ['Bishkek', 'Osh', 'Manas', 'Karakol', 'Tokmok', 'Uzgen', 'Kara-Balta', 'Balykchy', 'Naryn', 'Bazar-Korgon', 'Talas', 'Razzakov'], 'KH': ['Phnom Penh', 'Takeo', 'Siem Reap', 'Battambang', 'Paoy Paet', 'Dangkao', 'Kampong Chhnang', 'Sihanoukville', 'Preaek Prasab', 'Kampong Cham', 'Anlong Veaeng', 'Pursat'], 'KI': ['Tarawa', 'Betio Village', 'Bikenibeu Village'], 'KM': ['Moroni', 'Moutsamoudou', 'Fomboni', 'Tsimbeo', 'Domoni', 'Mirontsi', 'Adda-Douéni', 'Ouani', 'Nkourani', 'Sima', 'Koni-Djodjo', 'Moya'], 'KN': ['Basseterre', 'Sandy Point Town', 'Fig Tree', 'Market Shop', 'Saint Paul’s', 'Middle Island', 'Nicola Town', 'Trinity', 'Charlestown', 'Cayon', 'Dieppe Bay Town', 'Monkey Hill'], 'KP': ['Pyongyang', 'Hamhŭng', 'Namp’o', 'Sunch’ŏn', 'Hŭngnam', 'Kaesŏng', 'Wŏnsan', 'Chongjin', 'Man’gyŏngdae-ri', 'Kaech’ŏn', 'Sariwŏn-si', 'Sinŭiju'], 'KR': ['Seoul', 'Daegu', 'Daejeon', 'Gwangju', 'Suwon', 'Ulsan', 'Goyang-si', 'Changwon', 'Seongnam-si', 'Cheongju-si', 'Bucheon-si', 'Cheonan'], 'KW': ['Al Aḩmadī', 'Ḩawallī', 'As Sālimīyah', 'Şabāḩ as Sālim', 'Al Farwānīyah', 'Al Faḩāḩīl', 'Kuwait City', 'Ar Rumaythīyah', 'Ar Riqqah', 'Salwá', 'Al Manqaf', 'Ar Rābiyah'], 'KY': ['George Town', 'West Bay', 'Bodden Town', 'Channel Land', 'Midland Acres', 'Further Ground', 'The Mountain', 'North Sound Estates', 'Breakers', 'Frank Sound', 'Whitehall Estates', 'North Ward'], 'KZ': ['Almaty', 'Astana', 'Shymkent', 'Aktobe', 'Karagandy', 'Taraz', 'Kyzylorda', 'Oral', 'Pavlodar', 'Ust-Kamenogorsk', 'Semey', 'Atyrau'], 'LA': ['Vientiane', 'Savannakhet', 'Thakhèk', 'Pakse', 'Ban Khoan', 'Xam Nua', 'Luang Prabang', 'Muang Phônsavan', 'Ban Xénô', 'Muang Xay', 'Vang Vieng', 'Muang Sing'], 'LB': ['Beirut', 'Ra’s Bayrūt', 'Tripoli', 'Sidon', 'Tyre', 'Aley', 'Nabatîyé et Tahta', 'Habboûch', 'Jounieh', 'Zahlé', 'Aarsâl', 'Ghazieh'], 'LC': ['Gros Islet', 'Castries', 'Bisee', 'Dennery', 'Laborie', 'Choiseul', 'Vieux Fort', 'Micoud', 'Soufrière', 'Anse La Raye'], 'LI': ['Schaan', 'Triesen', 'Vaduz', 'Balzers', 'Eschen', 'Mauren', 'Triesenberg', 'Ruggell', 'Gamprin', 'Schellenberg', 'Planken'], 'LK': ['Colombo', 'Dehiwala-Mount Lavinia', 'Maharagama', 'Jaffna', 'Moratuwa', 'Negombo', 'Pita Kotte', 'Sri Jayewardenepura Kotte', 'Kandy', 'Trincomalee', 'Kalmunai', 'Galle'], 'LR': ['Monrovia', 'Gbarnga', 'Buchanan', 'Ganta', 'Kakata', 'Zwedru', 'Harbel', 'Harper', 'Pleebo City', 'Foya Kamara', 'New Yekepa', 'Voinjama'], 'LS': ['Maseru', 'Maputsoe', "Mohale's Hoek", 'Mafeteng', 'Hlotse', 'Butha-Buthe', 'Mabote', 'Quthing', 'Teyateyaneng', 'Qacha’s Nek', 'Thaba-Tseka', 'Mokhotlong'], 'LT': ['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys', 'Dainava (Kaunas)', 'Alytus', 'Šilainiai', 'Eiguliai', 'Antakalnis', 'Fabijoniškės', 'Naujoji Vilnia'], 'LU': ['Luxembourg', 'Esch-sur-Alzette', 'Dudelange', 'Bonnevoie-Sud', 'Belair', 'Limpertsberg', 'Gare', 'Kirchberg', 'Gasperich', 'Belvaux', 'Schifflange', 'Walferdange'], 'LV': ['Riga', 'Daugavpils', 'Liepāja', 'Jelgava', 'Jūrmala', 'Ventspils', 'Rēzekne', 'Valmiera', 'Ogre', 'Jēkabpils', 'Mārupe', 'Salaspils'], 'LY': ['Tripoli', 'Benghazi', 'Misratah', 'Zliten', 'Al Khums', 'Az Zāwīyah', 'Zawiya', 'Janzūr', 'Sabha', 'Tobruk', 'Ajdabiya', 'Al Ajaylat'], 'MA': ['Fes', 'Tangier', 'Marrakesh', 'Salé', 'Agadir', 'Meknes', 'Oujda', 'Kenitra', 'Tétouan', 'Al Hoceïma', 'Temara', 'Safi'], 'MC': ['Monaco', 'Monte-Carlo', 'La Condamine', 'La Rousse', 'Jardin Exotique'], 'MD': ['Chisinau', 'Tiraspol', 'Bălţi', 'Bender', 'Rîbniţa', 'Cahul', 'Ungheni', 'Soroca', 'Durleşti', 'Orhei', 'Dubăsari', 'Comrat'], 'ME': ['Podgorica', 'Nikšić', 'Herceg Novi', 'Pljevlja', 'Budva', 'Bar', 'Bijelo Polje', 'Cetinje', 'Berane', 'Ulcinj', 'Rožaje', 'Tivat'], 'MF': ['Grand-Case', 'Concordia', 'Marigot'], 'MG': ['Antananarivo', 'Toamasina', 'Antsirabe', 'Mahajanga', 'Fianarantsoa', 'Toliara', 'Antsiranana', 'Sambava', 'Imerintsiatosika', 'Antalaha', 'Tôlanaro', 'Antanifotsy'], 'MH': ['Majuro', 'Dalap-Uliga-Dorrit', 'Ebaye', 'Arno', 'Jabor', 'Wotje', 'Mili', 'Namdrik', 'Ebon', 'Kili', 'Likiep', 'Ailuk'], 'MK': ['Skopje', 'Kumanovo', 'Prilep', 'Bitola', 'Čair', 'Tetovo', 'Kisela Voda', 'Veles', 'Gostivar', 'Shtip', 'Centar Župa', 'Ohrid'], 'ML': ['Bamako', 'Sikasso', 'Koutiala', 'Ségou', 'Kayes', 'Mopti', 'Kalaban-Koro', 'Gao', 'Kati', 'San', 'Bougouni', 'Timbuktu'], 'MM': ['Yangon', 'Mandalay', 'Nay Pyi Taw', 'Hlaingthaya', 'Mawlamyine', 'Kalemyo', 'Insein', 'Bago', 'Amarapura', 'Pathein', 'Yawnghwe', 'Monywa'], 'MN': ['Ulan Bator', 'Erdenet', 'Darhan', 'Choibalsan', 'Nalayh', 'Mörön', 'Bayanhongor', 'Ulaangom', 'Khovd', 'Arvayheer', 'Ölgii', 'Bogd'], 'MP': ['Saipan', 'San Jose Village'], 'MQ': ['Fort-de-France', 'Le Lamentin', 'Le Robert', 'Sainte-Marie', 'Le François', 'Ducos', 'Saint-Joseph', 'La Trinité', 'Rivière-Pilote', 'Le Gros-Morne', 'Sainte-Luce', 'Saint-Esprit'], 'MR': ['Nouakchott', 'Nouadhibou', 'Kiffa', 'Dar Naim', 'Néma', 'Mbera', 'Ksar', 'Kaédi', 'Zouérat', 'Tevragh Zeina', 'Bougadoum', 'Sélibaby'], 'MS': ['Brades', 'Plymouth', 'Saint Peters'], 'MT': ['San Pawl il-Baħar', 'Birkirkara', 'Mosta', 'Sliema', 'Qormi', 'Żabbar', 'Naxxar', 'San Ġwann', 'Swieqi', 'San Ġiljan', 'Imsida', 'Birżebbuġa'], 'MU': ['Port Louis', 'Vacoas', 'Beau Bassin-Rose Hill', 'Curepipe', 'Quatre Bornes', 'Triolet', 'Goodlands', 'Bel Air Rivière Sèche', 'Bambous', 'Centre de Flacq', 'Mahébourg', 'Saint Pierre'], 'MV': ['Male', 'Fuvahmulah', 'Hithadhoo', 'Kulhudhuffushi', 'Thinadhoo', 'Naifaru', 'Dhihdhoo', 'Viligili', 'Funadhoo', 'Eydhafushi', 'Mahibadhoo', 'Fonadhoo'], 'MW': ['Lilongwe', 'Blantyre', 'Mzuzu', 'Zomba', 'Karonga', 'Kasungu', 'Mangochi', 'Salima', 'Liwonde', 'Balaka', 'Dedza', 'Nkhotakota'], 'MX': ['Mexico City', 'Tijuana', 'Iztapalapa', 'Puebla', 'Ecatepec de Morelos', 'Santiago de Querétaro', 'León de los Aldama', 'Ciudad Juárez', 'Zapopan', 'Mérida', 'Gustavo Adolfo Madero', 'Ciudad Nezahualcoyotl'], 'MY': ['Kuala Lumpur', 'Johor Bahru', 'Kampung Baru Subang', 'Petaling Jaya', 'Ipoh', 'Shah Alam', 'Subang Jaya', 'Bukit Rahman Putra', 'Pelentong', 'Malacca', 'Iskandar Puteri', 'Kota Bharu'], 'MZ': ['Maputo', 'Matola', 'Nampula', 'Beira', 'Chimoio', 'Tete', 'Quelimane', 'Lichinga', 'Nacala', 'Pemba', 'Mocuba', 'Gurúè'], 'NA': ['Windhoek', 'Rundu', 'Walvis Bay', 'Swakopmund', 'Oshakati', 'Rehoboth', 'Katima Mulilo', 'Otjiwarongo', 'Ondangwa', 'Okahandja', 'Grootfontein', 'Ongwediva'], 'NC': ['Nouméa', 'Mont-Dore', 'Dumbéa', 'Païta', 'Wé', 'Vallée des Colons', 'Tadine', 'Magenta', 'Rivière-Salée', 'Bourail', 'Poindimié', 'Koné'], 'NE': ['Niamey', 'Maradi', 'Zinder', 'Tahoua', 'Agadez', 'Arlit', 'Alaghsas', 'Birni N Konni', 'Dosso', 'Gaya', 'Tessaoua', 'Diffa'], 'NF': ['Kingston', 'Burnt Pine'], 'NG': ['Ibadan', 'Abuja', 'Port Harcourt', 'Kaduna', 'Benin City', 'Onitsha', 'Aba', 'Maiduguri', 'Ilorin', 'Jos', 'Sokoto', 'Zaria'], 'NI': ['Managua', 'León', 'Masaya', 'Chinandega', 'Matagalpa', 'Estelí', 'Granada', 'Mateare', 'Jinotega', 'El Viejo', 'Nueva Guinea', 'Ciudad Sandino'], 'NL': ['Rotterdam', 'The Hague', 'Utrecht', 'Groningen', 'Eindhoven', 'Tilburg', 'Breda', 'Nijmegen', 'Almere Stad', 'Haarlem', 'Arnhem', "'s-Hertogenbosch"], 'NO': ['Stavanger', 'Kristiansand', 'Drammen', 'Lillestrøm', 'Sandnes', 'Fredrikstad', 'Sandefjord', 'Asker', 'Sarpsborg', 'Tønsberg', 'Ålesund', 'Skien'], 'NP': ['Kathmandu', 'Pokhara', 'Bharatpur', 'Pātan', 'Birgañj', 'Biratnagar', 'Dhangaḍhi̇̄', 'Hetauda', 'Janakpur', 'Butwāl', 'Dharān', 'Nepalgunj'], 'NR': ['Yangor', 'Yaren', 'Baiti', 'Anabar', 'Anibare', 'Uaboe', 'Ijuw'], 'NU': ['Alofi', 'Hakupu', 'Avatele', 'Mutalau', 'Tuapa'], 'NZ': ['Manukau City', 'North Shore', 'Hamilton', 'Tauranga', 'Dunedin', 'Lower Hutt', 'Palmerston North', 'New Plymouth', 'Hastings', 'Napier', 'Rotorua', 'Porirua'], 'OM': ['Muscat', 'Seeb', 'Bawshar', '‘Ibrī', 'Şalālah', 'Şaḩam', 'Rustaq', 'Sohar', 'As Suwayq', 'Barkā’', 'Samā’il', 'Al Buraymī'], 'PA': ['Panama City', 'San Miguelito', 'Juan Díaz', 'David', 'Colón', 'Arraiján', 'Las Cumbres', 'La Chorrera', 'Pedregal', 'Tocumen', 'Santiago de Veraguas', 'Parque Lefevre'], 'PE': ['Callao', 'Trujillo', 'Piura', 'Chiclayo', 'Huancayo', 'Iquitos', 'Pucallpa', 'Chimbote', 'Tacna', 'Ica', 'Santiago de Surco', 'Juliaca'], 'PF': ['Faaa', 'Papeete', 'Punaauia', 'Pirae', 'Mahina', 'Paea', 'Papao', 'Arue', 'Vaitoare', 'Afaahiti', 'Uturoa', 'Taiohae'], 'PG': ['Port Moresby', 'Lae', 'Arawa', 'Mount Hagen', 'Popondetta', 'Madang', 'Kokopo', 'Mendi', 'Kimbe', 'Goroka', 'Wewak', 'Bulolo'], 'PH': ['Quezon City', 'Caloocan', 'Taguig', 'Budta', 'Malingao', 'Zamboanga', 'Cebu City', 'Antipolo', 'Pasig City', 'Cagayan de Oro', 'Valenzuela', 'General Santos'], 'PK': ['Lahore', 'Karachi', 'Peshawar', 'Faisalabad', 'Rawalpindi', 'Gujranwala', 'Multan', 'Hyderabad', 'Quetta', 'Bannu', 'Sargodha', 'Sialkot'], 'PL': ['Warsaw', 'Kraków', 'Wrocław', 'Łódź', 'Poznań', 'Szczecin', 'Lublin', 'Bydgoszcz', 'Białystok', 'Katowice', 'Gdynia', 'Częstochowa'], 'PM': ['Saint-Pierre', 'Miquelon'], 'PR': ['San Juan', 'Bayamón', 'Carolina', 'Ponce', 'Arecibo', 'Caguas', 'Guaynabo', 'Trujillo Alto', 'Mayagüez', 'Fajardo', 'Levittown', 'Vega Baja'], 'PS': ['East Jerusalem', 'Gaza', 'Khān Yūnis', 'Jabālyā', 'Hebron', 'Nablus', 'Rafaḩ', 'Dayr al Balaḩ', 'Bayt Lāhyā', 'Battir', 'Ţūlkarm', 'Ramallah'], 'PT': ['Lisbon', 'Porto', 'Braga', 'Amadora', 'Leiria', 'Setúbal', 'Funchal', 'Viseu', 'Queluz', 'Cacém', 'Aveiro', 'Vila Nova de Gaia'], 'PW': ['Koror', 'Koror Town', 'Kloulklubed', 'Ulimang', 'Mengellang', 'Ngchesar Hamlet', 'Melekeok Village', 'Ngchemiangel', 'Ngerkeai', 'Ngardmau', 'Angaur State', 'Kayangel'], 'PY': ['Asunción', 'Ciudad del Este', 'San Lorenzo', 'Capiatá', 'Lambaré', 'Fernando de la Mora', 'Limpio', 'Nemby', 'Pedro Juan Caballero', 'Encarnación', 'Mariano Roque Alonso', 'Itauguá'], 'QA': ['Doha', 'Ar Rayyān', 'Lusail', 'Al Maţār al ‘Atīq', 'Al Manşūrah', 'Az̧ Z̧a‘āyin', 'Madīnat Khalīfah', 'An Najmah', 'Al ‘Unayzah', 'Umm Ghuwaylīnah', 'As Sadd', 'Farīj al Amīr'], 'RO': ['Bucharest', 'Sector 3', 'Iaşi', 'Sector 6', 'Constanţa', 'Sector 2', 'Sector 4', 'Cluj-Napoca', 'Sector 5', 'Braşov', 'Timişoara', 'Craiova'], 'RS': ['Belgrade', 'Niš', 'Novi Sad', 'Novi Beograd', 'Zemun', 'Kragujevac', 'Čačak', 'Subotica', 'Leskovac', 'Novi Pazar', 'Kraljevo', 'Zrenjanin'], 'RU': ['Moscow', 'Saint Petersburg', 'Yekaterinburg', 'Nizhniy Novgorod', 'Kazan', 'Chelyabinsk', 'Omsk', 'Samara', 'Rostov-on-Don', 'Ufa', 'Krasnoyarsk', 'Voronezh'], 'RW': ['Kigali', 'Gisenyi', 'Musanze', 'Nyagatare', 'Gitarama', 'Muhanga', 'Butare', 'Kibuye', 'Rwamagana', 'Kibungo', 'Cyangugu', 'Shyorongi'], 'SA': ['Jeddah', 'Riyadh', 'Makkah', 'Madinah', 'Dammam', 'Sulţānah', 'Buraydah', 'Ta’if', 'Tabuk', "Ha'il", 'Najrān', 'Al Kharj'], 'SB': ['Honiara', 'Panatina', 'Nggosi', 'Tandai', "Kola'a", 'Vura', 'Malango', 'Vavaea', 'Noro', 'Gizo', 'Auki', 'Mbumburu'], 'SC': ['Victoria', 'Cascade', 'Perseverance', 'Baie Sainte Anne', 'Anse Boileau', 'Bel Ombre', 'Beau Vallon', 'Anse Royale', 'Port Glaud', 'Takamaka', 'La Passe'], 'SD': ['Khartoum', 'Omdurman', 'Khartoum North', 'Nyala', 'Port Sudan', 'Kassala', 'El Obeid', 'Al Qadarif', 'Kosti', 'Wad Medani', 'El Daein', 'El Fasher'], 'SE': ['Stockholm', 'Gothenburg', 'Uppsala', 'Linköping', 'Örebro', 'Sollentuna', 'Umeå', 'Västerås', 'Södermalm', 'Jönköping', 'Helsingborg', 'Norrköping'], 'SG': ['Singapore', 'Bedok New Town', 'Ulu Bedok', 'Sengkang New Town', 'Tampines Estate', 'Jurong Town', 'Tampines New Town', 'Woodlands', 'Jurong West', 'Yishun New Town', 'Hougang New Town', 'Punggol'], 'SI': ['Ljubljana', 'Maribor', 'Celje', 'Kranj', 'Koper', 'Novo Mesto', 'Velenje', 'Ptuj', 'Trbovlje', 'Kamnik', 'Jesenice', 'Domžale'], 'SJ': ['Longyearbyen', 'Olonkinbyen'], 'SK': ['Bratislava', 'Košice', 'Petržalka', 'Nitra', 'Prešov', 'Žilina', 'Banská Bystrica', 'Trnava', 'Trenčín', 'Martin', 'Poprad', 'Staré Mesto'], 'SL': ['Freetown', 'Kenema', 'Bo', 'Koidu', 'Makeni', 'Waterloo', 'Port Loko', 'Njala', 'Lunsar', 'Goderich', 'Kabala', 'Segbwema'], 'SM': ['Serravalle', 'Dogana', 'Valdragone', 'Borgo Maggiore', 'San Marino', 'Domagnano', 'Fiorentino', 'Acquaviva', 'Faetano', 'Poggio di Chiesanuova', 'Monte Giardino'], 'SN': ['Dakar', 'Pikine', 'Touba', 'Guédiawaye', 'Thiès', 'Kaolack', 'Rufisque', 'Mbour', 'Saint-Louis', 'Thiès Nones', 'Rufisque est', 'Ziguinchor'], 'SO': ['Mogadishu', 'Borama', 'Hargeysa', 'Berbera', 'Kismayo', 'Marka', 'El Dibir', 'Ruqi', 'Baidoa', 'Cabudwaaq', 'Burao', 'Kaambooni'], 'SR': ['Paramaribo', 'Blauwgrond', 'Latour', 'Pontbuiten', 'Rainville', 'Flora', 'Welgelegen', 'Lelydorp', 'Munder Buiten', 'Beekhuizen', 'Weg naar Zee', 'Tammenga'], 'SS': ['Juba', 'Winejok', 'Yei', 'Malakal', 'Wau', 'Kuacjok', 'Pajok', 'Gogrial', 'Yambio', 'Aweil', 'Rumbek', 'Bor'], 'ST': ['São Tomé', 'Neves', 'Água Izé', 'Folha Fede', 'Santo António'], 'SV': ['San Salvador', 'Soyapango', 'San Miguel', 'Santa Ana', 'Mejicanos', 'Santa Tecla', 'Apopa', 'Delgado', 'Sonsonate', 'San Marcos', 'Usulután', 'Cojutepeque'], 'SX': ['Cul de Sac', 'Lower Prince’s Quarter', 'Koolbaai', 'Little Bay', 'Philipsburg'], 'SY': ['Aleppo', 'Damascus', 'Homs', 'Latakia', 'Ar Raqqah', 'Ḩamāh', 'Ţarţūs', 'Al Ḩasakah', 'Deir ez-Zor', 'Al Qāmishlī', 'Al Bāb', 'Idlib'], 'SZ': ['Manzini', 'Mbabane', 'Malkerns', 'Nhlangano', 'Mhlume', 'Hluti', 'Big Bend', 'Siteki', 'Piggs Peak', 'Lobamba'], 'TC': ['Providenciales', 'Cockburn Town'], 'TD': ["N'Djamena", 'Moundou', 'Abéché', 'Sarh', 'Kelo', 'Am Timan', 'Doba', 'Pala', 'Bongor', 'Goz Beida', 'Koumra', 'Mongo'], 'TG': ['Lomé', 'Sokodé', 'Kara', 'Atakpamé', 'Kpalimé', 'Bassar', 'Dapaong', 'Tsévié', 'Aného', 'Mango', 'Anié', 'Notsé'], 'TH': ['Samut Prakan', 'Mueang Nonthaburi', 'Chon Buri', 'Phra Pradaeng', 'Bang Khae', 'Hat Yai', 'Pak Kret', 'Sai Mai', 'Si Racha', 'Latkrabang', 'Watthana', 'Khlong Sam Wa'], 'TJ': ['Dushanbe', 'Isfara', 'Istaravshan', 'Kŭlob', 'Konibodom', 'Khujand', 'Bokhtar', 'Qayroqqum', 'Vahdat', 'Tursunzoda', 'Buston', 'Panjakent'], 'TK': ['Nukunonu', 'Atafu Village', 'Fale old settlement'], 'TL': ['Dili', 'Maliana', 'Suai', 'Likisá', 'Aileu', 'Lospalos', 'Atsabe', 'Maubara', 'Baukau', 'Venilale', 'Ainaro', 'Hatoudo'], 'TM': ['Ashgabat', 'Türkmenabat', 'Daşoguz', 'Mary', 'Türkmenbaşy', 'Balkanabat', 'Bayramaly', 'Tejen', 'Gyzylarbat', 'Magdanly', 'Boldumsaz', 'Abadan'], 'TN': ['Tunis', 'Sfax', 'Sousse', 'Sukrah', 'Kairouan', 'Bizerte', 'Sīdī Ḥusayn', 'Sakiet ed Daier', 'El Mourouj', 'Aryanah', 'Gabès', 'Hammamet'], 'TO': ['Nuku‘alofa', 'Neiafu', 'Pangai', "'Ohonua", 'Hihifo'], 'TR': ['Istanbul', 'Bursa', 'İzmir', 'Gaziantep', 'Diyarbakır', 'Adana', 'Kayseri', 'Konya', 'Antalya', 'Esenyurt', 'Eskişehir', 'Çankaya'], 'TT': ['Chaguanas', 'Mon Repos', 'San Fernando', 'Port of Spain', 'Rio Claro', 'Arima', 'Marabella', 'Diego Martin', 'Laventille', 'Point Fortin', 'Tunapuna', 'Scarborough'], 'TV': ['Funafuti', 'Savave Village', 'Tanrake Village', 'Toga Village', 'Asau Village', 'Kulia Village'], 'TW': ['New Taipei City', 'Taichung', 'Tainan', 'Banqiao', 'Taoyuan', 'Hsinchu', 'Keelung', 'Fengshan', 'Neihu', 'Chiayi City', 'Yongkang', 'Chang-hua'], 'TZ': ['Dar es Salaam', 'Mwanza', 'Dodoma', 'Zanzibar', 'Arusha', 'Mbeya', 'Morogoro', 'Kahama', 'Tanga', 'Geita', 'Tabora', 'Sumbawanga'], 'UA': ['Kharkiv', 'Dnipro', 'Donetsk', 'Lviv', 'Zaporizhzhya', 'Kryvyy Rih', 'Sevastopol', 'Mykolayiv', 'Vinnytsya', 'Saltivka', 'Luhansk', 'Desna'], 'UG': ['Kampala', 'Nansana', 'Kira', 'Bunamwaya', 'Kyengera', 'Kasangati', 'Mbarara', 'Njeru', 'Mukono', 'Gulu', 'Kajansi', 'Katabi'], 'US': ['New York City', 'Brooklyn', 'Chicago', 'Queens', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'Manhattan', 'San Diego', 'The Bronx', 'Dallas'], 'UY': ['Montevideo', 'Salto', 'Maldonado', 'Rivera', 'Paysandú', 'Las Piedras', 'Tacuarembó', 'Melo', 'Artigas', 'Mercedes', 'Durazno', 'Minas'], 'UZ': ['Tashkent', 'Andijon', 'Namangan', 'Samarkand', 'Yunusobod', 'Nukus', 'Fergana', 'Bukhara', 'Qarshi', 'Chilanzar', 'Qo‘qon', 'Marg‘ilon'], 'VA': ['Vatican City'], 'VC': ['Kingstown', 'Calliaqua', 'Georgetown', 'Barrouallie', 'Port Elizabeth', 'Chateaubelair', 'Layou'], 'VE': ['Barquisimeto', 'Ciudad Guayana', 'Barcelona', 'Maturín', 'Maracay', 'Ciudad Bolívar', 'Cumaná', 'Barinas', 'Puerto La Cruz', 'Petare', 'Cabimas', 'Turmero'], 'VG': ['Road Town', 'Spanish Town', 'The Settlement'], 'VI': ['Saint Croix', 'Charlotte Amalie', 'Tutu', 'Cruz Bay'], 'VN': ['Ho Chi Minh City', 'Haiphong', 'Cần Thơ', 'Huế', 'Biên Hòa', 'Thanh Hóa', 'Vinh', 'Thuận An', 'Nha Trang', 'Chợ Lớn', 'Bình Thạnh', 'Thủ Đức'], 'VU': ['Port-Vila', 'Luganville', 'Isangel', 'Sola', 'Lakatoro', 'Saratamata'], 'WF': ['Mata-Utu', 'Leava', 'Alo'], 'WS': ['Apia', 'Palauli', 'Vaitele', 'Asau', 'Mulifanua', 'Afega', 'Leulumoega', 'Safotu', 'Lufilufi', 'Vailoa', 'Samamea', 'Safotulafai'], 'YE': ['Sanaa', 'Aden', 'Taiz', 'Ibb', 'Al Ḩudaydah', 'Mukalla', 'Dhamār', '‘Amrān', 'Sayyān', 'Zabīd', "Sa'dah", 'Bājil'], 'ZA': ['Johannesburg', 'Cape Town', 'Durban', 'Soweto', 'Gqeberha', 'Soshanguve', 'Pietermaritzburg', 'Evaton', 'Benoni', 'Bloemfontein', 'Thembisa', 'East London'], 'ZM': ['Lusaka', 'Kitwe', 'Ndola', 'Chipata', 'Solwezi', 'Kabwe', 'Chingola', 'Luanshya', 'Kasama', 'Livingstone', 'Mansa', 'Mufulira'], 'ZW': ['Harare', 'Bulawayo', 'Chitungwiza', 'Mutare', 'Epworth', 'Gweru', 'Kwekwe', 'Kadoma', 'Ruwa', 'Chinhoyi', 'Masvingo', 'Norton']}
# Recorre `LOCALIDADES_ADICIONALES_POR_PAIS.items()`; ejecuta el bloque una vez por cada valor asignado a `(_codigo_localidad, _localidades_adicionales)`.
for _codigo_localidad, _localidades_adicionales in LOCALIDADES_ADICIONALES_POR_PAIS.items():
    # Añadir a la lista todos los elementos de la colección indicada.
    LOCALIDADES_POR_PAIS.setdefault(_codigo_localidad, []).extend(_localidades_adicionales)
# Define `TIPOS_CANCER` para listar tipos generales que puede producir la simulación ficticia.
TIPOS_CANCER = ['cáncer de mama', 'cáncer de pulmón', 'cáncer colorrectal', 'cáncer de piel (melanoma)', 'cáncer de piel (no melanoma)', 'cáncer de páncreas', 'cáncer de hígado', 'cáncer de estómago', 'cáncer de esófago', 'cáncer de riñón', 'cáncer de vejiga', 'cáncer de tiroides', 'cáncer de cerebro', 'leucemia', 'linfoma de Hodgkin', 'linfoma no Hodgkin', 'mieloma múltiple', 'cáncer de hueso', 'cáncer de boca', 'cáncer de garganta', 'cáncer de laringe', 'cáncer de nasofaringe', 'cáncer de vesícula biliar', 'cáncer de vías biliares', 'cáncer de intestino delgado', 'cáncer de recto', 'cáncer de ano', 'mesotelioma', 'sarcoma', 'neuroblastoma', 'retinoblastoma', 'tumor carcinoide', 'cáncer de glándulas salivales']
# Define `TIPOS_CANCER_POR_GENERO` para listar tipos ficticios asociados al género.
TIPOS_CANCER_POR_GENERO = {'F': ['cáncer de ovario', 'cáncer de útero', 'cáncer de cuello uterino', 'cáncer de endometrio', 'cáncer de vulva', 'cáncer de vagina'], 'M': ['cáncer de próstata', 'cáncer testicular']}

# Define `determinar_signo_zodiacal` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_signo_zodiacal(fecha_nacimiento):
    """Devuelve el signo zodiacal occidental según el día y el mes."""
    # Crea `limites` con los datos u opciones que se procesan después.
    limites = [((1, 20), 'Acuario'), ((2, 19), 'Piscis'), ((3, 21), 'Aries'), ((4, 20), 'Tauro'), ((5, 21), 'Géminis'), ((6, 21), 'Cáncer'), ((7, 23), 'Leo'), ((8, 23), 'Virgo'), ((9, 23), 'Libra'), ((10, 23), 'Escorpio'), ((11, 22), 'Sagitario'), ((12, 22), 'Capricornio')]
    # Crea `fecha` con los datos u opciones que se procesan después.
    fecha = (fecha_nacimiento.month, fecha_nacimiento.day)
    # Recorre `reversed(limites)`; ejecuta el bloque una vez por cada valor asignado a `((mes_inicio, dia_inicio), signo)`.
    for (mes_inicio, dia_inicio), signo in reversed(limites):
        # Comprueba `fecha >= (mes_inicio, dia_inicio)`; solo ejecuta este bloque cuando se cumple la condición.
        if fecha >= (mes_inicio, dia_inicio):
            # Devuelve `signo` al código que llamó a esta función.
            return signo
    # Devuelve `'Capricornio'` al código que llamó a esta función.
    return 'Capricornio'

# Define `determinar_localidad_nacimiento` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_localidad_nacimiento(pais):
    """Escoge una localidad de la muestra correspondiente al país."""
    # Calcula y guarda en `probabilidad_atlantis` el valor que se necesita en las instrucciones siguientes.
    probabilidad_atlantis = 1e-14
    # Calcula y guarda en `probabilidad_espacio` el valor que se necesita en las instrucciones siguientes.
    probabilidad_espacio = 1e-07
    # Guarda en `tirada_lugar_especial` el resultado de obtener un decimal aleatorio entre 0 y 1 para compararlo con una probabilidad; se reutiliza en los pasos siguientes.
    tirada_lugar_especial = random.random()
    # Comprueba `tirada_lugar_especial < probabilidad_atlantis`; solo ejecuta este bloque cuando se cumple la condición.
    if tirada_lugar_especial < probabilidad_atlantis:
        # Devuelve `'Atlantis'` al código que llamó a esta función.
        return 'Atlantis'
    # Comprueba `tirada_lugar_especial < probabilidad_atlantis + probabilidad_espacio`; solo ejecuta este bloque cuando se cumple la condición.
    if tirada_lugar_especial < probabilidad_atlantis + probabilidad_espacio:
        # Devuelve `'Espacio'` al código que llamó a esta función.
        return 'Espacio'
    # La capital sirve de alternativa cuando el catálogo no tiene ciudades para ese país.
    # Guarda en `localidades` el resultado de obtener el resultado de `LOCALIDADES_POR_PAIS.get`; se reutiliza en los pasos siguientes.
    localidades = LOCALIDADES_POR_PAIS.get(pais, [])
    # Guarda en `capital` el resultado de obtener el resultado de `CAPITALES_POR_PAIS.get`; se reutiliza en los pasos siguientes.
    capital = CAPITALES_POR_PAIS.get(pais)
    # Comprueba `capital is None`; solo ejecuta este bloque cuando se cumple la condición.
    if capital is None:
        # Lanza `ValueError(f'No hay localidades ni capital catalogadas para el país {pais}.')` para informar que este caso no se puede procesar.
        raise ValueError(f'No hay localidades ni capital catalogadas para el país {pais}.')
    # Devuelve `random.choice(localidades or [capital])` al código que llamó a esta función.
    return random.choice(localidades or [capital])

# Define `formatear_pais` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def formatear_pais(pais):
    """Devuelve el código y el nombre del país para mostrarlo en informes."""
    nombre = NOMBRES_PAISES.get(pais)
    return f'{pais}, {nombre}' if nombre else pais

# Define `determinar_tipo_cancer` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_tipo_cancer(genero):
    """Aplica la probabilidad ficticia de cáncer con tipos compatibles con el género."""
    # Comprueba `random.random() < 0.00031415926`; solo ejecuta este bloque cuando se cumple la condición.
    if random.random() < 0.00031415926:
        # Calcula y guarda en `opciones` el valor que se necesita en las instrucciones siguientes.
        opciones = TIPOS_CANCER + TIPOS_CANCER_POR_GENERO.get(genero, [])
        # Devuelve `random.choice(opciones)` al código que llamó a esta función.
        return random.choice(opciones)
    # Devuelve `None` al código que llamó a esta función.
    return None

# Define `determinar_tid` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_tid():
    """Determina el trastorno y la capacidad ficticia asociada."""
    # Comprueba `random.randint(1, 9218) != 3`; solo ejecuta este bloque cuando se cumple la condición.
    if random.randint(1, 9218) != 3:
        # Devuelve `(None, None)` al código que llamó a esta función.
        return (None, None)
    # Calcula y guarda en `poder_tid` el valor que se necesita en las instrucciones siguientes.
    poder_tid = 'Duplicarse' if random.choice(('cara', 'cruz')) == 'cara' else 'Otras mentes'
    # Devuelve `('Trastorno de identidad disociativa', poder_tid)` al código que llamó a esta función.
    return ('Trastorno de identidad disociativa', poder_tid)

# Define `pedir_pais` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def pedir_pais(nombre_progenitor):
    """Solicita un código reconocido y repite la pregunta si la entrada no es válida."""
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `pais` el resultado de obtener el resultado de `input(f'Introduce el código del país ...`; se reutiliza en los pasos siguientes.
        pais = input(f'Introduce el código del país de {nombre_progenitor} (por ejemplo, ES; ZW; FR; ATL; TER; JP...): ').strip().upper()
        # Comprueba `pais in TODOS_LOS_PAISES`; solo ejecuta este bloque cuando se cumple la condición.
        if pais in TODOS_LOS_PAISES:
            # Devuelve `pais` al código que llamó a esta función.
            return pais
        # Mostrar el mensaje o resultado en la consola.
        print('Código de país inválido o no reconocido. Usa un código ISO, como ES (España), JP (Japón), ZW (Zimbabue)... ')

# Define `obtener_region` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def obtener_region(pais):
    """Busca la región asociada al código; los catálogos deben incluir todos los países."""
    # Devuelve `next((region for region, paises in PAISES_POR_REGION.items() if pais in paises))` al código que llamó a esta función.
    return next((region for region, paises in PAISES_POR_REGION.items() if pais in paises))

# Define `pedir_apellido` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def pedir_apellido(nombre_progenitor):
    """Pide un apellido obligatorio y no acepta una cadena vacía."""
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `apellido` el resultado de obtener el resultado de `input(f'Introduce el apellido de {nom...`; se reutiliza en los pasos siguientes.
        apellido = input(f'Introduce el apellido de {nombre_progenitor}: ').strip()
        # Comprueba `apellido`; solo ejecuta este bloque cuando se cumple la condición.
        if apellido:
            # Devuelve `apellido` al código que llamó a esta función.
            return apellido
        # Mostrar el mensaje o resultado en la consola.
        print('El apellido no puede estar vacío.')

# Define `pedir_nombre_padre` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def pedir_nombre_padre():
    """Pide el nombre de pila del padre porque se usa para formar el nombre del hijo."""
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `nombre` el resultado de obtener el resultado de `input('Introduce el nombre de pila de...`; se reutiliza en los pasos siguientes.
        nombre = input('Introduce el nombre de pila del padre: ').strip()
        # Comprueba `nombre`; solo ejecuta este bloque cuando se cumple la condición.
        if nombre:
            # Devuelve `nombre` al código que llamó a esta función.
            return nombre
        # Mostrar el mensaje o resultado en la consola.
        print('El nombre no puede estar vacío.')

# Define `generar_nombre_hijo` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def generar_nombre_hijo(genero, pais_padre, pais_madre, nombre_padre, apellido_padre, apellido_madre):
    """Genera nombre(s) regionales y los combina con ambos apellidos parentales."""
    # Crea `paises_parentales` con los datos u opciones que se procesan después.
    paises_parentales = {pais_padre, pais_madre}
    # Comprueba `random.random() < 0.2`; solo ejecuta este bloque cuando se cumple la condición.
    if random.random() < 0.2:
        # Crea `paises_con_banco` con los datos u opciones que se procesan después.
        paises_con_banco = {pais for region, paises in PAISES_POR_REGION.items() if region in BANCO_NOMBRES_POR_REGION for pais in paises}
        # Guarda en `paises_externos` el resultado de obtener el resultado de `sorted`; se reutiliza en los pasos siguientes.
        paises_externos = sorted(paises_con_banco - paises_parentales)
        # Comprueba `not paises_externos`; solo ejecuta este bloque cuando se cumple la condición.
        if not paises_externos:
            # Lanza `ValueError('No hay países externos disponibles para generar el nombre.')` para informar que este caso no se puede procesar.
            raise ValueError('No hay países externos disponibles para generar el nombre.')
        # Guarda en `pais_origen_nombre` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        pais_origen_nombre = random.choice(paises_externos)
    # Si `random.random() < 0.2` no se cumple, ejecuta esta alternativa.
    else:
        # Guarda en `pais_origen_nombre` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        pais_origen_nombre = random.choice((pais_padre, pais_madre))
    # Calcula y guarda en `banco` el valor que se necesita en las instrucciones siguientes.
    banco = BANCO_NOMBRES_POR_REGION[obtener_region(pais_origen_nombre)]
    # Guarda en `nombres` el resultado de obtener el resultado de `quitar_nombres_duplicados`; se reutiliza en los pasos siguientes.
    nombres = quitar_nombres_duplicados((*banco[genero], *banco['N']))
    # Guarda en `nombre` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
    nombre = random.choice(nombres)
    # Guarda en `tiene_segundo_nombre` `True` o `False` según se cumpla la comparación.
    tiene_segundo_nombre = random.random() < 0.33
    # Comprueba `tiene_segundo_nombre`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_segundo_nombre:
        # Guarda en `clave_nombre` el resultado de obtener el resultado de `clave_normalizada_nombre`; se reutiliza en los pasos siguientes.
        clave_nombre = clave_normalizada_nombre(nombre)
        # Crea `nombres_segundo` con los datos u opciones que se procesan después.
        nombres_segundo = [opcion for opcion in nombres if clave_normalizada_nombre(opcion) != clave_nombre]
        # Guarda en `segundo_nombre` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        segundo_nombre = random.choice(nombres_segundo)
        # Construye en `nombre` un texto con valores interpolados para usarlo después.
        nombre = f'{nombre} {segundo_nombre}'
    # Comprueba `clave_normalizada_nombre(nombre.split()[0]) == clave_normalizada_nombre(nombre_padre.split()[0])`; solo ejecuta este bloque cuando se cumple la condición.
    if clave_normalizada_nombre(nombre.split()[0]) == clave_normalizada_nombre(nombre_padre.split()[0]):
        # Construye en `nombre` un texto con valores interpolados para usarlo después.
        nombre = f'{nombre} Junior'
    # Construye en `nombre_completo` un texto con valores interpolados para usarlo después.
    nombre_completo = f'{nombre} {apellido_padre} {apellido_madre}'
    # Devuelve `(nombre_completo, pais_origen_nombre, tiene_segundo_nombre)` al código que llamó a esta función.
    return (nombre_completo, pais_origen_nombre, tiene_segundo_nombre)

# Define `elegir_pais_de_region` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def elegir_pais_de_region(region, excluir):
    """Escoge de forma estable entre los países de una región que no estén excluidos."""
    # Guarda en `opciones` el resultado de obtener el resultado de `sorted`; se reutiliza en los pasos siguientes.
    opciones = sorted(PAISES_POR_REGION[region] - excluir)
    # Devuelve `random.choice(opciones) if opciones else None` al código que llamó a esta función.
    return random.choice(opciones) if opciones else None

# Define `elegir_otro_pais` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def elegir_otro_pais(excluir):
    """Elige un país fuera del conjunto excluido; India tiene aquí un peso preferente."""
    # Guarda en `opciones` el resultado de obtener el resultado de `sorted`; se reutiliza en los pasos siguientes.
    opciones = sorted(TODOS_LOS_PAISES - excluir)
    # Comprueba `not opciones`; solo ejecuta este bloque cuando se cumple la condición.
    if not opciones:
        # Lanza `ValueError('No hay países alternativos disponibles para la simulación.')` para informar que este caso no se puede procesar.
        raise ValueError('No hay países alternativos disponibles para la simulación.')
    # Comprueba `'IN' in opciones and random.random() < 0.8`; solo ejecuta este bloque cuando se cumple la condición.
    if 'IN' in opciones and random.random() < 0.8:
        # Devuelve `'IN'` al código que llamó a esta función.
        return 'IN'
    # Crea `opciones_sin_india` con los datos u opciones que se procesan después.
    opciones_sin_india = [pais for pais in opciones if pais != 'IN']
    # Devuelve `random.choice(opciones_sin_india or opciones)` al código que llamó a esta función.
    return random.choice(opciones_sin_india or opciones)

# Define `determinar_pais_hijo` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_pais_hijo(pais_padre, pais_madre):
    """Calcula el país según los países parentales y las probabilidades establecidas."""
    # Crea `progenitores` con los datos u opciones que se procesan después.
    progenitores = {pais_padre, pais_madre}
    # Comprueba `'KP' in progenitores`; solo ejecuta este bloque cuando se cumple la condición.
    if 'KP' in progenitores:
        # Comprueba `random.random() < 0.99`; solo ejecuta este bloque cuando se cumple la condición.
        if random.random() < 0.99:
            # Devuelve `'KP'` al código que llamó a esta función.
            return 'KP'
        # Devuelve `elegir_otro_pais(progenitores)` al código que llamó a esta función.
        return elegir_otro_pais(progenitores)
    # Comprueba `pais_padre == pais_madre`; solo ejecuta este bloque cuando se cumple la condición.
    if pais_padre == pais_madre:
        # Crea `pesos_regionales` para guardar las regiones candidatas y el peso de cada una.
        pesos_regionales = [(obtener_region(pais_padre), 8)]
        # Crea `pesos_progenitores` para guardar los países parentales y el peso de cada uno.
        pesos_progenitores = [(pais_padre, 90)]
    # Comprueba `obtener_region(pais_padre) == obtener_region(pais_madre)`; solo ejecuta este bloque cuando se cumple la condición.
    elif obtener_region(pais_padre) == obtener_region(pais_madre):
        # Crea `pesos_regionales` para guardar las regiones candidatas y el peso de cada una.
        pesos_regionales = [(obtener_region(pais_padre), 8)]
        # Crea `pesos_progenitores` para guardar los países parentales y el peso de cada uno.
        pesos_progenitores = [(pais_padre, 45), (pais_madre, 45)]
    # Si `obtener_region(pais_padre) == obtener_region(pais_madre)` no se cumple, ejecuta esta alternativa.
    else:
        # Crea `pesos_regionales` para guardar las regiones candidatas y el peso de cada una.
        pesos_regionales = [(obtener_region(pais_padre), 4), (obtener_region(pais_madre), 4)]
        # Crea `pesos_progenitores` para guardar los países parentales y el peso de cada uno.
        pesos_progenitores = [(pais_padre, 45), (pais_madre, 45)]
    # Crea `regiones_excluidas` para identificar regiones que no deben repetirse en la categoría de otros países.
    regiones_excluidas = {region for region, _ in pesos_regionales}
    # Crea `pesos` con los datos u opciones que se procesan después.
    pesos = [(('parental', pais), peso) for pais, peso in pesos_progenitores]
    # Añadir a la lista todos los elementos de la colección indicada.
    pesos.extend(((('regional', region), peso) for region, peso in pesos_regionales if PAISES_POR_REGION[region] - progenitores))
    # Añadir un solo elemento a la lista que se está construyendo.
    pesos.append((('other', None), 2))
    # Calcula y guarda en `otros_paises` el valor que se necesita en las instrucciones siguientes.
    otros_paises = TODOS_LOS_PAISES - progenitores
    # Recorre `regiones_excluidas`; ejecuta el bloque una vez por cada valor asignado a `region`.
    for region in regiones_excluidas:
        # Actualiza `otros_paises`: resta el valor actual con `PAISES_POR_REGION[region]`.
        otros_paises -= PAISES_POR_REGION[region]
    # Calcula y guarda en `seleccion` el valor que se necesita en las instrucciones siguientes.
    seleccion = random.choices([categoria for categoria, _ in pesos], weights=[peso for _, peso in pesos], k=1)[0]
    # Desempaqueta el resultado en `tipo`, `valor`; cada valor queda asociado a su variable correspondiente.
    tipo, valor = seleccion
    # Comprueba `tipo == 'parental'`; solo ejecuta este bloque cuando se cumple la condición.
    if tipo == 'parental':
        # Devuelve `valor` al código que llamó a esta función.
        return valor
    # Comprueba `tipo == 'regional'`; solo ejecuta este bloque cuando se cumple la condición.
    if tipo == 'regional':
        # Devuelve `elegir_pais_de_region(valor, progenitores)` al código que llamó a esta función.
        return elegir_pais_de_region(valor, progenitores)
    # Devuelve `elegir_otro_pais(progenitores | TODOS_LOS_PAISES - otros_paises)` al código que llamó a esta función.
    return elegir_otro_pais(progenitores | TODOS_LOS_PAISES - otros_paises)

# Define `pedir_fecha_concepcion` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def pedir_fecha_concepcion():
    """Lee la fecha en formato día/mes/año y vuelve a pedirla si no existe o no encaja."""
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `fecha_input` el resultado de obtener el resultado de `input('Introduce la fecha de concepci...`; se reutiliza en los pasos siguientes.
        fecha_input = input('Introduce la fecha de concepción (DD/MM/AAAA): ').strip()
        # Protege esta operación para poder atender de forma explícita los errores que puedan ocurrir.
        try:
            # Devuelve `datetime.strptime(fecha_input, '%d/%m/%Y').date()` al código que llamó a esta función.
            return datetime.strptime(fecha_input, '%d/%m/%Y').date()
        # Si el bloque protegido provoca `ValueError`, ejecuta esta rama para tratar el error explícitamente.
        except ValueError:
            # Mostrar el mensaje o resultado en la consola.
            print('Fecha inválida. Usa el formato DD/MM/AAAA y una fecha válida.')

# Define `determinar_gestacion` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_gestacion():
    """Selecciona la duración gestacional con las probabilidades indicadas."""
    # Crea `etapas` con los datos u opciones que se procesan después.
    etapas = [(7, 7), (8, 25), (9, 65), (10, 1.5), (11, 1), (12, 0.5)]
    # random.choices usa pesos relativos: no hace falta que sumen exactamente 100.
    # Calcula y guarda en `mes_gestacion` el valor que se necesita en las instrucciones siguientes.
    mes_gestacion = random.choices([mes for mes, _ in etapas], weights=[probabilidad for _, probabilidad in etapas], k=1)[0]
    # Cada intervalo de días corresponde a la etapa seleccionada; randint incluye ambos extremos.
    # Crea `rangos_dias` con los datos u opciones que se procesan después.
    rangos_dias = {7: (210, 249), 8: (250, 269), 9: (260, 300), 10: (301, 330), 11: (331, 345), 12: (346, 360)}
    # Guarda en `dias_gestacion` el resultado de obtener un entero aleatorio dentro del intervalo, incluidos sus extremos; se reutiliza en los pasos siguientes.
    dias_gestacion = random.randint(*rangos_dias[mes_gestacion])
    # Devuelve `(mes_gestacion, dias_gestacion)` al código que llamó a esta función.
    return (mes_gestacion, dias_gestacion)

# Define `tiene_enfermedad_genetica` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def tiene_enfermedad_genetica(mes_gestacion):
    """Aplica la regla ficticia: solo hay tirada adicional si la gestación no dura nueve meses."""
    # Devuelve `mes_gestacion != 9 and random.randint(1, 100) <= 5` al código que llamó a esta función.
    return mes_gestacion != 9 and random.randint(1, 100) <= 5

# Define `determinar_reconocimientos` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_reconocimientos(genero, fecha_nacimiento, poderes_activos, genoma, tiene_autismo_y_tea=False):
    """Reúne reconocimientos especiales cuando se cumplen todas sus condiciones."""
    # Crea `reconocimientos` para acumular los mensajes especiales que cumplen sus condiciones.
    reconocimientos = []
    # Guarda en `nace_18_abril` `True` o `False` según se cumpla la comparación.
    nace_18_abril = (fecha_nacimiento.month, fecha_nacimiento.day) == (4, 18)
    # Comprueba `nace_18_abril`; solo ejecuta este bloque cuando se cumple la condición.
    if nace_18_abril:
        # Añadir un solo elemento a la lista que se está construyendo.
        reconocimientos.append('felicidades creador')
    # Crea `poderes_requeridos` con los datos u opciones que se procesan después.
    poderes_requeridos = {3, 6, 9, 10, 13, 15, 16, 19}
    # Guarda en `tiene_genoma_ab` el resultado de obtener el resultado de `all`; se reutiliza en los pasos siguientes.
    tiene_genoma_ab = all((genoma.get(cromosoma) == 'Ab' for cromosoma in range(1, 23)))
    # Comprueba `nace_18_abril and genero == 'M' and poderes_requeridos.issubset(poderes_activos) and tiene_genoma...`; solo ejecuta este bloque cuando se cumple la condición.
    if nace_18_abril and genero == 'M' and poderes_requeridos.issubset(poderes_activos) and tiene_genoma_ab and tiene_autismo_y_tea:
        # Añadir un solo elemento a la lista que se está construyendo.
        reconocimientos.append('Poder ilimitado, Izan')
    # Devuelve `reconocimientos` al código que llamó a esta función.
    return reconocimientos

# Define `comprobar_tabla_activacion` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def comprobar_tabla_activacion(p_gen, m_gen):
    """Verifica si la combinación Padre-Madre resulta en Positivo según tus reglas"""
    # Comprueba `m_gen == 'ab'`; solo ejecuta este bloque cuando se cumple la condición.
    if m_gen == 'ab':
        # Devuelve `False` al código que llamó a esta función.
        return False
    # Crea `combinaciones_positivas` con los datos u opciones que se procesan después.
    combinaciones_positivas = [('AB', 'AB'), ('Ab', 'AB'), ('aB', 'AB'), ('ab', 'AB'), ('AB', 'Ab'), ('aB', 'Ab'), ('AB', 'aB'), ('Ab', 'aB')]
    # Devuelve `(p_gen, m_gen) in combinaciones_positivas` al código que llamó a esta función.
    return (p_gen, m_gen) in combinaciones_positivas

# Define `evaluar_poder_cromosomico` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def evaluar_poder_cromosomico(cromosoma, padre, madre, genoma_hijo):
    """Evalúa la herencia, el poder nuevo y una posible mutación positiva."""
    # Guarda en `combinacion_positiva` el resultado de obtener el resultado de `comprobar_tabla_activacion`; se reutiliza en los pasos siguientes.
    combinacion_positiva = comprobar_tabla_activacion(padre[cromosoma]['genes'], madre[cromosoma]['genes'])
    # Calcula y guarda en `poder_heredado` el resultado lógico de esta condición.
    poder_heredado = combinacion_positiva and padre[cromosoma]['poder'] == 1 and (madre[cromosoma]['poder'] == 1)
    # Calcula y guarda en `poder_nuevo` el resultado lógico de esta condición.
    poder_nuevo = padre[cromosoma]['poder'] != 1 and madre[cromosoma]['poder'] != 1 and (random.random() < 0.03)
    # Calcula y guarda en `mutacion_positiva` el resultado lógico de esta condición.
    mutacion_positiva = not combinacion_positiva and random.random() < 0.06
    # Comprueba `mutacion_positiva`; solo ejecuta este bloque cuando se cumple la condición.
    if mutacion_positiva:
        # Calcula y guarda en `genoma_hijo[cromosoma]` el valor que se necesita en las instrucciones siguientes.
        genoma_hijo[cromosoma] = 'AB'
    # Devuelve `(poder_heredado or poder_nuevo, poder_nuevo, mutacion_positiva)` al código que llamó a esta función.
    return (poder_heredado or poder_nuevo, poder_nuevo, mutacion_positiva)

# Define `tirar_con_bono_probabilidad` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def tirar_con_bono_probabilidad(tirada_base, probabilidad_base, bono):
    """Aplica un bono en puntos porcentuales sin alterar la probabilidad base."""
    # Comprueba `tirada_base or bono <= 0`; solo ejecuta este bloque cuando se cumple la condición.
    if tirada_base or bono <= 0:
        # Devuelve `tirada_base` al código que llamó a esta función.
        return tirada_base
    # Como la tirada base ya falló, se calcula la probabilidad condicional necesaria
    # para que el resultado final aumente exactamente en el bono solicitado.
    # Guarda en `probabilidad_extra` el resultado de obtener el resultado de `min`; se reutiliza en los pasos siguientes.
    probabilidad_extra = min(1, bono / (1 - probabilidad_base))
    # Devuelve `random.random() < probabilidad_extra` al código que llamó a esta función.
    return random.random() < probabilidad_extra

# Define `ajustar_probabilidades` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def ajustar_probabilidades(probabilidades, indice_favorecido, bono):
    """Suma un bono a una opción y lo resta proporcionalmente a las demás."""
    # Comprueba `indice_favorecido is None or bono <= 0`; solo ejecuta este bloque cuando se cumple la condición.
    if indice_favorecido is None or bono <= 0:
        # Devuelve `probabilidades` al código que llamó a esta función.
        return probabilidades
    # Guarda en `probabilidades` el resultado de obtener el resultado de `list`; se reutiliza en los pasos siguientes.
    probabilidades = list(probabilidades)
    # Guarda en `bono` el resultado de obtener el resultado de `min`; se reutiliza en los pasos siguientes.
    bono = min(bono, 1 - probabilidades[indice_favorecido])
    # Calcula y guarda en `resto_original` el valor que se necesita en las instrucciones siguientes.
    resto_original = 1 - probabilidades[indice_favorecido]
    # Comprueba `resto_original <= 0`; solo ejecuta este bloque cuando se cumple la condición.
    if resto_original <= 0:
        # Devuelve `probabilidades` al código que llamó a esta función.
        return probabilidades
    # Se conserva la suma total en 1 repartiendo la reducción entre las otras opciones.
    # Calcula y guarda en `factor_resto` el valor que se necesita en las instrucciones siguientes.
    factor_resto = (resto_original - bono) / resto_original
    # Devuelve `[probabilidad + bono if indice == indice_favorecido else probabilidad * factor_resto for indice, ...` al código que llamó a esta función.
    return [probabilidad + bono if indice == indice_favorecido else probabilidad * factor_resto for indice, probabilidad in enumerate(probabilidades)]

# Define `determinar_variantes_especiales` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_variantes_especiales(genero, padre, madre):
    """Genera condiciones y poderes del universo ficticio según las variantes parentales."""
    # Crea `mutaciones` para acumular las mutaciones para mostrarlas en la ficha final.
    mutaciones = []
    # Crea `poderes` para acumular los poderes asociados a las variantes detectadas.
    poderes = []
    # Crea `variantes_padres` con los datos u opciones que se procesan después.
    variantes_padres = [padre['variantes'], madre['variantes']]
    # Crea `variantes_presentes` con los datos u opciones que se procesan después.
    variantes_presentes = [variante for datos in variantes_padres for variante in datos['neurovariantes']]
    # Guarda en `tirada_autismo` `True` o `False` según se cumpla la comparación.
    tirada_autismo = random.randint(1, 150) == 35
    # Guarda en `tiene_autismo` el resultado de obtener el resultado de `tirar_con_bono_probabilidad`; se reutiliza en los pasos siguientes.
    tiene_autismo = tirar_con_bono_probabilidad(tirada_autismo, 1 / 150, 0.15 if any(('TEA' in datos['neurovariantes'] for datos in variantes_padres)) else 0)
    # Calcula y guarda en `subtipo_autismo` el valor que se necesita en las instrucciones siguientes.
    subtipo_autismo = None
    # Comprueba `tiene_autismo`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_autismo:
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append('Autismo')
        # Añadir un solo elemento a la lista que se está construyendo.
        poderes.append('Adaptarse')
        # Calcula y guarda en `racha_repeticiones` el valor que se necesita en las instrucciones siguientes.
        racha_repeticiones = 0
        # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
        while True:
            # Guarda en `resultado_d5` el resultado de obtener un entero aleatorio dentro del intervalo, incluidos sus extremos; se reutiliza en los pasos siguientes.
            resultado_d5 = random.randint(1, 5)
            # Comprueba `resultado_d5 in (1, 2, 3)`; solo ejecuta este bloque cuando se cumple la condición.
            if resultado_d5 in (1, 2, 3):
                # Calcula y guarda en `subtipo_autismo` el valor que se necesita en las instrucciones siguientes.
                subtipo_autismo = {1: 'TEA', 2: 'TDA', 3: 'TDH'}[resultado_d5]
                # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
                break
            # Actualiza `racha_repeticiones`: suma el valor actual con `1`.
            racha_repeticiones += 1
            # Comprueba `racha_repeticiones == 6`; solo ejecuta este bloque cuando se cumple la condición.
            if racha_repeticiones == 6:
                # Añadir un solo elemento a la lista que se está construyendo.
                mutaciones.append('Ludopatía')
                # Añadir un solo elemento a la lista que se está construyendo.
                poderes.append('ludopathy')
                # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
                break
        # Guarda en `subtipos_parentales` el resultado de obtener el resultado de `sorted`; se reutiliza en los pasos siguientes.
        subtipos_parentales = sorted(set(variantes_presentes) & {'TEA', 'TDA', 'TDH'})
        # Comprueba `subtipo_autismo and subtipos_parentales`; solo ejecuta este bloque cuando se cumple la condición.
        if subtipo_autismo and subtipos_parentales:
            # Guarda en `subtipo_favorecido` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
            subtipo_favorecido = random.choice(subtipos_parentales)
            # Crea `probabilidades_base` con los datos u opciones que se procesan después.
            probabilidades_base = [1 / 3, 1 / 3, 1 / 3]
            # Guarda en `indice_favorecido` el resultado de obtener el resultado de `['TEA', 'TDA', 'TDH'].index`; se reutiliza en los pasos siguientes.
            indice_favorecido = ['TEA', 'TDA', 'TDH'].index(subtipo_favorecido)
            # Guarda en `probabilidades_ajustadas` el resultado de obtener el resultado de `ajustar_probabilidades`; se reutiliza en los pasos siguientes.
            probabilidades_ajustadas = ajustar_probabilidades(probabilidades_base, indice_favorecido, 0.15)
            # Calcula y guarda en `probabilidad_reasignacion` el valor que se necesita en las instrucciones siguientes.
            probabilidad_reasignacion = (probabilidades_ajustadas[indice_favorecido] - 1 / 3) / (1 - 1 / 3)
            # Comprueba `subtipo_autismo != subtipo_favorecido and random.random() < probabilidad_reasignacion`; solo ejecuta este bloque cuando se cumple la condición.
            if subtipo_autismo != subtipo_favorecido and random.random() < probabilidad_reasignacion:
                # Calcula y guarda en `subtipo_autismo` el valor que se necesita en las instrucciones siguientes.
                subtipo_autismo = subtipo_favorecido
        # Comprueba `subtipo_autismo`; solo ejecuta este bloque cuando se cumple la condición.
        if subtipo_autismo:
            # Añadir un solo elemento a la lista que se está construyendo.
            mutaciones.append(subtipo_autismo)
    # Comprueba `'Ludopatía' not in mutaciones and any((datos['ludopathy'] for datos in variantes_padres)) and (ra...`; solo ejecuta este bloque cuando se cumple la condición.
    if 'Ludopatía' not in mutaciones and any((datos['ludopathy'] for datos in variantes_padres)) and (random.random() < 0.15):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append('Ludopatía')
        # Añadir un solo elemento a la lista que se está construyendo.
        poderes.append('ludopathy')
    # Guarda en `tiene_diabetes_padres` el resultado de obtener el resultado de `any`; se reutiliza en los pasos siguientes.
    tiene_diabetes_padres = any((datos['diabetes'] is not None for datos in variantes_padres))
    # Guarda en `tirada_diabetes` `True` o `False` según se cumpla la comparación.
    tirada_diabetes = random.randint(1, 100) <= 5
    # Guarda en `tiene_diabetes` el resultado de obtener el resultado de `tirar_con_bono_probabilidad`; se reutiliza en los pasos siguientes.
    tiene_diabetes = tirar_con_bono_probabilidad(tirada_diabetes, 0.05, 0.15 if tiene_diabetes_padres else 0)
    # Comprueba `tiene_diabetes`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_diabetes:
        # Crea `tipos_diabetes` con los datos u opciones que se procesan después.
        tipos_diabetes = ['A', 'B', 'Otros tipos']
        # Crea `probabilidades_diabetes` con los datos u opciones que se procesan después.
        probabilidades_diabetes = [0.6, 0.3, 0.1]
        # Guarda en `tipos_parentales` el resultado de obtener el resultado de `sorted`; se reutiliza en los pasos siguientes.
        tipos_parentales = sorted({datos['diabetes'] for datos in variantes_padres if datos['diabetes'] is not None})
        # Calcula y guarda en `tipo_favorecido` el valor que se necesita en las instrucciones siguientes.
        tipo_favorecido = random.choice(tipos_parentales) if tipos_parentales else None
        # Calcula y guarda en `indice_favorecido` el valor que se necesita en las instrucciones siguientes.
        indice_favorecido = tipos_diabetes.index(tipo_favorecido) if tipo_favorecido in tipos_diabetes else None
        # Guarda en `probabilidades_diabetes` el resultado de obtener el resultado de `ajustar_probabilidades`; se reutiliza en los pasos siguientes.
        probabilidades_diabetes = ajustar_probabilidades(probabilidades_diabetes, indice_favorecido, 0.15)
        # Calcula y guarda en `tipo_diabetes` el valor que se necesita en las instrucciones siguientes.
        tipo_diabetes = random.choices(tipos_diabetes, weights=probabilidades_diabetes, k=1)[0]
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append(f'Diabetes tipo {tipo_diabetes}')
        # Añadir un solo elemento a la lista que se está construyendo.
        poderes.append({'A': 'Sugarrush', 'B': 'Sugar power', 'Otros tipos': 'Sugar infinite'}[tipo_diabetes])
    # Calcula y guarda en `tiene_omnisciencia` el resultado lógico de esta condición.
    tiene_omnisciencia = genero == 'M' and random.randint(1, 7 ** 77) == 777
    # Comprueba `tiene_omnisciencia`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_omnisciencia:
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append('Omnisciencia')
        # Añadir un solo elemento a la lista que se está construyendo.
        poderes.append('Omnisciencia')
    # Devuelve `(mutaciones, poderes, tiene_omnisciencia)` al código que llamó a esta función.
    return (mutaciones, poderes, tiene_omnisciencia)

# Define `determinar_dioptrias` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_dioptrias(padre, madre, ojos_hijo):
    """Genera dioptrías y necesidad de gafas para el personaje ficticio."""
    # Comprueba `ojos_hijo == 'Ceguera'`; solo ejecuta este bloque cuando se cumple la condición.
    if ojos_hijo == 'Ceguera':
        # Devuelve `(None, False, 'No aplica (ceguera)')` al código que llamó a esta función.
        return (None, False, 'No aplica (ceguera)')
    # Crea `niveles_parentales` con los datos u opciones que se procesan después.
    niveles_parentales = [datos['variantes']['dioptria'] for datos in (padre, madre) if datos['variantes']['dioptria'] is not None]
    # Calcula y guarda en `probabilidad_gafas` el valor que se necesita en las instrucciones siguientes.
    probabilidad_gafas = 0.78 if niveles_parentales else 0.45
    # Guarda en `necesita_gafas` `True` o `False` según se cumpla la comparación.
    necesita_gafas = random.random() < probabilidad_gafas
    # Comprueba `not necesita_gafas`; solo ejecuta este bloque cuando se cumple la condición.
    if not necesita_gafas:
        # Devuelve `(None, False, 'Sin dioptrías; no necesita gafas')` al código que llamó a esta función.
        return (None, False, 'Sin dioptrías; no necesita gafas')
    # Guarda en `niveles` el resultado de obtener el resultado de `list`; se reutiliza en los pasos siguientes.
    niveles = list(range(1, 11))
    # Crea `pesos` con los datos u opciones que se procesan después.
    pesos = [30 - 3 * indice for indice in range(len(niveles))]
    # Crea `probabilidades` para conservar las probabilidades ajustadas que se usarán en la siguiente elección.
    probabilidades = [peso / sum(pesos) for peso in pesos]
    # Calcula y guarda en `nivel_favorecido` el valor que se necesita en las instrucciones siguientes.
    nivel_favorecido = random.choice(niveles_parentales) if niveles_parentales else None
    # Calcula y guarda en `indice_favorecido` el valor que se necesita en las instrucciones siguientes.
    indice_favorecido = niveles.index(nivel_favorecido) if nivel_favorecido else None
    # Guarda en `probabilidades` el resultado de obtener el resultado de `ajustar_probabilidades`; se reutiliza en los pasos siguientes.
    probabilidades = ajustar_probabilidades(probabilidades, indice_favorecido, 0.12)
    # Calcula y guarda en `dioptria` el valor que se necesita en las instrucciones siguientes.
    dioptria = random.choices(niveles, weights=probabilidades, k=1)[0]
    # Calcula y guarda en `descripcion` el valor que se necesita en las instrucciones siguientes.
    descripcion = 'Casi ciego' if dioptria == 10 else str(dioptria)
    # Devuelve `(dioptria, True, f'{descripcion} dioptrías; necesita gafas')` al código que llamó a esta función.
    return (dioptria, True, f'{descripcion} dioptrías; necesita gafas')

# Define `evaluar_mutaciones` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def evaluar_mutaciones(genero, factor_sindrome, probabilidad_adicional=0.0):
    """Evalúa mutaciones con el bono hereditario y una probabilidad adicional opcional."""
    # Crea `mutaciones_activas` con los datos u opciones que se procesan después.
    mutaciones_activas = []
    # Crea `poderes_mutantes` para acumular poderes ficticios despertados por mutaciones.
    poderes_mutantes = []
    # Reducir el denominador de cada tirada aumenta su probabilidad aproximadamente un 12%.
    # Calcula y guarda en `mult` el valor que se necesita en las instrucciones siguientes.
    mult = 1.12 if factor_sindrome else 1.0
    if not 0 <= probabilidad_adicional <= 1:
        raise ValueError('La probabilidad adicional debe estar entre 0 y 1.')

    def ocurre(denominador):
        if probabilidad_adicional == 0:
            return random.randint(1, int(denominador / mult)) <= 1
        probabilidad_base = 1 / denominador
        return random.random() < min(
            probabilidad_base * mult + probabilidad_adicional, 1.0
        )

    if ocurre(1000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Down (Cromosoma 21 duplicado)')
        # Comprueba `random.randint(1, 20) == 17`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 20) == 17:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Manipulación de materia')
    if genero == 'F' and ocurre(3000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Turner (X único)')
        # Comprueba `random.randint(1, 20) == 12`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 20) == 12:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Las cosas se materializan lejos')
    if genero == 'M' and ocurre(3000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Klinefelter (Más de 1 X)')
        # Comprueba `random.randint(1, 20) == 8`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 20) == 8:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Aumenta los poderes físicos')
        # Calcula y guarda en `num_x` el valor que se necesita en las instrucciones siguientes.
        num_x = 2
        # Repite el bloque mientras se cumpla `random.randint(1, 100) == 18`; la condición controla cuándo termina.
        while random.randint(1, 100) == 18:
            # Actualiza `num_x`: suma el valor actual con `1`.
            num_x += 1
        # Recorre `range(num_x)`; ejecuta el bloque una vez por cada valor asignado a `_`.
        for _ in range(num_x):
            # Comprueba `random.randint(1, 100) == 34`; solo ejecuta este bloque cuando se cumple la condición.
            if random.randint(1, 100) == 34:
                # Añadir un solo elemento a la lista que se está construyendo.
                poderes_mutantes.append('Aumenta los poderes físicos (X Extra)')
    if ocurre(5000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Edwards (Cromosoma 18 duplicado)')
        # Comprueba `random.randint(1, 20) == 1`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 20) == 1:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Viento')
    if ocurre(20000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Patau (Cromosoma 13 duplicado)')
        # Comprueba `random.randint(1, 100) == 29`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 100) == 29:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Mental')
    if ocurre(50000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome del Maullido de Gato (Cromosoma 5 mal)')
        # Comprueba `random.randint(1, 1000) == 238`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 1000) == 238:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Transformación')
    if genero == 'F' and ocurre(1000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome Triple X (3 Cromosomas X)')
        # Comprueba `random.randint(1, 20) == 4`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 20) == 4:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Levitación')
    if ocurre(50000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Wolf-Hirschhorn (Cromosoma 4 mal)')
        # Comprueba `random.randint(1, 666) == 249`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 666) == 249:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Roca')
    # Calcula y guarda en `tiene_pw` el valor que se necesita en las instrucciones siguientes.
    tiene_pw = False
    if ocurre(30000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Prader-Willi (Región Cromosoma 15 mal)')
        # Calcula y guarda en `tiene_pw` el valor que se necesita en las instrucciones siguientes.
        tiene_pw = True
        # Comprueba `random.randint(1, 2048) == 1024`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 2048) == 1024:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Anti Neutrón')
    if not tiene_pw and ocurre(20000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Angelman (Región Cromosoma 15 mal)')
        # Comprueba `random.randint(1, 20) == 10`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 20) == 10:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Anti Protón')
    if ocurre(20000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Síndrome de Williams (Cromosoma 7 mal)')
        # Comprueba `random.randint(1, 240) == 210`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 240) == 210:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Anti Electrón')
    if ocurre(100000000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Nulisomía (Falta de 1 par de cromosomas)')
        # Guarda en `d_pander` el resultado de obtener un entero aleatorio dentro del intervalo, incluidos sus extremos; se reutiliza en los pasos siguientes.
        d_pander = random.randint(1, 100000)
        # Comprueba `d_pander == 93`; solo ejecuta este bloque cuando se cumple la condición.
        if d_pander == 93:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Muerte')
        # Comprueba `d_pander % 2 == 0`; solo ejecuta este bloque cuando se cumple la condición.
        if d_pander % 2 == 0:
            # Añadir un solo elemento a la lista que se está construyendo.
            mutaciones_activas.append('EFECTO CRÍTICO: Muere antes del año')
    if ocurre(100000000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Doble Monosomía (Falta de 2 cromosomas)')
        # Guarda en `d_pander` el resultado de obtener un entero aleatorio dentro del intervalo, incluidos sus extremos; se reutiliza en los pasos siguientes.
        d_pander = random.randint(1, 100000)
        # Comprueba `d_pander == 94`; solo ejecuta este bloque cuando se cumple la condición.
        if d_pander == 94:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Vida')
        # Comprueba `d_pander % 2 != 0`; solo ejecuta este bloque cuando se cumple la condición.
        if d_pander % 2 != 0:
            # Añadir un solo elemento a la lista que se está construyendo.
            mutaciones_activas.append('EFECTO CRÍTICO: Muere antes del año')
    if genero == 'M' and ocurre(4500):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('Intersexual (H+M)')
        # Comprueba `random.randint(1, 9999) == 4938`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 9999) == 4938:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_mutantes.append('Suerte')
    # Comprueba `random.randint(1, 500000) == 1`; solo ejecuta este bloque cuando se cumple la condición.
    if ocurre(500000):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones_activas.append('EFECTO CRÍTICO: Condición de Paralítico')
    # Devuelve `(mutaciones_activas, poderes_mutantes)` al código que llamó a esta función.
    return (mutaciones_activas, poderes_mutantes)

# Define `obtener_nombre_poder` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def obtener_nombre_poder(cromosoma, genero):
    """Traduce el número de cromosoma a su poder ficticio para mostrarlo en pantalla."""
    # Crea `poderes` para acumular los poderes asociados a las variantes detectadas.
    poderes = {1: 'Oxígeno', 2: 'Hidrógeno', 3: 'Nitrógeno', 4: 'Calcio', 5: 'Carbono', 6: 'Clorofila', 7: 'Electrón', 8: 'Metales', 9: 'Líquido', 10: 'Sólido', 11: 'Gaseoso', 12: 'Plasma', 13: 'Psíquico', 14: 'Sodio', 15: 'Protón (Pelo)', 16: 'Neutrón (Piel)', 17: 'Uranio', 18: 'Frío', 19: 'Calor (Ojos)', 20: 'Corporal', 21: 'Materia', 22: 'Anti materia'}
    # Comprueba `cromosoma == 23`; solo ejecuta este bloque cuando se cumple la condición.
    if cromosoma == 23:
        # Devuelve `'Género: Físico (Masc 1)' if genero == 'M' else 'Género: Especial (Fem 0)'` al código que llamó a esta función.
        return 'Género: Físico (Masc 1)' if genero == 'M' else 'Género: Especial (Fem 0)'
    # Devuelve `poderes.get(cromosoma, 'Desconocido')` al código que llamó a esta función.
    return poderes.get(cromosoma, 'Desconocido')

# Define `pedir_grupo_sanguineo` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def pedir_grupo_sanguineo(nombre_progenitor):
    """Solicita un grupo de la lista admitida; upper() permite escribirlo en cualquier caso."""
    # Crea `grupos_validos` con los datos u opciones que se procesan después.
    grupos_validos = {'A': 'A', 'B': 'B', 'O': 'O', 'AB': 'AB', 'DORADA': 'Dorada'}
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `grupo` el resultado de obtener el resultado de `input(f'Grupo sanguíneo de {nombre_pr...`; se reutiliza en los pasos siguientes.
        grupo = input(f'Grupo sanguíneo de {nombre_progenitor} (A, B, O, AB, Dorada): ').strip().upper()
        # Comprueba `grupo in grupos_validos`; solo ejecuta este bloque cuando se cumple la condición.
        if grupo in grupos_validos:
            # Devuelve `grupos_validos[grupo]` al código que llamó a esta función.
            return grupos_validos[grupo]
        # Mostrar el mensaje o resultado en la consola.
        print('Entrada inválida. Introduce A, B, O, AB o Dorada.')

# Define `pedir_factor_rh` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def pedir_factor_rh(nombre_progenitor):
    """Normaliza el factor Rh y conserva 'neutro' como etiqueta legible."""
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `rh` el resultado de obtener el resultado de `input(f'Factor Rh de {nombre_progenit...`; se reutiliza en los pasos siguientes.
        rh = input(f'Factor Rh de {nombre_progenitor} (+, -, neutro): ').strip().lower()
        # Comprueba `rh in {'+', '-', 'neutro'}`; solo ejecuta este bloque cuando se cumple la condición.
        if rh in {'+', '-', 'neutro'}:
            # Devuelve `'Neutro' if rh == 'neutro' else rh` al código que llamó a esta función.
            return 'Neutro' if rh == 'neutro' else rh
        # Mostrar el mensaje o resultado en la consola.
        print('Entrada inválida. Introduce +, - o neutro.')

# Define `determinar_grupo_sanguineo` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_grupo_sanguineo(grupo_padre, grupo_madre):
    """Calcula el grupo ABO posible y la probabilidad excepcional de sangre dorada."""
    # Comprueba `random.randint(1, 100000000) == 1`; solo ejecuta este bloque cuando se cumple la condición.
    if random.randint(1, 100000000) == 1:
        # Devuelve `'Dorada'` al código que llamó a esta función.
        return 'Dorada'
    # Crea `posibilidades` con los datos u opciones que se procesan después.
    posibilidades = {frozenset(('O',)): ('O',), frozenset(('A', 'O')): ('A', 'O'), frozenset(('A',)): ('A', 'O'), frozenset(('B', 'O')): ('B', 'O'), frozenset(('B',)): ('B', 'O'), frozenset(('A', 'B')): ('A', 'B', 'AB', 'O'), frozenset(('AB', 'O')): ('A', 'B'), frozenset(('AB', 'A')): ('A', 'B', 'AB'), frozenset(('AB', 'B')): ('A', 'B', 'AB'), frozenset(('AB',)): ('A', 'B', 'AB')}
    # El tipo dorado no participa en la tabla ABO definida por este simulador,
    # por eso en ese caso se usa la lista general de grupos posibles.
    # Comprueba `'Dorada' in (grupo_padre, grupo_madre)`; solo ejecuta este bloque cuando se cumple la condición.
    if 'Dorada' in (grupo_padre, grupo_madre):
        # Crea `grupos_posibles` con los datos u opciones que se procesan después.
        grupos_posibles = ('A', 'B', 'O', 'AB')
    # Si `'Dorada' in (grupo_padre, grupo_madre)` no se cumple, ejecuta esta alternativa.
    else:
        # Calcula y guarda en `grupos_posibles` el valor que se necesita en las instrucciones siguientes.
        grupos_posibles = posibilidades[frozenset((grupo_padre, grupo_madre))]
    # Devuelve `random.choice(grupos_posibles)` al código que llamó a esta función.
    return random.choice(grupos_posibles)

# Define `determinar_rh_hijo` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_rh_hijo(rh_padre, rh_madre):
    """Combina los valores Rh codificados como 1, 0 y -1 y devuelve su signo."""
    # Crea `valores_rh` con los datos u opciones que se procesan después.
    valores_rh = {'+': 1, 'Neutro': 0, '-': -1}
    # Calcula y guarda en `promedio` el valor que se necesita en las instrucciones siguientes.
    promedio = (valores_rh[rh_padre] + valores_rh[rh_madre]) / 2
    # Comprueba `promedio > 0`; solo ejecuta este bloque cuando se cumple la condición.
    if promedio > 0:
        # Devuelve `'+'` al código que llamó a esta función.
        return '+'
    # Comprueba `promedio < 0`; solo ejecuta este bloque cuando se cumple la condición.
    if promedio < 0:
        # Devuelve `'-'` al código que llamó a esta función.
        return '-'
    # Devuelve `'Neutro'` al código que llamó a esta función.
    return 'Neutro'

# Define `pedir_datos_progenitor` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def pedir_datos_progenitor(nombre_progenitor, genero_progenitor):
    """Recoge y valida los rasgos del progenitor para poder usarlos después en la simulación."""
    # Mostrar el mensaje o resultado en la consola.
    print(f'\n=== CONFIGURACIÓN DE GENES Y RASGOS DEL {nombre_progenitor.upper()} ===')
    # Crea `cromosomas` para recopilar los datos del progenitor antes de devolverlos.
    cromosomas = {}
    # Crea `cromosomas['sangre']` con los datos u opciones que se procesan después.
    cromosomas['sangre'] = {'grupo': pedir_grupo_sanguineo(nombre_progenitor), 'rh': pedir_factor_rh(nombre_progenitor)}
    # Crea `poderes_guia` con los datos u opciones que se procesan después.
    poderes_guia = {1: 'Oxígeno', 2: 'Hidrógeno', 3: 'Nitrógeno', 4: 'Calcio', 5: 'Carbono', 6: 'Clorofila', 7: 'Electrón', 8: 'Metales', 9: 'Líquido', 10: 'Sólido', 11: 'Gaseoso', 12: 'Plasma', 13: 'Psíquico', 14: 'Sodio', 15: 'Protón (Pelo)', 16: 'Neutrón (Piel)', 17: 'Uranio', 18: 'Frío', 19: 'Calor (Ojos)', 20: 'Corporal', 21: 'Materia', 22: 'Anti materia'}
    # Recorre `range(1, 23)`; ejecuta el bloque una vez por cada valor asignado a `i`.
    for i in range(1, 23):
        # Guarda en `nombre_poder` el resultado de obtener el resultado de `poderes_guia.get`; se reutiliza en los pasos siguientes.
        nombre_poder = poderes_guia.get(i, 'Desconocido')
        # Mostrar el mensaje o resultado en la consola.
        print(f'\n--- Configurando Cromosoma {i} (Poder: {nombre_poder}) ---')
        # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
        while True:
            # Guarda en `poder_input` el resultado de obtener el resultado de `input(f'¿Cromosoma {i} ({nombre_poder...`; se reutiliza en los pasos siguientes.
            poder_input = input(f'¿Cromosoma {i} ({nombre_poder}) de {nombre_progenitor} negativo o positivo (0/1)?: ').strip()
            # Comprueba `poder_input in ['0', '1']`; solo ejecuta este bloque cuando se cumple la condición.
            if poder_input in ['0', '1']:
                # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
                break
            # Mostrar el mensaje o resultado en la consola.
            print('Entrada inválida. Introduce solo 0 o 1.')
        # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
        while True:
            # Guarda en `genes_input` el resultado de obtener el resultado de `input(f'¿Cromosoma {i} ({nombre_poder...`; se reutiliza en los pasos siguientes.
            genes_input = input(f'¿Cromosoma {i} ({nombre_poder}) de {nombre_progenitor}? (AB, Ab, aB, ab): ').strip()
            # Comprueba `genes_input in ['AB', 'Ab', 'aB', 'ab']`; solo ejecuta este bloque cuando se cumple la condición.
            if genes_input in ['AB', 'Ab', 'aB', 'ab']:
                # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
                break
            # Mostrar el mensaje o resultado en la consola.
            print('Entrada inválida. Introduce una combinación exacta (AB, Ab, aB o ab).')
        # Crea `cromosomas[i]` con los datos u opciones que se procesan después.
        cromosomas[i] = {'genes': genes_input, 'poder': int(poder_input)}
    # Mostrar el mensaje o resultado en la consola.
    print(f'\n--- HISTORIAL DE SÍNDROMES Y TRASTORNOS DE {nombre_progenitor.upper()} ---')
    # Crea `sindromes_progenitor` con los datos u opciones que se procesan después.
    sindromes_progenitor = []

    # Define `preguntar_sindrome` como una tarea reutilizable; sus parámetros indican los datos que necesita.
    def preguntar_sindrome(nombre_sindrome):
        """Reutiliza la misma entrada binaria para cada pregunta de historial."""
        # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
        while True:
            # Guarda en `resp` el resultado de obtener el resultado de `input(f'¿Tiene {nombre_sindrome}? (0 ...`; se reutiliza en los pasos siguientes.
            resp = input(f'¿Tiene {nombre_sindrome}? (0 = No, 1 = Sí): ').strip()
            # Comprueba `resp in ['0', '1']`; solo ejecuta este bloque cuando se cumple la condición.
            if resp in ['0', '1']:
                # Devuelve `int(resp) == 1` al código que llamó a esta función.
                return int(resp) == 1
            # Mostrar el mensaje o resultado en la consola.
            print('Entrada inválida. Introduce 0 o 1.')
    # Comprueba `preguntar_sindrome('Síndrome de Down')`; solo ejecuta este bloque cuando se cumple la condición.
    if preguntar_sindrome('Síndrome de Down'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Síndrome de Down')
    # Comprueba `preguntar_sindrome('Síndrome de Edwards')`; solo ejecuta este bloque cuando se cumple la condición.
    if preguntar_sindrome('Síndrome de Edwards'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Síndrome de Edwards')
    # Comprueba `preguntar_sindrome('Síndrome de Patau')`; solo ejecuta este bloque cuando se cumple la condición.
    if preguntar_sindrome('Síndrome de Patau'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Síndrome de Patau')
    # Comprueba `preguntar_sindrome('Síndrome del Maullido de Gato (Cri du Chat)')`; solo ejecuta este bloque cuando se cumple la condición.
    if preguntar_sindrome('Síndrome del Maullido de Gato (Cri du Chat)'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Cri du Chat')
    # Comprueba `preguntar_sindrome('Síndrome de Wolf-Hirschhorn')`; solo ejecuta este bloque cuando se cumple la condición.
    if preguntar_sindrome('Síndrome de Wolf-Hirschhorn'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Wolf-Hirschhorn')
    # Comprueba `preguntar_sindrome('Síndrome de Williams')`; solo ejecuta este bloque cuando se cumple la condición.
    if preguntar_sindrome('Síndrome de Williams'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Williams')
    # Guarda en `tiene_pw` el resultado de obtener el resultado de `preguntar_sindrome`; se reutiliza en los pasos siguientes.
    tiene_pw = preguntar_sindrome('Síndrome de Prader-Willi')
    # Comprueba `tiene_pw`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_pw:
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Prader-Willi')
    # Comprueba `preguntar_sindrome('Síndrome de Angelman')`; solo ejecuta este bloque cuando se cumple la condición.
    elif preguntar_sindrome('Síndrome de Angelman'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Angelman')
    # Comprueba `preguntar_sindrome('Nulisomía')`; solo ejecuta este bloque cuando se cumple la condición.
    if preguntar_sindrome('Nulisomía'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Nulisomía')
    # Comprueba `preguntar_sindrome('Doble Monosomía')`; solo ejecuta este bloque cuando se cumple la condición.
    if preguntar_sindrome('Doble Monosomía'):
        # Añadir un solo elemento a la lista que se está construyendo.
        sindromes_progenitor.append('Doble Monosomía')
    # Comprueba `genero_progenitor == 'M'`; solo ejecuta este bloque cuando se cumple la condición.
    if genero_progenitor == 'M':
        # Comprueba `preguntar_sindrome('Síndrome de Klinefelter')`; solo ejecuta este bloque cuando se cumple la condición.
        if preguntar_sindrome('Síndrome de Klinefelter'):
            # Añadir un solo elemento a la lista que se está construyendo.
            sindromes_progenitor.append('Klinefelter')
        # Comprueba `preguntar_sindrome('Condición Intersexual')`; solo ejecuta este bloque cuando se cumple la condición.
        if preguntar_sindrome('Condición Intersexual'):
            # Añadir un solo elemento a la lista que se está construyendo.
            sindromes_progenitor.append('Intersexual')
    # Si `genero_progenitor == 'M'` no se cumple, ejecuta esta alternativa.
    else:
        # Comprueba `preguntar_sindrome('Síndrome de Turner')`; solo ejecuta este bloque cuando se cumple la condición.
        if preguntar_sindrome('Síndrome de Turner'):
            # Añadir un solo elemento a la lista que se está construyendo.
            sindromes_progenitor.append('Turner')
        # Comprueba `preguntar_sindrome('Síndrome Triple X')`; solo ejecuta este bloque cuando se cumple la condición.
        if preguntar_sindrome('Síndrome Triple X'):
            # Añadir un solo elemento a la lista que se está construyendo.
            sindromes_progenitor.append('Triple X')
    # Mostrar el mensaje o resultado en la consola.
    print(f'\n--- VARIANTES ADICIONALES DE {nombre_progenitor.upper()} ---')
    # Crea `neurovariantes` con los datos u opciones que se procesan después.
    neurovariantes = [variante for variante in ('TEA', 'TDA', 'TDH') if preguntar_sindrome(variante)]
    # Guarda en `tiene_ludopathy` el resultado de obtener el resultado de `preguntar_sindrome`; se reutiliza en los pasos siguientes.
    tiene_ludopathy = preguntar_sindrome('ludopathy')
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `diabetes_input` el resultado de obtener el resultado de `input('¿Tiene diabetes? (0 = No, 1 = ...`; se reutiliza en los pasos siguientes.
        diabetes_input = input('¿Tiene diabetes? (0 = No, 1 = Tipo A, 2 = Tipo B, 3 = Otros tipos): ').strip()
        # Comprueba `diabetes_input in ('0', '1', '2', '3')`; solo ejecuta este bloque cuando se cumple la condición.
        if diabetes_input in ('0', '1', '2', '3'):
            # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
            break
        # Mostrar el mensaje o resultado en la consola.
        print('Entrada inválida. Introduce 0, 1, 2 o 3.')
    # Calcula y guarda en `tipo_diabetes` el valor que se necesita en las instrucciones siguientes.
    tipo_diabetes = {'0': None, '1': 'A', '2': 'B', '3': 'Otros tipos'}[diabetes_input]
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `dioptria_input` el resultado de obtener el resultado de `input('Dioptrías del progenitor (0 = ...`; se reutiliza en los pasos siguientes.
        dioptria_input = input('Dioptrías del progenitor (0 = Ninguna, 1-10 = nivel; 10 = casi ciego): ').strip()
        # Comprueba `dioptria_input.isdigit() and 0 <= int(dioptria_input) <= 10`; solo ejecuta este bloque cuando se cumple la condición.
        if dioptria_input.isdigit() and 0 <= int(dioptria_input) <= 10:
            # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
            break
        # Mostrar el mensaje o resultado en la consola.
        print('Entrada inválida. Introduce un número del 0 al 10.')
    # Calcula y guarda en `nivel_dioptria` el resultado lógico de esta condición.
    nivel_dioptria = int(dioptria_input) or None
    # Guarda en `tiene_gafas` el resultado de obtener el resultado de `preguntar_sindrome`; se reutiliza en los pasos siguientes.
    tiene_gafas = preguntar_sindrome('usa gafas')
    # Calcula y guarda en `omnisciencia` el valor que se necesita en las instrucciones siguientes.
    omnisciencia = preguntar_sindrome('omnisciencia') if genero_progenitor == 'M' else False
    # Mostrar el mensaje o resultado en la consola.
    print(f'\n--- Rasgos Físicos del {nombre_progenitor} ---')
    # Crea `colores_pelo_validos` con los datos u opciones que se procesan después.
    colores_pelo_validos = ['Castaño', 'Rubio', 'Negro', 'Blanco', 'Rojo', 'Naranja']
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `pelo` el resultado de obtener el resultado de `input(f"Color de pelo de {nombre_prog...`; se reutiliza en los pasos siguientes.
        pelo = input(f"Color de pelo de {nombre_progenitor} ({', '.join(colores_pelo_validos)}): ").strip().capitalize()
        # Comprueba `pelo in colores_pelo_validos`; solo ejecuta este bloque cuando se cumple la condición.
        if pelo in colores_pelo_validos:
            # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
            break
        # Mostrar el mensaje o resultado en la consola.
        print('Opción inválida. Elige uno de la lista.')
    # Crea `colores_piel_validos` con los datos u opciones que se procesan después.
    colores_piel_validos = ['Blanco', 'Crema', 'Mestizo', 'Marron', 'Oscuro', 'Albino']
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `piel` el resultado de obtener el resultado de `input(f"Color de piel de {nombre_prog...`; se reutiliza en los pasos siguientes.
        piel = input(f"Color de piel de {nombre_progenitor} ({', '.join(colores_piel_validos)}): ").strip().capitalize()
        # Comprueba `piel in colores_piel_validos`; solo ejecuta este bloque cuando se cumple la condición.
        if piel in colores_piel_validos:
            # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
            break
        # Mostrar el mensaje o resultado en la consola.
        print('Opción inválida. Elige uno de la lista.')
    # Crea `colores_ojos_validos` con los datos u opciones que se procesan después.
    colores_ojos_validos = ['Rojo', 'Marron oscuro', 'Miel', 'Azul', 'Verde', 'Pardo', 'Blancos']
    # Repite el bloque mientras se cumpla `True`; la condición controla cuándo termina.
    while True:
        # Guarda en `ojos` el resultado de obtener el resultado de `input(f'Color de ojos de {nombre_prog...`; se reutiliza en los pasos siguientes.
        ojos = input(f'Color de ojos de {nombre_progenitor} (Rojo, Marron oscuro, Miel, Azul, Verde, Pardo, Blancos): ').strip().capitalize()
        # Comprueba `ojos in colores_ojos_validos or ojos in ['Marron oscuro']`; solo ejecuta este bloque cuando se cumple la condición.
        if ojos in colores_ojos_validos or ojos in ['Marron oscuro']:
            # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
            break
        # Mostrar el mensaje o resultado en la consola.
        print('Opción inválida. Elige uno de la lista.')
    # Crea `cromosomas['fenotipo']` con los datos u opciones que se procesan después.
    cromosomas['fenotipo'] = {'pelo': pelo, 'piel': piel, 'ojos': ojos}
    # Calcula y guarda en `cromosomas['sindromes']` el valor que se necesita en las instrucciones siguientes.
    cromosomas['sindromes'] = sindromes_progenitor
    # Crea `cromosomas['variantes']` con los datos u opciones que se procesan después.
    cromosomas['variantes'] = {'neurovariantes': neurovariantes, 'ludopathy': tiene_ludopathy, 'diabetes': tipo_diabetes, 'dioptria': nivel_dioptria, 'gafas': tiene_gafas, 'omnisciencia': omnisciencia}
    # Devuelve `cromosomas` al código que llamó a esta función.
    return cromosomas

# Define `heredar_genoma` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def heredar_genoma(padre, madre, genero):
    """Mezcla alelos con reglas aleatorias simplificadas propias de este simulador."""
    # Calcula y guarda en `progenitor_base` el valor que se necesita en las instrucciones siguientes.
    progenitor_base = 'padre' if genero == 'F' else 'madre'
    # Crea `genoma` para guardar los alelos heredados por cromosoma.
    genoma = {}
    # Crea `origenes` para registrar qué progenitor se marca como origen de cada cromosoma.
    origenes = {}
    # Recorre `range(1, 23)`; ejecuta el bloque una vez por cada valor asignado a `cromosoma`.
    for cromosoma in range(1, 23):
        # Calcula y guarda en `progenitor` el valor que se necesita en las instrucciones siguientes.
        progenitor = progenitor_base
        # La tirada cambia el origen parental registrado con probabilidad 1/10.
        # Comprueba `random.randint(1, 10) == 1`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 10) == 1:
            # Calcula y guarda en `progenitor` el valor que se necesita en las instrucciones siguientes.
            progenitor = 'madre' if progenitor_base == 'padre' else 'padre'
        # Se elige un carácter (alelo) de cada cadena para formar el par heredado.
        # Guarda en `alelo_padre` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        alelo_padre = random.choice(padre[cromosoma]['genes'])
        # Guarda en `alelo_madre` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        alelo_madre = random.choice(madre[cromosoma]['genes'])
        # Guarda en `genes_hijo` el resultado de obtener el resultado de `''.join`; se reutiliza en los pasos siguientes.
        genes_hijo = ''.join(sorted([alelo_padre, alelo_madre], key=str.lower))
        # Calcula y guarda en `genoma[cromosoma]` el valor que se necesita en las instrucciones siguientes.
        genoma[cromosoma] = genes_hijo
        # Calcula y guarda en `origenes[cromosoma]` el valor que se necesita en las instrucciones siguientes.
        origenes[cromosoma] = 'Padre' if progenitor == 'padre' else 'Madre'
    # Calcula y guarda en `genoma[23]` el valor que se necesita en las instrucciones siguientes.
    genoma[23] = padre[23]['genes'] if genero == 'F' else madre[23]['genes']
    # Calcula y guarda en `origenes[23]` el valor que se necesita en las instrucciones siguientes.
    origenes[23] = 'Padre' if genero == 'F' else 'Madre'
    # Devuelve `(genoma, origenes)` al código que llamó a esta función.
    return (genoma, origenes)

# Define `determinar_rasgos_hijo` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_rasgos_hijo(padre, madre):
    """Calcula el pelo (Cr 15), la piel (Cr 16) y los ojos (Cr 19) según las reglas indicadas"""
    # Calcula y guarda en `p_pelo` el valor que se necesita en las instrucciones siguientes.
    p_pelo = padre['fenotipo']['pelo']
    # Calcula y guarda en `m_pelo` el valor que se necesita en las instrucciones siguientes.
    m_pelo = madre['fenotipo']['pelo']
    # Calcula y guarda en `p_piel` el valor que se necesita en las instrucciones siguientes.
    p_piel = padre['fenotipo']['piel']
    # Calcula y guarda en `m_piel` el valor que se necesita en las instrucciones siguientes.
    m_piel = madre['fenotipo']['piel']
    # Calcula y guarda en `p_ojos` el valor que se necesita en las instrucciones siguientes.
    p_ojos = padre['fenotipo']['ojos']
    # Calcula y guarda en `m_ojos` el valor que se necesita en las instrucciones siguientes.
    m_ojos = madre['fenotipo']['ojos']
    # Comprueba `p_piel == 'Albino' and m_piel == 'Albino'`; solo ejecuta este bloque cuando se cumple la condición.
    if p_piel == 'Albino' and m_piel == 'Albino':
        # Guarda en `rand_val` el resultado de obtener un entero aleatorio dentro del intervalo, incluidos sus extremos; se reutiliza en los pasos siguientes.
        rand_val = random.randint(1, 100)
        # Comprueba `rand_val <= 40`; solo ejecuta este bloque cuando se cumple la condición.
        if rand_val <= 40:
            # Guarda en `piel_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
            piel_hijo = random.choice(['Blanco', 'Crema'])
        # Comprueba `rand_val <= 65`; solo ejecuta este bloque cuando se cumple la condición.
        elif rand_val <= 65:
            # Guarda en `piel_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
            piel_hijo = random.choice(['Marron', 'Oscuro'])
        # Comprueba `rand_val <= 75`; solo ejecuta este bloque cuando se cumple la condición.
        elif rand_val <= 75:
            # Calcula y guarda en `piel_hijo` el valor que se necesita en las instrucciones siguientes.
            piel_hijo = 'Albino'
        # Si `rand_val <= 75` no se cumple, ejecuta esta alternativa.
        else:
            # Calcula y guarda en `piel_hijo` el valor que se necesita en las instrucciones siguientes.
            piel_hijo = 'Mestizo'
    # Comprueba `random.randint(1, 100000) == 1`; solo ejecuta este bloque cuando se cumple la condición.
    elif random.randint(1, 100000) == 1:
        # Calcula y guarda en `piel_hijo` el valor que se necesita en las instrucciones siguientes.
        piel_hijo = 'Albino'
    # Comprueba `p_piel != m_piel and random.randint(1, 10) == 1`; solo ejecuta este bloque cuando se cumple la condición.
    elif p_piel != m_piel and random.randint(1, 10) == 1:
        # Calcula y guarda en `piel_hijo` el valor que se necesita en las instrucciones siguientes.
        piel_hijo = 'Mestizo'
    # Si `p_piel != m_piel and random.randint(1, 10) == 1` no se cumple, ejecuta esta alternativa.
    else:
        # Guarda en `piel_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        piel_hijo = random.choice([p_piel, m_piel])
    # Comprueba `piel_hijo == 'Albino'`; solo ejecuta este bloque cuando se cumple la condición.
    if piel_hijo == 'Albino':
        # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
        pelo_hijo = 'Blanco'
        # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
        ojos_hijo = 'Rojo'
        # Devuelve `(pelo_hijo, piel_hijo, ojos_hijo)` al código que llamó a esta función.
        return (pelo_hijo, piel_hijo, ojos_hijo)
    # Comprueba `p_pelo == 'Albino' and m_pelo == 'Albino'`; solo ejecuta este bloque cuando se cumple la condición.
    if p_pelo == 'Albino' and m_pelo == 'Albino':
        # Guarda en `rand_val` el resultado de obtener un entero aleatorio dentro del intervalo, incluidos sus extremos; se reutiliza en los pasos siguientes.
        rand_val = random.randint(1, 100)
        # Comprueba `rand_val <= 25`; solo ejecuta este bloque cuando se cumple la condición.
        if rand_val <= 25:
            # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
            pelo_hijo = 'Castaño'
        # Comprueba `rand_val <= 50`; solo ejecuta este bloque cuando se cumple la condición.
        elif rand_val <= 50:
            # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
            pelo_hijo = 'Rubio'
        # Comprueba `rand_val <= 60`; solo ejecuta este bloque cuando se cumple la condición.
        elif rand_val <= 60:
            # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
            pelo_hijo = 'Albino'
        # Si `rand_val <= 60` no se cumple, ejecuta esta alternativa.
        else:
            # Guarda en `pelo_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
            pelo_hijo = random.choice(['Negro', 'Rojo', 'Naranja'])
    # Comprueba `random.randint(1, 10000) == 1`; solo ejecuta este bloque cuando se cumple la condición.
    elif random.randint(1, 10000) == 1:
        # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
        pelo_hijo = 'Rojo'
    # Comprueba `p_pelo == 'Castaño' and m_pelo == 'Castaño' and (random.randint(1, 5000) <= 1)`; solo ejecuta este bloque cuando se cumple la condición.
    elif p_pelo == 'Castaño' and m_pelo == 'Castaño' and (random.randint(1, 5000) <= 1):
        # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
        pelo_hijo = 'Rubio'
    # Comprueba `p_pelo == 'Rubio' and m_pelo == 'Rubio' and (random.randint(1, 4000) <= 1)`; solo ejecuta este bloque cuando se cumple la condición.
    elif p_pelo == 'Rubio' and m_pelo == 'Rubio' and (random.randint(1, 4000) <= 1):
        # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
        pelo_hijo = 'Castaño'
    # Si `p_pelo == 'Rubio' and m_pelo == 'Rubio' and (random.randint(1, 4000) <= 1)` no se cumple, ejecuta esta alternativa.
    else:
        # Guarda en `pelo_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        pelo_hijo = random.choice([p_pelo, m_pelo])
    # Comprueba `random.randint(1, 100) == 1`; solo ejecuta este bloque cuando se cumple la condición.
    if random.randint(1, 100) == 1:
        # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
        pelo_hijo = 'Naranja'
    # Crea `restringidos` con los datos u opciones que se procesan después.
    restringidos = ['Verde', 'Pardo', 'Azul']
    # Comprueba `p_ojos in restringidos and m_ojos in restringidos`; solo ejecuta este bloque cuando se cumple la condición.
    if p_ojos in restringidos and m_ojos in restringidos:
        # Crea `opciones_disponibles` con los datos u opciones que se procesan después.
        opciones_disponibles = ['Azul', 'Verde', 'Pardo', 'Rojo', 'Blancos']
        # Guarda en `ojos_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        ojos_hijo = random.choice(opciones_disponibles)
    # Comprueba `p_ojos == 'Pardo' and m_ojos == 'Pardo' and (random.randint(1, 5000) <= 1)`; solo ejecuta este bloque cuando se cumple la condición.
    elif p_ojos == 'Pardo' and m_ojos == 'Pardo' and (random.randint(1, 5000) <= 1):
        # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
        ojos_hijo = 'Marron oscuro'
    # Comprueba `p_ojos in ['Marron oscuro', 'Miel'] or m_ojos in ['Marron oscuro', 'Miel']`; solo ejecuta este bloque cuando se cumple la condición.
    elif p_ojos in ['Marron oscuro', 'Miel'] or m_ojos in ['Marron oscuro', 'Miel']:
        # Comprueba `random.randint(1, 100) <= 10`; solo ejecuta este bloque cuando se cumple la condición.
        if random.randint(1, 100) <= 10:
            # Guarda en `r_val` el resultado de obtener el resultado de `random.uniform`; se reutiliza en los pasos siguientes.
            r_val = random.uniform(0, 10)
            # Comprueba `r_val <= 2`; solo ejecuta este bloque cuando se cumple la condición.
            if r_val <= 2:
                # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
                ojos_hijo = 'Azul'
            # Comprueba `r_val <= 5`; solo ejecuta este bloque cuando se cumple la condición.
            elif r_val <= 5:
                # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
                ojos_hijo = 'Verde'
            # Comprueba `r_val <= 8`; solo ejecuta este bloque cuando se cumple la condición.
            elif r_val <= 8:
                # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
                ojos_hijo = 'Pardo'
            # Comprueba `r_val < 9.981`; solo ejecuta este bloque cuando se cumple la condición.
            elif r_val < 9.981:
                # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
                ojos_hijo = 'Rojo'
            # Comprueba `r_val < 10`; solo ejecuta este bloque cuando se cumple la condición.
            elif r_val < 10:
                # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
                ojos_hijo = 'Blancos'
            # Si `r_val < 10` no se cumple, ejecuta esta alternativa.
            else:
                # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
                ojos_hijo = 'Ceguera'
        # Si `random.randint(1, 100) <= 10` no se cumple, ejecuta esta alternativa.
        else:
            # Guarda en `ojos_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
            ojos_hijo = random.choice([p_ojos, m_ojos])
    # Si `p_ojos in ['Marron oscuro', 'Miel'] or m_ojos in ['Marron oscuro', 'Miel']` no se cumple, ejecuta esta alternativa.
    else:
        # Guarda en `ojos_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        ojos_hijo = random.choice([p_ojos, m_ojos])
    # Devuelve `(pelo_hijo, piel_hijo, ojos_hijo)` al código que llamó a esta función.
    return (pelo_hijo, piel_hijo, ojos_hijo)

# Define `determinar_nacimiento` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_nacimiento():
    """Calcula el número de hijos y marca los eventos ficticios de gemelos o siameses."""
    # Guarda en `gemelos_identicos` `True` o `False` según se cumpla la comparación.
    gemelos_identicos = random.randint(1, 2000) in (290, 459)
    # Guarda en `siameses` `True` o `False` según se cumpla la comparación.
    siameses = random.randint(1, 50000) == 19
    # Calcula y guarda en `numero_hijos` el valor que se necesita en las instrucciones siguientes.
    numero_hijos = 2 if gemelos_identicos or siameses else 1
    # Comprueba `gemelos_identicos`; solo ejecuta este bloque cuando se cumple la condición.
    if gemelos_identicos:
        # Recorre `range(3, 10)`; ejecuta el bloque una vez por cada valor asignado a `siguiente_numero`.
        for siguiente_numero in range(3, 10):
            # Comprueba `random.randint(1, 2500) in (6, 9, 2041)`; solo ejecuta este bloque cuando se cumple la condición.
            if random.randint(1, 2500) in (6, 9, 2041):
                # Calcula y guarda en `numero_hijos` el valor que se necesita en las instrucciones siguientes.
                numero_hijos = siguiente_numero
            # Si `random.randint(1, 2500) in (6, 9, 2041)` no se cumple, ejecuta esta alternativa.
            else:
                # Sale del bucle de inmediato porque ya no hace falta seguir probando opciones.
                break
        # Comprueba `numero_hijos == 9 and random.randint(1, 7) == 3`; solo ejecuta este bloque cuando se cumple la condición.
        if numero_hijos == 9 and random.randint(1, 7) == 3:
            # Calcula y guarda en `numero_hijos` el valor que se necesita en las instrucciones siguientes.
            numero_hijos = 10
    # Devuelve `(numero_hijos, gemelos_identicos, siameses)` al código que llamó a esta función.
    return (numero_hijos, gemelos_identicos, siameses)

# Define `determinar_dedos_extra` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_dedos_extra():
    """Realiza una tirada independiente para cada mano y pie."""
    # Crea `extremidades` con los datos u opciones que se procesan después.
    extremidades = ('mano izquierda', 'mano derecha', 'pie izquierdo', 'pie derecho')
    # Devuelve `[extremidad for extremidad in extremidades if random.randint(1, 700) == 1]` al código que llamó a esta función.
    return [extremidad for extremidad in extremidades if random.randint(1, 700) == 1]

# Define `determinar_evento_steven` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_evento_steven():
    """Comprueba el evento excepcional de Steven."""
    # Devuelve `random.randint(1, 4934993) == 1` al código que llamó a esta función.
    return random.randint(1, 4934993) == 1

# Define `determinar_piel_al_reves` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def determinar_piel_al_reves():
    """Genera la mutación extremadamente rara y comprueba su supervivencia."""
    # Comprueba `random.randint(1, 249294992499) != 1`; solo ejecuta este bloque cuando se cumple la condición.
    if random.randint(1, 249294992499) != 1:
        # Devuelve `(False, None, None)` al código que llamó a esta función.
        return (False, None, None)
    # Guarda en `tirada_supervivencia` el resultado de obtener un entero aleatorio dentro del intervalo, incluidos sus extremos; se reutiliza en los pasos siguientes.
    tirada_supervivencia = random.randint(1, 2000000)
    # Guarda en `sobrevive` `True` o `False` según se cumpla la comparación.
    sobrevive = tirada_supervivencia == 18
    # Devuelve `(True, tirada_supervivencia, sobrevive)` al código que llamó a esta función.
    return (True, tirada_supervivencia, sobrevive)

# Define `simular_hijo_interactivo` como una tarea reutilizable; sus parámetros indican los datos que necesita.
def simular_hijo_interactivo():
    """Coordina las preguntas, tiradas aleatorias, cálculo de rasgos y creación del informe."""
    # Mostrar el mensaje o resultado en la consola.
    print('BIENVENIDO AL SIMULADOR GENÉTICO INTERACTIVO ')
    # Primero se determina el calendario y luego los datos geográficos y los nombres.
    # Guarda en `fecha_concepcion` el resultado de obtener el resultado de `pedir_fecha_concepcion`; se reutiliza en los pasos siguientes.
    fecha_concepcion = pedir_fecha_concepcion()
    # Guarda en `mes_gestacion`, `dias_gestacion` el resultado de obtener el resultado de `determinar_gestacion`; se reutiliza en los pasos siguientes.
    mes_gestacion, dias_gestacion = determinar_gestacion()
    # Calcula y guarda en `fecha_nacimiento` el valor que se necesita en las instrucciones siguientes.
    fecha_nacimiento = fecha_concepcion + timedelta(days=dias_gestacion)
    # Guarda en `minuto_nacimiento` el resultado de obtener un entero aleatorio dentro del intervalo, incluidos sus extremos; se reutiliza en los pasos siguientes.
    minuto_nacimiento = random.randint(0, 23 * 60 + 59)
    # Guarda en `hora_nacimiento` el resultado de obtener el resultado de `hora`; se reutiliza en los pasos siguientes.
    hora_nacimiento = hora(minuto_nacimiento // 60, minuto_nacimiento % 60)
    # Guarda en `signo_zodiacal` el resultado de obtener el resultado de `determinar_signo_zodiacal`; se reutiliza en los pasos siguientes.
    signo_zodiacal = determinar_signo_zodiacal(fecha_nacimiento)
    # Guarda en `pais_padre` el resultado de obtener el resultado de `pedir_pais`; se reutiliza en los pasos siguientes.
    pais_padre = pedir_pais('padre')
    # Guarda en `pais_madre` el resultado de obtener el resultado de `pedir_pais`; se reutiliza en los pasos siguientes.
    pais_madre = pedir_pais('madre')
    # Guarda en `nombre_padre` el resultado de obtener el resultado de `pedir_nombre_padre`; se reutiliza en los pasos siguientes.
    nombre_padre = pedir_nombre_padre()
    # Guarda en `apellido_padre` el resultado de obtener el resultado de `pedir_apellido`; se reutiliza en los pasos siguientes.
    apellido_padre = pedir_apellido('padre')
    # Guarda en `apellido_madre` el resultado de obtener el resultado de `pedir_apellido`; se reutiliza en los pasos siguientes.
    apellido_madre = pedir_apellido('madre')
    # Guarda en `pais_hijo` el resultado de obtener el resultado de `determinar_pais_hijo`; se reutiliza en los pasos siguientes.
    pais_hijo = determinar_pais_hijo(pais_padre, pais_madre)
    # Guarda en `localidad_nacimiento` el resultado de obtener el resultado de `determinar_localidad_nacimiento`; se reutiliza en los pasos siguientes.
    localidad_nacimiento = determinar_localidad_nacimiento(pais_hijo)
    # Guarda en `nace_en_atlantis` `True` o `False` según se cumpla la comparación.
    nace_en_atlantis = localidad_nacimiento == 'Atlantis'
    # Calcula y guarda en `nacionalidad_hijo` el valor que se necesita en las instrucciones siguientes.
    nacionalidad_hijo = 'ATL' if nace_en_atlantis else 'TER' if localidad_nacimiento == 'Espacio' else pais_hijo
    # Guarda en `padre_base` el resultado de obtener el resultado de `pedir_datos_progenitor`; se reutiliza en los pasos siguientes.
    padre_base = pedir_datos_progenitor('padre', 'M')
    # Guarda en `madre_base` el resultado de obtener el resultado de `pedir_datos_progenitor`; se reutiliza en los pasos siguientes.
    madre_base = pedir_datos_progenitor('madre', 'F')
    # Los rasgos de ambos progenitores alimentan los cálculos del hijo.
    # Guarda en `grupo_sanguineo_hijo` el resultado de obtener el resultado de `determinar_grupo_sanguineo`; se reutiliza en los pasos siguientes.
    grupo_sanguineo_hijo = determinar_grupo_sanguineo(padre_base['sangre']['grupo'], madre_base['sangre']['grupo'])
    # Guarda en `rh_hijo` el resultado de obtener el resultado de `determinar_rh_hijo`; se reutiliza en los pasos siguientes.
    rh_hijo = determinar_rh_hijo(padre_base['sangre']['rh'], madre_base['sangre']['rh'])
    # Calcula y guarda en `tiene_sindrome_padres` el resultado lógico de esta condición.
    tiene_sindrome_padres = len(padre_base['sindromes']) > 0 or len(madre_base['sindromes']) > 0
    # Guarda en `genero_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
    genero_hijo = random.choice(['M', 'F'])
    # Calcula y guarda en `c23_binario` el valor que se necesita en las instrucciones siguientes.
    c23_binario = 'Masc 1' if genero_hijo == 'M' else 'Fem 0'
    # Guarda en `nombre_personaje`, `pais_origen_nombre`, `tiene_segundo_nombre` el resultado de obtener el resultado de `generar_nombre_hijo`; se reutiliza en los pasos siguientes.
    nombre_personaje, pais_origen_nombre, tiene_segundo_nombre = generar_nombre_hijo(genero_hijo, pais_padre, pais_madre, nombre_padre, apellido_padre, apellido_madre)
    # Guarda en `es_steven` el resultado de obtener el resultado de `determinar_evento_steven`; se reutiliza en los pasos siguientes.
    es_steven = determinar_evento_steven()
    # Comprueba `es_steven`; solo ejecuta este bloque cuando se cumple la condición.
    if es_steven:
        # Calcula y guarda en `nombre_personaje` el valor que se necesita en las instrucciones siguientes.
        nombre_personaje = 'Steven Steven Steven'
    # Guarda en `tiene_piel_al_reves`, `tirada_supervivencia_piel`, `sobrevive_piel_al_reves` el resultado de obtener el resultado de `determinar_piel_al_reves`; se reutiliza en los pasos siguientes.
    tiene_piel_al_reves, tirada_supervivencia_piel, sobrevive_piel_al_reves = determinar_piel_al_reves()
    # Guarda en `numero_hijos`, `gemelos_identicos`, `siameses` el resultado de obtener el resultado de `determinar_nacimiento`; se reutiliza en los pasos siguientes.
    numero_hijos, gemelos_identicos, siameses = determinar_nacimiento()
    # Guarda en `extremidades_con_dedo_extra` el resultado de obtener el resultado de `determinar_dedos_extra`; se reutiliza en los pasos siguientes.
    extremidades_con_dedo_extra = determinar_dedos_extra()
    # Se separan los cromosomas numerados de los datos descriptivos del progenitor.
    # Crea `padre` con los datos u opciones que se procesan después.
    padre = {i: padre_base[i] for i in range(1, 23)}
    # Crea `madre` con los datos u opciones que se procesan después.
    madre = {i: madre_base[i] for i in range(1, 23)}
    # Crea `padre[23]` con los datos u opciones que se procesan después.
    padre[23] = {'genes': 'AB' if genero_hijo == 'M' else 'ab', 'poder': 1 if genero_hijo == 'M' else 0}
    # Crea `madre[23]` con los datos u opciones que se procesan después.
    madre[23] = {'genes': 'AB' if genero_hijo == 'F' else 'ab', 'poder': 0 if genero_hijo == 'M' else 1}
    # Guarda en `madre_tiene_poder_global` el resultado de obtener el resultado de `any`; se reutiliza en los pasos siguientes.
    madre_tiene_poder_global = any((madre[i]['poder'] == 1 for i in range(1, 23)))
    # Guarda en `genoma_hijo`, `origen_genoma` el resultado de obtener el resultado de `heredar_genoma`; se reutiliza en los pasos siguientes.
    genoma_hijo, origen_genoma = heredar_genoma(padre, madre, genero_hijo)
    # Guarda en `pelo_hijo`, `piel_hijo`, `ojos_hijo` el resultado de obtener el resultado de `determinar_rasgos_hijo`; se reutiliza en los pasos siguientes.
    pelo_hijo, piel_hijo, ojos_hijo = determinar_rasgos_hijo(padre_base, madre_base)
    # Comprueba `numero_hijos > 1 and random.randint(1, 100) <= 80`; solo ejecuta este bloque cuando se cumple la condición.
    if numero_hijos > 1 and random.randint(1, 100) <= 80:
        # Guarda en `rasgo_a_cambiar` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
        rasgo_a_cambiar = random.choice(['pelo', 'piel', 'ojos'])
        # Comprueba `rasgo_a_cambiar == 'pelo'`; solo ejecuta este bloque cuando se cumple la condición.
        if rasgo_a_cambiar == 'pelo':
            # Guarda en `pelo_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
            pelo_hijo = random.choice(['Castaño', 'Rubio', 'Negro', 'Blanco', 'Rojo', 'Naranja'])
        # Comprueba `rasgo_a_cambiar == 'piel'`; solo ejecuta este bloque cuando se cumple la condición.
        elif rasgo_a_cambiar == 'piel':
            # Guarda en `piel_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
            piel_hijo = random.choice(['Blanco', 'Crema', 'Mestizo', 'Marron', 'Oscuro', 'Albino'])
        # Si `rasgo_a_cambiar == 'piel'` no se cumple, ejecuta esta alternativa.
        else:
            # Guarda en `ojos_hijo` el resultado de elegir un elemento al azar entre las opciones; se reutiliza en los pasos siguientes.
            ojos_hijo = random.choice(['Rojo', 'Marron oscuro', 'Miel', 'Azul', 'Verde', 'Pardo', 'Blancos'])
    # Calcula y guarda en `tiene_segunda_cabeza_siamesa` el valor que se necesita en las instrucciones siguientes.
    tiene_segunda_cabeza_siamesa = es_steven
    # Comprueba `es_steven`; solo ejecuta este bloque cuando se cumple la condición.
    if es_steven:
        # Calcula y guarda en `pelo_hijo` el valor que se necesita en las instrucciones siguientes.
        pelo_hijo = 'Negro'
        # Calcula y guarda en `piel_hijo` el valor que se necesita en las instrucciones siguientes.
        piel_hijo = 'Negro'
        # Calcula y guarda en `ojos_hijo` el valor que se necesita en las instrucciones siguientes.
        ojos_hijo = 'Blancos'
    # Comprueba `tiene_piel_al_reves`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_piel_al_reves:
        # Calcula y guarda en `piel_hijo` el valor que se necesita en las instrucciones siguientes.
        piel_hijo = 'Al revés'
    # Calcula y guarda en `tiene_pecas` el resultado lógico de esta condición.
    tiene_pecas = pelo_hijo == 'Rojo' and random.random() < 0.33
    # Crea `poderes_naturales` para acumular los poderes heredados que se mostrarán como activos.
    poderes_naturales = []
    # Guarda en `poderes_activos` el resultado de obtener el resultado de `set`; se reutiliza en los pasos siguientes.
    poderes_activos = set()
    # Guarda en `cromosomas_mutados_positivos` el resultado de obtener el resultado de `set`; se reutiliza en los pasos siguientes.
    cromosomas_mutados_positivos = set()
    # El 23 se representa aparte como rasgo sexual; los otros 22 se evalúan con la tabla.
    # Recorre `range(1, 24)`; ejecuta el bloque una vez por cada valor asignado a `i`.
    for i in range(1, 24):
        # Comprueba `i == 23`; solo ejecuta este bloque cuando se cumple la condición.
        if i == 23:
            # Añadir un solo elemento a la lista que se está construyendo.
            poderes_naturales.append(f'Cromosoma 23: {obtener_nombre_poder(23, genero_hijo)}')
        # Si `i == 23` no se cumple, ejecuta esta alternativa.
        else:
            # Guarda en `tiene_poder`, `es_poder_nuevo`, `mutacion_positiva` el resultado de obtener el resultado de `evaluar_poder_cromosomico`; se reutiliza en los pasos siguientes.
            tiene_poder, es_poder_nuevo, mutacion_positiva = evaluar_poder_cromosomico(i, padre, madre, genoma_hijo)
            # Comprueba `mutacion_positiva`; solo ejecuta este bloque cuando se cumple la condición.
            if mutacion_positiva:
                # Incorpora un elemento al conjunto, evitando duplicados.
                # Incorporar un elemento al conjunto sin crear duplicados.
                cromosomas_mutados_positivos.add(i)
            # Comprueba `tiene_poder`; solo ejecuta este bloque cuando se cumple la condición.
            if tiene_poder:
                # Calcula y guarda en `detalle_poder` el valor que se necesita en las instrucciones siguientes.
                detalle_poder = ' (poder nuevo, 3%)' if es_poder_nuevo else ''
                # Añadir un solo elemento a la lista que se está construyendo.
                poderes_naturales.append(f'Cromosoma {i}: {obtener_nombre_poder(i, genero_hijo)}{detalle_poder}')
                # Incorpora un elemento al conjunto, evitando duplicados.
                # Incorporar un elemento al conjunto sin crear duplicados.
                poderes_activos.add(i)
    # Comprueba `nace_en_atlantis`; solo ejecuta este bloque cuando se cumple la condición.
    if nace_en_atlantis:
        # Añadir un solo elemento a la lista que se está construyendo.
        poderes_naturales.append('Poder de nacimiento: POSEIDÓN')
    # Guarda en `mutaciones`, `poderes_mutantes` el resultado de obtener el resultado de `evaluar_mutaciones`; se reutiliza en los pasos siguientes.
    mutaciones, poderes_mutantes = evaluar_mutaciones(genero_hijo, tiene_sindrome_padres)
    # Comprueba `es_steven`; solo ejecuta este bloque cuando se cumple la condición.
    if es_steven:
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append('Evento excepcional de Steven')
        # Añadir un solo elemento a la lista que se está construyendo.
        poderes_mutantes.append('Steven')
    # Comprueba `tiene_piel_al_reves`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_piel_al_reves:
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append('Piel al revés')
    # Guarda en `mutaciones_especiales`, `poderes_especiales`, `tiene_omnisciencia` el resultado de obtener el resultado de `determinar_variantes_especiales`; se reutiliza en los pasos siguientes.
    mutaciones_especiales, poderes_especiales, tiene_omnisciencia = determinar_variantes_especiales(genero_hijo, padre_base, madre_base)
    # Añadir a la lista todos los elementos de la colección indicada.
    mutaciones.extend(mutaciones_especiales)
    # Añadir a la lista todos los elementos de la colección indicada.
    poderes_mutantes.extend(poderes_especiales)
    # Guarda en `tipo_cancer` el resultado de obtener el resultado de `determinar_tipo_cancer`; se reutiliza en los pasos siguientes.
    tipo_cancer = determinar_tipo_cancer(genero_hijo)
    # Comprueba `tipo_cancer`; solo ejecuta este bloque cuando se cumple la condición.
    if tipo_cancer:
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append(tipo_cancer)
    # Guarda en `trastorno_tid`, `poder_tid` el resultado de obtener el resultado de `determinar_tid`; se reutiliza en los pasos siguientes.
    trastorno_tid, poder_tid = determinar_tid()
    # Comprueba `trastorno_tid`; solo ejecuta este bloque cuando se cumple la condición.
    if trastorno_tid:
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append(trastorno_tid)
        # Añadir un solo elemento a la lista que se está construyendo.
        poderes_mutantes.append(poder_tid)
    # Guarda en `_`, `_`, `resumen_vista` el resultado de obtener el resultado de `determinar_dioptrias`; se reutiliza en los pasos siguientes.
    _, _, resumen_vista = determinar_dioptrias(padre_base, madre_base, ojos_hijo)
    # Comprueba `tiene_enfermedad_genetica(mes_gestacion)`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_enfermedad_genetica(mes_gestacion):
        # Añadir un solo elemento a la lista que se está construyendo.
        mutaciones.append('Posible enfermedad genética (probabilidad adicional del 5% por gestación no novemesina)')
    # Guarda en `reconocimientos` el resultado de obtener el resultado de `determinar_reconocimientos`; se reutiliza en los pasos siguientes.
    reconocimientos = determinar_reconocimientos(genero_hijo, fecha_nacimiento, poderes_activos, genoma_hijo, tiene_autismo_y_tea='Autismo' in mutaciones_especiales and 'TEA' in mutaciones_especiales)
    # Comprueba `tiene_omnisciencia`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_omnisciencia:
        # Añadir un solo elemento a la lista que se está construyendo.
        reconocimientos.append('Vegetta GOD: omnisciencia')
    # Se construye una lista de líneas y se une al final para conservar el formato del informe.
    # Crea `texto_guardar` para reunir, en orden, las líneas que formarán el informe.
    texto_guardar = []
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'FICHA GENÉTICA: {nombre_personaje}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"Género obtenido: {('Niña (Femenino)' if genero_hijo == 'F' else 'Niño (Masculino)')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'Configuración Cromosoma 23: {c23_binario}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"Rasgos Físicos del Hijo -> Pelo: {pelo_hijo} | Piel: {piel_hijo} | Ojos: {ojos_hijo} | Pecas: {('Sí' if tiene_pecas else 'No')}")
    # Comprueba `tiene_piel_al_reves`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_piel_al_reves:
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append(f"Evento de piel al revés: dado de 2.000.000 caras = {tirada_supervivencia_piel}; {('sobrevive' if sobrevive_piel_al_reves else 'no sobrevive')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append('Dedos extra: ' + (', '.join(extremidades_con_dedo_extra) if extremidades_con_dedo_extra else 'ninguno'))
    # Comprueba `tiene_segunda_cabeza_siamesa`; solo ejecuta este bloque cuando se cumple la condición.
    if tiene_segunda_cabeza_siamesa:
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append('Rasgo especial: segunda cabeza siamesa')
    # Comprueba `es_steven`; solo ejecuta este bloque cuando se cumple la condición.
    if es_steven:
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append('Evento especial: Steven (probabilidad 1 entre 4.934.993)')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'Vista: {resumen_vista}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"Fecha de concepción: {fecha_concepcion.strftime('%d/%m/%Y')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'Gestación: {mes_gestacion} meses ({dias_gestacion} días)')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"Fecha estimada de nacimiento: {fecha_nacimiento.strftime('%d/%m/%Y')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"Hora de nacimiento: {hora_nacimiento.strftime('%H:%M')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'Signo zodiacal: {signo_zodiacal}')
    # Calcula y guarda en `lugar_nacimiento` el valor que se necesita en las instrucciones siguientes.
    lugar_nacimiento = (
        localidad_nacimiento
        if localidad_nacimiento in {'Atlantis', 'Espacio'}
        else f'{localidad_nacimiento}, {formatear_pais(pais_hijo)}'
    )
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'Lugar de nacimiento: {lugar_nacimiento}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'País del padre: {formatear_pais(pais_padre)}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'País de la madre: {formatear_pais(pais_madre)}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'Nacionalidad del hijo/a: {formatear_pais(nacionalidad_hijo)}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"Origen del nombre: {formatear_pais(pais_origen_nombre)} ({('segundo nombre incluido' if tiene_segundo_nombre else 'sin segundo nombre')})")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'Grupo sanguíneo y Rh: {grupo_sanguineo_hijo} ({rh_hijo})')
    # Crea `nombres_nacimiento` con los datos u opciones que se procesan después.
    nombres_nacimiento = {1: 'hijo/a único/a', 2: 'gemelos', 3: 'trillizos idénticos', 4: 'cuatrillizos idénticos', 5: 'quintillizos idénticos', 6: 'sextillizos idénticos', 7: 'septillizos idénticos', 8: 'octillizos idénticos', 9: 'nonellizos idénticos', 10: 'decillizos idénticos'}
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"Número de hijos: {numero_hijos} ({(nombres_nacimiento[numero_hijos] if numero_hijos in nombres_nacimiento else 'múltiples')})")
    # Comprueba `gemelos_identicos`; solo ejecuta este bloque cuando se cumple la condición.
    if gemelos_identicos:
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append('Nacimiento: gemelos idénticos')
    # Comprueba `siameses`; solo ejecuta este bloque cuando se cumple la condición.
    if siameses:
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append('Nacimiento: siameses')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"¿Algún padre aportó historial de síndromes?: {('Sí (+12% mutación)' if tiene_sindrome_padres else 'No')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"¿La madre tenía poder base activo?: {('Sí' if madre_tiene_poder_global else 'No')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append('\n[DATOS DEL PADRE]')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"  Rasgos: Pelo={padre_base['fenotipo']['pelo']}, Piel={padre_base['fenotipo']['piel']}, Ojos={padre_base['fenotipo']['ojos']}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'  Nombre: {nombre_padre}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'  Apellido: {apellido_padre}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"  Síndromes del Padre: {(', '.join(padre_base['sindromes']) if padre_base['sindromes'] else 'Ninguno')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"  Variantes del Padre: {', '.join(padre_base['variantes']['neurovariantes']) or 'Ninguna'}; ludopathy={('Sí' if padre_base['variantes']['ludopathy'] else 'No')}; diabetes={padre_base['variantes']['diabetes'] or 'No'}; dioptrías={padre_base['variantes']['dioptria'] or 'Ninguna'}; gafas={('Sí' if padre_base['variantes']['gafas'] else 'No')}; omnisciencia={('Sí' if padre_base['variantes']['omnisciencia'] else 'No')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"  Grupo sanguíneo y Rh: {padre_base['sangre']['grupo']} ({padre_base['sangre']['rh']})")
    # Recorre `range(1, 24)`; ejecuta el bloque una vez por cada valor asignado a `i`.
    for i in range(1, 24):
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append(f"  Cr {i:02d}: Genes=[{padre[i]['genes']}] Poder=[{padre[i]['poder']}]")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append('\n[DATOS DE LA MADRE]')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"  Rasgos: Pelo={madre_base['fenotipo']['pelo']}, Piel={madre_base['fenotipo']['piel']}, Ojos={madre_base['fenotipo']['ojos']}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f'  Apellido: {apellido_madre}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"  Síndromes de la Madre: {(', '.join(madre_base['sindromes']) if madre_base['sindromes'] else 'Ninguna')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"  Variantes de la Madre: {', '.join(madre_base['variantes']['neurovariantes']) or 'Ninguna'}; ludopathy={('Sí' if madre_base['variantes']['ludopathy'] else 'No')}; diabetes={madre_base['variantes']['diabetes'] or 'No'}; dioptrías={madre_base['variantes']['dioptria'] or 'Ninguna'}; gafas={('Sí' if madre_base['variantes']['gafas'] else 'No')}")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append(f"  Grupo sanguíneo y Rh: {madre_base['sangre']['grupo']} ({madre_base['sangre']['rh']})")
    # Recorre `range(1, 24)`; ejecuta el bloque una vez por cada valor asignado a `i`.
    for i in range(1, 24):
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append(f"  Cr {i:02d}: Genes=[{madre[i]['genes']}] Poder=[{madre[i]['poder']}]")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append('\n[GENOMA FINAL DEL HIJO (Mezcla de Alelos)]')
    # Recorre `range(1, 24)`; ejecuta el bloque una vez por cada valor asignado a `i`.
    for i in range(1, 24):
        # Calcula y guarda en `detalle_mutacion` el valor que se necesita en las instrucciones siguientes.
        detalle_mutacion = ' (+ por mutación, 6%)' if i in cromosomas_mutados_positivos else ''
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append(f'  Cr {i:02d}: [{genoma_hijo[i]}] (Alelo cruzado, origen primario: {origen_genoma[i]}){detalle_mutacion}')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append('\n[PODERES Y AFINIDADES NATURALES]')
    # Comprueba `poderes_naturales`; solo ejecuta este bloque cuando se cumple la condición.
    if poderes_naturales:
        # Recorre `poderes_naturales`; ejecuta el bloque una vez por cada valor asignado a `poder`.
        for poder in poderes_naturales:
            # Añadir un solo elemento a la lista que se está construyendo.
            texto_guardar.append(f'  - [ACTIVO] {poder}')
    # Si `poderes_naturales` no se cumple, ejecuta esta alternativa.
    else:
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append("  - [NINGUNO] No se cumplieron requisitos binarios o la madre es 'ab'.")
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append('\n[MUTACIONES Y SÍNDROMES]')
    # Comprueba `mutaciones`; solo ejecuta este bloque cuando se cumple la condición.
    if mutaciones:
        # Recorre `mutaciones`; ejecuta el bloque una vez por cada valor asignado a `mut`.
        for mut in mutaciones:
            # Añadir un solo elemento a la lista que se está construyendo.
            texto_guardar.append(f'  - {mut}')
        # Comprueba `poderes_mutantes`; solo ejecuta este bloque cuando se cumple la condición.
        if poderes_mutantes:
            # Añadir un solo elemento a la lista que se está construyendo.
            texto_guardar.append('  - PODERES MUTANTES DESPERTADOS:')
            # Recorre `poderes_mutantes`; ejecuta el bloque una vez por cada valor asignado a `pm`.
            for pm in poderes_mutantes:
                # Añadir un solo elemento a la lista que se está construyendo.
                texto_guardar.append(f'    * [DESPIERTO] {pm}')
    # Si `mutaciones` no se cumple, ejecuta esta alternativa.
    else:
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append('  - Genoma estable sin mutaciones.')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append('__________')
    # Añadir a la lista todos los elementos de la colección indicada.
    texto_guardar.extend(reconocimientos)
    # Comprueba `fecha_nacimiento == date.today()`; solo ejecuta este bloque cuando se cumple la condición.
    if fecha_nacimiento == date.today():
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append('¡Feliz cumpleaños!')
    # Comprueba `tipo_cancer`; solo ejecuta este bloque cuando se cumple la condición.
    if tipo_cancer:
        # Añadir un solo elemento a la lista que se está construyendo.
        texto_guardar.append('tienes cáncer Andy...')
    # Añadir un solo elemento a la lista que se está construyendo.
    texto_guardar.append('')
    # Guarda en `informe` el resultado de obtener el resultado de `'\n'.join`; se reutiliza en los pasos siguientes.
    informe = '\n'.join(texto_guardar)
    # Mostrar el mensaje o resultado en la consola.
    print(informe)
    # Devuelve `informe` al código que llamó a esta función.
    return informe
# Comprueba `__name__ == '__main__'`; solo ejecuta este bloque cuando se cumple la condición.
if __name__ == '__main__':
    # Este bloque solo se ejecuta al lanzar el archivo directamente, no al importarlo.
    # Guarda en `informe_generado` el resultado de obtener el resultado de `simular_hijo_interactivo`; se reutiliza en los pasos siguientes.
    informe_generado = simular_hijo_interactivo()
    # Guarda en `ruta_home` el resultado de obtener el resultado de `os.path.expanduser`; se reutiliza en los pasos siguientes.
    ruta_home = os.path.expanduser('~')
    # Guarda en `ruta_escritorio` el resultado de obtener el resultado de `os.path.join`; se reutiliza en los pasos siguientes.
    ruta_escritorio = os.path.join(ruta_home, 'Desktop', 'personajes_genetica.txt')
    # Protege esta operación para poder atender de forma explícita los errores que puedan ocurrir.
    try:
        # exist_ok permite crear Escritorio si falta; modo 'a' agrega fichas sin borrar las anteriores.
        # Crea la carpeta necesaria antes de guardar el informe.
        # Obtener el resultado de `os.makedirs`.
        os.makedirs(os.path.dirname(ruta_escritorio), exist_ok=True)
        # Abre `ruta_escritorio` como recurso; `with` garantiza que se cierre al terminar el bloque.
        with open(ruta_escritorio, 'a', encoding='utf-8') as f:
            # Calcula el resultado llamando a `f.write`.
            # Escribir el texto generado en el archivo abierto.
            f.write(informe_generado + '\n')
        # Mostrar el mensaje o resultado en la consola.
        print(f'\n-Jugando con la genetica, eh?-')
        # Mostrar el mensaje o resultado en la consola.
        print(f' ¡1 de casi infinitas de combinaciones posibles! \n')
        # Mostrar el mensaje o resultado en la consola.
        print(f'El archivo se ha actualizado correctamente en tu Escritorio.')
        # Mostrar el mensaje o resultado en la consola.
        print(f"Ruta: '{ruta_escritorio}'")
        # Mostrar el mensaje o resultado en la consola.
        print(f'-Sabes que eres un monstruo? Dr. A. Beanies?-\n')
    # Si el bloque protegido provoca `OSError`, ejecuta esta rama para tratar el error explícitamente.
    except OSError as e:
        # Mostrar el mensaje o resultado en la consola.
        print(f'\n Error al guardar el archivo: {e}\n')
# Cabrón, no me copies el código original de ©IzanDragoMorato
