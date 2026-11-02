# -*- coding: utf-8 -*-

ONBOARDING_HTML = """
<!-- ============================================================ -->
<!-- ===  ASSESSMENT MODAL OVERLAY (ONBOARDING QUESTIONS)       === -->
<!-- ============================================================ -->
<div class="modal-overlay" id="assessmentModal" onclick="closeBgModal(event, 'assessmentModal')">
  <div class="modal-sheet" style="max-height: 94vh; overflow-y: auto;">
    <div class="sheet-drag"></div>
    <div class="sheet-hdr">
      <div class="sheet-title" id="obHeaderTitle">Recovery Assessment</div>
      <button class="sheet-close-btn" onclick="closeModal('assessmentModal')"><i class="ti ti-x"></i></button>
    </div>

    <!-- Step 1: Questions (Q1 to Q6) -->
    <div id="obStepQuestions">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span style="font-size: 12px; font-weight: 700; color: #64748b;" id="obQProgressLabel">Question 1 of 6</span>
        <span style="font-size: 11px; font-weight: 600; color: var(--primary);">Initial Assessment</span>
      </div>
      <div class="streak-bar-bg" style="background: #e2e8f0; height: 5px; margin-bottom: 16px;">
        <div class="streak-bar-fill" id="obQProgressBar" style="width: 16.6%; background: var(--primary);"></div>
      </div>

      <div style="display: flex; justify-content: center; margin: 10px 0;">
        <div style="width: 60px; height: 60px; border-radius: 50%; background: #e0f2fe; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 800; color: var(--primary);" id="obQBadge">
          Q1
        </div>
      </div>

      <div style="text-align: center; font-size: 13px; font-weight: 700; color: #1a5fa8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">
        Let's Find Out If You Have a Problem with Porn
      </div>

      <div class="ob-q-title" id="obQTitle" style="font-size: 18px; margin: 6px 0 6px; line-height: 1.4; text-align: center;">
        Do you watch pornography more than once a week?
      </div>
      <div class="ob-q-sub" id="obQSub" style="margin-bottom: 20px; font-size: 13px; text-align: center; color: #64748b;">
        Your answers help us support you better.
      </div>

      <!-- Yes / No Options (for Q1 to Q5) -->
      <div id="obYesNoOptions">
        <button class="ob-opt-btn" onclick="answerAssessmentQuestion(true)" style="margin-bottom: 10px;">
          <span>Yes</span>
          <i class="ti ti-check" style="color: var(--primary); font-size: 18px;"></i>
        </button>
        <button class="ob-opt-btn" onclick="answerAssessmentQuestion(false)">
          <span>No</span>
          <i class="ti ti-x" style="color: #64748b; font-size: 18px;"></i>
        </button>
      </div>

      <!-- Multi-choice Frequency Options (for Q6) -->
      <div id="obFrequencyOptions" style="display: none; flex-direction: column; gap: 10px;">
        <button class="ob-opt-btn" onclick="answerFrequency(4)" style="display: flex; flex-direction: column; align-items: flex-start; padding: 12px 16px;">
          <span style="font-weight: 800; font-size: 15px; color: #1e293b;">Daily</span>
          <span style="font-size: 12px; color: #64748b; margin-top: 2px;">Every day or almost every day</span>
        </button>
        <button class="ob-opt-btn" onclick="answerFrequency(3)" style="display: flex; flex-direction: column; align-items: flex-start; padding: 12px 16px;">
          <span style="font-weight: 800; font-size: 15px; color: #1e293b;">Weekly</span>
          <span style="font-size: 12px; color: #64748b; margin-top: 2px;">Several times a week</span>
        </button>
        <button class="ob-opt-btn" onclick="answerFrequency(2)" style="display: flex; flex-direction: column; align-items: flex-start; padding: 12px 16px;">
          <span style="font-weight: 800; font-size: 15px; color: #1e293b;">Monthly</span>
          <span style="font-size: 12px; color: #64748b; margin-top: 2px;">A few times a month</span>
        </button>
        <button class="ob-opt-btn" onclick="answerFrequency(1)" style="display: flex; flex-direction: column; align-items: flex-start; padding: 12px 16px;">
          <span style="font-weight: 800; font-size: 15px; color: #1e293b;">Rarely</span>
          <span style="font-size: 12px; color: #64748b; margin-top: 2px;">Occasionally or trying to quit</span>
        </button>
      </div>
    </div>

    <!-- Step 2: Assessment Results Screen -->
    <div id="obStepResults" style="display: none;">
      <div style="text-align: center; margin-bottom: 16px;">
        <div style="width: 72px; height: 72px; border-radius: 50%; background: #0284c7; color: #fff; font-size: 22px; font-weight: 800; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px;" id="resScoreCircle">
          4 / 6
        </div>
        <h3 style="font-size: 20px; font-weight: 800; color: var(--text-primary); margin-top: 4px;">Your Assessment Results</h3>
        <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-top: 6px;" id="resDescription">
          Your responses indicate challenges. This app will guide you step by step to freedom.
        </p>
      </div>

      <div style="background: #ffffff; border: 1.5px solid var(--border); border-radius: 16px; padding: 16px 14px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
        <!-- Mental Impact -->
        <div style="margin-bottom: 14px;">
          <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 700; margin-bottom: 5px;">
            <span style="color: #1e293b;">Mental Impact</span>
            <span style="color: #ef4444;" id="resMentalScore">70%</span>
          </div>
          <div class="streak-bar-bg" style="background: #fee2e2; height: 8px;">
            <div style="height: 100%; border-radius: 999px; background: #ef4444; width: 70%; transition: width 1s ease;" id="resMentalBar"></div>
          </div>
        </div>

        <!-- Spiritual Impact -->
        <div style="margin-bottom: 14px;">
          <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 700; margin-bottom: 5px;">
            <span style="color: #1e293b;">Spiritual Impact</span>
            <span style="color: #0284c7;" id="resSpiritualScore">80%</span>
          </div>
          <div class="streak-bar-bg" style="background: #e0f2fe; height: 8px;">
            <div style="height: 100%; border-radius: 999px; background: #0284c7; width: 80%; transition: width 1s ease;" id="resSpiritualBar"></div>
          </div>
        </div>

        <!-- Relational Impact -->
        <div>
          <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 700; margin-bottom: 5px;">
            <span style="color: #1e293b;">Relational Impact</span>
            <span style="color: #0284c7;" id="resRelationalScore">60%</span>
          </div>
          <div class="streak-bar-bg" style="background: #e0f2fe; height: 8px;">
            <div style="height: 100%; border-radius: 999px; background: #0284c7; width: 60%; transition: width 1s ease;" id="resRelationalBar"></div>
          </div>
        </div>
      </div>

      <!-- Quranic Verse (Surah At-Talaq 65:3) -->
      <div style="background: #eff6ff; border-left: 4px solid #0284c7; border-radius: 0 12px 12px 0; padding: 14px 16px; margin-bottom: 16px;">
        <div style="font-size: 13.5px; font-style: italic; color: #1e3a8a; line-height: 1.5;">
          "And whoever relies upon Allah &mdash; then He is sufficient for him."
        </div>
        <div style="font-size: 11.5px; font-weight: 700; color: #0284c7; margin-top: 6px;">
          Surah At-Talaq 65:3 &bull; Tarjuma: Kanzul Iman (Aala Hazrat)
        </div>
      </div>

      <button class="home-action-btn btn-clean" onclick="finishAssessmentAndSetNiyah()">
        Begin Your Journey &rarr;
      </button>
    </div>

  </div>
</div>
"""
