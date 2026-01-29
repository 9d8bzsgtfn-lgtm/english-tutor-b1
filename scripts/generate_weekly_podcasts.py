#!/usr/bin/env python3
"""
GENERADOR SEMANAL DE PODCASTS DE VOCABULARIO
Genera los 7 podcasts de vocabulario con explicaciones en español y repeticiones

Uso:
    python generate_weekly_podcasts.py              # Genera todos
    python generate_weekly_podcasts.py monday       # Genera solo un día
    python generate_weekly_podcasts.py --list       # Lista los días disponibles

Requisitos:
    pip install edge-tts
"""

import asyncio
import argparse
import sys
from pathlib import Path
from datetime import datetime

try:
    import edge_tts
except ImportError:
    print("Error: edge_tts no instalado. Ejecuta: pip install edge-tts")
    sys.exit(1)

# Configuración
VOICE_EN = "en-GB-RyanNeural"
RATE = "-10%"
VOLUME = "+0%"

# Directorio base
BASE_DIR = Path(__file__).parent.parent
PODCASTS_DIR = BASE_DIR / "podcasts" / "vocabulary"
PODCASTS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# SCRIPTS DE VOCABULARIO - FORMATO V2 (Español + Repeticiones)
# ============================================================================

VOCABULARY_SCRIPTS_V2 = {

"monday": """
Hello and welcome to Monday Vocabulary!

Bienvenido al podcast de vocabulario del lunes.

Today we're learning vocabulary about work and careers.

Hoy vamos a aprender vocabulario sobre trabajo y carreras profesionales.

Listen carefully and repeat each word three times.

Escucha atentamente y repite cada palabra tres veces.

Let's begin! Empezamos.

...

Section 1: Job Titles. Sección 1: Títulos de trabajo.

...

Word number 1: Accountant.

Accountant significa contable en español. Es la persona que gestiona las cuentas y finanzas.

Listen and repeat three times:

Accountant. ... Accountant. ... Accountant.

Now faster: Accountant. Accountant.

Example: My sister works as an accountant.

Mi hermana trabaja como contable.

...

Word number 2: Entrepreneur.

Entrepreneur significa emprendedor. Es una persona que crea su propio negocio.

Listen and repeat three times:

Entrepreneur. ... Entrepreneur. ... Entrepreneur.

Now faster: Entrepreneur. Entrepreneur.

Example: He's an entrepreneur who started his own company.

Es un emprendedor que fundó su propia empresa.

...

Word number 3: Freelancer.

Freelancer significa autónomo o trabajador independiente.

Listen and repeat three times:

Freelancer. ... Freelancer. ... Freelancer.

Now faster: Freelancer. Freelancer.

Example: She's a freelancer, so she works from home.

Es autónoma, así que trabaja desde casa.

...

Word number 4: Manager.

Manager significa gerente o director de un equipo.

Listen and repeat three times:

Manager. ... Manager. ... Manager.

Now faster: Manager. Manager.

Example: I need to speak to the manager.

Necesito hablar con el gerente.

...

Word number 5: Colleague.

Colleague significa compañero de trabajo.

Listen and repeat three times:

Colleague. ... Colleague. ... Colleague.

Now faster: Colleague. Colleague.

Example: My colleagues are very friendly.

Mis compañeros de trabajo son muy amables.

...

Section 2: Work Verbs. Sección 2: Verbos de trabajo.

...

Word number 6: Apply for.

Apply for significa solicitar un empleo.

Listen and repeat three times:

Apply for. ... Apply for. ... Apply for.

Now faster: Apply for. Apply for.

Example: I'm going to apply for a new job.

Voy a solicitar un nuevo trabajo.

...

Word number 7: Hire.

Hire significa contratar a alguien.

Listen and repeat three times:

Hire. ... Hire. ... Hire.

Now faster: Hire. Hire.

Example: The company wants to hire five employees.

La empresa quiere contratar a cinco empleados.

...

Word number 8: Resign.

Resign significa dimitir voluntariamente.

Listen and repeat three times:

Resign. ... Resign. ... Resign.

Now faster: Resign. Resign.

Example: He resigned from his job last month.

Dimitió de su trabajo el mes pasado.

...

Word number 9: Promote.

Promote significa ascender a alguien.

Listen and repeat three times:

Promote. ... Promote. ... Promote.

Now faster: Promote. Promote.

Example: She was promoted to senior manager.

La ascendieron a gerente senior.

...

Word number 10: Retire.

Retire significa jubilarse.

Listen and repeat three times:

Retire. ... Retire. ... Retire.

Now faster: Retire. Retire.

Example: My father will retire next year.

Mi padre se jubilará el año que viene.

...

Section 3: Workplace Words. Sección 3: Palabras del trabajo.

...

Word number 11: Salary.

Salary significa salario mensual.

Listen and repeat three times:

Salary. ... Salary. ... Salary.

Now faster: Salary. Salary.

Example: The salary for this job is very good.

El salario para este trabajo es muy bueno.

...

Word number 12: Deadline.

Deadline significa fecha límite de entrega.

Listen and repeat three times:

Deadline. ... Deadline. ... Deadline.

Now faster: Deadline. Deadline.

Example: The deadline is Friday.

La fecha límite es el viernes.

...

Word number 13: Meeting.

Meeting significa reunión de trabajo.

Listen and repeat three times:

Meeting. ... Meeting. ... Meeting.

Now faster: Meeting. Meeting.

Example: We have a meeting at ten o'clock.

Tenemos una reunión a las diez.

...

Word number 14: Overtime.

Overtime significa horas extra.

Listen and repeat three times:

Overtime. ... Overtime. ... Overtime.

Now faster: Overtime. Overtime.

Example: I worked overtime to finish the project.

Trabajé horas extra para terminar el proyecto.

...

Word number 15: Contract.

Contract significa contrato laboral.

Listen and repeat three times:

Contract. ... Contract. ... Contract.

Now faster: Contract. Contract.

Example: I signed a two-year contract.

Firmé un contrato de dos años.

...

Section 4: Expressions. Sección 4: Expresiones.

...

Expression 16: Work-life balance.

Work-life balance significa equilibrio entre trabajo y vida personal.

Listen and repeat three times:

Work-life balance. ... Work-life balance. ... Work-life balance.

Example: I'm trying to improve my work-life balance.

Estoy intentando mejorar mi equilibrio trabajo-vida.

...

Expression 17: Be in charge of.

Be in charge of significa estar a cargo de algo.

Listen and repeat three times:

Be in charge of. ... Be in charge of. ... Be in charge of.

Example: She's in charge of marketing.

Ella está a cargo del marketing.

...

Expression 18: Make a living.

Make a living significa ganarse la vida.

Listen and repeat three times:

Make a living. ... Make a living. ... Make a living.

Example: He makes a living as a designer.

Se gana la vida como diseñador.

...

Final review. Repaso final.

Job titles: Accountant, Entrepreneur, Freelancer, Manager, Colleague.

Work verbs: Apply for, Hire, Resign, Promote, Retire.

Workplace: Salary, Deadline, Meeting, Overtime, Contract.

Expressions: Work-life balance, Be in charge of, Make a living.

...

Excellent work! Has hecho un trabajo excelente.

See you tomorrow! Hasta mañana.
""",

"tuesday": """
Hello and welcome to Tuesday Vocabulary!

Bienvenido al podcast de vocabulario del martes.

Today we're learning vocabulary about travel and tourism.

Hoy vamos a aprender vocabulario sobre viajes y turismo.

Listen and repeat each word three times. Escucha y repite cada palabra tres veces.

Let's begin! Empezamos.

...

Section 1: Types of Holidays. Sección 1: Tipos de vacaciones.

...

Word number 1: Package holiday.

Package holiday significa viaje organizado, con vuelo y hotel incluidos.

Listen and repeat three times:

Package holiday. ... Package holiday. ... Package holiday.

Now faster: Package holiday. Package holiday.

Example: We booked a package holiday to Greece.

Reservamos un viaje organizado a Grecia.

...

Word number 2: Backpacking.

Backpacking significa viajar de mochilero, viajando barato con una mochila.

Listen and repeat three times:

Backpacking. ... Backpacking. ... Backpacking.

Now faster: Backpacking. Backpacking.

Example: I went backpacking around Asia.

Viajé de mochilero por Asia.

...

Word number 3: City break.

City break significa escapada urbana, unas vacaciones cortas en una ciudad.

Listen and repeat three times:

City break. ... City break. ... City break.

Now faster: City break. City break.

Example: We had a lovely city break in Barcelona.

Tuvimos una escapada urbana preciosa en Barcelona.

...

Word number 4: Cruise.

Cruise significa crucero, vacaciones en un barco grande.

Listen and repeat three times:

Cruise. ... Cruise. ... Cruise.

Now faster: Cruise. Cruise.

Example: My parents went on a cruise.

Mis padres fueron de crucero.

...

Word number 5: Road trip.

Road trip significa viaje por carretera.

Listen and repeat three times:

Road trip. ... Road trip. ... Road trip.

Now faster: Road trip. Road trip.

Example: We're planning a road trip along the coast.

Estamos planeando un viaje por carretera por la costa.

...

Section 2: Accommodation. Sección 2: Alojamiento.

...

Word number 6: Bed and breakfast.

Bed and breakfast significa pensión con desayuno incluido.

Listen and repeat three times:

Bed and breakfast. ... Bed and breakfast. ... Bed and breakfast.

Now faster: Bed and breakfast. Bed and breakfast.

Example: We stayed at a lovely bed and breakfast.

Nos alojamos en una pensión encantadora.

...

Word number 7: Hostel.

Hostel significa albergue, alojamiento barato con habitaciones compartidas.

Listen and repeat three times:

Hostel. ... Hostel. ... Hostel.

Now faster: Hostel. Hostel.

Example: Hostels are cheap for young travellers.

Los albergues son baratos para viajeros jóvenes.

...

Word number 8: Self-catering.

Self-catering significa alojamiento con cocina propia.

Listen and repeat three times:

Self-catering. ... Self-catering. ... Self-catering.

Now faster: Self-catering. Self-catering.

Example: We rented a self-catering apartment.

Alquilamos un apartamento con cocina.

...

Word number 9: All-inclusive.

All-inclusive significa todo incluido, con todas las comidas y bebidas.

Listen and repeat three times:

All-inclusive. ... All-inclusive. ... All-inclusive.

Now faster: All-inclusive. All-inclusive.

Example: The all-inclusive resort was fantastic.

El resort todo incluido fue fantástico.

...

Section 3: At the Airport. Sección 3: En el aeropuerto.

...

Word number 10: Boarding pass.

Boarding pass significa tarjeta de embarque.

Listen and repeat three times:

Boarding pass. ... Boarding pass. ... Boarding pass.

Now faster: Boarding pass. Boarding pass.

Example: Please have your boarding pass ready.

Por favor, tenga su tarjeta de embarque preparada.

...

Word number 11: Check in.

Check in significa facturar en el aeropuerto.

Listen and repeat three times:

Check in. ... Check in. ... Check in.

Now faster: Check in. Check in.

Example: You can check in online.

Puedes facturar online.

...

Word number 12: Hand luggage.

Hand luggage significa equipaje de mano.

Listen and repeat three times:

Hand luggage. ... Hand luggage. ... Hand luggage.

Now faster: Hand luggage. Hand luggage.

Example: You can only bring one piece of hand luggage.

Solo puedes llevar un bulto de equipaje de mano.

...

Word number 13: Departure lounge.

Departure lounge significa sala de embarque.

Listen and repeat three times:

Departure lounge. ... Departure lounge. ... Departure lounge.

Now faster: Departure lounge. Departure lounge.

Example: We waited in the departure lounge.

Esperamos en la sala de embarque.

...

Word number 14: Layover.

Layover significa escala, una parada durante el viaje.

Listen and repeat three times:

Layover. ... Layover. ... Layover.

Now faster: Layover. Layover.

Example: We had a four-hour layover in Dubai.

Tuvimos una escala de cuatro horas en Dubai.

...

Section 4: Sightseeing. Sección 4: Turismo.

...

Word number 15: Landmark.

Landmark significa monumento o lugar emblemático.

Listen and repeat three times:

Landmark. ... Landmark. ... Landmark.

Now faster: Landmark. Landmark.

Example: The Eiffel Tower is a famous landmark.

La Torre Eiffel es un monumento famoso.

...

Word number 16: Guided tour.

Guided tour significa visita guiada.

Listen and repeat three times:

Guided tour. ... Guided tour. ... Guided tour.

Now faster: Guided tour. Guided tour.

Example: We took a guided tour of the museum.

Hicimos una visita guiada del museo.

...

Word number 17: Souvenir.

Souvenir significa recuerdo, algo que compras para recordar un lugar.

Listen and repeat three times:

Souvenir. ... Souvenir. ... Souvenir.

Now faster: Souvenir. Souvenir.

Example: I bought souvenirs for my family.

Compré recuerdos para mi familia.

...

Word number 18: Breathtaking.

Breathtaking significa impresionante, que te deja sin aliento.

Listen and repeat three times:

Breathtaking. ... Breathtaking. ... Breathtaking.

Now faster: Breathtaking. Breathtaking.

Example: The view was breathtaking.

La vista era impresionante.

...

Final review. Repaso final.

Holidays: Package holiday, Backpacking, City break, Cruise, Road trip.

Accommodation: Bed and breakfast, Hostel, Self-catering, All-inclusive.

Airport: Boarding pass, Check in, Hand luggage, Departure lounge, Layover.

Sightseeing: Landmark, Guided tour, Souvenir, Breathtaking.

...

Excellent! See you tomorrow! Hasta mañana.
""",

"wednesday": """
Hello and welcome to Wednesday Vocabulary!

Bienvenido al podcast de vocabulario del miércoles.

Today we're learning vocabulary about health and wellbeing.

Hoy vamos a aprender vocabulario sobre salud y bienestar.

Listen and repeat each word three times. Escucha y repite tres veces.

Let's begin! Empezamos.

...

Section 1: Illnesses. Sección 1: Enfermedades.

...

Word number 1: Headache.

Headache significa dolor de cabeza.

Listen and repeat three times:

Headache. ... Headache. ... Headache.

Now faster: Headache. Headache.

Example: I've had a terrible headache all day.

He tenido un dolor de cabeza terrible todo el día.

...

Word number 2: Sore throat.

Sore throat significa dolor de garganta.

Listen and repeat three times:

Sore throat. ... Sore throat. ... Sore throat.

Now faster: Sore throat. Sore throat.

Example: I have a sore throat and can't talk much.

Tengo dolor de garganta y no puedo hablar mucho.

...

Word number 3: Food poisoning.

Food poisoning significa intoxicación alimentaria.

Listen and repeat three times:

Food poisoning. ... Food poisoning. ... Food poisoning.

Now faster: Food poisoning. Food poisoning.

Example: I got food poisoning from the restaurant.

Tuve una intoxicación alimentaria del restaurante.

...

Word number 4: Fever.

Fever significa fiebre.

Listen and repeat three times:

Fever. ... Fever. ... Fever.

Now faster: Fever. Fever.

Example: She has a high fever and needs rest.

Tiene mucha fiebre y necesita descansar.

...

Word number 5: Allergy.

Allergy significa alergia.

Listen and repeat three times:

Allergy. ... Allergy. ... Allergy.

Now faster: Allergy. Allergy.

Example: I have an allergy to peanuts.

Tengo alergia a los cacahuetes.

...

Section 2: At the Doctor's. Sección 2: En el médico.

...

Word number 6: Appointment.

Appointment significa cita médica.

Listen and repeat three times:

Appointment. ... Appointment. ... Appointment.

Now faster: Appointment. Appointment.

Example: I'd like to make an appointment.

Me gustaría pedir una cita.

...

Word number 7: Prescription.

Prescription significa receta médica.

Listen and repeat three times:

Prescription. ... Prescription. ... Prescription.

Now faster: Prescription. Prescription.

Example: The doctor gave me a prescription.

El médico me dio una receta.

...

Word number 8: Symptoms.

Symptoms significa síntomas de una enfermedad.

Listen and repeat three times:

Symptoms. ... Symptoms. ... Symptoms.

Now faster: Symptoms. Symptoms.

Example: What are your main symptoms?

¿Cuáles son tus síntomas principales?

...

Word number 9: Side effects.

Side effects significa efectos secundarios de un medicamento.

Listen and repeat three times:

Side effects. ... Side effects. ... Side effects.

Now faster: Side effects. Side effects.

Example: This medicine may cause side effects.

Este medicamento puede causar efectos secundarios.

...

Section 3: Healthy Habits. Sección 3: Hábitos saludables.

...

Word number 10: Balanced diet.

Balanced diet significa dieta equilibrada.

Listen and repeat three times:

Balanced diet. ... Balanced diet. ... Balanced diet.

Now faster: Balanced diet. Balanced diet.

Example: A balanced diet includes fruits and vegetables.

Una dieta equilibrada incluye frutas y verduras.

...

Word number 11: Work out.

Work out significa hacer ejercicio en el gimnasio.

Listen and repeat three times:

Work out. ... Work out. ... Work out.

Now faster: Work out. Work out.

Example: I work out three times a week.

Hago ejercicio tres veces a la semana.

...

Word number 12: Get enough sleep.

Get enough sleep significa dormir lo suficiente.

Listen and repeat three times:

Get enough sleep. ... Get enough sleep. ... Get enough sleep.

Now faster: Get enough sleep. Get enough sleep.

Example: It's important to get enough sleep.

Es importante dormir lo suficiente.

...

Word number 13: Quit smoking.

Quit smoking significa dejar de fumar.

Listen and repeat three times:

Quit smoking. ... Quit smoking. ... Quit smoking.

Now faster: Quit smoking. Quit smoking.

Example: My resolution is to quit smoking.

Mi propósito es dejar de fumar.

...

Section 4: Mental Health. Sección 4: Salud mental.

...

Word number 14: Anxiety.

Anxiety significa ansiedad.

Listen and repeat three times:

Anxiety. ... Anxiety. ... Anxiety.

Now faster: Anxiety. Anxiety.

Example: She suffers from anxiety before exams.

Sufre ansiedad antes de los exámenes.

...

Word number 15: Wellbeing.

Wellbeing significa bienestar general.

Listen and repeat three times:

Wellbeing. ... Wellbeing. ... Wellbeing.

Now faster: Wellbeing. Wellbeing.

Example: Exercise is good for your wellbeing.

El ejercicio es bueno para tu bienestar.

...

Word number 16: Mindfulness.

Mindfulness significa atención plena, estar presente en el momento.

Listen and repeat three times:

Mindfulness. ... Mindfulness. ... Mindfulness.

Now faster: Mindfulness. Mindfulness.

Example: I practice mindfulness meditation.

Practico meditación de atención plena.

...

Word number 17: Self-care.

Self-care significa autocuidado.

Listen and repeat three times:

Self-care. ... Self-care. ... Self-care.

Now faster: Self-care. Self-care.

Example: Self-care is important for your health.

El autocuidado es importante para tu salud.

...

Final review. Repaso final.

Illnesses: Headache, Sore throat, Food poisoning, Fever, Allergy.

Doctor: Appointment, Prescription, Symptoms, Side effects.

Healthy habits: Balanced diet, Work out, Get enough sleep, Quit smoking.

Mental health: Anxiety, Wellbeing, Mindfulness, Self-care.

...

Excellent! Stay healthy! Mantente sano. See you tomorrow!
""",

"thursday": """
Hello and welcome to Thursday Vocabulary!

Bienvenido al podcast de vocabulario del jueves.

Today we're learning vocabulary about technology.

Hoy vamos a aprender vocabulario sobre tecnología.

Listen and repeat each word three times. Escucha y repite tres veces.

Let's begin! Empezamos.

...

Section 1: Devices. Sección 1: Dispositivos.

...

Word number 1: Smartphone.

Smartphone significa teléfono inteligente.

Listen and repeat three times:

Smartphone. ... Smartphone. ... Smartphone.

Now faster: Smartphone. Smartphone.

Example: I can't live without my smartphone.

No puedo vivir sin mi teléfono inteligente.

...

Word number 2: Laptop.

Laptop significa ordenador portátil.

Listen and repeat three times:

Laptop. ... Laptop. ... Laptop.

Now faster: Laptop. Laptop.

Example: I take my laptop everywhere.

Llevo mi portátil a todas partes.

...

Word number 3: Tablet.

Tablet significa tableta electrónica.

Listen and repeat three times:

Tablet. ... Tablet. ... Tablet.

Now faster: Tablet. Tablet.

Example: I use my tablet for reading.

Uso mi tableta para leer.

...

Word number 4: Charger.

Charger significa cargador de batería.

Listen and repeat three times:

Charger. ... Charger. ... Charger.

Now faster: Charger. Charger.

Example: I forgot my phone charger at home.

Olvidé mi cargador en casa.

...

Word number 5: Headphones.

Headphones significa auriculares.

Listen and repeat three times:

Headphones. ... Headphones. ... Headphones.

Now faster: Headphones. Headphones.

Example: I always wear headphones on the train.

Siempre uso auriculares en el tren.

...

Section 2: Internet. Sección 2: Internet.

...

Word number 6: Browse.

Browse significa navegar por internet.

Listen and repeat three times:

Browse. ... Browse. ... Browse.

Now faster: Browse. Browse.

Example: I spend hours browsing the internet.

Paso horas navegando por internet.

...

Word number 7: Download.

Download significa descargar archivos de internet.

Listen and repeat three times:

Download. ... Download. ... Download.

Now faster: Download. Download.

Example: I need to download the update.

Necesito descargar la actualización.

...

Word number 8: Upload.

Upload significa subir archivos a internet.

Listen and repeat three times:

Upload. ... Upload. ... Upload.

Now faster: Upload. Upload.

Example: I uploaded my photos to the cloud.

Subí mis fotos a la nube.

...

Word number 9: Streaming.

Streaming significa ver contenido en directo por internet.

Listen and repeat three times:

Streaming. ... Streaming. ... Streaming.

Now faster: Streaming. Streaming.

Example: I prefer streaming films at home.

Prefiero ver películas en streaming en casa.

...

Word number 10: Wi-Fi.

Wi-Fi significa conexión inalámbrica a internet.

Listen and repeat three times:

Wi-Fi. ... Wi-Fi. ... Wi-Fi.

Now faster: Wi-Fi. Wi-Fi.

Example: Is there free Wi-Fi here?

¿Hay Wi-Fi gratis aquí?

...

Section 3: Social Media. Sección 3: Redes sociales.

...

Word number 11: Post.

Post significa publicación en redes sociales.

Listen and repeat three times:

Post. ... Post. ... Post.

Now faster: Post. Post.

Example: Did you see her latest post?

¿Viste su última publicación?

...

Word number 12: Follower.

Follower significa seguidor en redes sociales.

Listen and repeat three times:

Follower. ... Follower. ... Follower.

Now faster: Follower. Follower.

Example: She has thousands of followers.

Tiene miles de seguidores.

...

Word number 13: Go viral.

Go viral significa hacerse viral, muy popular rápidamente.

Listen and repeat three times:

Go viral. ... Go viral. ... Go viral.

Now faster: Go viral. Go viral.

Example: His video went viral overnight.

Su vídeo se hizo viral de la noche a la mañana.

...

Word number 14: Notification.

Notification significa notificación de una aplicación.

Listen and repeat three times:

Notification. ... Notification. ... Notification.

Now faster: Notification. Notification.

Example: I turned off my notifications.

Desactivé mis notificaciones.

...

Section 4: Problems. Sección 4: Problemas técnicos.

...

Word number 15: Crash.

Crash significa bloquearse, cuando un programa falla.

Listen and repeat three times:

Crash. ... Crash. ... Crash.

Now faster: Crash. Crash.

Example: My computer crashed and I lost my work.

Mi ordenador se bloqueó y perdí mi trabajo.

...

Word number 16: Bug.

Bug significa error en un programa.

Listen and repeat three times:

Bug. ... Bug. ... Bug.

Now faster: Bug. Bug.

Example: There's a bug in the software.

Hay un error en el software.

...

Word number 17: Backup.

Backup significa copia de seguridad.

Listen and repeat three times:

Backup. ... Backup. ... Backup.

Now faster: Backup. Backup.

Example: Always make a backup of your files.

Siempre haz una copia de seguridad de tus archivos.

...

Word number 18: Password.

Password significa contraseña.

Listen and repeat three times:

Password. ... Password. ... Password.

Now faster: Password. Password.

Example: Use a strong password.

Usa una contraseña segura.

...

Final review. Repaso final.

Devices: Smartphone, Laptop, Tablet, Charger, Headphones.

Internet: Browse, Download, Upload, Streaming, Wi-Fi.

Social media: Post, Follower, Go viral, Notification.

Problems: Crash, Bug, Backup, Password.

...

Excellent! See you tomorrow! Hasta mañana.
""",

"friday": """
Hello and welcome to Friday Vocabulary!

Bienvenido al podcast de vocabulario del viernes.

Today we're learning vocabulary about entertainment.

Hoy vamos a aprender vocabulario sobre entretenimiento.

Listen and repeat each word three times. Escucha y repite tres veces.

Let's begin! Empezamos.

...

Section 1: Films. Sección 1: Películas.

...

Word number 1: Blockbuster.

Blockbuster significa superproducción, película de gran éxito.

Listen and repeat three times:

Blockbuster. ... Blockbuster. ... Blockbuster.

Now faster: Blockbuster. Blockbuster.

Example: The new Marvel film is a blockbuster.

La nueva película de Marvel es una superproducción.

...

Word number 2: Sequel.

Sequel significa secuela, continuación de una película.

Listen and repeat three times:

Sequel. ... Sequel. ... Sequel.

Now faster: Sequel. Sequel.

Example: They're making a sequel to that film.

Están haciendo una secuela de esa película.

...

Word number 3: Plot.

Plot significa trama o argumento de una historia.

Listen and repeat three times:

Plot. ... Plot. ... Plot.

Now faster: Plot. Plot.

Example: The plot was confusing but interesting.

La trama era confusa pero interesante.

...

Word number 4: Subtitles.

Subtitles significa subtítulos.

Listen and repeat three times:

Subtitles. ... Subtitles. ... Subtitles.

Now faster: Subtitles. Subtitles.

Example: I watch films with English subtitles.

Veo películas con subtítulos en inglés.

...

Word number 5: Spoiler.

Spoiler significa spoiler, información que arruina la sorpresa.

Listen and repeat three times:

Spoiler. ... Spoiler. ... Spoiler.

Now faster: Spoiler. Spoiler.

Example: No spoilers please!

¡Sin spoilers por favor!

...

Section 2: TV Shows. Sección 2: Series de televisión.

...

Word number 6: Binge-watch.

Binge-watch significa ver muchos episodios seguidos, maratón de series.

Listen and repeat three times:

Binge-watch. ... Binge-watch. ... Binge-watch.

Now faster: Binge-watch. Binge-watch.

Example: I binge-watched the whole series.

Vi toda la serie de un tirón.

...

Word number 7: Episode.

Episode significa episodio o capítulo.

Listen and repeat three times:

Episode. ... Episode. ... Episode.

Now faster: Episode. Episode.

Example: The latest episode was amazing.

El último episodio fue increíble.

...

Word number 8: Season.

Season significa temporada de una serie.

Listen and repeat three times:

Season. ... Season. ... Season.

Now faster: Season. Season.

Example: The new season starts next month.

La nueva temporada empieza el mes que viene.

...

Word number 9: Documentary.

Documentary significa documental.

Listen and repeat three times:

Documentary. ... Documentary. ... Documentary.

Now faster: Documentary. Documentary.

Example: I watched a fascinating documentary.

Vi un documental fascinante.

...

Section 3: Music. Sección 3: Música.

...

Word number 10: Gig.

Gig significa concierto en lenguaje informal.

Listen and repeat three times:

Gig. ... Gig. ... Gig.

Now faster: Gig. Gig.

Example: We're going to a gig tonight.

Vamos a un concierto esta noche.

...

Word number 11: Lyrics.

Lyrics significa letra de una canción.

Listen and repeat three times:

Lyrics. ... Lyrics. ... Lyrics.

Now faster: Lyrics. Lyrics.

Example: I love the lyrics of this song.

Me encanta la letra de esta canción.

...

Word number 12: Catchy.

Catchy significa pegadizo, fácil de recordar.

Listen and repeat three times:

Catchy. ... Catchy. ... Catchy.

Now faster: Catchy. Catchy.

Example: That song is so catchy.

Esa canción es muy pegadiza.

...

Word number 13: Playlist.

Playlist significa lista de reproducción.

Listen and repeat three times:

Playlist. ... Playlist. ... Playlist.

Now faster: Playlist. Playlist.

Example: I made a playlist for my workout.

Hice una lista de reproducción para entrenar.

...

Section 4: Hobbies. Sección 4: Hobbies.

...

Word number 14: Take up.

Take up significa empezar un nuevo hobby.

Listen and repeat three times:

Take up. ... Take up. ... Take up.

Now faster: Take up. Take up.

Example: I want to take up photography.

Quiero empezar con la fotografía.

...

Word number 15: Pastime.

Pastime significa pasatiempo.

Listen and repeat three times:

Pastime. ... Pastime. ... Pastime.

Now faster: Pastime. Pastime.

Example: Reading is my favourite pastime.

Leer es mi pasatiempo favorito.

...

Word number 16: Relaxing.

Relaxing significa relajante.

Listen and repeat three times:

Relaxing. ... Relaxing. ... Relaxing.

Now faster: Relaxing. Relaxing.

Example: Gardening is very relaxing.

La jardinería es muy relajante.

...

Word number 17: Rewarding.

Rewarding significa gratificante.

Listen and repeat three times:

Rewarding. ... Rewarding. ... Rewarding.

Now faster: Rewarding. Rewarding.

Example: Volunteering is very rewarding.

El voluntariado es muy gratificante.

...

Final review. Repaso final.

Films: Blockbuster, Sequel, Plot, Subtitles, Spoiler.

TV: Binge-watch, Episode, Season, Documentary.

Music: Gig, Lyrics, Catchy, Playlist.

Hobbies: Take up, Pastime, Relaxing, Rewarding.

...

Excellent! Enjoy your weekend! Disfruta el fin de semana.
""",

"saturday": """
Hello and welcome to Saturday Vocabulary!

Bienvenido al podcast de vocabulario del sábado.

Today we're learning vocabulary about food and dining.

Hoy vamos a aprender vocabulario sobre comida y restaurantes.

Listen and repeat each word three times. Escucha y repite tres veces.

Let's begin! Empezamos.

...

Section 1: Cooking Methods. Sección 1: Métodos de cocina.

...

Word number 1: Roast.

Roast significa asar en el horno.

Listen and repeat three times:

Roast. ... Roast. ... Roast.

Now faster: Roast. Roast.

Example: We roast chicken every Sunday.

Asamos pollo todos los domingos.

...

Word number 2: Grill.

Grill significa asar a la parrilla.

Listen and repeat three times:

Grill. ... Grill. ... Grill.

Now faster: Grill. Grill.

Example: I prefer to grill fish.

Prefiero asar el pescado a la parrilla.

...

Word number 3: Steam.

Steam significa cocinar al vapor.

Listen and repeat three times:

Steam. ... Steam. ... Steam.

Now faster: Steam. Steam.

Example: Steaming vegetables is healthy.

Cocinar verduras al vapor es saludable.

...

Word number 4: Stir-fry.

Stir-fry significa saltear en el wok.

Listen and repeat three times:

Stir-fry. ... Stir-fry. ... Stir-fry.

Now faster: Stir-fry. Stir-fry.

Example: I love to stir-fry vegetables.

Me encanta saltear verduras.

...

Word number 5: Simmer.

Simmer significa cocer a fuego lento.

Listen and repeat three times:

Simmer. ... Simmer. ... Simmer.

Now faster: Simmer. Simmer.

Example: Let the sauce simmer for twenty minutes.

Deja la salsa a fuego lento veinte minutos.

...

Section 2: Describing Food. Sección 2: Describir comida.

...

Word number 6: Delicious.

Delicious significa delicioso.

Listen and repeat three times:

Delicious. ... Delicious. ... Delicious.

Now faster: Delicious. Delicious.

Example: This pasta is delicious!

¡Esta pasta está deliciosa!

...

Word number 7: Bland.

Bland significa soso, sin sabor.

Listen and repeat three times:

Bland. ... Bland. ... Bland.

Now faster: Bland. Bland.

Example: The soup was a bit bland.

La sopa estaba un poco sosa.

...

Word number 8: Spicy.

Spicy significa picante.

Listen and repeat three times:

Spicy. ... Spicy. ... Spicy.

Now faster: Spicy. Spicy.

Example: I love spicy food.

Me encanta la comida picante.

...

Word number 9: Crispy.

Crispy significa crujiente.

Listen and repeat three times:

Crispy. ... Crispy. ... Crispy.

Now faster: Crispy. Crispy.

Example: I like my bacon crispy.

Me gusta el bacon crujiente.

...

Word number 10: Tender.

Tender significa tierno, suave.

Listen and repeat three times:

Tender. ... Tender. ... Tender.

Now faster: Tender. Tender.

Example: The meat was very tender.

La carne estaba muy tierna.

...

Section 3: At the Restaurant. Sección 3: En el restaurante.

...

Word number 11: Reservation.

Reservation significa reserva de mesa.

Listen and repeat three times:

Reservation. ... Reservation. ... Reservation.

Now faster: Reservation. Reservation.

Example: I'd like to make a reservation.

Me gustaría hacer una reserva.

...

Word number 12: Starter.

Starter significa entrante, primer plato.

Listen and repeat three times:

Starter. ... Starter. ... Starter.

Now faster: Starter. Starter.

Example: Would you like a starter?

¿Le gustaría un entrante?

...

Word number 13: Main course.

Main course significa plato principal.

Listen and repeat three times:

Main course. ... Main course. ... Main course.

Now faster: Main course. Main course.

Example: For the main course, I'll have steak.

De plato principal, quiero filete.

...

Word number 14: Side dish.

Side dish significa acompañamiento.

Listen and repeat three times:

Side dish. ... Side dish. ... Side dish.

Now faster: Side dish. Side dish.

Example: What side dishes do you have?

¿Qué acompañamientos tienen?

...

Word number 15: Bill.

Bill significa la cuenta del restaurante.

Listen and repeat three times:

Bill. ... Bill. ... Bill.

Now faster: Bill. Bill.

Example: Could we have the bill please?

¿Nos trae la cuenta por favor?

...

Section 4: Diets. Sección 4: Dietas.

...

Word number 16: Vegetarian.

Vegetarian significa vegetariano.

Listen and repeat three times:

Vegetarian. ... Vegetarian. ... Vegetarian.

Now faster: Vegetarian. Vegetarian.

Example: I've been vegetarian for five years.

Soy vegetariano desde hace cinco años.

...

Word number 17: Vegan.

Vegan significa vegano, sin productos animales.

Listen and repeat three times:

Vegan. ... Vegan. ... Vegan.

Now faster: Vegan. Vegan.

Example: Do you have vegan options?

¿Tienen opciones veganas?

...

Word number 18: Gluten-free.

Gluten-free significa sin gluten.

Listen and repeat three times:

Gluten-free. ... Gluten-free. ... Gluten-free.

Now faster: Gluten-free. Gluten-free.

Example: I need gluten-free food.

Necesito comida sin gluten.

...

Final review. Repaso final.

Cooking: Roast, Grill, Steam, Stir-fry, Simmer.

Describing: Delicious, Bland, Spicy, Crispy, Tender.

Restaurant: Reservation, Starter, Main course, Side dish, Bill.

Diets: Vegetarian, Vegan, Gluten-free.

...

Excellent! Bon appétit! Buen provecho. See you tomorrow!
""",

"sunday": """
Hello and welcome to Sunday Vocabulary!

Bienvenido al podcast de vocabulario del domingo.

Today we're learning vocabulary about environment and nature.

Hoy vamos a aprender vocabulario sobre medio ambiente y naturaleza.

Listen and repeat each word three times. Escucha y repite tres veces.

Let's begin! Empezamos.

...

Section 1: Environmental Problems. Sección 1: Problemas ambientales.

...

Word number 1: Climate change.

Climate change significa cambio climático.

Listen and repeat three times:

Climate change. ... Climate change. ... Climate change.

Now faster: Climate change. Climate change.

Example: Climate change is a serious problem.

El cambio climático es un problema serio.

...

Word number 2: Global warming.

Global warming significa calentamiento global.

Listen and repeat three times:

Global warming. ... Global warming. ... Global warming.

Now faster: Global warming. Global warming.

Example: Global warming is melting the ice.

El calentamiento global está derritiendo el hielo.

...

Word number 3: Pollution.

Pollution significa contaminación.

Listen and repeat three times:

Pollution. ... Pollution. ... Pollution.

Now faster: Pollution. Pollution.

Example: Air pollution is a big problem in cities.

La contaminación del aire es un gran problema en las ciudades.

...

Word number 4: Deforestation.

Deforestation significa deforestación, talar bosques.

Listen and repeat three times:

Deforestation. ... Deforestation. ... Deforestation.

Now faster: Deforestation. Deforestation.

Example: Deforestation is destroying the Amazon.

La deforestación está destruyendo el Amazonas.

...

Word number 5: Endangered species.

Endangered species significa especies en peligro de extinción.

Listen and repeat three times:

Endangered species. ... Endangered species. ... Endangered species.

Now faster: Endangered species. Endangered species.

Example: We must protect endangered species.

Debemos proteger las especies en peligro.

...

Section 2: Solutions. Sección 2: Soluciones.

...

Word number 6: Recycle.

Recycle significa reciclar.

Listen and repeat three times:

Recycle. ... Recycle. ... Recycle.

Now faster: Recycle. Recycle.

Example: We recycle paper, plastic, and glass.

Reciclamos papel, plástico y vidrio.

...

Word number 7: Renewable energy.

Renewable energy significa energía renovable.

Listen and repeat three times:

Renewable energy. ... Renewable energy. ... Renewable energy.

Now faster: Renewable energy. Renewable energy.

Example: Solar power is renewable energy.

La energía solar es renovable.

...

Word number 8: Sustainable.

Sustainable significa sostenible.

Listen and repeat three times:

Sustainable. ... Sustainable. ... Sustainable.

Now faster: Sustainable. Sustainable.

Example: We need sustainable solutions.

Necesitamos soluciones sostenibles.

...

Word number 9: Carbon footprint.

Carbon footprint significa huella de carbono.

Listen and repeat three times:

Carbon footprint. ... Carbon footprint. ... Carbon footprint.

Now faster: Carbon footprint. Carbon footprint.

Example: I'm trying to reduce my carbon footprint.

Estoy intentando reducir mi huella de carbono.

...

Word number 10: Eco-friendly.

Eco-friendly significa ecológico, respetuoso con el medio ambiente.

Listen and repeat three times:

Eco-friendly. ... Eco-friendly. ... Eco-friendly.

Now faster: Eco-friendly. Eco-friendly.

Example: I buy eco-friendly products.

Compro productos ecológicos.

...

Section 3: Nature. Sección 3: Naturaleza.

...

Word number 11: Wildlife.

Wildlife significa fauna salvaje.

Listen and repeat three times:

Wildlife. ... Wildlife. ... Wildlife.

Now faster: Wildlife. Wildlife.

Example: The park has amazing wildlife.

El parque tiene una fauna increíble.

...

Word number 12: Habitat.

Habitat significa hábitat, el hogar natural de los animales.

Listen and repeat three times:

Habitat. ... Habitat. ... Habitat.

Now faster: Habitat. Habitat.

Example: Animals lose their habitat.

Los animales pierden su hábitat.

...

Word number 13: Ecosystem.

Ecosystem significa ecosistema.

Listen and repeat three times:

Ecosystem. ... Ecosystem. ... Ecosystem.

Now faster: Ecosystem. Ecosystem.

Example: Coral reefs are delicate ecosystems.

Los arrecifes de coral son ecosistemas delicados.

...

Word number 14: Biodiversity.

Biodiversity significa biodiversidad.

Listen and repeat three times:

Biodiversity. ... Biodiversity. ... Biodiversity.

Now faster: Biodiversity. Biodiversity.

Example: The rainforest has incredible biodiversity.

La selva tiene una biodiversidad increíble.

...

Section 4: Actions. Sección 4: Acciones.

...

Word number 15: Reduce.

Reduce significa reducir el consumo.

Listen and repeat three times:

Reduce. ... Reduce. ... Reduce.

Now faster: Reduce. Reduce.

Example: We should reduce plastic use.

Deberíamos reducir el uso de plástico.

...

Word number 16: Reuse.

Reuse significa reutilizar.

Listen and repeat three times:

Reuse. ... Reuse. ... Reuse.

Now faster: Reuse. Reuse.

Example: I reuse shopping bags.

Reutilizo las bolsas de la compra.

...

Word number 17: Raise awareness.

Raise awareness significa concienciar, crear conciencia.

Listen and repeat three times:

Raise awareness. ... Raise awareness. ... Raise awareness.

Now faster: Raise awareness. Raise awareness.

Example: We need to raise awareness about climate change.

Necesitamos concienciar sobre el cambio climático.

...

Word number 18: Make a difference.

Make a difference significa marcar la diferencia.

Listen and repeat three times:

Make a difference. ... Make a difference. ... Make a difference.

Now faster: Make a difference. Make a difference.

Example: Every action can make a difference.

Cada acción puede marcar la diferencia.

...

Final review. Repaso final.

Problems: Climate change, Global warming, Pollution, Deforestation, Endangered species.

Solutions: Recycle, Renewable energy, Sustainable, Carbon footprint, Eco-friendly.

Nature: Wildlife, Habitat, Ecosystem, Biodiversity.

Actions: Reduce, Reuse, Raise awareness, Make a difference.

...

Congratulations! You've completed the weekly vocabulary!

¡Felicidades! Has completado el vocabulario semanal.

Start again on Monday! Empieza de nuevo el lunes.

Goodbye! Adiós!
""",
}


async def generate_podcast(day: str) -> str:
    """Genera un podcast para un día específico."""
    day_lower = day.lower()
    script = VOCABULARY_SCRIPTS_V2.get(day_lower)

    if script is None:
        print(f"Error: No hay script para '{day}'")
        print(f"Días disponibles: {', '.join(VOCABULARY_SCRIPTS_V2.keys())}")
        return None

    output_file = PODCASTS_DIR / f"{day_lower}-vocabulary.mp3"

    print(f"Generando podcast para {day.capitalize()}...")
    print(f"Voz: {VOICE_EN}")
    print(f"Velocidad: {RATE}")

    communicate = edge_tts.Communicate(
        text=script.strip(),
        voice=VOICE_EN,
        rate=RATE,
        volume=VOLUME
    )

    await communicate.save(str(output_file))

    print(f"✓ Guardado en: {output_file}")
    return str(output_file)


async def generate_all_podcasts():
    """Genera todos los podcasts de la semana."""
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    print(f"=== Generando podcasts de vocabulario semanal ===")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    for day in days:
        await generate_podcast(day)
        print()

    print("=== ¡Todos los podcasts generados! ===")


def main():
    parser = argparse.ArgumentParser(
        description="Genera podcasts de vocabulario con español y repeticiones"
    )
    parser.add_argument(
        "day",
        nargs="?",
        type=str,
        help="Día de la semana (monday-sunday) o --all para todos"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Genera todos los podcasts de la semana"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Lista los días disponibles"
    )

    args = parser.parse_args()

    if args.list:
        print("Días disponibles:")
        for day in VOCABULARY_SCRIPTS_V2.keys():
            print(f"  - {day}")
        return

    if args.all:
        asyncio.run(generate_all_podcasts())
        return

    if args.day is None:
        parser.print_help()
        print("\nEjemplos:")
        print("  python generate_weekly_podcasts.py monday")
        print("  python generate_weekly_podcasts.py --all")
        return

    asyncio.run(generate_podcast(args.day))


if __name__ == "__main__":
    main()
