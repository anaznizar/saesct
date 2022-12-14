function menuButton() {
    var x = document.getElementById("responsive");
    if (x.className === "on") {
        x.className = "off";
    } else {
        x.className = "on";
    }
    goToTop()
}

window.onscroll = function () {
    var x = document.getElementById("responsive");
    var currentScrollPos = window.pageYOffset;
    if (currentScrollPos > 5) {
        x.className = "off";
    }
}

function goToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}