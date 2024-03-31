const carouselList = document.getElementById('carouselList');
const items = carouselList.getElementsByClassName('carousel-item');
const itemHeight = items[0].offsetHeight;
const totalItems = items.length;
let currentIndex = 0;

function scrollCarousel() {
    currentIndex++;
    if (currentIndex === totalItems) {
        currentIndex = 0;
    }
    const displacement = -currentIndex * itemHeight;
    carouselList.style.top = displacement + 'px';
}

// Set interval for autoscrolling (adjust timing as needed)
const scrollInterval = setInterval(scrollCarousel, 2000);