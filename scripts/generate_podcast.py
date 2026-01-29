#!/usr/bin/env python3
"""
GENERADOR DE PODCASTS - English Tutor B1
Genera podcasts con explicaciones de cada lección usando edge_tts (gratis)

Uso:
    python generate_podcast.py 1      # Genera podcast de la lección 1
    python generate_podcast.py --all  # Genera todos los podcasts

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
always, usually, often, sometimes, never, every day, every week, on Mondays, at weekends.

For Present Continuous, look for words like:
now, right now, at the moment, currently, today, this week.

Now, here's something very important: Stative Verbs.

Some verbs describe states, not actions. These verbs do NOT use the ING form.

Common stative verbs are:
Like, love, hate, want, need, know, believe, understand, remember, see, hear, have, own, belong.

For example:
WRONG: "I'm liking this book."
CORRECT: "I like this book."

Let's summarize:
First: Present Simple is for routines and permanent situations.
Second: Present Continuous is for now and temporary situations.
Third: Look for time expressions to help you choose.
Fourth: Stative verbs do NOT use ING.
Fifth: Don't forget the S for he, she, it in Present Simple.

That's the end of Lesson 1. Good luck with your studies!
""",

    2: """
Welcome to English Tutor B1, Lesson 2: Past Simple versus Past Continuous.

Today we'll learn when to use each past tense.

Let's start with the key difference.

Past Simple is for completed actions at a specific time in the past.
For example: "I watched a film yesterday." The action is finished.

Past Continuous is for actions in progress at a moment in the past.
For example: "I was watching a film at 8 o'clock." The action was happening at that moment.

Now, here's the most important use of Past Continuous:
We use it for background actions that were interrupted.

For example: "I was having dinner when the phone rang."
"Was having" is the longer background action.
"Rang" is the short action that interrupted it.

The structure is simple.

For Past Simple:
Regular verbs add ED: worked, played, watched.
Irregular verbs have special forms: went, saw, had, made.

For Past Continuous:
Use WAS or WERE plus verb ING.
I was working. You were working. He was working. They were working.

Time expressions help you choose.

For Past Simple: yesterday, last week, in 2020, two days ago, when I was young.

For Past Continuous: while, when, as, at that moment, at 6 o'clock yesterday.

Here's a common pattern in stories:
"While I was walking home, I saw an old friend."
"When she was cooking, the fire alarm went off."

The WHILE clause uses Past Continuous.
The main action uses Past Simple.

Common mistakes to avoid:

Mistake 1: Using Past Simple for both actions.
WRONG: "I had dinner when the phone rang."
CORRECT: "I was having dinner when the phone rang."

Mistake 2: Forgetting WAS or WERE.
WRONG: "I watching TV."
CORRECT: "I was watching TV."

Let's summarize:
Past Simple is for completed actions.
Past Continuous is for actions in progress.
Use Past Continuous for background actions with WHILE.
Use Past Simple for the interrupting action with WHEN.

That's the end of Lesson 2. Keep practicing!
""",

    3: """
Welcome to English Tutor B1, Lesson 3: Present Perfect.

This is one of the most important tenses for B1 level.

The Present Perfect connects the past to the present.

Structure: HAVE or HAS plus Past Participle.
"I have worked. She has finished. They have arrived."

When do we use Present Perfect?

Use 1: Life experiences with EVER and NEVER.
"Have you ever been to London?"
"I have never tried sushi."
We don't say when because we're talking about any time in your life.

Use 2: Recent actions with JUST, ALREADY, YET.
"I've just finished my homework." This means a moment ago.
"She has already left." This means before now.
"Have you eaten yet?" YET is for questions and negatives.

Use 3: Unfinished time with TODAY, THIS WEEK, THIS YEAR.
"I've had three coffees today." Today is not finished.
"She's written two reports this week." The week is not finished.

Use 4: Actions that started in the past and continue now with FOR and SINCE.
"I've lived here for five years." The period of time.
"She's worked here since 2019." The starting point.

Remember: FOR plus a period. SINCE plus a point in time.

IMPORTANT: Present Perfect versus Past Simple.

Present Perfect: No specific time mentioned.
"I've been to Paris." We don't know when.

Past Simple: Specific time mentioned.
"I went to Paris in 2020." We know exactly when.

WRONG: "I have been to Paris yesterday."
CORRECT: "I went to Paris yesterday."

The word YESTERDAY needs Past Simple, not Present Perfect.

Common mistakes:

Mistake 1: Using Present Perfect with specific past time.
WRONG: "I have seen him last week."
CORRECT: "I saw him last week."

Mistake 2: Confusing BEEN and GONE.
"She's been to France" means she went and came back.
"She's gone to France" means she's still there now.

Mistake 3: Forgetting HAVE or HAS.
WRONG: "I finished already."
CORRECT: "I've already finished."

Let's summarize:
Present Perfect connects past to present.
Use EVER and NEVER for life experiences.
Use JUST, ALREADY, YET for recent actions.
Use FOR for periods, SINCE for points in time.
Don't use Present Perfect with specific past times.

That's the end of Lesson 3. Well done!
""",

    4: """
Welcome to English Tutor B1, Lesson 4: Future Forms.

English has several ways to talk about the future. Let's learn them all.

Number 1: WILL plus infinitive.

Use WILL for:
Predictions: "It will rain tomorrow."
Decisions made now: "I'll have the chicken, please."
Promises: "I will help you."
Offers: "I'll carry that for you."

Structure: Subject plus WILL plus base verb.
"I will go. She will come. They will arrive."

Negative: WON'T. "I won't be late."

Number 2: BE GOING TO plus infinitive.

Use GOING TO for:
Plans already decided: "I'm going to visit my parents this weekend."
Predictions with evidence: "Look at those clouds. It's going to rain."

Structure: Subject plus AM, IS, ARE plus GOING TO plus base verb.
"I'm going to study. She's going to travel."

Number 3: Present Continuous for future.

Use Present Continuous for:
Fixed arrangements with a specific time and place.
"I'm meeting John at 6 o'clock." This is arranged, confirmed.
"We're flying to Paris tomorrow." The tickets are booked.

Number 4: Present Simple for future.

Use Present Simple for:
Timetables and schedules.
"The train leaves at 9:15."
"The film starts at 8 o'clock."

Now, let's compare WILL versus GOING TO.

Spontaneous decision: WILL.
"The phone is ringing. I'll answer it." You decide now.

Planned decision: GOING TO.
"I'm going to learn French next year." You already decided.

Prediction without evidence: WILL.
"I think she will pass the exam."

Prediction with evidence: GOING TO.
"She's studied a lot. She's going to pass."

Time expressions for future:
Tomorrow, next week, next month, next year.
In two days, in a week, in the future.
Soon, later, tonight, this evening.

Common mistakes:

Mistake 1: Using WILL for plans.
WRONG: "I will meet my friends tonight." If already arranged.
CORRECT: "I'm meeting my friends tonight." Or "I'm going to meet..."

Mistake 2: Forgetting TO in GOING TO.
WRONG: "I'm going study."
CORRECT: "I'm going to study."

Let's summarize:
WILL for spontaneous decisions, promises, predictions.
GOING TO for plans and predictions with evidence.
Present Continuous for fixed arrangements.
Present Simple for timetables.

That's the end of Lesson 4. Good luck!
""",

    5: """
Welcome to English Tutor B1, Lesson 5: Comparatives and Superlatives.

Today we learn how to compare things.

There are two types of adjectives: short and long.

Short adjectives have one syllable: big, small, fast, old, young.
Long adjectives have two or more syllables: expensive, beautiful, interesting.

For SHORT adjectives:

Comparative: Add ER plus THAN.
"She is taller than me."
"This car is faster than that one."

Superlative: Add THE plus EST.
"He is the tallest in the class."
"This is the fastest car."

For LONG adjectives:

Comparative: Add MORE plus THAN.
"This book is more interesting than that one."
"The hotel was more expensive than we expected."

Superlative: Add THE MOST.
"This is the most beautiful city I've visited."
"It's the most expensive restaurant in town."

Now, spelling rules for short adjectives:

If it ends in E, just add R or ST: nice, nicer, nicest.

If it ends in consonant-vowel-consonant, double the last letter:
big, bigger, biggest. hot, hotter, hottest.

If it ends in Y, change to IER or IEST:
happy, happier, happiest. easy, easier, easiest.

IRREGULAR adjectives - you must memorize these:

Good, better, the best.
Bad, worse, the worst.
Far, farther or further, the farthest or furthest.

Now, equality comparisons with AS... AS.

"He is as tall as his father." They are the same height.
"This exam is not as difficult as I expected." Less difficult.

Modifiers make comparisons stronger or weaker:

MUCH or FAR plus comparative: "much better, far more expensive."
A BIT or A LITTLE plus comparative: "a bit cheaper, a little taller."
BY FAR plus superlative: "This is by far the best restaurant."

Common mistakes:

Mistake 1: Using MORE with short adjectives.
WRONG: "more cheap"
CORRECT: "cheaper"

Mistake 2: Forgetting THAN.
WRONG: "She is taller me."
CORRECT: "She is taller than me."

Mistake 3: Forgetting THE with superlatives.
WRONG: "He is tallest."
CORRECT: "He is the tallest."

Let's summarize:
Short adjectives: ER, EST.
Long adjectives: MORE, THE MOST.
Irregular: good-better-best, bad-worse-worst.
Use THAN with comparatives.
Use THE with superlatives.

That's the end of Lesson 5. Keep comparing!
""",

    6: """
Welcome to English Tutor B1, Lesson 6: Modal Verbs.

Modal verbs are special helping verbs. Let's learn the main ones.

Important rule: Modals are always followed by the base verb, no TO, no ING.
"I can swim." Not "I can to swim." Not "I can swimming."

Let's start with CAN and CAN'T.

CAN expresses ability.
"I can speak English."
"She can play the piano."

CAN also expresses permission informally.
"Can I use your phone?"
"You can park here."

CAN'T is the negative.
"I can't swim."
"You can't smoke here."

Now, COULD.

COULD is the past of CAN for ability.
"When I was young, I could run very fast."

COULD is also for polite requests.
"Could you help me, please?" More polite than CAN.

COULD expresses possibility.
"It could rain later." It's possible.

Now, MUST and MUSTN'T.

MUST expresses strong obligation.
"You must wear a seatbelt." It's the law.
"I must finish this today." I feel it's necessary.

MUSTN'T expresses prohibition.
"You mustn't smoke here." It's forbidden.
"You mustn't tell anyone." It's prohibited.

IMPORTANT: MUSTN'T versus DON'T HAVE TO.

MUSTN'T means it's prohibited, forbidden.
"You mustn't park here." It's not allowed.

DON'T HAVE TO means it's not necessary.
"You don't have to wear a tie." You can if you want, but it's not required.

This is a very common mistake!

Now, SHOULD and SHOULDN'T.

SHOULD is for advice and recommendations.
"You should see a doctor."
"You should study more."

SHOULDN'T is for negative advice.
"You shouldn't eat so much sugar."
"You shouldn't stay up late."

Finally, MAY and MIGHT.

Both express possibility, but MAY is slightly more probable.
"It may rain tomorrow." Maybe 50 percent chance.
"It might rain tomorrow." Maybe 30 percent chance.

MAY is also formal permission.
"May I come in?" Very polite.

Let's summarize:
CAN and COULD for ability and requests.
MUST for obligation, MUSTN'T for prohibition.
DON'T HAVE TO means not necessary.
SHOULD for advice.
MAY and MIGHT for possibility.

That's the end of Lesson 6. You should practice these!
""",

    7: """
Welcome to English Tutor B1, Lesson 7: Conditionals.

Conditionals are IF sentences. We'll learn three types today.

ZERO CONDITIONAL: General truths and facts.

Structure: IF plus Present Simple, Present Simple.

"If you heat water, it boils."
"If it rains, the ground gets wet."

These are always true, scientific facts, general truths.

You can also use WHEN instead of IF.
"When you heat water, it boils."

FIRST CONDITIONAL: Real future possibilities.

Structure: IF plus Present Simple, WILL plus infinitive.

"If it rains tomorrow, I will stay home."
"If you study hard, you will pass the exam."

These are real possibilities that might happen.

Common mistake: Don't use WILL in the IF clause.
WRONG: "If it will rain..."
CORRECT: "If it rains..."

SECOND CONDITIONAL: Unreal or hypothetical situations.

Structure: IF plus Past Simple, WOULD plus infinitive.

"If I had more money, I would travel the world."
"If I were you, I would accept the job."

These are imaginary situations, not real.

Notice: We use WERE for all persons, even with I, he, she.
"If I were rich..." Not "If I was rich..." in formal English.

Now, UNLESS.

UNLESS means IF NOT.
"I'll go out unless it rains." Equals "I'll go out if it doesn't rain."
"Unless you hurry, you'll miss the bus."

Other conditional connectors:

AS LONG AS: "I'll help you as long as you help me too."
PROVIDED THAT: "We'll go provided that the weather is good."
IN CASE: "Take an umbrella in case it rains."

Comparing First and Second Conditional:

First Conditional: "If I have time, I will help you."
This is a real possibility. I might have time.

Second Conditional: "If I had time, I would help you."
This is unreal. I don't have time, so I can't help.

Common mistakes:

Mistake 1: Using WOULD in the IF clause.
WRONG: "If I would have money..."
CORRECT: "If I had money..."

Mistake 2: Mixing conditionals.
WRONG: "If I have more money, I would travel."
CORRECT: "If I had more money, I would travel."

Let's summarize:
Zero Conditional: If plus Present, Present. For facts.
First Conditional: If plus Present, Will. For real possibilities.
Second Conditional: If plus Past, Would. For unreal situations.
UNLESS equals IF NOT.

That's the end of Lesson 7. Practice these conditionals!
""",

    8: """
Welcome to English Tutor B1, Lesson 8: The Passive Voice.

The passive voice focuses on the action, not who does it.

Structure: Subject plus BE plus Past Participle.

Active: "Someone stole my bike."
Passive: "My bike was stolen."

We focus on the bike, not on who stole it.

When do we use the passive?

Use 1: When we don't know who did the action.
"My car was broken into last night."

Use 2: When it's obvious who did it.
"The criminal was arrested." By the police, obviously.

Use 3: When the action is more important than the person.
"The Eiffel Tower was built in 1889."

Use 4: In formal or scientific writing.
"The experiment was conducted three times."

Now, passive in different tenses.

Present Simple Passive: AM, IS, ARE plus Past Participle.
"English is spoken here."
"These cars are made in Germany."

Past Simple Passive: WAS, WERE plus Past Participle.
"The book was written in 1990."
"The houses were built last year."

Present Perfect Passive: HAS, HAVE BEEN plus Past Participle.
"The report has been finished."
"Three people have been arrested."

Future Passive: WILL BE plus Past Participle.
"The results will be announced tomorrow."

Modal Passive: Modal plus BE plus Past Participle.
"This can be done."
"It must be completed today."
"It should be checked."

BY plus agent.

Use BY when it's important to say who did the action.
"The book was written by J.K. Rowling."
"America was discovered by Columbus."

Don't use BY when it's obvious or unimportant.
"My bag was stolen." Not "by someone."
"The road is being repaired." Not "by workers."

How to change active to passive:

Step 1: The object becomes the subject.
Step 2: Use the correct form of BE.
Step 3: Use the past participle.
Step 4: The subject becomes BY plus agent, if needed.

Active: "Shakespeare wrote Hamlet."
Passive: "Hamlet was written by Shakespeare."

Common mistakes:

Mistake 1: Forgetting the verb BE.
WRONG: "The window broken."
CORRECT: "The window was broken."

Mistake 2: Using the wrong form of BE.
WRONG: "The letters was sent."
CORRECT: "The letters were sent."

Let's summarize:
Passive structure: BE plus Past Participle.
Use passive when the action is more important.
Use BY plus agent only when necessary.
Match the tense of BE to the original tense.

That's the end of Lesson 8. The lesson has been completed!
""",

    9: """
Welcome to English Tutor B1, Lesson 9: Reported Speech.

Reported speech tells what someone said without using their exact words.

Direct speech: She said, "I am tired."
Reported speech: She said that she was tired.

The main rule: When reporting, we usually move the tense back.

Present becomes Past:
"I work here" becomes "He said he worked there."

Present Continuous becomes Past Continuous:
"I am studying" becomes "She said she was studying."

Past Simple becomes Past Perfect:
"I saw the film" becomes "He said he had seen the film."

Present Perfect becomes Past Perfect:
"I have finished" becomes "She said she had finished."

Will becomes Would:
"I will help" becomes "He said he would help."

Can becomes Could:
"I can swim" becomes "She said she could swim."

Now, the pronouns also change.

"I love coffee" becomes "She said she loved coffee."
"We are ready" becomes "They said they were ready."
I becomes he or she. We becomes they. My becomes his or her.

Time expressions also change:

Today becomes that day.
Tomorrow becomes the next day.
Yesterday becomes the day before.
Now becomes then.
Here becomes there.
This becomes that.

SAY versus TELL.

SAY: "He said that he was tired." No person after SAY.
TELL: "He told me that he was tired." Always use a person after TELL.

WRONG: "He said me that..."
CORRECT: "He told me that..."

Reported Questions.

For yes/no questions, use IF or WHETHER:
"Are you coming?" becomes "She asked if I was coming."

For WH questions, keep the question word but use normal word order:
"Where do you live?" becomes "He asked where I lived."

IMPORTANT: Don't use question word order in reported questions.
WRONG: "She asked where did I live."
CORRECT: "She asked where I lived."

Reported Commands and Requests.

Use TOLD plus person plus TO infinitive for commands.
"Open the door!" becomes "He told me to open the door."

Use ASKED plus person plus TO infinitive for requests.
"Please help me" becomes "She asked me to help her."

For negative commands: TOLD plus person plus NOT TO.
"Don't be late!" becomes "She told me not to be late."

Other reporting verbs:

Admit: He admitted that he had made a mistake.
Deny: She denied taking the money.
Promise: He promised to call me.
Offer: She offered to help.
Suggest: He suggested going to the cinema.

Let's summarize:
Move tenses back when reporting.
Change pronouns and time expressions.
SAY for no person, TELL for person.
Use IF for yes/no questions.
Use TO infinitive for commands.

That's the end of Lesson 9. She said it was a great lesson!
""",

    10: """
Welcome to English Tutor B1, Lesson 10: Relative Clauses.

Relative clauses give extra information about a noun.

The main relative pronouns are:
WHO for people.
WHICH for things and animals.
THAT for people or things.
WHOSE for possession.
WHERE for places.
WHEN for times.

Examples:
"The woman who lives next door is a doctor."
"The book which I bought is very interesting."
"That's the restaurant where we had dinner."

There are two types of relative clauses.

DEFINING relative clauses give essential information.
"The man who called you is waiting." Which man? The one who called.
No commas. Essential information.

NON-DEFINING relative clauses give extra, non-essential information.
"My brother, who lives in London, is visiting us."
We already know who my brother is. The extra information is optional.
Use commas. Extra information.

IMPORTANT: You cannot use THAT in non-defining clauses.
WRONG: "My mother, that is a doctor, works at the hospital."
CORRECT: "My mother, who is a doctor, works at the hospital."

When can you omit the relative pronoun?

In defining clauses, when the pronoun is the OBJECT, you can omit it.
"The book which I bought" equals "The book I bought."
"The man who I met" equals "The man I met."

But when the pronoun is the SUBJECT, you cannot omit it.
"The man who called me" - WHO is the subject. Cannot omit.
"The book which is on the table" - WHICH is the subject. Cannot omit.

WHOSE shows possession.
"The man whose car was stolen called the police."
"That's the company whose products I use."

WHERE for places.
"That's the hotel where we stayed."
"This is the town where I grew up."

WHEN for times.
"I remember the day when we met."
"That was the year when everything changed."

Prepositions in relative clauses.

Informal: "The girl who I spoke to."
Formal: "The girl to whom I spoke."

Informal: "The company which I work for."
Formal: "The company for which I work."

Common mistakes:

Mistake 1: Using WHAT instead of THAT or WHICH.
WRONG: "The thing what I like..."
CORRECT: "The thing that I like..."

Mistake 2: Using a pronoun twice.
WRONG: "The man who I met him yesterday."
CORRECT: "The man who I met yesterday."

Let's summarize:
WHO for people, WHICH for things, THAT for both.
Defining clauses have no commas.
Non-defining clauses have commas, no THAT.
Omit the pronoun when it's the object in defining clauses.

That's the end of Lesson 10. Which lesson is your favorite?
""",

    11: """
Welcome to English Tutor B1, Lesson 11: Phrasal Verbs.

Phrasal verbs are verbs combined with prepositions or adverbs.
They often have a different meaning from the original verb.

LOOK means to see. But LOOK AFTER means to take care of.
"I look after my grandmother." I take care of her.

There are two types: separable and inseparable.

SEPARABLE phrasal verbs:
The object can go in the middle or at the end.
"Turn off the TV" or "Turn the TV off." Both correct.

But with pronouns, you MUST put them in the middle.
"Turn it off." CORRECT.
"Turn off it." WRONG!

INSEPARABLE phrasal verbs:
The object must go at the end.
"Look after the children." CORRECT.
"Look the children after." WRONG!

Let's learn common phrasal verbs by verb.

GET phrasal verbs:
Get up: to leave bed. "I get up at 7 o'clock."
Get on: to enter a bus or train. "Get on the bus here."
Get off: to leave a bus or train. "We get off at the next stop."
Get over: to recover from. "She got over her cold."
Get along with: to have a good relationship. "I get along with my colleagues."

TAKE phrasal verbs:
Take off: to remove clothes, or for planes to leave. "Take off your jacket."
Take up: to start a hobby. "I've taken up yoga."
Take after: to resemble a family member. "She takes after her mother."
Take on: to accept responsibility. "We're taking on new staff."

LOOK phrasal verbs:
Look for: to search. "I'm looking for my keys."
Look after: to take care of. "Can you look after my cat?"
Look forward to: to be excited about. "I look forward to seeing you."
Look up: to search for information. "Look it up in the dictionary."

TURN phrasal verbs:
Turn on: to start a machine. "Turn on the light."
Turn off: to stop a machine. "Turn off the computer."
Turn up: to increase volume, or to arrive. "Turn up the music."
Turn down: to decrease volume, or to reject. "She turned down the job offer."

PUT phrasal verbs:
Put on: to wear. "Put on your coat."
Put off: to postpone. "We put off the meeting."
Put up with: to tolerate. "I can't put up with this noise."

GIVE phrasal verbs:
Give up: to stop trying or quit. "Don't give up!"
Give back: to return. "Give back my book."

Common mistakes:

Mistake 1: Separating inseparable phrasal verbs.
WRONG: "I'm looking my keys for."
CORRECT: "I'm looking for my keys."

Mistake 2: Not separating with pronouns.
WRONG: "Turn off it."
CORRECT: "Turn it off."

Mistake 3: Forgetting the particle.
WRONG: "I gave smoking."
CORRECT: "I gave up smoking."

Let's summarize:
Phrasal verbs combine verbs with particles.
Separable: object can go in middle or end.
Inseparable: object must go at end.
Pronouns must go in the middle of separable phrasal verbs.

That's the end of Lesson 11. Don't give up on phrasal verbs!
""",

    12: """
Welcome to English Tutor B1, Lesson 12: Linking Words and Connectors.

Linking words connect ideas and make your English flow better.

Let's organize them by function.

ADDITION - Adding more information:
AND, ALSO, AS WELL, TOO.
"I speak English and Spanish."
"She also speaks French."
"He plays guitar as well."

More formal: MOREOVER, FURTHERMORE, IN ADDITION.
"The hotel was cheap. Moreover, it had great views."

CONTRAST - Showing difference:
BUT, HOWEVER, ALTHOUGH, DESPITE.

BUT is simple contrast.
"I like coffee, but I don't like tea."

HOWEVER is more formal and starts a new sentence.
"The test was difficult. However, I passed."

ALTHOUGH plus a clause.
"Although it was raining, we went out."
"I went out although it was raining."

DESPITE plus a noun or ING.
"Despite the rain, we went out."
"Despite being tired, he finished the race."

IN SPITE OF works like DESPITE.
"In spite of the traffic, we arrived on time."

CAUSE - Explaining why:
BECAUSE, SINCE, AS.

"I stayed home because I was ill."
"Since it was late, I went to bed."
"As she was tired, she decided to rest."

BECAUSE OF plus a noun.
"I stayed home because of my illness."

DUE TO is more formal.
"The flight was cancelled due to bad weather."

RESULT - Showing consequence:
SO, THEREFORE, AS A RESULT, CONSEQUENTLY.

"I was tired, so I went to bed early."
"It rained all day. Therefore, the match was cancelled."
"The road was closed. As a result, we were late."

SEQUENCE - Ordering ideas:
FIRST, FIRSTLY, SECOND, THEN, NEXT, AFTER THAT, FINALLY.

"First, preheat the oven. Then, prepare the ingredients. Finally, bake for 30 minutes."

PURPOSE - Explaining the goal:
TO, IN ORDER TO, SO THAT.

"I'm studying to pass the exam."
"She left early in order to catch the train."
"I spoke slowly so that everyone could understand."

EXAMPLE - Giving examples:
FOR EXAMPLE, FOR INSTANCE, SUCH AS.

"I like sports, for example tennis and swimming."
"Some countries, such as Japan and Korea, have low crime rates."

Common mistakes:

Mistake 1: Confusing ALTHOUGH and DESPITE.
ALTHOUGH plus clause: "Although I was tired, I continued."
DESPITE plus noun: "Despite my tiredness, I continued."
WRONG: "Despite I was tired..."

Mistake 2: Confusing BECAUSE and BECAUSE OF.
BECAUSE plus clause: "Because it rained, we stayed home."
BECAUSE OF plus noun: "Because of the rain, we stayed home."
WRONG: "Because of it rained..."

Mistake 3: Starting sentences incorrectly.
WRONG: "But I think..."
BETTER: "However, I think..."

Let's summarize:
Use AND, ALSO for addition.
Use BUT, HOWEVER, ALTHOUGH for contrast.
Use BECAUSE, DUE TO for cause.
Use SO, THEREFORE for result.
ALTHOUGH plus clause, DESPITE plus noun.
BECAUSE plus clause, BECAUSE OF plus noun.

That's the end of Lesson 12 and the course!

Congratulations on completing English Tutor B1.

Remember: practice makes perfect. Keep listening, speaking, and learning.

Good luck with your English journey!
""",
}


async def generate_podcast(lesson_id: int, script: str = None) -> str:
    """Genera un podcast para una lección."""
    global VOICE, RATE, VOLUME

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

    print(f"✓ Podcast guardado en: {output_file}")
    return str(output_file)


async def generate_all_podcasts():
    """Genera todos los podcasts."""
    for lesson_id in range(1, 13):
        await generate_podcast(lesson_id)
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

    parser = argparse.ArgumentParser(description="Generador de podcasts para English Tutor B1")
    parser.add_argument("lesson", nargs="?", type=int, help="Número de lección (1-12)")
    parser.add_argument("--all", action="store_true", help="Genera todos los podcasts (1-12)")
    parser.add_argument("--list-voices", action="store_true", help="Lista las voces disponibles")
    parser.add_argument("--voice", type=str, default=VOICE, help=f"Voz a usar (default: {VOICE})")

    args = parser.parse_args()

    if args.list_voices:
        asyncio.run(list_voices())
        return

    if args.voice:
        VOICE = args.voice

    if args.all:
        print("Generando todos los podcasts (1-12)...\n")
        asyncio.run(generate_all_podcasts())
        print("\n¡Todos los podcasts generados!")
        return

    if args.lesson is None:
        parser.print_help()
        print("\nEjemplos:")
        print("  python generate_podcast.py 1      # Genera solo lección 1")
        print("  python generate_podcast.py --all  # Genera todas las lecciones")
        return

    if args.lesson < 1 or args.lesson > 12:
        print("Error: El número de lección debe estar entre 1 y 12")
        return

    asyncio.run(generate_podcast(args.lesson))


if __name__ == "__main__":
    main()
