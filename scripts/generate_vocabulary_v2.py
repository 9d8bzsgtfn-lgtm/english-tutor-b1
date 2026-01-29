#!/usr/bin/env python3
"""
GENERADOR DE PODCASTS DE VOCABULARIO V2 - Con repeticiones y español
Incluye explicaciones en castellano y repeticiones para mejorar la fonética

Uso:
    python generate_vocabulary_v2.py monday
    python generate_vocabulary_v2.py --all

Requisitos:
    pip install edge-tts
"""

import asyncio
import argparse
import sys
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("Error: edge_tts no instalado. Ejecuta: pip install edge-tts")
    sys.exit(1)

# Configuración
VOICE_EN = "en-GB-RyanNeural"  # Voz inglesa
VOICE_ES = "es-ES-AlvaroNeural"  # Voz española
RATE = "-10%"  # Más lento para vocabulario
VOLUME = "+0%"

# Directorio base
BASE_DIR = Path(__file__).parent.parent
PODCASTS_DIR = BASE_DIR / "podcasts" / "vocabulary"
PODCASTS_DIR.mkdir(parents=True, exist_ok=True)

# Script mejorado del lunes con repeticiones y español
MONDAY_SCRIPT_V2 = """
Hello and welcome to Monday Vocabulary!

Bienvenido al podcast de vocabulario del lunes.

Today we're learning vocabulary about work and careers.

Hoy vamos a aprender vocabulario sobre trabajo y carreras profesionales.

Listen carefully and repeat each word three times. I will say the word slowly, then at normal speed.

Escucha atentamente y repite cada palabra tres veces. Diré la palabra despacio y luego a velocidad normal.

Let's begin!

Empezamos.

...

Section 1: Job Titles. Sección 1: Títulos de trabajo.

...

Word number 1: Accountant.

Accountant significa contable en español. Es la persona que gestiona las cuentas y finanzas de una empresa.

Listen and repeat three times:

Accountant.

...

Accountant.

...

Accountant.

...

Now faster: Accountant. Accountant.

Example sentence: My sister works as an accountant.

Mi hermana trabaja como contable.

...

Word number 2: Entrepreneur.

Entrepreneur significa emprendedor en español. Es una persona que crea su propio negocio.

Listen and repeat three times:

Entrepreneur.

...

Entrepreneur.

...

Entrepreneur.

...

Now faster: Entrepreneur. Entrepreneur.

Example sentence: He's an entrepreneur who started his own company.

Es un emprendedor que fundó su propia empresa.

...

Word number 3: Freelancer.

Freelancer significa autónomo o trabajador independiente. Es alguien que trabaja por cuenta propia para diferentes clientes.

Listen and repeat three times:

Freelancer.

...

Freelancer.

...

Freelancer.

...

Now faster: Freelancer. Freelancer.

Example sentence: She's a freelancer, so she works from home.

Es autónoma, así que trabaja desde casa.

...

Word number 4: Manager.

Manager significa gerente o director. Es la persona responsable de un equipo o departamento.

Listen and repeat three times:

Manager.

...

Manager.

...

Manager.

...

Now faster: Manager. Manager.

Example sentence: I need to speak to the manager.

Necesito hablar con el gerente.

...

Word number 5: Colleague.

Colleague significa compañero de trabajo. Son las personas con las que trabajas.

Listen and repeat three times:

Colleague.

...

Colleague.

...

Colleague.

...

Now faster: Colleague. Colleague.

Example sentence: My colleagues are very friendly.

Mis compañeros de trabajo son muy amables.

...

Section 2: Work Verbs. Sección 2: Verbos de trabajo.

...

Word number 6: Apply for.

Apply for significa solicitar, como solicitar un empleo.

Listen and repeat three times:

Apply for.

...

Apply for.

...

Apply for.

...

Now faster: Apply for. Apply for.

Example sentence: I'm going to apply for a new job.

Voy a solicitar un nuevo trabajo.

...

Word number 7: Hire.

Hire significa contratar. Es cuando una empresa da trabajo a alguien.

Listen and repeat three times:

Hire.

...

Hire.

...

Hire.

...

Now faster: Hire. Hire.

Example sentence: The company wants to hire five employees.

La empresa quiere contratar a cinco empleados.

...

Word number 8: Resign.

Resign significa dimitir o renunciar voluntariamente a tu trabajo.

Listen and repeat three times:

Resign.

...

Resign.

...

Resign.

...

Now faster: Resign. Resign.

Example sentence: He resigned from his job last month.

Dimitió de su trabajo el mes pasado.

...

Word number 9: Promote.

Promote significa ascender a alguien a un puesto más alto.

Listen and repeat three times:

Promote.

...

Promote.

...

Promote.

...

Now faster: Promote. Promote.

Example sentence: She was promoted to senior manager.

La ascendieron a gerente senior.

...

Word number 10: Retire.

Retire significa jubilarse, dejar de trabajar por edad.

Listen and repeat three times:

Retire.

...

Retire.

...

Retire.

...

Now faster: Retire. Retire.

Example sentence: My father will retire next year.

Mi padre se jubilará el año que viene.

...

Section 3: Workplace Vocabulary. Sección 3: Vocabulario del lugar de trabajo.

...

Word number 11: Salary.

Salary significa salario, el dinero que recibes por tu trabajo cada mes.

Listen and repeat three times:

Salary.

...

Salary.

...

Salary.

...

Now faster: Salary. Salary.

Example sentence: The salary for this job is very good.

El salario para este trabajo es muy bueno.

...

Word number 12: Deadline.

Deadline significa fecha límite, el último día para entregar algo.

Listen and repeat three times:

Deadline.

...

Deadline.

...

Deadline.

...

Now faster: Deadline. Deadline.

Example sentence: The deadline is Friday.

La fecha límite es el viernes.

...

Word number 13: Meeting.

Meeting significa reunión, cuando un grupo de personas se junta para hablar de trabajo.

Listen and repeat three times:

Meeting.

...

Meeting.

...

Meeting.

...

Now faster: Meeting. Meeting.

Example sentence: We have a meeting at ten o'clock.

Tenemos una reunión a las diez.

...

Word number 14: Overtime.

Overtime significa horas extra, trabajar más horas de lo normal.

Listen and repeat three times:

Overtime.

...

Overtime.

...

Overtime.

...

Now faster: Overtime. Overtime.

Example sentence: I worked overtime to finish the project.

Trabajé horas extra para terminar el proyecto.

...

Word number 15: Contract.

Contract significa contrato, el documento legal que firmas con tu empresa.

Listen and repeat three times:

Contract.

...

Contract.

...

Contract.

...

Now faster: Contract. Contract.

Example sentence: I signed a two-year contract.

Firmé un contrato de dos años.

...

Section 4: Useful Expressions. Sección 4: Expresiones útiles.

...

Expression number 16: Work-life balance.

Work-life balance significa equilibrio entre trabajo y vida personal. Es importante para no estresarse.

Listen and repeat three times:

Work-life balance.

...

Work-life balance.

...

Work-life balance.

...

Example sentence: I'm trying to improve my work-life balance.

Estoy intentando mejorar mi equilibrio entre trabajo y vida personal.

...

Expression number 17: Be in charge of.

Be in charge of significa estar a cargo de, ser responsable de algo.

Listen and repeat three times:

Be in charge of.

...

Be in charge of.

...

Be in charge of.

...

Example sentence: She's in charge of the marketing department.

Ella está a cargo del departamento de marketing.

...

Expression number 18: Make a living.

Make a living significa ganarse la vida, ganar dinero para vivir.

Listen and repeat three times:

Make a living.

...

Make a living.

...

Make a living.

...

Example sentence: He makes a living as a designer.

Se gana la vida como diseñador.

...

Expression number 19: Job satisfaction.

Job satisfaction significa satisfacción laboral, estar contento con tu trabajo.

Listen and repeat three times:

Job satisfaction.

...

Job satisfaction.

...

Job satisfaction.

...

Example sentence: Job satisfaction is more important than money.

La satisfacción laboral es más importante que el dinero.

...

Now let's review all the words one more time.

Ahora vamos a repasar todas las palabras una vez más.

...

Job titles: Accountant. Entrepreneur. Freelancer. Manager. Colleague.

Títulos de trabajo: Contable. Emprendedor. Autónomo. Gerente. Compañero de trabajo.

...

Work verbs: Apply for. Hire. Resign. Promote. Retire.

Verbos de trabajo: Solicitar. Contratar. Dimitir. Ascender. Jubilarse.

...

Workplace words: Salary. Deadline. Meeting. Overtime. Contract.

Palabras del trabajo: Salario. Fecha límite. Reunión. Horas extra. Contrato.

...

Expressions: Work-life balance. Be in charge of. Make a living. Job satisfaction.

Expresiones: Equilibrio trabajo-vida. Estar a cargo de. Ganarse la vida. Satisfacción laboral.

...

Excellent work today! Has hecho un trabajo excelente hoy.

Remember to practice these words during the week.

Recuerda practicar estas palabras durante la semana.

See you tomorrow for Tuesday's podcast about Travel.

Nos vemos mañana para el podcast del martes sobre Viajes.

Goodbye! Adiós!
"""


async def generate_bilingual_podcast(day: str, script: str) -> str:
    """Genera un podcast bilingüe."""
    output_file = PODCASTS_DIR / f"{day.lower()}-vocabulary.mp3"

    print(f"Generando podcast bilingüe para {day.capitalize()}...")
    print(f"Voz inglesa: {VOICE_EN}")
    print(f"Velocidad: {RATE}")

    # Usamos la voz inglesa para todo (el TTS maneja bien las frases en español con acento inglés)
    # Para un resultado más profesional se necesitaría mezclar dos voces
    communicate = edge_tts.Communicate(
        text=script.strip(),
        voice=VOICE_EN,
        rate=RATE,
        volume=VOLUME
    )

    await communicate.save(str(output_file))

    print(f"✓ Podcast guardado en: {output_file}")
    return str(output_file)


async def main_generate(day: str):
    """Genera el podcast del día especificado."""
    scripts = {
        "monday": MONDAY_SCRIPT_V2,
    }

    if day.lower() not in scripts:
        print(f"Script V2 no disponible para {day}. Solo está disponible: monday")
        return

    await generate_bilingual_podcast(day, scripts[day.lower()])


def main():
    parser = argparse.ArgumentParser(description="Generador de podcasts V2 con español y repeticiones")
    parser.add_argument("day", nargs="?", type=str, default="monday",
                       help="Día de la semana (por ahora solo monday)")

    args = parser.parse_args()
    asyncio.run(main_generate(args.day))


if __name__ == "__main__":
    main()
