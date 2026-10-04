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

  const mainImage = document.getElementById("main-image");
  const galleryThumbnails = document.querySelectorAll(".gallery-thumb");

  if (mainImage && galleryThumbnails.length > 0) {
    galleryThumbnails.forEach((thumbnail) => {
      thumbnail.addEventListener("click", () => {
        mainImage.src = thumbnail.src;

        galleryThumbnails.forEach((image) => {
          image.classList.remove("active");
        });

        thumbnail.classList.add("active");
      });
    });
  }

  // ==========================================
  //          Report Preview Gallery
  // ==========================================

  const reportPreviewMainImage = document.getElementById(
    "reportPreviewMainImage",
  );

  const reportPreviewThumbnails = document.querySelectorAll(
    ".report-preview-thumbnail",
  );

  if (reportPreviewMainImage && reportPreviewThumbnails.length > 0) {
    reportPreviewThumbnails.forEach((thumbnail) => {
      thumbnail.addEventListener("click", () => {
        const imageSource = thumbnail.dataset.image;

        if (!imageSource) {
          return;
        }

        reportPreviewMainImage.src = imageSource;

        reportPreviewThumbnails.forEach((image) => {
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

      menuToggle.textContent = mobileMenu.classList.contains("active")
        ? "✕"
        : "☰";
    });

    document.querySelectorAll(".mobile-nav a").forEach((link) => {
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

  projectCards.forEach((card) => {
    card.addEventListener("click", (event) => {
      // Don't hijack clicks on actual links
      if (event.target.closest("a")) {
        return;
      }

      window.location.href = card.dataset.url;
    });
  });
});

//const backButton = document.getElementById("backButton");

//if (backButton) {
//backButton.addEventListener("click", (event) => {
//event.preventDefault();

//if (window.history.length > 1) {
//window.history.back();
//} else {
//window.location.href = "/";
//}
//});
//}

// ==========================================
//          Report Preview Modal
// ==========================================

let previewTrigger = null;

function openPreviewModal() {
  const modal = document.getElementById("reportPreviewModal");

  if (!modal) {
    return;
  }

  previewTrigger = document.activeElement;

  modal.removeAttribute("inert");
  modal.setAttribute("aria-hidden", "false");
  modal.classList.add("is-open");

  document.body.classList.add("preview-modal-open");

  const closeButton = modal.querySelector(".report-preview-close");

  if (closeButton) {
    closeButton.focus();
  }
}

function closePreviewModal() {
  const modal = document.getElementById("reportPreviewModal");

  if (!modal) {
    return;
  }

  modal.classList.remove("is-open");
  modal.setAttribute("aria-hidden", "true");
  modal.setAttribute("inert", "");

  document.body.classList.remove("preview-modal-open");

  if (previewTrigger && typeof previewTrigger.focus === "function") {
    previewTrigger.focus();
  }

  previewTrigger = null;
}

function changeReportPreview(button) {
  const mainImage = document.getElementById("reportPreviewMainImage");

  if (!mainImage || !button) {
    return;
  }

  const imageSrc = button.dataset.image;

  if (!imageSrc) {
    return;
  }

  mainImage.src = imageSrc;

  document
    .querySelectorAll(".report-preview-thumbnail")
    .forEach((thumbnail) => {
      thumbnail.classList.remove("active");
    });

  button.classList.add("active");
}

document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    closePreviewModal();
  }
});
