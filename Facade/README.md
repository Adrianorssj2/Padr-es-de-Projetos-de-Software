# Facade


É um padrão que simplifica a interface de um ou mais subsistemas complexos, fornecendo uma interface unificada para o cliente.


- Exercício 1: Considere uma classe Cliente que precisa interagir com uma classe BaseDeDados
para efetuar operações de cadastro, recuperação, atualização e remoção de
instâncias de uma classe Modelo que possui vários Elementos. O Cliente precisa
estabelecer uma conexão como a BaseDeDados receber uma instância de uma
classe Conexão e a partir da Conexão efetuar as operações desejadas. Forneça uma
solução utilizando padrões que simplifique a interação do Cliente com as demais
classes deste subsistema;
- Exercício 2: Suponha que você deseja construir seu proprio home theater. O sistema contém
uma TV, um som sorround, aparelhagem de DVD e um sintonizador para TV a cabo
ou canais abertos. A TV tem as opções de ligar, desligar, controle de volume e
escolha da entrada do sinal (DVD ou Sintonizador de TV). O Sistema de som
surround tem as opções de Entrada (DVD ou Sintonizador de TV), controle de
volume. Ligar estereo ou mono. O sintonizador de TV tem as opções de canais (AR
ou Cabo) e opçoes de liga e desliga. Você deseja que o controle do seu sistema
home theater seja feito de maneira automatizada por meio de um controle remoto.