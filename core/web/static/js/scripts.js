function setLanguageUA() {
    Cookies.set('lang', 'ukr'); 
    location.reload();
}

function setLanguageEN() {
    Cookies.set('lang', 'eng'); 
    location.reload();
}

function openNav() {
    document.getElementById("sideNav").style.width = '250px';
}
  
function closeNav() {
    document.getElementById("sideNav").style.width = '0';
}

function showContent(btn, contentID) {
    btn.style.display = 'none';
    document.getElementById(contentID).style.display = 'block';
}