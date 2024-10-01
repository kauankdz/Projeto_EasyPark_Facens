// Máscara de CPF
document.getElementById('cpf').addEventListener('input', function (e) {
    let cpf = e.target.value.replace(/\D/g, '');
    if (cpf.length > 9) {
        cpf = cpf.slice(0, 3) + '.' + cpf.slice(3, 6) + '.' + cpf.slice(6, 9) + '-' + cpf.slice(9, 11);
    } else if (cpf.length > 6) {
        cpf = cpf.slice(0, 3) + '.' + cpf.slice(3, 6) + '.' + cpf.slice(6, 9);
    } else if (cpf.length > 3) {
        cpf = cpf.slice(0, 3) + '.' + cpf.slice(3, 6);
    }
    e.target.value = cpf;
});

// Máscara de Telefone
document.getElementById('phone').addEventListener('input', function (e) {
    let phone = e.target.value.replace(/\D/g, '');
    if (phone.length > 10) {
        phone = '(' + phone.slice(0, 2) + ') ' + phone.slice(2, 7) + '-' + phone.slice(7, 11);
    } else if (phone.length > 6) {
        phone = '(' + phone.slice(0, 2) + ') ' + phone.slice(2, 6) + '-' + phone.slice(6, 10);
    } else if (phone.length > 2) {
        phone = '(' + phone.slice(0, 2) + ') ' + phone.slice(2, 6);
    }
    e.target.value = phone;
});

// Máscara de CEP
document.getElementById('inputCep').addEventListener('input', function (e) {
    let cep = e.target.value.replace(/\D/g, '');
    if (cep.length > 5) {
        cep = cep.slice(0, 5) + '-' + cep.slice(5, 8);
    }
    e.target.value = cep;
});

//icon de visualizar a senha
    // Seleciona os elementos do DOM
    const toggleSenha = document.querySelector("#toggleSenha");
    const senhaInput = document.querySelector("#senha");
    const iconOlho = document.querySelector("#iconOlho");

    // Adiciona o evento de clique para alternar a visualização da senha
    toggleSenha.addEventListener("click", function () {
        // Alterna o tipo do input de "password" para "text" ou vice-versa
        const tipo = senhaInput.getAttribute("type") === "password" ? "text" : "password";
        senhaInput.setAttribute("type", tipo);

        // Alterna o ícone entre "fa-eye" e "fa-eye-slash"
        iconOlho.classList.toggle("fa-eye");
        iconOlho.classList.toggle("fa-eye-slash");
    });
