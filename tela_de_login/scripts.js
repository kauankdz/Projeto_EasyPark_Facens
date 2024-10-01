// Seleciona os elementos do DOM
const toggleSenha = document.querySelector("#toggleSenha");
const senhaInput = document.querySelector("#password");
const iconOlho = document.querySelector("#iconOlho");

// Função para alternar a visualização da senha
function alternarVisualizacaoSenha() {
    toggleSenha.addEventListener("click", function () {
        const tipo = senhaInput.getAttribute("type") === "password" ? "text" : "password";
        senhaInput.setAttribute("type", tipo);

        iconOlho.classList.toggle("fa-eye-slash");
    });
}

// Função principal para inicializar todas as funções de manipulação
function inicializarFormulario() {
    alternarVisualizacaoSenha();
}

// Inicializa o formulário assim que a página carregar
document.addEventListener('DOMContentLoaded', inicializarFormulario);
