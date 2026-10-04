function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector(".hero-search input");

  if (!input) return;

  const form = input.closest(".hero-search");

  const dropdown = document.createElement("div");

  dropdown.className = "search-dropdown";

  form.appendChild(dropdown);

  let timer;
  let searchRequestId = 0;

  input.addEventListener("input", () => {
    clearTimeout(timer);

    const query = input.value.trim();

    if (query.length < 2) {
      dropdown.style.display = "none";

      dropdown.innerHTML = "";

      return;
    }

    dropdown.innerHTML = `

        <div class="search-loading">

        Searching...

        </div>

        `;

    dropdown.style.display = "block";

    const requestId = ++searchRequestId;

    timer = setTimeout(async () => {
      try {
        const response = await fetch(
          `/search-api?q=${encodeURIComponent(query)}`,
        );

        if (!response.ok) {
          throw new Error("Search request failed");
        }

        const results = await response.json();

        if (requestId !== searchRequestId) {
          return;
        }

        if (!response.ok || !Array.isArray(results)) {
          throw new Error("Search request failed");
        }

        if (results.length === 0) {
          dropdown.innerHTML =
            '<div class="search-empty">No projects found.</div>';

          dropdown.style.display = "block";

          return;
        }

        dropdown.innerHTML = results
          .map((project) => {
            const escapedQuery = query.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
            const regex = new RegExp(`(${escapedQuery})`, "ig");

            const safeTitle = escapeHtml(project.title);
            const highlightedTitle = safeTitle.replace(
              regex,
              "<mark>$1</mark>",
            );

            return `

            <a href="/projects/${project.slug}" class="search-item">

                <div class="search-icon">

                    <i class="fa-solid fa-file-lines"></i>

                </div>

                <div class="search-content">

                    <strong>${highlightedTitle}</strong>

                    <span>

                    ${escapeHtml(project.department)}
                    •
                    ${escapeHtml(project.technology)}

                    </span>

                </div>

            </a>

            `;
          })
          .join("");

        dropdown.innerHTML += `

            <a class="search-view-all"

            href="/search?search=${encodeURIComponent(query)}">

            View all matching projects →

            </a>

            `;

        dropdown.style.display = "block";
      } catch (error) {
        console.error("Search error:", error);

        dropdown.innerHTML =
          '<div class="search-empty">Unable to search right now. Please try again.</div>';

        dropdown.style.display = "block";
      }
    }, 250);
  });

  document.addEventListener("click", (e) => {
    if (!form.contains(e.target)) {
      dropdown.style.display = "none";
    }
  });
});
