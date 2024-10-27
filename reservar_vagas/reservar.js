
 
        // Função para mostrar/esconder o formulário de reserva
        function mostrarFormulario(btn) {
            const form = btn.nextElementSibling;
            if (form.style.display === "none") {
                form.style.display = "block";
            } else {
                form.style.display = "none";
            }
        }

        // Função para filtrar os cards de acordo com a busca
        function filterCards() {
            const searchInput = document.getElementById('searchInput').value.toLowerCase();
            const cards = document.getElementsByClassName('vaga-card');

            for (let i = 0; i < cards.length; i++) {
                const location = cards[i].getAttribute('data-location').toLowerCase();
                if (location.includes(searchInput)) {
                    cards[i].style.display = '';
                } else {
                    cards[i].style.display = 'none';
                }
            }
        }

   
       // Função para exibir o formulário de informações do veículo
        function mostrarFormulario(button) {
            const formCarro = button.parentElement.querySelector('.formulario-carro');
            formCarro.style.display = "block";
        }

        // Função para abrir o modal de vagas
        function abrirModal() {
            $('#vagasModal').modal('show');  // Mostra o modal usando Bootstrap
        }

        // Função para confirmar as vagas
        function confirmarVagas() {
            const checkboxes = document.querySelectorAll('#vagasForm input[type="checkbox"]:checked');
            let vagasSelecionadas = [];
            
            checkboxes.forEach((checkbox) => {
                vagasSelecionadas.push(checkbox.value);
            });

            if (vagasSelecionadas.length > 0) {
                alert("Vagas selecionadas: " + vagasSelecionadas.join(", "));
                $('#vagasModal').modal('hide');
            } else {
                alert("Por favor, selecione ao menos uma vaga.");
            }
        }