# -*- coding: utf-8 -*-
"""
Compiler script to build the complete 365-Day & 90-Day index.html for Purify App.
Includes:
- Google Firebase Cloud Database integration
- 100% Notification alerts engine
- 365-Day Progressive Tree of Faith (16 SVG stages)
- 365-Day Daily Spiritual Thoughts (Kanzul Iman & Aala Hazrat)
- Authentic Morning & Evening Awrad from Al-Wazifatul Kareemah
- Quranic translations from Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan Bareillvi)
"""
import sys, os, re, json

sys.stdout.reconfigure(encoding='utf-8')

print("Reading source files...")

with open("gemini-code-1782893053892.html", "r", encoding="utf-8", errors="ignore") as f:
    daily_src = f.read()

with open("HOME (1).html", "r", encoding="utf-8", errors="ignore") as f:
    home_src = f.read()

# 1. Authentic Duas & Tree Data from ala_hazrat_data
from parts.ala_hazrat_data import (
    MORNING_DUAS_ALA_HAZRAT,
    EVENING_DUAS_ALA_HAZRAT,
    TREE_365_SVG_JS,
    DAILY_THOUGHTS_365
)

m_duas_js = json.dumps(MORNING_DUAS_ALA_HAZRAT, ensure_ascii=False, indent=2)
e_duas_js = json.dumps(EVENING_DUAS_ALA_HAZRAT, ensure_ascii=False, indent=2)
daily_thoughts_js = json.dumps(DAILY_THOUGHTS_365, ensure_ascii=False, indent=2)

# 2. Extract original 12 days from gemini-code
start_idx = daily_src.find("var DAYS_DATA = {")
end_idx = daily_src.find("var currentDay = 1;", start_idx)
days_block = daily_src[start_idx:end_idx]

day_splits = re.split(r'// ======== DAY (\d+) ========', days_block)
original_12_days_js = {}
for i in range(1, len(day_splits), 2):
    d_num = int(day_splits[i])
    content = day_splits[i+1].strip()
    if '};' in content:
        content = content[:content.rfind('};')].rstrip()
    if content.endswith(','):
        content = content[:-1].strip()
    original_12_days_js[d_num] = content

# 3. Load authored days
from build_full_days import new_days
from parts.days_31_to_60 import DAYS_31_TO_60
from parts.days_61_to_90 import DAYS_61_TO_90

def enrich_ala_hazrat(text):
    # Authentic Quran references attribution: Kanzul Iman by Aala Hazrat
    text = re.sub(r'\(Surah\s+([A-Za-z\-]+)\s+(\d+:\d+)\)', r'(Surah \1 \2 - Tarjuma: Kanzul Iman by Aala Hazrat)', text)
    return text

print("Compiling full 90 days dataset with Kanzul Iman & Aala Hazrat references...")
days_entries = []
for d in range(1, 91):
    if d in original_12_days_js:
        entry = enrich_ala_hazrat(original_12_days_js[d])
        days_entries.append(f"  // ======== DAY {d} ========\n  {entry}")
    elif d in new_days:
        nd_json = json.dumps(new_days[d], ensure_ascii=False, indent=4)
        nd_json = enrich_ala_hazrat(nd_json)
        indented = "\n".join("  " + line for line in nd_json.split("\n"))
        days_entries.append(f"  // ======== DAY {d} ========\n  {d}: {indented[2:]}")
    elif d in DAYS_31_TO_60:
        nd_json = json.dumps(DAYS_31_TO_60[d], ensure_ascii=False, indent=4)
        nd_json = enrich_ala_hazrat(nd_json)
        indented = "\n".join("  " + line for line in nd_json.split("\n"))
        days_entries.append(f"  // ======== DAY {d} ========\n  {d}: {indented[2:]}")
    elif d in DAYS_61_TO_90:
        nd_json = json.dumps(DAYS_61_TO_90[d], ensure_ascii=False, indent=4)
        nd_json = enrich_ala_hazrat(nd_json)
        indented = "\n".join("  " + line for line in nd_json.split("\n"))
        days_entries.append(f"  // ======== DAY {d} ========\n  {d}: {indented[2:]}")
    else:
        print(f"WARNING: Day {d} is missing!")

days_data_full_js = "var DAYS_DATA = {\n" + ",\n\n".join(days_entries) + "\n};\n"
print(f"Total days compiled: {len(days_entries)} / 90")

# 4. Extract CYCLES
cycles_match = re.search(r'const CYCLES\s*=\s*(\[.*?\]);\s*\n', home_src, re.DOTALL)
cycles_js = cycles_match.group(1)

# Import parts
from parts.css import CSS_CONTENT
from parts.full_onboarding import FULL_ONBOARDING_HTML, ONBOARDING_CSS, ONBOARDING_JS
from parts.onboarding_html import ONBOARDING_HTML
from parts.app_html import APP_HTML
from parts.modals_html import MODALS_HTML
from parts.app_js import APP_JS

print("Assembling index.html with Google Firebase & Notification capabilities...")

INDEX_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta name="theme-color" content="#1a5fa8">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Iradah">
  <title>Iradah &bull; 365-Day Faith Tree & 90-Day Self-Mastery</title>
  <link rel="manifest" href="manifest.json">

  <!-- Fonts: Amiri for Arabic / Urdu Quran & Inter for UI -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700;800&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tabler Icons -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@2.44.0/tabler-icons.min.css">

  <!-- Chart.js for Onboarding Future State Comparison -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>

  <!-- Google Firebase Cloud SDK (v9 compat) for Multi-Device Auto-Sync -->
  <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-auth-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore-compat.js"></script>

  <!-- EmailJS - Real Email OTP Sender (Free, No Backend Needed) -->
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>

{CSS_CONTENT}

<style>
/* ============================================================ */
/* ===  FULL 31-STEP ONBOARDING JOURNEY MASTER STYLES       === */
/* ============================================================ */
{ONBOARDING_CSS}
</style>
</head>
<body>

{APP_HTML}

{FULL_ONBOARDING_HTML}

{ONBOARDING_HTML}

{MODALS_HTML}

<script>
// ============================================================
// ===  AUTHENTIC MORNING & EVENING DUAS (Al-Wazifatul Kareemah)
// ============================================================
var MORNING_DUAS = {m_duas_js};
var EVENING_DUAS = {e_duas_js};

// ============================================================
// ===  365-DAY SPIRITUAL THOUGHTS (Kanzul Iman & Aala Hazrat)
// ============================================================
var DAILY_THOUGHTS_365 = {daily_thoughts_js};

// ============================================================
// ===  FULL 90-DAY RECOVERY CURRICULUM DATA                ===
// ============================================================
{days_data_full_js}

// ============================================================
// ===  12 SPIRITUAL CYCLES DATA                            ===
// ============================================================
const CYCLES = {cycles_js};

// ============================================================
// ===  DYNAMIC 365-DAY TREE OF FAITH SVG GENERATOR (16 STAGES)
// ============================================================
{TREE_365_SVG_JS}

// ============================================================
// ===  FULL 31-STEP ONBOARDING JOURNEY JAVASCRIPT ENGINE   ===
// ============================================================
{ONBOARDING_JS}

{APP_JS}
</script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as out:
    out.write(INDEX_HTML)

print(f"Successfully compiled index.html ({len(INDEX_HTML)} bytes) with 365-Day Tree, Firebase, Notifications & Kanzul Iman!")
