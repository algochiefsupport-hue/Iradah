# -*- coding: utf-8 -*-

ONBOARDING_CSS = """/* ===== BASE RESET ===== */
*{box-sizing:border-box;margin:0;padding:0;}
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Nunito:wght@400;600;700;800;900&family=Amiri:ital@0;1&display=swap');

:root{
  --blue:#1a9fc0;
  --red:#e53e3e;
  --green:#38a169;
  --bg:#f4f6f9;
  --text:#1a1a2e;
}

/* ===== PHASE 1: 6_tak styles (splash, Q screens, urge tools) ===== */
.p1-wrap {
  font-family: 'Inter', sans-serif;
  background: #f5f7fa;
  width: 340px;
  min-height: 680px;
  border-radius: 28px;
  border: 0.5px solid #d0d8e4;
  margin: 1rem auto;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.progress-bar-track { width:100%; height:5px; background:#e2e8f0; flex-shrink:0; }
.progress-bar-fill { height:5px; background:#2196F3; border-radius:0 3px 3px 0; transition:width 0.4s; }
.page-count { text-align:right; font-size:12px; color:#9aa3b2; padding:5px 18px 0; }

/* SPLASH */
.splash { width:340px; height:680px; border-radius:28px; overflow:hidden; position:relative; display:flex; flex-direction:column; justify-content:flex-end; border:0.5px solid #d0d8e4; margin:1rem auto; }
.splash-bg { position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; }
.splash-content { position:relative; z-index:2; padding:0 22px 28px; display:flex; flex-direction:column; align-items:center; }
.main-title { font-size:32px; font-weight:800; color:white; text-align:center; line-height:1.2; margin-bottom:14px; }
.sub-text { font-size:15px; color:rgba(255,255,255,0.85); text-align:center; line-height:1.6; margin-bottom:28px; }
.btn-journey { width:100%; padding:16px; background:#00bcd4; color:white; font-size:17px; font-weight:700; border:none; border-radius:16px; cursor:pointer; font-family:'Inter',sans-serif; margin-bottom:18px; }
.signin-text { font-size:14px; color:rgba(255,255,255,0.65); text-align:center; }
.signin-text strong { color:white; font-weight:700; cursor:pointer; }

/* ASSESSMENT */
.screen-p1 { display:none; flex-direction:column; flex:1; }
.screen-p1.active { display:flex; }
.circle-area { display:flex; justify-content:center; padding:28px 0 20px; }
.big-circle { width:155px; height:155px; border-radius:50%; background:#e4edf8; display:flex; align-items:center; justify-content:center; }
.q-badge { width:58px; height:58px; border-radius:50%; background:#2196F3; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:800; color:white; }
.card-title { text-align:center; font-size:17px; font-weight:800; color:#1a1a2e; padding:0 24px; line-height:1.35; }
.q-count-row { display:flex; align-items:center; padding:8px 28px 20px; }
.q-count-text { font-size:13px; color:#9aa3b2; white-space:nowrap; margin-right:8px; }
.underline-blue { height:2.5px; background:#2196F3; border-radius:2px; transition:width 0.4s; }
.line-gray { flex:1; height:1.5px; background:#dde6f0; }
.question-text { font-size:21px; font-weight:800; color:#111827; text-align:center; padding:0 22px; line-height:1.3; margin-bottom:8px; }
.help-text { text-align:center; font-size:13px; font-weight:600; color:#555e75; margin-bottom:24px; padding:0 22px; }
.options-area { padding:0 18px; display:flex; flex-direction:column; gap:12px; }
.option-btn { display:flex; align-items:center; gap:14px; background:white; border:1px solid #e2e8f2; border-radius:14px; padding:15px 18px; cursor:pointer; font-family:'Inter',sans-serif; width:100%; text-align:left; }
.option-btn:active { background:#e8f0fb; }
.option-icon { width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; flex-shrink:0; background:#eef1f6; }
.option-icon i { font-size:16px; color:#8a99bb; }
.option-label { font-size:16px; font-weight:700; color:#1a1a2e; }
.option-btn-multi { display:flex; flex-direction:column; background:white; border:1px solid #e2e8f2; border-radius:14px; padding:14px 18px; cursor:pointer; font-family:'Inter',sans-serif; width:100%; text-align:left; }
.option-btn-multi:active { background:#e8f0fb; }
.opt-title { font-size:15px; font-weight:700; color:#1a1a2e; }
.opt-sub { font-size:12px; color:#8a99bb; margin-top:2px; }

/* RESULTS */
.results-inner { padding:0 18px 28px; width:100%; display:flex; flex-direction:column; align-items:center; }
.score-circle { width:90px; height:90px; border-radius:50%; background:#2196F3; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:800; color:white; margin:20px 0 14px; }
.results-title { font-size:20px; font-weight:800; color:#1a1a2e; text-align:center; margin-bottom:16px; }
.impact-card { width:100%; background:white; border:1px solid #e2e8f2; border-radius:16px; padding:16px 18px; margin-bottom:14px; }
.impact-row { margin-bottom:14px; }
.impact-row:last-child { margin-bottom:0; }
.impact-label-row { display:flex; justify-content:space-between; align-items:center; margin-bottom:7px; }
.impact-label { font-size:14px; font-weight:700; color:#1a1a2e; }
.impact-pct-red { font-size:14px; font-weight:700; color:#e53e3e; }
.impact-pct-blue { font-size:14px; font-weight:700; color:#2196F3; }
.bar-track-p1 { height:8px; background:#e8edf5; border-radius:4px; overflow:hidden; }
.bar-fill-p1 { height:8px; border-radius:4px; width:0%; transition:width 1.4s cubic-bezier(0.4,0,0.2,1); }
.bar-fill-red { background:#e53e3e; }
.bar-fill-blue { background:#2196F3; }
.result-desc { font-size:13px; color:#555e75; text-align:center; line-height:1.6; margin-bottom:16px; }
.quran-card-p1 { width:100%; background:#eaf3fb; border-radius:14px; border-left:4px solid #2196F3; padding:14px 16px; margin-bottom:20px; }
.quran-text { font-size:13px; font-style:italic; color:#1a2d5a; line-height:1.6; margin-bottom:4px; }
.quran-ref { font-size:12px; font-weight:700; color:#4a6fa5; text-align:center; }
.btn-continue { width:100%; padding:15px; background:#00bcd4; color:white; font-size:16px; font-weight:700; border:none; border-radius:14px; cursor:pointer; font-family:'Inter',sans-serif; display:block; }
.btn-continue:active { background:#0097a7; transform:scale(0.98); }

/* GENDER */
.gender-body { padding:32px 22px 28px; display:flex; flex-direction:column; align-items:center; flex:1; }
.gender-title { font-size:24px; font-weight:800; color:#1a1a2e; text-align:center; margin-bottom:10px; }
.gender-sub { font-size:14px; font-weight:600; color:#555e75; text-align:center; line-height:1.5; margin-bottom:32px; }
.gender-cards { display:flex; gap:14px; width:100%; margin-bottom:28px; }
.gender-card { flex:1; background:white; border:2px solid #e2e8f2; border-radius:16px; padding:22px 10px 16px; display:flex; flex-direction:column; align-items:center; cursor:pointer; transition:all 0.15s; }
.gender-card.selected { background:#dbeafe; border-color:#2196F3; }
.gender-avatar { width:56px; height:56px; border-radius:50%; background:#e8edf5; display:flex; align-items:center; justify-content:center; margin-bottom:12px; }
.gender-card.selected .gender-avatar { background:#bfdbfe; }
.gender-avatar i { font-size:28px; color:#8a99bb; }
.gender-card.selected .gender-avatar i { color:#2196F3; }
.gender-label { font-size:16px; font-weight:700; color:#8a99bb; }
.gender-card.selected .gender-label { color:#2196F3; }

/* URGE SCREEN */
.urge-screen { width:340px; min-height:680px; border-radius:28px; border:0.5px solid #d0d8e4; margin:1rem auto; overflow:hidden; display:flex; flex-direction:column; position:relative; font-family:'Inter',sans-serif; }
.urge-bg { position:absolute; top:0; left:0; width:100%; height:100%; z-index:0; }
.urge-top { position:relative; z-index:2; padding:0 22px 0; }
.urge-prog-track { width:100%; height:5px; background:rgba(255,255,255,0.25); }
.urge-prog-fill { height:5px; background:#00bcd4; border-radius:0 3px 3px 0; width:13.7%; }
.urge-page-count { text-align:right; font-size:12px; color:rgba(255,255,255,0.65); padding:5px 0 0; }
.urge-title { font-size:26px; font-weight:800; color:white; text-align:left; line-height:1.3; margin:24px 0 10px; }
.urge-sub { font-size:14px; color:rgba(255,255,255,0.8); text-align:left; line-height:1.5; margin-bottom:22px; }
.urge-pct-text { font-size:42px; font-weight:800; color:white; text-align:center; margin-bottom:10px; }
.urge-bar-track { height:10px; background:rgba(255,255,255,0.25); border-radius:5px; overflow:hidden; margin-bottom:0; }
.urge-bar-fill { height:10px; background:#e53e3e; border-radius:5px; width:0%; transition:width 1.5s cubic-bezier(0.4,0,0.2,1); }
.urge-cards-area { position:relative; z-index:2; padding:0 14px 28px; display:flex; gap:10px; margin-top:auto; }
.urge-card { flex:1; background:white; border-radius:16px; padding:18px 8px 14px; display:flex; flex-direction:column; align-items:center; cursor:pointer; border:none; font-family:'Inter',sans-serif; opacity:0; transform:translateY(24px); transition: opacity 0.5s, transform 0.5s; }
.urge-card.visible { opacity:1; transform:translateY(0); }
.urge-card:active { transform:scale(0.97); }
.urge-icon-circle { width:52px; height:52px; border-radius:50%; background:#e8f5ee; display:flex; align-items:center; justify-content:center; margin-bottom:10px; }
.urge-icon-circle i { font-size:26px; color:#2e7d5a; }
.urge-card-label { font-size:13px; font-weight:700; color:#1a1a2e; text-align:center; }

.hidden { display:none; }

/* ===== PHASE 2: 16.html styles (screens 7-17) ===== */
.p2-wrap {
  font-family:'Nunito',sans-serif;
  background:var(--bg);
  width:100%;
  max-width:420px;
  min-height:100vh;
  display:flex;
  flex-direction:column;
  position:relative;
  display:none;
}
.p2-wrap.active { display:flex; }

.prog-wrap{height:6px;background:#d1dbe8;position:sticky;top:0;z-index:100;}
.prog-fill{height:100%;background:var(--blue);border-radius:0 3px 3px 0;transition:width .5s ease;}
.step-ctr{text-align:right;font-size:13px;color:#777;font-weight:600;padding:8px 18px 0;}

.screen{display:none;flex-direction:column;padding:20px 20px 30px;flex:1;animation:fadeIn .35s ease;}
.screen.active{display:flex;}
@keyframes fadeIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}

.s-title{font-size:24px;font-weight:900;color:var(--text);text-align:center;margin-bottom:8px;line-height:1.3;}
.s-sub{font-size:14px;color:#666;text-align:center;font-weight:600;margin-bottom:22px;line-height:1.5;}

.opt-list{display:flex;flex-direction:column;gap:10px;overflow-y:auto;flex:1;padding-bottom:10px;}
.opt-list::-webkit-scrollbar{display:none;}
.opt{display:flex;align-items:center;gap:14px;background:#fff;border:2.5px solid transparent;border-radius:14px;padding:15px 16px;cursor:pointer;transition:all .18s;box-shadow:0 1px 4px rgba(0,0,0,.06);}
.opt:active,.opt:hover{border-color:var(--blue);}
.opt.sel{border-color:var(--blue);background:#e8f7fc;}
.radio{width:22px;height:22px;border-radius:50%;border:2px solid #ccc;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:all .2s;}
.opt.sel .radio{border-color:var(--blue);background:var(--blue);}
.opt.sel .radio::after{content:'';width:8px;height:8px;background:#fff;border-radius:50%;}
.opt-lbl{font-size:15px;font-weight:700;color:var(--text);}

.qbox{background:#eaf5f9;border-left:4px solid var(--blue);border-radius:10px;padding:14px 16px;margin-top:18px;}
.qtext{font-family:'Amiri',serif;font-style:italic;font-size:15px;color:#1a4a5a;text-align:center;line-height:1.6;}
.qref{font-size:12px;font-weight:700;color:var(--blue);text-align:center;margin-top:5px;}

.btn{background:var(--blue);color:#fff;border:none;border-radius:14px;padding:16px;font-size:17px;font-weight:800;font-family:'Nunito',sans-serif;cursor:pointer;margin-top:18px;width:100%;box-shadow:0 4px 14px rgba(26,159,192,.35);transition:all .2s;}
.btn:hover{background:#1585a3;}
.btn:disabled{background:#c5d5de;box-shadow:none;cursor:not-allowed;}

.cost-items{display:flex;flex-direction:column;gap:12px;margin-bottom:8px;}
.cost-item{display:flex;align-items:center;gap:14px;background:#fff;border-radius:14px;padding:14px 16px;box-shadow:0 1px 5px rgba(0,0,0,.07);animation:slideIn .4s ease both;}
@keyframes slideIn{from{opacity:0;transform:translateX(-18px)}to{opacity:1;transform:translateX(0)}}
.cost-item:nth-child(1){animation-delay:.05s}
.cost-item:nth-child(2){animation-delay:.15s}
.cost-item:nth-child(3){animation-delay:.25s}
.cost-item:nth-child(4){animation-delay:.35s}
.cicon{width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0;}

.bars-wrap{display:flex;flex-direction:column;gap:16px;margin:16px 0;}
.bar-row{display:flex;flex-direction:column;gap:6px;}
.bar-lr{display:flex;justify-content:space-between;}
.bar-name{font-size:14px;font-weight:800;color:var(--text);}
.bar-pct{font-size:14px;font-weight:900;color:var(--red);}
.bar-track{width:100%;height:10px;background:#e2e8f0;border-radius:99px;overflow:hidden;position:relative;}
.bar-red,.bar-grn{position:absolute;left:0;top:0;height:100%;border-radius:99px;transition:width 1.3s cubic-bezier(.22,1,.36,1);}
.bar-red{background:var(--red);}
.bar-grn{background:var(--green);}

.card-stack{position:relative;height:280px;margin:0 4px;}
.scard{position:absolute;top:0;left:0;right:0;background:#fff;border-radius:18px;border:2px solid #f0e0e0;box-shadow:0 4px 20px rgba(0,0,0,.10);padding:20px;cursor:grab;user-select:none;height:270px;transition:transform .3s ease,opacity .3s ease;}
.scard.active-scard{border-left:5px solid var(--red);}
.scard.fly-l{transform:translateX(-130%) rotate(-15deg)!important;opacity:0;transition:transform .4s ease,opacity .3s ease;}
.scard.fly-r{transform:translateX(130%) rotate(15deg)!important;opacity:0;transition:transform .4s ease,opacity .3s ease;}
.ch{display:flex;align-items:center;gap:12px;margin-bottom:14px;}
.cicon2{width:46px;height:46px;border-radius:12px;background:#fdecea;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0;}
.ctag{font-size:12px;font-weight:800;color:var(--red);letter-spacing:1px;flex:1;}
.cnum{font-size:13px;font-weight:700;color:#aaa;}
.ctitle{font-size:19px;font-weight:900;color:var(--text);margin-bottom:10px;}
.cbody{font-size:14px;color:#555;font-weight:600;line-height:1.6;}
.dots{display:flex;justify-content:center;gap:8px;margin-top:12px;}
.dot{width:10px;height:10px;border-radius:50%;background:#ddd;transition:background .3s;}
.dot.on{background:var(--red);}

.toll-row{display:flex;align-items:center;padding:16px 18px;}
.toll-pct{font-size:32px;font-weight:900;color:var(--red);min-width:78px;}
.toll-div{width:2px;height:44px;background:#eee;margin:0 14px;flex-shrink:0;}
.toll-t{font-size:15px;font-weight:800;color:var(--text);margin-bottom:3px;}
.toll-s{font-size:13px;color:#888;font-weight:600;}

.light-item{display:flex;align-items:flex-start;gap:12px;font-size:15px;font-weight:600;color:var(--text);line-height:1.4;animation:fadeIn .5s ease both;}
.rdot{width:12px;height:12px;border-radius:50%;background:var(--red);flex-shrink:0;margin-top:4px;}
.lost-item{display:flex;align-items:center;background:#fff;border-radius:14px;border-left:4px solid #fca5a5;padding:13px 16px;font-size:15px;font-weight:700;color:var(--text);box-shadow:0 1px 5px rgba(0,0,0,.05);animation:fadeIn .5s ease both;}
.ldot-wrap{width:34px;height:34px;background:#fdecea;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-right:13px;}
.ldot{width:11px;height:11px;border-radius:50%;background:var(--red);}

.future-tab{flex:1;padding:10px 6px;border-radius:99px;border:none;background:transparent;font-size:12px;font-weight:700;color:#888;cursor:pointer;font-family:'Nunito',sans-serif;transition:all .2s;white-space:nowrap;}
.future-tab.on{background:var(--blue);color:#fff;box-shadow:0 3px 10px rgba(26,159,192,.35);}

/* ===== BODY WRAPPER ===== */
body{background:#dde4ed;display:flex;justify-content:center;min-height:100vh;}

/* ===== PHASE 3 styles from 22.html ===== */
.phone { width: 380px; min-height: 700px; background: #fff; position: relative; overflow: hidden; margin: 1rem auto; border-radius: 28px; border: 0.5px solid #d0d8e4; }
.screen22 { display: none; flex-direction: column; min-height: 700px; }
.screen22.active { display: flex; }
.progress-bar-container { padding: 16px 16px 4px; }
.step-label { font-size: 12px; color: #aaa; text-align: right; margin-top: 4px; }
.screen-body { padding: 12px 20px 24px; flex: 1; display: flex; flex-direction: column; }
.screen-title { font-size: 22px; font-weight: 700; color: #1a1a2e; text-align: center; margin-bottom: 6px; }
.screen-sub { font-size: 14px; color: #555; text-align: center; margin-bottom: 18px; }
.tabs22 { display: flex; gap: 0; background: #f2f6f9; border-radius: 30px; padding: 3px; margin-bottom: 18px; }
.tab22 { flex: 1; text-align: center; padding: 7px 4px; border-radius: 28px; font-size: 12px; font-weight: 500; color: #555; cursor: pointer; transition: all 0.2s; }
.tab22.active { background: #1ab3c8; color: #fff; }
.chart-wrapper { position: relative; height: 220px; margin-bottom: 10px; }
.chart-legend { display: flex; gap: 20px; justify-content: center; margin-bottom: 14px; font-size: 13px; }
.legend-dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; margin-right: 5px; vertical-align: middle; }
.quran-box { background: #eef7fc; border-left: 4px solid #1ab3c8; border-radius: 10px; padding: 14px 16px; margin-bottom: 18px; font-style: italic; font-size: 14px; color: #333; line-height: 1.6; text-align: center; }
.quran-box span { display: block; font-size: 12px; color: #888; font-style: normal; margin-top: 4px; }
.reward-list { display: flex; flex-direction: column; gap: 10px; margin-bottom: 18px; }
.reward-item { display: flex; align-items: center; gap: 14px; background: #f7fbfd; border: 1px solid #d5edf5; border-left: 3px solid #1ab3c8; border-radius: 10px; padding: 12px 14px; font-size: 14px; color: #222; }
.reward-icon { width: 38px; height: 38px; background: #daf3f8; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.reward-icon svg { width: 20px; height: 20px; stroke: #1ab3c8; fill: none; stroke-width: 2; }
.transform-section { margin-top: 10px; }
.transform-title { font-size: 16px; font-weight: 700; color: #1a1a2e; text-align: center; margin-bottom: 14px; }
.bar-row22 { margin-bottom: 14px; }
.bar-label22 { display: flex; justify-content: space-between; font-size: 14px; font-weight: 600; color: #333; margin-bottom: 6px; }
.bar-label22 span.pct-red { color: #e05a5a; }
.bar-label22 span.pct-teal { color: #1ab3c8; }
.bar-track22 { height: 12px; background: #eee; border-radius: 8px; overflow: hidden; }
.bar-fill22 { height: 12px; border-radius: 8px; width: 0; transition: width 1.4s cubic-bezier(.22,.68,0,1.2); }
.bar-red22 { background: #e05a5a; }
.bar-teal22 { background: #1ab3c8; }
.feature-list { display: flex; flex-direction: column; gap: 0; }
.feature-item { display: flex; align-items: flex-start; gap: 14px; padding: 14px 0; border-bottom: 1px solid #f0f0f0; cursor: pointer; }
.feature-item:last-child { border-bottom: none; }
.feat-icon { width: 42px; height: 42px; background: #daf3f8; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.feat-icon svg { width: 22px; height: 22px; stroke: #1ab3c8; fill: none; stroke-width: 1.8; }
.feat-text h4 { font-size: 15px; font-weight: 700; color: #1a1a2e; margin-bottom: 2px; }
.feat-text p { font-size: 13px; color: #777; line-height: 1.5; }
.feat-chevron { margin-left: auto; color: #bbb; font-size: 18px; padding-top: 2px; }
.lesson-list { display: flex; flex-direction: column; gap: 12px; }
.lesson-item { display: flex; align-items: center; gap: 14px; background: #fff; border: 1px solid #e0e0e0; border-radius: 14px; padding: 16px; cursor: pointer; }
.lesson-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.lesson-icon.teal { background: #daf3f8; }
.lesson-icon.green { background: #d8f3e9; }
.lesson-icon.orange { background: #fef3e0; }
.lesson-icon svg { width: 22px; height: 22px; stroke-width: 1.8; fill: none; }
.lesson-icon.teal svg { stroke: #1ab3c8; }
.lesson-icon.green svg { stroke: #22a06b; }
.lesson-icon.orange svg { stroke: #f59e0b; }
.lesson-label { font-size: 15px; font-weight: 600; color: #1a1a2e; flex: 1; }
.lesson-arrow { color: #1ab3c8; font-size: 20px; }
.cta-btn { background: linear-gradient(135deg, #1ab3c8, #0e8fa0); color: #fff; border: none; border-radius: 16px; font-size: 17px; font-weight: 600; padding: 17px; width: 100%; cursor: pointer; margin-top: auto; }
.pur-screen22 { display: none; flex-direction: column; min-height: 700px; background: #0d1b2e; }
.pur-screen22.active { display: flex; }
.pur-dots22 { display: flex; gap: 8px; padding: 18px 20px 8px; align-items: center; }
.pur-dot22 { width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.3); transition: background 0.3s; }
.pur-dot22.active { background: #1ab3c8; }
.pur-back22 { background: none; border: none; color: rgba(255,255,255,0.6); font-size: 22px; cursor: pointer; padding: 0; margin-right: 4px; line-height: 1; }
.pur-dots-row22 { display: flex; align-items: center; }
.pur-body22 { padding: 20px 22px 24px; flex: 1; display: flex; flex-direction: column; overflow-y: auto; }
.pur-tag22 { font-size: 11px; font-weight: 700; letter-spacing: 1.5px; color: #1ab3c8; margin-bottom: 18px; text-transform: uppercase; }
.pur-text22 { font-size: 22px; font-weight: 700; color: #ffffff; line-height: 1.55; flex: 1; }
.pur-textarea22 { width: 100%; flex: 1; background: transparent; border: none; outline: none; color: #ffffff; font-size: 18px; font-weight: 500; line-height: 1.6; resize: none; min-height: 300px; }
.pur-textarea22::placeholder { color: rgba(255,255,255,0.3); }
.pur-continue22:disabled { background: #2a3a4a; color: #556677; cursor: not-allowed; }
.pur-continue22 { background: #1ab3c8; color: #fff; border: none; border-radius: 14px; font-size: 17px; font-weight: 600; padding: 17px; width: 100%; cursor: pointer; margin-top: 16px; flex-shrink: 0; }
.bf-screen22 { display: none; flex-direction: column; min-height: 700px; background: #0d1b2e; }
.bf-screen22.active { display: flex; }
.dr-screen22 { display: none; flex-direction: column; min-height: 700px; background: #0d1b2e; }
.dr-screen22.active { display: flex; }
@keyframes fadeInUp22 { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
.screen22.active .screen-body > * { animation: fadeInUp22 0.35s ease both; }

.p4app{max-width:390px;margin:0 auto;background:#fff;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;border-radius:28px;border:0.5px solid #d0d8e4;overflow:hidden;}
.p4prog-wrap{padding:12px 16px 2px}
.p4prog-track{background:#E5E7EB;border-radius:999px;height:6px;position:relative}
.p4prog-fill{background:#0EA5C9;border-radius:999px;height:6px;transition:width .4s}
.p4prog-dot{position:absolute;right:-7px;top:-5px;width:16px;height:16px;border-radius:50%;background:#0EA5C9;border:2.5px solid white}
.p4prog-lbl{text-align:right;font-size:12px;color:#6B7280;margin-top:5px}
.p4screen{padding:18px 18px 28px;display:none;flex-direction:column;gap:15px}
.p4screen.active{display:flex}
.p4app h1{font-size:23px;font-weight:800;color:#111827;line-height:1.3}
.p4sub{color:#6B7280;font-size:14px;line-height:1.6}
.p4btn{width:100%;padding:15px;border-radius:14px;border:none;background:linear-gradient(90deg,#0EA5C9,#06B6D4);color:white;font-size:16px;font-weight:700;cursor:pointer}
.p4btn:active{opacity:.85}
.p4card{background:white;border:1px solid #E5E7EB;border-radius:14px;padding:15px;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.p4qbox{background:#F0FBFF;border-left:4px solid #0EA5C9;border-radius:0 10px 10px 0;padding:14px 16px;font-style:italic;font-size:13.5px;color:#374151;line-height:1.6}
.p4qsrc{margin-top:6px;font-style:normal;font-size:12px;font-weight:600;color:#6B7280}
.p4tog{width:44px;height:26px;border-radius:13px;background:#D1D5DB;position:relative;cursor:pointer;flex-shrink:0;transition:background .2s}
.p4tog.on{background:#0EA5C9}
.p4togdot{width:20px;height:20px;border-radius:50%;background:white;position:absolute;top:3px;left:3px;transition:left .2s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.p4tog.on .p4togdot{left:21px}
.p4chip{padding:8px 16px;border-radius:999px;border:2px solid #D1D5DB;background:white;color:#374151;font-size:13px;font-weight:600;cursor:pointer}
.p4chip.sel{border-color:#0EA5C9;background:#E0F7FA;color:#0EA5C9}
.p4swcard{background:white;border-radius:18px;border:2.5px solid #0EA5C9;padding:22px 20px;box-shadow:4px 4px 0 #E5E7EB;user-select:none;cursor:grab}
.p4jdot{height:10px;border-radius:999px;background:#D1FAE5;cursor:pointer;transition:all .25s}
.p4jdot.on{background:#0EA5C9;width:22px!important}
.p4ibox{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.p4step-c{width:34px;height:34px;border-radius:50%;background:#E0F7FA;color:#0EA5C9;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0;border:1.5px solid #0EA5C9}
.p4step-c.done{background:#0EA5C9;color:white;border-color:#0EA5C9}
.p4cal-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.45);display:flex;align-items:flex-end;justify-content:center;z-index:999}
.p4cal-sheet{background:white;border-radius:20px 20px 0 0;padding:20px;width:100%;max-width:390px}
.p4cal-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
.p4cal-nav{width:36px;height:36px;border-radius:50%;border:1px solid #E5E7EB;background:white;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:16px;color:#374151}
.p4cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;text-align:center}
.p4cal-day-name{font-size:11px;font-weight:600;color:#9CA3AF;padding:4px 0}
.p4cal-day{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;cursor:pointer;margin:0 auto;color:#374151}
.p4cal-day:hover{background:#E0F7FA;color:#0EA5C9}
.p4cal-day.today{border:1.5px solid #0EA5C9;color:#0EA5C9;font-weight:700}
.p4cal-day.selected{background:#0EA5C9;color:white;font-weight:700}
.p4cal-day.other-month{color:#D1D5DB}
.p4cal-day.past{color:#D1D5DB;cursor:default}
.p4cal-day.past:hover{background:transparent;color:#D1D5DB}

/* ============================================================ */
/* === MASTER UNIFIED RESPONSIVE SIZING FOR ALL 31 ONBOARDING SCREENS === */
/* ============================================================ */
#onboardingFlowContainer {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  height: 100dvh !important;
  z-index: 9990 !important;
  background: #f1f5f9 !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch !important;
  margin: 0 !important;
  padding: 0 !important;
}

#onboardingFlowContainer > div {
  width: 100% !important;
  min-height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start !important;
  padding: 0 !important;
  margin: 0 !important;
}

.splash,
.p1-wrap,
.urge-screen,
.p2-wrap,
#phase3-wrap,
#phase3-wrap .phone,
#phase4-wrap,
.p4app {
  width: 100% !important;
  max-width: 430px !important;
  margin: 0 auto !important;
  box-sizing: border-box !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch !important;
}

.screen-p1,
.screen,
.screen22,
.pur-screen22,
.bf-screen22,
.dr-screen22 {
  min-height: 100vh !important;
  min-height: 100dvh !important;
  box-sizing: border-box !important;
  display: flex !important;
  flex-direction: column !important;
  padding-bottom: calc(24px + env(safe-area-inset-bottom, 0px)) !important;
}

.screen22:not(.active),
.pur-screen22:not(.active),
.bf-screen22:not(.active),
.dr-screen22:not(.active),
.screen:not(.active),
.screen-p1:not(.active) {
  display: none !important;
}

@media (max-width: 480px) {
  #onboardingFlowContainer {
    background: #ffffff !important;
  }
  .splash,
  .p1-wrap,
  .urge-screen,
  .p2-wrap,
  #phase3-wrap,
  #phase3-wrap .phone,
  #phase4-wrap,
  .p4app {
    width: 100% !important;
    max-width: 100% !important;
    min-height: 100vh !important;
    min-height: 100dvh !important;
    border-radius: 0 !important;
    border: none !important;
    box-shadow: none !important;
    margin: 0 !important;
  }
  .splash {
    height: 100vh !important;
    height: 100dvh !important;
  }
}

@media (min-width: 481px) {
  .splash,
  .p1-wrap,
  .urge-screen,
  .p2-wrap,
  #phase3-wrap .phone,
  .p4app {
    min-height: calc(100vh - 32px) !important;
    min-height: calc(100dvh - 32px) !important;
    border-radius: 28px !important;
    border: 1px solid #d0d8e4 !important;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.12) !important;
    margin: 16px auto !important;
  }
  .splash {
    height: calc(100vh - 32px) !important;
    height: calc(100dvh - 32px) !important;
  }
}
"""

FULL_ONBOARDING_HTML = """<!-- ============================================================ -->
<!-- ===  FULL 31-STEP ONBOARDING JOURNEY (FROM USER SETUP)   === -->
<!-- ============================================================ -->
<div id="onboardingFlowContainer" style="display: none; width: 100%; min-height: 100vh; position: fixed; top: 0; left: 0; z-index: 9990; background: #dde4ed; overflow-y: auto; -webkit-overflow-scrolling: touch; justify-content: center; align-items: flex-start;">
  <div style="width: 100%; display: flex; flex-direction: column; align-items: center; padding-bottom: 40px;">
<!-- ============================================================ -->
<!-- PHASE 1: Splash + Q1-Q6 + Results + Gender + Urge tools     -->
<!-- ============================================================ -->

<!-- SPLASH -->
<div id="splash-screen" class="splash">
  <svg class="splash-bg" viewBox="0 0 340 680" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <rect width="340" height="680" fill="#00bfa5"/>
    <rect width="340" height="320" fill="#00e5cc" opacity="0.5"/>
    <ellipse cx="240" cy="60" rx="55" ry="32" fill="rgba(255,255,255,0.55)"/>
    <ellipse cx="270" cy="50" rx="40" ry="28" fill="rgba(255,255,255,0.6)"/>
    <ellipse cx="215" cy="55" rx="30" ry="22" fill="rgba(255,255,255,0.5)"/>
    <ellipse cx="310" cy="110" rx="35" ry="22" fill="rgba(255,255,255,0.45)"/>
    <path d="M-10 680 L-10 300 Q30 180 120 260 Q160 300 140 680 Z" fill="#0a0e1a"/>
    <path d="M80 680 Q140 400 220 350 Q290 310 340 360 L340 680 Z" fill="#1a3a6b" opacity="0.9"/>
    <path d="M100 680 Q180 420 260 370 Q310 345 340 380 L340 680 Z" fill="#1e4080" opacity="0.7"/>
    <path d="M120 680 Q200 460 280 410 Q320 390 340 410 L340 680 Z" fill="#2a5298" opacity="0.6"/>
    <path d="M0 580 Q80 550 160 565 Q240 580 340 555 L340 680 L0 680 Z" fill="#060810"/>
    <rect x="238" y="490" width="7" height="80" fill="#1a2e1a"/>
    <ellipse cx="241" cy="470" rx="22" ry="30" fill="#2d5a1b" opacity="0.9"/>
    <ellipse cx="30" cy="600" rx="28" ry="18" fill="#1a3a1a" opacity="0.9"/>
    <ellipse cx="300" cy="610" rx="20" ry="12" fill="#1a3a1a" opacity="0.7"/>
    <defs>
      <linearGradient id="fg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#0a0e1a" stop-opacity="0"/>
        <stop offset="60%" stop-color="#0a0e1a" stop-opacity="0.85"/>
        <stop offset="100%" stop-color="#0a0e1a" stop-opacity="1"/>
      </linearGradient>
    </defs>
    <rect x="0" y="420" width="340" height="260" fill="url(#fg)"/>
  </svg>
  <div class="splash-content">
    <div class="main-title">Your Heart<br>Deserves Freedom</div>
    <div class="sub-text">Most people don't know they can truly recover.<br>With Allah's mercy, you can.</div>
    <button class="btn-journey" onclick="showQ()">Start Your Journey</button>
    <div class="signin-text">Already have an account? <strong onclick="openAuthModal()" style="cursor:pointer; text-decoration:underline;">Sign In</strong></div>
  </div>
</div>

<!-- Q1-Q5 -->
<div id="q-screen" class="p1-wrap hidden">
  <div class="screen-p1 active">
    <div class="progress-bar-track"><div class="progress-bar-fill" id="prog-bar" style="width:16.6%"></div></div>
    <div class="page-count">1 of 31</div>
    <div class="circle-area"><div class="big-circle"><div class="q-badge" id="q-badge">Q1</div></div></div>
    <div class="card-title">Let's Find Out If You Have a Problem with Porn</div>
    <div class="q-count-row">
      <span class="q-count-text" id="q-count-text">Question 1 of 6</span>
      <div class="underline-blue" id="underline-blue" style="width:28px"></div>
      <div class="line-gray"></div>
    </div>
    <div class="question-text" id="q-text">Do you watch pornography more than once a week?</div>
    <div class="help-text" id="q-help">Your answers help us support you better.</div>
    <div class="options-area">
      <button class="option-btn" onclick="answer(true)">
        <div class="option-icon"><i class="ti ti-check" aria-hidden="true"></i></div>
        <span class="option-label">Yes</span>
      </button>
      <button class="option-btn" onclick="answer(false)">
        <div class="option-icon"><i class="ti ti-x" aria-hidden="true"></i></div>
        <span class="option-label">No</span>
      </button>
    </div>
  </div>
</div>

<!-- Q6 -->
<div id="q6-screen" class="p1-wrap hidden">
  <div class="screen-p1 active">
    <div class="progress-bar-track"><div class="progress-bar-fill" style="width:100%"></div></div>
    <div class="page-count">1 of 31</div>
    <div class="circle-area"><div class="big-circle"><div class="q-badge">Q6</div></div></div>
    <div class="card-title">Let's Find Out If You Have a Problem with Porn</div>
    <div class="q-count-row">
      <span class="q-count-text">Question 6 of 6</span>
      <div class="underline-blue" style="width:110px"></div>
      <div class="line-gray" style="flex:0"></div>
    </div>
    <div class="question-text">How often do you watch pornography?</div>
    <div class="help-text">Be honest — this helps us understand your situation.</div>
    <div class="options-area">
      <button class="option-btn-multi" onclick="goResults(4)"><div class="opt-title">Daily</div><div class="opt-sub">Every day or almost every day</div></button>
      <button class="option-btn-multi" onclick="goResults(3)"><div class="opt-title">Weekly</div><div class="opt-sub">Several times a week</div></button>
      <button class="option-btn-multi" onclick="goResults(2)"><div class="opt-title">Monthly</div><div class="opt-sub">A few times a month</div></button>
      <button class="option-btn-multi" onclick="goResults(1)"><div class="opt-title">Rarely</div><div class="opt-sub">Occasionally or trying to quit</div></button>
    </div>
  </div>
</div>

<!-- RESULTS -->
<div id="results-screen" class="p1-wrap hidden">
  <div class="screen-p1 active">
    <div class="progress-bar-track" style="flex-shrink:0"><div class="progress-bar-fill" style="width:100%"></div></div>
    <div class="results-inner">
      <div style="width:100%; text-align:right; font-size:12px; color:#9aa3b2; padding-top:5px;">1 of 31</div>
      <div class="score-circle" id="score-display">0/6</div>
      <div class="results-title">Your Assessment Results</div>
      <div class="impact-card">
        <div class="impact-row">
          <div class="impact-label-row"><span class="impact-label">Mental Impact</span><span class="impact-pct-red" id="mental-pct">0%</span></div>
          <div class="bar-track-p1"><div class="bar-fill-p1 bar-fill-red" id="bar-mental"></div></div>
        </div>
        <div class="impact-row">
          <div class="impact-label-row"><span class="impact-label">Spiritual Impact</span><span class="impact-pct-blue" id="spiritual-pct">0%</span></div>
          <div class="bar-track-p1"><div class="bar-fill-p1 bar-fill-blue" id="bar-spiritual"></div></div>
        </div>
        <div class="impact-row">
          <div class="impact-label-row"><span class="impact-label">Relational Impact</span><span class="impact-pct-blue" id="relational-pct">0%</span></div>
          <div class="bar-track-p1"><div class="bar-fill-p1 bar-fill-blue" id="bar-relational"></div></div>
        </div>
      </div>
      <div class="result-desc" id="result-desc"></div>
      <div class="quran-card-p1">
        <div class="quran-text">"And whoever relies upon Allah - then He is sufficient for him"</div>
        <div class="quran-ref">Surah At-Talaq 65:3</div>
      </div>
      <button class="btn-continue" onclick="showGender()">Continue</button>
    </div>
  </div>
</div>

<!-- GENDER -->
<div id="gender-screen" class="p1-wrap hidden">
  <div class="screen-p1 active">
    <div class="progress-bar-track"><div class="progress-bar-fill" style="width:6.4%"></div></div>
    <div class="page-count">2 of 31</div>
    <div class="gender-body">
      <div class="gender-title">Join Your Community</div>
      <div class="gender-sub">Choose your gender to connect with a safe, like-minded community.</div>
      <div class="gender-cards">
        <div class="gender-card selected" id="card-male" onclick="selectGender('male')">
          <div class="gender-avatar"><i class="ti ti-user" aria-hidden="true"></i></div>
          <div class="gender-label">Male</div>
        </div>
        <div class="gender-card" id="card-female" onclick="selectGender('female')">
          <div class="gender-avatar"><i class="ti ti-user-circle" aria-hidden="true"></i></div>
          <div class="gender-label">Female</div>
        </div>
      </div>
      <div class="quran-card-p1">
        <div class="quran-text">"Guard your modesty. That is purer for them. Surely Allah is All-Aware of what they do"</div>
        <div class="quran-ref">Surah An-Nur 24:30-31</div>
      </div>
      <button class="btn-continue" onclick="showUrge()">Continue</button>
    </div>
  </div>
</div>

<!-- URGE SCREEN -->
<div id="urge-screen" class="urge-screen hidden">
  <svg class="urge-bg" viewBox="0 0 340 680" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <rect width="340" height="680" fill="#ddd4e4"/>
    <rect width="340" height="420" fill="#e8e0f0"/>
    <path d="M-10 430 Q60 290 140 330 Q190 355 230 300 Q280 240 360 330 L360 680 L-10 680 Z" fill="#c8a0b8" opacity="0.55"/>
    <path d="M-10 450 Q50 330 120 365 Q170 390 210 345 Q260 295 360 365 L360 680 L-10 680 Z" fill="#b890a8" opacity="0.45"/>
    <path d="M-10 530 Q80 480 180 500 Q260 515 360 485 L360 680 L-10 680 Z" fill="#a8c878" opacity="0.85"/>
    <path d="M-10 565 Q80 545 200 558 Q270 565 360 548 L360 680 L-10 680 Z" fill="#90b860"/>
    <path d="M-10 595 Q80 578 200 585 Q270 590 360 575 L360 680 L-10 680 Z" fill="#7aaa50"/>
    <rect x="0" y="0" width="340" height="300" fill="rgba(50,30,70,0.28)"/>
  </svg>
  <div class="urge-top">
    <div class="urge-prog-track"><div class="urge-prog-fill"></div></div>
    <div class="urge-page-count">4 of 31</div>
    <div class="urge-title">Let's handle an urge together</div>
    <div class="urge-sub">Your urge is peaking. Pick a tool and bring it down.</div>
    <div class="urge-pct-text" id="urge-pct-text">0%</div>
    <div class="urge-bar-track"><div class="urge-bar-fill" id="urge-bar"></div></div>
  </div>
  <div style="flex:1;"></div>
  <div class="urge-cards-area">
    <button class="urge-card" id="card-dhikr" onclick="showDhikr()">
      <div class="urge-icon-circle">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#2e7d5a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M8 13V6.5a1 1 0 0 1 2 0V12"/><path d="M10 5.5a1 1 0 0 1 2 0V12"/>
          <path d="M12 5.5a1 1 0 0 1 2 0V12"/><path d="M14 6.5a1 1 0 0 1 2 0V14a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5v-3a1 1 0 0 1 2 0"/>
        </svg>
      </div>
      <div class="urge-card-label">Make Dhikr</div>
    </button>
    <button class="urge-card" id="card-breathe" onclick="showBreathe()">
      <div class="urge-icon-circle">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#2e7d5a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M5 8c.667-1.333 2-2 4-2s3.333.667 4 2c.667 1.333 2 2 4 2"/>
          <path d="M5 12c.667-1.333 2-2 4-2s3.333.667 4 2c.667 1.333 2 2 4 2"/>
          <path d="M5 16c.667-1.333 2-2 4-2s3.333.667 4 2c.667 1.333 2 2 4 2"/>
        </svg>
      </div>
      <div class="urge-card-label">Breathe</div>
    </button>
    <button class="urge-card" id="card-dua" onclick="showDua()">
      <div class="urge-icon-circle">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#2e7d5a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M3 19a9 9 0 0 1 9 0 9 9 0 0 1 9 0"/><path d="M3 6a9 9 0 0 1 9 0 9 9 0 0 1 9 0"/>
          <line x1="3" y1="6" x2="3" y2="19"/><line x1="12" y1="6" x2="12" y2="19"/><line x1="21" y1="6" x2="21" y2="19"/>
        </svg>
      </div>
      <div class="urge-card-label">Du'ā</div>
    </button>
  </div>
</div>

<!-- DHIKR SCREEN -->
<div id="dhikr-screen" class="urge-screen hidden">
  <svg class="urge-bg" viewBox="0 0 340 680" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <rect width="340" height="680" fill="#ddd4e4"/>
    <rect width="340" height="420" fill="#e8e0f0"/>
    <path d="M-10 430 Q60 290 140 330 Q190 355 230 300 Q280 240 360 330 L360 680 L-10 680 Z" fill="#c8a0b8" opacity="0.55"/>
    <path d="M-10 530 Q80 480 180 500 Q260 515 360 485 L360 680 L-10 680 Z" fill="#a8c878" opacity="0.85"/>
    <path d="M-10 565 Q80 545 200 558 Q270 565 360 548 L360 680 L-10 680 Z" fill="#90b860"/>
    <rect x="0" y="0" width="340" height="300" fill="rgba(50,30,70,0.28)"/>
  </svg>
  <div style="position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;min-height:680px;font-family:'Inter',sans-serif;">
    <div style="width:100%;padding:0 18px;">
      <div style="width:100%;height:5px;background:rgba(255,255,255,0.25);border-radius:3px;margin-top:10px;">
        <div style="height:5px;background:#00bcd4;border-radius:3px;width:13.7%;"></div>
      </div>
      <div style="text-align:right;font-size:12px;color:rgba(255,255,255,0.65);padding:4px 0 0;">4 of 31</div>
    </div>
    <div style="font-size:22px;font-weight:800;color:white;text-align:center;margin:14px 20px 4px;line-height:1.25;">Let's handle an urge together</div>
    <div style="font-size:13px;color:rgba(255,255,255,0.8);text-align:center;margin-bottom:12px;">Watch your urge drop as you engage.</div>
    <div style="font-size:46px;font-weight:800;color:white;text-align:center;line-height:1;" id="zk-urge-pct">75%</div>
    <div style="width:290px;margin:8px 0 18px;">
      <div style="height:12px;background:rgba(255,255,255,0.25);border-radius:6px;overflow:hidden;">
        <div id="zk-urge-bar" style="height:12px;border-radius:6px;background:#e53e3e;width:75%;transition:width 0.4s ease;"></div>
      </div>
    </div>
    <div id="zk-dhikr-block" style="display:flex;flex-direction:column;align-items:center;width:100%;padding:0 20px;">
      <div style="font-size:15px;font-weight:700;color:white;text-align:center;margin-bottom:12px;">Make Dhikr</div>
      <div style="width:100%;background:white;border-radius:18px;padding:20px 18px 16px;margin-bottom:12px;text-align:center;">
        <div id="zk-arabic" style="font-size:28px;color:#1a1a2e;margin-bottom:6px;font-weight:700;">سُبْحَانَ اللّٰهُ</div>
        <div id="zk-text" style="font-size:20px;font-weight:800;color:#2196F3;margin-bottom:4px;">SubhanAllah</div>
        <div id="zk-meaning" style="font-size:13px;color:#8a99bb;">Glory be to Allah</div>
      </div>
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
        <div id="zk-counter" style="font-size:22px;font-weight:800;color:white;min-width:90px;text-align:center;background:rgba(255,255,255,0.18);border-radius:12px;padding:8px 16px;">0 / 33</div>
      </div>
      <div style="display:flex;gap:8px;margin-bottom:6px;width:100%;">
        <div style="flex:1;text-align:center;padding:6px 4px;border-radius:10px;background:rgba(255,255,255,0.15);">
          <div style="font-size:10px;color:rgba(255,255,255,0.6);margin-bottom:2px;">SubhanAllah</div>
          <div style="font-size:13px;font-weight:700;color:white;" id="zk-p1-done">0/33</div>
        </div>
        <div style="flex:1;text-align:center;padding:6px 4px;border-radius:10px;background:rgba(255,255,255,0.15);">
          <div style="font-size:10px;color:rgba(255,255,255,0.6);margin-bottom:2px;">Alhamdulillah</div>
          <div style="font-size:13px;font-weight:700;color:white;" id="zk-p2-done">0/33</div>
        </div>
        <div style="flex:1;text-align:center;padding:6px 4px;border-radius:10px;background:rgba(255,255,255,0.15);">
          <div style="font-size:10px;color:rgba(255,255,255,0.6);margin-bottom:2px;">Allahu Akbar</div>
          <div style="font-size:13px;font-weight:700;color:white;" id="zk-p3-done">0/34</div>
        </div>
      </div>
      <button id="zk-tap-btn" onclick="tapDhikr()" style="width:100%;padding:18px;background:#00bcd4;color:white;font-size:18px;font-weight:800;border:none;border-radius:16px;cursor:pointer;font-family:'Inter',sans-serif;margin-top:8px;transition:transform 0.1s;">Tap to Recite</button>
    </div>
    <div id="zk-done-block" style="display:none;flex-direction:column;align-items:center;width:100%;padding:0 20px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;">
        <div style="width:28px;height:28px;border-radius:50%;border:2.5px solid #00bcd4;display:flex;align-items:center;justify-content:center;"><i class="ti ti-check" style="font-size:16px;color:#00bcd4;" aria-hidden="true"></i></div>
        <div style="font-size:15px;font-weight:800;color:white;">You are not controlled by urges.</div>
      </div>
      <div style="width:100%;background:rgba(255,255,255,0.75);border-left:4px solid #00bcd4;border-radius:0 12px 12px 0;padding:14px 16px;margin-bottom:20px;text-align:center;">
        <div style="font-size:13px;font-style:italic;color:#1a2d5a;line-height:1.6;">"And seek help through patience and prayer"</div>
        <div style="font-size:12px;font-weight:700;color:#4a6fa5;margin-top:6px;">Surah Al-Baqarah 2:45</div>
      </div>
      <button class="btn-continue" onclick="showUsername()">Continue</button>
    </div>
  </div>
</div>

<!-- DUA SCREEN -->
<div id="dua-screen" class="urge-screen hidden">
  <svg class="urge-bg" viewBox="0 0 340 680" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <rect width="340" height="680" fill="#ddd4e4"/>
    <rect width="340" height="420" fill="#e8e0f0"/>
    <path d="M-10 430 Q60 290 140 330 Q190 355 230 300 Q280 240 360 330 L360 680 L-10 680 Z" fill="#c8a0b8" opacity="0.55"/>
    <path d="M-10 530 Q80 480 180 500 Q260 515 360 485 L360 680 L-10 680 Z" fill="#a8c878" opacity="0.85"/>
    <path d="M-10 565 Q80 545 200 558 Q270 565 360 548 L360 680 L-10 680 Z" fill="#90b860"/>
    <rect x="0" y="0" width="340" height="300" fill="rgba(50,30,70,0.28)"/>
  </svg>
  <div style="position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;min-height:680px;font-family:'Inter',sans-serif;">
    <div style="width:100%;padding:0 18px;">
      <div style="width:100%;height:5px;background:rgba(255,255,255,0.25);border-radius:3px;margin-top:10px;"><div style="height:5px;background:#00bcd4;border-radius:3px;width:13.7%;"></div></div>
      <div style="text-align:right;font-size:12px;color:rgba(255,255,255,0.65);padding:4px 0 0;">4 of 31</div>
    </div>
    <div style="font-size:24px;font-weight:800;color:white;text-align:center;margin:18px 20px 6px;line-height:1.25;">Let's handle an urge together</div>
    <div style="font-size:13px;color:rgba(255,255,255,0.8);text-align:center;margin-bottom:14px;">Watch your urge drop as you engage.</div>
    <div style="font-size:48px;font-weight:800;color:white;text-align:center;line-height:1;" id="d-urge-pct">75%</div>
    <div style="width:290px;margin:10px 0 22px;">
      <div style="height:12px;background:rgba(255,255,255,0.25);border-radius:6px;overflow:hidden;">
        <div id="d-urge-bar" style="height:12px;border-radius:6px;background:#e53e3e;width:75%;transition:width 0.5s ease;"></div>
      </div>
    </div>
    <div id="d-dua-block" style="display:flex;flex-direction:column;align-items:center;width:100%;padding:0 20px;">
      <div style="font-size:16px;font-weight:800;color:white;text-align:center;margin-bottom:14px;">Seek Allah's protection</div>
      <div style="width:100%;background:white;border-radius:16px;padding:20px 18px;margin-bottom:10px;">
        <div id="d-dua-text" style="font-size:16px;font-weight:600;color:#1a1a2e;line-height:1.5;">Astaghfirullah (I seek forgiveness from Allah)</div>
      </div>
      <div style="font-size:13px;color:rgba(255,255,255,0.7);margin-bottom:18px;">Recite slowly, focus on Allah's mercy</div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
        <div id="d-count-display" style="font-size:18px;font-weight:800;color:white;min-width:80px;text-align:center;background:rgba(255,255,255,0.15);border-radius:10px;padding:8px 14px;">0 / 10</div>
      </div>
      <button id="d-recite-btn" onclick="reciteDua()" style="width:180px;padding:16px;background:#00bcd4;color:white;font-size:17px;font-weight:700;border:none;border-radius:16px;cursor:pointer;font-family:'Inter',sans-serif;margin-top:10px;">Recite</button>
    </div>
    <div id="d-done-block" style="display:none;flex-direction:column;align-items:center;width:100%;padding:0 20px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;">
        <div style="width:28px;height:28px;border-radius:50%;border:2.5px solid #00bcd4;display:flex;align-items:center;justify-content:center;"><i class="ti ti-check" style="font-size:16px;color:#00bcd4;" aria-hidden="true"></i></div>
        <div style="font-size:15px;font-weight:800;color:white;">You are not controlled by urges.</div>
      </div>
      <div style="width:100%;background:rgba(255,255,255,0.75);border-left:4px solid #00bcd4;border-radius:0 12px 12px 0;padding:14px 16px;margin-bottom:20px;text-align:center;">
        <div style="font-size:13px;font-style:italic;color:#1a2d5a;line-height:1.6;">"And seek help through patience and prayer"</div>
        <div style="font-size:12px;font-weight:700;color:#4a6fa5;margin-top:6px;">Surah Al-Baqarah 2:45</div>
      </div>
      <button class="btn-continue" onclick="showUsername()">Continue</button>
    </div>
  </div>
</div>

<!-- BREATHE SCREEN -->
<div id="breathe-screen" class="urge-screen hidden">
  <svg class="urge-bg" viewBox="0 0 340 680" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <rect width="340" height="680" fill="#ddd4e4"/>
    <rect width="340" height="420" fill="#e8e0f0"/>
    <path d="M-10 420 Q60 280 140 320 Q190 350 230 290 Q280 230 360 320 L360 680 L-10 680 Z" fill="#c8a0b8" opacity="0.55"/>
    <path d="M-10 520 Q80 470 180 490 Q260 505 360 475 L360 680 L-10 680 Z" fill="#a8c878" opacity="0.85"/>
    <path d="M-10 560 Q80 540 200 555 Q270 563 360 545 L360 680 L-10 680 Z" fill="#90b860"/>
  </svg>
  <div style="position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;min-height:680px;font-family:'Inter',sans-serif;padding:0 20px;">
    <div style="width:100%;padding:0;margin-top:10px;">
      <div style="width:100%;height:5px;background:rgba(255,255,255,0.35);border-radius:3px;"><div style="height:5px;background:#00bcd4;border-radius:3px;width:13.7%;"></div></div>
      <div style="text-align:right;font-size:12px;color:rgba(80,60,100,0.7);padding:4px 0 0;">4 of 31</div>
    </div>
    <div style="font-size:22px;font-weight:800;color:white;text-align:center;margin:16px 0 6px;line-height:1.3;">Breathing Exercise</div>
    <div style="font-size:13px;color:rgba(255,255,255,0.8);text-align:center;margin-bottom:14px;">Watch your urge drop as you breathe.</div>
    <div style="font-size:46px;font-weight:800;color:white;text-align:center;" id="b-urge-pct">75%</div>
    <div style="width:100%;margin:8px 0 18px;">
      <div style="height:12px;background:rgba(255,255,255,0.3);border-radius:6px;overflow:hidden;">
        <div id="b-urge-bar" style="height:12px;border-radius:6px;background:#e53e3e;width:75%;transition:width 0.4s ease;"></div>
      </div>
    </div>
    <div id="b-breathe-block" style="display:flex;flex-direction:column;align-items:center;width:100%;">
      <div id="b-circle" style="width:150px;height:150px;border-radius:50%;border:4px solid #2196F3;display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:18px;transition:border-color 0.5s;">
        <div id="b-phase-name" style="font-size:20px;font-weight:800;color:#2196F3;transition:color 0.5s;">INHALE</div>
        <div id="b-phase-num" style="font-size:42px;font-weight:900;color:#1a1a2e;">4</div>
        <div id="b-phase-hint" style="font-size:12px;color:#888;font-weight:600;">through nose</div>
      </div>
      <div style="font-size:13px;color:rgba(255,255,255,0.7);text-align:center;">Follow the breathing pattern. 3 rounds total.</div>
    </div>
    <div id="b-done-block" style="display:none;flex-direction:column;align-items:center;width:100%;margin-top:20px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;">
        <div style="width:28px;height:28px;border-radius:50%;border:2.5px solid #00bcd4;display:flex;align-items:center;justify-content:center;"><i class="ti ti-check" style="font-size:16px;color:#00bcd4;"></i></div>
        <div style="font-size:15px;font-weight:800;color:white;">You are not controlled by urges.</div>
      </div>
      <div style="width:100%;background:rgba(255,255,255,0.75);border-left:4px solid #00bcd4;border-radius:0 12px 12px 0;padding:14px 16px;margin-bottom:20px;text-align:center;">
        <div style="font-size:13px;font-style:italic;color:#1a2d5a;line-height:1.6;">"And seek help through patience and prayer"</div>
        <div style="font-size:12px;font-weight:700;color:#4a6fa5;margin-top:6px;">Surah Al-Baqarah 2:45</div>
      </div>
      <button class="btn-continue" onclick="showUsername()">Continue</button>
    </div>
  </div>
</div>

<!-- USERNAME SCREEN -->
<div id="username-screen" class="p1-wrap hidden">
  <div class="screen-p1 active">
    <div class="progress-bar-track"><div class="progress-bar-fill" style="width:16.1%"></div></div>
    <div class="page-count">5 of 31</div>
    <div style="flex:1;display:flex;flex-direction:column;padding:0 22px 32px;">
      <div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
        <div style="font-size:24px;font-weight:800;color:#1a1a2e;text-align:center;margin-bottom:14px;line-height:1.3;">Choose Your Username</div>
        <div style="font-size:15px;font-weight:700;color:#1a1a2e;text-align:center;line-height:1.55;margin-bottom:32px;">This appears on leaderboards and forums.<br>Avoid real names for privacy. Keep it respectful.</div>
        <div style="position:relative;margin-bottom:6px;">
          <input id="username-input" type="text" maxlength="20" placeholder="Enter username (e.g., Hopeful123)"
            oninput="onUsernameInput(this)"
            style="width:100%;padding:18px 16px;font-size:16px;border:2px solid #2196F3;border-radius:14px;font-family:'Inter',sans-serif;background:white;color:#1a1a2e;outline:none;">
        </div>
        <div style="text-align:right;font-size:13px;color:#9aa3b2;margin-bottom:22px;" id="username-count">0/20</div>
        <div style="background:white;border-radius:14px;padding:18px 20px;margin-bottom:32px;">
          <div style="font-size:14px;font-weight:800;color:#1a1a2e;margin-bottom:10px;">Tips:</div>
          <div style="font-size:14px;color:#555e75;line-height:1.8;">• Use a meaningful but anonymous name<br>• Avoid personal information<br>• Choose something that inspires you</div>
        </div>
      </div>
      <button id="username-continue-btn" disabled onclick="showWhyStop()"
        style="width:100%;padding:16px;background:#e2e8f0;color:#9aa3b2;font-size:16px;font-weight:700;border:none;border-radius:14px;cursor:not-allowed;font-family:'Inter',sans-serif;transition:all 0.2s;">
        Continue
      </button>
    </div>
  </div>
</div>

<!-- WHY STOP SCREEN -->
<div id="whystop-screen" class="p1-wrap hidden" style="background:#f0f4fa;">
  <div class="screen-p1 active" style="overflow-y:auto;">
    <div class="progress-bar-track"><div class="progress-bar-fill" style="width:19.3%"></div></div>
    <div class="page-count">6 of 31</div>
    <div style="padding:24px 18px 0;">
      <div style="font-size:23px;font-weight:800;color:#1a1a2e;text-align:center;margin-bottom:10px;line-height:1.3;">Why Do You Want to Stop?</div>
      <div style="font-size:14px;font-weight:700;color:#1a1a2e;text-align:center;line-height:1.5;margin-bottom:22px;">Select all that apply. Your motivations will guide your recovery.</div>
      <div id="ws-options" style="display:flex;flex-direction:column;gap:10px;margin-bottom:18px;"></div>
      <div style="font-size:14px;font-weight:700;color:#1a1a2e;margin-bottom:8px;">Other reason (optional):</div>
      <textarea id="ws-other" maxlength="100" placeholder="Enter your personal reason..."
        oninput="document.getElementById('ws-other-count').textContent=this.value.length+'/100';"
        style="width:100%;padding:14px 16px;font-size:14px;border:1px solid #dde6f0;border-radius:12px;font-family:'Inter',sans-serif;background:white;color:#1a1a2e;outline:none;resize:none;height:80px;"></textarea>
      <div style="text-align:right;font-size:13px;color:#9aa3b2;margin-bottom:16px;" id="ws-other-count">0/100</div>
      <div style="background:#e8f0fb;border-radius:12px;border-left:4px solid #2196F3;padding:16px 16px;margin-bottom:20px;text-align:center;">
        <div style="font-size:13px;font-style:italic;color:#1a2d5a;line-height:1.6;">"And whoever strives only strives for [the benefit of] himself"</div>
        <div style="font-size:12px;font-weight:700;color:#4a6fa5;margin-top:6px;">Surah Al-Ankabut 29:6</div>
      </div>
      <button class="btn-continue" onclick="startPhase2()">Next →</button>
      <div style="height:24px;"></div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- PHASE 2: Screens 7–17 from 16.html                          -->
<!-- ============================================================ -->
<div class="p2-wrap" id="phase2">
  <div class="prog-wrap"><div class="prog-fill" id="pFill"></div></div>
  <div class="step-ctr" id="pCtr"></div>

  <!-- SCREEN 7 -->
  <div class="screen" id="screen7">
    <div class="s-title">Do any of these feel familiar?</div>
    <div class="s-sub">These are common effects of porn use. Check all that apply.</div>
    <div class="opt-list">
      <div class="opt" data-key="anxiety" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Anxiety</span></div>
      <div class="opt" data-key="concentration" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Poor concentration</span></div>
      <div class="opt" data-key="motivation" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Poor motivation</span></div>
      <div class="opt" data-key="guilt" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Guilt and shame</span></div>
      <div class="opt" data-key="sexual_dysfunction" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Sexual dysfunction</span></div>
      <div class="opt" data-key="family_argue" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Arguing with family</span></div>
      <div class="opt" data-key="isolation" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Social isolation</span></div>
      <div class="opt" data-key="depression" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Depression</span></div>
      <div class="opt" data-key="sleep" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Sleep problems</span></div>
      <div class="opt" data-key="self_esteem" data-g="s7" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Low self-esteem</span></div>
      <div class="qbox"><div class="qtext">"And whoever relies upon Allah — then He is sufficient for him"</div><div class="qref">Surah At-Talaq 65:3</div></div>
    </div>
    <button class="btn" onclick="go(8)">Next</button>
  </div>

  <!-- SCREEN 8 -->
  <div class="screen" id="screen8">
    <div class="s-title">Do any of these resonate spiritually?</div>
    <div class="s-sub">Porn can distance you from Allah. Check all that apply.</div>
    <div class="opt-list">
      <div class="opt" data-key="prayers" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Missing prayers</span></div>
      <div class="opt" data-key="darkness" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Darkness in soul</span></div>
      <div class="opt" data-key="imaan" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Low imaan (faith)</span></div>
      <div class="opt" data-key="family_issues" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Family issues</span></div>
      <div class="opt" data-key="islamic_knowledge" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Lack of Islamic knowledge</span></div>
      <div class="opt" data-key="rizq" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Lack of rizq (provision)</span></div>
      <div class="opt" data-key="fears" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Fears and anxieties</span></div>
      <div class="opt" data-key="distance_allah" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Distance from Allah</span></div>
      <div class="opt" data-key="dua" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Difficulty making dua</span></div>
      <div class="opt" data-key="spiritual_motivation" data-g="s8" onclick="tog(this)"><div class="radio"></div><span class="opt-lbl">Loss of spiritual motivation</span></div>
      <div class="qbox"><div class="qtext">"Surely in the remembrance of Allah do hearts find comfort"</div><div class="qref">(Surah Ar-Ra'd 13:28)</div></div>
    </div>
    <button class="btn" onclick="go(9)">Next</button>
  </div>

  <!-- SCREEN 9 -->
  <div class="screen" id="screen9">
    <div class="s-title">The Hidden Cost of Addiction</div>
    <div class="s-sub">The cycle of shame and guilt can feel endless, but Allah's mercy is greater.</div>
    <div class="cost-items">
      <div class="cost-item"><div class="cicon" style="background:#fdecea">🧠</div><span style="font-size:15px;font-weight:700;color:var(--text)">Fuels anxiety and restlessness</span></div>
      <div class="cost-item"><div class="cicon" style="background:#e3f4f9">⚠️</div><span style="font-size:15px;font-weight:700;color:var(--text)">Isolates you from family</span></div>
      <div class="cost-item"><div class="cicon" style="background:#fdecea">❤️</div><span style="font-size:15px;font-weight:700;color:var(--text)">Weakens your iman and connection</span></div>
      <div class="cost-item"><div class="cicon" style="background:#e3f4f9">🛡️</div><span style="font-size:15px;font-weight:700;color:var(--text)">Makes tawbah feel distant</span></div>
    </div>
    <div class="qbox"><div class="qtext">"The heart that turns to Allah finds peace"</div><div class="qref">(Surah Ar-Ra'd 13:28)</div></div>
    <button class="btn" onclick="go(10)">Continue</button>
  </div>

  <!-- SCREEN 10 -->
  <div class="screen" id="screen10">
    <div style="font-size:11px;font-weight:800;color:var(--red);letter-spacing:1.5px;text-align:center;margin-bottom:6px;">THE COST</div>
    <div class="s-title">It Steals From Everything</div>
    <div class="s-sub">Porn trains your brain to feel almost nothing from real life. Everyday pleasures lose their power.</div>
    <div class="bars-wrap" id="barsWrap"></div>
    <div style="font-size:11px;color:#999;text-align:right;margin-top:-8px;">vs. healthy baseline</div>
    <div class="qbox" style="margin-top:14px;"><div class="qtext">"Surely in the remembrance of Allah do hearts find rest."</div><div class="qref">Surah Ar-Ra'd 13:28</div></div>
    <button class="btn" onclick="go(11)">Continue</button>
  </div>

  <!-- SCREEN 11 -->
  <div class="screen" id="screen11">
    <div style="text-align:center;margin-bottom:6px;"><span style="background:#fdecea;color:var(--red);font-size:11px;font-weight:800;letter-spacing:1.5px;padding:5px 14px;border-radius:99px;">THE COST</span></div>
    <div class="s-title">It Pushes People Away</div>
    <div class="s-sub" id="swSub">Swipe through each card.</div>
    <div class="card-stack" id="cardStack">
      <div class="scard active-scard" id="sc1" style="z-index:3;">
        <div class="ch"><div class="cicon2">❤️</div><span class="ctag">BOND</span><span class="cnum">1 / 3</span></div>
        <div class="ctitle">Your Spouse or Partner</div>
        <div class="cbody">You're present physically but absent emotionally. The distance grows silently over months. Trust, once eroded this way, takes years to rebuild — if it's rebuilt at all.</div>
      </div>
      <div class="scard" id="sc2" style="z-index:2;transform:scale(0.96) translateY(10px);">
        <div class="ch"><div class="cicon2">🏠</div><span class="ctag">FAMILY</span><span class="cnum">2 / 3</span></div>
        <div class="ctitle">Your Family</div>
        <div class="cbody">You show up in body but not in spirit. Your children sense your distraction. Your parents feel a distance they can't name. The shame creates a wall between you and those who love you most.</div>
      </div>
      <div class="scard" id="sc3" style="z-index:1;transform:scale(0.92) translateY(20px);">
        <div class="ch"><div class="cicon2">👤</div><span class="ctag">SELF</span><span class="cnum">3 / 3</span></div>
        <div class="ctitle">Your Own Heart</div>
        <div class="cbody">Shame makes real connection feel impossible. You stop letting people in — and slowly forget what genuine closeness actually feels like. The loneliness deepens in silence.</div>
      </div>
    </div>
    <div style="text-align:center;color:#bbb;font-size:13px;font-weight:600;margin-top:14px;" id="swHint">← swipe either way →</div>
    <div class="dots" id="swDots"><div class="dot on" id="d1"></div><div class="dot" id="d2"></div><div class="dot" id="d3"></div></div>
    <div id="swSummary" style="display:none;margin-top:16px;">
      <div style="background:#fdecea;border-left:4px solid var(--red);border-radius:10px;padding:14px 16px;margin-bottom:14px;">
        <div style="font-style:italic;font-size:14px;color:#7a1a1a;font-weight:600;">This is what's already at stake.</div>
      </div>
      <div class="qbox"><div class="qtext">"And hold firmly to the rope of Allah all together and do not be divided."</div><div class="qref">Surah Aal-e-Imran 3:103</div></div>
      <button class="btn" onclick="go(12)">Continue</button>
    </div>
  </div>

  <!-- SCREEN 12 -->
  <div class="screen" id="screen12">
    <div style="text-align:center;margin-bottom:4px;"><span style="color:var(--red);font-size:11px;font-weight:800;letter-spacing:1.5px;">THE COST</span></div>
    <div class="s-title">The Daily Toll</div>
    <div class="s-sub">These aren't just feelings. They're documented effects experienced by men like you.</div>
    <div style="background:#fff;border-radius:18px;box-shadow:0 2px 12px rgba(0,0,0,.07);overflow:hidden;">
      <div class="toll-row"><div class="toll-pct" id="t1">0%</div><div class="toll-div"></div><div><div class="toll-t">Guilt &amp; Shame</div><div class="toll-s">Spiraling shame and self-judgement</div></div></div>
      <div class="toll-row" style="border-top:1px solid #f0f0f0"><div class="toll-pct" id="t2">0%</div><div class="toll-div"></div><div><div class="toll-t">Anxiety</div><div class="toll-s">Constant inner tension and worry</div></div></div>
      <div class="toll-row" style="border-top:1px solid #f0f0f0"><div class="toll-pct" id="t3">0%</div><div class="toll-div"></div><div><div class="toll-t">Dissatisfaction</div><div class="toll-s">Nothing ever feels like enough</div></div></div>
      <div class="toll-row" style="border-top:1px solid #f0f0f0"><div class="toll-pct" id="t4">0%</div><div class="toll-div"></div><div><div class="toll-t">Mood Swings</div><div class="toll-s">Emotional instability and irritability</div></div></div>
    </div>
    <div style="font-size:11px;color:#aaa;text-align:center;margin:8px 0 4px;font-style:italic;">% of men reporting this in recovery programs</div>
    <div class="qbox"><div class="qtext">"And whoever turns away from My remembrance — indeed, he will have a depressed life."</div><div class="qref">Surah Ta-Ha 20:124</div></div>
    <button class="btn" onclick="go(13)">Continue</button>
  </div>

  <!-- SCREEN 13 -->
  <div class="screen" id="screen13">
    <div style="text-align:center;margin-bottom:8px;color:var(--red);font-size:11px;font-weight:800;letter-spacing:1.5px;">SPIRITUAL COST</div>
    <div class="s-title">Loss of Inner Light</div>
    <div class="s-sub" style="font-weight:700;">Sin extinguishes the light of knowledge in your heart. When we disobey Allah, our spiritual senses become clouded.</div>
    <div style="display:flex;flex-direction:column;gap:14px;margin-bottom:20px;">
      <div class="light-item" style="animation-delay:.05s"><div class="rdot"></div><span>The light of knowledge becomes extinguished</span></div>
      <div class="light-item" style="animation-delay:.15s"><div class="rdot"></div><span>Your heart becomes hardened to guidance</span></div>
      <div class="light-item" style="animation-delay:.25s"><div class="rdot"></div><span>Du'a feels heavy and disconnected</span></div>
      <div class="light-item" style="animation-delay:.35s"><div class="rdot"></div><span>Quran recitation loses its sweetness</span></div>
      <div class="light-item" style="animation-delay:.45s"><div class="rdot"></div><span>Night prayers become difficult to maintain</span></div>
      <div class="light-item" style="animation-delay:.55s"><div class="rdot"></div><span>A veil forms between you and your Rabb</span></div>
    </div>
    <div class="qbox"><div class="qtext">"I think that Allah has caused light to enter your heart, so do not extinguish it with the darkness of sin."</div><div class="qref">— Imam Malik to Ash-Shafi'i</div></div>
    <button class="btn" onclick="go(14)">Continue</button>
  </div>

  <!-- SCREEN 14 -->
  <div class="screen" id="screen14">
    <div style="text-align:center;margin-bottom:10px;"><span style="background:#fdecea;color:var(--red);font-size:11px;font-weight:800;letter-spacing:1.5px;padding:5px 14px;border-radius:99px;">SPIRITUAL COST</span></div>
    <div class="s-title">Deprived of Provision</div>
    <div class="s-sub">The Prophet ﷺ warned that sins cut off the channels through which Allah sends us sustenance and blessings.</div>
    <div style="background:#1e2235;border-radius:18px;padding:22px 20px;margin-bottom:14px;box-shadow:0 4px 20px rgba(0,0,0,.15);">
      <div style="font-size:26px;color:var(--red);margin-bottom:12px;font-weight:900;">"</div>
      <div style="font-family:'Amiri',serif;font-style:italic;font-size:17px;color:#fff;line-height:1.7;margin-bottom:14px;">A man is deprived of provision because of the sins that he commits.</div>
      <div style="display:flex;align-items:center;gap:10px;"><div style="width:28px;height:2px;background:var(--red);border-radius:2px;"></div><div style="font-size:13px;color:#aaa;font-weight:700;">Ibn Majah</div></div>
    </div>
    <div style="background:#fdecea;border-left:4px solid var(--red);border-radius:10px;padding:14px 16px;margin-bottom:18px;">
      <div style="font-style:italic;font-size:14px;color:#7a1a1a;font-weight:600;line-height:1.6;">Every sin quietly closes a door that Allah had opened for you.</div>
    </div>
    <button class="btn" onclick="go(15)">Continue</button>
  </div>

  <!-- SCREEN 15 -->
  <div class="screen" id="screen15">
    <div class="s-title">What You've Lost</div>
    <div class="s-sub" style="font-weight:700;">Sin creates a barrier between us and Allah, and distances us from everything sacred.</div>
    <div style="display:flex;flex-direction:column;gap:10px;flex:1;overflow-y:auto;padding-bottom:4px;">
      <div class="lost-item" style="animation-delay:.05s"><div class="ldot-wrap"><div class="ldot"></div></div>Closeness to Allah</div>
      <div class="lost-item" style="animation-delay:.15s"><div class="ldot-wrap"><div class="ldot"></div></div>Sweetness of worship</div>
      <div class="lost-item" style="animation-delay:.25s"><div class="ldot-wrap"><div class="ldot"></div></div>Peace in solitude</div>
      <div class="lost-item" style="animation-delay:.35s"><div class="ldot-wrap"><div class="ldot"></div></div>Clarity of purpose</div>
      <div class="lost-item" style="animation-delay:.45s"><div class="ldot-wrap"><div class="ldot"></div></div>Connection with righteous people</div>
      <div class="lost-item" style="animation-delay:.55s"><div class="ldot-wrap"><div class="ldot"></div></div>Barakah in your time and provision</div>
      <div class="qbox" style="margin-top:6px;"><div class="qtext">"And whoever turns away from My remembrance — indeed, he will have a depressed life"</div><div class="qref">(Surah Ta-Ha 20:124)</div></div>
    </div>
    <button class="btn" onclick="go(16)">Continue</button>
  </div>

  <!-- SCREEN 16: HOLD -->
  <div class="screen" id="screen16" style="padding:0;">
    <div id="holdZone" style="background:#daeef7;min-height:100vh;display:flex;flex-direction:column;align-items:center;padding:34px 22px 48px;">
      <div style="font-size:14px;font-weight:700;color:#555;margin-bottom:18px;text-align:center;">You've seen the cost...</div>
      <div style="font-size:34px;font-weight:900;color:var(--text);text-align:center;line-height:1.25;margin-bottom:14px;">But everything<br>can be restored.</div>
      <div style="width:44px;height:3px;background:var(--blue);border-radius:3px;margin-bottom:20px;"></div>
      <div style="font-size:17px;font-weight:700;color:var(--blue);text-align:center;line-height:1.6;margin-bottom:26px;">Allah's mercy is greater than any sin.<br>Your journey back begins with a single step.</div>
      <div style="width:100%;background:#eaf5f9;border-left:4px solid var(--blue);border-radius:10px;padding:18px;margin-bottom:34px;">
        <div style="font-family:'Amiri',serif;font-style:italic;font-size:15px;color:#1a4a5a;text-align:center;line-height:1.7;">"Say: O My servants who have transgressed against themselves — do not despair of the mercy of Allah. Indeed, Allah forgives all sins."</div>
        <div id="bismLine" style="overflow:hidden;max-height:0;opacity:0;transition:max-height .4s ease,opacity .4s ease;">
          <div style="margin-top:12px;border-top:1px solid #c5e4ef;padding-top:10px;text-align:center;">
            <div style="font-family:'Amiri',serif;font-size:22px;color:var(--blue);font-weight:900;">بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ</div>
            <div style="font-family:'Amiri',serif;font-style:italic;font-size:13px;color:#1a7a9a;font-weight:700;margin-top:4px;">Bismillah ir-Rahman ir-Rahim</div>
          </div>
        </div>
        <div style="font-size:12px;font-weight:700;color:var(--blue);text-align:center;margin-top:10px;">Surah Az-Zumar 39:53</div>
      </div>
      <div style="flex:1;"></div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:14px;width:100%;">
        <div style="width:64px;height:14px;background:#b8dce8;border-radius:99px;overflow:hidden;position:relative;">
          <div id="holdPill" style="position:absolute;left:0;top:0;height:100%;width:0%;background:var(--blue);border-radius:99px;transition:width .04s linear;"></div>
        </div>
        <div id="hLabel" style="font-size:26px;font-weight:900;color:var(--text);text-align:center;">Hold</div>
        <div id="hSub" style="font-size:13px;color:#888;font-weight:600;text-align:center;">to begin</div>
      </div>
    </div>
  </div>

  <!-- SCREEN 17: SEE YOUR FUTURE -->
  <div class="screen" id="screen17">
    <div class="s-title">See Your Future</div>
    <div class="s-sub">This is the difference one decision makes.</div>
    <div style="display:flex;gap:5px;margin-bottom:18px;">
      <button class="future-tab on" id="tab-mental" onclick="switchFutureTab('mental')">Mental Health</button>
      <button class="future-tab" id="tab-spiritual" onclick="switchFutureTab('spiritual')">Spiritual State</button>
      <button class="future-tab" id="tab-relations" onclick="switchFutureTab('relations')">Relationships</button>
    </div>
    <div style="background:#fff;border-radius:16px;padding:14px 8px 8px;box-shadow:0 2px 10px rgba(0,0,0,.06);margin-bottom:6px;">
      <canvas id="fChart" height="200" style="width:100%;display:block;"></canvas>
    </div>
    <div style="display:flex;gap:18px;padding:8px 4px 14px;align-items:center;">
      <div style="display:flex;align-items:center;gap:6px;"><div style="width:12px;height:12px;border-radius:50%;background:var(--blue);"></div><span style="font-size:13px;font-weight:700;color:#333;">With Purify</span></div>
      <div style="display:flex;align-items:center;gap:6px;"><div style="width:12px;height:12px;border-radius:50%;background:var(--red);"></div><span style="font-size:13px;font-weight:700;color:#333;">Without recovery</span></div>
    </div>
    <div class="qbox" style="margin-bottom:18px;">
      <div class="qtext" id="fQuote">"Verily, with hardship comes ease."</div>
      <div class="qref" id="fRef">(Surah Ash-Sharh 94:6)</div>
    </div>
    <button class="btn" onclick="goToPhase3('s19')">Continue</button>
  </div>

</div><!-- end .p2-wrap -->

<!-- ============================================================ -->
<!-- PHASE 3: 22.html screens (19 onwards)                        -->
<!-- ============================================================ -->
<div id="phase3-wrap" style="display:none;">
<style>
/* ===== PHASE 3 styles from 22.html ===== */
.phone { width: 380px; min-height: 700px; background: #fff; position: relative; overflow: hidden; margin: 1rem auto; border-radius: 28px; border: 0.5px solid #d0d8e4; }
.screen22 { display: none; flex-direction: column; min-height: 700px; }
.screen22.active { display: flex; }
.progress-bar-container { padding: 16px 16px 4px; }
.step-label { font-size: 12px; color: #aaa; text-align: right; margin-top: 4px; }
.screen-body { padding: 12px 20px 24px; flex: 1; display: flex; flex-direction: column; }
.screen-title { font-size: 22px; font-weight: 700; color: #1a1a2e; text-align: center; margin-bottom: 6px; }
.screen-sub { font-size: 14px; color: #555; text-align: center; margin-bottom: 18px; }
.tabs22 { display: flex; gap: 0; background: #f2f6f9; border-radius: 30px; padding: 3px; margin-bottom: 18px; }
.tab22 { flex: 1; text-align: center; padding: 7px 4px; border-radius: 28px; font-size: 12px; font-weight: 500; color: #555; cursor: pointer; transition: all 0.2s; }
.tab22.active { background: #1ab3c8; color: #fff; }
.chart-wrapper { position: relative; height: 220px; margin-bottom: 10px; }
.chart-legend { display: flex; gap: 20px; justify-content: center; margin-bottom: 14px; font-size: 13px; }
.legend-dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; margin-right: 5px; vertical-align: middle; }
.quran-box { background: #eef7fc; border-left: 4px solid #1ab3c8; border-radius: 10px; padding: 14px 16px; margin-bottom: 18px; font-style: italic; font-size: 14px; color: #333; line-height: 1.6; text-align: center; }
.quran-box span { display: block; font-size: 12px; color: #888; font-style: normal; margin-top: 4px; }
.reward-list { display: flex; flex-direction: column; gap: 10px; margin-bottom: 18px; }
.reward-item { display: flex; align-items: center; gap: 14px; background: #f7fbfd; border: 1px solid #d5edf5; border-left: 3px solid #1ab3c8; border-radius: 10px; padding: 12px 14px; font-size: 14px; color: #222; }
.reward-icon { width: 38px; height: 38px; background: #daf3f8; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.reward-icon svg { width: 20px; height: 20px; stroke: #1ab3c8; fill: none; stroke-width: 2; }
.transform-section { margin-top: 10px; }
.transform-title { font-size: 16px; font-weight: 700; color: #1a1a2e; text-align: center; margin-bottom: 14px; }
.bar-row22 { margin-bottom: 14px; }
.bar-label22 { display: flex; justify-content: space-between; font-size: 14px; font-weight: 600; color: #333; margin-bottom: 6px; }
.bar-label22 span.pct-red { color: #e05a5a; }
.bar-label22 span.pct-teal { color: #1ab3c8; }
.bar-track22 { height: 12px; background: #eee; border-radius: 8px; overflow: hidden; }
.bar-fill22 { height: 12px; border-radius: 8px; width: 0; transition: width 1.4s cubic-bezier(.22,.68,0,1.2); }
.bar-red22 { background: #e05a5a; }
.bar-teal22 { background: #1ab3c8; }
.feature-list { display: flex; flex-direction: column; gap: 0; }
.feature-item { display: flex; align-items: flex-start; gap: 14px; padding: 14px 0; border-bottom: 1px solid #f0f0f0; cursor: pointer; }
.feature-item:last-child { border-bottom: none; }
.feat-icon { width: 42px; height: 42px; background: #daf3f8; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.feat-icon svg { width: 22px; height: 22px; stroke: #1ab3c8; fill: none; stroke-width: 1.8; }
.feat-text h4 { font-size: 15px; font-weight: 700; color: #1a1a2e; margin-bottom: 2px; }
.feat-text p { font-size: 13px; color: #777; line-height: 1.5; }
.feat-chevron { margin-left: auto; color: #bbb; font-size: 18px; padding-top: 2px; }
.lesson-list { display: flex; flex-direction: column; gap: 12px; }
.lesson-item { display: flex; align-items: center; gap: 14px; background: #fff; border: 1px solid #e0e0e0; border-radius: 14px; padding: 16px; cursor: pointer; }
.lesson-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.lesson-icon.teal { background: #daf3f8; }
.lesson-icon.green { background: #d8f3e9; }
.lesson-icon.orange { background: #fef3e0; }
.lesson-icon svg { width: 22px; height: 22px; stroke-width: 1.8; fill: none; }
.lesson-icon.teal svg { stroke: #1ab3c8; }
.lesson-icon.green svg { stroke: #22a06b; }
.lesson-icon.orange svg { stroke: #f59e0b; }
.lesson-label { font-size: 15px; font-weight: 600; color: #1a1a2e; flex: 1; }
.lesson-arrow { color: #1ab3c8; font-size: 20px; }
.cta-btn { background: linear-gradient(135deg, #1ab3c8, #0e8fa0); color: #fff; border: none; border-radius: 16px; font-size: 17px; font-weight: 600; padding: 17px; width: 100%; cursor: pointer; margin-top: auto; }
.pur-screen22 { display: none; flex-direction: column; min-height: 700px; background: #0d1b2e; }
.pur-screen22.active { display: flex; }
.pur-dots22 { display: flex; gap: 8px; padding: 18px 20px 8px; align-items: center; }
.pur-dot22 { width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.3); transition: background 0.3s; }
.pur-dot22.active { background: #1ab3c8; }
.pur-back22 { background: none; border: none; color: rgba(255,255,255,0.6); font-size: 22px; cursor: pointer; padding: 0; margin-right: 4px; line-height: 1; }
.pur-dots-row22 { display: flex; align-items: center; }
.pur-body22 { padding: 20px 22px 24px; flex: 1; display: flex; flex-direction: column; overflow-y: auto; }
.pur-tag22 { font-size: 11px; font-weight: 700; letter-spacing: 1.5px; color: #1ab3c8; margin-bottom: 18px; text-transform: uppercase; }
.pur-text22 { font-size: 22px; font-weight: 700; color: #ffffff; line-height: 1.55; flex: 1; }
.pur-textarea22 { width: 100%; flex: 1; background: transparent; border: none; outline: none; color: #ffffff; font-size: 18px; font-weight: 500; line-height: 1.6; resize: none; min-height: 300px; }
.pur-textarea22::placeholder { color: rgba(255,255,255,0.3); }
.pur-continue22:disabled { background: #2a3a4a; color: #556677; cursor: not-allowed; }
.pur-continue22 { background: #1ab3c8; color: #fff; border: none; border-radius: 14px; font-size: 17px; font-weight: 600; padding: 17px; width: 100%; cursor: pointer; margin-top: 16px; flex-shrink: 0; }
.bf-screen22 { display: none; flex-direction: column; min-height: 700px; background: #0d1b2e; }
.bf-screen22.active { display: flex; }
.dr-screen22 { display: none; flex-direction: column; min-height: 700px; background: #0d1b2e; }
.dr-screen22.active { display: flex; }
@keyframes fadeInUp22 { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
.screen22.active .screen-body > * { animation: fadeInUp22 0.35s ease both; }
</style>

<div class="phone" id="phase3Phone">

<!-- SCREEN 19 -->
<div class="screen22" id="s19">
  <div class="progress-bar-container">
    <div class="progress-bar-track"><div class="progress-bar-fill" style="width:61%"></div></div>
    <div class="step-label">19 of 31</div>
  </div>
  <div class="screen-body">
    <div class="screen-title">Rewards of Quitting</div>
    <div class="reward-list">
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>Preserving wealth and easy provision</div>
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div>Means for worldly and religious benefits</div>
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/></svg></div>Wholesome and blessed life</div>
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></div>Heart happiness and joy</div>
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>Security from worries and grief</div>
    </div>
    <div class="quran-box">"And whoever fears Allah - He will make for him ease in his matter"<span>(Surah At-Talaq 65:4)</span></div>
    <button class="cta-btn" onclick="goTo22('s20')">Next</button>
  </div>
</div>

<!-- SCREEN 20 -->
<div class="screen22" id="s20">
  <div class="progress-bar-container">
    <div class="progress-bar-track"><div class="progress-bar-fill" style="width:64%"></div></div>
    <div class="step-label">20 of 31</div>
  </div>
  <div class="screen-body">
    <div class="screen-title">More Rewards</div>
    <div class="reward-list">
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div>Less worry and grief in your heart</div>
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>Closeness of angels, distance from devils</div>
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><path d="M12 2l2.4 7.4H22l-6.2 4.5 2.4 7.4L12 17l-6.2 4.3 2.4-7.4L2 9.4h7.6z"/></svg></div>Angels' joy and supplications for you</div>
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2z"/></svg></div>Increased intellect and faith</div>
      <div class="reward-item"><div class="reward-icon"><svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div>Allah's love and special attention</div>
    </div>
    <div class="transform-section">
      <div class="transform-title">Your Transformation</div>
      <div class="bar-row22">
        <div class="bar-label22">Before Recovery <span class="pct-red" id="pct1">0%</span></div>
        <div class="bar-track22"><div class="bar-fill22 bar-red22" id="bar1"></div></div>
      </div>
      <div class="bar-row22">
        <div class="bar-label22">After Recovery <span class="pct-teal" id="pct2">0%</span></div>
        <div class="bar-track22"><div class="bar-fill22 bar-teal22" id="bar2"></div></div>
      </div>
    </div>
    <button class="cta-btn" onclick="goTo22('s21')" style="margin-top:14px">Next</button>
  </div>
</div>

<!-- SCREEN 21 -->
<div class="screen22" id="s21">
  <div class="progress-bar-container">
    <div class="progress-bar-track"><div class="progress-bar-fill" style="width:67%"></div></div>
    <div class="step-label">21 of 31</div>
  </div>
  <div class="screen-body">
    <div class="screen-title">How Purify Helps</div>
    <div class="screen-sub">Tap each feature to learn more about how we support your recovery.</div>
    <div class="feature-list">
      <div class="feature-item"><div class="feat-icon"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div><div class="feat-text"><h4>Daily Recovery Program</h4><p>Structured daily tasks and Islamic reminders</p></div><div class="feat-chevron">›</div></div>
      <div class="feature-item"><div class="feat-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/></svg></div><div class="feat-text"><h4>Gamified Progress</h4><p>Earn XP, advance your journey, and earn your rank in the community</p></div><div class="feat-chevron">›</div></div>
      <div class="feature-item"><div class="feat-icon"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div><div class="feat-text"><h4>Community Support</h4><p>Connect with others on the same journey</p></div><div class="feat-chevron">›</div></div>
      <div class="feature-item"><div class="feat-icon"><svg viewBox="0 0 24 24"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></div><div class="feat-text"><h4>Track Progress</h4><p>Monitor your streak and celebrate milestones</p></div><div class="feat-chevron">›</div></div>
    </div>
    <button class="cta-btn" onclick="goTo22('s22')">Next</button>
  </div>
</div>

<!-- SCREEN 22 -->
<div class="screen22" id="s22">
  <div class="progress-bar-container">
    <div class="progress-bar-track"><div class="progress-bar-fill" style="width:71%"></div></div>
    <div class="step-label">22 of 31</div>
  </div>
  <div class="screen-body">
    <div class="screen-title">Experience Your First Lesson</div>
    <div class="screen-sub" id="modules-sub">0 of 3 modules done — keep going</div>
    <div class="lesson-list">
      <div class="lesson-item" id="ibn-item" onclick="openPur()"><div class="lesson-icon teal" id="ibn-icon"><svg viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div><span class="lesson-label" id="ibn-label">Ibn Qayyim Purification</span><span class="lesson-arrow" id="ibn-arrow">›</span></div>
      <div class="lesson-item" id="bf-item" onclick="openBF()"><div class="lesson-icon green"><svg viewBox="0 0 24 24"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2z"/></svg></div><span class="lesson-label">Breaking Free (Neuroscience)</span><span class="lesson-arrow">›</span></div>
      <div class="lesson-item" id="dr-item" onclick="openDR()"><div class="lesson-icon orange"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/></svg></div><span class="lesson-label">Daily Reminder</span><span class="lesson-arrow">›</span></div>
    </div>
    <button class="cta-btn" id="s22ContinueBtn" onclick="goToPhase4('p4s22')" style="display:none;margin-top:18px;">Continue</button>
  </div>
</div>

<!-- PURIFICATION LESSON SCREENS -->
<div class="pur-screen22" id="pur1">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="closePur()">‹</button>
    <div class="pur-dots22">
      <div class="pur-dot22 active"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div>
    </div>
  </div>
  <div class="pur-body22">
    <div class="pur-tag22">Key Quote</div>
    <div class="pur-text22">It is not an overstatement to declare that we are living in a dopaminergic society. This means that society is structured in a way that aims to maximize the release of dopamine, the neurotransmitter associated with pleasure in our brains.</div>
    <button class="pur-continue22" onclick="goToPur22('pur2')">Continue</button>
  </div>
</div>

<div class="pur-screen22" id="pur2">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="goToPur22('pur1')">‹</button>
    <div class="pur-dots22">
      <div class="pur-dot22"></div><div class="pur-dot22 active"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div>
    </div>
  </div>
  <div class="pur-body22">
    <div class="pur-tag22">Teaching Points</div>
    <div class="pur-text22">Everywhere you turn—your phone, your fridge, even the advertisements on the street—things are designed to catch your attention and give you a quick shot of pleasure. Social media scrolls, colorful foods, binge-worthy shows... these are engineered to spike dopamine in your brain. It feels good in the moment, but the high fades quickly, leaving you wanting more.</div>
    <button class="pur-continue22" onclick="goToPur22('pur3')">Continue</button>
  </div>
</div>

<div class="pur-screen22" id="pur3">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="goToPur22('pur2')">‹</button>
    <div class="pur-dots22">
      <div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22 active"></div><div class="pur-dot22"></div><div class="pur-dot22"></div>
    </div>
  </div>
  <div class="pur-body22">
    <div class="pur-text22" style="font-size:18px;">Over time, this cycle doesn't just affect your habits—it can hold your heart captive. True well-being isn't about chasing the next burst of dopamine—it's about finding balance and freedom from being controlled by every urge.<br><br>Take 5 quiet minutes today. Think of one everyday activity that gives you that 'instant hit' of pleasure.<br><br>Ask yourself:<br>• How quickly does the urge to repeat it come back?<br>• How does it make you feel right after, and an hour later?<br>• Does it feel like freedom… or a loop you can't step out of?</div>
    <button class="pur-continue22" onclick="goToPur22('pur4')">Continue</button>
  </div>
</div>

<div class="pur-screen22" id="pur4">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;justify-content:space-between;">
    <div style="display:flex;align-items:center;">
      <button class="pur-back22" onclick="goToPur22('pur3')">‹</button>
      <div class="pur-dots22"><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22 active"></div><div class="pur-dot22"></div></div>
    </div>
    <div style="font-size:11px;font-weight:700;letter-spacing:1.5px;color:#1ab3c8;padding-right:4px;">YOUR REFLECTION</div>
  </div>
  <div class="pur-body22" style="display:flex;flex-direction:column;">
    <textarea class="pur-textarea22" id="reflectionText" placeholder="Begin writing..." oninput="checkPurText22()"></textarea>
    <button class="pur-continue22" id="purContBtn" onclick="goToPur22('pur5')" disabled>Continue</button>
  </div>
</div>

<div class="pur-screen22" id="pur5">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="goToPur22('pur4')">‹</button>
    <div class="pur-dots22"><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22 active"></div></div>
  </div>
  <div class="pur-body22">
    <div class="pur-tag22">Closing Reflection</div>
    <div class="pur-text22">You've just taken your first important step: noticing the patterns around you. Our society is designed to keep us hooked on quick pleasure, but awareness is a form of resistance. By seeing the trap, you give yourself the choice to rise above it.</div>
    <button class="pur-continue22" onclick="closePur22()">Continue</button>
  </div>
</div>

<!-- BREAKING FREE SCREENS -->
<div class="bf-screen22" id="bf1">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="closeBF22()">‹</button>
    <div class="pur-dots22"><div class="pur-dot22 active"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div></div>
  </div>
  <div class="pur-body22">
    <div class="pur-tag22">Concept</div>
    <div class="pur-text22">The brain is a powerful organ. It's not a moral compass, but a complex learning machine. When it comes to habits, your brain isn't broken—it's simply learned a pattern. And what it's learned, it can unlearn.</div>
    <button class="pur-continue22" onclick="goToBF22('bf2')">Continue</button>
  </div>
</div>

<div class="bf-screen22" id="bf2">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="goToBF22('bf1')">‹</button>
    <div class="pur-dots22"><div class="pur-dot22"></div><div class="pur-dot22 active"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div></div>
  </div>
  <div class="pur-body22">
    <div class="pur-tag22">Teaching Points</div>
    <div class="pur-text22" style="font-size:18px;">The Reward Pathway: Pornography can hijack the brain's reward system. The immediate novelty and intensity of the content cause a massive release of dopamine, much larger than what would be released in a real-world experience.</div>
    <button class="pur-continue22" onclick="goToBF22('bf3')">Continue</button>
  </div>
</div>

<div class="bf-screen22" id="bf3">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="goToBF22('bf2')">‹</button>
    <div class="pur-dots22"><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22 active"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div></div>
  </div>
  <div class="pur-body22">
    <div class="pur-text22" style="font-size:18px;">The Cycle of Desensitization: When the brain is repeatedly exposed to high dopamine spikes, it adjusts and requires more stimulation for the same effect. This isn't a sign of moral failing—it's a predictable neurobiological response. The good news: just as your brain adapted to this pattern, it can adapt to new, healthier patterns too.</div>
    <button class="pur-continue22" onclick="goToBF22('bf4')">Continue</button>
  </div>
</div>

<div class="bf-screen22" id="bf4">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="goToBF22('bf3')">‹</button>
    <div class="pur-dots22"><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22 active"></div><div class="pur-dot22"></div><div class="pur-dot22"></div></div>
  </div>
  <div class="pur-body22">
    <div class="pur-tag22">Practical Exercise</div>
    <div class="pur-text22" style="font-size:18px;">Think of yourself as a detective. Start a trigger list — a trigger is anything that consistently comes before compulsive behavior: a feeling (boredom, loneliness, stress), a time of day, or an external cue.<br><br>In the text box below, start your list. There are no right or wrong answers.</div>
    <button class="pur-continue22" onclick="goToBF22('bf5')">Continue</button>
  </div>
</div>

<div class="bf-screen22" id="bf5">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;justify-content:space-between;">
    <div style="display:flex;align-items:center;">
      <button class="pur-back22" onclick="goToBF22('bf4')">‹</button>
      <div class="pur-dots22"><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22 active"></div><div class="pur-dot22"></div></div>
    </div>
    <div style="font-size:11px;font-weight:700;letter-spacing:1.5px;color:#1ab3c8;padding-right:4px;">YOUR REFLECTION</div>
  </div>
  <div class="pur-body22" style="display:flex;flex-direction:column;">
    <textarea class="pur-textarea22" id="bfReflectionText" placeholder="Begin writing..." oninput="checkBFText22()"></textarea>
    <button class="pur-continue22" id="bfContBtn" onclick="goToBF22('bf6')" disabled>Continue</button>
  </div>
</div>

<div class="bf-screen22" id="bf6">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="goToBF22('bf5')">‹</button>
    <div class="pur-dots22"><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22"></div><div class="pur-dot22 active"></div></div>
  </div>
  <div class="pur-body22">
    <div class="pur-tag22">Insight</div>
    <div class="pur-text22">You've just taken the first, most powerful step on your journey. By identifying these patterns, you've moved from autopilot to intentional observation. You're beginning to take back control — not by fighting your brain, but by understanding it.<br><br>Identifying your triggers is the foundation of recovery.</div>
    <button class="pur-continue22" onclick="closeBF22()">Continue</button>
  </div>
</div>

<!-- DAILY REMINDER SCREEN -->
<div class="dr-screen22" id="dr1">
  <div class="pur-dots-row22" style="padding:18px 20px 8px;display:flex;align-items:center;">
    <button class="pur-back22" onclick="closeDR22()">‹</button>
    <div class="pur-dots22"><div class="pur-dot22 active"></div></div>
  </div>
  <div class="pur-body22">
    <div class="pur-tag22">Use Your Brain To Fight Urges</div>
    <div class="pur-text22">When unwanted sexual thoughts come, try puzzles or brain games to keep your mind busy. Have tools ready - keep a book of brain-teasers, puzzle apps, or fun websites nearby so you can dive in when needed. Engaging in something like a Tetris level or crossword keeps your brain busy and leaves no room for intrusive thoughts.</div>
    <button class="pur-continue22" onclick="closeDR22()">Continue</button>
  </div>
</div>

</div><!-- end #phase3Phone -->
</div><!-- end #phase3-wrap -->





<!-- ============================================================ -->
<!-- PHASE 4: 31_TAK.html screens (S22–S31 + done)              -->
<!-- ============================================================ -->
<div id="phase4-wrap" style="display:none;">
<style>
.p4app{max-width:390px;margin:0 auto;background:#fff;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;border-radius:28px;border:0.5px solid #d0d8e4;overflow:hidden;}
.p4prog-wrap{padding:12px 16px 2px}
.p4prog-track{background:#E5E7EB;border-radius:999px;height:6px;position:relative}
.p4prog-fill{background:#0EA5C9;border-radius:999px;height:6px;transition:width .4s}
.p4prog-dot{position:absolute;right:-7px;top:-5px;width:16px;height:16px;border-radius:50%;background:#0EA5C9;border:2.5px solid white}
.p4prog-lbl{text-align:right;font-size:12px;color:#6B7280;margin-top:5px}
.p4screen{padding:18px 18px 28px;display:none;flex-direction:column;gap:15px}
.p4screen.active{display:flex}
.p4app h1{font-size:23px;font-weight:800;color:#111827;line-height:1.3}
.p4sub{color:#6B7280;font-size:14px;line-height:1.6}
.p4btn{width:100%;padding:15px;border-radius:14px;border:none;background:linear-gradient(90deg,#0EA5C9,#06B6D4);color:white;font-size:16px;font-weight:700;cursor:pointer}
.p4btn:active{opacity:.85}
.p4card{background:white;border:1px solid #E5E7EB;border-radius:14px;padding:15px;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.p4qbox{background:#F0FBFF;border-left:4px solid #0EA5C9;border-radius:0 10px 10px 0;padding:14px 16px;font-style:italic;font-size:13.5px;color:#374151;line-height:1.6}
.p4qsrc{margin-top:6px;font-style:normal;font-size:12px;font-weight:600;color:#6B7280}
.p4tog{width:44px;height:26px;border-radius:13px;background:#D1D5DB;position:relative;cursor:pointer;flex-shrink:0;transition:background .2s}
.p4tog.on{background:#0EA5C9}
.p4togdot{width:20px;height:20px;border-radius:50%;background:white;position:absolute;top:3px;left:3px;transition:left .2s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.p4tog.on .p4togdot{left:21px}
.p4chip{padding:8px 16px;border-radius:999px;border:2px solid #D1D5DB;background:white;color:#374151;font-size:13px;font-weight:600;cursor:pointer}
.p4chip.sel{border-color:#0EA5C9;background:#E0F7FA;color:#0EA5C9}
.p4swcard{background:white;border-radius:18px;border:2.5px solid #0EA5C9;padding:22px 20px;box-shadow:4px 4px 0 #E5E7EB;user-select:none;cursor:grab}
.p4jdot{height:10px;border-radius:999px;background:#D1FAE5;cursor:pointer;transition:all .25s}
.p4jdot.on{background:#0EA5C9;width:22px!important}
.p4ibox{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.p4step-c{width:34px;height:34px;border-radius:50%;background:#E0F7FA;color:#0EA5C9;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0;border:1.5px solid #0EA5C9}
.p4step-c.done{background:#0EA5C9;color:white;border-color:#0EA5C9}
.p4cal-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.45);display:flex;align-items:flex-end;justify-content:center;z-index:999}
.p4cal-sheet{background:white;border-radius:20px 20px 0 0;padding:20px;width:100%;max-width:390px}
.p4cal-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
.p4cal-nav{width:36px;height:36px;border-radius:50%;border:1px solid #E5E7EB;background:white;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:16px;color:#374151}
.p4cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;text-align:center}
.p4cal-day-name{font-size:11px;font-weight:600;color:#9CA3AF;padding:4px 0}
.p4cal-day{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;cursor:pointer;margin:0 auto;color:#374151}
.p4cal-day:hover{background:#E0F7FA;color:#0EA5C9}
.p4cal-day.today{border:1.5px solid #0EA5C9;color:#0EA5C9;font-weight:700}
.p4cal-day.selected{background:#0EA5C9;color:white;font-weight:700}
.p4cal-day.other-month{color:#D1D5DB}
.p4cal-day.past{color:#D1D5DB;cursor:default}
.p4cal-day.past:hover{background:transparent;color:#D1D5DB}
</style>

<div class="p4app">
<div class="p4prog-wrap">
  <div class="p4prog-track">
    <div class="p4prog-fill" id="p4pf" style="width:71%"><div class="p4prog-dot"></div></div>
  </div>
  <div class="p4prog-lbl" id="p4plbl">22 of 31</div>
</div>

<!-- P4 S22 -->
<div class="p4screen active" id="p4s22">
  <div style="text-align:center">
    <h1>This is what makes Purify different</h1>
    <p class="p4sub" style="margin-top:10px">Willpower alone has a 97% failure rate. Real, lasting recovery needs three things working together.</p>
  </div>
  <div class="p4card" style="display:flex;gap:13px;align-items:flex-start">
    <div class="p4ibox" style="background:#E0F7FA"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></div>
    <div><div style="font-weight:700;font-size:14px;color:#111827">90-Day Structured Programme</div><div class="p4sub" style="font-size:13px;margin-top:3px">Every day has a plan. You never have to wonder what to do next — just show up.</div></div>
  </div>
  <div class="p4card" style="display:flex;gap:13px;align-items:flex-start">
    <div class="p4ibox" style="background:#E0F7FA"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg></div>
    <div><div style="font-weight:700;font-size:14px;color:#111827">Tazkiya — Spiritual Purification</div><div class="p4sub" style="font-size:13px;margin-top:3px">Rooted in the teachings of Ibn Qayyim and the Quran. Your recovery strengthens your faith.</div></div>
  </div>
  <div class="p4card" style="display:flex;gap:13px;align-items:flex-start">
    <div class="p4ibox" style="background:#E0F7FA"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-1.96-3 2.5 2.5 0 0 1-1.32-4.24 3 3 0 0 1 .34-5.58 2.5 2.5 0 0 1 1.32-4.24A2.5 2.5 0 0 1 9.5 2"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 1.96-3 2.5 2.5 0 0 0 1.32-4.24 3 3 0 0 0-.34-5.58 2.5 2.5 0 0 0-1.32-4.24A2.5 2.5 0 0 0 14.5 2"/></svg></div>
    <div><div style="font-weight:700;font-size:14px;color:#111827">Neuroscience-Based Recovery</div><div class="p4sub" style="font-size:13px;margin-top:3px">Understand how your brain was hijacked — and how to rewire it for lasting freedom.</div></div>
  </div>
  <div style="background:#DCFCE7;border-radius:12px;padding:14px 16px;text-align:center;color:#16A34A;font-weight:700;font-size:14px">Day 1 is already done. You're already on your way.</div>
  <button class="p4btn" onclick="p4go(23)">Let's Continue</button>
</div>

<!-- P4 S23 -->
<div class="p4screen" id="p4s23">
  <div style="text-align:center">
    <h1>Level Up in Life</h1>
    <p class="p4sub" style="margin-top:8px">Gain knowledge, build healthy habits, and quit forever. With sincere tawbah, strengthen your connection to Allah and transform your life.</p>
  </div>
  <div class="p4card">
    <div style="display:flex;justify-content:space-between;align-items:center">
      <span style="color:#0EA5C9;font-weight:700;font-size:15px">Level 1</span>
      <span style="font-size:13px;font-weight:600;color:#374151">150 / 1000 XP</span>
    </div>
    <div style="background:#E5E7EB;border-radius:999px;height:8px;margin-top:7px"><div style="background:#0EA5C9;border-radius:999px;height:8px;width:15%"></div></div>
    <div style="text-align:center;font-size:12px;font-style:italic;color:#6B7280;margin-top:7px">Every clean day earns XP and advances your journey</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:8px">
    <div style="display:flex;align-items:center;gap:12px;padding:13px 14px;background:white;border-radius:11px;border-left:3px solid #0EA5C9;box-shadow:0 1px 3px rgba(0,0,0,.04)"><div class="p4ibox" style="background:#E0F7FA"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-1.96-3 2.5 2.5 0 0 1-1.32-4.24 3 3 0 0 1 .34-5.58 2.5 2.5 0 0 1 1.32-4.24A2.5 2.5 0 0 1 9.5 2"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 1.96-3 2.5 2.5 0 0 0 1.32-4.24 3 3 0 0 0-.34-5.58 2.5 2.5 0 0 0-1.32-4.24A2.5 2.5 0 0 0 14.5 2"/></svg></div><span style="font-weight:600;font-size:14px;color:#111827">Clearer thinking and better focus</span></div>
    <div style="display:flex;align-items:center;gap:12px;padding:13px 14px;background:white;border-radius:11px;border-left:3px solid #0EA5C9;box-shadow:0 1px 3px rgba(0,0,0,.04)"><div class="p4ibox" style="background:#E0F7FA"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div><span style="font-weight:600;font-size:14px;color:#111827">Stronger relationships and trust</span></div>
    <div style="display:flex;align-items:center;gap:12px;padding:13px 14px;background:white;border-radius:11px;border-left:3px solid #0EA5C9;box-shadow:0 1px 3px rgba(0,0,0,.04)"><div class="p4ibox" style="background:#E0F7FA"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 11V6a2 2 0 0 0-2-2 2 2 0 0 0-2 2"/><path d="M14 10V4a2 2 0 0 0-2-2 2 2 0 0 0-2 2v2"/><path d="M10 10.5V6a2 2 0 0 0-2-2 2 2 0 0 0-2 2v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/></svg></div><span style="font-weight:600;font-size:14px;color:#111827">Deeper connection with Allah</span></div>
    <div style="display:flex;align-items:center;gap:12px;padding:13px 14px;background:white;border-radius:11px;border-left:3px solid #0EA5C9;box-shadow:0 1px 3px rgba(0,0,0,.04)"><div class="p4ibox" style="background:#E0F7FA"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/><path d="M5 3v4"/><path d="M19 17v4"/><path d="M3 5h4"/><path d="M17 19h4"/></svg></div><span style="font-weight:600;font-size:14px;color:#111827">Inner peace and self-respect</span></div>
  </div>
  <div class="p4qbox">"And whoever does righteous deeds - whether male or female - while being a believer, those will enter Paradise"<div class="p4qsrc">(Surah An-Nisa 4:124)</div></div>
  <button class="p4btn" onclick="p4go(24)">Next</button>
</div>

<!-- P4 S24 -->
<div class="p4screen" id="p4s24">
  <div style="text-align:center">
    <div style="color:#0EA5C9;font-weight:700;font-size:11px;letter-spacing:2px;text-transform:uppercase">YOUR JOURNEY</div>
    <h1 style="margin-top:6px">360 Days of Transformation</h1>
    <p class="p4sub" style="margin-top:5px">Swipe through to see what's ahead.</p>
  </div>
  <div id="p4jcard-wrap" style="touch-action:pan-y">
    <div class="p4swcard" id="p4jcard">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
        <div style="display:flex;align-items:center;gap:10px">
          <div class="p4ibox" style="background:#E0F7FA"><svg id="p4jc-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg></div>
          <span style="color:#0EA5C9;font-weight:700;font-size:12px;letter-spacing:1px" id="p4jc-range">DAYS 1–90</span>
        </div>
        <span style="color:#9CA3AF;font-size:12px;font-weight:600" id="p4jc-num">1 / 5</span>
      </div>
      <h2 style="margin-bottom:10px" id="p4jc-title">You plant the seed</h2>
      <p class="p4sub" id="p4jc-desc">The first 90 days are the hardest. You'll struggle, stumble, and rebuild. But every clean day is a seed of faith taking root inside you.</p>
    </div>
  </div>
  <div style="text-align:center">
    <div class="p4sub" style="font-size:12px;margin-bottom:8px">← swipe either way →</div>
    <div style="display:flex;gap:7px;justify-content:center;align-items:center" id="p4jdots"></div>
  </div>
  <div id="p4jsummary" style="display:none;background:#F0FBFF;border-radius:14px;padding:18px;text-align:center">
    <div style="font-weight:800;font-size:17px;margin-bottom:14px">This is what awaits you.</div>
    <div style="display:flex;justify-content:space-around;margin-bottom:14px">
      <div><div style="font-size:30px;font-weight:800;color:#0EA5C9">360</div><div class="p4sub" style="font-size:12px">Days</div></div>
      <div><div style="font-size:30px;font-weight:800;color:#0EA5C9">12</div><div class="p4sub" style="font-size:12px">Cycles</div></div>
      <div><div style="font-size:30px;font-weight:800;color:#0EA5C9">∞</div><div class="p4sub" style="font-size:12px">Growth</div></div>
    </div>
    <div class="p4qbox" style="text-align:left">"Verily, with hardship comes ease."<div class="p4qsrc">Surah Ash-Sharh 94:6</div></div>
  <button class="p4btn" onclick="finishFullOnboarding()" style="margin-top:24px; padding:18px; font-size:17px; background:linear-gradient(90deg,#0EA5C9,#06B6D4); box-shadow:0 4px 15px rgba(14,165,201,0.4); cursor:pointer;">Start Day 1 in App &rarr;</button>

  </div>
  <button class="p4btn" onclick="p4go(25)">Let's begin</button>
</div>

<!-- P4 S25 -->
<div class="p4screen" id="p4s25">
  <div style="text-align:center">
    <h1>Your recovery starts the moment you decide</h1>
    <p class="p4sub" style="margin-top:10px;font-weight:500">Choose when you'll begin your journey to freedom.</p>
  </div>
  <div style="text-align:center;padding:8px 0">
    <div style="font-weight:700;font-size:15px;margin-bottom:8px">Your Quit Date:</div>
    <div style="color:#0EA5C9;font-weight:800;font-size:20px;margin-bottom:18px" id="p4quit-lbl">Saturday, May 30, 2026</div>
    <button onclick="p4openCal()" style="background:linear-gradient(90deg,#0EA5C9,#06B6D4);color:white;border:none;border-radius:14px;padding:13px 38px;font-size:15px;font-weight:700;cursor:pointer">Change Date</button>
  </div>
  <div class="p4qbox">"And it is He who created the heavens and earth in truth. And the day He says, 'Be,' and it is, His word is the truth"<div class="p4qsrc">(Surah Al-An'am 6:73)</div></div>
  <button class="p4btn" onclick="p4go(26)">Set Date</button>
</div>

<!-- P4 S26 -->
<div class="p4screen" id="p4s26">
  <div>
    <div style="color:#0EA5C9;font-weight:700;font-size:11px;letter-spacing:2px;text-transform:uppercase">DAYS 1–7</div>
    <h1 style="margin-top:6px">What 7 clean days will do</h1>
    <p class="p4sub" style="margin-top:4px">This is what's coming for you.</p>
  </div>
  <div style="display:flex;flex-direction:column">
    <div style="display:flex;gap:13px;align-items:flex-start;padding:8px 0"><div class="p4step-c">1</div><p class="p4sub" style="font-size:13px;padding-top:7px">The urge peaks. You don't give in. That's your first victory.</p></div>
    <div style="display:flex;gap:13px;align-items:flex-start;padding:8px 0"><div class="p4step-c">2</div><p class="p4sub" style="font-size:13px;padding-top:7px">Withdrawal sets in. Your brain begins to recalibrate.</p></div>
    <div style="display:flex;gap:13px;align-items:flex-start;padding:8px 0"><div class="p4step-c">3</div><p class="p4sub" style="font-size:13px;padding-top:7px">The hardest day. Most people quit here. You keep going.</p></div>
    <div style="display:flex;gap:13px;align-items:flex-start;padding:8px 0"><div class="p4step-c">4</div><p class="p4sub" style="font-size:13px;padding-top:7px">Something shifts. The mental fog starts to lift.</p></div>
    <div style="display:flex;gap:13px;align-items:flex-start;padding:8px 0"><div class="p4step-c">5</div><p class="p4sub" style="font-size:13px;padding-top:7px">Small beauties return. The world feels less grey.</p></div>
    <div style="display:flex;gap:13px;align-items:flex-start;padding:8px 0"><div class="p4step-c">6</div><p class="p4sub" style="font-size:13px;padding-top:7px">Prayer feels more present. Your focus sharpens.</p></div>
    <div style="display:flex;gap:13px;align-items:flex-start;padding:8px 0"><div class="p4step-c done">7</div><p style="font-size:13px;font-weight:700;color:#111827;padding-top:7px">One week clean. A real foundation is set.</p></div>
  </div>
  <div style="text-align:center;font-weight:700;font-size:14px;color:#111827;line-height:1.9">Each of these is waiting for you.<br>It starts today.</div>
  <button class="p4btn" onclick="p4go(27)">Continue</button>
</div>

<!-- P4 S27 -->
<div class="p4screen" id="p4s27">
  <div>
    <div style="color:#0EA5C9;font-weight:700;font-size:11px;letter-spacing:2px;text-transform:uppercase">IF YOU SLIP</div>
    <h1 style="margin-top:6px">Log It, Don't Hide It</h1>
    <p class="p4sub" style="margin-top:4px">Every relapse is data. Your honesty is the tool.</p>
  </div>
  <div class="p4card">
    <div style="font-weight:700;font-size:14px;margin-bottom:12px">What triggered you?</div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px">
      <button class="p4chip sel" onclick="p4pickChip(this)">Stress</button>
      <button class="p4chip" onclick="p4pickChip(this)">Boredom</button>
      <button class="p4chip" onclick="p4pickChip(this)">Late Night</button>
    </div>
    <div style="display:flex;align-items:center;gap:8px;color:#6B7280;font-size:13px">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#6B7280" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      <strong style="color:#374151">11:30 PM</strong><span>· When it happened</span>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:4px">
    <p style="font-style:italic;font-size:13px;color:#6B7280;text-align:center">Select what triggered you — no judgement, just honesty</p>
    <p style="font-style:italic;font-size:13px;color:#6B7280;text-align:center">Note the time — patterns emerge from when it tends to happen</p>
  </div>
  <div class="p4card">
    <div style="font-weight:700;font-size:14px;margin-bottom:13px">Your pattern, over time</div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:9px"><span style="width:62px;font-size:13px;color:#374151">Evening</span><div style="flex:1;background:#E5E7EB;border-radius:999px;height:8px"><div style="width:60%;background:#0EA5C9;border-radius:999px;height:8px"></div></div><span style="font-size:13px;width:32px;text-align:right;color:#374151">60%</span></div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:9px"><span style="width:62px;font-size:13px;color:#374151">Night</span><div style="flex:1;background:#E5E7EB;border-radius:999px;height:8px"><div style="width:30%;background:#0EA5C9;border-radius:999px;height:8px"></div></div><span style="font-size:13px;width:32px;text-align:right;color:#374151">30%</span></div>
    <div style="display:flex;align-items:center;gap:10px"><span style="width:62px;font-size:13px;color:#374151">Morning</span><div style="flex:1;background:#E5E7EB;border-radius:999px;height:8px"><div style="width:10%;background:#0EA5C9;border-radius:999px;height:8px"></div></div><span style="font-size:13px;width:32px;text-align:right;color:#374151">10%</span></div>
  </div>
  <div style="font-weight:700;font-size:13.5px;color:#111827;text-align:center">Over time, your logs reveal your weak spots — so you can protect them</div>
  <button class="p4btn" onclick="p4go(28)">Continue</button>
</div>

<!-- P4 S28 -->
<div class="p4screen" id="p4s28">
  <div style="text-align:center">
    <div style="color:#0EA5C9;font-weight:700;font-size:11px;letter-spacing:2px;text-transform:uppercase">REPENTANCE LIVES</div>
    <h1 style="margin-top:6px">A Safety Net for When You Slip</h1>
    <p class="p4sub" style="margin-top:6px">One stumble doesn't erase your progress.</p>
  </div>
  <div style="text-align:center">
    <div style="font-size:40px;letter-spacing:6px">❤️❤️❤️</div>
    <div style="font-weight:600;font-size:14px;margin-top:6px">3 lives available</div>
    <p class="p4sub" style="font-size:13px;margin-top:6px">When you relapse, you can spend a life to protect your journey progress</p>
  </div>
  <div class="p4card" style="display:flex;overflow:hidden;padding:0">
    <div style="flex:1;padding:16px;text-align:center;border-right:1px solid #E5E7EB">
      <div style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;padding:2px 8px;border-radius:4px;background:#FEE2E2;color:#B91C1C">RESETS</div>
      <div class="p4sub" style="font-size:12px;margin-top:6px">Streak</div>
      <div style="font-size:34px;font-weight:800;color:#EF4444">0</div>
      <div class="p4sub" style="font-size:12px">days</div>
    </div>
    <div style="flex:1;padding:16px;text-align:center">
      <div style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;padding:2px 8px;border-radius:4px;background:#E0F7FA;color:#0369A1">PROTECTED</div>
      <div class="p4sub" style="font-size:12px;margin-top:6px">Journey Day</div>
      <div style="font-size:34px;font-weight:800;color:#0EA5C9">47</div>
      <div class="p4sub" style="font-size:12px">of 360</div>
    </div>
  </div>
  <p class="p4sub" style="text-align:center;font-size:13px">Your consecutive streak resets — but your place in the 360-day programme stays intact</p>
  <div class="p4card">
    <div style="font-weight:700;font-size:14px;margin-bottom:12px">How to earn a life back</div>
    <div style="display:flex;align-items:center;gap:12px">
      <div style="background:#E0F7FA;border-radius:11px;padding:10px 14px;text-align:center"><div style="font-size:22px;font-weight:800;color:#0EA5C9">10</div><div style="font-size:11px;color:#0EA5C9;font-weight:600">clean days</div></div>
      <span style="font-size:18px;color:#6B7280">→</span>
      <span style="font-size:26px">❤️</span>
      <span style="font-weight:700;font-size:14px">+1 life restored</span>
    </div>
    <div class="p4sub" style="font-size:11px;font-style:italic;margin-top:10px">Maximum 3 lives at any time</div>
  </div>
  <button class="p4btn" onclick="p4go(29)">Got it — continue</button>
</div>

<!-- P4 S29 -->
<div class="p4screen" id="p4s29">
  <div style="text-align:center">
    <h1>What is your intention?</h1>
    <p style="font-style:italic;font-size:14px;color:#374151;margin-top:8px">Write it for Allah alone.</p>
  </div>
  <div>
    <div style="font-weight:700;font-size:14px;margin-bottom:10px">My intention for quitting is...</div>
    <textarea id="p4itxt" maxlength="200" placeholder="To strengthen my iman and draw closer to Allah"
      oninput="document.getElementById('p4icnt').textContent=this.value.length+'/200';document.getElementById('p4s29btn').style.opacity=this.value.trim()?'1':'0.4'"
      style="width:100%;border:none;border-bottom:2px solid #0EA5C9;outline:none;font-size:14px;color:#374151;background:transparent;resize:none;padding:8px 0;min-height:55px;font-family:inherit"></textarea>
    <div style="text-align:right;font-size:11px;color:#9CA3AF" id="p4icnt">0/200</div>
  </div>
  <div class="p4card">
    <div style="font-weight:700;font-size:14px;margin-bottom:10px">Example intentions:</div>
    <div class="p4sub" style="font-size:13px;line-height:2.1">• To purify my heart for Allah<br>• To become a better Muslim and role model<br>• To strengthen my family relationships<br>• To prepare myself for a blessed marriage</div>
  </div>
  <div class="p4qbox">"Actions are judged by intentions"<div class="p4qsrc">Hadith - Bukhari &amp; Muslim</div></div>
  <button class="p4btn" id="p4s29btn" style="opacity:.4" onclick="if(document.getElementById('p4itxt').value.trim())p4go(30)">Continue</button>
</div>

<!-- P4 S30 -->
<div class="p4screen" id="p4s30">
  <div style="text-align:center">
    <h1>Your Porn-Free Date</h1>
    <p class="p4sub" style="margin-top:8px;font-weight:500">Aim to be completely free 90 days from your quit date.</p>
  </div>
  <div style="display:flex;justify-content:center">
    <div style="width:158px;height:158px;border-radius:50%;border:3px solid #0EA5C9;background:#F0FBFF;display:flex;flex-direction:column;align-items:center;justify-content:center">
      <div style="font-size:46px;font-weight:800;color:#0EA5C9">90</div>
      <div style="font-size:10px;font-weight:700;color:#0EA5C9;letter-spacing:1px">DAYS TO</div>
      <div style="font-size:10px;font-weight:700;color:#0EA5C9;letter-spacing:1px">FREEDOM</div>
    </div>
  </div>
  <div style="text-align:center">
    <div style="font-size:10px;font-weight:700;color:#6B7280;letter-spacing:1.5px;text-transform:uppercase">TARGET FREEDOM DATE</div>
    <div style="font-size:19px;font-weight:800;color:#111827;margin-top:4px" id="p4free-date-lbl">Friday, August 28, 2026</div>
  </div>
  <div style="background:white;border-left:4px solid #0EA5C9;border-radius:0 11px 11px 0;padding:14px 16px;box-shadow:0 1px 3px rgba(0,0,0,.05)">
    <div style="font-weight:700;font-size:14px;margin-bottom:7px">Why 90 Days?</div>
    <p class="p4sub" style="font-size:13px">Research shows it takes approximately 90 days to break addiction patterns and rewire the brain. This gives your mind time to heal and establish new, healthy habits.</p>
  </div>
  <div class="p4qbox">"And give good tidings to the patient, Who, when disaster strikes them, say, 'Indeed we belong to Allah, and indeed to Him we will return'"<div class="p4qsrc">(Surah Al-Baqarah 2:155-156)</div></div>
  <button class="p4btn" onclick="p4go(31)">Continue</button>
</div>

<!-- P4 S31 -->
<div class="p4screen" id="p4s31">
  <div class="p4card" style="text-align:center;padding:18px 16px;cursor:pointer" onclick="p4openTimePicker()">
    <div style="font-size:32px;font-weight:800;color:#0EA5C9" id="p4time-display">8:00 PM</div>
    <div style="font-size:12px;color:#9CA3AF;margin-top:4px">Tap to change</div>
  </div>
  <div class="p4card"><div style="display:flex;gap:12px;align-items:center"><div class="p4ibox" style="background:#FEF3C7"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg></div><div style="flex:1"><div style="font-weight:700;font-size:14px;color:#111827">Morning Adhkar</div><div class="p4sub" style="font-size:12px;margin-top:3px">Start your day with morning remembrance</div></div><div class="p4tog" id="p4t_morning" onclick="p4tog('p4t_morning')"><div class="p4togdot"></div></div></div></div>
  <div class="p4card"><div style="display:flex;gap:12px;align-items:center"><div class="p4ibox" style="background:#EDE9FE"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#7C3AED" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg></div><div style="flex:1"><div style="font-weight:700;font-size:14px;color:#111827">Evening Adhkar</div><div class="p4sub" style="font-size:12px;margin-top:3px">End your day with evening remembrance</div></div><div class="p4tog" id="p4t_evening" onclick="p4tog('p4t_evening')"><div class="p4togdot"></div></div></div></div>
  <div class="p4card"><div style="display:flex;gap:12px;align-items:center"><div class="p4ibox" style="background:#E0F7FA"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></div><div style="flex:1"><div style="font-weight:700;font-size:14px;color:#111827">Purification Module</div><div class="p4sub" style="font-size:12px;margin-top:3px">Daily lessons from Ibn Qayyim</div></div><div class="p4tog" id="p4t_purify" onclick="p4tog('p4t_purify')"><div class="p4togdot"></div></div></div></div>
  <div class="p4card"><div style="display:flex;gap:12px;align-items:center"><div class="p4ibox" style="background:#E0F7FA"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-1.96-3 2.5 2.5 0 0 1-1.32-4.24 3 3 0 0 1 .34-5.58 2.5 2.5 0 0 1 1.32-4.24A2.5 2.5 0 0 1 9.5 2"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 1.96-3 2.5 2.5 0 0 0 1.32-4.24 3 3 0 0 0-.34-5.58 2.5 2.5 0 0 0-1.32-4.24A2.5 2.5 0 0 0 14.5 2"/></svg></div><div style="flex:1"><div style="font-weight:700;font-size:14px;color:#111827">Neuroscience Module</div><div class="p4sub" style="font-size:12px;margin-top:3px">Breaking Free: Understand your recovery</div></div><div class="p4tog" id="p4t_neuro" onclick="p4tog('p4t_neuro')"><div class="p4togdot"></div></div></div></div>
  <div class="p4qbox" style="display:flex;gap:10px;align-items:flex-start"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0EA5C9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-top:2px"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg><span>"And remind, for indeed, the reminder benefits the believers." <div class="p4qsrc">- Quran 51:55</div></span></div>
  <button class="p4btn" id="p4notif-btn" onclick="p4enableNotifications()">Enable Notifications</button>
  <div style="text-align:center"><span style="font-size:13px;color:#6B7280;text-decoration:underline;cursor:pointer" onclick="p4goDone()">Skip for now</span></div>
</div>

<!-- P4 DONE -->
<div class="p4screen" id="p4sdone" style="align-items:center;text-align:center;padding-top:50px">
  <div style="font-size:60px">🌟</div>
  <h1>Bismillah. Your journey begins.</h1>
  <p class="p4sub">You've taken the first step. Every moment of strength from here is written for you.</p>
  <div class="p4qbox" style="text-align:left">"Verily, with hardship comes ease."<div class="p4qsrc">Surah Ash-Sharh 94:6</div></div>
  <button class="p4btn" onclick="finishFullOnboarding()" style="margin-top:24px; padding:18px; font-size:17px; background:linear-gradient(90deg,#0EA5C9,#06B6D4); box-shadow:0 4px 15px rgba(14,165,201,0.4); cursor:pointer;">Start Day 1 in App &rarr;</button>

</div>

</div><!-- end .p4app -->

<!-- P4 CALENDAR OVERLAY -->
<div class="p4cal-overlay" id="p4cal-overlay" style="display:none" onclick="if(event.target===this)p4closeCal()">
  <div class="p4cal-sheet">
    <div class="p4cal-header">
      <button class="p4cal-nav" onclick="p4calPrevMonth()">&#8249;</button>
      <div style="font-weight:700;font-size:16px;color:#111827" id="p4cal-month-lbl">May 2026</div>
      <button class="p4cal-nav" onclick="p4calNextMonth()">&#8250;</button>
    </div>
    <div class="p4cal-grid" id="p4cal-grid"></div>
    <div style="display:flex;gap:10px;margin-top:16px">
      <button onclick="p4closeCal()" style="flex:1;padding:13px;border-radius:12px;border:1.5px solid #E5E7EB;background:white;font-size:14px;font-weight:600;cursor:pointer;color:#374151">Cancel</button>
      <button onclick="p4confirmDate()" style="flex:1;padding:13px;border-radius:12px;border:none;background:linear-gradient(90deg,#0EA5C9,#06B6D4);color:white;font-size:14px;font-weight:700;cursor:pointer">Confirm</button>
    </div>
  </div>
</div>

<!-- P4 TIME PICKER OVERLAY -->
<div class="p4cal-overlay" id="p4time-overlay" style="display:none" onclick="if(event.target===this)p4closeTimePicker()">
  <div class="p4cal-sheet">
    <div class="p4cal-header">
      <div style="font-weight:700;font-size:17px;color:#111827">Set Reminder Time</div>
      <button class="p4cal-nav" onclick="p4closeTimePicker()" style="font-size:20px;color:#9CA3AF">✕</button>
    </div>
    <div style="display:flex;justify-content:center;align-items:center;gap:8px;padding:20px 0">
      <div style="display:flex;flex-direction:column;align-items:center;gap:6px">
        <button onclick="p4changeHour(1)" style="background:none;border:none;font-size:22px;color:#0EA5C9;cursor:pointer">▲</button>
        <div id="p4tp-hour" style="font-size:36px;font-weight:800;color:#111827;width:60px;text-align:center">08</div>
        <button onclick="p4changeHour(-1)" style="background:none;border:none;font-size:22px;color:#0EA5C9;cursor:pointer">▼</button>
      </div>
      <div style="font-size:32px;font-weight:800;color:#111827;padding-bottom:4px">:</div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:6px">
        <button onclick="p4changeMin(1)" style="background:none;border:none;font-size:22px;color:#0EA5C9;cursor:pointer">▲</button>
        <div id="p4tp-min" style="font-size:36px;font-weight:800;color:#111827;width:60px;text-align:center">00</div>
        <button onclick="p4changeMin(-1)" style="background:none;border:none;font-size:22px;color:#0EA5C9;cursor:pointer">▼</button>
      </div>
      <div style="display:flex;flex-direction:column;gap:8px;margin-left:8px">
        <button id="p4tp-am" onclick="p4setAmPm('AM')" style="padding:8px 14px;border-radius:10px;border:2px solid #E5E7EB;background:white;font-weight:700;font-size:14px;cursor:pointer;color:#374151">AM</button>
        <button id="p4tp-pm" onclick="p4setAmPm('PM')" style="padding:8px 14px;border-radius:10px;border:2px solid #0EA5C9;background:#E0F7FA;font-weight:700;font-size:14px;cursor:pointer;color:#0EA5C9">PM</button>
      </div>
    </div>
    <div style="display:flex;gap:10px;margin-top:6px">
      <button onclick="p4closeTimePicker()" style="flex:1;padding:13px;border-radius:12px;border:1.5px solid #E5E7EB;background:white;font-size:14px;font-weight:600;cursor:pointer;color:#374151">Cancel</button>
      <button onclick="p4confirmTime()" style="flex:1;padding:13px;border-radius:12px;border:none;background:linear-gradient(90deg,#0EA5C9,#06B6D4);color:white;font-size:14px;font-weight:700;cursor:pointer">Set Time</button>
    </div>
  </div>
</div>

</div><!-- end #phase4-wrap -->


</html>
  </div>
</div>
<style>

/* ============================================================ */
/* === MASTER UNIFIED RESPONSIVE SIZING FOR ALL 31 ONBOARDING SCREENS === */
/* ============================================================ */
#onboardingFlowContainer {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  height: 100dvh !important;
  z-index: 9990 !important;
  background: #f1f5f9 !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch !important;
  margin: 0 !important;
  padding: 0 !important;
}

#onboardingFlowContainer > div {
  width: 100% !important;
  min-height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start !important;
  padding: 0 !important;
  margin: 0 !important;
}

.splash,
.p1-wrap,
.urge-screen,
.p2-wrap,
#phase3-wrap,
#phase3-wrap .phone,
#phase4-wrap,
.p4app {
  width: 100% !important;
  max-width: 430px !important;
  margin: 0 auto !important;
  box-sizing: border-box !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch !important;
}

.screen-p1,
.screen,
.screen22,
.pur-screen22,
.bf-screen22,
.dr-screen22 {
  min-height: 100vh !important;
  min-height: 100dvh !important;
  box-sizing: border-box !important;
  display: flex !important;
  flex-direction: column !important;
  padding-bottom: calc(24px + env(safe-area-inset-bottom, 0px)) !important;
}

.screen22:not(.active),
.pur-screen22:not(.active),
.bf-screen22:not(.active),
.dr-screen22:not(.active),
.screen:not(.active),
.screen-p1:not(.active) {
  display: none !important;
}

@media (max-width: 480px) {
  #onboardingFlowContainer {
    background: #ffffff !important;
  }
  .splash,
  .p1-wrap,
  .urge-screen,
  .p2-wrap,
  #phase3-wrap,
  #phase3-wrap .phone,
  #phase4-wrap,
  .p4app {
    width: 100% !important;
    max-width: 100% !important;
    min-height: 100vh !important;
    min-height: 100dvh !important;
    border-radius: 0 !important;
    border: none !important;
    box-shadow: none !important;
    margin: 0 !important;
  }
  .splash {
    height: 100vh !important;
    height: 100dvh !important;
  }
}

@media (min-width: 481px) {
  .splash,
  .p1-wrap,
  .urge-screen,
  .p2-wrap,
  #phase3-wrap .phone,
  .p4app {
    min-height: calc(100vh - 32px) !important;
    min-height: calc(100dvh - 32px) !important;
    border-radius: 28px !important;
    border: 1px solid #d0d8e4 !important;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.12) !important;
    margin: 16px auto !important;
  }
  .splash {
    height: calc(100vh - 32px) !important;
    height: calc(100dvh - 32px) !important;
  }
}

</style>"""

ONBOARDING_JS = """// ===== PHASE 3 NAVIGATION =====
function goToPhase3(screenId) {
  // Hide phase 2
  document.querySelector('.p2-wrap').style.display = 'none';
  // Show phase 3
  document.getElementById('phase3-wrap').style.display = 'block';
  goTo22(screenId);
  if (screenId === 's20') animateBars22();
}

function goTo22(id) {
  document.querySelectorAll('#phase3Phone .screen22').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('#phase3Phone .pur-screen22').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('#phase3Phone .bf-screen22').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('#phase3Phone .dr-screen22').forEach(s => s.classList.remove('active'));
  var el = document.getElementById(id);
  if (el) el.classList.add('active');
  if (id === 's20') animateBars22();
}

// Chart for phase 3 (s19 doesn't have chart; it's on s17 which is already in 16_TAK)
// No duplicate chart needed here

function animateBars22() {
  setTimeout(function() {
    var b1 = document.getElementById('bar1');
    var b2 = document.getElementById('bar2');
    var p1 = document.getElementById('pct1');
    var p2 = document.getElementById('pct2');
    if (!b1) return;
    b1.style.width = '30%';
    b2.style.width = '90%';
    var v1 = 0, v2 = 0;
    var iv = setInterval(function() {
      if (v1 < 30) { v1++; p1.textContent = v1 + '%'; }
      if (v2 < 90) { v2 += 3; if (v2 > 90) v2 = 90; p2.textContent = v2 + '%'; }
      if (v1 >= 30 && v2 >= 90) clearInterval(iv);
    }, 20);
  }, 400);
}

// Purification screens
function openPur() {
  document.querySelectorAll('#phase3Phone .screen22').forEach(s => s.classList.remove('active'));
  document.getElementById('pur1').classList.add('active');
}
function goToPur22(id) {
  document.querySelectorAll('#phase3Phone .pur-screen22').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}
function closePur22() {
  document.querySelectorAll('#phase3Phone .pur-screen22').forEach(s => s.classList.remove('active'));
  document.getElementById('s22').classList.add('active');
  markDone22('ibn-item');
  updateModuleCount22();
}
function checkPurText22() {
  var txt = document.getElementById('reflectionText');
  var btn = document.getElementById('purContBtn');
  btn.disabled = txt.value.trim().length === 0;
}

// Breaking Free screens
var bfDone22 = false;
function openBF() {
  document.querySelectorAll('#phase3Phone .screen22').forEach(s => s.classList.remove('active'));
  document.getElementById('bf1').classList.add('active');
}
function goToBF22(id) {
  document.querySelectorAll('#phase3Phone .bf-screen22').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}
function closeBF22() {
  document.querySelectorAll('#phase3Phone .bf-screen22').forEach(s => s.classList.remove('active'));
  document.getElementById('s22').classList.add('active');
  bfDone22 = true;
  markDone22('bf-item');
  updateModuleCount22();
}
function checkBFText22() {
  var txt = document.getElementById('bfReflectionText');
  var btn = document.getElementById('bfContBtn');
  btn.disabled = txt.value.trim().length === 0;
}

// Daily Reminder
var drDone22 = false;
function openDR() {
  document.querySelectorAll('#phase3Phone .screen22').forEach(s => s.classList.remove('active'));
  document.getElementById('dr1').classList.add('active');
}
function closeDR22() {
  document.querySelectorAll('#phase3Phone .dr-screen22').forEach(s => s.classList.remove('active'));
  document.getElementById('s22').classList.add('active');
  drDone22 = true;
  markDone22('dr-item');
  updateModuleCount22();
}

function markDone22(itemId) {
  var item = document.getElementById(itemId);
  if (!item) return;
  item.style.background = '#eafaf4';
  item.style.border = '1.5px solid #22a06b';
  var icon = item.querySelector('.lesson-icon');
  if (icon) { icon.style.background = '#d0f0e4'; icon.innerHTML = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#22a06b" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>'; }
  var lbl = item.querySelector('.lesson-label');
  if (lbl) lbl.style.color = '#22a06b';
  var arrow = item.querySelector('.lesson-arrow');
  if (arrow) arrow.textContent = '';
  item.onclick = null;
}
function updateModuleCount22() {
  var count = 0;
  if (document.getElementById('ibn-item') && document.getElementById('ibn-item').onclick === null) count++;
  if (bfDone22) count++;
  if (drDone22) count++;
  var sub = document.getElementById('modules-sub');
  var contBtn = document.getElementById('s22ContinueBtn');
  if (count === 3) {
    if (sub) sub.textContent = 'Day 1 complete. Well done.';
    if (contBtn) contBtn.style.display = 'block';
  } else {
    if (sub) sub.textContent = count + ' of 3 modules done — keep going';
    if (contBtn) contBtn.style.display = 'none';
  }
}

// ================================================================
// PHASE 1 JAVASCRIPT (6_tak screens)
// ================================================================
const questions = [
  { q:"Do you watch pornography more than once a week?", help:"Your answers help us support you better.", type:"mental" },
  { q:"Does pornography use interfere with your daily responsibilities?", help:"Your answers help us support you better.", type:"mental" },
  { q:"Do you feel guilty or ashamed after watching pornography?", help:"Your answers help us support you better.", type:"spiritual" },
  { q:"Have you tried to stop but found it difficult?", help:"Your answers help us support you better.", type:"mental" },
  { q:"Does pornography use affect your relationships or spiritual life?", help:"Your answers help us support you better.", type:"relational" }
];
let current=0, answers=[];
const ulWidths=[28,46,64,82,100];

function showQ(){
  document.getElementById('splash-screen').classList.add('hidden');
  document.getElementById('q-screen').classList.remove('hidden');
  current=0; answers=[];
}

function answer(isYes){
  answers.push({yes:isYes, type:questions[current].type});
  current++;
  if(current<5){
    document.getElementById('q-badge').textContent='Q'+(current+1);
    document.getElementById('q-text').textContent=questions[current].q;
    document.getElementById('q-help').textContent=questions[current].help;
    document.getElementById('q-count-text').textContent='Question '+(current+1)+' of 6';
    document.getElementById('prog-bar').style.width=((current+1)/6*100)+'%';
    document.getElementById('underline-blue').style.width=ulWidths[current]+'px';
  } else {
    document.getElementById('q-screen').classList.add('hidden');
    document.getElementById('q6-screen').classList.remove('hidden');
  }
}

function goResults(freq){
  document.getElementById('q6-screen').classList.add('hidden');
  document.getElementById('results-screen').classList.remove('hidden');
  let mY=answers.filter(a=>a.type==='mental'&&a.yes).length;
  let mT=answers.filter(a=>a.type==='mental').length;
  let sY=answers.filter(a=>a.type==='spiritual'&&a.yes).length;
  let rY=answers.filter(a=>a.type==='relational'&&a.yes).length;
  let total=answers.filter(a=>a.yes).length;
  let fb=(freq-1)*8;
  let mp=Math.min(95,Math.round((mY/Math.max(mT,1))*70+fb+10));
  let sp=Math.min(95,Math.round((sY+((freq>2)?1:0))/2*80+fb+10));
  let rp=Math.min(95,Math.round((rY+(total>2?1:0))/2*70+fb+10));
  document.getElementById('score-display').textContent=total+'/6';
  document.getElementById('result-desc').textContent=total<=1
    ? "Your responses suggest minimal challenges. Keep up the good work and stay vigilant."
    : total<=3
    ? "Your responses indicate some challenges with pornography use. Recovery support can be beneficial."
    : "Your responses indicate significant challenges. This app will guide you step by step to freedom.";
  setTimeout(function(){
    document.getElementById('bar-mental').style.width=mp+'%';
    document.getElementById('bar-spiritual').style.width=sp+'%';
    document.getElementById('bar-relational').style.width=rp+'%';
    animNumP1('mental-pct',0,mp,1400);
    animNumP1('spiritual-pct',0,sp,1400);
    animNumP1('relational-pct',0,rp,1400);
  },200);
}

function animNumP1(id,from,to,dur){
  const el=document.getElementById(id);
  const t0=performance.now();
  function u(t){ const p=Math.min((t-t0)/dur,1); const e=1-Math.pow(1-p,3); el.textContent=Math.round(from+(to-from)*e)+'%'; if(p<1) requestAnimationFrame(u); }
  requestAnimationFrame(u);
}

function showGender(){
  document.getElementById('results-screen').classList.add('hidden');
  document.getElementById('gender-screen').classList.remove('hidden');
}

function selectGender(g){
  document.getElementById('card-male').classList.remove('selected');
  document.getElementById('card-female').classList.remove('selected');
  document.getElementById('card-'+g).classList.add('selected');
}

function showUrge(){
  document.getElementById('gender-screen').classList.add('hidden');
  document.getElementById('urge-screen').classList.remove('hidden');
  const bar=document.getElementById('urge-bar');
  const txt=document.getElementById('urge-pct-text');
  setTimeout(function(){ bar.style.width='75%'; animNumEl(txt,0,75,1500); },300);
  setTimeout(function(){ document.getElementById('card-dhikr').classList.add('visible'); },600);
  setTimeout(function(){ document.getElementById('card-breathe').classList.add('visible'); },800);
  setTimeout(function(){ document.getElementById('card-dua').classList.add('visible'); },1000);
}

function animNumEl(el,from,to,dur){
  const t0=performance.now();
  function u(t){ const p=Math.min((t-t0)/dur,1); const e=1-Math.pow(1-p,3); el.textContent=Math.round(from+(to-from)*e)+'%'; if(p<1) requestAnimationFrame(u); }
  requestAnimationFrame(u);
}

// DUA
const D_DUAS=["Astaghfirullah (I seek forgiveness from Allah)","A'udhu billahi mina ash-shaytanir rajeem","La hawla wa la quwwata illa billah","Hasbunallahu wa ni'mal wakeel","Subhanallah wa bihamdihi"];
let dCurrentDua=0,dCount=0,dUrge=75,dRunning=false;
const D_STEPS=10;

function showDua(){
  document.getElementById('urge-screen').classList.add('hidden');
  document.getElementById('dua-screen').classList.remove('hidden');
  dCurrentDua=0; dCount=0; dUrge=75; dRunning=true;
  document.getElementById('d-dua-text').textContent=D_DUAS[0];
  document.getElementById('d-count-display').textContent='0 / '+D_STEPS;
  document.getElementById('d-urge-pct').textContent='75%';
  document.getElementById('d-urge-bar').style.width='75%';
  document.getElementById('d-dua-block').style.display='flex';
  document.getElementById('d-done-block').style.display='none';
}

function reciteDua(){
  if(!dRunning) return;
  dCount++;
  const totalDone=(dCurrentDua*D_STEPS)+dCount;
  const totalNeeded=D_DUAS.length*D_STEPS;
  const prog=totalDone/totalNeeded;
  dUrge=Math.round(75-(75-15)*prog);
  document.getElementById('d-urge-pct').textContent=dUrge+'%';
  document.getElementById('d-urge-bar').style.width=dUrge+'%';
  document.getElementById('d-count-display').textContent=dCount+' / '+D_STEPS;
  const btn=document.getElementById('d-recite-btn');
  btn.style.transform='scale(0.95)';
  setTimeout(function(){btn.style.transform='scale(1)';},120);
  if(dCount>=D_STEPS){
    dCount=0; dCurrentDua++;
    if(dCurrentDua>=D_DUAS.length || dUrge<=15){
      dRunning=false;
      document.getElementById('d-urge-pct').textContent='15%';
      document.getElementById('d-urge-bar').style.width='15%';
      document.getElementById('d-dua-block').style.display='none';
      document.getElementById('d-done-block').style.display='flex';
    } else {
      document.getElementById('d-dua-text').textContent=D_DUAS[dCurrentDua];
      document.getElementById('d-count-display').textContent='0 / '+D_STEPS;
    }
  }
}

// DHIKR
const ZK_SEQUENCE=[
  {text:'SubhanAllah',arabic:'سُبْحَانَ اللّٰهُ',meaning:'Glory be to Allah',target:33},
  {text:'Alhamdulillah',arabic:'اَلْحَمْدُ لِلّٰهِ',meaning:'All praise is for Allah',target:33},
  {text:'Allahu Akbar',arabic:'اَللّٰهُ أَكْبَرُ',meaning:'Allah is the Greatest',target:34}
];
let zkPhase=0,zkCount=0,zkRunning=false;

function showDhikr(){
  document.getElementById('urge-screen').classList.add('hidden');
  document.getElementById('dhikr-screen').classList.remove('hidden');
  zkPhase=0; zkCount=0; zkRunning=true;
  zkRender();
  document.getElementById('zk-urge-pct').textContent='75%';
  document.getElementById('zk-urge-bar').style.width='75%';
  document.getElementById('zk-dhikr-block').style.display='flex';
  document.getElementById('zk-done-block').style.display='none';
}

function zkRender(){
  const ph=ZK_SEQUENCE[zkPhase];
  document.getElementById('zk-arabic').textContent=ph.arabic;
  document.getElementById('zk-text').textContent=ph.text;
  document.getElementById('zk-meaning').textContent=ph.meaning;
  document.getElementById('zk-counter').textContent=zkCount+' / '+ph.target;
  document.getElementById('zk-p1-done').textContent=(zkPhase>0?ZK_SEQUENCE[0].target:(zkPhase===0?zkCount:0))+'/'+ZK_SEQUENCE[0].target;
  document.getElementById('zk-p2-done').textContent=(zkPhase>1?ZK_SEQUENCE[1].target:(zkPhase===1?zkCount:0))+'/'+ZK_SEQUENCE[1].target;
  document.getElementById('zk-p3-done').textContent=(zkPhase>2?ZK_SEQUENCE[2].target:(zkPhase===2?zkCount:0))+'/'+ZK_SEQUENCE[2].target;
  const phasePct=zkPhase/3, inPhasePct=zkCount/ph.target;
  const total=phasePct+inPhasePct/3;
  const urge=Math.round(75-(75-15)*total);
  document.getElementById('zk-urge-pct').textContent=urge+'%';
  document.getElementById('zk-urge-bar').style.width=urge+'%';
}

function tapDhikr(){
  if(!zkRunning) return;
  zkCount++;
  const ph=ZK_SEQUENCE[zkPhase];
  const btn=document.getElementById('zk-tap-btn');
  btn.style.transform='scale(0.93)';
  setTimeout(function(){btn.style.transform='scale(1)';},110);
  if(zkCount>=ph.target){
    zkPhase++;
    if(zkPhase>=ZK_SEQUENCE.length){
      zkRunning=false;
      document.getElementById('zk-urge-pct').textContent='15%';
      document.getElementById('zk-urge-bar').style.width='15%';
      document.getElementById('zk-dhikr-block').style.display='none';
      document.getElementById('zk-done-block').style.display='flex';
      return;
    }
    zkCount=0;
  }
  zkRender();
}

// BREATHE
const B_PHASES=[
  {name:'INHALE',dur:4,hint:'through nose',color:'#2196F3'},
  {name:'HOLD',dur:7,hint:'Hold gently',color:'#9c27b0'},
  {name:'EXHALE',dur:8,hint:'through mouth',color:'#00897b'}
];
let bRunning=false,bTimer=null,bPi=0,bTick=4,bElapsed=0;
const B_TOTAL_SECS=3*(4+7+8);

function showBreathe(){
  document.getElementById('urge-screen').classList.add('hidden');
  document.getElementById('breathe-screen').classList.remove('hidden');
  bRunning=true; bPi=0; bTick=B_PHASES[0].dur; bElapsed=0;
  bSetPhase(0);
  if(bTimer) clearInterval(bTimer);
  bTimer=setInterval(bStep,1000);
}

function bSetPhase(i){
  bPi=i;
  document.getElementById('b-phase-name').textContent=B_PHASES[i].name;
  document.getElementById('b-phase-name').style.color=B_PHASES[i].color;
  document.getElementById('b-phase-num').textContent=bTick;
  document.getElementById('b-phase-hint').textContent=B_PHASES[i].hint;
  document.getElementById('b-circle').style.borderColor=B_PHASES[i].color;
}

function bStep(){
  if(!bRunning) return;
  bElapsed++;
  const prog=Math.min(bElapsed/B_TOTAL_SECS,1);
  const val=Math.round(75-(75-15)*prog);
  document.getElementById('b-urge-pct').textContent=val+'%';
  document.getElementById('b-urge-bar').style.width=val+'%';
  bTick--;
  document.getElementById('b-phase-num').textContent=bTick;
  if(bTick<=0){
    bPi=(bPi+1)%3;
    bTick=B_PHASES[bPi].dur;
    bSetPhase(bPi);
  }
  if(bElapsed>=B_TOTAL_SECS){
    bRunning=false; clearInterval(bTimer);
    document.getElementById('b-urge-pct').textContent='15%';
    document.getElementById('b-urge-bar').style.width='15%';
    document.getElementById('b-breathe-block').style.display='none';
    document.getElementById('b-done-block').style.display='flex';
  }
}

// USERNAME
function showUsername(){
  ['breathe-screen','dhikr-screen','dua-screen','urge-screen'].forEach(function(id){
    var el=document.getElementById(id);
    if(el) el.classList.add('hidden');
  });
  document.getElementById('username-screen').classList.remove('hidden');
}

function onUsernameInput(el){
  var val=el.value.trim();
  var len=el.value.length;
  document.getElementById('username-count').textContent=len+'/20';
  var btn=document.getElementById('username-continue-btn');
  if(val.length>=3){
    btn.disabled=false; btn.style.background='#00bcd4'; btn.style.color='white'; btn.style.cursor='pointer';
  } else {
    btn.disabled=true; btn.style.background='#e2e8f0'; btn.style.color='#9aa3b2'; btn.style.cursor='not-allowed';
  }
}

// WHY STOP
const WS_OPTIONS=['Improve my iman (faith)','Strengthen family relationships','Regain self-respect and dignity','Better mental health','Improve focus and productivity','Prepare for marriage','Become a better Muslim','Break free from addiction'];
let wsSelected=new Set();

function showWhyStop(){
  document.getElementById('username-screen').classList.add('hidden');
  document.getElementById('whystop-screen').classList.remove('hidden');
  const container=document.getElementById('ws-options');
  container.innerHTML='';
  WS_OPTIONS.forEach(function(opt,i){
    const btn=document.createElement('button');
    btn.id='ws-opt-'+i;
    btn.onclick=function(){ toggleWS(i,btn); };
    btn.style.cssText='display:flex;align-items:center;gap:14px;background:white;border:1.5px solid #dde6f0;border-radius:14px;padding:15px 16px;cursor:pointer;font-family:Inter,sans-serif;width:100%;text-align:left;transition:all 0.15s;';
    btn.innerHTML='<div id="ws-chk-'+i+'" style="width:26px;height:26px;border-radius:7px;border:2px solid #dde6f0;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:white;"></div>'
      +'<span style="font-size:15px;font-weight:600;color:#1a1a2e;">'+opt+'</span>';
    container.appendChild(btn);
  });
}

function toggleWS(i,btn){
  const chk=document.getElementById('ws-chk-'+i);
  if(wsSelected.has(i)){
    wsSelected.delete(i);
    btn.style.background='white'; btn.style.borderColor='#dde6f0';
    chk.style.background='white'; chk.style.borderColor='#dde6f0'; chk.innerHTML='';
  } else {
    wsSelected.add(i);
    btn.style.background='#e4f6fb'; btn.style.borderColor='#00bcd4';
    chk.style.background='#00bcd4'; chk.style.borderColor='#00bcd4';
    chk.innerHTML='<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><polyline points="2,7 6,11 12,3" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  }
}

// *** KEY BRIDGE FUNCTION: WhyStop → Phase 2 ***
function startPhase2(){
  document.getElementById('whystop-screen').classList.add('hidden');
  document.getElementById('phase2').classList.add('active');
  window.scrollTo(0,0);
  go(7); // Start from screen7
}

// ================================================================
// PHASE 2 JAVASCRIPT (16.html screens 7-17)
// ================================================================
const sel = {s7: new Set(), s8: new Set()};
const TOTAL = 31;

function tog(el) {
  const key = el.dataset.key, g = el.dataset.g;
  if (sel[g].has(key)) { sel[g].delete(key); el.classList.remove('sel'); }
  else { sel[g].add(key); el.classList.add('sel'); }
}

function go(n) {
  document.querySelectorAll('#phase2 .screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen'+n).classList.add('active');
  const pct = (n/TOTAL)*100;
  document.getElementById('pFill').style.width = pct+'%';
  document.getElementById('pCtr').textContent = n+' of '+TOTAL;
  window.scrollTo(0,0);
  if (n===10) setTimeout(buildBars, 100);
  if (n===11) initSwipe();
  if (n===12) setTimeout(buildToll, 200);
  if (n===16) setTimeout(setupHold, 200);
  if (n===17) setTimeout(initChart, 150);
}

// BARS (Screen 10)
const BASE = {prayer:28, family:42, work:55, sport:38, intimacy:30};
const EFF7 = {
  anxiety:{prayer:3,family:2,work:4,sport:3,intimacy:2},
  concentration:{prayer:2,family:1,work:5,sport:2,intimacy:1},
  motivation:{prayer:4,family:2,work:6,sport:4,intimacy:2},
  guilt:{prayer:5,family:3,work:3,sport:2,intimacy:4},
  sexual_dysfunction:{prayer:1,family:2,work:2,sport:1,intimacy:8},
  family_argue:{prayer:2,family:6,work:3,sport:2,intimacy:3},
  isolation:{prayer:3,family:5,work:3,sport:4,intimacy:3},
  depression:{prayer:5,family:4,work:5,sport:4,intimacy:3},
  sleep:{prayer:3,family:2,work:4,sport:3,intimacy:2},
  self_esteem:{prayer:4,family:3,work:4,sport:3,intimacy:5}
};
const EFF8 = {
  prayers:{prayer:8,family:2,work:2,sport:1,intimacy:1},
  darkness:{prayer:5,family:3,work:3,sport:2,intimacy:2},
  imaan:{prayer:6,family:3,work:2,sport:2,intimacy:2},
  family_issues:{prayer:2,family:7,work:3,sport:2,intimacy:3},
  islamic_knowledge:{prayer:4,family:2,work:1,sport:1,intimacy:1},
  rizq:{prayer:2,family:2,work:5,sport:2,intimacy:1},
  fears:{prayer:3,family:2,work:4,sport:3,intimacy:2},
  distance_allah:{prayer:7,family:2,work:2,sport:2,intimacy:2},
  dua:{prayer:5,family:2,work:2,sport:1,intimacy:2},
  spiritual_motivation:{prayer:5,family:2,work:3,sport:2,intimacy:2}
};

function calcBars() {
  const p = {...BASE};
  sel.s7.forEach(k => { const e=EFF7[k]||{}; for(const c in e) p[c]=Math.min(97,p[c]+e[c]); });
  sel.s8.forEach(k => { const e=EFF8[k]||{}; for(const c in e) p[c]=Math.min(97,p[c]+e[c]); });
  return p;
}

const BAR_LIST = [
  {key:'prayer',label:'Prayer & dhikr'},
  {key:'family',label:'Family time'},
  {key:'work',label:'Work & achievement'},
  {key:'sport',label:'Sport & hobbies'},
  {key:'intimacy',label:'Real intimacy'}
];

function animNum(el, to, dur) {
  const start = performance.now();
  (function step(now) {
    const t = Math.min((now-start)/dur,1);
    const ease = 1-Math.pow(1-t,3);
    el.textContent = Math.round(to*ease)+'%';
    if(t<1) requestAnimationFrame(step);
  })(performance.now());
}

function buildBars() {
  const pcts = calcBars();
  const wrap = document.getElementById('barsWrap');
  wrap.innerHTML = '';
  BAR_LIST.forEach(({key,label}) => {
    const row = document.createElement('div');
    row.className = 'bar-row';
    row.innerHTML = `<div class="bar-lr"><span class="bar-name">${label}</span><span class="bar-pct" id="bp_${key}">0%</span></div>
      <div class="bar-track"><div class="bar-red" id="br_${key}" style="width:0%"></div><div class="bar-grn" id="bg_${key}" style="width:0%"></div></div>`;
    wrap.appendChild(row);
  });
  requestAnimationFrame(()=>requestAnimationFrame(()=>{
    BAR_LIST.forEach(({key})=>{
      const pct=pcts[key];
      document.getElementById('br_'+key).style.width=pct+'%';
      document.getElementById('bg_'+key).style.width=(100-pct)+'%';
      animNum(document.getElementById('bp_'+key),pct,1400);
    });
  }));
}

// SWIPE (Screen 11)
let curCard=1, swipeDone=false;
function initSwipe() {
  curCard=1; swipeDone=false;
  ['sc1','sc2','sc3'].forEach((id,i)=>{
    const c=document.getElementById(id);
    c.className='scard'; c.style.opacity='1';
    if(i===0){c.classList.add('active-scard');c.style.zIndex=3;c.style.transform='';}
    else if(i===1){c.style.zIndex=2;c.style.transform='scale(0.96) translateY(10px)';}
    else{c.style.zIndex=1;c.style.transform='scale(0.92) translateY(20px)';}
  });
  document.getElementById('swSummary').style.display='none';
  document.getElementById('swHint').style.display='block';
  document.getElementById('swSub').style.display='block';
  document.getElementById('swDots').style.display='flex';
  updDots(1);
  [1,2,3].forEach(n=>setupCard(n));
}
function updDots(n){ [1,2,3].forEach(i=>{ document.getElementById('d'+i).className='dot'+(i<=n?' on':''); }); }
function advCard(n, dir) {
  if(n!==curCard) return;
  const el=document.getElementById('sc'+n);
  el.classList.add(dir==='l'?'fly-l':'fly-r');
  setTimeout(()=>{
    curCard++;
    if(curCard<=3){
      const nx=document.getElementById('sc'+curCard);
      nx.classList.add('active-scard'); nx.style.zIndex=3; nx.style.transform='';
      if(curCard+1<=3){ const af=document.getElementById('sc'+(curCard+1)); af.style.zIndex=2; af.style.transform='scale(0.96) translateY(10px)'; }
      updDots(curCard);
    } else {
      document.getElementById('swHint').style.display='none';
      document.getElementById('swSub').style.display='none';
      document.getElementById('swDots').style.display='none';
      document.getElementById('swSummary').style.display='block';
    }
  },400);
}
function setupCard(n) {
  const el=document.getElementById('sc'+n);
  let sx=0, dragging=false;
  el.addEventListener('touchstart',e=>{if(n!==curCard)return;sx=e.touches[0].clientX;dragging=true;},{passive:true});
  el.addEventListener('touchmove',e=>{if(!dragging||n!==curCard)return;const dx=e.touches[0].clientX-sx;el.style.transform=`translateX(${dx}px) rotate(${dx*.08}deg)`;},{passive:true});
  el.addEventListener('touchend',e=>{if(!dragging||n!==curCard)return;dragging=false;const dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>80)advCard(n,dx<0?'l':'r');else el.style.transform='';});
  el.addEventListener('mousedown',e=>{if(n!==curCard)return;sx=e.clientX;dragging=true;});
  window.addEventListener('mousemove',e=>{if(!dragging||n!==curCard)return;const dx=e.clientX-sx;el.style.transform=`translateX(${dx}px) rotate(${dx*.08}deg)`;});
  window.addEventListener('mouseup',e=>{if(!dragging||n!==curCard)return;dragging=false;const dx=e.clientX-sx;if(Math.abs(dx)>80)advCard(n,dx<0?'l':'r');else el.style.transform='';});
}

// TOLL (Screen 12)
function buildToll() {
  let g=81,a=74,d=72,m=67;
  if(sel.s7.has('guilt')){g=Math.min(97,g+6);a+=2;}
  if(sel.s7.has('anxiety')){a=Math.min(97,a+6);m+=3;}
  if(sel.s7.has('motivation')){d=Math.min(97,d+5);}
  if(sel.s7.has('depression')){m=Math.min(97,m+7);a+=4;}
  if(sel.s7.has('self_esteem')){g+=5;d+=4;}
  if(sel.s8.has('darkness')){g+=4;m+=3;}
  if(sel.s8.has('imaan')){a+=3;d+=3;}
  if(sel.s8.has('fears')){a=Math.min(97,a+5);m+=4;}
  [['t1',g],['t2',a],['t3',d],['t4',m]].forEach(([id,v])=>{ animNum(document.getElementById(id),Math.min(97,v),1400); });
}

// HOLD (Screen 16)
let hRAF=null, hStart=null, hDone=false;
const Hdur=2200;
function setupHold() {
  hDone=false;
  const pill=document.getElementById('holdPill');
  const lbl=document.getElementById('hLabel');
  const sub=document.getElementById('hSub');
  const bism=document.getElementById('bismLine');
  const zone=document.getElementById('holdZone');
  if(!pill) return;
  pill.style.width='0%'; pill.style.background='#1a9fc0';
  bism.style.maxHeight='0'; bism.style.opacity='0';
  lbl.textContent='Hold'; sub.textContent='to begin'; lbl.style.color='#1a1a2e';

  function start(e) {
    if(hDone) return; e.preventDefault(); hStart=performance.now(); anim();
  }
  function anim() {
    hRAF=requestAnimationFrame(now=>{
      if(!hStart) return;
      const pct=Math.min((now-hStart)/Hdur,1);
      pill.style.width=(pct*100)+'%';
      if(pct>0.35){ bism.style.maxHeight='120px'; bism.style.opacity=Math.min((pct-.35)/.3,1); }
      else { bism.style.maxHeight='0'; bism.style.opacity='0'; }
      if(pct<.5){lbl.textContent='Hold...';sub.textContent='Keep holding';}
      else if(pct<.85){lbl.textContent='Hold...';sub.textContent='Almost there...';}
      else if(pct<1){lbl.textContent='Hold...';sub.textContent='Just a moment...';}
      if(pct<1){anim();}
      else{
        hDone=true; hStart=null;
        pill.style.width='100%'; pill.style.background='#38a169';
        lbl.textContent='✓ Bismillah!'; lbl.style.color='#1a9fc0';
        sub.textContent='جزاک اللہ خیراً';
        bism.style.maxHeight='120px'; bism.style.opacity='1';
        setTimeout(()=>go(17),1800);
      }
    });
  }
  function stop() {
    if(hDone) return;
    if(hRAF) cancelAnimationFrame(hRAF);
    hRAF=null; hStart=null;
    pill.style.width='0%'; bism.style.maxHeight='0'; bism.style.opacity='0';
    lbl.textContent='Hold'; sub.textContent='to begin';
  }
  zone.addEventListener('touchstart',start,{passive:false});
  zone.addEventListener('touchend',stop);
  zone.addEventListener('touchcancel',stop);
  zone.addEventListener('mousedown',start);
  window.addEventListener('mouseup',stop);
}

// CHART (Screen 17)
const TABS={
  mental:{good:[30,34,40,48,55,62,68,73,77,80,83,85,87,88],bad:[60,58,62,54,56,50,53,46,44,48,40,38,35,36],quote:'"Verily, with hardship comes ease."',ref:'(Surah Ash-Sharh 94:6)'},
  spiritual:{good:[20,26,34,43,52,60,66,71,76,80,84,87,89,90],bad:[55,50,54,46,48,42,45,38,36,40,32,30,27,28],quote:'"Surely in the remembrance of Allah do hearts find rest."',ref:"(Surah Ar-Ra'd 13:28)"},
  relations:{good:[35,39,44,50,57,63,68,72,76,79,82,84,86,88],bad:[62,60,63,55,57,51,54,47,45,49,41,39,36,37],quote:'"And hold firmly to the rope of Allah all together."',ref:'(Surah Aal-e-Imran 3:103)'}
};
let fCtx=null, fCanvas=null, activeTab='mental', fRAF=null;

function switchFutureTab(tab){
  activeTab=tab;
  document.querySelectorAll('.future-tab').forEach(t=>t.classList.remove('on'));
  document.getElementById('tab-'+tab).classList.add('on');
  document.getElementById('fQuote').textContent=TABS[tab].quote;
  document.getElementById('fRef').textContent=TABS[tab].ref;
  animChart();
}
function animChart(){
  if(fRAF) cancelAnimationFrame(fRAF);
  const start=performance.now(), dur=1000;
  (function step(now){
    const pct=Math.min((now-start)/dur,1);
    const ease=1-Math.pow(1-pct,3);
    drawChart(ease);
    if(pct<1) fRAF=requestAnimationFrame(step);
  })(performance.now());
}
function drawChart(pct){
  if(!fCtx) return;
  const data=TABS[activeTab], N=data.good.length;
  const W=fCanvas.width, H=fCanvas.height;
  const dpr=window.devicePixelRatio||1;
  const cW=W/dpr, cH=H/dpr;
  const PAD={top:16,bottom:34,left:8,right:8};
  const dW=cW-PAD.left-PAD.right, dH=cH-PAD.top-PAD.bottom;
  fCtx.clearRect(0,0,W,H);
  fCtx.save(); fCtx.scale(dpr,dpr);
  fCtx.setLineDash([5,5]); fCtx.strokeStyle='#e0e0e0'; fCtx.lineWidth=1;
  [.2,.5,.8].forEach(y=>{ const yy=PAD.top+dH*(1-y); fCtx.beginPath(); fCtx.moveTo(PAD.left,yy); fCtx.lineTo(cW-PAD.right,yy); fCtx.stroke(); });
  fCtx.setLineDash([]);
  fCtx.strokeStyle='#ccc'; fCtx.lineWidth=1;
  fCtx.beginPath(); fCtx.moveTo(PAD.left,PAD.top+dH); fCtx.lineTo(cW-PAD.right,PAD.top+dH); fCtx.stroke();
  fCtx.fillStyle='#999'; fCtx.font='11px Nunito,sans-serif'; fCtx.textAlign='center';
  ['Day 0','Day 30','Day 60','Day 90'].forEach((l,i)=>fCtx.fillText(l,PAD.left+(i/3)*dW,cH-4));
  function dLine(vals,color,p){
    const pts=Math.max(2,Math.round(N*p));
    fCtx.beginPath(); fCtx.lineWidth=3; fCtx.strokeStyle=color; fCtx.lineJoin='round'; fCtx.lineCap='round';
    for(let i=0;i<pts;i++){
      const x=PAD.left+(i/(N-1))*dW, y=PAD.top+dH*(1-vals[i]/100);
      i===0?fCtx.moveTo(x,y):fCtx.lineTo(x,y);
    }
    fCtx.stroke();
    if(pts>=1){ const li=pts-1,ex=PAD.left+(li/(N-1))*dW,ey=PAD.top+dH*(1-vals[li]/100); fCtx.beginPath(); fCtx.arc(ex,ey,5,0,Math.PI*2); fCtx.fillStyle=color; fCtx.fill(); }
  }
  dLine(data.bad,'#e53e3e',pct);
  dLine(data.good,'#1a9fc0',pct);
  fCtx.restore();
}
function initChart(){
  fCanvas=document.getElementById('fChart');
  if(!fCanvas) return;
  const dpr=window.devicePixelRatio||1;
  const rect=fCanvas.getBoundingClientRect();
  fCanvas.width=(rect.width||340)*dpr;
  fCanvas.height=200*dpr;
  fCtx=fCanvas.getContext('2d');
  animChart();
}

// ===== PHASE 4 NAVIGATION =====
var p4smap={22:71,23:74,24:77,25:80,26:84,27:87,28:90,29:94,30:97,31:100};

function goToPhase4(screenId) {
  document.getElementById('phase3-wrap').style.display = 'none';
  document.getElementById('phase4-wrap').style.display = 'block';
  p4go(parseInt(screenId.replace('p4s','')));
  if (screenId === 'p4s24') { p4renderJ(); }
}

function p4go(n) {
  document.querySelectorAll('#phase4-wrap .p4screen').forEach(function(s){s.classList.remove('active');});
  var el = document.getElementById('p4s'+n);
  if(el) el.classList.add('active');
  document.getElementById('p4pf').style.width=(p4smap[n]||100)+'%';
  document.getElementById('p4plbl').textContent=n+' of 31';
  if(n===24) { setTimeout(p4renderJ, 100); }
}

function p4goDone(){
  document.querySelectorAll('#phase4-wrap .p4screen').forEach(function(s){s.classList.remove('active');});
  document.getElementById('p4sdone').classList.add('active');
  document.getElementById('p4pf').style.width='100%';
  document.getElementById('p4plbl').textContent='31 of 31';
}

function p4tog(id){document.getElementById(id).classList.toggle('on');}
function p4pickChip(el){document.querySelectorAll('.p4chip').forEach(function(c){c.classList.remove('sel');});el.classList.add('sel');}

// Journey cards
var p4jdata=[
  {svg:'<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',range:'DAYS 1–90',num:'1 / 5',title:'You plant the seed',desc:"The first 90 days are the hardest. You'll struggle, stumble, and rebuild. But every clean day is a seed of faith taking root inside you."},
  {svg:'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',range:'DAYS 91–180',num:'2 / 5',title:'You face the storms',desc:"The middle path is where most people quit. You'll discover that urges fade, cravings weaken, and your soul begins to breathe again."},
  {svg:'<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',range:'DAYS 181–270',num:'3 / 5',title:'Your heart changes',desc:"Something shifts inside you. The person you were shrinks. The person you were made to be — the one Allah intended — starts to emerge."},
  {svg:'<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',range:'DAYS 271–360',num:'4 / 5',title:'You become free',desc:"You're no longer just fighting a habit. You're living your purpose. Clean not because you're trying — but because you've truly changed."},
  {svg:'<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',range:'DAY 360',num:'5 / 5',title:'You arrive',desc:"12 cycles. 360 clean days. Levels, streaks, and XP track your growth — but the real reward is the man you'll have become."}
];
var p4jIdx=0;
function p4renderJ(){
  var c=p4jdata[p4jIdx];
  var svgEl=document.getElementById('p4jc-svg');
  if(!svgEl) return;
  svgEl.innerHTML=c.svg;
  document.getElementById('p4jc-range').textContent=c.range;
  document.getElementById('p4jc-num').textContent=c.num;
  document.getElementById('p4jc-title').textContent=c.title;
  document.getElementById('p4jc-desc').textContent=c.desc;
  var dots=document.getElementById('p4jdots');dots.innerHTML='';
  p4jdata.forEach(function(_,i){
    var d=document.createElement('div');
    d.className='p4jdot'+(i===p4jIdx?' on':'');
    d.style.width=i===p4jIdx?'22px':'10px';
    d.onclick=function(){p4jIdx=i;p4renderJ();};
    dots.appendChild(d);
  });
  document.getElementById('p4jsummary').style.display=p4jIdx===4?'block':'none';
}

var p4sx=null,p4mx=null;
document.addEventListener('DOMContentLoaded',function(){
  var jw=document.getElementById('p4jcard-wrap');
  if(!jw) return;
  jw.addEventListener('touchstart',function(e){p4sx=e.touches[0].clientX;},{passive:true});
  jw.addEventListener('touchend',function(e){
    if(p4sx===null)return;
    var dx=p4sx-e.changedTouches[0].clientX;
    if(Math.abs(dx)>35){if(dx>0&&p4jIdx<4){p4jIdx++;p4renderJ();}else if(dx<0&&p4jIdx>0){p4jIdx--;p4renderJ();}}
    p4sx=null;
  });
  jw.addEventListener('mousedown',function(e){p4mx=e.clientX;});
  window.addEventListener('mouseup',function(e){
    if(p4mx===null)return;
    var dx=p4mx-e.clientX;
    if(Math.abs(dx)>35){if(dx>0&&p4jIdx<4){p4jIdx++;p4renderJ();}else if(dx<0&&p4jIdx>0){p4jIdx--;p4renderJ();}}
    p4mx=null;
  });
});

// Calendar
var P4_DAYS_N=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
var P4_MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];
var P4_DAYS_FULL=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
var p4selDate=new Date(2026,4,30),p4tempDate=new Date(2026,4,30),p4calYear=2026,p4calMonth=4;
function p4fmtDate(d){return P4_DAYS_FULL[d.getDay()]+', '+P4_MONTHS[d.getMonth()]+' '+d.getDate()+', '+d.getFullYear();}
function p4openCal(){p4tempDate=new Date(p4selDate);p4calYear=p4selDate.getFullYear();p4calMonth=p4selDate.getMonth();p4renderCal();document.getElementById('p4cal-overlay').style.display='flex';}
function p4closeCal(){document.getElementById('p4cal-overlay').style.display='none';}
function p4confirmDate(){p4selDate=new Date(p4tempDate);document.getElementById('p4quit-lbl').textContent=p4fmtDate(p4selDate);var fd=new Date(p4selDate);fd.setDate(fd.getDate()+90);document.getElementById('p4free-date-lbl').textContent=p4fmtDate(fd);p4closeCal();}
function p4calPrevMonth(){p4calMonth--;if(p4calMonth<0){p4calMonth=11;p4calYear--;}p4renderCal();}
function p4calNextMonth(){p4calMonth++;if(p4calMonth>11){p4calMonth=0;p4calYear++;}p4renderCal();}
function p4renderCal(){
  document.getElementById('p4cal-month-lbl').textContent=P4_MONTHS[p4calMonth]+' '+p4calYear;
  var grid=document.getElementById('p4cal-grid');grid.innerHTML='';
  P4_DAYS_N.forEach(function(d){var el=document.createElement('div');el.className='p4cal-day-name';el.textContent=d;grid.appendChild(el);});
  var first=new Date(p4calYear,p4calMonth,1).getDay(),dim=new Date(p4calYear,p4calMonth+1,0).getDate(),today=new Date();today.setHours(0,0,0,0);
  for(var i=0;i<first;i++){var prev=new Date(p4calYear,p4calMonth,0-first+i+1);var el=document.createElement('div');el.className='p4cal-day other-month';el.textContent=prev.getDate();grid.appendChild(el);}
  for(var d=1;d<=dim;d++){
    var el=document.createElement('div'),thisD=new Date(p4calYear,p4calMonth,d),cls='p4cal-day';
    if(thisD<today)cls+=' past';
    if(thisD.toDateString()===today.toDateString())cls+=' today';
    if(thisD.toDateString()===p4tempDate.toDateString())cls+=' selected';
    el.className=cls;el.textContent=d;
    (function(dd,td){el.onclick=function(){if(td<today)return;p4tempDate=new Date(p4calYear,p4calMonth,dd);p4renderCal();};})(d,thisD);
    grid.appendChild(el);
  }
}

// Time Picker
var p4tpHour=8,p4tpMin=0,p4tpAmPm='PM';
function p4openTimePicker(){document.getElementById('p4time-overlay').style.display='flex';p4renderTP();}
function p4closeTimePicker(){document.getElementById('p4time-overlay').style.display='none';}
function p4renderTP(){
  document.getElementById('p4tp-hour').textContent=String(p4tpHour).padStart(2,'0');
  document.getElementById('p4tp-min').textContent=String(p4tpMin).padStart(2,'0');
  var am=document.getElementById('p4tp-am'),pm=document.getElementById('p4tp-pm');
  if(p4tpAmPm==='AM'){am.style.borderColor='#0EA5C9';am.style.background='#E0F7FA';am.style.color='#0EA5C9';pm.style.borderColor='#E5E7EB';pm.style.background='white';pm.style.color='#374151';}
  else{pm.style.borderColor='#0EA5C9';pm.style.background='#E0F7FA';pm.style.color='#0EA5C9';am.style.borderColor='#E5E7EB';am.style.background='white';am.style.color='#374151';}
}
function p4changeHour(d){p4tpHour=(p4tpHour-1+d+12)%12+1;p4renderTP();}
function p4changeMin(d){p4tpMin=(p4tpMin+d*5+60)%60;p4renderTP();}
function p4setAmPm(v){p4tpAmPm=v;p4renderTP();}
function p4confirmTime(){var display=String(p4tpHour).padStart(2,'0')+':'+String(p4tpMin).padStart(2,'0')+' '+p4tpAmPm;document.getElementById('p4time-display').textContent=display;p4closeTimePicker();}

// Notifications
var p4notifGranted=false;
function p4enableNotifications(){
  if(!('Notification' in window)){alert('Browser notifications not supported.');return;}
  Notification.requestPermission().then(function(perm){
    if(perm==='granted'){
      p4notifGranted=true;
      document.getElementById('p4notif-btn').textContent='✓ Notifications Enabled';
      document.getElementById('p4notif-btn').style.background='linear-gradient(90deg,#16A34A,#22C55E)';
      setTimeout(function(){p4goDone();},800);
    } else {
      alert('Notifications not allowed. Please enable in browser settings.');
    }
  });
}"""
