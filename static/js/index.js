var window.onscroll = function () {
    scrollRotate();
};

function scrollRotate() {
    let image = document.getElementById("spin-logo");
    image.style.transform = "rotate(" + window.pageYOffset/2 + "deg)";
}