let currentIndex = 0;

function showSlide(index) {
    const slider = document.getElementById('gallery-slider');
    const totalSlides = slider.children.length;
    if (index >= totalSlides) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = totalSlides - 1;
    } else {
        currentIndex = index;
    }
    const offset = -currentIndex * 100;
    slider.style.transform = `translateX(${offset}%)`;
}

function nextSlide() {
    showSlide(currentIndex + 1);
}

function prevSlide() {
    showSlide(currentIndex - 1);
}

function changeColor(color) {
    document.body.style.backgroundColor = color;
}
