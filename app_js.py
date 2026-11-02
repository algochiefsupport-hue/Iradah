# -*- coding: utf-8 -*-

APP_JS = """
// ============================================================
// ===  PURIFY UNIFIED MOBILE APP - MASTER JAVASCRIPT       ===
// ============================================================

// --- Helper Functions ---
function pad2(n) { return String(Math.floor(n)).padStart(2, '0'); }
function formatDateKey(d) { return d.getFullYear() + '-' + pad2(d.getMonth() + 1) + '-' + pad2(d.getDate()); }
function todayDateKey() { return formatDateKey(new Date()); }

// --- App State ---
var AppState = {
  user: {
    email: '',
    name: '',
    avatar: '👤',
    joinedDate: new Date().toISOString(),
    isLoggedIn: false
  },
  cloudSync: {
    provider: 'firebase',
    firebaseConfig: null,
    lastSynced: null,
    status: 'ready'
  },
  onboardingDone: false, // Triggers assessment for new account
  assessment: {
    answers: [],
    mentalScore: 57,
    spiritualScore: 64,
    relationalScore: 50,
    completedDate: null
  },
  streak: {
    startDate: null,
    lives: 3
  },
  dayLogs: {}, // 'YYYY-MM-DD': 'clean' | 'relapse'
  relapseHistory: [],
  niyah: { text: '', date: '' },
  dailyProgram: {
    currentDay: 1,
    dayProgress: {} // [day]: { morningDone, eveningDone, ibnDone, bfDone, drDone, ibnRefl, bfRefl, mChecked, eChecked }
  },
  settings: {
    notifications: false,
    sound: true
  },
  xp: 0,
  level: 1,
  lastSaved: null
};

// ============================================================
// ===  GOOGLE FIREBASE & AUTOMATIC BACKGROUND SYNC          ===
// ============================================================
const FIREBASE_CONFIG = {
  apiKey: "AIzaSyCrsSTwej3lcGcXToq-zyYn6xicLYLc9oI",
  authDomain: "purify-app-b5f8b.firebaseapp.com",
  projectId: "purify-app-b5f8b",
  storageBucket: "purify-app-b5f8b.firebasestorage.app",
  messagingSenderId: "443583155361",
  appId: "1:443583155361:web:b0b63acee8430e3220f4e0",
  measurementId: "G-G4TQMV4JT2"
};

var firebaseDb = null;
var isFirebaseReady = false;

function initFirebase() {
  try {
    if (typeof firebase !== 'undefined' && FIREBASE_CONFIG.apiKey) {
      if (!firebase.apps || firebase.apps.length === 0) {
        firebase.initializeApp(FIREBASE_CONFIG);
      }
      firebaseDb = firebase.firestore();

      // Enable offline persistence so data is always saved locally and synced automatically when online
      try {
        firebaseDb.enablePersistence({ synchronizeTabs: true }).catch(function(err) {
          console.log('Firestore persistence info:', err.code);
        });
      } catch(ex) {}

      isFirebaseReady = true;
      console.log('Connected to Google Firebase Cloud (purify-app-b5f8b) 🟢');
    }
  } catch(e) {
    console.warn('Firebase init notice:', e);
  }

  // Automatic online/offline network listeners
  window.addEventListener('online', function() {
    console.log('Internet connected: auto-syncing with Google Firebase...');
    if (AppState.user.isLoggedIn && AppState.user.email) {
      saveToCloudDatabase(AppState.user.email, AppState);
    }
    updateSyncIndicator(true);
  });

  window.addEventListener('offline', function() {
    console.log('Device offline: saving to local storage.');
    updateSyncIndicator(false);
  });
}

function sanitizeEmailForDoc(email) {
  return email.toLowerCase().trim().replace(/[^a-z0-9]/g, '_');
}

function saveToCloudDatabase(email, state) {
  if (!email) return;
  var docKey = sanitizeEmailForDoc(email);
  var payload = JSON.parse(JSON.stringify(state));
  payload.lastSaved = new Date().toISOString();

  // 1. Save to Google Firebase Firestore automatically
  if (isFirebaseReady && firebaseDb) {
    firebaseDb.collection('users').doc(docKey).set(payload, { merge: true })
      .then(function() {
        AppState.cloudSync.lastSynced = new Date().toISOString();
        updateSyncIndicator(true);
      })
      .catch(function(err) {
        console.log('Firestore auto-sync cached locally (will upload when online):', err.message);
      });
  }

  // 2. Also keep secondary local backup
  try {
    localStorage.setItem('purify_cloud_' + docKey, JSON.stringify(payload));
  } catch(e) {}
}

function loadFromCloudDatabase(email, callback) {
  if (!email) return;
  var docKey = sanitizeEmailForDoc(email);
  var called = false;
  function done(data, found) {
    if (!called) {
      called = true;
      callback(data, found);
    }
  }

  // Fast local check first
  var cached = null;
  try { cached = localStorage.getItem('purify_cloud_' + docKey); } catch(e){}

  // Safety timer so network or offline lag never blocks the user
  var timer = setTimeout(function() {
    if (cached) done(JSON.parse(cached), true);
    else if (AppState.user && AppState.user.email && AppState.user.email.toLowerCase() === email.toLowerCase()) {
      done(JSON.parse(JSON.stringify(AppState)), true);
    } else {
      done(null, false);
    }
  }, 1000);

  // If online, fetch latest from Firestore
  if (isFirebaseReady && firebaseDb && navigator.onLine) {
    firebaseDb.collection('users').doc(docKey).get()
      .then(function(doc) {
        clearTimeout(timer);
        if (doc.exists) {
          done(doc.data(), true);
        } else if (cached) {
          done(JSON.parse(cached), true);
        } else if (AppState.user && AppState.user.email && AppState.user.email.toLowerCase() === email.toLowerCase()) {
          done(JSON.parse(JSON.stringify(AppState)), true);
        } else {
          done(null, false);
        }
      })
      .catch(function(err) {
        clearTimeout(timer);
        if (cached) done(JSON.parse(cached), true);
        else if (AppState.user && AppState.user.email && AppState.user.email.toLowerCase() === email.toLowerCase()) {
          done(JSON.parse(JSON.stringify(AppState)), true);
        } else {
          done(null, false);
        }
      });
  } else {
    clearTimeout(timer);
    if (cached) done(JSON.parse(cached), true);
    else if (AppState.user && AppState.user.email && AppState.user.email.toLowerCase() === email.toLowerCase()) {
      done(JSON.parse(JSON.stringify(AppState)), true);
    } else {
      done(null, false);
    }
  }
}

// ============================================================
// ===  STORAGE & AUTO-SAVE ENGINE                           ===
// ============================================================
var autoSaveTimer = null;
function debouncedSave() {
  if (autoSaveTimer) clearTimeout(autoSaveTimer);
  autoSaveTimer = setTimeout(function() {
    saveAppState(false);
  }, 400);
}

function saveAppState(showToastAlert) {
  try {
    AppState.lastSaved = new Date().toISOString();
    localStorage.setItem('purify_app_state_v2', JSON.stringify(AppState));
    updateSyncIndicator(true);

    // Auto-save to cloud if user is logged in
    if (AppState.user.isLoggedIn && AppState.user.email) {
      saveToCloudDatabase(AppState.user.email, AppState);
    }

    if (showToastAlert) showToast('Progress auto-saved ✓');
  } catch(e) {
    console.error('Save failed:', e);
  }
}

function loadAppState() {
  try {
    var raw = localStorage.getItem('purify_app_state_v2');
    if (raw) {
      var parsed = JSON.parse(raw);
      if (parsed) {
        AppState = Object.assign(AppState, parsed);
        if (typeof AppState.xp !== 'number') AppState.xp = 0;
        if (typeof AppState.level !== 'number') AppState.level = Math.floor(AppState.xp / 100) + 1;
        if (!AppState.streak) AppState.streak = { startDate: null, lives: 3 };
        if (AppState.streak.lives === undefined) AppState.streak.lives = 3;
      }
    } else {
      // Migrate from old HOME rstate if available
      var oldRstate = localStorage.getItem('rstate');
      if (oldRstate) {
        try {
          var s = JSON.parse(oldRstate);
          if (s.dl) AppState.dayLogs = s.dl;
          if (s.lv !== undefined) AppState.streak.lives = s.lv;
        } catch(err) {}
      }
    }
  } catch(e) {
    console.error('Load failed:', e);
  }

  ensureDayProgress(AppState.dailyProgram.currentDay);
}

function ensureDayProgress(d) {
  if (!AppState.dailyProgram.dayProgress) AppState.dailyProgram.dayProgress = {};
  if (!AppState.dailyProgram.dayProgress[d]) {
    AppState.dailyProgram.dayProgress[d] = {
      morningDone: false,
      eveningDone: false,
      ibnDone: false,
      bfDone: false,
      drDone: false,
      ibnRefl: '',
      bfRefl: '',
      mChecked: (typeof MORNING_DUAS !== 'undefined') ? new Array(MORNING_DUAS.length).fill(false) : [],
      eChecked: (typeof EVENING_DUAS !== 'undefined') ? new Array(EVENING_DUAS.length).fill(false) : []
    };
  }
}

function updateSyncIndicator(saved) {
  var dot = document.getElementById('headerSyncDot');
  var userTxt = document.getElementById('headerUserText');
  var setTxt = document.getElementById('settingsSyncText');
  var setEmail = document.getElementById('settingsUserEmail');

  if (AppState.user.isLoggedIn && AppState.user.email) {
    if (userTxt) userTxt.textContent = AppState.user.name || AppState.user.email.split('@')[0];
    if (setEmail) setEmail.textContent = AppState.user.email;
    if (setTxt) setTxt.textContent = navigator.onLine ? 'Backup & Sync Active' : 'Offline — will sync when connected';
    if (dot) dot.style.background = navigator.onLine ? '#10b981' : '#f59e0b';
  } else {
    if (userTxt) userTxt.textContent = 'Sign In';
    if (setEmail) setEmail.textContent = 'Guest User';
    if (setTxt) setTxt.textContent = 'Sign in to enable cross-device restore';
    if (dot) dot.style.background = '#94a3b8';
  }
}

// ============================================================
// ===  XP & LEVEL SYSTEM                                   ===
// ============================================================
function addXP(amount) {
  if (typeof AppState.xp !== 'number') AppState.xp = 0;
  var oldLevel = Math.floor(AppState.xp / 100) + 1;
  AppState.xp += amount;
  var newLevel = Math.floor(AppState.xp / 100) + 1;
  AppState.level = newLevel;
  if (newLevel > oldLevel) {
    showToast('Level Up! You reached Level ' + newLevel + ' 🌟');
  }
  updateXPDisplay();
  saveAppState(false);
}

function updateXPDisplay() {
  var xpEl = document.getElementById('headerXp');
  var lvEl = document.getElementById('headerLv');
  if (typeof AppState.xp !== 'number') AppState.xp = 0;
  AppState.level = Math.floor(AppState.xp / 100) + 1;
  if (xpEl) xpEl.textContent = AppState.xp;
  if (lvEl) lvEl.textContent = AppState.level;
}

// ============================================================
// ===  SECURE EMAIL + PASSWORD AUTH & CLOUD RESTORE        ===
// ============================================================
var currentAuthMode = 'login'; // 'login', 'register', or 'forgot'
var forgotAccountData = null;
var forgotAccountEmail = '';

function switchAuthTab(mode) {
  currentAuthMode = mode;
  var tabGroup = document.getElementById('authTabGroup');
  var tabLogin = document.getElementById('authTabLogin');
  var tabReg = document.getElementById('authTabRegister');
  var nameGroup = document.getElementById('authNameGroup');
  var secGroup = document.getElementById('authSecurityGroup');
  var mainForm = document.getElementById('authMainForm');
  var forgotForm = document.getElementById('authForgotForm');
  var title = document.getElementById('authModalTitle');
  var desc = document.getElementById('authModalDesc');
  var btn = document.getElementById('authSubmitBtn');
  var forgotLink = document.getElementById('authForgotLinkRow');

  if (mode === 'login') {
    if (tabGroup) tabGroup.style.display = 'flex';
    if (mainForm) mainForm.style.display = 'block';
    if (forgotForm) forgotForm.style.display = 'none';
    if (tabLogin) { tabLogin.style.background = '#fff'; tabLogin.style.color = '#1a5fa8'; }
    if (tabReg) { tabReg.style.background = 'transparent'; tabReg.style.color = '#64748b'; }
    if (nameGroup) nameGroup.style.display = 'none';
    if (secGroup) secGroup.style.display = 'none';
    if (forgotLink) forgotLink.style.display = 'flex';
    if (title) title.textContent = 'Sign In to Account';
    if (desc) desc.textContent = 'Enter your email & secure PIN to restore your progress.';
    if (btn) btn.textContent = 'Sign In';
  } else if (mode === 'register') {
    if (tabGroup) tabGroup.style.display = 'flex';
    if (mainForm) mainForm.style.display = 'block';
    if (forgotForm) forgotForm.style.display = 'none';
    if (tabLogin) { tabLogin.style.background = 'transparent'; tabLogin.style.color = '#64748b'; }
    if (tabReg) { tabReg.style.background = '#fff'; tabReg.style.color = '#1a5fa8'; }
    if (nameGroup) nameGroup.style.display = 'block';
    if (secGroup) secGroup.style.display = 'block';
    if (forgotLink) forgotLink.style.display = 'none';
    if (title) title.textContent = 'Create New Account';
    if (desc) desc.textContent = 'Set up your account & recovery question to back up your journey.';
    if (btn) btn.textContent = 'Create Account';
  } else if (mode === 'forgot') {
    if (tabGroup) tabGroup.style.display = 'none';
    if (mainForm) mainForm.style.display = 'none';
    if (forgotForm) forgotForm.style.display = 'block';
    if (title) title.textContent = 'Reset Password';
    if (desc) desc.textContent = 'OTP will be sent directly to your registered email.';
    // Reset OTP form to Step 1
    var st1 = document.getElementById('otpStep1');
    var st2 = document.getElementById('otpStep2');
    var st3 = document.getElementById('otpStep3');
    var backRow = document.getElementById('otpBackRow');
    if (st1) st1.style.display = 'block';
    if (st2) st2.style.display = 'none';
    if (st3) st3.style.display = 'none';
    if (backRow) backRow.style.display = 'block';
    var emailInpF = document.getElementById('authForgotEmailInput');
    if (emailInpF) emailInpF.value = '';
    var otpInpF = document.getElementById('authForgotOtpInput');
    if (otpInpF) otpInpF.value = '';
    var newPwdF = document.getElementById('authForgotNewPwd');
    if (newPwdF) newPwdF.value = '';
    var sendErr = document.getElementById('otpSendError');
    if (sendErr) sendErr.style.display = 'none';
    var verErr = document.getElementById('otpVerifyError');
    if (verErr) verErr.style.display = 'none';
    // Reset OTP state
    _otpCode = ''; _otpExpiry = 0; _otpEmail = '';
  }
}

function openAuthModal() {
  var emailInp = document.getElementById('authEmailInput');
  var nameInp = document.getElementById('authNameInput');
  var pwdInp = document.getElementById('authPasswordInput');
  if (emailInp) emailInp.value = AppState.user.email || '';
  if (nameInp) nameInp.value = AppState.user.name || '';
  if (pwdInp) pwdInp.value = '';
  switchAuthTab('login');
  openModal('authModal');
}

// Simple deterministic hash for password & answer check
function hashSecret(str) {
  var hash = 0;
  for (var i = 0; i < str.length; i++) {
    var char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash |= 0;
  }
  return 'p_' + Math.abs(hash).toString(36);
}

function submitEmailAuth() {
  var email = document.getElementById('authEmailInput').value.trim();
  var password = document.getElementById('authPasswordInput').value.trim();
  var name = document.getElementById('authNameInput').value.trim();

  if (!email || !email.includes('@')) {
    alert('Please enter a valid email address.');
    return;
  }
  if (!password || password.length < 4) {
    alert('Please enter a password/PIN of at least 4 characters for account security.');
    return;
  }

  var hashedPwd = hashSecret(password);
  showToast('Connecting...');

  loadFromCloudDatabase(email, function(existingCloudData, found) {
    if (currentAuthMode === 'login') {
      if (!found || !existingCloudData) {
        alert('No account found with this email. Please click "New Account" tab to register.');
        switchAuthTab('register');
        return;
      }
      // Check password if account has one set
      if (existingCloudData.authHash && existingCloudData.authHash !== hashedPwd) {
        alert('Incorrect password for this account. If you forgot your password, click "Forgot Password / PIN?".');
        return;
      }

      // RESTORE EXISTING USER PROGRESS ON NEW PHONE!
      AppState = Object.assign(AppState, existingCloudData);
      AppState.user.isLoggedIn = true;
      if (AppState.onboardingDone === undefined) {
        AppState.onboardingDone = true;
      }
      saveAppState(false);
      renderAll();
      closeModal('authModal');
      checkOnboardingOrMainApp();
      showToast('Welcome back! Journey restored ☁️');
    } else {
      // REGISTER MODE
      if (found && existingCloudData && existingCloudData.authHash) {
        alert('An account already exists with this email. Please click "Sign In".');
        switchAuthTab('login');
        return;
      }

      var secQ = document.getElementById('authSecurityQuestion').value;
      var secA = document.getElementById('authSecurityAnswer').value.trim();
      if (!secA || secA.length < 2) {
        alert('Please answer the security question (required if you ever forget your password).');
        return;
      }

      AppState.user.email = email;
      AppState.user.name = name || email.split('@')[0];
      AppState.user.isLoggedIn = true;
      AppState.authHash = hashedPwd;
      AppState.securityQuestion = secQ;
      AppState.securityAnswerHash = hashSecret(secA.toLowerCase());

      // Assign anonymous community handle
      if (!AppState.communityAlias) {
        var randomNum = Math.floor(100 + Math.random() * 900);
        var titles = ['Mujahid', 'Salik', 'Sabir', 'Muhsin', 'Seeker', 'Servant'];
        AppState.communityAlias = titles[Math.floor(Math.random() * titles.length)] + ' #' + randomNum;
      }

      AppState.onboardingDone = false; // Fresh onboarding questions for new account!
      saveAppState(false);
      saveToCloudDatabase(email, AppState);
      closeModal('authModal');
      renderAll();
      showToast('Account created! Let us calibrate your baseline.');

      // Launch full 31-step onboarding journey for new account!
      setTimeout(function() {
        openFullOnboardingJourney();
      }, 300);
    }
    updateSyncIndicator(true);
  });
}

// ============================================================
// ===  SECURE ACCOUNT RECOVERY (SECURITY QUESTION & EMAIL)  ===
// ============================================================
var SEC_QUESTIONS = {
  'school': 'What was the name of your first school?',
  'nickname': 'What was your childhood nickname?',
  'book': 'What is your favorite Islamic book?',
  'mother': "What is your mother's first name?"
};

// ============================================================
// === EMAIL OTP PASSWORD RECOVERY (via EmailJS - Secure) ===
// ============================================================
// SETUP INSTRUCTIONS:
//   1. Go to https://emailjs.com and create a FREE account
//   2. Add Email Service: Gmail → Service ID = "service_iradah"
//   3. Create Email Template with these variables:
//      Subject: Your Iradah OTP Code: {{otp_code}}
//      Body:
//        Assalamu Alaikum {{user_name}},
//        Your Iradah password reset OTP is: {{otp_code}}
//        Valid for 10 minutes. Do NOT share this code.
//      Template ID = "template_iradah_otp"
//   4. Copy your Public Key from Account > API Keys
//      Replace YOUR_EMAILJS_PUBLIC_KEY below
// ============================================================

var EMAILJS_SERVICE_ID   = 'service_iradah';      // Your EmailJS Service ID
var EMAILJS_TEMPLATE_ID  = 'template_iradah_otp'; // Your EmailJS Template ID
var EMAILJS_PUBLIC_KEY   = 'YOUR_EMAILJS_PUBLIC_KEY'; // Your EmailJS Public Key

var _otpCode     = '';     // Current OTP (6-digit)
var _otpExpiry   = 0;      // Timestamp when OTP expires
var _otpEmail    = '';     // Email OTP was sent to

function _generateOTP() {
  return String(Math.floor(100000 + Math.random() * 900000));
}

function sendEmailOTP() {
  var email = (document.getElementById('authForgotEmailInput') || {}).value;
  if (!email) email = '';
  email = email.trim().toLowerCase();
  var errEl = document.getElementById('otpSendError');
  if (errEl) errEl.style.display = 'none';

  if (!email || !email.includes('@')) {
    if (errEl) { errEl.textContent = 'Please enter a valid email address.'; errEl.style.display = 'block'; }
    return;
  }

  // Check if email is registered in Firebase
  showToast('Verifying account...');
  var btn = document.getElementById('btnSendOtp');
  if (btn) { btn.disabled = true; btn.textContent = 'Sending...'; }

  loadFromCloudDatabase(email, function(data) {
    if (!data || !data.user || !data.user.email) {
      if (btn) { btn.disabled = false; btn.innerHTML = '<i class="ti ti-send"></i> Send OTP to My Email'; }
      if (errEl) { errEl.textContent = 'No account found with this email. Please check your email or create a new account.'; errEl.style.display = 'block'; }
      return;
    }

    // Account found - generate OTP and send via EmailJS
    _otpCode   = _generateOTP();
    _otpExpiry = Date.now() + (10 * 60 * 1000); // 10 minutes
    _otpEmail  = email;

    // Initialize EmailJS
    if (typeof emailjs === 'undefined') {
      if (btn) { btn.disabled = false; btn.innerHTML = '<i class="ti ti-send"></i> Send OTP to My Email'; }
      if (errEl) { errEl.textContent = 'Email service not loaded. Please check your internet connection and try again.'; errEl.style.display = 'block'; }
      return;
    }

    emailjs.init(EMAILJS_PUBLIC_KEY);

    var templateParams = {
      to_email:  email,
      user_name: (data.user && data.user.name) ? data.user.name : 'User',
      otp_code:  _otpCode,
      app_name:  'Iradah'
    };

    emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, templateParams)
      .then(function(response) {
        if (btn) { btn.disabled = false; btn.innerHTML = '<i class="ti ti-send"></i> Send OTP to My Email'; }
        // Show step 2
        var step1 = document.getElementById('otpStep1');
        var step2 = document.getElementById('otpStep2');
        var sentMsg = document.getElementById('otpSentToMsg');
        if (step1) step1.style.display = 'none';
        if (step2) step2.style.display = 'block';
        if (sentMsg) sentMsg.textContent = 'OTP sent to: ' + email + ' (check Spam folder too)';
        showToast('OTP sent to your email!');
      }, function(error) {
        if (btn) { btn.disabled = false; btn.innerHTML = '<i class="ti ti-send"></i> Send OTP to My Email'; }
        if (errEl) {
          if (EMAILJS_PUBLIC_KEY === 'YOUR_EMAILJS_PUBLIC_KEY') {
            errEl.textContent = 'EmailJS not configured yet. Please follow setup instructions in the app code.';
          } else {
            errEl.textContent = 'Failed to send OTP: ' + (error.text || 'Please check internet connection.');
          }
          errEl.style.display = 'block';
        }
        console.error('EmailJS error:', error);
      });
  });
}

function verifyEmailOTP() {
  var enteredOtp = ((document.getElementById('authForgotOtpInput') || {}).value || '').trim();
  var newPwd     = ((document.getElementById('authForgotNewPwd') || {}).value || '').trim();
  var errEl      = document.getElementById('otpVerifyError');
  if (errEl) errEl.style.display = 'none';

  if (!enteredOtp || enteredOtp.length !== 6) {
    if (errEl) { errEl.textContent = 'Please enter the 6-digit OTP code.'; errEl.style.display = 'block'; }
    return;
  }
  if (!newPwd || newPwd.length < 4) {
    if (errEl) { errEl.textContent = 'New password must be at least 4 characters.'; errEl.style.display = 'block'; }
    return;
  }
  if (Date.now() > _otpExpiry) {
    if (errEl) { errEl.textContent = 'OTP has expired. Please request a new one.'; errEl.style.display = 'block'; }
    // Go back to step 1
    var step1 = document.getElementById('otpStep1');
    var step2 = document.getElementById('otpStep2');
    if (step1) step1.style.display = 'block';
    if (step2) step2.style.display = 'none';
    return;
  }
  if (enteredOtp !== _otpCode) {
    if (errEl) { errEl.textContent = 'Incorrect OTP. Please try again.'; errEl.style.display = 'block'; }
    return;
  }

  // OTP correct! Reset password in Firebase
  showToast('Verifying...');
  loadFromCloudDatabase(_otpEmail, function(data) {
    if (!data) {
      if (errEl) { errEl.textContent = 'Account not found. Please try again.'; errEl.style.display = 'block'; }
      return;
    }
    // Hash new password same way as registration
    var newHash = simpleHash(newPwd);
    // Update in Firebase
    var db = (typeof firebase !== 'undefined' && firebase.apps && firebase.apps.length > 0)
      ? firebase.firestore() : null;
    if (db) {
      var safeEmail = _otpEmail.replace(/[.#$[\]]/g, '_');
      db.collection('iradah_users').doc(safeEmail).update({
        authHash: newHash
      }).then(function() {
        // OTP used - clear it
        _otpCode = '';
        _otpExpiry = 0;
        // Show success step
        var step2 = document.getElementById('otpStep2');
        var step3 = document.getElementById('otpStep3');
        var backRow = document.getElementById('otpBackRow');
        if (step2) step2.style.display = 'none';
        if (step3) step3.style.display = 'block';
        if (backRow) backRow.style.display = 'none';
        showToast('Password reset successfully!');
      }).catch(function(e) {
        if (errEl) { errEl.textContent = 'Error saving new password. Please try again.'; errEl.style.display = 'block'; }
        console.error('Reset error:', e);
      });
    } else {
      // Local fallback (offline mode)
      AppState.authHash = simpleHash(newPwd);
      _otpCode = '';
      _otpExpiry = 0;
      var step2 = document.getElementById('otpStep2');
      var step3 = document.getElementById('otpStep3');
      var backRow = document.getElementById('otpBackRow');
      if (step2) step2.style.display = 'none';
      if (step3) step3.style.display = 'block';
      if (backRow) backRow.style.display = 'none';
      showToast('Password reset successfully!');
    }
  });
}

function resendOTP() {
  var step1 = document.getElementById('otpStep1');
  var step2 = document.getElementById('otpStep2');
  if (step1) step1.style.display = 'block';
  if (step2) step2.style.display = 'none';
  _otpCode = '';
  _otpExpiry = 0;
}

function continueAsGuest() {
  closeModal('authModal');
  showToast('Continuing as guest');
  checkOnboardingOrMainApp();
}

// ============================================================
// ===  NOTIFICATION & 100% DAILY ALERT ENGINE               ===
// ============================================================
var scheduledAlertTimer = null;

function initNotifications() {
  var badge = document.getElementById('settingsNotifBadge');
  var statusText = document.getElementById('settingsNotifStatus');
  var bell = document.getElementById('headerNotifBell');

  if (!("Notification" in window)) {
    if (statusText) statusText.textContent = "Notifications not supported in this browser";
    return;
  }

  if (Notification.permission === "granted") {
    AppState.settings.notifications = true;
    if (badge) { badge.textContent = "100% Active"; badge.style.background = "#dcfce7"; badge.style.color = "#166534"; }
    if (statusText) statusText.textContent = "Alerts 100% Enabled (Fajr, Zohar, Maghrib & Night Muhasaba)";
    if (bell) bell.classList.add('active');
    startScheduledAlerts();
  } else {
    AppState.settings.notifications = false;
    if (badge) { badge.textContent = "Disabled"; badge.style.background = "#fee2e2"; badge.style.color = "#991b1b"; }
    if (statusText) statusText.textContent = "Tap here to enable 100% alerts on your mobile";
    if (bell) bell.classList.remove('active');
  }
}

function toggleNotificationPermission() {
  if (!("Notification" in window)) {
    alert("This device browser does not support Web Notifications.");
    return;
  }

  if (Notification.permission === "granted") {
    sendTestNotification();
    showToast("Notifications are active 🔔");
    return;
  }

  Notification.requestPermission().then(function(permission) {
    if (permission === "granted") {
      AppState.settings.notifications = true;
      saveAppState(false);
      initNotifications();
      sendNotification("Daily Reminders Active", "You will receive morning, evening, and daily reflection reminders.");
      showToast("Notifications enabled 🔔");
    } else {
      alert("Notification permission denied. You can enable them anytime in your browser settings.");
    }
  });
}

function sendNotification(title, body) {
  try {
    if (navigator.serviceWorker && navigator.serviceWorker.controller) {
      navigator.serviceWorker.ready.then(function(reg) {
        reg.showNotification(title, {
          body: body,
          icon: 'manifest.json',
          badge: 'manifest.json',
          vibrate: [200, 100, 200]
        });
      });
    } else if ("Notification" in window && Notification.permission === "granted") {
      new Notification(title, { body: body });
    }
  } catch(e) {
    console.warn('Notification error:', e);
  }
}

function sendTestNotification() {
  if (Notification.permission !== "granted") {
    toggleNotificationPermission();
    return;
  }
  sendNotification("Purify Reminder", "Your daily reminder system is active and working properly.");
  showToast("Test notification sent 📲");
}

function startScheduledAlerts() {
  if (scheduledAlertTimer) clearInterval(scheduledAlertTimer);
  scheduledAlertTimer = setInterval(checkDailyNotificationTimes, 60000);
}

function checkDailyNotificationTimes() {
  var now = new Date();
  var hours = now.getHours();
  var mins = now.getMinutes();

  if (mins === 0) {
    if (hours === 6) {
      sendNotification("Morning Adhkar • Al-Wazifatul Kareemah", "Begin your morning with authentic remembrance and renew your daily intention.");
    } else if (hours === 14) {
      sendNotification("Mindful Pause • Guarding the Gaze", "Protecting your gaze brings tranquility and peace of heart.");
    } else if (hours === 18) {
      sendNotification("Evening Adhkar • Al-Wazifatul Kareemah", "Shield your heart with evening supplications before nightfall.");
    } else if (hours === 22) {
      sendNotification("Night Reflection • Muhasaba", "Take a quiet moment to reflect on your day and log your clean streak.");
    }
  }
}

// ============================================================
// ===  BACKUP & RESTORE (.json)                             ===
// ============================================================
function exportBackupData() {
  saveAppState(false);
  var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(AppState, null, 2));
  var downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", "purify_backup_" + todayDateKey() + ".json");
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
  showToast('Backup downloaded successfully 📥');
}

function importBackupData(event) {
  var file = event.target.files[0];
  if (!file) return;
  var reader = new FileReader();
  reader.onload = function(e) {
    try {
      var imported = JSON.parse(e.target.result);
      if (imported && (imported.dayLogs || imported.dailyProgram)) {
        AppState = Object.assign(AppState, imported);
        saveAppState(false);
        renderAll();
        showToast('Backup restored successfully! 🎉');
      } else {
        alert('Invalid backup file format.');
      }
    } catch(err) {
      alert('Could not parse backup file.');
    }
  };
  reader.readAsText(file);
}

// ============================================================
// ===  NAVIGATION & TAB SWITCHING                           ===
// ============================================================
var currentTab = 'home';
function switchTab(tabId) {
  currentTab = tabId;
  document.querySelectorAll('.tab-screen').forEach(function(s) { s.classList.remove('active'); });
  document.querySelectorAll('.bnav-item').forEach(function(b) { b.classList.remove('active'); });

  var screenEl = document.getElementById('tab-' + tabId);
  var navEl = document.getElementById('bnav-' + tabId);
  if (screenEl) screenEl.classList.add('active');
  if (navEl) navEl.classList.add('active');

  if (tabId === 'home') {
    renderWeek();
    renderHomeTree();
  } else if (tabId === 'daily') {
    renderDailyDay();
  } else if (tabId === 'journey') {
    renderJourneyCycles();
    renderHomeTree();
  } else if (tabId === 'community') {
    initCommunity();
  }
}

function openModal(id) {
  var el = document.getElementById(id);
  if (el) el.classList.add('open');
}
function closeModal(id) {
  var el = document.getElementById(id);
  if (el) el.classList.remove('open');
}
function closeBgModal(e, id) {
  if (e.target === document.getElementById(id)) {
    closeModal(id);
  }
}
function showToast(msg) {
  var t = document.getElementById('appToast');
  var txt = document.getElementById('toastText');
  if (t && txt) {
    txt.textContent = msg;
    t.classList.add('show');
    setTimeout(function() { t.classList.remove('show'); }, 2500);
  }
}

// ============================================================
// ===  STREAK & WEEKLY CALENDAR LOGIC                       ===
// ============================================================
function calcStreakStartDate() {
  if (AppState.streak.startDate) return new Date(AppState.streak.startDate);

  var dates = Object.keys(AppState.dayLogs).sort().reverse();
  var todayKey = todayDateKey();
  var consecutive = 0;
  var cursor = new Date();

  while (true) {
    var key = formatDateKey(cursor);
    var status = AppState.dayLogs[key];
    if (status === 'clean') {
      consecutive++;
      cursor.setDate(cursor.getDate() - 1);
    } else if (key === todayKey && !status) {
      // today not logged yet, continue to yesterday
      cursor.setDate(cursor.getDate() - 1);
    } else {
      break;
    }
  }

  if (consecutive > 0) {
    var start = new Date();
    start.setDate(start.getDate() - consecutive);
    return start;
  }
  return null;
}

function updateStreakTimer() {
  var start = calcStreakStartDate();
  if (!start) {
    document.getElementById('timer-d').textContent = '00';
    document.getElementById('timer-h').textContent = '00';
    document.getElementById('timer-m').textContent = '00';
    document.getElementById('timer-s').textContent = '00';
    var prog = document.getElementById('homeCycleProg');
    if (prog) prog.textContent = 'Day 1 of 365 • 0%';
    return;
  }

  var diff = Date.now() - start.getTime();
  if (diff < 0) diff = 0;

  var days = Math.floor(diff / (1000 * 60 * 60 * 24));
  var hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  var mins = Math.floor((diff / (1000 * 60)) % 60);
  var secs = Math.floor((diff / 1000) % 60);

  document.getElementById('timer-d').textContent = pad2(days);
  document.getElementById('timer-h').textContent = pad2(hours);
  document.getElementById('timer-m').textContent = pad2(mins);
  document.getElementById('timer-s').textContent = pad2(secs);

  var pct = Math.min(100, Math.round((days / 365) * 100));
  var progEl = document.getElementById('homeCycleProg');
  if (progEl) progEl.textContent = 'Day ' + (days + 1) + ' of 365 • ' + pct + '%';
  var barEl = document.getElementById('homeDayBar');
  if (barEl) barEl.style.width = Math.max(3, pct) + '%';
}

var currentWeekOffset = 0;
function changeWeek(delta) {
  currentWeekOffset += delta;
  if (currentWeekOffset > 0) currentWeekOffset = 0;
  var btnNext = document.getElementById('btnNextWeek');
  if (btnNext) btnNext.disabled = (currentWeekOffset >= 0);
  renderWeek();
}

function renderWeek() {
  var grid = document.getElementById('weekGrid');
  if (!grid) return;
  grid.innerHTML = '';

  var now = new Date();
  var monday = new Date(now);
  var dayOfWeek = monday.getDay(); // 0 is Sun, 1 is Mon
  var diffToMon = dayOfWeek === 0 ? -6 : 1 - dayOfWeek;
  monday.setDate(monday.getDate() + diffToMon + (currentWeekOffset * 7));

  var dayNames = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];
  var todayKey = todayDateKey();

  for (var i = 0; i < 7; i++) {
    var cur = new Date(monday);
    cur.setDate(cur.getDate() + i);
    var dateKey = formatDateKey(cur);
    var isToday = (dateKey === todayKey);
    var isFuture = (cur > now && !isToday);

    var col = document.createElement('div');
    col.className = 'day-col';

    var nameEl = document.createElement('div');
    nameEl.className = 'day-col-name' + (isToday ? ' today' : '');
    nameEl.textContent = dayNames[i];
    col.appendChild(nameEl);

    var dotEl = document.createElement('div');
    var status = AppState.dayLogs[dateKey];

    if (status === 'clean') {
      dotEl.className = 'day-dot clean';
      dotEl.innerHTML = '<i class="ti ti-check" style="font-size:11px;"></i>';
    } else if (status === 'relapse') {
      dotEl.className = 'day-dot relapse';
      dotEl.innerHTML = '<i class="ti ti-x" style="font-size:11px;"></i>';
    } else if (isFuture) {
      dotEl.className = 'day-dot future';
    } else {
      dotEl.className = 'day-dot empty';
    }

    if (!isFuture) {
      dotEl.style.cursor = 'pointer';
      (function(k, d) {
        dotEl.onclick = function() { openDayEditModal(k, d); };
      })(dateKey, cur.toDateString());
    }

    col.appendChild(dotEl);
    grid.appendChild(col);
  }

  var weekTitle = document.getElementById('weekTitle');
  if (weekTitle) {
    if (currentWeekOffset === 0) weekTitle.textContent = 'This Week';
    else if (currentWeekOffset === -1) weekTitle.textContent = 'Last Week';
    else weekTitle.textContent = Math.abs(currentWeekOffset) + ' Weeks Ago';
  }

  var todayLog = AppState.dayLogs[todayKey];
  var markBtn = document.getElementById('btnMarkClean');
  if (markBtn) {
    if (todayLog === 'clean') {
      markBtn.innerHTML = '<i class="ti ti-circle-check"></i> <span>Today Logged Clean ✓</span>';
      markBtn.style.opacity = '0.85';
    } else {
      markBtn.innerHTML = '<i class="ti ti-check"></i> <span>Mark Today as Clean</span>';
      markBtn.style.opacity = '1';
    }
  }

  renderTaskBadges();
}

function markTodayClean() {
  var key = todayDateKey();
  AppState.dayLogs[key] = 'clean';
  if (!AppState.streak.startDate) {
    AppState.streak.startDate = new Date().toISOString();
  }
  addXP(20);

  // Check 10 consecutive clean days to restore 1 life (up to 3)
  var currentLives = AppState.streak.lives !== undefined ? AppState.streak.lives : 3;
  if (currentLives < 3) {
    var consecutive = 0;
    var d = new Date();
    for (var i = 0; i < 10; i++) {
      var checkKey = d.toISOString().split('T')[0];
      if (AppState.dayLogs[checkKey] === 'clean') {
        consecutive++;
      } else {
        break;
      }
      d.setDate(d.getDate() - 1);
    }
    if (consecutive >= 10 && !AppState.streak.lastLifeRestoredAt10) {
      AppState.streak.lives = Math.min(3, currentLives + 1);
      AppState.streak.lastLifeRestoredAt10 = true;
      renderLivesDisplay();
      showToast('Alhamdulillah! 10 clean days achieved — 1 Life restored! 💖');
    }
  }

  saveAppState(true);
  renderWeek();
  renderHomeTree();
  renderLivesDisplay();
  updateStreakTimer();
  showToast('Today marked as clean 🌟 +20 XP');
}

var editingDayDateKey = null;
function openDayEditModal(k, d) {
  editingDayDateKey = k;
  var title = document.getElementById('dayEditTitle');
  if (title) title.textContent = 'Log Day: ' + d;
  openModal('dayEditModal');
}

function setPastDayStatus(status) {
  if (!editingDayDateKey) return;
  AppState.dayLogs[editingDayDateKey] = status;
  saveAppState(true);
  closeModal('dayEditModal');
  renderWeek();
  renderHomeTree();
  updateStreakTimer();
  showToast('Day updated to ' + status);
}

// ============================================================
// ===  LIVES & REPENTANCE                                   ===
// ============================================================
function renderLivesDisplay() {
  var heartsEl = document.getElementById('headerHearts');
  var livesCount = AppState.streak.lives !== undefined ? AppState.streak.lives : 3;
  if (heartsEl) {
    heartsEl.innerHTML = '';
    for (var i = 0; i < 3; i++) {
      var s = document.createElement('span');
      s.className = 'ht';
      s.textContent = '❤️';
      s.style.opacity = (i < livesCount) ? '1' : '0.2';
      heartsEl.appendChild(s);
    }
  }
  var setLives = document.getElementById('settingsLivesCount');
  if (setLives) setLives.textContent = livesCount;
}

function useRepentanceLife() {
  var lives = AppState.streak.lives !== undefined ? AppState.streak.lives : 3;
  if (lives <= 0) {
    alert('No repentance lives remaining. Complete 10 clean days to earn a life back!');
    return;
  }
  AppState.streak.lives = lives - 1;
  saveAppState(true);
  renderLivesDisplay();
  showToast('Repentance life used. Streak preserved! 💖');
}

function confirmFullReset() {
  if (confirm('Are you sure you want to reset your streak timer to Day 1? Your history will be preserved.')) {
    AppState.dayLogs[todayDateKey()] = 'relapse';
    AppState.streak.startDate = new Date().toISOString();
    saveAppState(true);
    renderWeek();
    renderHomeTree();
    updateStreakTimer();
    showToast('Streak reset to Day 1');
  }
}

// ============================================================
// ===  RELAPSE LOGGER & TAUBAH                              ===
// ============================================================
var selectedTriggers = [];
function openRelapseModal() {
  selectedTriggers = [];
  document.querySelectorAll('#relapseTriggersGrid button').forEach(function(b) {
    b.style.borderColor = 'var(--border)';
    b.style.background = '#fff';
    b.style.color = '#1e293b';
  });
  var nInp = document.getElementById('relapseNotesInput');
  if (nInp) nInp.value = '';

  // Update lives display in modal
  var livesCount = AppState.streak.lives !== undefined ? AppState.streak.lives : 3;
  var livesDisp = document.getElementById('relapseModalLivesDisplay');
  if (livesDisp) {
    var hearts = '';
    for (var i = 0; i < 3; i++) {
      hearts += (i < livesCount) ? '💖 ' : '🖤 ';
    }
    livesDisp.textContent = hearts.trim();
  }
  var shieldMsg = document.getElementById('relapseShieldMsg');
  var shieldBtn = document.getElementById('btnUseShield');
  var shieldBtnText = document.getElementById('btnUseShieldText');
  if (livesCount <= 0) {
    if (shieldMsg) shieldMsg.textContent = 'No Lives remaining. Complete 10 consecutive clean days to earn a Life back. You must fully reset your streak.';
    if (shieldBtn) { shieldBtn.disabled = true; shieldBtn.style.opacity = '0.4'; shieldBtn.style.pointerEvents = 'none'; }
    if (shieldBtnText) shieldBtnText.textContent = 'No Shield Lives Remaining';
  } else {
    if (shieldMsg) shieldMsg.textContent = 'You have ' + livesCount + ' ' + (livesCount === 1 ? 'Life' : 'Lives') + ' remaining. You can sacrifice 1 Life to shield your clean streak while making sincere Tawbah!';
    if (shieldBtn) { shieldBtn.disabled = false; shieldBtn.style.opacity = '1'; shieldBtn.style.pointerEvents = 'auto'; }
    if (shieldBtnText) shieldBtnText.textContent = 'Use 1 Life to Shield Streak';
  }

  openModal('relapseModal');
}

function toggleTrigger(btn) {
  var txt = btn.textContent.trim();
  var idx = selectedTriggers.indexOf(txt);
  if (idx !== -1) {
    selectedTriggers.splice(idx, 1);
    btn.style.borderColor = 'var(--border)';
    btn.style.background = '#fff';
    btn.style.color = '#1e293b';
  } else {
    selectedTriggers.push(txt);
    btn.style.borderColor = 'var(--red)';
    btn.style.background = '#fee2e2';
    btn.style.color = 'var(--red)';
  }
}

function submitRelapseLog() {
  var notes = document.getElementById('relapseNotesInput').value.trim();
  var entry = {
    date: new Date().toISOString(),
    triggers: selectedTriggers,
    notes: notes
  };
  AppState.relapseHistory.push(entry);
  AppState.dayLogs[todayDateKey()] = 'relapse';
  AppState.streak.startDate = new Date().toISOString();

  saveAppState(true);
  closeModal('relapseModal');
  renderWeek();
  renderHomeTree();
  updateStreakTimer();
  showToast('Tawbah recorded. Renew your intention and rise again.');
}

function submitRelapseWithShield() {
  var lives = AppState.streak.lives !== undefined ? AppState.streak.lives : 3;
  if (lives <= 0) {
    showToast('No shield lives remaining!');
    return;
  }
  var notes = document.getElementById('relapseNotesInput').value.trim();
  var entry = {
    date: new Date().toISOString(),
    triggers: selectedTriggers,
    notes: notes,
    shieldUsed: true
  };
  AppState.relapseHistory.push(entry);
  AppState.dayLogs[todayDateKey()] = 'relapse';
  AppState.streak.lives = lives - 1;
  // Do NOT reset streak startDate — shield preserves streak!

  saveAppState(true);
  closeModal('relapseModal');
  renderWeek();
  renderHomeTree();
  renderLivesDisplay();
  updateStreakTimer();
  showToast('Shield used! Streak preserved. ' + AppState.streak.lives + ' lives remaining. 💖');
}

function submitRelapseFullReset() {
  var notes = document.getElementById('relapseNotesInput').value.trim();
  var entry = {
    date: new Date().toISOString(),
    triggers: selectedTriggers,
    notes: notes,
    fullReset: true
  };
  AppState.relapseHistory.push(entry);
  AppState.dayLogs[todayDateKey()] = 'relapse';
  AppState.streak.startDate = new Date().toISOString();
  // Do NOT touch lives count on full reset

  saveAppState(true);
  closeModal('relapseModal');
  renderWeek();
  renderHomeTree();
  renderLivesDisplay();
  updateStreakTimer();
  showToast('Tawbah recorded. Timer reset. Rise again!');
}

// ============================================================
// ===  DAILY NIYAH (INTENTION)                              ===
// ============================================================
function openNiyahModal() {
  var inp = document.getElementById('niyahTextInput');
  if (inp) inp.value = AppState.niyah.text || '';
  openModal('niyahModal');
}

function submitNiyah() {
  var txt = document.getElementById('niyahTextInput').value.trim();
  AppState.niyah.text = txt;
  AppState.niyah.date = todayDateKey();
  addXP(10);
  saveAppState(true);
  closeModal('niyahModal');
  renderTaskBadges();
  showToast('Intention saved for today! +10 XP 🌟');
}

// ============================================================
// ===  365-DAY TREE OF FAITH & 16-STAGE SVG PROGRESSION     ===
// ============================================================
const TREE_MILESTONES = [
  { stage: 0, maxDay: 0, title: "Stage 0: Seed in Soil (Taubah)", nextTarget: "First Sprout", nextDays: 7 },
  { stage: 1, maxDay: 7, title: "Stage 1: First Sprout (Day 1-7)", nextTarget: "Twin Leaves", nextDays: 14 },
  { stage: 2, maxDay: 14, title: "Stage 2: Twin Leaves (Day 8-14)", nextTarget: "Firm Stem", nextDays: 21 },
  { stage: 3, maxDay: 21, title: "Stage 3: Firm Stem (Day 15-21)", nextTarget: "Young Plant", nextDays: 30 },
  { stage: 4, maxDay: 30, title: "Stage 4: Young Plant (Day 22-30)", nextTarget: "Deep Roots", nextDays: 45 },
  { stage: 5, maxDay: 45, title: "Stage 5: Deep Roots (Day 31-45)", nextTarget: "Sturdy Sapling", nextDays: 60 },
  { stage: 6, maxDay: 60, title: "Stage 6: Sturdy Sapling (Day 46-60)", nextTarget: "Dense Green Tree", nextDays: 90 },
  { stage: 7, maxDay: 90, title: "Stage 7: Dense Green Tree (Day 61-90)", nextTarget: "Young Cedar", nextDays: 120 },
  { stage: 8, maxDay: 120, title: "Stage 8: Young Cedar (Day 91-120)", nextTarget: "Expanding Foliage", nextDays: 150 },
  { stage: 9, maxDay: 150, title: "Stage 9: Expanding Foliage (Day 121-150)", nextTarget: "Half-Year Blossoms", nextDays: 180 },
  { stage: 10, maxDay: 180, title: "Stage 10: Half-Year Blossoms (Day 151-180)", nextTarget: "Fruit Bearing Shajar", nextDays: 220 },
  { stage: 11, maxDay: 220, title: "Stage 11: Fruit Bearing Shajar (Day 181-220)", nextTarget: "Emerald Sanctuary", nextDays: 270 },
  { stage: 12, maxDay: 270, title: "Stage 12: Emerald Sanctuary (Day 221-270)", nextTarget: "Golden Radiance", nextDays: 320 },
  { stage: 13, maxDay: 320, title: "Stage 13: Golden Radiance (Day 271-320)", nextTarget: "Ancient Guardian Oak", nextDays: 364 },
  { stage: 14, maxDay: 364, title: "Stage 14: Ancient Guardian Oak (Day 321-364)", nextTarget: "Shajarah-e-Tayyibah", nextDays: 365 },
  { stage: 15, maxDay: 9999, title: "Stage 15: Shajarah-e-Tayyibah (365+ Days)", nextTarget: "Full Year Complete!", nextDays: 365 }
];

function getTreeStage(day) {
  if (day <= 0) return 0;
  if (day <= 7) return 1;
  if (day <= 14) return 2;
  if (day <= 21) return 3;
  if (day <= 30) return 4;
  if (day <= 45) return 5;
  if (day <= 60) return 6;
  if (day <= 90) return 7;
  if (day <= 120) return 8;
  if (day <= 150) return 9;
  if (day <= 180) return 10;
  if (day <= 220) return 11;
  if (day <= 270) return 12;
  if (day <= 320) return 13;
  if (day <= 364) return 14;
  return 15;
}

function renderHomeTree() {
  var start = calcStreakStartDate();
  var daysClean = 0;
  if (start) {
    daysClean = Math.max(0, Math.floor((Date.now() - start.getTime()) / 86400000));
  }

  var stage = getTreeStage(daysClean);
  var icon = document.getElementById('homeTreeIcon');
  if (icon && typeof drawTree === 'function') {
    icon.innerHTML = drawTree(stage);
  }

  var jIcon = document.getElementById('journeyTreeIcon');
  if (jIcon && typeof drawTree === 'function') {
    jIcon.innerHTML = drawTree(stage);
  }

  var ms = TREE_MILESTONES[stage];
  var lbl = document.getElementById('homeTreeStage');
  if (lbl) lbl.textContent = ms.title;

  var jLbl = document.getElementById('journeyTreeStageTitle');
  if (jLbl) jLbl.textContent = ms.title;

  var jClean = document.getElementById('journeyCleanDaysText');
  if (jClean) jClean.textContent = daysClean + ' Clean Days Logged (Goal: 365)';

  // Milestone Progress bar
  var targetLabel = document.getElementById('treeMilestoneTarget');
  var daysLabel = document.getElementById('treeMilestoneDays');
  var bar = document.getElementById('treeMilestoneBar');

  if (targetLabel) targetLabel.textContent = 'Next: ' + ms.nextTarget;
  if (daysLabel) daysLabel.textContent = daysClean + ' / ' + ms.nextDays + ' Days';
  if (bar) {
    var pct = Math.min(100, Math.round((daysClean / ms.nextDays) * 100));
    bar.style.width = Math.max(5, pct) + '%';
  }

  // Render Daily Spiritual Thought for today's clean day
  renderDailyThought(Math.max(1, Math.min(365, daysClean + 1)));
}

// ============================================================
// ===  365 DAYS DAILY SPIRITUAL THOUGHT ENGINE              ===
// ============================================================
var currentThoughtDay = 1;

function renderDailyThought(day) {
  currentThoughtDay = Math.max(1, Math.min(365, day));
  if (typeof DAILY_THOUGHTS_365 === 'undefined' || !DAILY_THOUGHTS_365.length) return;

  var item = DAILY_THOUGHTS_365[currentThoughtDay - 1];
  if (!item) return;

  var dayDisplay = document.getElementById('thoughtDayDisplay');
  var topic = document.getElementById('thoughtTopic');
  var quote = document.getElementById('thoughtQuote');
  var ref = document.getElementById('thoughtRef');
  var wisdom = document.getElementById('thoughtWisdom');

  if (dayDisplay) dayDisplay.textContent = currentThoughtDay;
  if (topic) topic.textContent = item.topic;
  if (quote) quote.textContent = '"' + item.quote + '"';
  if (ref) ref.textContent = item.ref;
  if (wisdom) wisdom.textContent = item.wisdom;
}

function prevDailyThought() {
  if (currentThoughtDay > 1) {
    renderDailyThought(currentThoughtDay - 1);
  } else {
    renderDailyThought(365);
  }
}

function nextDailyThought() {
  if (currentThoughtDay < 365) {
    renderDailyThought(currentThoughtDay + 1);
  } else {
    renderDailyThought(1);
  }
}

// ============================================================
// ===  DAILY PROGRAM DAY SLIDER (DAYS 1 TO 90)              ===
// ============================================================
var currentSelectedDay = 1;

function getDayData(day) {
  if (typeof DAYS_DATA !== 'undefined' && DAYS_DATA[day]) return DAYS_DATA[day];
  if (typeof DAYS_DATA !== 'undefined' && DAYS_DATA[1]) return DAYS_DATA[1];
  return { ibnQayyim: { title: "Day " + day, excerpt: "", slides: [] }, breakingFree: { title: "", excerpt: "", slides: [] }, reminder: { title: "", body: "" } };
}

function getDayData(day) {
  var raw = (typeof DAYS_DATA !== 'undefined' && DAYS_DATA[day]) ? DAYS_DATA[day] : null;
  if (!raw && typeof DAYS_DATA !== 'undefined') raw = DAYS_DATA[1];
  if (!raw) return { ibn: { title: "Tazkiyah - Day " + day, excerpt: "", slides: [] }, bf: { title: "", excerpt: "", slides: [] }, dr: { title: "", body: "" } };

  var ibnMod = raw.ibn || raw.ibnQayyim || {};
  var bfMod = raw.bf || raw.breakingFree || {};
  var drMod = raw.dr || raw.reminder || {};
  return { ibn: ibnMod, bf: bfMod, dr: drMod };
}

// Function to calculate maximum accessible day (Day locking logic)
function getMaxUnlockedDay() {
  if (!AppState.dailyProgram || !AppState.dailyProgram.dayProgress) return 1;
  var maxUnlocked = 1;
  for (var d = 1; d <= 90; d++) {
    var p = AppState.dailyProgram.dayProgress[d];
    // A day is considered completed if at least one core lesson is completed
    if (p && (p.ibnDone || p.bfDone)) {
      maxUnlocked = Math.min(90, d + 1);
    } else {
      break;
    }
  }
  return maxUnlocked;
}

function onDaySliderChange(val) {
  currentSelectedDay = parseInt(val, 10);
  renderDailyDay();
}

function changeDailyDay(delta) {
  var n = currentSelectedDay + delta;
  if (n < 1) n = 1;
  if (n > 90) n = 90;
  currentSelectedDay = n;
  var slider = document.getElementById('daySlider');
  if (slider) slider.value = n;
  renderDailyDay();
}

function renderDailyDay() {
  var d = currentSelectedDay;
  var dData = getDayData(d);

  var badge = document.getElementById('dailyDayBadge');
  if (badge) badge.textContent = 'Day ' + d;

  var cycleBadge = document.getElementById('dailyCycleBadge');
  if (cycleBadge) {
    var cIdx = Math.floor((d - 1) / 7.5) + 1;
    if (typeof CYCLES !== 'undefined' && CYCLES[cIdx - 1]) {
      cycleBadge.textContent = 'Cycle ' + cIdx + ' • ' + CYCLES[cIdx - 1].name;
    } else {
      cycleBadge.textContent = 'Day ' + d + ' of 90';
    }
  }

  // Tazkiyah & Kanzul Iman module
  var ibnT = document.getElementById('dailyIbnTitle');
  var ibnE = document.getElementById('dailyIbnExcerpt');
  if (dData.ibn) {
    if (ibnT) ibnT.textContent = dData.ibn.title;
    var ex = dData.ibn.excerpt;
    if (!ex && dData.ibn.slides && dData.ibn.slides[0]) {
      ex = dData.ibn.slides[0].body || dData.ibn.slides[0].text || '';
    }
    if (ibnE) ibnE.textContent = ex;
  }

  // Breaking Free Neuroscience module
  var bfT = document.getElementById('dailyBfTitle');
  var bfE = document.getElementById('dailyBfExcerpt');
  if (dData.bf) {
    if (bfT) bfT.textContent = dData.bf.title;
    var bfEx = dData.bf.excerpt;
    if (!bfEx && dData.bf.slides && dData.bf.slides[0]) {
      bfEx = dData.bf.slides[0].body || dData.bf.slides[0].text || '';
    }
    if (bfE) bfE.textContent = bfEx;
  }

  // Practical Reminder module
  var drT = document.getElementById('dailyDrTitle');
  var drB = document.getElementById('dailyDrText');
  if (dData.dr) {
    if (drT) drT.textContent = dData.dr.title || 'Daily Practical Reminder';
    if (drB) drB.textContent = dData.dr.body || dData.dr.text || '';
  }

  // Journal input
  ensureDayProgress(d);
  var prog = AppState.dailyProgram.dayProgress[d];
  var jInp = document.getElementById('dailyJournalInput');
  if (jInp) jInp.value = prog.ibnRefl || '';

  renderTaskBadges();
}

function onJournalInput() {
  var jInp = document.getElementById('dailyJournalInput');
  if (!jInp) return;
  ensureDayProgress(currentSelectedDay);
  AppState.dailyProgram.dayProgress[currentSelectedDay].ibnRefl = jInp.value;
  var status = document.getElementById('journalSaveStatus');
  if (status) status.textContent = 'Saving...';
  debouncedSave();
  setTimeout(function() {
    if (status) status.textContent = 'Saved ✓';
  }, 600);
}

function onLessonSlideInput(val) {
  ensureDayProgress(currentSelectedDay);
  if (currentLessonType === 'ibn') {
    AppState.dailyProgram.dayProgress[currentSelectedDay].ibnRefl = val;
    var jInp = document.getElementById('dailyJournalInput');
    if (jInp) jInp.value = val;
  } else {
    AppState.dailyProgram.dayProgress[currentSelectedDay].bfRefl = val;
  }
  debouncedSave();
}

// ============================================================
// ===  LESSON SLIDES MODAL LOGIC                            ===
// ============================================================
var currentLessonType = 'ibn';
var currentLessonSlides = [];
var currentLessonIdx = 0;

function onLessonReflectionInput() {
  var errEl = document.getElementById('lessonReflectionError');
  if (errEl) errEl.style.display = 'none';
  var inp = document.getElementById('lessonReflectionInput');
  if (inp) {
    ensureDayProgress(currentSelectedDay);
    if (currentLessonType === 'ibn') {
      AppState.dailyProgram.dayProgress[currentSelectedDay].ibnRefl = inp.value;
    } else {
      AppState.dailyProgram.dayProgress[currentSelectedDay].bfRefl = inp.value;
    }
  }
}

function openFullLessonModal(type) {
  currentLessonType = type;
  var dData = getDayData(currentSelectedDay);
  var mod = (type === 'ibn') ? dData.ibn : dData.bf;

  if (!mod || !mod.slides || mod.slides.length === 0) {
    showToast('Lesson slides coming soon!');
    return;
  }

  currentLessonSlides = mod.slides;
  currentLessonIdx = 0;

  var titleEl = document.getElementById('lessonModalTitle');
  if (titleEl) {
    titleEl.textContent = mod.title || (type === 'ibn' ? 'Tazkiyah Lesson' : 'Neuroscience Lesson');
  }

  ensureDayProgress(currentSelectedDay);
  var prog = AppState.dailyProgram.dayProgress[currentSelectedDay];
  var savedRefl = (type === 'ibn') ? (prog.ibnRefl || '') : (prog.bfRefl || '');
  var reflInp = document.getElementById('lessonReflectionInput');
  if (reflInp) reflInp.value = savedRefl;
  var errEl = document.getElementById('lessonReflectionError');
  if (errEl) errEl.style.display = 'none';

  renderLessonSlide();
  openModal('lessonModal');
}

function renderLessonSlide() {
  var slide = currentLessonSlides[currentLessonIdx];
  var container = document.getElementById('lessonContentContainer');
  var indicator = document.getElementById('lessonSlideIndicator');

  if (indicator) indicator.textContent = 'Slide ' + (currentLessonIdx + 1) + ' of ' + currentLessonSlides.length;

  if (container && slide) {
    var title = slide.title || (slide.tag ? slide.tag : '');
    var body = slide.body || slide.text || '';
    var quote = slide.quote || '';
    var ref = slide.ref || '';
    var isIslamic = (currentLessonType === 'ibn');

    var html = '<div class="lesson-slide-content">';
    if (isIslamic) {
      html += '<div style="display:inline-block;padding:3px 10px;border-radius:6px;background:rgba(2,132,199,0.25);color:#7dd3fc;font-size:11px;font-weight:700;margin-bottom:8px;letter-spacing:0.4px;">';
      html += '  TAZKIYAH &bull; PURIFICATION OF THE HEART';
      html += '</div>';
    }
    if (title) html += '<h3 style="font-size:18px;font-weight:800;color:#fff;margin-bottom:12px;">' + title + '</h3>';
    if (body) {
      var formattedBody = body.replace(/\\n/g, '<br>');
      html += '<div style="font-size:14px;line-height:1.65;color:rgba(255,255,255,0.92);margin-bottom:16px;">' + formattedBody + '</div>';
    }

    if (quote) {
      html += '<div style="background:rgba(255,255,255,0.1);border-left:3px solid #38bdf8;padding:12px 14px;border-radius:0 10px 10px 0;margin-top:14px;">';
      html += '  <div style="font-style:italic;color:#e0f2fe;font-size:13.5px;">"' + quote + '"</div>';
      if (ref) {
        html += '  <div style="font-size:11.5px;color:#7dd3fc;margin-top:4px;font-weight:700;">' + ref + '</div>';
      } else if (isIslamic) {
        html += '  <div style="font-size:11px;color:#bae6fd;margin-top:4px;font-weight:700;">Tarjuma: Kanzul Iman (Aala Hazrat Imam Ahmad Raza Khan Bareillvi)</div>';
      }
      html += '</div>';
    } else if (isIslamic && body.indexOf('Surah') !== -1 && body.indexOf('Kanzul Iman') === -1) {
      html += '<div style="font-size:11px;color:#7dd3fc;margin-top:8px;font-weight:700;">[Tarjuma: Kanzul Iman - Aala Hazrat Imam Ahmad Raza Khan Bareillvi]</div>';
    }
    html += '</div>';
    container.innerHTML = html;
  }

  var isLastSlide = (currentLessonIdx === currentLessonSlides.length - 1);
  var reflSec = document.getElementById('lessonReflectionSection');
  if (reflSec) reflSec.style.display = isLastSlide ? 'block' : 'none';

  var btnPrev = document.getElementById('btnLessonPrev');
  var btnNext = document.getElementById('btnLessonNext');
  if (btnPrev) btnPrev.disabled = (currentLessonIdx === 0);
  if (btnNext) {
    if (isLastSlide) {
      btnNext.innerHTML = 'Complete Lesson &bull; +25 XP 🌟';
    } else {
      btnNext.innerHTML = 'Next &rarr;';
    }
  }
}

function lessonPrevSlide() {
  if (currentLessonIdx > 0) {
    currentLessonIdx--;
    renderLessonSlide();
  }
}

function lessonNextSlide() {
  if (currentLessonIdx < currentLessonSlides.length - 1) {
    currentLessonIdx++;
    renderLessonSlide();
  } else {
    var reflInp = document.getElementById('lessonReflectionInput');
    var val = reflInp ? reflInp.value.trim() : '';
    var errEl = document.getElementById('lessonReflectionError');
    if (!val || val.length < 5) {
      if (errEl) {
        errEl.style.display = 'block';
        errEl.textContent = '⚠️ Reflection required: please write your takeaway or commitment above before marking complete.';
      }
      if (reflInp) reflInp.focus();
      showToast('Please write your reflection before completing!');
      return;
    }

    ensureDayProgress(currentSelectedDay);
    if (currentLessonType === 'ibn') {
      AppState.dailyProgram.dayProgress[currentSelectedDay].ibnDone = true;
      AppState.dailyProgram.dayProgress[currentSelectedDay].ibnRefl = val;
    } else {
      AppState.dailyProgram.dayProgress[currentSelectedDay].bfDone = true;
      AppState.dailyProgram.dayProgress[currentSelectedDay].bfRefl = val;
    }
    addXP(25);
    saveAppState(true);
    closeModal('lessonModal');
    renderTaskBadges();
    showToast('Lesson completed! +25 XP 🌟');
  }
}

// ============================================================
// ===  MORNING & EVENING ADHKAR MODALS                      ===
// ============================================================
function openMorningModal() {
  renderDuaList('morning');
  openModal('morningModal');
}

function openEveningModal() {
  renderDuaList('evening');
  openModal('eveningModal');
}

function renderDuaList(type) {
  var list = (type === 'morning') ? MORNING_DUAS : EVENING_DUAS;
  var containerId = (type === 'morning') ? 'morningDuaList' : 'eveningDuaList';
  var container = document.getElementById(containerId);
  if (!container || !list) return;

  ensureDayProgress(currentSelectedDay);
  var checkedArr = (type === 'morning') ? AppState.dailyProgram.dayProgress[currentSelectedDay].mChecked : AppState.dailyProgram.dayProgress[currentSelectedDay].eChecked;

  var html = '';
  for (var i = 0; i < list.length; i++) {
    var d = list[i];
    var isChk = checkedArr && checkedArr[i];
    html += '<div class="dua-item' + (isChk ? ' checked' : '') + '" onclick="toggleDuaCheck(\\\'' + type + '\\\', ' + i + ')">';
    html += '  <div class="dua-hdr">';
    html += '    <div class="dua-title">' + (d.name || 'Dua') + (d.count ? ' (' + d.count + ')' : '') + '</div>';
    html += '    <div class="ritual-chk" style="width:22px;height:22px;' + (isChk ? 'background:#10b981;color:#fff;' : '') + '"><i class="ti ti-check" style="font-size:12px;"></i></div>';
    html += '  </div>';
    if (d.arabic) html += '  <div class="dua-arabic">' + d.arabic + '</div>';
    if (d.translit) html += '  <div class="dua-translit">' + d.translit + '</div>';
    if (d.translationUrdu) html += '  <div class="dua-translation" style="color:#0f766e;font-weight:600;margin-bottom:4px;">' + d.translationUrdu + '</div>';
    if (d.translation) html += '  <div class="dua-translation">' + d.translation + '</div>';
    if (d.source) html += '  <div class="dua-source">' + d.source + '</div>';
    html += '</div>';
  }
  container.innerHTML = html;
}

function toggleDuaCheck(type, idx) {
  ensureDayProgress(currentSelectedDay);
  var prog = AppState.dailyProgram.dayProgress[currentSelectedDay];
  if (type === 'morning') {
    if (!prog.mChecked) prog.mChecked = [];
    prog.mChecked[idx] = !prog.mChecked[idx];
  } else {
    if (!prog.eChecked) prog.eChecked = [];
    prog.eChecked[idx] = !prog.eChecked[idx];
  }
  saveAppState(false);
  renderDuaList(type);
  if (navigator.vibrate) navigator.vibrate(20);
}

function completeAdhkar(type) {
  ensureDayProgress(currentSelectedDay);
  if (type === 'morning') AppState.dailyProgram.dayProgress[currentSelectedDay].morningDone = true;
  else AppState.dailyProgram.dayProgress[currentSelectedDay].eveningDone = true;
  addXP(15);
  saveAppState(true);
  closeModal(type + 'Modal');
  renderTaskBadges();
  showToast(type.charAt(0).toUpperCase() + type.slice(1) + ' Adhkar completed! +15 XP 🌟');
}

function renderTaskBadges() {
  ensureDayProgress(currentSelectedDay);
  var p = AppState.dailyProgram.dayProgress[currentSelectedDay];
  var mDone = !!p.morningDone;
  var eDone = !!p.eveningDone;
  var nDone = (AppState.niyah && AppState.niyah.date === todayDateKey());
  var ibnDone = !!p.ibnDone;
  var bfDone = !!p.bfDone;

  // 1. Daily Practices Badge (Morning, Evening, Niyyah)
  var pracDoneCount = (mDone ? 1 : 0) + (eDone ? 1 : 0) + (nDone ? 1 : 0);
  var pracBadge = document.getElementById('dailyPracticesBadge');
  if (pracBadge) pracBadge.textContent = pracDoneCount + ' / 3 Done';

  // 2. Daily Lessons Badge (Ibn Qayyim & Neuroscience)
  var lessonsDoneCount = (ibnDone ? 1 : 0) + (bfDone ? 1 : 0);
  var lessonsBadge = document.getElementById('dailyLessonsBadge');
  if (lessonsBadge) lessonsBadge.textContent = lessonsDoneCount + ' / 2 Completed';

  // 3. Rectangular tab 1: Ibn Qayyim status
  var tabIbn = document.getElementById('rectTabIbn');
  var badgeIbn = document.getElementById('badgeIbnStatus');
  if (badgeIbn) {
    if (ibnDone) {
      badgeIbn.className = 'module-rect-status-badge status-badge-complete';
      badgeIbn.innerHTML = '<i class="ti ti-check"></i> <span>Completed</span>';
      if (tabIbn) tabIbn.classList.add('completed');
    } else {
      badgeIbn.className = 'module-rect-status-badge status-badge-pending';
      badgeIbn.innerHTML = '<span>Read & Reflect</span> <i class="ti ti-chevron-right"></i>';
      if (tabIbn) tabIbn.classList.remove('completed');
    }
  }

  // 4. Rectangular tab 2: Neuroscience status
  var tabNeuro = document.getElementById('rectTabNeuro');
  var badgeNeuro = document.getElementById('badgeNeuroStatus');
  if (badgeNeuro) {
    if (bfDone) {
      badgeNeuro.className = 'module-rect-status-badge status-badge-complete';
      badgeNeuro.innerHTML = '<i class="ti ti-check"></i> <span>Completed</span>';
      if (tabNeuro) tabNeuro.classList.add('completed');
    } else {
      badgeNeuro.className = 'module-rect-status-badge status-badge-pending';
      badgeNeuro.innerHTML = '<span>Read & Reflect</span> <i class="ti ti-chevron-right"></i>';
      if (tabNeuro) tabNeuro.classList.remove('completed');
    }
  }

  // 5. Ritual check marks on Daily Practices cards
  var chkM = document.getElementById('chkRitualMorning');
  var chkE = document.getElementById('chkRitualEvening');
  var chkN = document.getElementById('chkRitualNiyah');

  if (chkM) { chkM.style.background = mDone ? '#10b981' : ''; chkM.style.color = mDone ? '#fff' : ''; }
  if (chkE) { chkE.style.background = eDone ? '#10b981' : ''; chkE.style.color = eDone ? '#fff' : ''; }
  if (chkN) { chkN.style.background = nDone ? '#10b981' : ''; chkN.style.color = nDone ? '#fff' : ''; }
}

// ============================================================
// ===  URGE TOOLS (BREATHING & 33-COUNT TASBEEH)             ===
// ============================================================
var breathingActive = false;
var breathTimer = null;
var breathPhases = [
  { name: 'Inhale 4s', dur: 4, cls: 'inhale' },
  { name: 'Hold 7s', dur: 7, cls: 'hold' },
  { name: 'Exhale 8s', dur: 8, cls: 'exhale' }
];
var breathPhaseIdx = 0;

function toggleBreathing() {
  breathingActive = !breathingActive;
  var btn = document.getElementById('btnBreathToggle');
  var circ = document.getElementById('breathCircle');
  var txt = document.getElementById('breathText');

  if (breathingActive) {
    if (btn) btn.textContent = 'Pause Breathing';
    breathPhaseIdx = 0;
    runBreathCycle();
  } else {
    if (btn) btn.textContent = 'Start Breathing';
    if (breathTimer) clearTimeout(breathTimer);
    if (txt) txt.textContent = 'Ready';
    if (circ) circ.className = 'breath-circle';
  }
}

function runBreathCycle() {
  if (!breathingActive) return;
  var p = breathPhases[breathPhaseIdx];
  var circ = document.getElementById('breathCircle');
  var txt = document.getElementById('breathText');

  if (circ) circ.className = 'breath-circle ' + p.cls;
  if (txt) txt.textContent = p.name;

  breathTimer = setTimeout(function() {
    breathPhaseIdx = (breathPhaseIdx + 1) % breathPhases.length;
    runBreathCycle();
  }, p.dur * 1000);
}

// Tasbeeh phrases with authentic Ala Hazrat wazaif
var tasbeehCount = 0;
var tasbeehPhrases = [
  { ar: 'SubhanAllah', tr: 'Glory be to Allah' },
  { ar: 'Alhamdulillah', tr: 'Praise be to Allah' },
  { ar: 'Allahu Akbar', tr: 'Allah is Greatest' },
  { ar: 'Astaghfirullah', tr: "I seek Allah's forgiveness" },
  { ar: 'صَلَّى اللّٰهُ عَلَى النَّبِيِّ الْاُمِّيِّ وَآلِهِ صَلَّى اللّٰهُ عَلَيْهِ وَسَلَّمَ', tr: 'Durood-e-Raza (Al-Wazifatul Kareemah)' },
  { ar: 'يَا قُدُّوسُ يَا حَفِيظُ', tr: 'Wazifa Daf Shahwat (Aala Hazrat)' },
  { ar: 'آمَنْتُ بِاللّٰهِ وَرُسُلِهِ', tr: 'Wazifa Daf Waswasah (Al-Wazifatul Kareemah)' }
];
var tasbeehPhraseIdx = 0;

function tapTasbeehRing() {
  tasbeehCount++;
  if (tasbeehCount > 33) tasbeehCount = 1;
  var cntEl = document.getElementById('tasbeehCount');
  if (cntEl) cntEl.textContent = tasbeehCount;
  if (navigator.vibrate) navigator.vibrate(20);
}

function nextTasbeehPhrase() {
  tasbeehPhraseIdx = (tasbeehPhraseIdx + 1) % tasbeehPhrases.length;
  tasbeehCount = 0;
  var item = tasbeehPhrases[tasbeehPhraseIdx];
  var phEl = document.getElementById('tasbeehPhrase');
  var trEl = document.getElementById('tasbeehTrans');
  var cntEl = document.getElementById('tasbeehCount');
  if (phEl) phEl.textContent = item.ar;
  if (trEl) trEl.textContent = item.tr;
  if (cntEl) cntEl.textContent = '0';
}

function resetTasbeeh() {
  tasbeehCount = 0;
  var cntEl = document.getElementById('tasbeehCount');
  if (cntEl) cntEl.textContent = '0';
}

// ============================================================
// ===  JOURNEY SCREEN LOGIC                                 ===
// ============================================================
function renderJourneyCycles() {
  var container = document.getElementById('cyclesList');
  if (!container || typeof CYCLES === 'undefined') return;
  var html = '';
  for (var i = 0; i < CYCLES.length; i++) {
    var c = CYCLES[i];
    html += '<div class="cycle-card">';
    html += '  <div class="cycle-top">';
    html += '    <div class="cycle-title"><span>' + (c.emoji || '🌱') + '</span> ' + c.name + '</div>';
    html += '    <div class="cycle-badge">' + c.days + ' Days</div>';
    html += '  </div>';
    html += '  <div class="cycle-stages-list">';
    if (c.stages) {
      for (var j = 0; j < Math.min(4, c.stages.length); j++) {
        var stg = c.stages[j];
        html += '    <div class="stage-item">';
        html += '      <div class="stage-dot">' + stg.day + '</div>';
        html += '      <div>';
        html += '        <div style="font-weight:700;color:var(--text-primary);">' + stg.title + '</div>';
        html += '        <div style="color:#64748b;margin-top:2px;">' + stg.refl + '</div>';
        html += '      </div>';
        html += '    </div>';
      }
    }
    html += '  </div>';
    html += '</div>';
  }
  container.innerHTML = html;
}

// ============================================================
// ===  ASSESSMENT MODAL LOGIC (ONBOARDING FOR NEW USERS)    ===
// ============================================================
var assessmentQuestions = [
  { q: "Do you watch pornography more than once a week?", sub: "Your answers help us support you better.", type: "mental" },
  { q: "Does pornography use interfere with your daily responsibilities?", sub: "Your answers help us support you better.", type: "mental" },
  { q: "Do you feel guilty or ashamed after watching pornography?", sub: "Your answers help us support you better.", type: "spiritual" },
  { q: "Have you tried to stop but found it difficult?", sub: "Your answers help us support you better.", type: "mental" },
  { q: "Does pornography use affect your relationships or spiritual life?", sub: "Your answers help us support you better.", type: "relational" },
  { q: "How often do you watch pornography?", sub: "Be honest — this helps us understand your situation.", type: "frequency" }
];
var assessmentStep = 0;
var assessmentAnswers = [];

function openAssessmentView() {
  assessmentStep = 0;
  assessmentAnswers = [];
  document.getElementById('obStepQuestions').style.display = 'block';
  document.getElementById('obStepResults').style.display = 'none';
  renderAssessmentQuestion();
  openModal('assessmentModal');
}

function renderAssessmentQuestion() {
  var item = assessmentQuestions[assessmentStep];
  var badge = document.getElementById('obQBadge');
  var title = document.getElementById('obQTitle');
  var sub = document.getElementById('obQSub');
  var lbl = document.getElementById('obQProgressLabel');
  var bar = document.getElementById('obQProgressBar');
  var yesNoArea = document.getElementById('obYesNoOptions');
  var freqArea = document.getElementById('obFrequencyOptions');

  if (badge) badge.textContent = 'Q' + (assessmentStep + 1);
  if (title) title.textContent = item.q;
  if (sub) sub.textContent = item.sub;
  if (lbl) lbl.textContent = 'Question ' + (assessmentStep + 1) + ' of ' + assessmentQuestions.length;
  if (bar) bar.style.width = Math.round(((assessmentStep + 1) / assessmentQuestions.length) * 100) + '%';

  if (assessmentStep < 5) {
    if (yesNoArea) yesNoArea.style.display = 'block';
    if (freqArea) freqArea.style.display = 'none';
  } else {
    if (yesNoArea) yesNoArea.style.display = 'none';
    if (freqArea) freqArea.style.display = 'flex';
  }
}

function answerAssessmentQuestion(ans) {
  assessmentAnswers.push({ yes: ans, type: assessmentQuestions[assessmentStep].type });
  if (assessmentStep < 5) {
    assessmentStep++;
    renderAssessmentQuestion();
  }
}

function answerFrequency(freq) {
  showAssessmentResults(freq);
}

function showAssessmentResults(freq) {
  if (!freq) freq = 3;
  document.getElementById('obStepQuestions').style.display = 'none';
  document.getElementById('obStepResults').style.display = 'block';

  var mY = assessmentAnswers.filter(function(a) { return a.type === 'mental' && a.yes; }).length;
  var mT = assessmentAnswers.filter(function(a) { return a.type === 'mental'; }).length || 1;
  var sY = assessmentAnswers.filter(function(a) { return a.type === 'spiritual' && a.yes; }).length;
  var rY = assessmentAnswers.filter(function(a) { return a.type === 'relational' && a.yes; }).length;
  var totalYes = assessmentAnswers.filter(function(a) { return a.yes; }).length;

  var fb = (freq - 1) * 8;
  var mental = Math.min(95, Math.round((mY / mT) * 70 + fb + 10));
  var spiritual = Math.min(95, Math.round((sY + (freq > 2 ? 1 : 0)) / 2 * 80 + fb + 10));
  var relational = Math.min(95, Math.round((rY + (totalYes > 2 ? 1 : 0)) / 2 * 70 + fb + 10));

  var displayScore = (totalYes + (freq >= 3 ? 1 : 0)) + ' / 6';
  var circle = document.getElementById('resScoreCircle');
  if (circle) circle.textContent = displayScore;

  var desc = document.getElementById('resDescription');
  if (desc) {
    if (totalYes <= 1) {
      desc.textContent = "Your responses suggest minimal challenges. Keep up the good work and stay vigilant.";
    } else if (totalYes <= 3) {
      desc.textContent = "Your responses indicate some challenges with pornography use. Recovery support can be beneficial.";
    } else {
      desc.textContent = "Your responses indicate significant challenges. This app will guide you step by step to freedom.";
    }
  }

  AppState.assessment.answers = assessmentAnswers;
  AppState.assessment.mentalScore = mental;
  AppState.assessment.spiritualScore = spiritual;
  AppState.assessment.relationalScore = relational;
  AppState.assessment.completedDate = new Date().toISOString();

  var mEl = document.getElementById('resMentalScore');
  var mBar = document.getElementById('resMentalBar');
  var sEl = document.getElementById('resSpiritualScore');
  var sBar = document.getElementById('resSpiritualBar');
  var rEl = document.getElementById('resRelationalScore');
  var rBar = document.getElementById('resRelationalBar');

  if (mEl) mEl.textContent = mental + '%';
  if (mBar) mBar.style.width = mental + '%';
  if (sEl) sEl.textContent = spiritual + '%';
  if (sBar) sBar.style.width = spiritual + '%';
  if (rEl) rEl.textContent = relational + '%';
  if (rBar) rBar.style.width = relational + '%';
}

function finishAssessmentAndSetNiyah() {
  AppState.onboardingDone = true;
  saveAppState(true);
  closeModal('assessmentModal');
  showToast('Assessment profile saved 📊');
  setTimeout(function() {
    openNiyahModal();
  }, 400);
}

// ============================================================
// ===  COMMUNITY BROTHERHOOD (ANONYMOUS RECOVERY FEED)      ===
// ============================================================
var defaultCommunityPosts = [
  {
    id: 'post_1',
    author: 'Mujahid #214',
    daysClean: 42,
    time: '2 hours ago',
    text: 'Alhamdulillah, reached Day 40 yesterday! When urges struck late at night, I did the 4-7-8 breathing and read Surah Fussilat. Stay strong brothers, your future clean self will thank you.',
    likes: 19
  },
  {
    id: 'post_2',
    author: 'Salik #805',
    daysClean: 14,
    time: '5 hours ago',
    text: 'Please make dua for me brothers. The flatline period has hit hard and feeling low energy, but I refuse to relapse. Dhikr and morning awrad are keeping me grounded.',
    likes: 14
  },
  {
    id: 'post_3',
    author: 'Seeker #391',
    daysClean: 78,
    time: 'Yesterday',
    text: 'The best thing that happened after 60 days: brain fog disappeared completely and Salah became sweet again. Guard your gaze strictly, especially on your phone screens.',
    likes: 31
  }
];

function initCommunity() {
  if (!AppState.communityPosts || AppState.communityPosts.length === 0) {
    AppState.communityPosts = defaultCommunityPosts.slice();
  }
  if (!AppState.communityAlias) {
    var randomNum = Math.floor(100 + Math.random() * 900);
    var titles = ['Mujahid', 'Salik', 'Sabir', 'Muhsin', 'Seeker', 'Servant'];
    AppState.communityAlias = titles[Math.floor(Math.random() * titles.length)] + ' #' + randomNum;
  }
  var aliasEl = document.getElementById('commAliasDisplay');
  var postingEl = document.getElementById('commPostingAs');
  if (aliasEl) aliasEl.textContent = AppState.communityAlias;
  if (postingEl) postingEl.textContent = AppState.communityAlias;
  renderCommunityFeed();
}

function renderCommunityFeed() {
  var container = document.getElementById('communityFeedList');
  if (!container) return;
  var posts = AppState.communityPosts || defaultCommunityPosts;
  var html = '';

  for (var i = 0; i < posts.length; i++) {
    var p = posts[i];
    html += '<div style="background:#ffffff; border-radius:16px; padding:15px; margin-bottom:12px; border:1px solid var(--border); box-shadow:0 2px 8px rgba(0,0,0,0.04);">';
    html += '  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">';
    html += '    <div style="display:flex; align-items:center; gap:8px;">';
    html += '      <div style="width:34px; height:34px; border-radius:50%; background:#e0f2fe; color:#0284c7; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:13px;">';
    html += '        ' + p.author.charAt(0);
    html += '      </div>';
    html += '      <div>';
    html += '        <div style="font-size:13px; font-weight:800; color:#1e293b;">' + p.author + '</div>';
    html += '        <div style="font-size:10.5px; color:#10b981; font-weight:700;">' + (p.daysClean || 1) + ' Days Clean</div>';
    html += '      </div>';
    html += '    </div>';
    html += '    <span style="font-size:11px; color:#94a3b8;">' + p.time + '</span>';
    html += '  </div>';
    html += '  <div style="font-size:13.5px; color:#334155; line-height:1.55; margin-bottom:10px;">' + p.text.replace(/\\n/g, '<br>') + '</div>';
    html += '  <div style="display:flex; justify-content:flex-end;">';
    html += '    <button onclick="likeCommunityPost(' + i + ')" style="background:none; border:none; color:#64748b; font-size:12px; font-weight:600; cursor:pointer; display:flex; align-items:center; gap:4px;">';
    html += '      <i class="ti ti-heart" style="color:#ef4444;"></i> ' + (p.likes || 0) + ' Brothers Inspired';
    html += '    </button>';
    html += '  </div>';
    html += '</div>';
  }
  container.innerHTML = html;
}

function submitCommunityPost() {
  var inp = document.getElementById('communityPostInput');
  if (!inp) return;
  var text = inp.value.trim();
  if (!text) {
    alert('Please enter your thought or reflection first.');
    return;
  }
  if (!AppState.communityPosts) AppState.communityPosts = [];
  var newP = {
    id: 'post_' + Date.now(),
    author: AppState.communityAlias || 'Anonymous Brother',
    daysClean: AppState.cleanDays || 1,
    time: 'Just now',
    text: text,
    likes: 1
  };
  AppState.communityPosts.unshift(newP);
  inp.value = '';
  saveAppState(true);
  renderCommunityFeed();
  showToast('Shared with Brotherhood anonymously! 🤝');
}

function likeCommunityPost(idx) {
  if (AppState.communityPosts && AppState.communityPosts[idx]) {
    AppState.communityPosts[idx].likes = (AppState.communityPosts[idx].likes || 0) + 1;
    saveAppState(false);
    renderCommunityFeed();
  }
}

function openUrgeRescueModal() {
  openModal('urgeModal');
}

// ============================================================
// ===  GLOBAL INITIALIZATION & EVENT LISTENERS              ===
// ============================================================
function checkOnboardingOrMainApp() {
  var obContainer = document.getElementById('onboardingFlowContainer');
  var shell = document.getElementById('appShell');

  if (!AppState.onboardingDone) {
    if (obContainer) {
      obContainer.style.display = 'flex';
      var splash = document.getElementById('splash-screen');
      if (splash) splash.classList.remove('hidden');
    }
    if (shell) shell.style.display = 'none';
  } else {
    if (obContainer) obContainer.style.display = 'none';
    if (shell) shell.style.display = 'flex';
    renderAll();
  }
}

function finishFullOnboarding() {
  AppState.onboardingDone = true;
  var uInp = document.getElementById('username-input');
  if (uInp && uInp.value.trim().length >= 3) {
    AppState.communityAlias = uInp.value.trim();
    if (!AppState.user.name) AppState.user.name = uInp.value.trim();
  }
  var itxt = document.getElementById('p4itxt');
  if (itxt && itxt.value.trim()) {
    AppState.niyah.text = itxt.value.trim();
    AppState.niyah.date = todayDateKey();
  }
  saveAppState(true);
  checkOnboardingOrMainApp();
  showToast('Welcome to Iradah! Bismillah 🌟');
}

function openFullOnboardingJourney() {
  var obContainer = document.getElementById('onboardingFlowContainer');
  var shell = document.getElementById('appShell');
  if (obContainer) {
    obContainer.style.display = 'flex';
    var screens = ['q-screen', 'q6-screen', 'results-screen', 'gender-screen', 'urge-screen', 'dhikr-screen', 'dua-screen', 'breathe-screen', 'username-screen', 'whystop-screen'];
    screens.forEach(function(sId) {
      var el = document.getElementById(sId);
      if (el) el.classList.add('hidden');
    });
    var splash = document.getElementById('splash-screen');
    if (splash) splash.classList.remove('hidden');
    var p2 = document.getElementById('phase2');
    if (p2) { p2.classList.remove('active'); p2.style.display = 'none'; }
    var p2wrap = document.querySelector('.p2-wrap');
    if (p2wrap) p2wrap.style.display = 'none';
    var p3 = document.getElementById('phase3-wrap');
    if (p3) p3.style.display = 'none';
    var p4 = document.getElementById('phase4-wrap');
    if (p4) p4.style.display = 'none';
    var p4sd = document.getElementById('p4sdone');
    if (p4sd) p4sd.style.display = 'none';
    window.scrollTo(0, 0);
  }
  if (shell) shell.style.display = 'none';
}

function renderAll() {
  updateSyncIndicator(true);
  updateXPDisplay();
  renderWeek();
  renderLivesDisplay();
  renderHomeTree();
  renderDailyDay();
  renderTaskBadges();
  updateStreakTimer();
  initNotifications();
  initCommunity();
}

document.addEventListener('DOMContentLoaded', function() {
  loadAppState();
  initFirebase();

  // Route to onboarding flow or main dashboard
  checkOnboardingOrMainApp();

  // Register service worker
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(function(){});
  }

  // Real-time timer update
  setInterval(updateStreakTimer, 1000);

  // Auto-save on page exit
  window.addEventListener('beforeunload', function() { saveAppState(false); });
  document.addEventListener('visibilitychange', function() {
    if (document.visibilityState === 'hidden') saveAppState(false);
  });
});
"""
