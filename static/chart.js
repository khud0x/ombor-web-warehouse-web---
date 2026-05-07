document.addEventListener("DOMContentLoaded", function () {

    if (!window.rawData || window.rawData.length === 0) {
        console.log("Data yo‘q");
        return;
    }

    // 🔥 DATA ajratish
    const labels = window.rawData.map(item => item[0]);
    const quantities = window.rawData.map(item => item[1]);
    const prices = window.rawData.map(item => item[2]);

    // =========================
    // 📊 1. MIQDOR GRAFIK (BAR)
    // =========================
    const ctx1 = document.getElementById('qtyChart');

    new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Miqdor (kg)',
                data: quantities,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // =========================
    // 💰 2. NARX GRAFIK (LINE)
    // =========================
    const ctx2 = document.getElementById('priceChart');

    new Chart(ctx2, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Narx (so‘m)',
                data: prices,
                tension: 0.3,
                fill: false
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

});