document.addEventListener("DOMContentLoaded",()=>{

const hero=document.querySelector(".hero");

const departmentCards = document.querySelectorAll(".department-card");

const heroSearch = document.querySelector(".hero-search input");

departmentCards.forEach(card=>{

card.addEventListener("click",()=>{

const department = card.dataset.department;

heroSearch.value = department;

heroSearch.focus();

window.scrollTo({

top:0,

behavior:"smooth"

});

});

});

hero.style.opacity="0";

hero.style.transform="translateY(30px)";

setTimeout(()=>{

hero.style.transition="all .8s ease";

hero.style.opacity="1";

hero.style.transform="translateY(0)";

},150);

}
)
;