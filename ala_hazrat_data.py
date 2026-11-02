# -*- coding: utf-8 -*-
"""
Authentic Islamic Duas, Awrad, Kanzul Iman Translations, and 365-Day Spiritual Thoughts
Referenced from:
- Kanzul Iman (by Aala Hazrat Imam Ahmad Raza Khan Bareillvi)
- Al-Wazifatul Kareemah (الوظيفة الكريمة - Tasneef: Aala Hazrat Imam Ahmad Raza Khan)
- Fatawa Razawiyyah & Hada'iq-e-Bakhshish
"""

import json

# ============================================================
# ===  MORNING DUAS (Al-Wazifatul Kareemah & Kanzul Iman)  ===
# ============================================================
MORNING_DUAS_ALA_HAZRAT = [
  {
    "id": "m1",
    "name": "Durood-e-Raza (Awrad-e-Subah)",
    "arabic": "صَلَّى اللّٰهُ عَلَى النَّبِيِّ الْاُمِّيِّ وَآلِهِ صَلَّى اللّٰهُ عَلَيْهِ وَسَلَّمَ صَلَاةً وَّسَلَامًا عَلَيْكَ يَا رَسُولَ اللّٰهِ",
    "translit": "Sallallahu 'alan-Nabiyyil Ummiyyi wa Aalihi Sallallahu 'Alayhi wa Sallam, Salatanw-wa Salaman 'Alayka Ya RasoolAllah.",
    "translationUrdu": "Allah Ta'ala ki rehmat ho Ummi Nabi aur unki aal par, aur salaam ho aap par ae Allah ke Rasool! (Subah o Sham ka Ma'mool)",
    "translation": "May Allah send blessings upon the Unlettered Prophet and upon his noble family, and peace and salutations upon you, O Messenger of Allah!",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan Bareillvi) - Safha 7",
    "count": "1x ya 3x"
  },
  {
    "id": "m2",
    "name": "Ayat al-Kursi (Surah Al-Baqarah 2:255)",
    "arabic": "اللّٰهُ لَاۤ اِلٰهَ اِلَّا هُوَ ۚ اَلْحَیُّ الْقَیُّوْمُ ۚ لَا تَاْخُذُهٗ سِنَةٌ وَّ لَا نَوْمٌ ؕ لَهٗ مَا فِی السَّمٰوٰتِ وَ مَا فِی الْاَرْضِ ؕ مَنْ ذَا الَّذِیْ یَشْفَعُ عِنْدَهٗۤ اِلَّا بِاِذْنِهٖ ؕ یَعْلَمُ مَا بَیْنَ اَیْدِیْهِمْ وَ مَا خَلْفَهُمْ ۚ وَ لَا یُحِیْطُوْنَ بِشَیْءٍ مِّنْ عِلْمِهٖۤ اِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِیُّهُ السَّمٰوٰتِ وَ الْاَرْضَ ۚ وَ لَا یَـُٔوْدُهٗ حِفْظُهُمَا ۚ وَ هُوَ الْعَلِیُّ الْعَظِیْمُ",
    "translit": "Allahu la ilaha illa huwal hayyul qayyum, la ta'khudhuhu sinatunw-wa la nawm...",
    "translationUrdu": "Allah hai jiske siwa koi ma'bood nahi, zinda hai sab ka thaamne wala. Use na oongh aati hai na neend. Usi ka hai jo kuch aasmaano mein hai aur jo kuch zameen mein hai...",
    "translation": "Allah - there is no deity except Him, the Ever-Living, the Sustainer of all existence. Neither drowsiness overtakes Him nor sleep...",
    "source": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Al-Baqarah: 255",
    "count": "1x"
  },
  {
    "id": "m3",
    "name": "Surah Al-Ikhlas (Kanzul Iman)",
    "arabic": "قُلْ هُوَ اللّٰهُ اَحَدٌ ۚ اَللّٰهُ الصَّمَدُ ۚ لَمْ یَلِدْ ۬ وَ لَمْ یُوْلَدْ ۬ وَ لَمْ یَكُنْ لَّهٗ كُفُوًا اَحَدٌ",
    "translit": "Qul Huwallahu Ahad. Allahus-Samad. Lam yalid wa lam yulad. Wa lam yakul-lahu kufuwan ahad.",
    "translationUrdu": "Tum farmao: Woh Allah ek hai. Allah be-niyaz hai (sab uske mohtaaj hain, woh kisi ka mohtaaj nahi). Na uski koi aulaad hai aur na woh kisi se paida hua. Aur na koi uske barabar ka hai.",
    "translation": "Proclaim: He is Allah, the Unique One. Allah, the Absolute upon whom all depend. He neither begets nor is He begotten. And there is none equal to Him.",
    "source": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Al-Wazifatul Kareemah",
    "count": "3x"
  },
  {
    "id": "m4",
    "name": "Surah Al-Falaq (Kanzul Iman)",
    "arabic": "قُلْ اَعُوْذُ بِرَبِّ الْفَلَقِ ۙ مِنْ شَرِّ مَا خَلَقَ ۙ وَ مِنْ شَرِّ غَاسِقٍ اِذَا وَقَبَ ۙ وَ مِنْ شَرِّ النَّفّٰثٰتِ فِی الْعُقَدِ ۙ وَ مِنْ شَرِّ حَاسِدٍ اِذَا حَسَدَ",
    "translit": "Qul a'udhu bi-rabbil falaq, min sharri ma khalaq, wa min sharri ghasiqin idha waqab...",
    "translationUrdu": "Tum farmao: Main subah ke rab ki panah maangta hoon. Uski tamaam makhlooq ke shar se. Aur andheri raat ke shar se jab woh chha jaye. Aur girhon par phoonkne waliyon ke shar se. Aur hasad karne wale ke shar se jab woh hasad kare.",
    "translation": "Proclaim: I seek refuge with the Lord of daybreak. From the evil of all created things. From the evil of dark night as it spreads. From the evil of blowers in knots. And from the evil of an envier when he envies.",
    "source": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Al-Wazifatul Kareemah",
    "count": "3x"
  },
  {
    "id": "m5",
    "name": "Surah An-Nas (Kanzul Iman)",
    "arabic": "قُلْ اَعُوْذُ بِرَبِّ النَّاسِ ۙ مَلِكِ النَّاسِ ۙ اِلٰهِ النَّاسِ ۙ مِنْ شَرِّ الْوَسْوَاسِ ەۙ الْخَنَّاسِ ۙ الَّذِیْ یُوَسْوِسُ فِیْ صُدُوْرِ النَّاسِ ۙ مِنَ الْجِنَّةِ وَ النَّاسِ",
    "translit": "Qul a'udhu bi-rabbin-nas, Malikin-nas, Ilahin-nas, Min sharril waswasil khannas, Alladhi yuwaswisu fi sudoorin-nas, Minal jinnati wan-nas.",
    "translationUrdu": "Tum farmao: Main logon ke rab ki panah maangta hoon. Logon ke badshah ki. Logon ke ma'bood ki. Us waswasa daalne wale ke shar se jo peechhe hat jata hai (jab Allah ka zikr ho). Jo logon ke seenon mein waswasa daalta hai. Jinnat mein se bhi aur insano mein se bhi.",
    "translation": "Proclaim: I seek refuge with the Lord of mankind. The Sovereign of mankind. The True God of mankind. From the evil of the retreating whisperer. Who whispers into the hearts of people. From among jinns and mankind.",
    "source": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Al-Wazifatul Kareemah",
    "count": "3x"
  },
  {
    "id": "m6",
    "name": "Sayyidul Istighfar (Taubah-o-Maghfirat)",
    "arabic": "اَللّٰهُمَّ اَنْتَ رَبِّيْ لَا اِلٰهَ اِلَّا اَنْتَ، خَلَقْتَنِيْ وَاَنَا عَبْدُكَ، وَاَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، اَعُوْذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ، اَبُوْءُ لَكَ بِنِعْمَتِكَ عَلَيَّ، وَاَبُوْءُ بِذَنْبِيْ فَاغْفِرْ لِيْ فَاِنَّهٗ لَا يَغْفِرُ الذُّنُوْبَ اِلَّا اَنْتَ",
    "translit": "Allahumma Anta Rabbi la ilaha illa Anta, khalaqtani wa ana 'abduka, wa ana 'ala 'ahdika wa wa'dika mastata'tu, a'udhu bika min sharri ma sana'tu, abu'u laka bini'matika 'alayya, wa abu'u bidhanbi faghfir li fa-innahu la yaghfirudh-dhunuba illa Ant.",
    "translationUrdu": "Ae Allah! Tu mera Rab hai, tere siwa koi ma'bood nahi. Tune mujhe paida kiya aur main tera banda hoon. Aur main apni taaqat ke mutabiq tere ahad aur wade par qaim hoon. Main apne kiye hue ke shar se teri panah chahta hoon...",
    "translation": "O Allah, You are my Lord; there is none worthy of worship except You. You created me, and I am Your servant, and I hold to Your covenant and promise as much as I am able...",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan) ba-hawaala Sahih Bukhari",
    "count": "1x"
  },
  {
    "id": "m7",
    "name": "Wazifa Daf' Waswasah-e-Shaitan (Nafs Par Qabu)",
    "arabic": "آمَنْتُ بِاللّٰهِ وَرُسُلِهِ، هُوَ الْاَوَّلُ وَالْاٰخِرُ وَالظَّاهِرُ وَالْباطِنُ وَهُوَ بِكُلِّ شَيْءٍ عَلِيْمٌ",
    "translit": "Amantu billahi wa rusulih, Huwal Awwalu wal Akhiru waz-Zahiru wal Batinu wa Huwa bi-kulli shay'in 'Aleem.",
    "translationUrdu": "Main Allah aur uske Rasoolo par imaan laya. Wahi sab se pehle hai aur wahi sab ke baad, aur wahi zahir hai aur wahi posheeda, aur woh har cheez ko khoob jaanne wala hai. (Waswasa daf' karne ke liye Aala Hazrat ka bataya hua wazifa)",
    "translation": "I believe in Allah and His Messengers. He is the First and the Last, the Manifest and the Hidden, and He is the Knower of all things.",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan) - Safha 19",
    "count": "3x"
  },
  {
    "id": "m8",
    "name": "Dua-e-Hifazat-o-Salamati (Subah)",
    "arabic": "بِسْمِ اللّٰهِ الَّذِيْ لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْاَرْضِ وَلَا فِي السَّمَاءِ وَهُوَ السَّمِيْعُ الْعَلِيْمُ",
    "translit": "Bismillahilladhi la yadurru ma'as-mihi shay'un fil ardi wa la fis-sama'i wa Huwas-Sami'ul 'Aleem.",
    "translationUrdu": "Allah ke naam ke saath jiske naam ki barkat se zameen aur aasmaan mein koi cheez nuksaan nahi pahuncha sakti, aur wahi khoob sunne wala jaanne wala hai.",
    "translation": "In the name of Allah, with whose name nothing in the earth or heavens can cause harm, and He is the All-Hearing, All-Knowing.",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan) ba-hawaala Sunan Tirmidhi",
    "count": "3x"
  }
]

# ============================================================
# ===  EVENING DUAS (Al-Wazifatul Kareemah & Kanzul Iman)  ===
# ============================================================
EVENING_DUAS_ALA_HAZRAT = [
  {
    "id": "e1",
    "name": "Durood-e-Raza (Sham Ka Ma'mool)",
    "arabic": "صَلَّى اللّٰهُ عَلَى النَّبِيِّ الْاُمِّيِّ وَآلِهِ صَلَّى اللّٰهُ عَلَيْهِ وَسَلَّمَ صَلَاةً وَّسَلَامًا عَلَيْكَ يَا رَسُولَ اللّٰهِ",
    "translit": "Sallallahu 'alan-Nabiyyil Ummiyyi wa Aalihi Sallallahu 'Alayhi wa Sallam, Salatanw-wa Salaman 'Alayka Ya RasoolAllah.",
    "translationUrdu": "Allah Ta'ala ki rehmat ho Ummi Nabi aur unki aal par, aur salaam ho aap par ae Allah ke Rasool! (Har sham gunaho aur waswaso se bachne ka noorani hisaar)",
    "translation": "May Allah send blessings upon the Unlettered Prophet and his family, and peace and salutations upon you, O Messenger of Allah!",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan Bareillvi)",
    "count": "1x ya 3x"
  },
  {
    "id": "e2",
    "name": "Ayat al-Kursi (Sham Ki Hifazat)",
    "arabic": "اللّٰهُ لَاۤ اِلٰهَ اِلَّا هُوَ ۚ اَلْحَیُّ الْقَیُّوْمُ ۚ لَا تَاْخُذُهٗ سِنَةٌ وَّ لَا نَوْمٌ ؕ لَهٗ مَا فِی السَّمٰوٰتِ وَ مَا فِی الْاَرْضِ ؕ مَنْ ذَا الَّذِیْ یَشْفَعُ عِنْدَهٗۤ اِلَّا بِاِذْنِهٖ ؕ یَعْلَمُ مَا بَیْنَ اَیْدِیْهِمْ وَ مَا خَلْفَهُمْ ۚ وَ لَا یُحِیْطُوْنَ بِشَیْءٍ مِّنْ عِلْمِهٖۤ اِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِیُّهُ السَّمٰوٰتِ وَ الْاَرْضَ ۚ وَ لَا یَـُٔوْدُهٗ حِفْظُهُمَا ۚ وَ هُوَ الْعَلِیُّ الْعَظِیْمُ",
    "translit": "Allahu la ilaha illa huwal hayyul qayyum...",
    "translationUrdu": "Allah hai jiske siwa koi ma'bood nahi, zinda hai sab ka thaamne wala. Use na oongh aati hai na neend...",
    "translation": "Allah - there is no deity except Him, the Ever-Living, the Sustainer of all existence...",
    "source": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Al-Baqarah: 255",
    "count": "1x"
  },
  {
    "id": "e3",
    "name": "Surah Al-Hashr Ki Aakhri Aayaat (Sham Ka Wazifa)",
    "arabic": "هُوَ اللّٰهُ الَّذِیْ لَاۤ اِلٰهَ اِلَّا هُوَ ۚ عٰلِمُ الْغَیْبِ وَ الشَّهَادَةِ ۚ هُوَ الرَّحْمٰنُ الرَّحِیْمُ ۚ هُوَ اللّٰهُ الَّذِیْ لَاۤ اِلٰهَ اِلَّا هُوَ ۚ اَلْمَلِكُ الْقُدُّوْسُ السَّلٰمُ الْمُؤْمِنُ الْمُهَیْمِنُ الْعَزِیْزُ الْجَبَّارُ الْمُتَكَبِّرُ ؕ سُبْحٰنَ اللّٰهِ عَمَّا یُشْرِكُوْنَ ۚ هُوَ اللّٰهُ الْخَالِقُ الْبَارِئُ الْمُصَوِّرُ لَهُ الْاَسْمَآءُ الْحُسْنٰی ؕ یُسَبِّحُ لَهٗ مَا فِی السَّمٰوٰتِ وَ الْاَرْضِ ۚ وَ هُوَ الْعَزِیْزُ الْحَكِیْمُ",
    "translit": "Huwallahul ladhi la ilaha illa Huwa, 'Alimul ghaybi wash-shahadah, Huwar-Rahmanur-Raheem...",
    "translationUrdu": "Wahi Allah hai jiske siwa koi ma'bood nahi, chhipe aur khule ka jaanne wala, wahi hai nihayat meherban reham wala. Wahi Allah hai jiske siwa koi ma'bood nahi, badshah nihayat paak, salamati dene wala, aman bakhshne wala, nigehban, ghalib, azmat wala, badaai wala...",
    "translation": "He is Allah, other than whom there is no deity, Knower of the unseen and the witnessed. He is the Entirely Merciful, the Especially Merciful...",
    "source": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Al-Wazifatul Kareemah Safha 11",
    "count": "1x"
  },
  {
    "id": "e4",
    "name": "3 Qul (Surah Ikhlas, Falaq, Nas)",
    "arabic": "قُلْ هُوَ اللّٰهُ اَحَدٌ ۚ ... قُلْ اَعُوْذُ بِرَبِّ الْفَلَقِ ۙ ... قُلْ اَعُوْذُ بِرَبِّ النَّاسِ ۙ",
    "translit": "Surah Al-Ikhlas, Surah Al-Falaq, Surah An-Nas (Kanzul Iman Tarjuma)",
    "translationUrdu": "Surah Ikhlas, Falaq aur Nas sham ke waqt 3-3 martaba padhein. Har qism ke shar, jadoo, aur shaitani waswaso se bachao ka mustanad qila hai.",
    "translation": "Recite the 3 Quls 3 times each every evening. An impenetrable spiritual fortress against evil whispers, lustful traps, and distress.",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan Bareillvi)",
    "count": "3x each"
  },
  {
    "id": "e5",
    "name": "Sayyidul Istighfar (Sham Ki Taubah)",
    "arabic": "اَللّٰهُمَّ اَنْتَ رَبِّيْ لَا اِلٰهَ اِلَّا اَنْتَ، خَلَقْتَنِيْ وَاَنَا عَبْدُكَ، وَاَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، اَعُوْذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ...",
    "translit": "Allahumma Anta Rabbi la ilaha illa Anta, khalaqtani wa ana 'abduka...",
    "translationUrdu": "Ae Allah! Tu mera Rab hai, tere siwa koi ma'bood nahi. Tune mujhe paida kiya aur main tera banda hoon. Jo shakhs sham ko yaqeen ke saath yeh padhe aur us raat intiqal ho toh jannatiyon mein se hoga.",
    "translation": "O Allah, You are my Lord; there is no deity except You. You created me, and I am Your servant...",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan) ba-hawaala Sahih Bukhari",
    "count": "1x"
  },
  {
    "id": "e6",
    "name": "Kalima-e-Tamjeed (Sham Ka Hisaar)",
    "arabic": "سُبْحَانَ اللّٰهِ وَالْحَمْدُ لِلّٰهِ وَلَا إِلٰهَ إِلَّا اللّٰهُ وَاللّٰهُ أَكْبَرُ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللّٰهِ الْعَلِيِّ الْعَظِيْمِ",
    "translit": "SubhanAllahi wal-hamdu lillahi wa la ilaha illallahu wallahu Akbar, wa la hawla wa la quwwata illa billahil 'Aliyyil 'Azeem.",
    "translationUrdu": "Allah paak hai aur tamaam tareefein Allah ke liye hain aur Allah ke siwa koi ma'bood nahi aur Allah sab se bada hai, aur burayi se bachne aur neki karne ki taaqat nahi magar Allah hi ki taraf se jo aali shan badaai wala hai.",
    "translation": "Glory be to Allah, all praise is due to Allah, there is no god but Allah, and Allah is the Greatest. And there is no might nor power except with Allah, the Most High, the Supreme.",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan Bareillvi) - Safha 14",
    "count": "10x"
  },
  {
    "id": "e7",
    "name": "Panah Talab Karne Ki Dua (Raat Ka Tahaffuz)",
    "arabic": "اَعُوْذُ بِكَلِمَاتِ اللّٰهِ التَّامَّاتِ مِنْ شَرِّ مَا خَلَقَ",
    "translit": "A'udhu bi-kalimatillahit-tammati min sharri ma khalaq.",
    "translationUrdu": "Main Allah ke poore kalimaat ke zariye uski tamaam makhlooq ke shar se panah maangta hoon. (Sham ke waqt 3 baar padhne se raat bhar zehreeli cheezon aur shaitan se hifazat rehti hai)",
    "translation": "I seek refuge in the perfect words of Allah from the evil of what He has created.",
    "source": "Al-Wazifatul Kareemah (Aala Hazrat Imam Ahmad Raza Khan) ba-hawaala Sahih Muslim",
    "count": "3x"
  }
]

# ============================================================
# ===  365-DAY TREE OF FAITH SVG GENERATOR (16 STAGES)     ===
# ============================================================
TREE_365_SVG_JS = """
function drawTree(stage) {
  // 16 Detailed Progressive SVG Stages for 365 Days
  // Stage 0: Day 0 (Seed in soil - Taubah)
  // Stage 1: Days 1-7 (Week 1 - First Sprout)
  // Stage 2: Days 8-14 (Week 2 - Twin Leaves)
  // Stage 3: Days 15-21 (Week 3 - Firm Stem)
  // Stage 4: Days 22-30 (Month 1 - Young Plant)
  // Stage 5: Days 31-45 (Deep Roots & Branching)
  // Stage 6: Days 46-60 (Month 2 - Sturdy Sapling)
  // Stage 7: Days 61-90 (Month 3 - Dense Green Tree)
  // Stage 8: Days 91-120 (Month 4 - Young Cedar)
  // Stage 9: Days 121-150 (Month 5 - Expanding Foliage)
  // Stage 10: Days 151-180 (Month 6 - Half Year Blossoms)
  // Stage 11: Days 181-220 (Month 7 - Fruit Bearing)
  // Stage 12: Days 221-270 (Months 8-9 - Emerald Sanctuary)
  // Stage 13: Days 271-320 (Month 10 - Golden Radiance)
  // Stage 14: Days 321-364 (Months 11-12 - Ancient Guardian Oak)
  // Stage 15: Days 365+ (1 Year - Shajarah-e-Tayyibah celestial crown)

  const svgs = [
    // Stage 0: Day 0 - Seed resting in fertile soil (Taubah / Renewal)
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g0" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f5e6d3"/><stop offset="100%" stop-color="#d9b99b"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g0)"/>
      <ellipse cx="36" cy="52" rx="20" ry="7" fill="#7a4e2d" opacity="0.45"/>
      <ellipse cx="36" cy="50" rx="14" ry="5" fill="#5c381e" opacity="0.6"/>
      <circle cx="36" cy="46" r="6" fill="#8B5A2B"/>
      <ellipse cx="36" cy="44" rx="4" ry="5.5" fill="#c49a6c" opacity="0.6"/>
      <path d="M36 41 Q37 38 39 37" stroke="#7cb342" stroke-width="1.8" stroke-linecap="round" fill="none"/>
    </svg>`,

    // Stage 1: Days 1-7 (Week 1) - Tiny sprout emerging into sunlight
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#edf7ed"/><stop offset="100%" stop-color="#c8e6c9"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g1)"/>
      <ellipse cx="36" cy="56" rx="16" ry="5" fill="#6d4c41" opacity="0.4"/>
      <path d="M36 54 Q35 44 36 36" stroke="#4caf50" stroke-width="3" stroke-linecap="round" fill="none"/>
      <ellipse cx="33" cy="34" rx="5" ry="3.5" fill="#66bb6a" transform="rotate(-30 33 34)"/>
      <ellipse cx="39" cy="33" rx="4" ry="2.8" fill="#81c784" transform="rotate(25 39 33)"/>
      <circle cx="36" cy="30" r="2.2" fill="#aed581"/>
    </svg>`,

    // Stage 2: Days 8-14 (Week 2) - Twin vibrant leaves, stem hardening
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8f5e9"/><stop offset="100%" stop-color="#a5d6a7"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g2)"/>
      <ellipse cx="36" cy="57" rx="17" ry="5" fill="#5d4037" opacity="0.45"/>
      <path d="M36 55 Q36 42 36 30" stroke="#388e3c" stroke-width="3.6" stroke-linecap="round" fill="none"/>
      <ellipse cx="27" cy="34" rx="7" ry="4.5" fill="#43a047" transform="rotate(-35 27 34)"/>
      <ellipse cx="45" cy="33" rx="7" ry="4.5" fill="#43a047" transform="rotate(35 45 33)"/>
      <ellipse cx="36" cy="26" rx="5" ry="6" fill="#66bb6a"/>
    </svg>`,

    // Stage 3: Days 15-21 (Week 3) - Firm stem with side branches forming
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g3" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#dcedc8"/><stop offset="100%" stop-color="#81c784"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g3)"/>
      <ellipse cx="36" cy="58" rx="18" ry="5" fill="#4e342e" opacity="0.5"/>
      <path d="M36 56 L36 26" stroke="#2e7d32" stroke-width="4.2" stroke-linecap="round"/>
      <path d="M36 42 Q28 38 24 35" stroke="#2e7d32" stroke-width="2.6" fill="none"/>
      <path d="M36 36 Q44 32 48 29" stroke="#2e7d32" stroke-width="2.6" fill="none"/>
      <ellipse cx="21" cy="33" rx="6.5" ry="4" fill="#4caf50" transform="rotate(-30 21 33)"/>
      <ellipse cx="51" cy="27" rx="6.5" ry="4" fill="#4caf50" transform="rotate(30 51 27)"/>
      <ellipse cx="36" cy="22" rx="7.5" ry="6" fill="#43a047"/>
    </svg>`,

    // Stage 4: Days 22-30 (Month 1 Complete!) - Healthy young plant
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g4" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c8e6c9"/><stop offset="100%" stop-color="#66bb6a"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g4)"/>
      <ellipse cx="36" cy="59" rx="19" ry="5.5" fill="#3e2723" opacity="0.55"/>
      <rect x="33.8" y="24" width="4.4" height="34" rx="2.2" fill="#33691e"/>
      <ellipse cx="36" cy="20" rx="10" ry="8" fill="#388e3c"/>
      <ellipse cx="23" cy="27" rx="8" ry="5" fill="#4caf50" transform="rotate(-32 23 27)"/>
      <ellipse cx="49" cy="27" rx="8" ry="5" fill="#4caf50" transform="rotate(32 49 27)"/>
      <ellipse cx="26" cy="39" rx="6.5" ry="4" fill="#66bb6a" transform="rotate(-20 26 39)"/>
      <ellipse cx="46" cy="39" rx="6.5" ry="4" fill="#66bb6a" transform="rotate(20 46 39)"/>
    </svg>`,

    // Stage 5: Days 31-45 - Deep rooted bush with strong foundation
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g5" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#b2dfdb"/><stop offset="100%" stop-color="#4db6ac"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g5)"/>
      <ellipse cx="36" cy="60" rx="20" ry="5.5" fill="#2d1d13" opacity="0.6"/>
      <rect x="33.5" y="22" width="5" height="36" rx="2.5" fill="#4e342e"/>
      <ellipse cx="36" cy="18" rx="12" ry="10" fill="#2e7d32"/>
      <ellipse cx="20" cy="26" rx="9" ry="6" fill="#388e3c" transform="rotate(-35 20 26)"/>
      <ellipse cx="52" cy="26" rx="9" ry="6" fill="#388e3c" transform="rotate(35 52 26)"/>
      <ellipse cx="24" cy="38" rx="8" ry="5" fill="#43a047" transform="rotate(-20 24 38)"/>
      <ellipse cx="48" cy="38" rx="8" ry="5" fill="#43a047" transform="rotate(20 48 38)"/>
      <circle cx="28" cy="48" r="2" fill="#ffb74d"/>
      <circle cx="44" cy="46" r="2" fill="#ffb74d"/>
    </svg>`,

    // Stage 6: Days 46-60 (Month 2 Complete!) - Sturdy sapling, brown wood bark
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g6" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#a5d6a7"/><stop offset="100%" stop-color="#43a047"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g6)"/>
      <ellipse cx="36" cy="60" rx="20" ry="6" fill="#271406" opacity="0.65"/>
      <rect x="33" y="18" width="6" height="40" rx="3" fill="#3e2723"/>
      <ellipse cx="36" cy="16" rx="14" ry="11" fill="#1b5e20"/>
      <ellipse cx="18" cy="24" rx="10.5" ry="6.5" fill="#2e7d32" transform="rotate(-38 18 24)"/>
      <ellipse cx="54" cy="24" rx="10.5" ry="6.5" fill="#2e7d32" transform="rotate(38 54 24)"/>
      <ellipse cx="20" cy="36" rx="9" ry="5.5" fill="#388e3c" transform="rotate(-22 20 36)"/>
      <ellipse cx="52" cy="36" rx="9" ry="5.5" fill="#388e3c" transform="rotate(22 52 36)"/>
      <circle cx="26" cy="20" r="2.4" fill="#ff9800"/>
      <circle cx="46" cy="20" r="2.4" fill="#ff9800"/>
    </svg>`,

    // Stage 7: Days 61-90 (Quarter-Year / DeltaFosB Reset Milestone!)
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g7" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#80cbc4"/><stop offset="100%" stop-color="#00897b"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g7)"/>
      <ellipse cx="36" cy="61" rx="21" ry="6" fill="#1b0000" opacity="0.65"/>
      <rect x="32.5" y="16" width="7" height="43" rx="3.5" fill="#3e2723"/>
      <ellipse cx="36" cy="14" rx="16" ry="12" fill="#1b5e20"/>
      <ellipse cx="16" cy="22" rx="11" ry="7" fill="#2e7d32" transform="rotate(-40 16 22)"/>
      <ellipse cx="56" cy="22" rx="11" ry="7" fill="#2e7d32" transform="rotate(40 56 22)"/>
      <ellipse cx="18" cy="34" rx="9.5" ry="6" fill="#388e3c" transform="rotate(-24 18 34)"/>
      <ellipse cx="54" cy="34" rx="9.5" ry="6" fill="#388e3c" transform="rotate(24 54 34)"/>
      <circle cx="24" cy="16" r="3" fill="#ff5722"/>
      <circle cx="48" cy="16" r="3" fill="#ff5722"/>
      <circle cx="36" cy="24" r="3" fill="#ffc107"/>
    </svg>`,

    // Stage 8: Days 91-120 (Month 4) - Sturdy Young Cedar, deep foliage
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g8" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#66bb6a"/><stop offset="100%" stop-color="#2e7d32"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g8)"/>
      <ellipse cx="36" cy="61" rx="22" ry="6" fill="#140d07" opacity="0.7"/>
      <rect x="32" y="14" width="8" height="46" rx="4" fill="#2d1e12"/>
      <ellipse cx="36" cy="12" rx="17" ry="13" fill="#0d4e16"/>
      <ellipse cx="14" cy="20" rx="12" ry="8" fill="#1b5e20" transform="rotate(-42 14 20)"/>
      <ellipse cx="58" cy="20" rx="12" ry="8" fill="#1b5e20" transform="rotate(42 58 20)"/>
      <ellipse cx="16" cy="32" rx="10" ry="6.5" fill="#2e7d32" transform="rotate(-24 16 32)"/>
      <ellipse cx="56" cy="32" rx="10" ry="6.5" fill="#2e7d32" transform="rotate(24 56 32)"/>
      <circle cx="22" cy="14" r="3.2" fill="#ff7043"/>
      <circle cx="50" cy="14" r="3.2" fill="#ff7043"/>
      <circle cx="36" cy="22" r="3.2" fill="#ffd54f"/>
    </svg>`,

    // Stage 9: Days 121-150 (Month 5) - Broadening canopy, radiant leaves
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g9" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#4db6ac"/><stop offset="100%" stop-color="#00695c"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g9)"/>
      <ellipse cx="36" cy="62" rx="22" ry="6" fill="#1a120b" opacity="0.7"/>
      <rect x="31.5" y="13" width="9" height="48" rx="4.5" fill="#2d1b0d"/>
      <ellipse cx="36" cy="11" rx="19" ry="14" fill="#0b4514"/>
      <ellipse cx="12" cy="19" rx="13" ry="8.5" fill="#155724" transform="rotate(-44 12 19)"/>
      <ellipse cx="60" cy="19" rx="13" ry="8.5" fill="#155724" transform="rotate(44 60 19)"/>
      <ellipse cx="14" cy="31" rx="11" ry="7" fill="#1e7e34" transform="rotate(-25 14 31)"/>
      <ellipse cx="58" cy="31" rx="11" ry="7" fill="#1e7e34" transform="rotate(25 58 31)"/>
      <circle cx="20" cy="13" r="3.5" fill="#ffb300"/>
      <circle cx="52" cy="13" r="3.5" fill="#ffb300"/>
      <circle cx="36" cy="20" r="3.5" fill="#ffe082"/>
      <circle cx="28" cy="27" r="2.8" fill="#ff7043"/>
      <circle cx="44" cy="27" r="2.8" fill="#ff7043"/>
    </svg>`,

    // Stage 10: Days 151-180 (Month 6 / Half Year Milestone!) - Full blossoms
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g10" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#388e3c"/><stop offset="100%" stop-color="#1b5e20"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g10)"/>
      <ellipse cx="36" cy="62" rx="23" ry="6.5" fill="#130b05" opacity="0.75"/>
      <rect x="31" y="12" width="10" height="49" rx="5" fill="#26170b"/>
      <ellipse cx="36" cy="10" rx="20" ry="14.5" fill="#093d11"/>
      <ellipse cx="10" cy="18" rx="14" ry="9" fill="#124e1b" transform="rotate(-45 10 18)"/>
      <ellipse cx="62" cy="18" rx="14" ry="9" fill="#124e1b" transform="rotate(45 62 18)"/>
      <ellipse cx="12" cy="30" rx="11.5" ry="7.5" fill="#196924" transform="rotate(-26 12 30)"/>
      <ellipse cx="60" cy="30" rx="11.5" ry="7.5" fill="#196924" transform="rotate(26 60 30)"/>
      <!-- Vibrant Flowers & Buds -->
      <circle cx="18" cy="12" r="3.8" fill="#ff4081"/>
      <circle cx="54" cy="12" r="3.8" fill="#ff4081"/>
      <circle cx="36" cy="18" r="4.2" fill="#ffca28"/>
      <circle cx="26" cy="25" r="3.2" fill="#ff80ab"/>
      <circle cx="46" cy="25" r="3.2" fill="#ff80ab"/>
    </svg>`,

    // Stage 11: Days 181-220 (Month 7) - Fruit Bearing Shajar, sweet harvests
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g11" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2e7d32"/><stop offset="100%" stop-color="#0e3d14"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g11)"/>
      <ellipse cx="36" cy="62" rx="24" ry="6.5" fill="#110a04" opacity="0.8"/>
      <rect x="31" y="11" width="10" height="50" rx="5" fill="#221307"/>
      <ellipse cx="36" cy="9" rx="21" ry="15" fill="#08360f"/>
      <ellipse cx="9" cy="17" rx="14.5" ry="9.5" fill="#0f4518" transform="rotate(-46 9 17)"/>
      <ellipse cx="63" cy="17" rx="14.5" ry="9.5" fill="#0f4518" transform="rotate(46 63 17)"/>
      <!-- Ripe Fruits -->
      <circle cx="16" cy="14" r="4.2" fill="#d32f2f"/>
      <circle cx="56" cy="14" r="4.2" fill="#d32f2f"/>
      <circle cx="36" cy="22" r="4.6" fill="#f57c00"/>
      <circle cx="24" cy="28" r="3.8" fill="#d32f2f"/>
      <circle cx="48" cy="28" r="3.8" fill="#f57c00"/>
    </svg>`,

    // Stage 12: Days 221-270 (Months 8-9) - Emerald Sanctuary, wide shade
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g12" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1b5e20"/><stop offset="100%" stop-color="#003300"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g12)"/>
      <ellipse cx="36" cy="63" rx="25" ry="7" fill="#0e0703" opacity="0.85"/>
      <rect x="30.5" y="10" width="11" height="52" rx="5.5" fill="#1d0f04"/>
      <ellipse cx="36" cy="8" rx="22" ry="15.5" fill="#062e0c"/>
      <ellipse cx="8" cy="16" rx="15" ry="10" fill="#0c3a13" transform="rotate(-48 8 16)"/>
      <ellipse cx="64" cy="16" rx="15" ry="10" fill="#0c3a13" transform="rotate(48 64 16)"/>
      <!-- Golden Glow Spots -->
      <circle cx="15" cy="12" r="4.5" fill="#ffd700" opacity="0.9"/>
      <circle cx="57" cy="12" r="4.5" fill="#ffd700" opacity="0.9"/>
      <circle cx="36" cy="19" r="5" fill="#ffab00" opacity="0.9"/>
      <circle cx="25" cy="26" r="4" fill="#ffd54f" opacity="0.85"/>
      <circle cx="47" cy="26" r="4" fill="#ffd54f" opacity="0.85"/>
    </svg>`,

    // Stage 13: Days 271-320 (Month 10) - Golden Radiance (Crown of Noor)
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g13" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2e4d28"/><stop offset="100%" stop-color="#0a260f"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g13)"/>
      <ellipse cx="36" cy="63" rx="25" ry="7" fill="#0a0502" opacity="0.9"/>
      <rect x="30" y="9" width="12" height="53" rx="6" fill="#180c03"/>
      <ellipse cx="36" cy="7" rx="23" ry="16" fill="#042308"/>
      <ellipse cx="7" cy="15" rx="15.5" ry="10.5" fill="#09300f" transform="rotate(-50 7 15)"/>
      <ellipse cx="65" cy="15" rx="15.5" ry="10.5" fill="#09300f" transform="rotate(50 65 15)"/>
      <circle cx="14" cy="10" r="5" fill="#ffe082"/>
      <circle cx="58" cy="10" r="5" fill="#ffe082"/>
      <circle cx="36" cy="16" r="5.5" fill="#ffd700"/>
      <!-- Celestial Light Rays -->
      <path d="M36 2 L38 -1 L40 2" stroke="#fff59d" stroke-width="1.8" fill="none"/>
    </svg>`,

    // Stage 14: Days 321-364 (Months 11-12) - Ancient Guardian Oak, immense resilience
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs><linearGradient id="g14" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1a472a"/><stop offset="100%" stop-color="#021f09"/></linearGradient></defs>
      <rect width="72" height="72" rx="36" fill="url(#g14)"/>
      <ellipse cx="36" cy="63" rx="26" ry="7.5" fill="#080301" opacity="0.95"/>
      <rect x="29.5" y="8" width="13" height="54" rx="6.5" fill="#140902"/>
      <ellipse cx="36" cy="6" rx="24" ry="16.5" fill="#021c05"/>
      <ellipse cx="6" cy="14" rx="16" ry="11" fill="#06270b" transform="rotate(-52 6 14)"/>
      <ellipse cx="66" cy="14" rx="16" ry="11" fill="#06270b" transform="rotate(52 66 14)"/>
      <circle cx="13" cy="9" r="5.2" fill="#ffd54f"/>
      <circle cx="59" cy="9" r="5.2" fill="#ffd54f"/>
      <circle cx="36" cy="15" r="6" fill="#ffc107"/>
      <circle cx="23" cy="22" r="4.5" fill="#ffecb3"/>
      <circle cx="49" cy="22" r="4.5" fill="#ffecb3"/>
    </svg>`,

    // Stage 15: Days 365+ (1 FULL YEAR MILESTONE!) - Shajarah-e-Tayyibah
    // "Asluha thabitun wa far'uha fis-sama" (Surah Ibrahim 14:24 - Kanzul Iman)
    `<svg viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="g15" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#0a2e18"/>
          <stop offset="50%" stop-color="#011b09"/>
          <stop offset="100%" stop-color="#000d04"/>
        </linearGradient>
        <radialGradient id="noor" cx="50%" cy="30%" r="50%">
          <stop offset="0%" stop-color="#fff9c4" stop-opacity="0.95"/>
          <stop offset="60%" stop-color="#fbc02d" stop-opacity="0.6"/>
          <stop offset="100%" stop-color="#f57f17" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <rect width="72" height="72" rx="36" fill="url(#g15)"/>
      <circle cx="36" cy="22" r="28" fill="url(#noor)"/>
      <ellipse cx="36" cy="64" rx="27" ry="8" fill="#050201"/>
      <rect x="29" y="8" width="14" height="55" rx="7" fill="#110701"/>
      <ellipse cx="36" cy="6" rx="25" ry="17" fill="#001804"/>
      <ellipse cx="5" cy="13" rx="17" ry="11.5" fill="#032108" transform="rotate(-54 5 13)"/>
      <ellipse cx="67" cy="13" rx="17" ry="11.5" fill="#032108" transform="rotate(54 67 13)"/>
      <!-- Golden Jewels of Jannah Fruits -->
      <circle cx="12" cy="8" r="5.5" fill="#ffd700" stroke="#fff" stroke-width="0.8"/>
      <circle cx="60" cy="8" r="5.5" fill="#ffd700" stroke="#fff" stroke-width="0.8"/>
      <circle cx="36" cy="14" r="6.5" fill="#ffe082" stroke="#fff" stroke-width="1"/>
      <circle cx="22" cy="21" r="5" fill="#ffca28"/>
      <circle cx="50" cy="21" r="5" fill="#ffca28"/>
      <!-- Crown of Light (Surah Ibrahim 14:24) -->
      <path d="M36 0 L39 -4 L42 0 L39 4 Z" fill="#ffffff"/>
      <circle cx="36" cy="-2" r="2.5" fill="#fff59d"/>
      <circle cx="28" cy="1" r="1.8" fill="#ffffff" opacity="0.8"/>
      <circle cx="44" cy="1" r="1.8" fill="#ffffff" opacity="0.8"/>
    </svg>`
  ];

  return svgs[Math.min(stage, svgs.length - 1)];
}
"""

# ============================================================
# ===  365 DAYS DAILY SPIRITUAL THOUGHTS GENERATOR         ===
# ============================================================
# Themes: Tazkiyah, Nigah Ki Hifazat (Fatawa Razawiyyah),
# Ishq-e-Rasool (Al-Wazifatul Kareemah), Muraqabah, Sabr, Shukr, Tawakkul
def generate_365_daily_thoughts():
    """Generates 365 authentic daily reflections with citations from Kanzul Iman & Aala Hazrat."""
    core_quotes = [
      {
        "topic": "Nigah Ki Hifazat (Guarding the Gaze)",
        "quote": "Musalman mardon ko hukum do ke apni nigahein kuch neechi rakhein aur apni sharmgahon ki hifazat karein, yeh unke liye bohot suthra hai.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah An-Nur 24:30",
        "wisdom": "Aala Hazrat Fatawa Razawiyyah (Jild 22) mein farmate hain: Aankh dil ka darwaza hai. Jab nigaah haram se bach jaati hai toh dil mein Imaan ki meethas aur noor utar aata hai."
      },
      {
        "topic": "Taubah Aur Allah Ki Rahmat",
        "quote": "Tum farmao: Ae mere woh bando jinhone apni jaano par zyadati ki! Allah ki rehmat se na-ummeed na ho, beshak Allah sab gunaah bakhsh deta hai.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Az-Zumar 39:53",
        "wisdom": "Taubah ka matlab sirf zaban se kehna nahi, balki dil mein sharmindagi, gunah ko foran chhodna aur aainda na karne ka pukhta ahad karna hai."
      },
      {
        "topic": "Nafs-e-Ammara Ki Pehchan",
        "quote": "Beshak nafs toh buraayi hi ka bada hukum dene wala hai magar jis par mera Rab rahem farmaye.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Yusuf 12:53",
        "wisdom": "Nafs ka kaam waswasa daalna aur lutf ka lalach dena hai. Magar jab banda Durood Sharif aur Al-Wazifatul Kareemah ke azkaar karta hai toh nafs kamzor ho jata hai."
      },
      {
        "topic": "Sabr-o-Istiqamah Ka Inaam",
        "quote": "Aur jinhone hamari raah mein koshish ki, zaroor hum unhein apne raaste dikha denge, aur beshak Allah neko-kaaron ke saath hai.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Al-Ankabut 29:69",
        "wisdom": "Shahwat (lust) ki aag paani se nahi, balki khauf-e-Khuda aur zikr-e-Habib Sallallahu Alayhi wa Sallam se thandi hoti hai."
      },
      {
        "topic": "Durood Sharif Ki Barkat",
        "quote": "Beshak Allah aur uske farishte Durood bhejte hain us ghaib batane wale (Nabi) par. Ae imaan walo! Un par Durood aur khoob salaam bhejo.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Al-Ahzab 33:56",
        "wisdom": "Aala Hazrat farmate hain: Jo kasrat se Durood-e-Paak padhta hai, Allah Ta'ala uske dil ko waswaso aur gunaah ki gandagi se paak saaf farma deta hai."
      },
      {
        "topic": "Muraqabah-e-Ilahi (Allah Dekh Raha Hai)",
        "quote": "Kya usne na jana ke beshak Allah dekh raha hai?",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Al-Alaq 96:14",
        "wisdom": "Tanhai mein jab koi dekhne wala na ho, tab yeh sochna ke Allah Ta'ala ki zaat mujhe dekh rahi hai — yahi Ihsan aur Wilayat ki bunyaad hai."
      },
      {
        "topic": "Waswasa Ka Qil'a (Protection from Whispers)",
        "quote": "Tum farmao: Main logon ke rab ki panah maangta hoon... Us waswasa daalne wale ke shar se jo peechhe hat jata hai.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah An-Nas 114:1-4",
        "wisdom": "Al-Wazifatul Kareemah mein Aala Hazrat ne farmaya: Waswasa aate hi 'Amantu billahi wa rusulih' padho, shaitan zaleel hokar bhaag jata hai."
      },
      {
        "topic": "Dunya Ki Haqiqat Aur Paak Daman Zindagi",
        "quote": "Aur dunya ki zindagi toh sirf dhoke ka samaan hai.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Al-Hadid 57:20",
        "wisdom": "Chand minute ka haram lutf ghanto ki sharmindagi aur roohani andhera laata hai. Paak-daamani mein daimi sukoon aur chehre ka noor hai."
      },
      {
        "topic": "Dil Ka Sukoon",
        "quote": "Sun lo! Allah ki yaad hi mein dilon ka chain hai.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Ar-Ra'd 13:28",
        "wisdom": "Mobile ki screen par sakoon dhoondhne wala thak jayega. Dil ka sukoon sirf Sajdah aur Tilawat-e-Quran mein wadiat kiya gaya hai."
      },
      {
        "topic": "Shajarah-e-Tayyibah Ka Sabak",
        "quote": "Kya tumne na dekha Allah ne kaisi misal bayan farmai: Paakiza baat jaise paakiza darakht, jiski jad qaim aur shakhhein aasmaan mein.",
        "ref": "Tarjuma Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan) - Surah Ibrahim 14:24",
        "wisdom": "Apni rooh ko rozana Taubah, Zikr aur Durood ka paani do taake tumhara Tree of Faith 365 din mein Shajarah-e-Tayyibah ban jaye."
      }
    ]

    thoughts = []
    for day in range(1, 366):
        template = core_quotes[(day - 1) % len(core_quotes)]
        cycle_num = ((day - 1) // 30) + 1
        day_in_cycle = ((day - 1) % 30) + 1
        
        thought = {
            "day": day,
            "cycle": cycle_num,
            "topic": f"Day {day}: {template['topic']}",
            "quote": template["quote"],
            "ref": template["ref"],
            "wisdom": f"Cycle {cycle_num} (Day {day_in_cycle}/30): {template['wisdom']}"
        }
        thoughts.append(thought)
    
    return thoughts

DAILY_THOUGHTS_365 = generate_365_daily_thoughts()
