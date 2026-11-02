# -*- coding: utf-8 -*-

CSS_CONTENT = """
<style>
/* ============================================================ */
/* ===  PURIFY UNIFIED MOBILE APP - MASTER STYLESHEET       === */
/* ============================================================ */
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent;}

:root {
  --primary: #1a5fa8;
  --primary-light: #2d8fd4;
  --accent-teal: #0EA5C9;
  --green: #2ecc71;
  --green-dark: #16a085;
  --red: #e74c3c;
  --gold: #f39c12;
  --bg: #f4f6f9;
  --card-bg: #ffffff;
  --text-primary: #1a2a3a;
  --text-secondary: #6B7280;
  --border: #e8ecf0;
  --shadow: 0 4px 14px rgba(0,0,0,0.06);
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  background: #0f172a;
  color: var(--text-primary);
  min-height: 100vh;
  margin: 0;
  padding: 16px 0;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

/* App Shell (Mobile phone frame on desktop, full screen on phone) */
.mobile-app-shell {
  width: 100%;
  max-width: 430px;
  height: 94vh;
  max-height: 880px;
  background: var(--bg);
  position: relative;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border-radius: 36px;
  border: 6px solid #1e293b;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.6);
}

@media (max-width: 480px) {
  body {
    padding: 0;
    background: var(--bg);
  }
  .mobile-app-shell {
    max-width: 100%;
    height: 100vh;
    max-height: 100vh;
    border: none;
    border-radius: 0;
    box-shadow: none;
  }
}

/* Top App Bar */
.app-top-bar {
  background: linear-gradient(160deg, var(--primary) 0%, var(--primary-light) 100%);
  padding: 14px 16px 12px;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;
  z-index: 10;
}
.app-user-pill {
  background: rgba(255,255,255,0.18);
  border-radius: 20px;
  padding: 4px 10px;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,0.25);
  max-width: 150px;
}
.app-user-pill .sync-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #4dd0e1;
  box-shadow: 0 0 6px #4dd0e1;
}
.app-user-pill span {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.app-header-right {
  display: flex;
  align-items: center;
  gap: 10px;
}
.app-hearts {
  display: flex;
  gap: 3px;
}
.app-hearts .ht {
  color: #ff4d4d;
  font-size: 17px;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
  transition: opacity 0.3s;
}
.app-xp-pill {
  background: #ffffff;
  border-radius: 16px;
  padding: 4px 10px;
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 11px;
  font-weight: 700;
  color: #1e3a8a;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}
.app-xp-pill i {
  color: #f59e0b;
  font-size: 13px;
}

/* Screens Container */
.screens-viewport {
  flex: 1;
  position: relative;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  -webkit-overflow-scrolling: touch;
}

.tab-screen {
  display: none;
  flex-direction: column;
  flex: 1;
  padding-bottom: 85px; /* space for bottom nav */
}
.tab-screen.active {
  display: flex;
}

/* Bottom Navigation */
.bottom-nav {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 64px;
  background: #ffffff;
  border-top: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 100;
  box-shadow: 0 -4px 16px rgba(0,0,0,0.08);
}
.bnav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  cursor: pointer;
  padding: 6px 10px;
  color: #94a3b8;
  transition: all 0.2s;
  flex: 1;
  user-select: none;
}
.bnav-item i {
  font-size: 22px;
}
.bnav-item span {
  font-size: 10.5px;
  font-weight: 700;
}
.bnav-item.active {
  color: var(--primary);
}
.bnav-item.active i {
  transform: translateY(-2px);
}

/* ============================================================ */
/* ===  HOME SCREEN STYLES                                   === */
/* ============================================================ */
.home-hdr-card {
  background: linear-gradient(160deg, var(--primary) 0%, var(--primary-light) 100%);
  padding: 4px 16px 18px;
  color: #fff;
}
.faith-card {
  background: #ffffff;
  border-radius: 18px;
  padding: 14px 15px;
  display: flex;
  align-items: center;
  gap: 14px;
  color: var(--text-primary);
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  margin-bottom: 14px;
  cursor: pointer;
}
.faith-tree-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  flex-shrink: 0;
}
.faith-tree-circle {
  width: 66px;
  height: 66px;
  border-radius: 50%;
  background: #e8d5b0;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow: 0 3px 8px rgba(0,0,0,0.1);
}
.faith-tree-lbl {
  font-size: 10px;
  font-weight: 700;
  color: #64748b;
  text-align: center;
  max-width: 70px;
  line-height: 1.2;
}
.faith-text {
  flex: 1;
}
.faith-title {
  font-size: 11px;
  font-weight: 700;
  color: var(--primary);
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 3px;
}
.faith-quote {
  font-size: 12.5px;
  line-height: 1.45;
  color: #334155;
  font-weight: 500;
}
.faith-ref {
  font-size: 11px;
  color: #64748b;
  font-style: italic;
  margin-top: 3px;
}

/* Streak Card */
.streak-card {
  background: #112233;
  border-radius: 16px;
  padding: 16px 14px 14px;
  text-align: center;
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}
.streak-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}
.streak-tag {
  color: rgba(255,255,255,0.7);
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
.streak-progress-txt {
  font-size: 11px;
  color: #4dd0e1;
  font-weight: 600;
}
.streak-timer-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 12px;
}
.timer-unit {
  text-align: center;
  min-width: 50px;
}
.timer-val {
  font-size: 32px;
  font-weight: 800;
  color: #ffffff;
  font-variant-numeric: tabular-nums;
  line-height: 1;
}
.timer-lbl {
  font-size: 9px;
  color: rgba(255,255,255,0.55);
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-top: 3px;
}
.timer-sep {
  font-size: 26px;
  font-weight: 700;
  color: rgba(255,255,255,0.4);
  margin-bottom: 14px;
}
.streak-bar-bg {
  width: 100%;
  height: 6px;
  background: rgba(255,255,255,0.15);
  border-radius: 999px;
  overflow: hidden;
}
.streak-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #4dd0e1, #2ecc71);
  border-radius: 999px;
  transition: width 0.5s ease;
}

/* Home Body Content */
.home-body {
  padding: 16px 14px;
}

/* Weekly Check-in */
.week-card {
  background: #ffffff;
  border-radius: 18px;
  padding: 16px 14px;
  margin-bottom: 14px;
  box-shadow: var(--shadow);
}
.week-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}
.week-header h3 {
  font-size: 15px;
  font-weight: 700;
  color: var(--text-primary);
}
.week-nav-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--primary);
  font-size: 18px;
  padding: 4px 8px;
  border-radius: 8px;
}
.week-nav-btn:disabled {
  color: #cbd5e1;
  cursor: default;
}
.week-days-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 4px;
  min-height: 58px;
}
.day-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  width: 40px;
}
.day-col-name {
  font-size: 11px;
  font-weight: 600;
  color: #64748b;
}
.day-col-name.today {
  color: var(--primary);
  font-weight: 800;
}
.day-dot {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}
.day-dot.clean {
  background: var(--green);
  color: #ffffff;
}
.day-dot.relapse {
  background: var(--red);
  color: #ffffff;
}
.day-dot.empty {
  background: #f1f5f9;
  border: 1.5px dashed #cbd5e1;
  color: #94a3b8;
}
.day-dot.future {
  background: #f8fafc;
  color: #cbd5e1;
  cursor: default;
}
.week-hint {
  text-align: center;
  font-size: 11px;
  color: #94a3b8;
  margin-top: 10px;
}

/* Primary Action Buttons */
.home-action-btn {
  width: 100%;
  padding: 15px;
  border-radius: 16px;
  border: none;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 10px;
  transition: transform 0.15s, opacity 0.15s;
}
.home-action-btn:active {
  transform: scale(0.98);
}
.btn-clean {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: #fff;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
}
.btn-clean.marked {
  background: #e2e8f0;
  color: #64748b;
  cursor: default;
  box-shadow: none;
}
.home-grid-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-bottom: 10px;
}
.btn-grid-sub {
  background: #ffffff;
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 13px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-grid-sub i {
  font-size: 20px;
}
.btn-grid-sub span {
  font-size: 12.5px;
  font-weight: 600;
}
.btn-grid-sub.niyah i, .btn-grid-sub.niyah span { color: var(--primary); }
.btn-grid-sub.relapse i, .btn-grid-sub.relapse span { color: var(--red); }
.btn-emergency {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  color: #fff;
  box-shadow: 0 4px 14px rgba(239, 68, 68, 0.3);
}

/* ============================================================ */
/* ===  DAILY RECOVERY PROGRAM STYLES                        === */
/* ============================================================ */
.daily-hdr {
  background: linear-gradient(160deg, var(--primary) 0%, var(--primary-light) 100%);
  padding: 14px 16px 16px;
  color: #fff;
  flex-shrink: 0;
}
.daily-day-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4px;
}
.daily-nav-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  border: none;
  color: #fff;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}
.daily-nav-btn:hover { background: rgba(255,255,255,0.3); }
.daily-day-title {
  font-size: 22px;
  font-weight: 800;
  text-align: center;
}
.daily-day-sub {
  font-size: 12.5px;
  color: rgba(255,255,255,0.85);
  text-align: center;
  margin-bottom: 4px;
}
.daily-completed-badge {
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,0.9);
  text-align: center;
  margin-bottom: 6px;
}
.daily-prog-bar-wrap {
  background: rgba(255,255,255,0.25);
  border-radius: 6px;
  height: 5px;
  overflow: hidden;
  margin-bottom: 4px;
}
.daily-prog-bar {
  height: 100%;
  background: #4dd0e1;
  border-radius: 6px;
  transition: width 0.4s ease;
}

.daily-content {
  padding: 14px 14px 90px;
}
.sec-title {
  font-size: 14.5px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 3px;
}
.sec-sub {
  font-size: 11.5px;
  color: #64748b;
  margin-bottom: 10px;
}

/* Adhkar Grid */
.adhkar-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-bottom: 14px;
}
.adhkar-card {
  background: #ffffff;
  border-radius: 16px;
  padding: 15px 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  border: 1.5px solid var(--border);
  box-shadow: var(--shadow);
  transition: all 0.2s;
}
.adhkar-card.done {
  background: #16a085;
  border-color: #16a085;
}
.adhkar-card i {
  font-size: 22px;
  color: var(--primary);
}
.adhkar-card.done i {
  color: #fff;
}
.adhkar-name {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--text-primary);
  text-align: center;
}
.adhkar-card.done .adhkar-name {
  color: #fff;
}
.adhkar-xp {
  font-size: 11px;
  font-weight: 600;
  color: var(--primary);
}
.adhkar-card.done .adhkar-xp {
  display: none;
}
.adhkar-done-pill {
  font-size: 11px;
  color: #fff;
  background: rgba(255,255,255,0.25);
  border-radius: 20px;
  padding: 2px 8px;
  display: none;
  align-items: center;
  gap: 3px;
}
.adhkar-card.done .adhkar-done-pill {
  display: flex;
}

/* Task Cards */
.task-card {
  background: #16a085;
  border-radius: 16px;
  padding: 14px 16px;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  color: #ffffff;
  box-shadow: 0 3px 10px rgba(22, 160, 133, 0.25);
  transition: opacity 0.2s, transform 0.15s;
}
.task-card:active {
  transform: scale(0.99);
}
.task-card.dr-card {
  background: #2563eb;
  box-shadow: 0 3px 10px rgba(37, 99, 235, 0.25);
}
.task-card.locked {
  background: #94a3b8;
  opacity: 0.6;
  cursor: not-allowed;
  box-shadow: none;
}
.task-left {
  display: flex;
  align-items: center;
  gap: 12px;
}
.task-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}
.task-name {
  font-size: 13.5px;
  font-weight: 700;
  line-height: 1.3;
}
.task-xp {
  font-size: 11px;
  opacity: 0.85;
}
.task-arrow {
  font-size: 18px;
  opacity: 0.7;
}

/* Day Summary */
.summary-card {
  background: #ffffff;
  border-radius: 18px;
  padding: 16px;
  border: 1.5px solid var(--border);
  box-shadow: var(--shadow);
  margin-top: 14px;
}
.summary-title {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 12px;
  color: var(--text-primary);
}
.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  text-align: center;
  gap: 8px;
}
.stat-box {
  background: #f8fafc;
  border-radius: 12px;
  padding: 10px 6px;
}
.stat-num {
  font-size: 20px;
  font-weight: 800;
  color: var(--primary);
}
.stat-lbl {
  font-size: 10px;
  font-weight: 600;
  color: #64748b;
  margin-top: 2px;
}

/* ============================================================ */
/* ===  JOURNEY SCREEN STYLES                                === */
/* ============================================================ */
.journey-header {
  background: linear-gradient(160deg, #1b4d3e 0%, #2e7d32 100%);
  padding: 18px 16px;
  color: #fff;
}
.journey-header h2 {
  font-size: 20px;
  font-weight: 800;
}
.journey-header p {
  font-size: 12px;
  opacity: 0.85;
  margin-top: 2px;
}
.journey-body {
  padding: 16px 14px 90px;
}
.cycle-card {
  background: #ffffff;
  border-radius: 18px;
  padding: 16px;
  margin-bottom: 12px;
  border: 1.5px solid var(--border);
  box-shadow: var(--shadow);
}
.cycle-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}
.cycle-title {
  font-size: 15px;
  font-weight: 800;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 8px;
}
.cycle-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 20px;
  background: #e8f5e9;
  color: #2e7d32;
}
.cycle-stages-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 10px;
}
.stage-item {
  background: #f8fafc;
  border-radius: 10px;
  padding: 10px 12px;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 12px;
}
.stage-dot {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #2e7d32;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 1px;
}

/* ============================================================ */
/* ===  URGE / EMERGENCY SCREEN STYLES                       === */
/* ============================================================ */
.urge-hdr {
  background: linear-gradient(160deg, #c0392b 0%, #e74c3c 100%);
  padding: 18px 16px;
  color: #fff;
  text-align: center;
}
.urge-hdr h2 {
  font-size: 20px;
  font-weight: 800;
}
.urge-hdr p {
  font-size: 12.5px;
  opacity: 0.9;
  margin-top: 2px;
}
.urge-tool-tabs {
  display: flex;
  background: #ffffff;
  border-bottom: 1px solid var(--border);
  padding: 4px;
}
.urge-tab {
  flex: 1;
  text-align: center;
  padding: 10px 4px;
  font-size: 12px;
  font-weight: 700;
  color: #64748b;
  cursor: pointer;
  border-radius: 10px;
  transition: all 0.2s;
}
.urge-tab.active {
  background: #fee2e2;
  color: #b91c1c;
}
.urge-body {
  padding: 20px 16px 90px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* 4-7-8 Breathing Circle */
.breath-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: 100%;
}
.breath-circle {
  width: 190px;
  height: 190px;
  border-radius: 50%;
  background: #e0f2fe;
  border: 8px solid #38bdf8;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 30px rgba(56, 189, 248, 0.3);
  transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}
.breath-circle.inhale {
  transform: scale(1.15);
  background: #e0f2fe;
  border-color: #0284c7;
}
.breath-circle.hold {
  transform: scale(1.15);
  background: #fef3c7;
  border-color: #f59e0b;
}
.breath-circle.exhale {
  transform: scale(0.92);
  background: #dcfce7;
  border-color: #22c55e;
}
.breath-num {
  font-size: 42px;
  font-weight: 800;
  color: #0f172a;
}
.breath-phase {
  font-size: 16px;
  font-weight: 700;
  color: #0f172a;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.breath-desc {
  font-size: 13px;
  color: #64748b;
  text-align: center;
}

/* Tasbeeh Digital Ring */
.tasbeeh-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: 100%;
}
.tasbeeh-ring {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  background: #ffffff;
  border: 8px solid #0EA5C9;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 10px 25px rgba(14, 165, 201, 0.25);
  user-select: none;
  transition: transform 0.1s;
}
.tasbeeh-ring:active {
  transform: scale(0.95);
}
.tasbeeh-count {
  font-size: 52px;
  font-weight: 800;
  color: #0EA5C9;
}
.tasbeeh-target {
  font-size: 13px;
  color: #64748b;
  font-weight: 600;
}
.tasbeeh-phrase {
  font-size: 17px;
  font-weight: 800;
  color: var(--text-primary);
  text-align: center;
  margin-top: 4px;
}
.tasbeeh-trans {
  font-size: 13px;
  color: #64748b;
  text-align: center;
}

/* Duas Card */
.duas-box {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.dua-box-card {
  background: #ffffff;
  border-radius: 18px;
  padding: 18px 16px;
  border: 1.5px solid var(--border);
  box-shadow: var(--shadow);
}
.dua-arabic {
  font-family: 'Amiri', serif;
  font-size: 20px;
  line-height: 1.8;
  color: #1e3a8a;
  text-align: right;
  direction: rtl;
  margin-bottom: 8px;
}
.dua-translit {
  font-size: 13px;
  font-weight: 600;
  color: #334155;
  margin-bottom: 6px;
}
.dua-transl {
  font-size: 12.5px;
  color: #64748b;
  line-height: 1.5;
}

/* ============================================================ */
/* ===  SETTINGS / PROFILE SCREEN STYLES                     === */
/* ============================================================ */
.settings-hdr {
  background: linear-gradient(160deg, #1e293b 0%, #334155 100%);
  padding: 18px 16px;
  color: #fff;
}
.settings-hdr h2 {
  font-size: 20px;
  font-weight: 800;
}
.settings-body {
  padding: 16px 14px 90px;
}
.profile-card {
  background: #ffffff;
  border-radius: 18px;
  padding: 16px;
  margin-bottom: 14px;
  border: 1.5px solid var(--border);
  box-shadow: var(--shadow);
  display: flex;
  align-items: center;
  gap: 14px;
}
.profile-avatar {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background: #e0f2fe;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: var(--primary);
  flex-shrink: 0;
}
.profile-info {
  flex: 1;
  overflow: hidden;
}
.profile-email {
  font-size: 14.5px;
  font-weight: 700;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.profile-sync-badge {
  font-size: 11px;
  font-weight: 600;
  color: #059669;
  display: flex;
  align-items: center;
  gap: 5px;
  margin-top: 3px;
}
.settings-sec-title {
  font-size: 11.5px;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 16px 4px 8px;
}
.settings-item {
  background: #ffffff;
  border-radius: 14px;
  padding: 14px 16px;
  margin-bottom: 8px;
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  transition: background 0.15s;
}
.settings-item:hover {
  background: #f8fafc;
}
.settings-item-left {
  display: flex;
  align-items: center;
  gap: 12px;
}
.settings-item-left i {
  font-size: 19px;
  color: var(--primary);
}
.settings-item-title {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--text-primary);
}
.settings-item-sub {
  font-size: 11px;
  color: #64748b;
}

/* ============================================================ */
/* ===  MODALS & SLIDE SHEETS                                === */
/* ============================================================ */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.55);
  display: none;
  align-items: flex-end;
  justify-content: center;
  z-index: 10050;
  backdrop-filter: blur(2px);
}
.modal-overlay.open {
  display: flex;
}
.modal-sheet {
  background: #ffffff;
  width: 100%;
  max-width: 430px;
  border-radius: 24px 24px 0 0;
  max-height: 90vh;
  overflow-y: auto;
  padding: 18px 18px 30px;
  animation: slideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes slideUp {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}
.sheet-drag {
  width: 36px;
  height: 4px;
  background: #cbd5e1;
  border-radius: 2px;
  margin: 0 auto 16px;
}
.sheet-hdr {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}
.sheet-title {
  font-size: 17px;
  font-weight: 800;
  color: var(--text-primary);
}
.sheet-close-btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #f1f5f9;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
}

/* Dua Items */
.dua-item {
  border: 1px solid var(--border);
  border-radius: 14px;
  margin-bottom: 10px;
  overflow: hidden;
}
.dua-header {
  padding: 12px 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  background: #ffffff;
}
.dua-check {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 2px solid #cbd5e1;
  display: flex;
  align-items: center;
  justify-content: center;
  color: transparent;
  flex-shrink: 0;
  transition: all 0.2s;
}
.dua-check.checked {
  background: #10b981;
  border-color: #10b981;
  color: #ffffff;
}
.dua-name {
  font-size: 13.5px;
  font-weight: 700;
  flex: 1;
}
.dua-body {
  display: none;
  padding: 12px 14px;
  background: #f8fafc;
  border-top: 1px solid var(--border);
}
.dua-body.open {
  display: block;
}
.dua-box-lbl {
  font-size: 10px;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  margin-bottom: 4px;
}
.dua-arabic-box {
  font-family: 'Amiri', serif;
  font-size: 18px;
  line-height: 1.8;
  color: #1e3a8a;
  text-align: right;
  direction: rtl;
  margin-bottom: 10px;
}

/* Lesson Sheet */
.lesson-sheet {
  background: #1a2a3a;
  color: #ffffff;
  min-height: 70vh;
}
.lesson-tag {
  color: #0EA5C9;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-bottom: 8px;
}
.lesson-quote {
  font-size: 18px;
  font-weight: 700;
  line-height: 1.45;
  color: #ffffff;
  margin-bottom: 16px;
  font-style: italic;
}
.lesson-text {
  font-size: 14px;
  line-height: 1.65;
  color: #cbd5e1;
  margin-bottom: 16px;
}
.lesson-textarea {
  width: 100%;
  min-height: 130px;
  background: rgba(255,255,255,0.07);
  border: 1.5px solid rgba(14, 165, 201, 0.4);
  border-radius: 12px;
  padding: 12px;
  color: #ffffff;
  font-family: inherit;
  font-size: 13.5px;
  resize: vertical;
  margin-top: 10px;
  margin-bottom: 14px;
}
.lesson-textarea:focus {
  outline: none;
  border-color: #0EA5C9;
}
.lesson-nav-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}
.lesson-btn {
  padding: 12px 20px;
  border-radius: 12px;
  border: none;
  font-size: 13.5px;
  font-weight: 700;
  cursor: pointer;
}
.lesson-btn-next {
  background: #0EA5C9;
  color: #fff;
}
.lesson-btn-prev {
  background: rgba(255,255,255,0.15);
  color: #fff;
}

/* Auth Modal Form */
.auth-input-group {
  margin-bottom: 14px;
}
.auth-label {
  font-size: 12px;
  font-weight: 700;
  color: #475569;
  margin-bottom: 6px;
  display: block;
}
.auth-input {
  width: 100%;
  padding: 13px 14px;
  border-radius: 12px;
  border: 1.5px solid var(--border);
  font-size: 14px;
  font-family: inherit;
  color: var(--text-primary);
}
.auth-input:focus {
  outline: none;
  border-color: var(--primary);
}
.auth-submit-btn {
  width: 100%;
  padding: 14px;
  border-radius: 14px;
  background: var(--primary);
  color: #fff;
  border: none;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(26, 95, 168, 0.3);
}

/* Toast */
.toast-msg {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%) translateY(-30px);
  background: rgba(15, 23, 42, 0.95);
  color: #fff;
  padding: 10px 20px;
  border-radius: 30px;
  font-size: 13px;
  font-weight: 600;
  z-index: 10100;
  opacity: 0;
  pointer-events: none;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 8px 20px rgba(0,0,0,0.25);
  display: flex;
  align-items: center;
  gap: 8px;
}
.toast-msg.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}

/* Onboarding / Options */
.ob-opt-btn {
  width: 100%;
  padding: 15px 18px;
  border-radius: 14px;
  border: 1.5px solid var(--border);
  background: #ffffff;
  font-size: 15px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all 0.15s;
}
.ob-opt-btn:hover {
  border-color: var(--primary);
  background: #f0f7ff;
}

/* Notification Quick Bell */
.notif-bell-btn {
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 15px;
}
.notif-bell-btn.active {
  background: #0284c7;
  color: #fff;
  box-shadow: 0 0 10px rgba(2, 132, 199, 0.5);
}

/* Daily Spiritual Thought Card */
.daily-thought-card {
  background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%);
  border: 1.5px solid #e2e8f0;
  border-left: 4px solid #0284c7;
  border-radius: 16px;
  padding: 14px 16px;
  margin-bottom: 14px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}
.daily-thought-hdr {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}
.daily-thought-title {
  font-size: 12px;
  font-weight: 700;
  color: #0284c7;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.thought-nav-btn {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 1px solid #cbd5e1;
  background: #ffffff;
  color: #475569;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 12px;
  transition: background 0.15s;
}
.thought-nav-btn:hover {
  background: #e2e8f0;
  color: #0f172a;
}
.daily-thought-topic {
  font-size: 14px;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 6px;
}
.daily-thought-quote {
  font-size: 13px;
  line-height: 1.5;
  color: #1e293b;
  font-style: italic;
  margin-bottom: 6px;
}
.daily-thought-ref {
  font-size: 11px;
  font-weight: 700;
  color: #0284c7;
  margin-bottom: 6px;
}
.daily-thought-wisdom {
  font-size: 12px;
  line-height: 1.45;
  color: #475569;
  background: rgba(255,255,255,0.7);
  padding: 8px 10px;
  border-radius: 8px;
}

/* Journey Tree Showcase Card */
.journey-tree-showcase {
  background: #ffffff;
  border-radius: 16px;
  border: 1.5px solid var(--border);
  padding: 14px 16px;
  margin-bottom: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

/* ============================================================ */
/* ===  COMMUNITY BROTHERHOOD TAB                            === */
/* ============================================================ */
.community-hdr {
  background: linear-gradient(160deg, #1e3a8a 0%, #2563eb 100%);
  padding: 18px 16px;
  color: #fff;
  text-align: center;
  flex-shrink: 0;
}
.community-hdr h2 {
  font-size: 20px;
  font-weight: 800;
}
.community-hdr p {
  font-size: 12.5px;
  opacity: 0.88;
  margin-top: 3px;
}

/* ============================================================ */
/* ===  DAILY TAB - TOP BAR, SLIDER, LESSON CARDS            === */
/* ============================================================ */
.daily-top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 14px 8px;
  background: linear-gradient(160deg, var(--primary) 0%, var(--primary-light) 100%);
  color: #fff;
  flex-shrink: 0;
}
.day-nav-arrow {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  border: none;
  color: #fff;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}
.day-nav-arrow:hover { background: rgba(255,255,255,0.3); }
.daily-day-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}
.day-badge-pill {
  background: rgba(255,255,255,0.25);
  padding: 4px 16px;
  border-radius: 99px;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 0.5px;
}
.day-cycle-label {
  font-size: 11px;
  opacity: 0.85;
  font-weight: 600;
}
.day-slider-container {
  padding: 8px 14px 4px;
  background: linear-gradient(160deg, var(--primary-light) 0%, var(--primary) 100%);
  flex-shrink: 0;
}
.day-slider {
  width: 100%;
  height: 6px;
  -webkit-appearance: none;
  appearance: none;
  background: rgba(255,255,255,0.2);
  border-radius: 99px;
  outline: none;
  cursor: pointer;
}
.day-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  cursor: pointer;
}
.day-slider::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  cursor: pointer;
  border: none;
}
.day-slider-marks {
  display: flex;
  justify-content: space-between;
  font-size: 10px;
  color: rgba(255,255,255,0.6);
  padding: 2px 2px 6px;
  font-weight: 600;
}

/* Daily Content Wrap */
.daily-content-wrap {
  flex: 1;
  overflow-y: auto;
  padding: 14px 14px 90px;
  -webkit-overflow-scrolling: touch;
}

/* Lesson Cards in Daily Tab */
/* Rectangular Small Module Tabs (Ibn Qayyim & Neuroscience) */
.module-rect-tabs-wrap {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 14px;
}
.module-rect-tab {
  background: #ffffff;
  border: 1.5px solid #e2e8f0;
  border-radius: 14px;
  padding: 12px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 2px 6px rgba(0,0,0,0.03);
}
.module-rect-tab:hover, .module-rect-tab:active {
  transform: translateY(-1px);
  border-color: #0284c7;
  box-shadow: 0 4px 12px rgba(2, 132, 199, 0.12);
}
.module-rect-tab.completed {
  border-color: #86efac;
  background: #f0fdf4;
}
.module-rect-icon {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
}
.mri-ibn {
  background: linear-gradient(135deg, #0ea5e9, #0284c7);
  color: #ffffff;
}
.mri-neuro {
  background: linear-gradient(135deg, #8b5cf6, #6366f1);
  color: #ffffff;
}
.module-rect-info {
  flex: 1;
  min-width: 0;
}
.module-rect-tag-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 2px;
}
.module-rect-tag {
  font-size: 10px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 2px 6px;
  border-radius: 4px;
}
.mrt-ibn {
  background: #e0f2fe;
  color: #0369a1;
}
.mrt-neuro {
  background: #ede9fe;
  color: #6d28d9;
}
.module-rect-readtime {
  font-size: 11px;
  color: #94a3b8;
}
.module-rect-title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.module-rect-status-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 5px 11px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  gap: 4px;
  flex-shrink: 0;
  transition: all 0.2s ease;
}
.status-badge-pending {
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #e2e8f0;
}
.status-badge-complete {
  background: #dcfce7;
  color: #15803d;
  border: 1px solid #bbf7d0;
}

.lesson-card {
  background: #ffffff;
  border-radius: 18px;
  padding: 18px 16px;
  margin-bottom: 14px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.06);
  border: 1px solid var(--border);
}
.lesson-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}
.lesson-card-title {
  font-size: 17px;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.35;
  margin-bottom: 8px;
}
.lesson-card-body {
  font-size: 13.5px;
  line-height: 1.6;
  color: #475569;
  margin-bottom: 12px;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.lesson-card-action {
  display: flex;
  justify-content: flex-end;
}
.btn-read-lesson {
  background: var(--primary);
  color: #fff;
  border: none;
  padding: 9px 18px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: opacity 0.2s;
}
.btn-read-lesson:hover { opacity: 0.9; }
.lesson-read-time {
  font-size: 11.5px;
  color: #94a3b8;
  display: flex;
  align-items: center;
  gap: 4px;
}
.lesson-slide-content {
  font-size: 14px;
  line-height: 1.65;
  color: #cbd5e1;
}
.tag-islamic {
  background: #0284c7;
  color: #fff;
  padding: 3px 10px;
  border-radius: 6px;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
.tag-neuro {
  background: #7c3aed;
  color: #fff;
  padding: 3px 10px;
  border-radius: 6px;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

/* Reminder Card */
.reminder-card {
  background: #fffbeb;
  border-radius: 16px;
  padding: 16px 14px;
  margin-bottom: 14px;
  border: 1.5px solid #fde68a;
}
.reminder-hdr {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}
.reminder-title {
  font-size: 14px;
  font-weight: 700;
  color: #92400e;
}
.reminder-body {
  font-size: 13px;
  line-height: 1.6;
  color: #78350f;
}

/* Journal Card */
.journal-card {
  background: #ffffff;
  border-radius: 16px;
  padding: 16px 14px;
  margin-bottom: 14px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  border: 1.5px solid var(--border);
}
.journal-hdr {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14.5px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 6px;
}
.journal-textarea {
  width: 100%;
  min-height: 100px;
  border: 1.5px solid var(--border);
  border-radius: 12px;
  padding: 12px;
  font-family: inherit;
  font-size: 13.5px;
  color: var(--text-primary);
  resize: vertical;
  background: #f8fafc;
  transition: border-color 0.2s;
}
.journal-textarea:focus {
  outline: none;
  border-color: var(--primary);
  background: #fff;
}
.journal-textarea::placeholder {
  color: #94a3b8;
}
.journal-save-status {
  font-size: 11.5px;
  color: #10b981;
  font-weight: 600;
  margin-top: 6px;
  text-align: right;
}

/* ============================================================ */
/* ===  HOME - DAILY PRACTICES / RITUALS GRID                === */
/* ============================================================ */
.daily-rituals-sec {
  margin-top: 16px;
}
.sec-hdr-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}
.sec-badge {
  font-size: 11px;
  font-weight: 700;
  color: #10b981;
  background: #ecfdf5;
  padding: 3px 10px;
  border-radius: 99px;
}
.rituals-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.ritual-card {
  background: #ffffff;
  border-radius: 14px;
  padding: 14px 12px;
  display: flex;
  align-items: center;
  gap: 12px;
  border: 1.5px solid var(--border);
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  cursor: pointer;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.ritual-card:active {
  border-color: var(--primary-light);
  box-shadow: 0 2px 12px rgba(26,95,168,0.12);
}
.ritual-card.done {
  border-color: #10b981;
  background: #f0fdf4;
}
.ritual-icon {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
}
.ri-morning { background: #fef3c7; color: #d97706; }
.ri-evening { background: #ede9fe; color: #7c3aed; }
.ri-lesson { background: #e0f2fe; color: #0284c7; }
.ri-niyah { background: #fce7f3; color: #db2777; }
.ritual-info {
  flex: 1;
  min-width: 0;
}
.ritual-title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text-primary);
}
.ritual-sub {
  font-size: 11.5px;
  color: #64748b;
  margin-top: 1px;
}
.ritual-chk {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 2px solid #cbd5e1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  color: transparent;
  flex-shrink: 0;
  transition: all 0.2s;
}
.ritual-card.done .ritual-chk {
  background: #10b981;
  border-color: #10b981;
  color: #fff;
}

/* Relapse Button */
.btn-relapse {
  background: #fff;
  color: var(--red);
  border: 1.5px solid #fca5a5;
  box-shadow: none;
}
.btn-relapse:hover {
  background: #fef2f2;
}

/* ============================================================ */
/* ===  URGE TAB - MISSING PIECES                            === */
/* ============================================================ */
.urge-pulse-circle {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  margin: 0 auto 12px;
  animation: urgePulse 2s ease-in-out infinite;
}
@keyframes urgePulse {
  0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255,255,255,0.4); }
  50% { transform: scale(1.08); box-shadow: 0 0 0 12px rgba(255,255,255,0); }
}
.urge-title {
  font-size: 20px;
  font-weight: 800;
}
.urge-sub {
  font-size: 12.5px;
  opacity: 0.9;
  margin-top: 4px;
}
.tool-card {
  width: 100%;
  background: #ffffff;
  border-radius: 18px;
  padding: 18px 16px;
  margin-bottom: 14px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.06);
}
.tool-title {
  font-size: 14.5px;
  font-weight: 700;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}
.tool-sub {
  font-size: 12px;
  color: #64748b;
  margin-bottom: 14px;
  line-height: 1.4;
}
.breath-widget {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}
.breath-ctrl-btn {
  background: #0284c7;
  color: #fff;
  border: none;
  padding: 10px 24px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.2s;
}
.breath-ctrl-btn:hover { opacity: 0.9; }
.breath-circle #breathText {
  font-size: 18px;
  font-weight: 700;
  color: #0f172a;
}
.tasbeeh-widget {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.tasbeeh-ring-btn {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: #ffffff;
  border: 6px solid #0EA5C9;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 8px 20px rgba(14, 165, 201, 0.2);
  user-select: none;
  transition: transform 0.1s;
  margin: 12px 0;
}
.tasbeeh-ring-btn:active { transform: scale(0.95); }
.tasbeeh-lbl {
  font-size: 11px;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* ============================================================ */
/* ===  JOURNEY TAB - MISSING STYLES                         === */
/* ============================================================ */
.journey-hdr {
  background: linear-gradient(160deg, #0f766e 0%, #0d9488 100%);
  padding: 20px 16px;
  color: #fff;
  text-align: center;
}
.journey-title {
  font-size: 20px;
  font-weight: 800;
}
.journey-sub {
  font-size: 12.5px;
  opacity: 0.85;
  margin-top: 4px;
}
.cycles-list {
  padding: 14px 14px 90px;
}

/* ============================================================ */
/* ===  DUA MODAL LIST STYLES                                === */
/* ============================================================ */
.dua-hdr {
  font-size: 13px;
  font-weight: 700;
  color: var(--primary);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 12px;
}
.dua-item {
  background: #f8fafc;
  border-radius: 14px;
  padding: 14px 12px;
  margin-bottom: 10px;
  border: 1.5px solid var(--border);
  cursor: pointer;
  transition: border-color 0.2s;
}
.dua-item.checked {
  border-color: #10b981;
  background: #f0fdf4;
}
.dua-title {
  font-family: 'Amiri', serif;
  font-size: 18px;
  line-height: 1.7;
  color: #0f172a;
  margin-bottom: 6px;
}
.dua-translation {
  font-size: 12.5px;
  color: #475569;
  line-height: 1.5;
  font-style: italic;
  margin-bottom: 4px;
}
.dua-source {
  font-size: 10.5px;
  color: #94a3b8;
  font-weight: 600;
}

/* ============================================================ */
/* ===  ONBOARDING QUESTION STYLES                           === */
/* ============================================================ */
.ob-q-title {
  font-size: 17px;
  font-weight: 800;
  color: #fff;
  margin-bottom: 6px;
}
.ob-q-sub {
  font-size: 13px;
  color: rgba(255,255,255,0.8);
  margin-bottom: 16px;
  line-height: 1.45;
}

/* ============================================================ */
/* ===  EMERGENCY URGE BUTTON ON HOME PAGE                   === */
/* ============================================================ */
.home-urge-btn {
  width: 100%;
  padding: 14px;
  border-radius: 16px;
  border: 2px solid #ef4444;
  background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
  color: #dc2626;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 10px;
  transition: transform 0.15s, box-shadow 0.15s;
  box-shadow: 0 3px 12px rgba(239,68,68,0.15);
}
.home-urge-btn:active {
  transform: scale(0.98);
  box-shadow: 0 1px 6px rgba(239,68,68,0.2);
}

</style>
"""
