document.addEventListener("DOMContentLoaded", () => {

    const hero = document.querySelector(".hero");
    const heroSearch = document.querySelector(".hero-search input");
    const departmentCards = document.querySelectorAll(".department-card");

    // Department card click
    if (departmentCards.length > 0 && heroSearch) {

        departmentCards.forEach(card => {

            card.addEventListener("click", () => {

                const department = card.dataset.department;

                heroSearch.value = department;
                heroSearch.focus();

                window.scrollTo({
                    top: 0,
                    behavior: "smooth"
                });

            });

        });

    }

    // Hero animation
    if (hero) {

        hero.style.opacity = "0";
        hero.style.transform = "translateY(30px)";

        setTimeout(() => {

            hero.style.transition = "all .8s ease";
            hero.style.opacity = "1";
            hero.style.transform = "translateY(0)";

        }, 150);

    }


    // ==========================================
    //              Project Gallery
    // ==========================================

    const mainPreview = document.getElementById("mainPreview");
    const thumbnails = document.querySelectorAll(".thumbnail");

    if (mainPreview && thumbnails.length > 0) {

        thumbnails.forEach(thumbnail => {

            thumbnail.addEventListener("click", () => {

                mainPreview.src = thumbnail.src;

                thumbnails.forEach(img => {

                img.classList.remove("active");

            });

            thumbnail.classList.add("active");

            });

        });

    }
});