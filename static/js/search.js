document.addEventListener("DOMContentLoaded", () => {

    const input = document.querySelector(".hero-search input");

    if (!input) return;

    const form = input.closest(".hero-search");

    const dropdown = document.createElement("div");

    dropdown.className = "search-dropdown";

    form.appendChild(dropdown);

    let timer;

    input.addEventListener("input", () => {

        clearTimeout(timer);

        const query = input.value.trim();

        if(query.length < 2){

            dropdown.style.display = "none";

            dropdown.innerHTML = "";

            return;

        }

        dropdown.innerHTML = `

        <div class="search-loading">

        Searching...

        </div>

        `;

        dropdown.style.display="block";

        timer = setTimeout(async ()=>{

            const response = await fetch(`/search-api?q=${encodeURIComponent(query)}`);

            const results = await response.json();

            if(results.length===0){

                dropdown.innerHTML='<div class="search-empty">No projects found.</div>';

                dropdown.style.display='block';

                return;

            }

            dropdown.innerHTML = results.map(project => {

                const regex = new RegExp(`(${query})`, "ig");

                const highlightedTitle = project.title.replace(
                    regex,
                    "<mark>$1</mark>"
                );

                return `

            <a href="/projects/${project.slug}" class="search-item">

                <div class="search-icon">

                    <i class="fa-solid fa-file-lines"></i>

                </div>

                <div class="search-content">

                    <strong>${highlightedTitle}</strong>

                    <span>

                    ${project.department}

                    •

                    ${project.technology}

                    </span>

                </div>

            </a>

            `;

            }).join("");

            dropdown.innerHTML += `

            <a class="search-view-all"

            href="/search?search=${encodeURIComponent(query)}">

            View all matching projects →

            </a>

            `;

            dropdown.style.display="block";

        },250);

    });

    document.addEventListener("click",(e)=>{

        if(!form.contains(e.target)){

            dropdown.style.display="none";

        }

    });

});