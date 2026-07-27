document.addEventListener("DOMContentLoaded",()=>{

const hero=document.querySelector(".hero");

hero.style.opacity="0";

hero.style.transform="translateY(30px)";

setTimeout(()=>{

hero.style.transition="all .8s ease";

hero.style.opacity="1";

hero.style.transform="translateY(0)";

},150);

});