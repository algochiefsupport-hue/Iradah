# -*- coding: utf-8 -*-
import re, json

with open("gemini-code-1782893053892.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Extract existing days
start_idx = text.find("var DAYS_DATA = {")
end_idx = text.find("var currentDay = 1;", start_idx)
days_block = text[start_idx:end_idx]

day_splits = re.split(r'// ======== DAY (\d+) ========', days_block)
existing_days = {}
for i in range(1, len(day_splits), 2):
    day_num = int(day_splits[i])
    content = day_splits[i+1].strip()
    if content.endswith(','):
        content = content[:-1].strip()
    existing_days[day_num] = content

# New missing days (2, 3, 7, 8, 13, 14, 15, 16, 21..30)
new_days = {
    2: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 2",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Deeds without sincerity are like a traveler who fills his pouch with sand; it burdens him, but provides him no nourishment whatsoever. \u2014 Ibn al-Qayyim, Al-Fawa'id"},
                {"tag": "TEACHING POINTS", "text": "Intention (Ikhlas) is the central axis upon which the transformation of the soul turns.\n\nWhen you quit a destructive habit merely for social reputation, fear of being caught, or fleeting motivation, the heart remains starved.\n\nWhen you make your intention purely for Allah\u2014seeking His pleasure, protecting the dignity He gave you, and purifying your heart\u2014an invincible strength settles into your chest.\n\nEvery time you turn your eyes away or endure an urge, your sincerity turns that discomfort into elevated spiritual rank."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Why did you start this journey? What would change in your relationship with your Creator if you remained pure for 90 days?\n\nWrite your deepest sincere intention in the box below.",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 2",
            "slides": [
                {"tag": "CONCEPT", "text": "Every compulsive behavior is driven by an automated neurological pattern called the 'Habit Loop': Cue \u2192 Craving \u2192 Response \u2192 Reward."},
                {"tag": "TEACHING POINTS", "text": "The Habit Loop: Your brain is constantly looking for shortcuts to save cognitive energy. When you encounter a specific cue (stress, solitude, boredom, late night), your brain activates a predictive craving for dopamine.\n\nThe response is the automatic reaching for explicit content, followed by the neurochemical reward.\n\nTo dismantle this loop, neuroscientists emphasize that you cannot simply 'erase' a neural pathway through brute willpower; you must map the loop and replace the response while keeping the cue manageable."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Identify your primary habit loop. What is the most common trigger cue that starts the cycle for you?\n\nWhen that cue appears today, what non-destructive physical response will you execute instead (e.g. 10 deep breaths, making wudhu, 20 pushups)?",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "The 10-Second Intention Check",
            "text": "Before unlocking your smartphone or opening your laptop, pause for 10 seconds. Ask yourself: 'What is my exact purpose in opening this device right now?' If you have no clear task, put the device face-down and step away."
        }
    },
    3: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 3",
            "slides": [
                {"tag": "KEY QUOTE", "text": "The soul (nafs) is a stubborn beast. If you do not ride it and direct where it goes, it will ride you and throw you off the cliff of destruction. \u2014 Ibn al-Qayyim, Madarij al-Salikin"},
                {"tag": "TEACHING POINTS", "text": "Ibn al-Qayyim describes three states of the soul in the Quran:\n\n1. An-Nafs al-Ammarah bi-s-Su' (the soul that aggressively commands evil)\n2. An-Nafs al-Lawwamah (the self-reproaching soul that feels guilt and struggles against wrongdoing)\n3. An-Nafs al-Mutma'innah (the soul at peace with divine decree).\n\nFeeling guilt, remorse, or conflict when fighting an urge is not a failure\u2014it proves that your conscience is alive! You have transitioned into the noble struggle of Al-Lawwamah. Embrace it as the furnace in which spiritual maturity is forged."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Acknowledge the voice inside you that wants righteousness. How does knowing that your internal struggle is a sign of living faith change your perspective on recovery?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 3",
            "slides": [
                {"tag": "CONCEPT", "text": "Willpower is governed by your Prefrontal Cortex (PFC), the brain's executive command center. When fatigued, the primal limbic system overpowers it."},
                {"tag": "TEACHING POINTS", "text": "The Prefrontal Cortex oversees impulse inhibition, long-term planning, and emotional control.\n\nHowever, PFC glucose and willpower bandwidth are finite resources that deplete over the day\u2014a phenomenon known as 'Ego Depletion'.\n\nBy evening, your executive resistance is naturally at its lowest. Compulsive behaviors prey on this fatigue.\n\nUnderstanding this biological rhythm allows you to construct environmental defenses before your willpower battery runs empty."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Audit your willpower reserves. At what time of day is your executive control at its weakest?\n\nDesign one physical obstacle for that vulnerability window (e.g. charging your phone outside your bedroom, installing a site blocker, scheduling an evening gym session).",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "The 5-Minute Pause Rule",
            "text": "Whenever a craving strikes, do not debate or negotiate with it in your head. Tell yourself: 'I will not touch any device or make any decision for the next 5 minutes.' During those 5 minutes, immediately stand up, drink a cold glass of water, and recite Ayat al-Kursi."
        }
    },
    7: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 7",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Gratitude is based on three pillars: internal acknowledgment of the blessing, verbal praise of the Benefactor, and utilizing the blessing in obedience to Him rather than disobedience. \u2014 Ibn al-Qayyim, Madarij al-Salikin"},
                {"tag": "TEACHING POINTS", "text": "You have completed 7 days of purity! This is not solely your own cleverness; it is Allah's preservation and mercy upon you.\n\nGratitude (Shukr) is described as 'Al-Hafidh' (the Preserver) of blessings and 'Al-Jalib' (the Attractor) of new strength.\n\nWhen you thank Allah for granting you 7 days of clean eyes and a clear conscience, He guarantees: 'If you are grateful, I will surely increase you.' (Surah Ibrahim 14:7).\n\nGuard your gratitude and do not let arrogance whisper that you are now immune."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "List 3 blessings you have begun noticing in your mind, body, or spirit over these first 7 clean days. Express heartfelt thanks to Allah for each one below.",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 7",
            "slides": [
                {"tag": "CONCEPT", "text": "The Week 1 Dopamine Dip: After cutting off high-frequency stimulation, your brain enters a temporary withdrawal phase where baseline dopamine drops below normal."},
                {"tag": "TEACHING POINTS", "text": "During the first 7 to 10 days, your dopamine receptors (D2 receptors) are still down-regulated, while your brain is deprived of artificial dopamine floods.\n\nThis creates a predictable neurochemical valley: you may experience irritability, flat mood, mild anhedonia, or sudden intense urges.\n\nThis is NOT a sign that recovery isn't working; it is neurochemical proof that your dopamine receptors are recalibrating. The discomfort is your brain healing."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Normalize the discomfort. When you feel bored or moody today, recognize it as receptor remodeling.\n\nWhat is one wholesome activity you can engage in to stimulate natural endorphins (brisk walk, stretching, calling a friend)?",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Never Reward Sobriety with Danger",
            "text": "Completing 7 days is a huge milestone, but beware of the subtle trap: 'I've done so well, I can peek just a little.' True celebration is another day of freedom and dignity, not returning to the cage."
        }
    },
    8: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 8",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Patience (Sabr) is to restrain the soul from panic, the tongue from complaining, and the limbs from harming. \u2014 Ibn al-Qayyim, Ad-Da' wad-Dawa'"},
                {"tag": "TEACHING POINTS", "text": "Ibn al-Qayyim categorizes patience into three essential forms:\n1. Sabr upon obedience (performing prayers and dhikr even when tired)\n2. Sabr against disobedience (resisting forbidden desires when cravings burn)\n3. Sabr through hardships (enduring the emotional storms of recovery).\n\nRestraining the soul from forbidden desires is the most heroic form of patience, for it denies an appetite screaming for satisfaction. The pain of patience is temporary; the shame of giving in lasts for months."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Which of the three types of patience feels most challenging for you right now? How can focusing on eternal reward help you endure the temporary discomfort?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 8",
            "slides": [
                {"tag": "CONCEPT", "text": "Delay Discounting: The brain's tendency to drastically undervalue a huge future reward in favor of an immediate, low-value reward right now."},
                {"tag": "TEACHING POINTS", "text": "In evolutionary biology, immediate survival rewards (food, warmth) were favored over distant promises.\n\nIn the modern hyper-stimulated world, this evolutionary trait works against you. Your primitive brain treats an immediate 5-minute dopamine blast as worth more than 90 days of self-respect, mental clarity, and marital happiness.\n\nWhen you become aware of delay discounting, you can manually bridge the gap by vividly visualizing your future self."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Close your eyes for two minutes. Visualize your life at Day 90: your posture, peace in prayer, the glow of your eyes, freedom from shame.\n\nContrast that with the 10 minutes following a relapse. Write down what your future self would advise you today.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "The 10-10-10 Rule",
            "text": "When tempted, ask: 'How will I feel about this in 10 minutes? In 10 hours? In 10 days?' The answer will always dispel the illusion of gratification."
        }
    },
    13: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 13",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Whoever leaves something for the sake of Allah, Allah will replace it with something far better than it in his heart, his life, and his afterlife. \u2014 Ibn al-Qayyim, Al-Fawa'id"},
                {"tag": "TEACHING POINTS", "text": "Ibn al-Qayyim explains that divine replacement (al-'Iwad) is not just material; its greatest manifestation is inner tranquility, a sweet radiance in the heart, joy in divine contemplation, and freedom from being a slave to pixels.\n\nWhen you say 'No' to a fleeting desire solely for Allah's sake, you deposit spiritual capital directly into your soul's treasury.\n\nThe pleasure of resisting for Allah's sake brings a lasting peace that sin can never replicate."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Reflect on what Allah has already begun replacing in your life: self-respect, reduced anxiety, better focus, or sincere tears in prayer. Write down what purity is giving back to you.",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 13",
            "slides": [
                {"tag": "CONCEPT", "text": "Upregulation of D2 Dopamine Receptors: As artificial super-stimuli are removed, your brain starts growing new dopamine receptors to capture everyday natural rewards."},
                {"tag": "TEACHING POINTS", "text": "Around the two-week mark, neuroplastic healing begins to show tangible results.\n\nThe brain's density of dopamine D2 receptors starts to rise back toward baseline.\n\nActivities that previously felt dull\u2014reading a book, tasting a home-cooked meal, taking a walk, laughing with family, the tranquility after Fajr\u2014begin to spark genuine, wholesome pleasure.\n\nThis is the biological definition of recovery: restoring your brain's capacity to be moved by real life."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Plan one completely screen-free natural reward today: sit in a park, drink tea without touching your phone, or read a chapter of an inspiring book. Notice how your attention feels.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Savor the Simple",
            "text": "Notice the taste of your food, the cool morning air, the warmth of the sun on your face. Purity returns the vibrant colors of life that addiction bleached away."
        }
    },
    14: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 14",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Do not belittle minor sins, for mountains are composed of tiny pebbles; and the greatest fire begins with an ignored spark. \u2014 Ibn al-Qayyim, Kitab al-Kaba'ir"},
                {"tag": "TEACHING POINTS", "text": "The devil does not invite a practicing believer to catastrophic ruin on day one. Allah warns: 'Do not follow the footsteps of Satan' (Surah Al-Baqarah 2:168).\n\nA footstep is subtle: a lingering glance on social media, clicking on clickbait, opening an app in bed, browsing late at night.\n\nSmall compromises erode the protective membrane of modesty (Haya'). Once that boundary is softened, catastrophic collapse follows easily.\n\nAbsolute vigilance at the outer perimeter is the secret to perpetual peace."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "What is a 'subtle footstep' or borderline behavior that you sometimes tolerate? What concrete boundary will you put in place today to eradicate it?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 14",
            "slides": [
                {"tag": "CONCEPT", "text": "The Chaser Effect & Neurochemical Priming: A brief glimpse or soft trigger activates a massive priming cascade, creating overpowering cravings for days."},
                {"tag": "TEACHING POINTS", "text": "When an addicted brain encounters an erotic cue, even if you look away after two seconds, the brain releases dopamine and noradrenaline in anticipation.\n\nThis is the 'Chaser Effect'. It sets off subconscious craving loops that continue throbbing in the background for hours or days.\n\nUnderstanding the chaser effect highlights why 'just peeking' or 'testing my willpower' is neurobiological suicide.\n\nZero tolerance is 100 times easier than 99% resistance."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Eliminate any lingering soft triggers. Unfollow provocative accounts, enable safe search, clean your browser history, and set rules for where devices are allowed.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Zero Peeking Principle",
            "text": "Looking once by accident is a mistake; looking twice is a choice. Kill the spark immediately before it sets the forest on fire."
        }
    },
    15: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 15",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Repentance (Tawbah) is not merely a verbal apology; it is a profound revolution of the heart, accompanied by deep remorse, immediate cessation, and an iron resolve never to return. \u2014 Ibn al-Qayyim, Madarij al-Salikin"},
                {"tag": "TEACHING POINTS", "text": "Ibn al-Qayyim wrote extensively on Tawbah Nasuha (sincere repentance). When a believer turns back to Allah with brokenness and humility, that brokenness is dearer to Allah than the proud obedience of the conceited.\n\nEven if you have stumbled in the past, know that Allah rejoices over the return of His servant more than a traveler who finds his lost provisions in a lethal desert.\n\nRepentance is not a one-time event; it is the daily breathing of the believer's soul."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Let go of past self-hatred. True repentance replaces toxic guilt with energetic action. Write a personal prayer of renewal from the depths of your heart.",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 15",
            "slides": [
                {"tag": "CONCEPT", "text": "Extinction Bursts: A temporary, sharp increase in the frequency or intensity of cravings right before the habit pathway finally collapses."},
                {"tag": "TEACHING POINTS", "text": "In behavioral psychology, when an established habit is consistently denied its expected reward, the brain doesn't surrender silently.\n\nAround day 14 to 21, the brain often panics and triggers an 'extinction burst'\u2014throwing its most potent cravings, nostalgic memories, and rationalizations at you in a desperate final bid.\n\nMany people misinterpret this spike as evidence of relapse inevitability. In truth, an extinction burst is the death rattle of the addiction pathway.\n\nIf you weather this storm, the habit loop weakens exponentially."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Prepare for the extinction burst. Recognize that sudden intense cravings mean the old neural highway is starving. When the wave crests, observe it objectively: 'This is my brain's extinction burst. I am not my craving.'",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "The Storm Means It's Working",
            "text": "When cravings scream the loudest, do not despair. The darkest hour of the night is just before the dawn of true neurological freedom."
        }
    },
    16: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 16",
            "slides": [
                {"tag": "KEY QUOTE", "text": "The Qur'an is the complete cure for all mental, spiritual, and physical ailments; whatever the heart suffers from ignorance, doubt, anxiety, and lust, the Qur'an provides its absolute antidote. \u2014 Ibn al-Qayyim, Zad al-Ma'ad"},
                {"tag": "TEACHING POINTS", "text": "The human heart cannot remain empty; if it is not filled with the beauty, majesty, and love of Allah's speech, it will inevitably be filled with base media and corrupt desires.\n\nThe Qur'an acts as an abrasive polish that scrubs the encrusted darkness from the inner eye.\n\nReciting aloud with contemplation (Tadabbur) floods the heart with divine light, making the cheap filth of pornography naturally repulsive to your spiritual palate."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Which Surah or Ayah brings the deepest peace to your heart? How will you make the Qur'an a daily living shield in your life?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 16",
            "slides": [
                {"tag": "CONCEPT", "text": "Auditory & Cortical Engagement: Reciting aloud and focused listening stimulates Broca's area, Wernicke's area, and the auditory cortex, disrupting intrusive sexual thoughts."},
                {"tag": "TEACHING POINTS", "text": "Neuroimaging shows that obsessive cravings activate default mode network (DMN) rumination loops.\n\nPassive silence often allows intrusive imagery to replay.\n\nReciting the Qur'an aloud requires vocal motor coordination, auditory feedback, and linguistic processing simultaneously.\n\nThis multisensory load effectively crowds out intrusive dopamine signaling in the brain, restoring cognitive equilibrium in minutes."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Spend 10 minutes reciting Surah Al-Mulk or Surah Ar-Rahman aloud in a quiet room with slow, melodic pacing. Feel the vibration of your voice and the calming effect on your nervous system.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Replace Filth with Light",
            "text": "You cannot conquer darkness by fighting darkness; you conquer darkness by turning on the light. Let Allah's words illuminate your room and your soul today."
        }
    },
    21: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 21",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Istiqamah (steadfastness) is the soul of all spiritual stations; through it alone do virtues reach perfection and eternal victory is attained. \u2014 Ibn al-Qayyim, Madarij al-Salikin"},
                {"tag": "TEACHING POINTS", "text": "21 days! Three full weeks of purity.\n\nIbn al-Qayyim reminds us that the miraculous nature of steadfastness does not consist of doing grand deeds once a year; it consists of showing up daily with quiet consistency.\n\nSmall, daily deeds performed with regular devotion are far more transformative to the heart than huge bursts followed by abandonment.\n\nYou have laid a formidable foundation of Istiqamah. Ask Allah to preserve your steps until your final breath."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Look at where you started on Day 1 versus today. What is the biggest internal shift you have observed in your self-control?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 21",
            "slides": [
                {"tag": "CONCEPT", "text": "21-Day Synaptic Pruning: After 21 consecutive days of non-activation, unused addictive synaptic connections begin to undergo microglial pruning."},
                {"tag": "TEACHING POINTS", "text": "The brain operates on 'Use it or lose it.' When an addictive habit pathway is starved for 21 days, the brain begins pruning away the superfluous dendritic spines that facilitated the compulsive behavior.\n\nConcurrently, the alternative pathways you have practiced\u2014exercise, prayer, reading, deep breathing\u2014have undergone myelination, making them your new default automatic responses.\n\nYou have crossed a vital neurological threshold."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Solidify your new neural pathways. Write down the top 3 healthy routines that have replaced your old addiction habits over these 21 days. Commit to defending these 3 routines at all costs.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Consistency Over Intensity",
            "text": "It is not what you do once in a while that changes your life; it is what you do consistently every single day. Guard your morning and evening habits with your life."
        }
    },
    22: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 22",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Al-Muraqabah is to maintain constant awareness that Allah is fully watchful over your inner thoughts, your secret gazes, and the deepest secrets of your heart. \u2014 Ibn al-Qayyim, Madarij al-Salikin"},
                {"tag": "TEACHING POINTS", "text": "The highest station of worship is Ihsan: to worship Allah as though you see Him, and if you cannot see Him, knowing that He sees you.\n\nCompulsive habits thrive in secrecy, darkness, and locked doors. Al-Muraqabah dissolves the illusion of secrecy.\n\nKnowing that the Creator of the heavens and the earth is closer to you than your jugular vein fills the room with holy majesty.\n\nThe desire to please Him extinguishes the shameless whisperings of the Nafs."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "How does living with the living reality that Allah is watching you with care and love transform the way you act when you are completely alone?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 22",
            "slides": [
                {"tag": "CONCEPT", "text": "Polyvagal Theory & Autonomic Regulation: Urges trigger sympathetic nervous system arousal; conscious down-regulation restores emotional safety."},
                {"tag": "TEACHING POINTS", "text": "Cravings are physiological states. When triggered, your sympathetic nervous system initiates a fight-or-flight arousal, flooding your blood with adrenaline and cortisol.\n\nYou feel agitated and driven to act. You cannot think your way out of a physiological storm; you must down-regulate your autonomic nervous system using somatic tools like the 'Physiological Sigh' (two quick inhales through the nose followed by a long, slow exhale through the mouth).\n\nThis stimulates the vagus nerve and activates parasympathetic calming."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Practice 5 physiological sighs right now: Inhale deeply through your nose, take an extra sharp sip of air at the top, then slowly sigh all the air out through your mouth for 6-8 seconds. Feel your heart rate slow and your shoulders drop.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "The Physiological Reset",
            "text": "Whenever your body feels restless or tense with cravings, don't argue with your thoughts. Do 3 physiological sighs and wash your face with cold water."
        }
    },
    23: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 23",
            "slides": [
                {"tag": "KEY QUOTE", "text": "The company you keep is like the air you breathe: it either infuses your lungs with vital life or poisons your soul with toxic decay. \u2014 Ibn al-Qayyim, Al-Jawab al-Kafi"},
                {"tag": "TEACHING POINTS", "text": "Ibn al-Qayyim outlines four types of companionship: those like food (essential always), those like medicine (needed at specific times), those like poison (toxic to faith), and those like plague (fatal to your soul).\n\nPornography is the ultimate disease of isolation. It trains you to seek solace in a glowing screen rather than in healthy, dignified human brotherhood and righteous company.\n\nSurround yourself with people who remind you of your highest values."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Who in your life inspires you toward righteousness, purity, and ambition? How can you spend more time in their company and less time isolated in private rooms?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 23",
            "slides": [
                {"tag": "CONCEPT", "text": "Social Mirroring & Oxytocin as the Natural Dopamine Antidote: Meaningful human connection releases oxytocin, reducing the brain's cravings for synthetic dopamine."},
                {"tag": "TEACHING POINTS", "text": "Johann Hari famously summarized modern addiction science: 'The opposite of addiction is not sobriety; the opposite of addiction is connection.'\n\nWhen humans are socially isolated, dopamine receptor sensitivity plunges and the brain seeks compensatory stimulation through hyper-potent artificial vices.\n\nGenuine eye contact, shared laughter, joint worship, and honest vulnerability trigger oxytocin release, which calms the amygdala and satisfies the primal mammalian need for belonging."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Reach out to a family member, mentor, or positive friend today. Send an encouraging message, meet for coffee, or have a meaningful conversation without looking at your phone.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Break the Isolation",
            "text": "Never stay alone in a room with a device when you are feeling low or exhausted. Step out into the living room, walk outside, or join others. Light and people dissolve darkness."
        }
    },
    24: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 24",
            "slides": [
                {"tag": "KEY QUOTE", "text": "The heart is like a mirror; the five senses are the doors through which images enter. If corrupt images enter unchecked, the mirror becomes opaque and can no longer reflect divine truth. \u2014 Ibn al-Qayyim, Al-Fawa'id"},
                {"tag": "TEACHING POINTS", "text": "Purity of mind is impossible if you treat your eyes and ears like open garbage cans for the culture.\n\nIbn al-Qayyim explains that the gaze is an arrow from the poisoned arrows of Iblis. Even if an arrow does not kill you outright, its poison circulates through the bloodstream of your spiritual heart.\n\nGuarding your eyes in public, skipping provocative reels, muting vulgar music, and turning away from vulgar conversations are not ascetic deprivations\u2014they are the vital sanitary hygiene of a warrior's soul."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "What digital content (memes, influencers, shows, feeds) acts as 'soft poison' in your daily life? Make a firm decision to eliminate it today.",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 24",
            "slides": [
                {"tag": "CONCEPT", "text": "Attentional Fragmentation: Fast-paced short-form video consumption erodes dopamine patience and weakens the prefrontal cortex's inhibitory braking system."},
                {"tag": "TEACHING POINTS", "text": "Scrolling through endless 15-second videos trains your brain for instant novelty seeking (hyper-novelty). Every swipe delivers a micro-dopamine pulse.\n\nOver time, this severe attentional fragmentation degrades your ability to sustain attention on complex, slow tasks like deep study, prayer, and emotional self-regulation.\n\nBy clearing away digital clutter, you restore your brain's attentional stamina and strengthen your impulse resistance."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Conduct a mini digital audit: Delete or set strict app timers on short-form video platforms (TikTok, Instagram Reels, YouTube Shorts). Experience the relief of unhurried mental space.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Protect Your Mental Diet",
            "text": "You wouldn't eat from the trash can; don't let trash enter through your eyes and ears. Protect your mind with the same ferocity you protect your home."
        }
    },
    25: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 25",
            "slides": [
                {"tag": "KEY QUOTE", "text": "The pleasures of this world compared to the Hereafter are like a traveler dipping his finger into the ocean and seeing what tiny drop returns upon his fingertip. \u2014 Ibn al-Qayyim, Rawdat al-Muhibbin"},
                {"tag": "TEACHING POINTS", "text": "Ibn al-Qayyim invites us to meditate deeply upon the fleeting nature of this worldly existence.\n\nA sinful release lasts for a mere five seconds; the subsequent guilt, weakness, spiritual desolation, and loss of divine closeness can haunt you for years.\n\nHow tragic is the bargain that trades the eternal delight of the Garden of Eden for five seconds of electronic illusion!\n\nKeep your eyes fixed on the horizon of eternity. Every urge you crush for Allah will be an immense treasure on the Day when neither wealth nor children will avail, except for him who comes to Allah with a clean heart."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Reflect on standing before Allah on the Day of Judgment. What will it feel like to know you fought your desires for His sake and stood firm? Write your reflections.",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 25",
            "slides": [
                {"tag": "CONCEPT", "text": "Future Self-Continuity & The Medial Prefrontal Cortex: People who feel emotionally connected to their future selves make far wiser decisions and resist addictive impulses with ease."},
                {"tag": "TEACHING POINTS", "text": "MRI studies demonstrate that when people think about their future self (1 year or 10 years from now), the brain often activates the same neural regions it uses when thinking about a stranger!\n\nThis 'future self disconnect' makes it easy to sacrifice the future for immediate comfort: 'Let my future self deal with the consequences.'\n\nIncreasing future self-continuity through vivid visualization and writing makes your future well-being tangible and urgent in the present moment."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Write a short paragraph to yourself one year from now. Describe the person you want to be: confident, pure-hearted, disciplined, and spiritually alive.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Don't Betray Your Future",
            "text": "The person you will be tomorrow is shaped by the choice you make right now in this private room. Make your future self proud."
        }
    },
    26: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 26",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Whoever abandons his desires for the sake of Allah will be crowned with divine majesty, dignity, and the veneration of people's hearts. \u2014 Ibn al-Qayyim, Al-Fawa'id"},
                {"tag": "TEACHING POINTS", "text": "There is a profound aura of dignity (Izzah) that radiates from a person who has conquered his lower passions.\n\nIbn al-Qayyim points out that those who surrender to base desires carry an invisible humbleness of shame and subservience, even if they dress in fine garments.\n\nBut the chaste person walks with the quiet nobility of a free person who bows only to his Lord.\n\nChastity (Iffah) is not weakness; it is the ultimate mastery of the human soul over primal instinct."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Embrace your new identity. You are no longer an addict struggling to survive; you are a person of dignity, purity, and purpose. What does being a chaste believer mean to you?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 26",
            "slides": [
                {"tag": "CONCEPT", "text": "Identity-Based Habit Formation: Habits rooted in cognitive identity ('I am a clean person') have 5x higher long-term adherence than outcome-based goals ('I am trying to quit')."},
                {"tag": "TEACHING POINTS", "text": "In behavioral psychology, identity shift is the highest level of behavioral change.\n\nIf your internal self-talk is: 'I am an addict trying to hold out for 30 days,' every temptation is an agonizing test.\n\nWhen your self-talk shifts to: 'I don't watch porn; that's simply not who I am anymore,' temptation loses its emotional leverage.\n\nYour brain strives for cognitive consistency with your core identity."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Repeat to yourself three times with deep conviction: 'I am a person of purity, discipline, and faith. Filth has no place in my life.' Notice the shift in your posture and mindset.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "You Are Free",
            "text": "Stop saying 'I'm trying to stop.' Say 'I am free. I do not touch that.' Step boldly into your true identity."
        }
    },
    27: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 27",
            "slides": [
                {"tag": "KEY QUOTE", "text": "Supplication (Du'a) is among the most powerful means of repelling evil and attaining what is beloved; it is the adversary of calamity, battling it, preventing its descent, and lifting it if it has occurred. \u2014 Ibn al-Qayyim, Ad-Da' wad-Dawa'"},
                {"tag": "TEACHING POINTS", "text": "Ibn al-Qayyim devotes the opening chapters of The Disease and The Cure to the unmatched power of Du'a.\n\nAllah loves to be asked, and He becomes displeased when His servant stops asking Him.\n\nWhen an urge threatens to overpower your frail human strength, raise your hands in desperate, sincere prayer. Cry out to Allah with the vulnerability of a drowning man: 'Ya Hayyu Ya Qayyum, bi rahmatika astagheeth!'\n\nNo urge can withstand the divine aid that rushes to the desperate believer."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "What is the most heartfelt prayer you want to ask Allah for your spiritual and worldly life? Make this Du'a tonight in the last third of the night (Tahajjud).",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 27",
            "slides": [
                {"tag": "CONCEPT", "text": "The Neurobiology of Hope and Surrender: Sincere prayer and transcendent contemplation down-regulate the default amygdala fear-craving response and flood the brain with calming endorphins."},
                {"tag": "TEACHING POINTS", "text": "When a person engages in deeply focused, emotionally authentic prayer and surrender to a higher power, neuroimaging reveals significant reduction in cortisol and an increase in frontal-parietal coherence.\n\nThis biological state of tranquility counteracts the obsessive loop of compulsive cravings, restoring emotional clarity and equilibrium."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Make it a rule: whenever you feel an urge, immediately prostrate (Sujud) on the floor. Whisper your weakness and helplessness to Allah. Stay in Sujud until the storm passes.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Take It to the Floor",
            "text": "The closest a servant is to his Lord is while in prostration. When the world feels heavy and urges bite, drop into Sujud. The ground will hold your tears; Allah will lift your heart."
        }
    },
    28: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 28",
            "slides": [
                {"tag": "KEY QUOTE", "text": "The most dangerous moment for the warrior is when he returns victorious from battle and drops his armor while the enemy is still lurking in the hills. \u2014 Ibn al-Qayyim, Ighathat al-Lahfan"},
                {"tag": "TEACHING POINTS", "text": "As you approach the 30-day milestone, your mind feels clearer, your confidence is soaring, and you feel like you have finally cracked the code.\n\nIbn al-Qayyim warns: this is precisely where arrogance (Ujb) and complacency strike!\n\nYou let your guard down, you keep your phone on your bed, thinking: 'I've mastered this now.'\n\nThe lower soul and Shaytan wait patiently for this exact moment of pride. True mastery is marked by ever-deepening humility and vigilant defense."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "What defense mechanisms did you rely on in your first 7 days that you might have become lazy with recently? Re-establish your ironclad boundaries today.",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 28",
            "slides": [
                {"tag": "CONCEPT", "text": "Relapse Prevention Architecture: Pre-committing to automated safety protocols before environmental and cognitive triggers emerge."},
                {"tag": "TEACHING POINTS", "text": "High-stakes performers and pilots rely on checklists and fail-safe protocols because they know that when stress or emergencies arise, human cognition deteriorates.\n\nYou cannot rely on spontaneous decision-making when tired, stressed, or emotionally triggered.\n\nBuilding an automated 'Relapse Prevention Architecture'\u2014emergency contacts, blocker pin codes kept by a friend, automated bedtime device shutoffs\u2014removes willpower from the equation."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Write out your Emergency Protocol: If an urge reaches intensity 8/10, what are the exact 3 steps you will execute without thinking (e.g. 1. Cold water on face, 2. Walk outside for 15 min, 3. Call accountability partner)?",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Never Lower Your Shield",
            "text": "A warrior does not take off his armor until he is safely inside the gates of Jannah. Stay vigilant, humble, and prepared."
        }
    },
    29: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 29",
            "slides": [
                {"tag": "KEY QUOTE", "text": "The root of faith is firmly anchored in the heart, its trunk is divine knowledge, its branches are righteous deeds, and its sweet fruits are peace of mind, wisdom, and eternal delight in Paradise. \u2014 Ibn al-Qayyim, Miftah Dar as-Sa'adah"},
                {"tag": "TEACHING POINTS", "text": "Look back at the tiny seed planted on Day 1.\n\nThrough twenty-nine days of patience, repentance, lowered gazes, and sincere supplications, your Tree of Faith has broken through the soil, weathered the winds of craving, and grown into a strong, blossoming tree.\n\nYou can feel the change in your chest: the heavy cloud of guilt has dissolved; your prayers have sweetness; your eyes hold genuine peace.\n\nThis is the fruit of obeying Allah. Remember this feeling forever, and never let anything deceive you into trading this garden for a handful of dirt."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Write a tribute to your own perseverance and to Allah's infinite mercy. What are the greatest gifts you have gained over these 29 clean days?",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 29",
            "slides": [
                {"tag": "CONCEPT", "text": "Frontal Lobe Neurogenesis & Restoration of Gray Matter Density: Significant restoration of prefrontal gray matter volume occurs across 30 days of abstinence."},
                {"tag": "TEACHING POINTS", "text": "MRI longitudinal studies show that chronic exposure to hyper-stimulating explicit content thins the prefrontal cortex and weakens connection fibers.\n\nThirty days of continuous abstinence allows neurogenesis and remyelination to restore gray matter density in the anterior cingulate cortex and prefrontal regions.\n\nYour working memory is sharper, your emotional stability is markedly higher, and your ability to delay gratification has fundamentally transformed.\n\nYou have literally rebuilt your brain."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Celebrate your neural transformation! Take note of your improved focus, your clearer memory, and your emotional calm. Write down how much better your brain feels today compared to Day 1.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Behold the Transformation",
            "text": "You are not the same person who started on Day 1. Your mind is sharp, your soul is clear, and your heart is alive. Stand tall in the light of Allah."
        }
    },
    30: {
        "ibn": {
            "title": "Ibn Qayyim Purification - Day 30",
            "slides": [
                {"tag": "KEY QUOTE", "text": "The journey of purification does not end with a single milestone; it is a lifelong ascent from light to greater light, until the soul meets its Creator satisfied and well-pleasing to Him. \u2014 Ibn al-Qayyim, Madarij al-Salikin"},
                {"tag": "TEACHING POINTS", "text": "Thirty days! A full monthly cycle of total purity and victory. You have proven to yourself, your soul, and the heavens that you are not powerless against your desires.\n\nIbn al-Qayyim describes how a habit broken for a full month loses its tyrannical grip on the human will.\n\nHowever, this is not the finish line; it is the graduation from the first level of spiritual discipline into the expansive journey toward 90 days and lifelong chastity.\n\nRenew your pledge with Allah today: 'My prayer, my sacrifice, my living, and my dying are for Allah, Lord of the worlds.' (Surah Al-An'am 6:162)."},
                {"tag": "CLOSING REFLECTION + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Renew your covenant. What is your pledge for the next 60 days on the road to the full 90-day reboot? Write your solemn declaration below.",
                 "text": ""}
            ]
        },
        "bf": {
            "title": "Breaking Free Neuroscience - Day 30",
            "slides": [
                {"tag": "CONCEPT", "text": "The 30-Day Reboot Foundation & The Road to the 90-Day Complete Brain Rewiring: 30 days breaks the chemical addiction cycle; 90 days establishes permanent new neural default networks."},
                {"tag": "TEACHING POINTS", "text": "In addiction neuroscience, 30 days marks the end of acute withdrawal and the normalization of dopamine baseline sensitivity.\n\nHowever, DeltaFosB (a protein that accumulates in neurons during chronic compulsive behavior) has a half-life of several weeks and takes approximately 90 days to fully degrade back to baseline levels.\n\nContinuing this path to Day 90 ensures complete neurobiological reboot and permanent lifestyle transformation.\n\nYou have won the first major campaign; now claim complete lifelong freedom."},
                {"tag": "PRACTICAL EXERCISE + YOUR REFLECTION", "isPracticeAndReflection": True,
                 "exercise": "Set your sights on Day 90! Mark your 90-day goal date on your calendar. Recommit to your daily Morning and Evening Adhkar and daily reminders as lifelong daily hygiene.",
                 "text": ""}
            ]
        },
        "dr": {
            "title": "Daily Reminder",
            "tag": "Forward to Day 90!",
            "text": "30 Days Clean! You have conquered the mountain; now enjoy the panoramic view and keep climbing toward eternal success. Barakallahu feek!"
        }
    }
}

print(f"Defined {len(new_days)} new days.")
print(f"Total days ready: {len(existing_days) + len(new_days)} days!")
