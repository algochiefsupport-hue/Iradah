# -*- coding: utf-8 -*-

APP_HTML = """
<!-- ============================================================ -->
<!-- ===  MOBILE APP CONTAINER                                 === -->
<!-- ============================================================ -->
<div class="mobile-app-shell" id="appShell">

  <!-- Top App Bar -->
  <header class="app-top-bar" id="appTopBar">
    <div class="app-user-pill" onclick="openAuthModal()" id="headerUserPill" title="Account & Profile">
      <div class="sync-dot" id="headerSyncDot" style="background: #10b981;"></div>
      <span id="headerUserText">Sign In</span>
    </div>
    <div class="app-header-right">
      <!-- Notification Quick Bell -->
      <button class="notif-bell-btn" id="headerNotifBell" onclick="toggleNotificationPermission()" title="Enable Notifications">
        <i class="ti ti-bell-ringing"></i>
      </button>
      <div class="app-hearts" id="headerHearts" title="Repentance Lives">
        <span class="ht">❤️</span><span class="ht">❤️</span><span class="ht">❤️</span>
      </div>
      <div class="app-xp-pill" id="headerXpPill">
        <i class="ti ti-bolt"></i> Lv <span id="headerLv">1</span> &bull; <span id="headerXp">0</span> XP
      </div>
    </div>
  </header>

  <!-- Screens Viewport -->
  <main class="screens-viewport">

    <!-- ======================================================== -->
    <!-- TAB 1: HOME DASHBOARD                                    -->
    <!-- ======================================================== -->
    <section class="tab-screen active" id="tab-home">
      <!-- Header Gradient Card -->
      <div class="home-hdr-card">
        <!-- Faith / 365-Day Tree of Faith Card -->
        <div class="faith-card" onclick="switchTab('journey')">
          <div class="faith-tree-wrap">
            <div class="faith-tree-circle" id="homeTreeIcon">
              <!-- Dynamic 16-Stage SVG Tree will be injected here -->
            </div>
            <div class="faith-tree-lbl" id="homeTreeStage">Stage 0: Seed in Soil</div>
          </div>
          <div class="faith-text">
            <div class="faith-title">Tree of Faith &bull; 365 Days Journey</div>
            <div class="faith-quote" id="homeTreeRefl">"A good word is like a good tree, its root is firmly fixed and its branches reach to the sky."</div>
            <div class="faith-ref" id="homeTreeRef">Tarjuma Kanzul Iman &bull; Surah Ibrahim 14:24</div>
            <!-- Stage Milestone Progress -->
            <div style="margin-top: 8px;">
              <div style="display: flex; justify-content: space-between; font-size: 10.5px; opacity: 0.85; margin-bottom: 3px;">
                <span id="treeMilestoneTarget">Next: Stage 1 (Day 7)</span>
                <span id="treeMilestoneDays">0 / 7 Days</span>
              </div>
              <div class="streak-bar-bg" style="background: rgba(255,255,255,0.25); height: 4px;">
                <div class="streak-bar-fill" id="treeMilestoneBar" style="width: 5%; background: #ffd54f;"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Live Clean Streak Card -->
        <div class="streak-card">
          <div class="streak-header">
            <span class="streak-tag">Clean Streak</span>
            <span class="streak-progress-txt" id="homeCycleProg">Day 1 of 365 &bull; 1%</span>
          </div>
          <div class="streak-timer-row">
            <div class="timer-unit"><div class="timer-val" id="timer-d">00</div><div class="timer-lbl">Days</div></div>
            <div class="timer-sep">:</div>
            <div class="timer-unit"><div class="timer-val" id="timer-h">00</div><div class="timer-lbl">Hrs</div></div>
            <div class="timer-sep">:</div>
            <div class="timer-unit"><div class="timer-val" id="timer-m">00</div><div class="timer-lbl">Min</div></div>
            <div class="timer-sep">:</div>
            <div class="timer-unit"><div class="timer-val" id="timer-s">00</div><div class="timer-lbl">Sec</div></div>
          </div>
          <div class="streak-bar-bg">
            <div class="streak-bar-fill" id="homeDayBar" style="width: 3%;"></div>
          </div>
        </div>
      </div>

      <!-- Home Body -->
      <div class="home-body">

        <!-- 365-Day Daily Spiritual Thought Card -->
        <div class="daily-thought-card">
          <div class="daily-thought-hdr">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 18px;">✨</span>
              <span class="daily-thought-title">Daily Reflection &bull; Day <span id="thoughtDayDisplay">1</span> of 365</span>
            </div>
            <div style="display: flex; gap: 4px;">
              <button class="thought-nav-btn" onclick="prevDailyThought()" title="Previous Day"><i class="ti ti-chevron-left"></i></button>
              <button class="thought-nav-btn" onclick="nextDailyThought()" title="Next Day"><i class="ti ti-chevron-right"></i></button>
            </div>
          </div>
          <div class="daily-thought-topic" id="thoughtTopic">Guarding the Gaze (Hifazat-e-Nazar)</div>
          <div class="daily-thought-quote" id="thoughtQuote">"Tell the believing men to lower their gaze and guard their chastity. That is purer for them."</div>
          <div class="daily-thought-ref" id="thoughtRef">Tarjuma: Kanzul Iman (Imam Ahmad Raza Khan) &bull; Surah An-Nur 24:30</div>
          <div class="daily-thought-wisdom" id="thoughtWisdom">Imam Ahmad Raza Khan notes in Fatawa Razawiyyah: The eyes are the gateway to the heart. When the gaze is preserved from the forbidden, the heart is filled with the sweetness of faith.</div>
        </div>

        <!-- Weekly Interactive Check-In -->
        <div class="week-card">
          <div class="week-header">
            <button class="week-nav-btn" onclick="changeWeek(-1)"><i class="ti ti-chevron-left"></i></button>
            <h3 id="weekTitle">This Week</h3>
            <button class="week-nav-btn" id="btnNextWeek" onclick="changeWeek(1)" disabled><i class="ti ti-chevron-right"></i></button>
          </div>
          <div class="week-days-row" id="weekGrid">
            <!-- 7 Days Grid generated by JS -->
          </div>
          <div class="week-hint">Tap any past day to log your status</div>
        </div>

        <!-- Primary Action: Mark Clean -->
        <button class="home-action-btn btn-clean" id="btnMarkClean" onclick="markTodayClean()">
          <i class="ti ti-check"></i> <span>Mark Today as Clean</span>
        </button>

        <!-- Secondary Action: Log Relapse & Taubah -->
        <button class="home-action-btn btn-relapse" onclick="openRelapseModal()">
          <i class="ti ti-rotate-clockwise"></i> <span>Log a Slip & Renew Tawbah</span>
        </button>

        <!-- Emergency Urge Breaker Button (Home Page) -->
        <button class="home-urge-btn" onclick="openUrgeRescueModal()">
          <i class="ti ti-shield-half"></i> <span>Emergency Urge Breaker</span>
        </button>

      </div><!-- end .home-body -->
    </section>

    <!-- ======================================================== -->
    <!-- TAB 2: DAILY 90-DAY RECOVERY CURRICULUM                  -->
    <!-- ======================================================== -->
    <section class="tab-screen" id="tab-daily">
      <!-- Top Day Selector Bar -->
      <div class="daily-top-bar">
        <button class="day-nav-arrow" id="btnPrevDay" onclick="changeDailyDay(-1)"><i class="ti ti-chevron-left"></i></button>
        <div class="daily-day-indicator">
          <span class="day-badge-pill" id="dailyDayBadge">Day 1</span>
          <span class="day-cycle-label" id="dailyCycleBadge">Cycle 1 &bull; The Awakening</span>
        </div>
        <button class="day-nav-arrow" id="btnNextDay" onclick="changeDailyDay(1)"><i class="ti ti-chevron-right"></i></button>
      </div>

      <!-- Quick Day Slider -->
      <div class="day-slider-container">
        <input type="range" min="1" max="90" value="1" class="day-slider" id="daySlider" oninput="onDaySliderChange(this.value)">
        <div class="day-slider-marks">
          <span>Day 1</span>
          <span>Day 30</span>
          <span>Day 60</span>
          <span>Day 90</span>
        </div>
      </div>

      <!-- Day Content Scrollable Area -->
      <div class="daily-content-wrap" id="dailyContentWrap">

        <!-- 1. Daily Spiritual Practices Grid (Moved from Home Page) -->
        <div class="daily-rituals-sec" style="margin-bottom: 16px;">
          <div class="sec-hdr-row">
            <h3 class="sec-title" style="font-size: 15px;"><i class="ti ti-pray"></i> Daily Practices</h3>
            <span class="sec-badge" id="dailyPracticesBadge">0 / 3 Done</span>
          </div>

          <div class="rituals-grid">
            <!-- 1. Morning Adhkar (Al-Wazifatul Kareemah) -->
            <div class="ritual-card" id="cardRitualMorning" onclick="openMorningModal()">
              <div class="ritual-icon ri-morning"><i class="ti ti-sun"></i></div>
              <div class="ritual-info">
                <div class="ritual-title">Morning Adhkar</div>
                <div class="ritual-sub">Al-Wazifatul Kareemah &bull; +15 XP</div>
              </div>
              <div class="ritual-chk" id="chkRitualMorning"><i class="ti ti-check"></i></div>
            </div>

            <!-- 2. Evening Adhkar (Al-Wazifatul Kareemah) -->
            <div class="ritual-card" id="cardRitualEvening" onclick="openEveningModal()">
              <div class="ritual-icon ri-evening"><i class="ti ti-moon-stars"></i></div>
              <div class="ritual-info">
                <div class="ritual-title">Evening Adhkar</div>
                <div class="ritual-sub">Al-Wazifatul Kareemah &bull; +15 XP</div>
              </div>
              <div class="ritual-chk" id="chkRitualEvening"><i class="ti ti-check"></i></div>
            </div>

            <!-- 3. Renew Niyah (Intention) -->
            <div class="ritual-card" id="cardRitualNiyah" onclick="openNiyahModal()">
              <div class="ritual-icon ri-niyah"><i class="ti ti-feather"></i></div>
              <div class="ritual-info">
                <div class="ritual-title">Daily Intention (Niyyah)</div>
                <div class="ritual-sub">Renew commitment &bull; +10 XP</div>
              </div>
              <div class="ritual-chk" id="chkRitualNiyah"><i class="ti ti-check"></i></div>
            </div>
          </div>
        </div>

        <!-- 2. Section Header: Daily Recovery Lessons -->
        <div class="sec-hdr-row" style="margin-bottom: 10px;">
          <h3 class="sec-title" style="font-size: 15px;"><i class="ti ti-book-2"></i> Daily Modules</h3>
          <span class="sec-badge" id="dailyLessonsBadge">0 / 2 Completed</span>
        </div>

        <!-- Small Rectangular Style Tabs for Ibn Qayyim & Neuroscience -->
        <div class="module-rect-tabs-wrap">
          <!-- Rectangular Tab 1: Ibn Qayyim Purification -->
          <div class="module-rect-tab" id="rectTabIbn" onclick="openFullLessonModal('ibn')">
            <div class="module-rect-icon mri-ibn">
              <i class="ti ti-sparkles"></i>
            </div>
            <div class="module-rect-info">
              <div class="module-rect-tag-row">
                <span class="module-rect-tag mrt-ibn">Tazkiyah &bull; Ibn Qayyim</span>
                <span class="module-rect-readtime"><i class="ti ti-clock"></i> 4 min read</span>
              </div>
              <div class="module-rect-title" id="dailyIbnTitle">Purification Lesson</div>
            </div>
            <div class="module-rect-status-badge status-badge-pending" id="badgeIbnStatus">
              <span>Read & Reflect</span> <i class="ti ti-chevron-right"></i>
            </div>
          </div>

          <!-- Rectangular Tab 2: Neuroscience Module -->
          <div class="module-rect-tab" id="rectTabNeuro" onclick="openFullLessonModal('bf')">
            <div class="module-rect-icon mri-neuro">
              <i class="ti ti-brain"></i>
            </div>
            <div class="module-rect-info">
              <div class="module-rect-tag-row">
                <span class="module-rect-tag mrt-neuro">Neuroscience &bull; Rewiring</span>
                <span class="module-rect-readtime"><i class="ti ti-clock"></i> 3 min read</span>
              </div>
              <div class="module-rect-title" id="dailyBfTitle">Brain Rewiring Lesson</div>
            </div>
            <div class="module-rect-status-badge status-badge-pending" id="badgeNeuroStatus">
              <span>Read & Reflect</span> <i class="ti ti-chevron-right"></i>
            </div>
          </div>
        </div>

        <!-- 3. Module 3: Daily Action Step / Reminder (No writing needed) -->
        <div class="reminder-card" id="cardModuleDr" style="margin-top: 6px;">
          <div class="reminder-hdr">
            <i class="ti ti-bulb" style="color: #f59e0b; font-size: 22px;"></i>
            <span class="reminder-title" id="dailyDrTitle">Today's Action Reminder</span>
          </div>
          <div class="reminder-body" id="dailyDrText" style="font-size: 13.5px; line-height: 1.6; color: #334155;">
            Action reminder content...
          </div>
        </div>

      </div><!-- end .daily-content-wrap -->
    </section>

    <!-- ======================================================== -->
    <!-- TAB 3: JOURNEY & 12 SPIRITUAL CYCLES                     -->
    <!-- ======================================================== -->
    <section class="tab-screen" id="tab-journey">
      <div class="journey-hdr">
        <h2 class="journey-title">The 12 Spiritual Cycles</h2>
        <p class="journey-sub">90 days of transformation &bull; From battle to lifelong purity</p>
      </div>

      <!-- 365 Days Faith Tree Showcase Card -->
      <div class="journey-tree-showcase">
        <div style="display: flex; align-items: center; gap: 14px;">
          <div class="faith-tree-circle" id="journeyTreeIcon" style="width: 72px; height: 72px;">
            <!-- Tree SVG -->
          </div>
          <div>
            <div style="font-size: 15px; font-weight: 800; color: #1e293b;" id="journeyTreeStageTitle">Stage 0: Seed in Soil</div>
            <div style="font-size: 12px; color: #64748b; margin-top: 2px;">Tree of Faith &bull; 365 Days Progression</div>
            <div style="font-size: 11px; color: #166534; font-weight: 700; margin-top: 4px;" id="journeyCleanDaysText">0 Clean Days Logged</div>
          </div>
        </div>
      </div>

      <!-- Cycles List -->
      <div class="cycles-list" id="cyclesList">
        <!-- 12 Cycles Rendered by JS -->
      </div>
    </section>

    <!-- ======================================================== -->
    <!-- TAB 4: BROTHERHOOD COMMUNITY (ANONYMOUS)                 -->
    <!-- ======================================================== -->
    <section class="tab-screen" id="tab-community" style="display: flex; flex-direction: column; overflow: hidden;">
      <div class="community-hdr">
        <h2><i class="ti ti-users"></i> Recovery Brotherhood</h2>
        <p>Anonymous Spiritual Community &bull; You are not alone</p>
      </div>

      <!-- Identity Privacy Notice Banner -->
      <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 12px 14px; margin: 12px 14px; border-radius: 8px; font-size: 12px; color: #1e40af; line-height: 1.45;">
        <div style="font-weight: 700; margin-bottom: 2px;">🛡️ 100% Anonymous & Protected Identity</div>
        In this community, your real identity, email, and personal name are strictly hidden. You post under a randomly assigned spiritual alias (e.g. <b><span id="commAliasDisplay">Warrior #482</span></b>) so you can share and ask questions with full modesty (Haya) and dignity.
      </div>

      <!-- Quick New Post Box -->
      <div style="background: #ffffff; border-radius: 16px; padding: 14px; margin: 0 14px 14px; border: 1.5px solid var(--border); box-shadow: var(--shadow);">
        <textarea id="communityPostInput" class="journal-textarea" style="min-height: 70px; margin-bottom: 8px;" placeholder="Share your victory, ask for dua, or encourage your brothers..."></textarea>
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 11px; color: #64748b;">Posting as: <b id="commPostingAs">Anonymous Brother</b></span>
          <button class="btn-read-lesson" onclick="submitCommunityPost()" style="padding: 7px 16px; font-size: 12.5px;">Post to Brotherhood</button>
        </div>
      </div>

      <!-- Community Feed -->
      <div id="communityFeedList" style="padding: 0 14px 90px; flex: 1; overflow-y: auto; -webkit-overflow-scrolling: touch;">
        <!-- Live posts rendered here -->
      </div>
    </section>

    <!-- ======================================================== -->
    <!-- TAB 5: SETTINGS & ACCOUNT                                 -->
    <!-- ======================================================== -->
    <section class="tab-screen" id="tab-settings">
      <div class="settings-hdr">
        <h2>Settings & Account</h2>
      </div>
      <div class="settings-body">

        <!-- User Profile Card -->
        <div class="profile-card">
          <div class="profile-avatar"><i class="ti ti-user"></i></div>
          <div class="profile-info">
            <div class="profile-email" id="settingsUserEmail">Guest User</div>
            <div class="profile-sync-badge">
              <span class="sync-dot" id="settingsSyncDot" style="background: #10b981;"></span>
              <span id="settingsSyncText">Backup & Sync Active</span>
            </div>
          </div>
          <button class="week-nav-btn" onclick="openAuthModal()" style="font-size: 13px; font-weight: 700; color: var(--primary);">
            Account
          </button>
        </div>

        <!-- Notifications Section -->
        <div class="settings-sec-title">Notifications</div>
        <div class="settings-item" onclick="toggleNotificationPermission()">
          <div class="settings-item-left">
            <i class="ti ti-bell-ringing" style="color: #0284c7; font-size: 22px;"></i>
            <div>
              <div class="settings-item-title">Daily Reminders</div>
              <div class="settings-item-sub" id="settingsNotifStatus">
                Morning, Evening, and Reflection check-in alerts
              </div>
            </div>
          </div>
          <span class="sec-badge" id="settingsNotifBadge" style="background: #e0f2fe; color: #0284c7;">Active</span>
        </div>

        <div class="settings-item" onclick="sendTestNotification()">
          <div class="settings-item-left">
            <i class="ti ti-device-mobile-message" style="color: #10b981;"></i>
            <div>
              <div class="settings-item-title">Send Test Notification</div>
              <div class="settings-item-sub">Verify alert and vibration on this device</div>
            </div>
          </div>
          <i class="ti ti-chevron-right" style="color: #94a3b8;"></i>
        </div>

        <!-- Recovery Journey Tools -->
        <div class="settings-sec-title">Recovery Tools</div>
        <div class="settings-item" onclick="useRepentanceLife()">
          <div class="settings-item-left">
            <i class="ti ti-heart-plus"></i>
            <div>
              <div class="settings-item-title">Use Repentance Life</div>
              <div class="settings-item-sub">Preserve your streak without resetting (<span id="settingsLivesCount">3</span> remaining)</div>
            </div>
          </div>
          <i class="ti ti-chevron-right" style="color: #94a3b8;"></i>
        </div>

        <div class="settings-item" onclick="openFullOnboardingJourney()">
          <div class="settings-item-left">
            <i class="ti ti-checklist"></i>
            <div>
              <div class="settings-item-title">Retake Onboarding Journey</div>
              <div class="settings-item-sub">Experience the 31-step recovery onboarding again</div>
            </div>
          </div>
          <i class="ti ti-chevron-right" style="color: #94a3b8;"></i>
        </div>

        <div class="settings-item" onclick="confirmFullReset()">
          <div class="settings-item-left">
            <i class="ti ti-refresh" style="color: var(--red);"></i>
            <div>
              <div class="settings-item-title" style="color: var(--red);">Reset Streak Counter</div>
              <div class="settings-item-sub">Restart streak timer from Day 1</div>
            </div>
          </div>
          <i class="ti ti-chevron-right" style="color: #94a3b8;"></i>
        </div>

        <!-- Authentic Scholarly Attribution -->
        <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 14px; margin-top: 20px; font-size: 11.5px; color: #475569; line-height: 1.5;">
          <div style="font-weight: 700; color: #0f172a; margin-bottom: 4px;">
            Scholarly References:
          </div>
          Quranic translations from <b>Kanzul Iman</b> by Imam Ahmad Raza Khan Bareillvi.
          Morning & Evening Awrad from <b>Al-Wazifatul Kareemah</b>.
        </div>

        <div style="text-align: center; font-size: 11.5px; color: #94a3b8; margin: 20px 0 10px;">
          Iradah &bull; 90-Day Self-Mastery &bull; 365-Day Faith Tree
        </div>
      </div>
    </section>

  </main>

  <!-- Bottom Navigation Bar -->
  <nav class="bottom-nav" id="bottomNav">
    <div class="bnav-item active" id="bnav-home" onclick="switchTab('home')">
      <i class="ti ti-home"></i>
      <span>Home</span>
    </div>
    <div class="bnav-item" id="bnav-daily" onclick="switchTab('daily')">
      <i class="ti ti-calendar"></i>
      <span>Daily</span>
    </div>
    <div class="bnav-item" id="bnav-journey" onclick="switchTab('journey')">
      <i class="ti ti-growth"></i>
      <span>Journey</span>
    </div>
    <div class="bnav-item" id="bnav-community" onclick="switchTab('community')">
      <i class="ti ti-users"></i>
      <span>Community</span>
    </div>
    <div class="bnav-item" id="bnav-settings" onclick="switchTab('settings')">
      <i class="ti ti-settings"></i>
      <span>Settings</span>
    </div>
  </nav>

</div><!-- end .mobile-app-shell -->
"""
