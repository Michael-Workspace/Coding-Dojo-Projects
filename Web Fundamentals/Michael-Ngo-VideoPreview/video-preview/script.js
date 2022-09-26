console.log("page loaded...");

function playvid(element) {
    element.play();
    element.muted=true;
}

function stopvid(element) {
    element.pause();
}