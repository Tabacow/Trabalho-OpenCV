PEGUE O LINK DO VIDEO https://youtu.be/2EN6P3Z-t-A

O projeto tem intenção de automatizar o jogo CryptoBomb

Sobre o jogo:

CryptoBomb é um jogo lançado há pouco tempo, ele é um jogo de NFT que está em uma crescente
bem alta, no lançamento, 1 moeda do jogo (BCOIN) custava 0.18 doláres, no momento atual
(19/11/2021) a moeda está custando em torno de 6.5 doláres.

História e motivação:

Eu estava morrendo de preguiça de jogar este jogo, então propus para meu amigo Marcello
Scatena que criassemos um bot para jogar o jogo, desta maneira, criamos o projeto com
OpenCV. Além de me livrar de um fardo que é jogar este jogo (que é extramamente chato)
ele aumentou meu rendimento pois eu consigo obter lucros mesmo quando estou dormindo.
Meus lucros no jogo saltaram de 7 moedas/dia para 11 moedas/dia! Isso sem fazer nenhum
esforço!

O Bot está preparado para lidar com a maior parte de erros de gameplay sendo eles:
problema de WebSocket, problema de Timeout do servidor, problema Manual (não existe
motivo aparente para este erro), para problemas Unknown e entre outros.

Sobre o loop de gameplay:

O bot sempre começa por obter estados iniciais (tela de login, tela do menu do jogo e tela
de selecionar os heróis)

Em seguida, ele entra na lista de heróis e seleciona todos os heróis até conseguir obter
o estado de "trabalhando" em todos eles, ele faz isso através de um objeto chamado
"heroes". Se todos os heroes estiverem trabalhando, ele se direciona ao mapa do jogo,
onde os heroes irão trabalhar, ele se mantem no mapa por 1 hora, caso algum ocorra,
ele reloga no jogo e retoma de onde ele parou. Ao terminar o periodo do mapa do jogo,
ele volta ao menu e manda os heroes trabalharem novamente.

Sobre a visão computacional:

Foi usado OpenCV, a biblioteca é acessada na classe Vision.

Nessa classe, existe uma função chamada refresh_frame(), ela tem por função, atualizar a 
imagem que o objeto irá usar para comparação. Com a imagem atualizada, a função 
find_template() funciona como o "encontrador" da template fornecida a ele e retorna então
as coordenadas do primeiro pixel da template, tudo isso em grayscale.

Sobre controle de mouse e teclado:

na classe Controller nós temos tudo responsável por controlar clicks de mouse e teclado.



Obrigado por aceitar nosso trabalho mestre!
Ainda existem melhorias para serem feita no loop de gameplay, mas com o tempo nós iremos
atualizar o bot para tirar maior proveito dele! >:)

PEGUE O LINK DO VIDEO https://youtu.be/2EN6P3Z-t-A
