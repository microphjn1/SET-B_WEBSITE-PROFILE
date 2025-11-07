
const slider = document.querySelector('.slider');
const list = slider.querySelector('.list');
const items = list.querySelectorAll('.item');
const thumbnails = slider.querySelectorAll('.thumbnail .item');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

let activeIndex = 0;

function updateActiveSlide(index) {
    console.log('Updating to slide:', index);
    items.forEach(item => item.classList.remove('active'));
    thumbnails.forEach(thumb => thumb.classList.remove('active'));

    items[index].classList.add('active');
    thumbnails[index].classList.add('active');
}

prevBtn.addEventListener('click', () => {
    console.log('Prev button clicked');
    activeIndex = (activeIndex - 1 + items.length) % items.length;
    updateActiveSlide(activeIndex);
});

nextBtn.addEventListener('click', () => {
    console.log('Next button clicked');
    activeIndex = (activeIndex + 1) % items.length;
    updateActiveSlide(activeIndex);
});


thumbnails.forEach((thumb, index) => {
    thumb.addEventListener('click', () => {
        console.log('Thumbnail clicked:', index);
        activeIndex = index;
        updateActiveSlide(activeIndex);
    });
});


setInterval(() => {
    activeIndex = (activeIndex + 1) % items.length;
    updateActiveSlide(activeIndex);
}, 5000);


console.log('JS loaded, initializing slider');
updateActiveSlide(activeIndex);