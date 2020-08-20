# Bot de comentários para instagram
Este programa consegue postar comentários em determinado post do instagram automaticamente. Ele possibilita configurar um intervalo entre cada comentário, 
o que impede que o seu perfil seja impossibilitado de comentar rapidamente. Você também pode definir a quantidade de vezes que quer que seja realizado os comentários
bem como quais.

# Como usar
Certifique que tenha o Python 3 instalado no seu computador. Caso não tenha baixe em https://www.python.org/downloads/. Feito isso instale o selenium, use no terminal o comando
`pip install selenium`. Por fim baixe o chrome webdriver que pode ser adquirido em https://chromedriver.chromium.org/downloads e o adicione a uma pasta chamada webdriver no
diretorio arquivos de programa.

# Possiveis erros
Certifique-se de que a versão do webdriver baixada é a mesma de seu navegador chrome.
Caso tenha adicionado o webdriver a outro diretório altere a linha `driver = webdriver.Chrome(executable_path="C:\Program Files\webdriver/chromedriver")` substituindo o
caminho especificado pelo da sua máquina.
