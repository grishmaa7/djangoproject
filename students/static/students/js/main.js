console.log("students/main.js loaded successfully!");

document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll("li");
    console.log(`Found ${items.length} student(s) on this page.`);
});