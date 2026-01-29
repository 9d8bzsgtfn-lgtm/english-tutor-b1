#!/usr/bin/env python3
"""
GENERADOR DE PODCASTS DE VOCABULARIO - English Tutor B1
Genera podcasts de vocabulario para cada día de la semana usando edge_tts

Uso:
    python generate_vocabulary_podcasts.py monday       # Genera podcast del lunes
    python generate_vocabulary_podcasts.py --all        # Genera todos los podcasts
    python generate_vocabulary_podcasts.py --list-voices # Lista voces disponibles

Requisitos:
    pip install edge-tts
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
RATE = "-5%"  # Ligeramente más lento para vocabulario
VOLUME = "+0%"

# Directorio base
BASE_DIR = Path(__file__).parent.parent
PODCASTS_DIR = BASE_DIR / "podcasts" / "vocabulary"
PODCASTS_DIR.mkdir(parents=True, exist_ok=True)

# Scripts de podcasts de vocabulario por día
VOCABULARY_SCRIPTS = {
    "monday": """
Hello and welcome to Monday Vocabulary! I'm your English tutor, and today we're going to learn vocabulary about work and careers.

This is essential vocabulary for job interviews, talking about your profession, and everyday work conversations. Let's begin!

Section 1: Job Titles and Professions.

First, let's learn some common job titles. Listen and repeat after me.

Accountant. A-CCOUN-TANT. Someone who manages financial records.
Example: "My sister works as an accountant for a big company."

Entrepreneur. ON-TRE-PRE-NEUR. Someone who starts their own business.
Example: "He's an entrepreneur who started his own tech company."

Freelancer. FREE-LAN-CER. Someone who works independently for different clients.
Example: "She's a freelancer, so she works from home."

Manager. MA-NA-GER. Someone who is in charge of a team or department.
Example: "I need to speak to the manager about this problem."

Colleague. CO-LLEAGUE. A person you work with.
Example: "My colleagues are very friendly and helpful."

Section 2: Work Verbs.

Now, let's learn important verbs related to work.

Apply for. To formally ask for a job.
Example: "I'm going to apply for a new job next week."

Hire. To give someone a job.
Example: "The company wants to hire five new employees."

Resign. To formally leave your job.
Example: "He resigned from his job to travel the world."

Promote. To give someone a higher position.
Example: "She was promoted to senior manager last month."

Retire. To stop working because of age.
Example: "My father is going to retire next year."

Section 3: Workplace Vocabulary.

Let's learn words for things and places at work.

Salary. The money you earn regularly from your job.
Example: "The salary for this position is very competitive."

Deadline. The final date to complete something.
Example: "The deadline for this project is Friday."

Meeting. A time when people come together to discuss things.
Example: "We have a meeting with the client at 10 o'clock."

Overtime. Extra hours worked beyond normal hours.
Example: "I had to work overtime to finish the report."

Contract. A formal written agreement.
Example: "I signed a two-year contract with the company."

Section 4: Useful Expressions.

Finally, let's learn some common work expressions.

Work-life balance. The balance between your job and personal life.
Example: "I'm trying to improve my work-life balance."

Be in charge of. To be responsible for something.
Example: "She's in charge of the marketing department."

Make a living. To earn money to live.
Example: "He makes a living as a graphic designer."

Job satisfaction. Feeling happy about your job.
Example: "Job satisfaction is more important than money to me."

Great work today! Remember to review this vocabulary and try to use it in your own sentences.

Practice makes perfect!

See you tomorrow for Tuesday's vocabulary podcast about Travel and Tourism.

Goodbye!
""",

    "tuesday": """
Hello and welcome to Tuesday Vocabulary! Today we're going to learn vocabulary about travel and tourism.

Whether you're planning a holiday or just dreaming about one, this vocabulary will be very useful. Let's get started!

Section 1: Types of Holidays.

First, let's learn different types of holidays. Listen and repeat.

Package holiday. A holiday where flights and hotel are included together.
Example: "We booked a package holiday to Greece. It includes flights and hotel."

Backpacking. Travelling cheaply with just a backpack.
Example: "I went backpacking around Southeast Asia for three months."

City break. A short holiday in a city.
Example: "We had a lovely city break in Barcelona last weekend."

Cruise. A holiday on a large ship.
Example: "My parents went on a cruise around the Mediterranean."

Road trip. A long journey by car.
Example: "We're planning a road trip along the coast."

Section 2: Accommodation.

Now let's learn vocabulary for places to stay.

Bed and breakfast. A small hotel that includes breakfast.
Example: "We stayed at a lovely bed and breakfast in the countryside."

Hostel. A cheap place where you share rooms with other travellers.
Example: "Hostels are a cheap option for young travellers."

Self-catering. Accommodation with a kitchen where you cook your own food.
Example: "We rented a self-catering apartment with a kitchen."

All-inclusive. A hotel where all meals and drinks are included.
Example: "The all-inclusive resort includes all meals and drinks."

Section 3: At the Airport.

Let's learn essential airport vocabulary.

Boarding pass. The document you need to get on the plane.
Example: "Please have your boarding pass ready."

Check in. To register at the airport before your flight.
Example: "You can check in online 24 hours before your flight."

Hand luggage. Small bags you take on the plane with you.
Example: "You can only bring one piece of hand luggage."

Departure lounge. The area where you wait before boarding.
Example: "We waited in the departure lounge for two hours."

Layover. A stop in another city during your journey.
Example: "We had a four-hour layover in Dubai."

Section 4: Sightseeing.

Finally, vocabulary for exploring new places.

Landmark. A famous building or place.
Example: "The Eiffel Tower is Paris's most famous landmark."

Guided tour. A tour with someone who explains things.
Example: "We took a guided tour of the museum."

Souvenir. Something you buy to remember a place.
Example: "I bought some souvenirs for my family."

Off the beaten track. A place not many tourists visit.
Example: "I prefer places that are off the beaten track."

Breathtaking. Extremely beautiful or impressive.
Example: "The view from the mountain was breathtaking."

Excellent! Now you have lots of vocabulary for your next trip.

Remember, the best way to learn is to use these words when you travel or talk about travelling.

See you tomorrow for Wednesday's vocabulary podcast about Health and Wellbeing.

Safe travels and goodbye!
""",

    "wednesday": """
Hello and welcome to Wednesday Vocabulary! Today we're focusing on health and wellbeing.

This vocabulary is essential for visiting the doctor, talking about how you feel, and discussing healthy habits. Let's begin!

Section 1: Common Illnesses and Symptoms.

First, let's learn how to describe health problems. Listen and repeat.

Headache. Pain in your head.
Example: "I've had a terrible headache all day."

Sore throat. Pain in your throat.
Example: "I can't talk much because I have a sore throat."

Food poisoning. Illness from eating bad food.
Example: "I think I got food poisoning from the restaurant."

Fever. A high body temperature.
Example: "She has a high fever and needs to rest."

Allergy. A bad reaction to certain foods or things.
Example: "I have an allergy to peanuts."

Section 2: At the Doctor's.

Now let's learn vocabulary for a doctor's visit.

Appointment. A planned meeting with the doctor.
Example: "I'd like to make an appointment with the doctor."

Prescription. A note from the doctor for medicine.
Example: "The doctor gave me a prescription for antibiotics."

Examination. When the doctor checks your body.
Example: "The doctor did a thorough examination."

Side effects. Unwanted effects of medicine.
Example: "This medicine may cause drowsiness as a side effect."

Symptoms. Signs that you are ill.
Example: "What are your main symptoms?"

Section 3: Healthy Habits.

Let's learn vocabulary about staying healthy.

Balanced diet. Eating different types of healthy food.
Example: "A balanced diet includes fruits, vegetables, and protein."

Work out. To exercise at a gym.
Example: "I try to work out at the gym three times a week."

Get enough sleep. To sleep the right amount.
Example: "It's important to get enough sleep every night."

Quit smoking. To stop smoking permanently.
Example: "My New Year resolution is to quit smoking."

Stress management. Ways to control stress.
Example: "Meditation helps with stress management."

Section 4: Mental Health.

Finally, vocabulary related to mental wellbeing.

Anxiety. A feeling of worry or nervousness.
Example: "She suffers from anxiety before exams."

Depression. A serious condition of deep sadness.
Example: "Depression is a serious condition that needs treatment."

Wellbeing. The state of being healthy and happy.
Example: "Exercise is good for your physical and mental wellbeing."

Mindfulness. Being aware of the present moment.
Example: "I practice mindfulness meditation every morning."

Self-care. Taking care of your own health and happiness.
Example: "Self-care includes rest, hobbies, and spending time with friends."

Well done! Health vocabulary is really important for everyday life.

Remember to take care of your health, both physical and mental.

See you tomorrow for Thursday's vocabulary podcast about Technology.

Stay healthy and goodbye!
""",

    "thursday": """
Hello and welcome to Thursday Vocabulary! Today we're going to learn vocabulary about technology and digital life.

Technology is everywhere, so this vocabulary will be very useful for your daily conversations. Let's dive in!

Section 1: Devices and Gadgets.

First, let's learn about common devices. Listen and repeat.

Smartphone. A mobile phone with many features.
Example: "I can't imagine life without my smartphone."

Tablet. A flat portable computer with a touchscreen.
Example: "I use my tablet for reading e-books."

Laptop. A portable computer.
Example: "I take my laptop everywhere for work."

Wearable. A device you wear on your body.
Example: "My smartwatch is a wearable that tracks my fitness."

Charger. A device that puts power into batteries.
Example: "I forgot my phone charger at home."

Section 2: Internet and Online Activities.

Now let's learn vocabulary for online activities.

Browse. To look at websites on the internet.
Example: "I spend hours browsing the internet."

Download. To copy files from the internet to your device.
Example: "I need to download the new app update."

Upload. To put files from your device onto the internet.
Example: "I uploaded my holiday photos to social media."

Streaming. Watching or listening to content directly from the internet.
Example: "I prefer streaming films to going to the cinema."

Wi-Fi. Wireless internet connection.
Example: "Is there free Wi-Fi in this café?"

Section 3: Social Media.

Let's learn vocabulary about social media.

Post. Something you share online, or the action of sharing it.
Example: "Did you see her latest post on Instagram?"

Follower. Someone who subscribes to your social media.
Example: "She has thousands of followers on Twitter."

Go viral. When something becomes very popular very quickly online.
Example: "His video went viral overnight."

Hashtag. A word with the hash symbol used to categorize posts.
Example: "Use the hashtag to find related posts."

Notification. An alert from an app or website.
Example: "I turned off my notifications to concentrate."

Section 4: Problems and Solutions.

Finally, vocabulary for tech problems.

Crash. When a computer or program stops working suddenly.
Example: "My computer crashed and I lost all my work."

Bug. An error in software.
Example: "There's a bug in the software that needs fixing."

Backup. A copy of your files for safety.
Example: "Always make a backup of important files."

Password. A secret word to access accounts.
Example: "You should use a strong password with numbers and symbols."

Update. A new version of software.
Example: "Don't forget to update your antivirus software."

Brilliant! Technology vocabulary is essential in today's world.

Practice using these words when you talk about your digital life.

See you tomorrow for Friday's vocabulary podcast about Entertainment and Leisure.

Stay connected and goodbye!
""",

    "friday": """
Hello and welcome to Friday Vocabulary! It's the end of the week, so let's learn vocabulary about entertainment and leisure.

This is perfect vocabulary for talking about your hobbies, favourite shows, and weekend plans. Let's start!

Section 1: Films and Cinema.

First, let's learn vocabulary about films and cinema. Listen and repeat.

Blockbuster. A very successful and popular film.
Example: "The new Marvel film is a real blockbuster."

Sequel. A film that continues the story of an earlier one.
Example: "They're making a sequel to that popular film."

Plot. The story of a film or book.
Example: "The plot was confusing but the acting was great."

Subtitles. Words at the bottom of the screen showing what people say.
Example: "I prefer watching films with English subtitles."

Spoiler. Information that reveals what happens in a story.
Example: "Don't tell me the ending. No spoilers please!"

Section 2: TV Shows and Streaming.

Now let's learn vocabulary for TV and streaming.

Binge-watch. To watch many episodes of a show in one session.
Example: "I binge-watched the whole series in one weekend."

Episode. One part of a TV series.
Example: "The latest episode had a shocking ending."

Season. A set of episodes of a TV show.
Example: "The new season starts next month."

Documentary. A film or programme about real events.
Example: "I watched a fascinating documentary about nature."

Sitcom. A funny TV show about the same characters.
Example: "Friends is one of the most popular sitcoms ever."

Section 3: Music.

Let's learn music vocabulary.

Gig. An informal word for a concert.
Example: "We're going to a gig at the stadium tonight."

Lyrics. The words of a song.
Example: "I love the lyrics of this song."

Catchy. A song that you easily remember.
Example: "That song is so catchy. I can't stop singing it."

Playlist. A list of songs to play.
Example: "I made a playlist for my workout."

Live performance. A performance in front of an audience.
Example: "Her live performances are incredible."

Section 4: Hobbies and Free Time.

Finally, vocabulary for hobbies and leisure activities.

Take up. To start a new hobby.
Example: "I want to take up photography this year."

Pastime. An activity done for enjoyment.
Example: "Reading is my favourite pastime."

Relaxing. Making you feel calm and less stressed.
Example: "Gardening is very relaxing for me."

Challenging. Difficult in an interesting way.
Example: "Rock climbing is challenging but exciting."

Rewarding. Making you feel satisfied and happy.
Example: "Volunteering is a very rewarding hobby."

Fantastic! Now you have plenty of vocabulary to talk about what you like to do in your free time.

Enjoy your weekend!

See you on Saturday for more vocabulary about Food and Dining.

Have fun and goodbye!
""",

    "saturday": """
Hello and welcome to Saturday Vocabulary! It's the weekend, and today we're learning vocabulary about food and dining.

This is perfect for ordering at restaurants, discussing recipes, and talking about your favourite dishes. Let's get cooking!

Section 1: Cooking Methods.

First, let's learn different ways to cook food. Listen and repeat.

Roast. To cook in an oven with oil or fat.
Example: "We roast chicken every Sunday."

Grill. To cook over high heat, usually with flames.
Example: "I prefer to grill fish rather than fry it."

Steam. To cook with hot water vapour.
Example: "Steaming vegetables keeps more nutrients."

Stir-fry. To cook quickly in hot oil while mixing.
Example: "I like to stir-fry vegetables with garlic and soy sauce."

Simmer. To cook slowly in liquid at low temperature.
Example: "Let the sauce simmer for 20 minutes."

Section 2: Describing Food.

Now let's learn adjectives to describe food.

Delicious. Very tasty.
Example: "This pasta is absolutely delicious!"

Bland. Without much flavour.
Example: "The soup was a bit bland. It needed more seasoning."

Spicy. With a hot, burning taste.
Example: "I love spicy food, especially Indian curry."

Crispy. Hard and making a cracking sound when eaten.
Example: "I like my bacon extra crispy."

Tender. Soft and easy to cut or chew.
Example: "The meat was so tender it melted in my mouth."

Section 3: At the Restaurant.

Let's learn vocabulary for eating out.

Reservation. An arrangement to have a table at a restaurant.
Example: "I'd like to make a reservation for 8 o'clock."

Starter. A small dish eaten before the main course.
Example: "Would you like a starter before your main course?"

Main course. The biggest dish in a meal.
Example: "For the main course, I'll have the steak."

Side dish. A smaller dish served with the main course.
Example: "What side dishes do you have?"

Bill. A piece of paper showing what you need to pay.
Example: "Could we have the bill, please?"

Section 4: Diets and Preferences.

Finally, vocabulary for dietary requirements.

Vegetarian. A person who doesn't eat meat.
Example: "I've been vegetarian for five years."

Vegan. A person who doesn't eat any animal products.
Example: "Do you have any vegan options?"

Gluten-free. Food without gluten, a protein in wheat.
Example: "I need to eat gluten-free because of my allergy."

Organic. Food grown without chemicals.
Example: "I prefer to buy organic vegetables."

Portion. The amount of food served.
Example: "The portions at this restaurant are huge!"

Wonderful! Now you're ready to talk about food in English.

Why not practice by describing what you're having for dinner tonight?

See you tomorrow for Sunday's vocabulary podcast about Environment and Nature.

Bon appétit and goodbye!
""",

    "sunday": """
Hello and welcome to Sunday Vocabulary! To end the week, we're going to learn vocabulary about the environment and nature.

This is an important topic for discussions, essays, and everyday conversations. Let's explore!

Section 1: Environmental Problems.

First, let's learn vocabulary about environmental issues. Listen and repeat.

Climate change. Long-term changes in temperature and weather.
Example: "Climate change is one of the biggest challenges we face."

Global warming. The increase in Earth's average temperature.
Example: "Global warming is causing glaciers to melt."

Pollution. Harmful substances in the environment.
Example: "Air pollution is a serious problem in big cities."

Deforestation. Cutting down large areas of forest.
Example: "Deforestation is destroying the Amazon rainforest."

Endangered species. Animals or plants that might become extinct.
Example: "Many endangered species need protection."

Section 2: Sustainability Solutions.

Now let's learn vocabulary about protecting the environment.

Recycle. To process waste so it can be used again.
Example: "We recycle paper, plastic, and glass at home."

Renewable energy. Energy from sources that don't run out.
Example: "Solar and wind are types of renewable energy."

Sustainable. Able to continue without damaging the environment.
Example: "We need to find more sustainable ways to live."

Carbon footprint. The amount of carbon dioxide you produce.
Example: "I'm trying to reduce my carbon footprint."

Eco-friendly. Not harmful to the environment.
Example: "I try to buy eco-friendly products."

Section 3: Nature and Wildlife.

Let's learn vocabulary about nature.

Wildlife. Wild animals and birds.
Example: "The park is home to amazing wildlife."

Habitat. The natural home of animals or plants.
Example: "Animals lose their habitat when forests are cut down."

Conservation. Protecting nature and animals.
Example: "Conservation efforts are helping to save the whales."

Ecosystem. A community of living things and their environment.
Example: "Coral reefs are delicate ecosystems."

Biodiversity. The variety of living things in an area.
Example: "The rainforest has incredible biodiversity."

Section 4: Taking Action.

Finally, vocabulary for environmental actions.

Reduce. To make something smaller in amount.
Example: "We should reduce our use of plastic."

Reuse. To use something again.
Example: "I reuse shopping bags instead of buying new ones."

Plant trees. To put trees in the ground to grow.
Example: "Many organisations plant trees to help the environment."

Raise awareness. To help people understand something important.
Example: "We need to raise awareness about climate change."

Make a difference. To have a positive effect.
Example: "Every small action can make a difference."

Excellent work this week! Environmental vocabulary is very useful for discussions and written work.

Remember: reduce, reuse, recycle!

That's the end of our weekly vocabulary podcasts.

Start again on Monday with Work and Career.

Have a great week and goodbye!
""",
}


async def generate_vocabulary_podcast(day: str) -> str:
    """Genera un podcast de vocabulario para un día específico."""
    global VOICE, RATE, VOLUME

    day_lower = day.lower()
    script = VOCABULARY_SCRIPTS.get(day_lower)

    if script is None:
        print(f"No hay script para el día: {day}")
        print(f"Días disponibles: {', '.join(VOCABULARY_SCRIPTS.keys())}")
        return None

    output_file = PODCASTS_DIR / f"{day_lower}-vocabulary.mp3"

    print(f"Generando podcast de vocabulario para {day.capitalize()}...")
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

    print(f"✓ Podcast guardado en: {output_file}")
    return str(output_file)


async def generate_all_vocabulary_podcasts():
    """Genera todos los podcasts de vocabulario."""
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for day in days:
        await generate_vocabulary_podcast(day)
        print()


async def list_voices():
    """Lista las voces disponibles en inglés."""
    voices = await edge_tts.list_voices()
    english_voices = [v for v in voices if v["Locale"].startswith("en-")]

    print("\nVoces disponibles en inglés:\n")
    for voice in english_voices:
        print(f"  {voice['ShortName']}: {voice['Gender']} - {voice['Locale']}")


def main():
    global VOICE

    parser = argparse.ArgumentParser(description="Generador de podcasts de vocabulario diarios")
    parser.add_argument("day", nargs="?", type=str,
                       help="Día de la semana (monday, tuesday, wednesday, thursday, friday, saturday, sunday)")
    parser.add_argument("--all", action="store_true", help="Genera todos los podcasts de vocabulario")
    parser.add_argument("--list-voices", action="store_true", help="Lista las voces disponibles")
    parser.add_argument("--voice", type=str, default=VOICE, help=f"Voz a usar (default: {VOICE})")

    args = parser.parse_args()

    if args.list_voices:
        asyncio.run(list_voices())
        return

    if args.voice:
        VOICE = args.voice

    if args.all:
        print("Generando todos los podcasts de vocabulario...\n")
        asyncio.run(generate_all_vocabulary_podcasts())
        print("\n¡Todos los podcasts de vocabulario generados!")
        return

    if args.day is None:
        parser.print_help()
        print("\nEjemplos:")
        print("  python generate_vocabulary_podcasts.py monday     # Genera solo podcast del lunes")
        print("  python generate_vocabulary_podcasts.py --all      # Genera todos los días")
        print("\nDías disponibles: monday, tuesday, wednesday, thursday, friday, saturday, sunday")
        return

    valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if args.day.lower() not in valid_days:
        print(f"Error: '{args.day}' no es un día válido.")
        print(f"Días válidos: {', '.join(valid_days)}")
        return

    asyncio.run(generate_vocabulary_podcast(args.day))


if __name__ == "__main__":
    main()
