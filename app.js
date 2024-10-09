// Step 1: get DOM elements
let ngoNextDom = document.getElementById('ngo-next');
let ngoPrevDom = document.getElementById('ngo-prev');

let ngoCarouselDom = document.querySelector('.ngo-carousel');
let ngoSliderDom = ngoCarouselDom.querySelector('.ngo-list');
let ngoThumbnailBorderDom = document.querySelector('.ngo-thumbnail');
let ngoThumbnailItemsDom = ngoThumbnailBorderDom.querySelectorAll('.ngo-item');
let ngoTimeDom = document.querySelector('.ngo-time');

// Append the first thumbnail to the end for looping
ngoThumbnailBorderDom.appendChild(ngoThumbnailItemsDom[0]);

let timeRunning = 3000; // Time for slider transition
let timeAutoNext = 7000; // Time for automatic transition

ngoNextDom.onclick = function () {
    showNgoSlider('next');    
}

ngoPrevDom.onclick = function () {
    showNgoSlider('prev');    
}

let runTimeOut;
let runNextAuto = setTimeout(() => {
    ngoNextDom.click();
}, timeAutoNext);

function showNgoSlider(type) {
    let ngoSliderItemsDom = ngoSliderDom.querySelectorAll('.ngo-item');
    let ngoThumbnailItemsDom = document.querySelectorAll('.ngo-thumbnail .ngo-item');
    
    if (type === 'next') {
        ngoSliderDom.appendChild(ngoSliderItemsDom[0]);
        ngoThumbnailBorderDom.appendChild(ngoThumbnailItemsDom[0]);
        ngoCarouselDom.classList.add('next');
    } else {
        ngoSliderDom.prepend(ngoSliderItemsDom[ngoSliderItemsDom.length - 1]);
        ngoThumbnailBorderDom.prepend(ngoThumbnailItemsDom[ngoThumbnailItemsDom.length - 1]);
        ngoCarouselDom.classList.add('prev');
    }
    
    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        ngoCarouselDom.classList.remove('next');
        ngoCarouselDom.classList.remove('prev');
    }, timeRunning);

    clearTimeout(runNextAuto);
    runNextAuto = setTimeout(() => {
        ngoNextDom.click();
    }, timeAutoNext);
}
