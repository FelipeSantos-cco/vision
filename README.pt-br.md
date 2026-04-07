# Vision Automation
### Pacote de visão computacional focado em automação e RPA

Uma forma diferente de usar o PyAutoGui. Focado em automações onde podemos ter barras de página com captchas e reCaptchas que impedem o uso do Selenium Driver, por exemplo. Neste pacote, há uma maneira de usar o PyAutoGui pelo nome de imagens salvas em uma pasta de templates, fazendo com que o código pesquise a tela e execute o que você deseja.

Funciona de uma forma simples: quando você passa uma imagem, o código compara a tela principal com a imagem fornecida, com 80% de assertividade por padrão (em alguns casos esse valor precisa ser reduzido, como ao buscar tokens e valores que mantêm a formatação mas mudam com frequência). Se a imagem for encontrada na tela, o código prossegue para executar a ação desejada, seja um clique duplo, simples ou até a seleção de um checkbox de captcha.

#### Como usar?

> [!NOTE]  
> Versão do Python utilizada para testes: **3.11.9**
> 
> Dependências: `pip install -r requirements.txt`

Neste exemplo estou usando uma pasta de templates chamada literalmente "templates".

Primeiro precisamos inicializar a classe VisionAutomation.

```py
import os
from src.vision import VisionAutomation 

parent_directory = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(parent_directory, 'templates') # Obtendo o caminho da pasta

vision = VisionAutomation(template_path)
```

A partir de agora você pode usar os nomes das imagens salvas na sua pasta de templates como parâmetros nos métodos do VisionAutomation. Por exemplo:

Um clique em um botão:
```py
vision.click("botao.png")
```

Clicar e escrever em um campo de entrada:
```py
vision.click_write("input_simples.png", "Valor a ser escrito no campo")
```

Um token que precisa ser copiado e colado em outro lugar.
É importante lembrar que a confiança neste caso é 50% (0.5) porque o token mantém a mesma formatação, mas seu valor sempre muda. Por exemplo, sempre serão letras vermelhas em bloco, mas são letras diferentes.
```py
vision.double_click_and_copy("token.png", confidence=0.5)
```

Em resumo, há uma enorme gama de combinações de funções que podem existir e diversos cenários onde podem ser aplicadas.
Mas obrigado por visitar e se interessar pelo projeto VisionAutomation. Estou sempre disponível e espero que este projeto te ajude ou te inspire de alguma forma.

```py
print("Muito obrigado ❤️")
```
