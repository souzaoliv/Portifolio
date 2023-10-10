window.onhashchange = function(e){
    const oldURL= e.oldURL.split('#')[1]
    const newURL= e.newURL.split('#')[1]
    const oldLINk = document.querySelector(`.nav-list a[href='#${oldURL}']`)
    const newLINk = document.querySelector(`.nav-list a[href='#${newURL}']`)
    oldLINk && oldLINk.classList.remove('selected')
    newLINk && newLINk.classList.add('selected') 

}


function menuShow() {
    let menuMobile = document.querySelector('.mobile-menu');
    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
        document.querySelector('.icon').src = "statics/IMG/menu.svg";
    } else {
        menuMobile.classList.add('open');
        document.querySelector('.icon').src = "statics/IMG/close-menu.svg";
    }
}

