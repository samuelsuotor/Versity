document.addEventListener("DOMContentLoaded", () => {

    // ==========================================
    //              Hero Animation
    // ==========================================

    const hero = document.querySelector(".hero");

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

                thumbnails.forEach(image => {

                    image.classList.remove("active");

                });

                thumbnail.classList.add("active");

            });

        });

    }


    // ==========================================
    //              Mobile Navigation
    // ==========================================

    const menuToggle = document.getElementById("menuToggle");
    const mobileMenu = document.getElementById("mobileMenu");

    if (menuToggle && mobileMenu) {

        menuToggle.addEventListener("click", () => {

            mobileMenu.classList.toggle("active");

            document.body.classList.toggle("menu-open");

            menuToggle.textContent =
                mobileMenu.classList.contains("active")
                    ? "✕"
                    : "☰";

        });

        document.querySelectorAll(".mobile-nav a").forEach(link => {

            link.addEventListener("click", () => {

                mobileMenu.classList.remove("active");

                document.body.classList.remove("menu-open");

                menuToggle.textContent = "☰";

            });

        });

        document.addEventListener("click", (event) => {

            if (

                mobileMenu.classList.contains("active") &&

                !mobileMenu.contains(event.target) &&

                !menuToggle.contains(event.target)

            ) {

                mobileMenu.classList.remove("active");

                document.body.classList.remove("menu-open");

                menuToggle.textContent = "☰";

            }

        });

    }

    // ==========================================
    //          Clickable Project Cards
    // ==========================================

    const projectCards = document.querySelectorAll(".project-card");

    projectCards.forEach(card => {

        card.addEventListener("click", (event) => {

            // Don't hijack clicks on actual links
            if (event.target.closest("a")) {
                return;
            }

            window.location.href = card.dataset.url;

        });

    });

});

const backButton = document.getElementById("backButton");

if (backButton) {

    backButton.addEventListener("click", (event) => {

        event.preventDefault();

        if (window.history.length > 1) {

            window.history.back();

        } else {

            window.location.href = "/";

        }

    });

}