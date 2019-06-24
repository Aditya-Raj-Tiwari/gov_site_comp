var listItm = $('h3');
var cssforh3 = {
    'color': 'white',
    'background': '#3a79d1',
    'margin-top': '12px',
    'margin-bottom': '-0px',
    'padding-left': '20px',
    'padding-top': '5px'
}

listItm.eq(0).css(cssforh3)
listItm.eq(1).css({
    'color': 'white',
    'margin-top': '12px',
    'background': '#3a79d1',
    'margin-bottom': '-0px',
    'padding-left': '20px',
    'padding-top': '5px'
})
listItm.eq(2).css(cssforh3)
listItm.eq(3).css({
    'color': 'white',
    'background': '#3a79d1',
    'margin-top': '12px',
    'margin-bottom': '-0px',
    'padding-left': '20px',
    'padding-top': '5px'
})


function showTime() {
    var date = new Date();
    var h = date.getHours(); // 0 - 23
    var m = date.getMinutes(); // 0 - 59
    var s = date.getSeconds(); // 0 - 59
    var session = "AM";

    if (h == 0) {
        h = 12;
    }

    if (h > 12) {
        h = h - 12;
        session = "PM";
    }

    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;

    var time = h + ":" + m + ":" + s + " " + session;
    document.getElementById("MyClockDisplay").innerText = time;
    document.getElementById("MyClockDisplay").textContent = time;

    setTimeout(showTime, 1000);

}

showTime();
