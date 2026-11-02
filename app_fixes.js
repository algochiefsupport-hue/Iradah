// secure_recovery_and_day_lock.js
// Drop-in fix for Iradah app:
// 1) Replace EmailJS OTP reset flow with a security-question reset flow.
// 2) Prevent day advancement until the previous day is completed.

(function () {
  'use strict';

  function hashSecret(str) {
    var hash = 0;
    if (!str) return 'p_0';
    for (var i = 0; i < str.length; i++) {
      var char = str.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash |= 0;
    }
    return 'p_' + Math.abs(hash).toString(36);
  }

  function getUserByEmail(email) {
    if (!email || !email.includes('@')) return null;
    var key = email.toLowerCase().trim().replace(/[^a-z0-9]/g, '_');
    try {
      var raw = localStorage.getItem('purify_cloud_' + key);
      if (!raw) return null;
      return JSON.parse(raw);
    } catch (e) {
      return null;
    }
  }

  function saveUserByEmail(email, data) {
    if (!email || !email.includes('@')) return;
    var key = email.toLowerCase().trim().replace(/[^a-z0-9]/g, '_');
    try {
      localStorage.setItem('purify_cloud_' + key, JSON.stringify(data));
    } catch (e) {}
  }

  function showToast(msg) {
    if (window.showToast) {
      window.showToast(msg);
      return;
    }
    console.log(msg);
  }

  // ---------------------------
  // 1) Security-question reset
  // ---------------------------
  function verifySecurityAnswer(email, answer) {
    var user = getUserByEmail(email);
    if (!user || !user.securityAnswerHash) return false;

    var normalized = (answer || '').trim().toLowerCase();
    return user.securityAnswerHash === hashSecret(normalized);
  }

  function secureForgotPasswordReset() {
    var email = document.getElementById('authForgotEmailInput')
      ? document.getElementById('authForgotEmailInput').value.trim().toLowerCase()
      : '';
    var user = getUserByEmail(email);

    if (!email || !user) {
      showToast('No account found with this email.');
      return false;
    }

    var q = user.securityQuestion || 'What was the name of your first school?';
    var response = prompt('Security question:\n\n' + q + '\n\nAnswer:', '');
    if (response === null) return false;

    if (!verifySecurityAnswer(email, response)) {
      showToast('Incorrect security answer.');
      return false;
    }

    var newPass = prompt('Enter new password (at least 4 chars):', '');
    if (newPass === null) return false;
    if (newPass.trim().length < 4) {
      showToast('Password must be at least 4 characters.');
      return false;
    }

    user.authHash = hashSecret(newPass.trim());
    saveUserByEmail(email, user);

    if (window.AppState) {
      window.AppState.authHash = user.authHash;
      window.AppState.user = window.AppState.user || {};
      window.AppState.user.email = email;
    }

    showToast('Password reset successful!');
    return true;
  }

  // Replace old OTP reset function if it exists.
  if (typeof window.verifyEmailOTP === 'function') {
    window.verifyEmailOTP = function () {
      return secureForgotPasswordReset();
    };
  }

  if (typeof window.sendEmailOTP === 'function') {
    window.sendEmailOTP = function () {
      var emailInput = document.getElementById('authForgotEmailInput');
      var email = emailInput ? emailInput.value.trim().toLowerCase() : '';
      var user = getUserByEmail(email);
      if (!email || !user) {
        showToast('No account found for this email.');
        return false;
      }
      showToast('Security question ready.');
      return true;
    };
  }

  // ---------------------------
  // 2) Day lock logic
  // ---------------------------
  function isDayProgressComplete(progress) {
    if (!progress) return false;
    return !!(progress.morningDone && progress.eveningDone && progress.ibnDone && progress.bfDone && progress.drDone);
  }

  function getMaxUnlockedDay() {
    var maxUnlocked = 1;
    var dayProgress = (window.AppState && window.AppState.dailyProgram && window.AppState.dailyProgram.dayProgress) || {};

    for (var d = 1; d <= 90; d++) {
      var progress = dayProgress[d];
      if (!progress) {
        break;
      }
      if (isDayProgressComplete(progress)) {
        maxUnlocked = d + 1;
      } else {
        break;
      }
    }

    return Math.max(1, Math.min(90, maxUnlocked));
  }

  function enforceDayLock(targetDay) {
    var day = Number(targetDay || 1);
    var unlocked = getMaxUnlockedDay();

    if (day > unlocked) {
      showToast('Complete the previous day first before unlocking the next day.');
      return false;
    }

    if (window.AppState) {
      window.AppState.dailyProgram = window.AppState.dailyProgram || {};
      window.AppState.dailyProgram.currentDay = day;
    }
    return true;
  }

  function attachDayLock() {
    if (!window.AppState) return;
    var current = Number(window.AppState.dailyProgram && window.AppState.dailyProgram.currentDay || 1);
    var unlocked = getMaxUnlockedDay();
    if (current > unlocked) {
      window.AppState.dailyProgram.currentDay = unlocked;
    }

    if (typeof window.changeDailyDay === 'function') {
      var originalChangeDailyDay = window.changeDailyDay;
      window.changeDailyDay = function (delta) {
        var currentDay = Number(window.AppState.dailyProgram.currentDay || 1);
        if (delta > 0 && !isDayProgressComplete((window.AppState.dailyProgram.dayProgress || {})[currentDay])) {
          showToast('Day ' + currentDay + ' is still incomplete. Finish it first.');
          return;
        }
        return originalChangeDailyDay(delta);
      };
    }

    if (typeof window.onDaySliderChange === 'function') {
      var originalOnDaySliderChange = window.onDaySliderChange;
      window.onDaySliderChange = function (value) {
        var day = Number(value || 1);
        if (!enforceDayLock(day)) return;
        return originalOnDaySliderChange(value);
      };
    }
  }

  // attach when the app becomes available
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      setTimeout(attachDayLock, 500);
    });
  } else {
    setTimeout(attachDayLock, 500);
  }

  window.secureForgotPasswordReset = secureForgotPasswordReset;
  window.enforceDayLock = enforceDayLock;
  window.getMaxUnlockedDay = getMaxUnlockedDay;
})();
