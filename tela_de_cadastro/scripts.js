    // Máscara de CPF
    document.getElementById('cpf').addEventListener('input', function (e) {
        let cpf = e.target.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (cpf.length > 9) {
            cpf = cpf.slice(0, 3) + '.' + cpf.slice(3, 6) + '.' + cpf.slice(6, 9) + '-' + cpf.slice(9, 11); // Formata com pontos e hífen
        } else if (cpf.length > 6) {
            cpf = cpf.slice(0, 3) + '.' + cpf.slice(3, 6) + '.' + cpf.slice(6, 9); // Adiciona os pontos
        } else if (cpf.length > 3) {
            cpf = cpf.slice(0, 3) + '.' + cpf.slice(3, 6); // Primeiro ponto
        }
        e.target.value = cpf; // Atualiza o valor do input
    });

    // Máscara de Telefone
    document.getElementById('phone').addEventListener('input', function (e) {
        let phone = e.target.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (phone.length > 10) {
            phone = '(' + phone.slice(0, 2) + ') ' + phone.slice(2, 7) + '-' + phone.slice(7, 11); // Formata telefone com 9 dígitos
        } else if (phone.length > 6) {
            phone = '(' + phone.slice(0, 2) + ') ' + phone.slice(2, 6) + '-' + phone.slice(6, 10); // Formata telefone com 8 dígitos
        } else if (phone.length > 2) {
            phone = '(' + phone.slice(0, 2) + ') ' + phone.slice(2, 6); // Adiciona parênteses e parte do número
        }
        e.target.value = phone; // Atualiza o valor do input
    });

    // Máscara de CEP
    document.getElementById('inputCep').addEventListener('input', function (e) {
        let cep = e.target.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (cep.length > 5) {
            cep = cep.slice(0, 5) + '-' + cep.slice(5, 8); // Adiciona o hífen
        }
        e.target.value = cep; // Atualiza o valor do input
    });

    // Seleciona os elementos do DOM
const toggleSenha = document.querySelector("#toggleSenha");
const senhaInput = document.querySelector("#senha");
const iconOlho = document.querySelector("#iconOlho");

// Adiciona o evento de clique para alternar a visualização da senha
toggleSenha.addEventListener("click", function () {
    // Alterna o tipo do input de "password" para "text" ou vice-versa
    const tipo = senhaInput.getAttribute("type") === "senha" ? "text" : "senha";
    senhaInput.setAttribute("type", tipo);

    // Alterna o ícone entre "fa-eye" e "fa-eye-slash"
    iconOlho.classList.toggle("fa-eye-slash");
});
