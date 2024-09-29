// Seleciona os elementos do DOM
const toggleSenha = document.querySelector("#toggleSenha");
const senhaInput = document.querySelector("#password");
const iconOlho = document.querySelector("#iconOlho");

// Adiciona o evento de clique para alternar a visualização da senha
toggleSenha.addEventListener("click", function () {
    // Alterna o tipo do input de "password" para "text" ou vice-versa
    const tipo = senhaInput.getAttribute("type") === "password" ? "text" : "password";
    senhaInput.setAttribute("type", tipo);

    // Alterna o ícone entre "fa-eye" e "fa-eye-slash"
    iconOlho.classList.toggle("fa-eye-slash");
});
