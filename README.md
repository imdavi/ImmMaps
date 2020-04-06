# ImmMaps

###### Instalações necesárias:

Unity Version: 2019.2.8f1 [Link](https://unity3d.com/get-unity/download?thank-you=update&download_nid=63067&os=Win)
Python Version: 3.7.5 [Link](https://www.python.org/downloads/release/python-375/)

Visual Studio Code - necessário para compilar alguns componenetes e o projeto do Unity.
O instalador do Unity deve fazer o download automaticamente para você. Se não o fizer, baixe a versão mais recente do site oficial.

Baixe também o [Visual Studio Build Tools](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16) e instale.

Na instalação deste, selecione o checkbox *C++ Build Tools* e clique em "Install".

**Reinicie o computador** depois de instalar o Unity e os componentes do Visual Studio.

##### Guia de Instalação Python:
---

Para fazer o setup de todas as bibliotecas existem diversas maneiras. Algumas têm uma série de problemas na instalação e muitas dificuldades. A maneira abaixo foi a forma mais simples que encontrei de fazer o setup completo.

**Instalação via Anaconda**

1. Download Anaconda [Python 3.7](https://www.anaconda.com/distribution/#download-section)
2. Instale usando as configurações padrão
3. Abra o console Anaconda (Iniciar > Busca > Anaconda)
4. Rode o seguinte comando ``` conda create -n gdal_env -c conda-forge gdal ```
5. Aguarde até que a instalação finalize

Esse procedimento criará um ambiente do python contendo o GDAL instalado bem como suas dependências.
Depois que o ambiente estiver configurado pelo Anaconda, utilize o comando ```conda activate gdal_env``` para trocar para o ambiente correto.
Você pode desativar e voltar para o ambiente padrão com ```conda deactivate```.

Lembre-se que as bibliotecas serão instaladas somente no python dentro do ambiente *gdal_env* e só serão acessíveis de lá.

Em seguida, precisamos instalar algumas bibliotecas.
Para isso, rode os seguintes comandos nessa ordem, com o ambiente ativo:

```conda install rtree```
```conda install geopandas```
```conda install -c conda-forge rasterio```

Com isso, todas as bibliotecas estão prontas para utilização.

##### Como rodar o ImmMaps
---
1. Clone o repositório inteiro para seu computador
2. Abra a pasta MapPlot no Unity como um projeto
3. Compile, se desejar
4. Modifique o caminho de output do dataset no arquivo main.py
5. Utilize o Python do ambiente *gdal_env* do Anaconda para rodar o main.py
6. Selecione a imagem e o *shapefile*
7. Ao clicar em Plot, o arquivo com o dataset é salvo na pasta do Unity
8. Inicie a aplicação Unity


##### Sample de imagem e shape:

Shape da cidade de Campinas: [Download CampinasSHP.zip](https://drive.google.com/file/d/1I6QLyeTc5z_Ddm0589ZY_xZ-HjnNp8fJ/view?usp=sharing)
Imagem .TIF contendo a cidade de Campinas: [Download img_satelite.tif](https://drive.google.com/file/d/1kFyU7F8Rt61z-jhrC_W5yg3AggKq9mgE/view?usp=sharing)

OBS: o conjunto de arquivos *shapefile* dentro do zip precisa estar no mesmo diretório para que as bibliotecas do Python consigam adquirir todos os metadados corretamente.
OBS2: por conter metadados, a imagem de satelite é bem pesada (aprox 200mb).
