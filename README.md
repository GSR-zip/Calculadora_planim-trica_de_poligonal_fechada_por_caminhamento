ENGLISH
I took a Fundamental Topography course during college, where I learned how to identify and correct angular and linear errors in various types of horizontal traverses (such as open/closed traverses, radiation, supported traverses, and calculating areas using analytical methods), as well as defining coordinate points. Calculating all of this by hand is extremely tedious and inefficient. At the time, the AIs I tried couldn't handle the math (they would get lost in the process), which inspired me to create a "complete software" to solve any topographic problem.
However, I only ended up building a tiny fraction of what I originally imagined for the program. Even so, it helped me tremendously with the calculations and with learning how to code. Since I’ve passed the course and am no longer using this script, I am making it publicly available. If you are reading this and want to use, modify, improve, or continue developing it, please feel free! If you need any help, you can count on me (it would be amazing to see this project fully completed).

⚠️ Important Note on Code Structure:
The section labeled primeira_versao (first_version) works, but it is completely unreadable. It was the literal first piece of code I ever wrote in my life. A more experienced developer who reviewed it to give me feedback actually asked if I hated programmers! So, I highly recommend not wasting your energy trying to decipher that specific part. At the very end of the file, you will find some sample angles and distances that you can use for testing.
How the program works:
It calculates the X and Y coordinates of a horizontal traverse and its total area through the following steps:
    • Data Input: You can input angles and distances either by copying and pasting or by typing them manually.
    • Linear Tolerance: Enter the allowable linear error ratio (e.g., 1:1000, 1:2000), which depends on the size of the surveyed land.
    • Instrument Tolerance: Input the angular error tolerance specified by the manufacturer of the surveying equipment.
    • Measurement Type: Choose between interior or exterior angles. The program uses this to calculate the angular error, find the difference between the ideal and measured values, and check it against the tolerance.
    • Azimuth Distribution: Once corrected, the program distributes the azimuths (the angle relative to North or an arbitrary direction, used to find the sine and cosine for X and Y coordinates).
    • Provisional Coordinates: The system calculates temporary coordinates using the azimuths and distances.
    • Initial Coordinates: The user provides the starting coordinates (useful if you are within a plot and need to locate a specific point).
    • Area Calculation: Finally, the program computes the total area based on these coordinates.
Future Roadmap / Ideas for continuation:
    • Vertical Surveying (Altimetry): This is quite simple in theory. The horizontal distance used in the current calculation would result from: horizontal_distance = measured_distance * cos(vertical_angle). The elevation would be: provisional_z = measured_distance * sin(vertical_angle). For vertical adjustment: correction = (final_elevation - initial_elevation) / number_of_stations, leading to final_z = provisional_z + correction.
    • Radiation Points: Implementing a specific feature for radiation points, though the current tools already provide a solid foundation.
    • Graphical User Interface (GUI): I tried creating a user interface but couldn't quite get it to work (lol), so a proper GUI would be a great addition.


PORTUGÊS
Passei pela matéria de topografia fundamental durante a faculdade, onde aprendi a encontrar e corrigir os erros angulares e distâncias de alguns tipos de poligonais planimétrica (por caminhamento, irradiação, suas áreas pelo método analítico, poligonal apoiada, entre outras) e definir a coordenada de seus pontos.
Calculá-las à mão é extremamente trabalhoso e ineficiente, e na época as IAs que usei não conseguiam calcular (elas se perdiam no processo), por isso pensei em fazer um "softwere completo" para calcular qualquer problema topográfico.
  
No em tando fiz uma ínfima parcela do total que imaginei para o programa (que me ajudou muito com as contas e a entender mais sobre programação) mas eu passei na matéria e não estou usando mais este código... portanto eu a deixo disponível publicamente. Se você que está lendo isso quiser usar, modificar, melhorar ou continuar fique à vontade e se precisar de ajuda conta comigo (seria bonito ver isso aqui inteiro).
De qualquer forma, o programa funciona assim:

Calcula as coordenadas x e y de uma poligonal planimétrica e sua área.

1-> Entrada de dados, onde serão fornecidos os ângulos e as distâncias (ela pode ser por cópia e cola ou digitando cada um manualmente);
2-> Fornecer a tolerância linear (dependendo do tamanho do terreno que você ira medir ele segue uma regra da tolerância do quanto o erro é aceitável 1:1000, 1:2000…);
3-> Fornecer a tolerância do aparelho: os aparelhos topográficos possuem uma tolerância do erro de leitura de seus ângulos (isso vem de fábrica e tem em todos os aparelhos uns mais precisos e outros menos);
4-> escolhe o tipo de medição (utilizando ângulos internos ou externos), ela serve para calcular o erro angular, calcular a diferença entre o ideal e o que foi medido e em seguida compara com a tolerância;
5-> Feita a correção o programa vai espalhar os azimutes (o ângulo em relação ao norte (ou uma direção arbitrária por onde obtemos o seno e o cosseno para as coordenadas x e y respectivamente);
6-> Com os azimutes e distâncias o programa calcula as coordenadas provisórias
7-> O usuário fornece as coordenadas iniciais (se tiver dentro de um terreno e quiser locar num ponto específico por exemplo).
8 -> A partir disso ele calcula a área

Para uma continuação pensei em adicionar ao programa a altimetria (é bem simples na teoria: a distância usada na conta atual seria resultado de uma outra conta [distancia * cos (ângulo_vertical) = distancia_usada_no_programa_atual] e a altura seria [distancia_medida * sen(angulo_vertical) = z_provisorio] e uma validação de altura (altura_final – altura inicial)/numero_de_estações = correção, z_final = correção + z_provisorio.

Adicionar pontos para ser irradiação (teria que fazer uma específica mas creio que com as ferramentas daqui de pra avançar bem
e possivelmente uma interface (tentei criar e não consegui lol)

to test:
----------------\\----------------
input:
1 - import

215.32.00;56.57 288.54.00;60.83 287.06.00;60.75 142.07.00;44.72 326.19.00;51.01

angle;distance angle;distance

tolerance:
2.00.00 (don't use 2°00'00")

angles:
1 - external angles

initial azimute:
you choose (exemple: 00.00.00)

linear tolerance:
1/100

coordenate x and y initial
you choose (0 for exemple)
----------------\\----------------
output:
coordenates and area