    // Dados fictícios das reservas (para exemplo)
    const reservas = [
        { vaga: 'A-12', data: '2024-11-01', horario: '08:00 - 18:00', local: 'Estacionamento Central' },
        { vaga: 'B-07', data: '2024-11-05', horario: '09:00 - 17:00', local: 'Shopping Center' },
        { vaga: 'C-03', data: '2024-11-10', horario: '08:00 - 20:00', local: 'Aeroporto' }
    ];

    // Função para renderizar as reservas
    function renderizarReservas() {
        const container = document.getElementById('reservas-container');
        container.innerHTML = ''; // Limpa o conteúdo anterior

        reservas.forEach(reserva => {
            const card = document.createElement('div');
            card.classList.add('col-md-4', 'mb-4');
            card.innerHTML = `
                <div class="card text-dark bg-light">
                    <div class="card-body">
                        <h5 class="card-title">Vaga: ${reserva.vaga}</h5>
                        <p class="card-text">Data: ${reserva.data}</p>
                        <p class="card-text">Horário: ${reserva.horario}</p>
                        <p class="card-text">Local: ${reserva.local}</p>
                        <button class="btn btn-danger btn-block">Cancelar Reserva</button>
                    </div>
                </div>
            `;
            container.appendChild(card);
        });
    }

    // Chama a função ao carregar a página
    document.addEventListener('DOMContentLoaded', renderizarReservas);
