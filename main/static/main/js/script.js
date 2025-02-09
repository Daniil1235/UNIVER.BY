/*jshint esversion: 6 */
    const currentTheme = sessionStorage.getItem('CurrentTheme');
     if (currentTheme === 'dark-theme') {
        document.body.className = 'dark-theme';
    } else {
        document.body.className = 'light-theme';
    }

document.getElementById('themeToggle').addEventListener('click', function() {
    "use strict";
    const currentTheme = sessionStorage.getItem('CurrentTheme');
    if (currentTheme === 'dark-theme') {
        document.body.className = 'light-theme';
        sessionStorage.setItem('CurrentTheme', 'light-theme');
    } else {
        document.body.className = 'dark-theme';
        sessionStorage.setItem('CurrentTheme', 'dark-theme');
    }
});
        document.getElementById('themeToggle2').addEventListener('click', function() {
    "use strict";
    const currentTheme = sessionStorage.getItem('CurrentTheme');
    if (currentTheme === 'dark-theme') {
        document.body.className = 'light-theme';
        sessionStorage.setItem('CurrentTheme', 'light-theme');
    } else {
        document.body.className = 'dark-theme';
        sessionStorage.setItem('CurrentTheme', 'dark-theme');
    }
});