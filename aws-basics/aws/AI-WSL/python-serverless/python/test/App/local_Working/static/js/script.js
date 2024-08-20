document.addEventListener('DOMContentLoaded', (event) => {
    const colors = ['#F0E68C', '#FFD700', '#98FB98', '#FF69B4', '#87CEFA']; // Khaki, Gold, PaleGreen, HotPink, LightSkyBlue
    let currentIndex = 0;

    function changeBackgroundColor() {
        document.body.style.backgroundColor = colors[currentIndex];
        currentIndex = (currentIndex + 1) % colors.length;
    }

    setInterval(changeBackgroundColor, 400); // Change every 3 seconds
});
