document.addEventListener('DOMContentLoaded', function () {
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    let slideIndex = 0;

    function updateSlider() {
      slider.style.transform = `translateX(-${slideIndex * 100}%)`;
    }


    nextBtn.addEventListener('click', () => {
        slideIndex = (slideIndex + 1) % slides.length;
        updateSlider();
    });

    prevBtn.addEventListener('click', () => {
        slideIndex = (slideIndex - 1 + slides.length) % slides.length;
        updateSlider();
    });

   //Autoplay the slider
   function autoSlide(){
    slideIndex = (slideIndex + 1) % slides.length;
     updateSlider();
   }
   setInterval(autoSlide, 5000); // Change slide every 5 seconds (5000ms)
});