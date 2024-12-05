async function updateChart() {
    const response = await fetch('/data');
    const users = await response.json();

    const ctx = document.getElementById('userChart').getContext('2d');
    const userChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: users.map(user => user.id),
            datasets: [{
                label: 'Usuários',
                data: users.map(user => user.id),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Atualiza o gráfico automaticamente quando a página é carregada
    setTimeout(updateChart, 5000); // Atualiza a cada 5 segundos
}
