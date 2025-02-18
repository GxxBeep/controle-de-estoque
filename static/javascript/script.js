function open_menu() {
    let menu = document.querySelector(".menu-nav")
    if (menu.getAttribute("enable")) {
        menu.removeAttribute("enable")
    } else {
        menu.setAttribute("enable", "true")
    }
}
