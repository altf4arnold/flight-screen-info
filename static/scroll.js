// JavaScript for autoscrolling all carousels simultaneously
const carouselContainers = document.querySelectorAll('.carousel-container');
const carousels = [];

carouselContainers.forEach(container => {
  const carouselList = container.querySelector('.carousel-list');
  const items = carouselList.getElementsByClassName('carousel-item');
  const itemHeight = items[0].offsetHeight;
  const totalItems = items.length;
  let currentIndex = 0;
  let isResetting = false;

  // Push each carousel object into an array
  carousels.push({
    carouselList,
    itemHeight,
    totalItems,
    currentIndex,
    isResetting
  });
});

function scrollAllCarousels() {
  carousels.forEach(carousel => {
    carousel.currentIndex++;
    if (carousel.currentIndex === carousel.totalItems) {
      carousel.isResetting = true;
      carousel.currentIndex = 0;
      carousel.carouselList.style.transition = 'top 0.5s ease-in-out'; // Enable transition for smooth scrolling
      carousel.carouselList.style.top = `${-carousel.itemHeight}px`; // Start scroll animation
    }
    if (carousel.isResetting && carousel.currentIndex === 0) {
      // If resetting and back to the top, reset the top position instantly without animation
      carousel.isResetting = false;
      carousel.carouselList.style.transition = 'none'; // Disable transition for instant reset
      carousel.carouselList.style.top = '0px'; // Reset to the top instantly
      setTimeout(() => {
        carousel.carouselList.style.transition = ''; // Re-enable transition
      }, 50); // Add a slight delay before re-enabling transition to ensure it takes effect
    }
    const displacement = -carousel.currentIndex * carousel.itemHeight;
    carousel.carouselList.style.top = `${displacement}px`;
  });
}

// Set interval for autoscrolling all carousels simultaneously
setInterval(scrollAllCarousels, 3000);
