from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product

home_bp = Blueprint('home', __name__)

categories = [Category(1, "Eletrônicos"), Category(2, "Jogos"), Category(3, "Lojas")]
products = [
    Product(1, "Helldrivers", 189.99, 2, "MERGULHE NA LUTA PELA LIBERDADE: nós precisamos de cidadãos corajosos o bastante para viajar pela Galáxia a fim de libertar mundos hostis e imprevisíveis e espalhar a nossa mensagem de paz, liberdade e democracia gerenciada através de missões ferozes, frenéticas e velozes. TORNE-SE UMA LENDA: como parte das forças de elite, todo o poderio militar da Superterra estará à sua disposição. Progrida na hierarquia completando missões vitais, mudando os rumos da batalha e protegendo o fronte. A GUERRA GALÁCTICA: campanhas são enfrentadas, vencidas e perdidas conforme a Guerra Galáctica se alastra em múltiplas frentes. Nossos inimigos sem pátria procuram frustrar cada passo nosso, mas não deixaremos de lutar até que todos os seres provem da Liberdade!.", [
        "https://blog.br.playstation.com/tachyon/sites/4/2024/01/3e6c953a579f738f5c6126e25deec10d17c444b0.jpeg?resize=1088%2C612&crop_strategy=smart",
    ]),
    Product(2, "Elden Ring", 345.50, 2, "O NOVO RPG DE AÇÃO E FANTASIA. Levante-se, Maculado, e seja guiado pela graça para portar o poder do Anel Prístino e se tornar um Lorde Prístino nas Terras Intermédias. • Um mundo vasto e emocionante Um mundo vasto onde campos abertos e uma variedade de situações e masmorras imensas, com complexos designs tridimensionais se conectam com fluidez. Conforme explora, sinta a alegria de descobrir poderosas e desconhecidas ameaças que aguardam por você, levando a um grande senso de conquista. • Crie seu próprio personagem Além de personalizar a aparência do seu personagem, você pode combinar livremente armas, armaduras e magias que equipar. Você pode desenvolver seu personagem de acordo com seu estilo de jogo, como aumentar a força muscular para se tornar um poderoso guerreiro, ou dominar a magia. • Um drama épico nascido de um mito Uma história cheia de camadas, contada em fragmentos. Um drama épico onde os vários pensamentos dos personagens se interligam nas Terras Intermédias. • Jogo on-line único que conecta você livremente aos outros Além do multijogador, onde você pode se conectar diretamente com outros jogadores e viajarem juntos, o jogo suporta um elemento on-line assíncrono único que permite que você sinta a presença dos outros..", [
        "https://upload.wikimedia.org/wikipedia/pt/0/0d/Elden_Ring_capa.jpg",
    ]),
    Product(3, "Ghost of Tsushima", 299.95, 2, "Descubra as maravilhas ocultas de Tsushima nesse jogo de ação e aventura em mundo aberto da Sucker Punch Productions e do PlayStation Studios, disponível para PS5 e PS4. Forje um novo caminho e trave uma guerra atípica pela liberdade de Tsushima. Desafie oponentes com sua katana, domine o arco para eliminar ameaças distantes, desenvolva táticas furtivas para emboscar inimigos e explore uma nova história na Ilha Iki.", [
        "https://cdn1.epicgames.com/offer/6e6aa039c73347b885803de65ac5d3db/EGS_GhostofTsushima_SuckerPunchProductions_S2_1200x1600-e23e02c1d70be7b528dba50860f87d39",
    ]),
    Product(4, "Fallout 76", 39.99, 2, "Vinte e cinco anos após as bombas caírem, você e seus colegas habitantes do Refúgio emergem nos Estados Unidos de um período pós-nuclear. Trabalhe em equipe (ou não) para sobreviver. Sob a ameaça constante de aniquilação nuclear, você vai conhecer o maior e mais dinâmico mundo já criado no universo lendário de Fallout.", [
        "https://upload.wikimedia.org/wikipedia/pt/0/06/Fallout_76_cover.jpg",
    ]),
    Product(5, "Watch Dogs Legion", 249.99, 2, "Constrói uma resistência com praticamente qualquer pessoa que encontras na rua, à medida que fazes hacking, te infiltras e lutas para recuperar a Londres de um futuro próximo que está à beira da ruína.", [
        "https://cdn1.epicgames.com/0a84818055e740a7be21a2e5b6162703/offer/WatchDogs_Legion_Store_Portrait_1200x1600-1200x1600-a6b2d4cce489aeeb87bad4a6db168bed.jpg",
    ]),
    Product(6, "Minecraft", 99.90, 2, "Em Minecraft: Java and Bedrock Edition você explora mundos gerados aleatoriamente e constroi coisas incríveis, desde casas mais simples até grandiosos castelos. Com o Minecraft: Java e Bedrock Edition, é possível alternar facilmente entre jogos com o iniciador unificado e o cross play em qualquer versão atual do Minecraft. Jogue no modo criativo com recursos ilimitados ou minere as profundezas do mundo no modo sobrevivência, criando armas e armaduras para afastar criaturas perigosas. Escale montanhas íngremes, encontre cavernas complexas e extraia grandes veios de minério. Descubra biomas de cavernas verdejantes e com espeleotemas. Ilumine seu mundo com velas para mostrar que você sabe tudo sobre espeleologia e alpinismo!.", [
        "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQfF1AmOwNQsQilYdRF4jVOFh2mkhET8N7AewIe_hCcw5RzkVIl-0aZyWErweQNLqnHn2lUm5cS2JI-fwh0cScALZGNC_dHorkV-E53kPuf2Td43qsqwtzFkA&usqp=CAE",
    ]),
    Product(7, "Controle Xbox", 374.90, 1, "Conecte-se, jogue e alterne rapidamente entre dispositivos, incluindo Xbox Series X|S, Xbox One, PC com Windows 10, telefones e tablets compatíveis. Compatível com dispositivos selecionados e versões de sistema operacional. Algumas funcionalidades não são suportadas no Android via Bluetooth", [
        "https://cgngamesbh.com.br/product_images/o/590/Controle_Xbox_One_S_Preto__82958_zoom.jpg",
    ]),
    Product(8, "Console Xbox Series X", 4129.99, 1, "Desfrute de jogos 4K a até 120 quadros por segundo, som 3D avançado especial e muito mais 4K a 120 FPS: requer conteúdo e exibição compatíveis Versão X - com leitor de disco", [
        "https://assets.xboxservices.com/assets/bc/40/bc40fdf3-85a6-4c36-af92-dca2d36fc7e5.png?n=642227_Hero-Gallery-0_A1_857x676.png",
    ]),
    Product(9, "Console Play Station 5", 3629.99, 1, "Domine o poder de uma CPU e GPU personalizadas e o SSD com E/S integradas que redefinem as regras do que o console PlayStation pode fazer. Maravilhe-se com os gráficos incríveis e experimente os recursos do novo PS5.", [
        "https://images.kabum.com.br/produtos/fotos/238671/console-sony-playstation-5_1634132556_g.jpg",
    ]),
    Product(10, "controle Play Station 5", 359.50, 1, "Sinta o feedback fisicamente responsivo às suas ações no jogo com atuadores duplos que substituem os motores tradicionais. Em suas mãos, essas vibrações dinâmicas podem simular a sensação de tudo, desde ambientes até o recuo de diferentes armas. Experimente vários níveis de força e tensão conforme você interage com o equipamento e os ambientes do jogo.", [
        "https://i.zst.com.br/thumbs/12/39/f/1190230696.jpg",
    ]),
    Product(11, "Gabinete Gamer", 559.50, 1, "Apresentamos o Zeus V2, um gabinete gamer de alto desempenho. Com dimensões imponentes e design deslumbrante em vidro, o Zeus V2 oferece espaço interno amplo para configurações poderosas. Compatível com placas-mãe ATX, Micro e ITX, possui suporte para HDD e SSDs, além de slots de expansão.", [
        "https://ecoms1.com/24308/@v3/1694166246940-gabinete-gamer-sem-fonte-p2t3c-com-led-rgb-gt-gamer-3-min.webp",
    ]),
    Product(12, "Teclado Gamer", 120.25, 1, "Uma partida gamer diferenciada exige um teclado diferenciado. E este é o Teclado Gamer Telas Coloridas Geek Windows Lock. Com design robusto e ergonômetro.", [
        "https://images.tcdn.com.br/img/img_prod/745260/teclado_gamer_semi_mecanico_led_rgb_abnt2_usb_pc_ps4_xbox_67_1_d5520f952b2ee293ee340c520427101e.jpg",
    ])
]

@home_bp.route('/')
def home():
    return render_template('index.html', categories=categories, products=products)
