const DOMSelectors = {
  displayContainer: document.querySelector(".menu-container"),
  themeBtn: document.querySelector(".theme-btn"),
  lightBtn: document.querySelector(".light-theme-btn"),
  darkBtn: document.querySelector(".dark-theme-btn"),
  body: document.querySelector("body"),
};

DOMSelectors.darkBtn.addEventListener("click", function () {
  if (DOMSelectors.body.classList.contains("light")) {
    DOMSelectors.body.classList.remove("light");
    DOMSelectors.body.classList.add("dark");
  } else {
    DOMSelectors.body.classList.add("dark");
  }
});
DOMSelectors.lightBtn.addEventListener("click", function () {
  if (DOMSelectors.body.classList.contains("dark")) {
    DOMSelectors.body.classList.remove("dark");
    DOMSelectors.body.classList.add("light");
  } else {
    DOMSelectors.body.classList.add("light");
  }
});
