# -*- coding: utf-8 -*-

MODALS_HTML = """
<!-- ============================================================ -->
<!-- ===  MODALS & OVERLAYS                                     === -->
<!-- ============================================================ -->

<!-- 1. Email Sign In Modal -->
<div class="modal-overlay" id="authModal" onclick="closeBgModal(event, 'authModal')">
  <div class="modal-sheet">
    <div class="sheet-drag"></div>
    <div class="sheet-hdr">
      <div class="sheet-title" id="authModalTitle">Sign In / Create Account</div>
      <button class="sheet-close-btn" onclick="closeModal('authModal')"><i class="ti ti-x"></i></button>
    </div>
    <div style="font-size: 13px; color: #64748b; margin-bottom: 16px; line-height: 1.5;" id="authModalDesc">
      Enter your email & secure PIN to save and restore your recovery journey on any device.
    </div>

    <!-- Toggle Login / Register / Forgot -->
    <div id="authTabGroup" style="display: flex; background: #f1f5f9; border-radius: 10px; padding: 3px; margin-bottom: 14px;">
      <button type="button" id="authTabLogin" onclick="switchAuthTab('login')" style="flex: 1; padding: 7px; border: none; border-radius: 8px; font-size: 13px; font-weight: 700; background: #fff; color: #1a5fa8; cursor: pointer;">Sign In</button>
      <button type="button" id="authTabRegister" onclick="switchAuthTab('register')" style="flex: 1; padding: 7px; border: none; border-radius: 8px; font-size: 13px; font-weight: 700; background: transparent; color: #64748b; cursor: pointer;">New Account</button>
    </div>

    <!-- Form 1: Login & Register Form -->
    <div id="authMainForm">
      <div class="auth-input-group" id="authNameGroup" style="display: none;">
        <label class="auth-label">Your Name</label>
        <input type="text" class="auth-input" id="authNameInput" placeholder="e.g. Abdullah">
      </div>

      <div class="auth-input-group">
        <label class="auth-label">Email Address</label>
        <input type="email" class="auth-input" id="authEmailInput" placeholder="your.email@example.com">
      </div>

      <div class="auth-input-group">
        <label class="auth-label">Password / PIN (Min 4 chars)</label>
        <input type="password" class="auth-input" id="authPasswordInput" placeholder="••••••••">
        <div id="authForgotLinkRow" style="display: flex; justify-content: flex-end; margin-top: 5px;">
          <button type="button" onclick="switchAuthTab('forgot')" style="background:none; border:none; color:#1a5fa8; font-size:12px; font-weight:700; cursor:pointer; text-decoration:underline;">Forgot Password / PIN?</button>
        </div>
      </div>

      <!-- Security Question for Registration (Recovery) -->
      <div id="authSecurityGroup" style="display: none; margin-bottom: 14px;">
        <label class="auth-label">Security Question (For Password Recovery)</label>
        <select class="auth-input" id="authSecurityQuestion" style="background: #fff; cursor: pointer; margin-bottom: 8px;">
          <option value="city">What is your birth city?</option>
          <option value="nickname">What was your childhood nickname?</option>
          <option value="book">What is your favorite Islamic book?</option>
          <option value="mother">What is your mother's first name?</option>
        </select>
        <label class="auth-label">Security Answer</label>
        <input type="text" class="auth-input" id="authSecurityAnswer" placeholder="Your secret answer">
      </div>

      <button class="auth-submit-btn" id="authSubmitBtn" onclick="submitEmailAuth()" style="margin-top: 6px;">
        Sign In
      </button>

      <div style="text-align: center; margin-top: 14px;">
        <button class="week-nav-btn" onclick="continueAsGuest()" style="font-size: 13px; color: #64748b;">
          Continue as Guest (Offline)
        </button>
      </div>
    </div>

    <!-- Form 2: Forgot Password - Email OTP (Secure) -->
    <div id="authForgotForm" style="display: none;">

      <!-- Step 1: Enter Email -->
      <div id="otpStep1">
        <div style="font-size: 13px; color: #475569; margin-bottom: 16px; line-height: 1.5;">
          Enter your registered email. A <strong>6-digit OTP</strong> will be sent directly to your inbox — secure and private.
        </div>
        <div class="auth-input-group">
          <label class="auth-label"><i class="ti ti-mail"></i> Registered Email Address</label>
          <input type="email" class="auth-input" id="authForgotEmailInput" placeholder="your.email@example.com">
        </div>
        <div id="otpSendError" style="display:none; color:#dc2626; font-size:12px; margin-bottom:10px; padding: 8px 12px; background:#fef2f2; border-radius:8px;"></div>
        <button type="button" class="auth-submit-btn" id="btnSendOtp" onclick="sendEmailOTP()" style="background: linear-gradient(135deg, #1a5fa8, #0284c7);">
          <i class="ti ti-send"></i> Send OTP to My Email
        </button>
        <div style="text-align:center; margin-top:10px; font-size:11.5px; color:#94a3b8;">
          <i class="ti ti-lock"></i> OTP expires in 10 minutes &bull; Sent only to your email
        </div>
      </div>

      <!-- Step 2: Enter OTP + New Password -->
      <div id="otpStep2" style="display:none;">
        <div style="background: #ecfdf5; border: 1.5px solid #10b981; border-radius: 10px; padding: 12px; margin-bottom: 14px;">
          <div style="font-size: 12.5px; font-weight: 700; color: #065f46; margin-bottom: 3px;">
            <i class="ti ti-mail-check"></i> OTP Sent Successfully!
          </div>
          <div style="font-size: 11.5px; color: #047857;" id="otpSentToMsg">
            Check your email inbox (and Spam folder).
          </div>
        </div>
        <div class="auth-input-group">
          <label class="auth-label"><i class="ti ti-numbers"></i> Enter 6-Digit OTP Code</label>
          <input type="number" class="auth-input" id="authForgotOtpInput" placeholder="e.g. 284739" maxlength="6" style="letter-spacing: 4px; font-size: 20px; font-weight: 700; text-align: center;">
        </div>
        <div class="auth-input-group">
          <label class="auth-label"><i class="ti ti-lock"></i> New Password / PIN (Min 4 chars)</label>
          <input type="password" class="auth-input" id="authForgotNewPwd" placeholder="••••••••">
        </div>
        <div id="otpVerifyError" style="display:none; color:#dc2626; font-size:12px; margin-bottom:10px; padding: 8px 12px; background:#fef2f2; border-radius:8px;"></div>
        <button type="button" class="auth-submit-btn" onclick="verifyEmailOTP()" style="background: linear-gradient(135deg, #10b981, #059669);">
          <i class="ti ti-shield-check"></i> Verify OTP & Reset Password
        </button>
        <div style="text-align:center; margin-top:10px;">
          <button type="button" onclick="resendOTP()" style="background:none; border:none; color:#1a5fa8; font-size:12px; font-weight:700; cursor:pointer; text-decoration:underline;">
            <i class="ti ti-refresh"></i> Resend OTP
          </button>
        </div>
      </div>

      <!-- Step 3: Success -->
      <div id="otpStep3" style="display:none; text-align:center; padding: 10px 0;">
        <div style="font-size: 48px; margin-bottom: 10px;">✅</div>
        <div style="font-size: 16px; font-weight: 800; color: #10b981; margin-bottom: 6px;">Password Reset!</div>
        <div style="font-size: 13px; color: #64748b; margin-bottom: 18px;">Your new password has been saved. You can now sign in.</div>
        <button type="button" class="auth-submit-btn" onclick="switchAuthTab('login')" style="background: linear-gradient(135deg, #1a5fa8, #0284c7);">
          Sign In Now
        </button>
      </div>

      <div style="text-align: center; margin-top: 14px;" id="otpBackRow">
        <button type="button" onclick="switchAuthTab('login')" class="week-nav-btn" style="font-size: 13px; color: #1a5fa8; font-weight: 700;">
          &larr; Back to Sign In
        </button>
      </div>
    </div></div>

  </div>
</div>

<!-- ============================================================ -->
<!-- ===  EMERGENCY URGE BREAKER MODAL                        === -->
<!-- ============================================================ -->
<div class="modal-overlay" id="urgeModal" onclick="closeBgModal(event, 'urgeModal')">
  <div class="modal-sheet" style="max-height: 88vh; overflow-y: auto;">
    <div class="sheet-drag"></div>
    <div class="sheet-hdr">
      <div>
        <div class="sheet-title" style="color: #dc2626;"><i class="ti ti-shield-half"></i> Emergency Urge Breaker</div>
        <div style="font-size: 11.5px; color: #64748b;">Take refuge in Allah & cool the dopamine rush immediately.</div>
      </div>
      <button class="sheet-close-btn" onclick="closeModal('urgeModal')"><i class="ti ti-x"></i></button>
    </div>

    <!-- 4-7-8 Breathing Tool -->
    <div class="tool-card" style="margin-top: 10px;">
      <div class="tool-title"><i class="ti ti-wind"></i> 4-7-8 Parasympathetic Breathing</div>
      <div class="tool-sub">Inhale 4s, Hold 7s, Exhale 8s to calm the prefrontal cortex</div>
      <div class="breath-widget">
        <div class="breath-circle" id="breathCircle">
          <span id="breathText">Ready</span>
        </div>
        <button class="breath-ctrl-btn" id="btnBreathToggle" onclick="toggleBreathing()">Start Breathing</button>
      </div>
    </div>

    <!-- Interactive 33-Count Tasbeeh Counter -->
    <div class="tool-card">
      <div class="tool-title"><i class="ti ti-fingerprint"></i> 33-Count Electronic Tasbeeh Ring</div>
      <div class="tool-sub">Tap the button to make dhikr. Shift attention to the Divine.</div>
      <div class="tasbeeh-widget">
        <div class="tasbeeh-phrase" id="tasbeehPhrase">SubhanAllah</div>
        <div class="tasbeeh-trans" id="tasbeehTrans">Glory be to Allah</div>
        <button class="tasbeeh-ring-btn" onclick="tapTasbeehRing()">
          <span class="tasbeeh-count" id="tasbeehCount">0</span>
          <span class="tasbeeh-lbl">TAP / ذكر</span>
        </button>
        <div style="display: flex; gap: 8px; margin-top: 10px;">
          <button class="week-nav-btn" onclick="nextTasbeehPhrase()" style="font-size: 12px;">Change Dhikr &rarr;</button>
          <button class="week-nav-btn" onclick="resetTasbeeh()" style="font-size: 12px;">Reset</button>
        </div>
      </div>
    </div>

    <!-- Quranic Refuge Card (Kanzul Iman) -->
    <div class="tool-card" style="background: linear-gradient(135deg, #064e3b 0%, #047857 100%); color: #fff;">
      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; opacity: 0.85;">Quranic Shield &bull; Panah-e-Ilahi</div>
      <div style="font-family: 'Amiri', serif; font-size: 19px; line-height: 1.8; text-align: center; margin: 10px 0;">
        وَإِمَّا يَنزَغَنَّكَ مِنَ الشَّيْطَانِ نَزْغٌ فَاسْتَعِذْ بِاللَّهِ ۖ إِنَّهُ هُوَ السَّمِيعُ الْعَلِيمُ
      </div>
      <div style="font-size: 12.5px; line-height: 1.5; font-style: italic; opacity: 0.95; text-align: center;">
        "And if a whisper from Satan touches you, seek refuge in Allah. Indeed, He is the Hearing, the Knowing."
      </div>
      <div style="font-size: 11px; text-align: center; opacity: 0.8; margin-top: 6px;">
        Tarjuma: Kanzul Iman (Imam Ahmad Raza Khan) &bull; Surah Fussilat 41:36
      </div>
    </div>

    <!-- Aala Hazrat Prescribed Dua for Urges -->
    <div class="tool-card" style="background: #f8fafc;">
      <div style="font-size: 12px; font-weight: 700; color: #0284c7;">Al-Wazifatul Kareemah &bull; Protection from Desires</div>
      <div style="font-family: 'Amiri', serif; font-size: 18px; line-height: 1.7; margin: 8px 0; color: #0f172a;">
        آمَنْتُ بِاللّٰهِ وَرُسُلِهِ، هُوَ الْاَوَّلُ وَالْاٰخِرُ وَالظَّاهِرُ وَالْباطِنُ وَهُوَ بِكُلِّ شَيْءٍ عَلِيْمٌ
      </div>
      <div style="font-size: 12px; color: #475569; line-height: 1.45;">
        Recite three times whenever temptation strikes, and blow over your chest for spiritual tranquility.
      </div>
    </div>

  </div>
</div>

<!-- 2. Morning Adhkar Modal -->
<div class="modal-overlay" id="morningModal" onclick="closeBgModal(event, 'morningModal')">
  <div class="modal-sheet">
    <div class="sheet-drag"></div>
    <div class="sheet-hdr">
      <div>
        <div class="sheet-title">Morning Adhkar &bull; أذكار الصباح</div>
        <div style="font-size: 11px; color: #0284c7; font-weight: 600; margin-top: 2px;">
          From Al-Wazifatul Kareemah (Imam Ahmad Raza Khan) &bull; Kanzul Iman
        </div>
      </div>
      <button class="sheet-close-btn" onclick="closeModal('morningModal')"><i class="ti ti-x"></i></button>
    </div>
    <div style="font-size: 12.5px; color: #64748b; margin-bottom: 14px;">
      Recite each supplication and tap to complete. Strengthen your spiritual fortress for the day.
    </div>
    <div id="morningDuaList"></div>
    <button class="home-action-btn btn-clean" id="btnCompleteMorning" onclick="completeAdhkar('morning')" style="margin-top: 14px;">
      Complete Morning Duas (+10 XP)
    </button>
  </div>
</div>

<!-- 3. Evening Adhkar Modal -->
<div class="modal-overlay" id="eveningModal" onclick="closeBgModal(event, 'eveningModal')">
  <div class="modal-sheet">
    <div class="sheet-drag"></div>
    <div class="sheet-hdr">
      <div>
        <div class="sheet-title">Evening Adhkar &bull; أذكار المساء</div>
        <div style="font-size: 11px; color: #0284c7; font-weight: 600; margin-top: 2px;">
          From Al-Wazifatul Kareemah (Imam Ahmad Raza Khan) &bull; Kanzul Iman
        </div>
      </div>
      <button class="sheet-close-btn" onclick="closeModal('eveningModal')"><i class="ti ti-x"></i></button>
    </div>
    <div style="font-size: 12.5px; color: #64748b; margin-bottom: 14px;">
      Evening supplications to shield your heart and protect against evening triggers and whispers.
    </div>
    <div id="eveningDuaList"></div>
    <button class="home-action-btn btn-clean" id="btnCompleteEvening" onclick="completeAdhkar('evening')" style="margin-top: 14px;">
      Complete Evening Duas (+10 XP)
    </button>
  </div>
</div>

<!-- 4. Interactive Lesson Reader Modal -->
<div class="modal-overlay" id="lessonModal" onclick="closeBgModal(event, 'lessonModal')">
  <div class="modal-sheet lesson-sheet" id="lessonSheet">
    <div class="sheet-drag" style="background: rgba(255,255,255,0.2);"></div>
    <div class="sheet-hdr" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span class="sheet-title" id="lessonModalTitle" style="color: #fff; font-size: 16px;">Lesson</span>
      </div>
      <button class="sheet-close-btn" style="background: rgba(255,255,255,0.1); color: #fff;" onclick="closeModal('lessonModal')">
        <i class="ti ti-x"></i>
      </button>
    </div>

    <!-- Slide Content Container -->
    <div id="lessonContentContainer" style="padding-top: 10px;">
      <!-- Dynamic slide content rendered by JS -->
    </div>

    <!-- Required Reflection Input Box -->
    <div id="lessonReflectionSection" style="margin: 14px 0 6px; padding: 14px; background: rgba(255,255,255,0.08); border: 1.5px solid rgba(255,255,255,0.18); border-radius: 14px;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
        <div style="font-weight: 700; font-size: 13.5px; color: #fff; display: flex; align-items: center; gap: 6px;">
          <i class="ti ti-pencil" style="color: #38bdf8;"></i> <span>Your Reflection (Required to Complete)</span>
        </div>
        <span style="font-size: 11px; color: #fbbf24; font-weight: 700; background: rgba(251,191,36,0.15); padding: 2px 7px; border-radius: 6px;">+25 XP</span>
      </div>
      <div style="font-size: 11.5px; color: rgba(255,255,255,0.7); margin-bottom: 8px; line-height: 1.4;">
        Writing engages your prefrontal cortex. Write at least 1 takeaway or commitment from this lesson to mark it complete:
      </div>
      <textarea id="lessonReflectionInput" style="width: 100%; min-height: 72px; background: rgba(0,0,0,0.3); border: 1.5px solid rgba(255,255,255,0.22); border-radius: 10px; padding: 10px; color: #fff; font-size: 13px; font-family: inherit; resize: vertical; box-sizing: border-box;" placeholder="What did you learn? How will you apply this today? (min 5 characters)..." oninput="onLessonReflectionInput()"></textarea>
      <div id="lessonReflectionError" style="display: none; color: #fca5a5; font-size: 12px; margin-top: 6px; font-weight: 600;">
        ⚠️ Please write your reflection above before marking this lesson complete.
      </div>
    </div>

    <!-- Navigation Buttons -->
    <div class="lesson-nav-row" style="margin-top: 10px;">
      <button class="lesson-btn lesson-btn-prev" id="btnLessonPrev" onclick="lessonPrevSlide()">
        &larr; Previous
      </button>
      <div style="font-size: 12px; color: rgba(255,255,255,0.6);" id="lessonSlideIndicator">
        Slide 1 of 3
      </div>
      <button class="lesson-btn lesson-btn-next" id="btnLessonNext" onclick="lessonNextSlide()">
        Next &rarr;
      </button>
    </div>
  </div>
</div>

<!-- 5. Relapse Logger Modal with 3 Lives Shield System -->
<div class="modal-overlay" id="relapseModal" onclick="closeBgModal(event, 'relapseModal')">
  <div class="modal-sheet">
    <div class="sheet-drag"></div>
    <div class="sheet-hdr">
      <div class="sheet-title" style="color: var(--red);">
        <i class="ti ti-alert-circle"></i> Log a Slip & Renew Tawbah
      </div>
      <button class="sheet-close-btn" onclick="closeModal('relapseModal')"><i class="ti ti-x"></i></button>
    </div>
    <div style="font-size: 13px; color: #64748b; margin-bottom: 12px; line-height: 1.45;">
      Honesty is the foundation of lasting freedom. A stumble is an opportunity to learn what boundary was crossed and fortify your defenses.
    </div>

    <!-- 3 Lives / Repentance Shield Status Box -->
    <div class="relapse-shield-box" id="relapseShieldBox" style="background: #fef2f2; border: 1.5px solid #fecaca; border-radius: 14px; padding: 14px; margin-bottom: 14px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-weight: 700; font-size: 13.5px; color: #991b1b;"><i class="ti ti-shield-heart"></i> Repentance Shield</span>
        <span id="relapseModalLivesDisplay" style="font-size: 16px; letter-spacing: 2px;">💖 💖 💖</span>
      </div>
      <div style="font-size: 12px; color: #7f1d1d; line-height: 1.45;" id="relapseShieldMsg">
        You have 3 Lives remaining. You can sacrifice 1 Life to shield your clean streak while making sincere Tawbah!
      </div>
    </div>

    <div class="auth-label">What triggered this slip? (Select all that apply)</div>
    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 14px;" id="relapseTriggersGrid">
      <button class="ob-opt-btn" style="width: auto; padding: 6px 14px; font-size: 12.5px; margin: 0;" onclick="toggleTrigger(this)">Boredom</button>
      <button class="ob-opt-btn" style="width: auto; padding: 6px 14px; font-size: 12.5px; margin: 0;" onclick="toggleTrigger(this)">Late Night Alone</button>
      <button class="ob-opt-btn" style="width: auto; padding: 6px 14px; font-size: 12.5px; margin: 0;" onclick="toggleTrigger(this)">Stress / Anxiety</button>
      <button class="ob-opt-btn" style="width: auto; padding: 6px 14px; font-size: 12.5px; margin: 0;" onclick="toggleTrigger(this)">Social Media Scrolling</button>
      <button class="ob-opt-btn" style="width: auto; padding: 6px 14px; font-size: 12.5px; margin: 0;" onclick="toggleTrigger(this)">Loneliness</button>
      <button class="ob-opt-btn" style="width: auto; padding: 6px 14px; font-size: 12.5px; margin: 0;" onclick="toggleTrigger(this)">Fatigue</button>
    </div>

    <div class="auth-label">Reflection & Next Steps</div>
    <textarea class="auth-input" id="relapseNotesInput" style="min-height: 70px; margin-bottom: 16px;" placeholder="What were you feeling right before this occurred? What rule or boundary will you set?"></textarea>

    <!-- Action Buttons: Shield vs Full Reset -->
    <div id="relapseActionButtons" style="display: flex; flex-direction: column; gap: 10px;">
      <button class="home-action-btn" id="btnUseShield" style="background: linear-gradient(135deg, #10b981, #059669); color: #fff; margin: 0; box-shadow: 0 4px 12px rgba(16,185,129,0.3);" onclick="submitRelapseWithShield()">
        <i class="ti ti-shield-check"></i> <span id="btnUseShieldText">Use 1 Life to Shield Streak</span>
      </button>

      <button class="home-action-btn" id="btnResetTimer" style="background: #f8fafc; color: #475569; border: 1.5px solid #cbd5e1; margin: 0;" onclick="submitRelapseFullReset()">
        <i class="ti ti-rotate-clockwise"></i> <span>Reset Streak to Day 1 (Keep Remaining Lives)</span>
      </button>
    </div>
  </div>
</div>

<!-- 6. Set Niyah (Intention) Modal -->
<div class="modal-overlay" id="niyahModal" onclick="closeBgModal(event, 'niyahModal')">
  <div class="modal-sheet">
    <div class="sheet-drag"></div>
    <div class="sheet-hdr">
      <div class="sheet-title">Renew Daily Intention (Niyyah)</div>
      <button class="sheet-close-btn" onclick="closeModal('niyahModal')"><i class="ti ti-x"></i></button>
    </div>
    <div style="font-size: 13px; color: #64748b; margin-bottom: 14px; line-height: 1.45;">
      Actions are judged by intentions. Renew your intention today to guard your eyes, mind, and heart purely for Allah.
    </div>
    <textarea class="auth-input" id="niyahTextInput" style="min-height: 100px; margin-bottom: 16px;" placeholder="In the name of Allah, today I intend to protect my gaze, purify my heart, and seek Allah's pleasure through discipline..."></textarea>
    <button class="home-action-btn btn-clean" onclick="submitNiyah()">
      Save Intention
    </button>
  </div>
</div>

<!-- 7. Day Edit Calendar Sheet -->
<div class="modal-overlay" id="dayEditModal" onclick="closeBgModal(event, 'dayEditModal')">
  <div class="modal-sheet">
    <div class="sheet-drag"></div>
    <div class="sheet-hdr">
      <div class="sheet-title" id="dayEditTitle">Log Day Status</div>
      <button class="sheet-close-btn" onclick="closeModal('dayEditModal')"><i class="ti ti-x"></i></button>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px;">
      <button class="home-action-btn btn-clean" onclick="setPastDayStatus('clean')">
        <i class="ti ti-check"></i> Clean
      </button>
      <button class="home-action-btn" style="background: var(--red); color: #fff;" onclick="setPastDayStatus('relapse')">
        <i class="ti ti-x"></i> Slip
      </button>
    </div>
  </div>
</div>

<!-- 8. Floating Toast Message -->
<div class="toast-msg" id="appToast">
  <i class="ti ti-info-circle"></i>
  <span id="toastText">Saved</span>
</div>
"""
