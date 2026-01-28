#!/usr/bin/env python3
"""
GENERADOR DE PODCASTS - English Tutor B1
Genera podcasts con explicaciones de cada lección usando edge_tts (gratis)

Uso:
    python generate_podcast.py 1  # Genera podcast de la lección 1

Requisitos:
    pip install edge-tts pydub

Opcional (para música de fondo):
    - Colocar archivo MP3 en: music/background.mp3
"""

import asyncio
import argparse
import os
import sys
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("Error: edge_tts no instalado. Ejecuta: pip install edge-tts")
    sys.exit(1)

# Configuración
VOICE = "en-GB-RyanNeural"  # Voz británica masculina clara
RATE = "-5%"  # Ligeramente más lento
VOLUME = "+0%"

# Directorio base
BASE_DIR = Path(__file__).parent.parent
PODCASTS_DIR = BASE_DIR / "podcasts"
PODCASTS_DIR.mkdir(exist_ok=True)

# Contenido de los podcasts por lección
PODCAST_SCRIPTS = {
    1: """
Welcome to English Tutor B1, Lesson 1: Present Tenses.

In this podcast, we'll learn the difference between Present Simple and Present Continuous.

Let's start with the most important rule.

Present Simple is for routines, habits, and permanent situations.
For example: "I work from home." This means it's my regular job, my routine.

Present Continuous is for actions happening now, or temporary situations.
For example: "I'm working from home this week." This means only this week, it's temporary.

Here's a simple trick to remember:
Simple equals Always or Usually. Think of the letter S for Simple and S for "Siempre" in Spanish.
Continuous equals Currently or Now. Think of C for Continuous and C for Currently.

Now, let's talk about the structure.

For Present Simple:
With I, you, we, they, use the base verb: "I work, you work, we work, they work."
With he, she, it, add S: "He works, she works, it works."

For Present Continuous:
Always use the verb TO BE plus the verb with ING.
"I am working. You are working. He is working."

Time expressions are very important. They help you choose the right tense.

For Present Simple, look for words like:
always, usually, often, sometimes, never
every day, every week, on Mondays, at weekends

For Present Continuous, look for words like:
now, right now, at the moment, currently, today, this week

Now, here's something very important: Stative Verbs.

Some verbs describe states, not actions. These verbs do NOT use the ING form.

Common stative verbs are:
Like, love, hate, want, need.
Know, believe, understand, remember.
See, hear, smell, taste.
Have, own, belong.

For example:
WRONG: "I'm liking this book."
CORRECT: "I like this book."

WRONG: "I'm knowing the answer."
CORRECT: "I know the answer."

Let's practice with some examples.

Example 1: "She works at a bank."
This is Present Simple because it's her permanent job.

Example 2: "She's working at a bank this summer."
This is Present Continuous because it's temporary, just this summer.

Example 3: "I drink coffee every morning."
This is Present Simple. Every morning means routine.

Example 4: "I'm drinking coffee right now."
This is Present Continuous. Right now means happening at this moment.

Now, let's review common mistakes.

Mistake 1: Forgetting the S in third person.
WRONG: "He work every day."
CORRECT: "He works every day."

Mistake 2: Forgetting TO BE in continuous.
WRONG: "I working now."
CORRECT: "I'm working now."

Mistake 3: Using ING with stative verbs.
WRONG: "I'm understanding you."
CORRECT: "I understand you."

Let's summarize what you need to remember:

First: Present Simple is for routines and permanent situations.
Second: Present Continuous is for now and temporary situations.
Third: Look for time expressions to help you choose.
Fourth: Stative verbs like, know, want, need do NOT use ING.
Fifth: Don't forget the S for he, she, it in Present Simple.

That's the end of Lesson 1.

Practice by describing your daily routine using Present Simple.
Then describe what you are doing right now using Present Continuous.

Good luck with your studies!
""",
}


async def generate_podcast(lesson_id: int, script: str = None) -> str:
    """Genera un podcast para una lección."""

    if script is None:
        script = PODCAST_SCRIPTS.get(lesson_id)
        if script is None:
            print(f"No hay script para la lección {lesson_id}")
            return None

    output_file = PODCASTS_DIR / f"lesson-{lesson_id}.mp3"

    print(f"Generando podcast para lección {lesson_id}...")
    print(f"Voz: {VOICE}")
    print(f"Velocidad: {RATE}")

    # Generar audio
    communicate = edge_tts.Communicate(
        text=script.strip(),
        voice=VOICE,
        rate=RATE,
        volume=VOLUME
    )

    await communicate.save(str(output_file))

    print(f"Podcast guardado en: {output_file}")
    return str(output_file)


async def list_voices():
    """Lista las voces disponibles en inglés."""
    voices = await edge_tts.list_voices()
    english_voices = [v for v in voices if v["Locale"].startswith("en-")]

    print("\nVoces disponibles en inglés:\n")
    for voice in english_voices:
        print(f"  {voice['ShortName']}: {voice['Gender']} - {voice['Locale']}")


def main():
    global VOICE

    parser = argparse.ArgumentParser(description="Generador de podcasts para English Tutor B1")
    parser.add_argument("lesson", nargs="?", type=int, help="Número de lección (1-12)")
    parser.add_argument("--list-voices", action="store_true", help="Lista las voces disponibles")
    parser.add_argument("--voice", type=str, default=VOICE, help=f"Voz a usar (default: {VOICE})")

    args = parser.parse_args()

    if args.list_voices:
        asyncio.run(list_voices())
        return

    if args.lesson is None:
        parser.print_help()
        print("\nEjemplo: python generate_podcast.py 1")
        return

    if args.lesson < 1 or args.lesson > 12:
        print("Error: El número de lección debe estar entre 1 y 12")
        return

    VOICE = args.voice

    asyncio.run(generate_podcast(args.lesson))


if __name__ == "__main__":
    main()
