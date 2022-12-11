

const init = () => {

    const inputEmail = document.querySelector('input[name="email"]');
    const inputSenha = document.querySelector('input[name="senha"]');
    const submitButton = document.querySelector('.login_submit');



    console.log('init');
    console.log('nome: ' + inputEmail);
    console.log('senha: ' + inputSenha);
}


window.onload = init;
