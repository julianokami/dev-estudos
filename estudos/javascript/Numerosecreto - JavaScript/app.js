alert('Bem vindo ao jogo do número secreto!');
let numeroMaximo = 5000
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1) ;
console.log(numeroSecreto); 
let palpite; 
let tentativas = 1;

//Enquanto o palpite for diferente do número secreto
while (palpite != numeroSecreto) {
    palpite = Number(prompt(`Escolha um número entre 1 e ${numeroMaximo}:`)); 
    if (palpite == numeroSecreto) {
        break;
    } else if (palpite > numeroSecreto) {
        alert(`O número secreto é menor que ${palpite}`);
    } else {
        alert(`O número secreto é maior que ${palpite}`);
    }
    // tentativas = tentativas + 1;
    tentativas++;
}

palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Muito bem! Você conseguiu descobrir o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`);






