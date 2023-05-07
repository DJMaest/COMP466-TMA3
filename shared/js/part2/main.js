var isRandom = false;
let slideIndex = 1;
let isPlaying = false;
var isRandom = false;
var interval;
const showToggle = document.getElementById("showToggle");

showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}

showToggle.addEventListener("change", (e) => {
    const val = e.target.value;
    if (val === "random") {

        $(".my-next").css("display", "none");
        $(".my-prev").css("display", "none");
        isRandom = true;
    } else {
        isRandom = false;
        $(".my-next").css("display", "");
        $(".my-prev").css("display", "");
    }

});

$("#playBtn").on("click", () => {

    if (isPlaying) {

        isPlaying = false;
        clearInterval(interval);
        $("#playBtn").attr("src", "/shared/images/part2/icons/play.png");

    } else {
        $("#playBtn").attr("src", "/shared/images/part2/icons/pause.png");

        interval = setInterval(() => {
            slideIndex = isRandom ? Math.round(Math.random() * (20 - 1) + 1) : slideIndex+1;
            showSlides(slideIndex);
        }, 2000);
        isPlaying = true;
    }
});

