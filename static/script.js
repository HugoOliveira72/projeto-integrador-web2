const formLogin = document.getElementById("formLogin");
const error = document.getElementById("error");


if (formLogin && error) {
    formLogin.addEventListener("submit", function fazerLogin(evento) {
        //Guarda o valor do input senha
        const senha = document.getElementById("senha").value;
        let mensagemErro = "";

        //Tamanho min da senha eh 6 e max 20
        if(senha.length <6) {
            mensagemErro = "A senha deve ter pelo menos 6 caracteres.";
        } else if (senha.length > 20) {
            mensagemErro = "A senha não pode ter mais de 20 caracteres.";
        }


        error.textContent = mensagemErro;
        // temos que criar esse evento
        //if (mensagemErro) {
          //  evento.preventDefault();
        //}

    });
}
