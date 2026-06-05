const toggle = document.getElementById("modeToggle");

toggle.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");

    // Change icon
    toggle.textContent =
        document.body.classList.contains("light-mode")
            ? "🌙︎︎︎"
            : "☀";
});