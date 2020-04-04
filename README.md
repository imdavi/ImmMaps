# ImmMaps

###### Instalações necesárias:

Unity Version: 2019.2.8f1 [Link](https://unity3d.com/get-unity/download?thank-you=update&download_nid=63067&os=Win)
Python Version: 3.7.5 [Link](https://www.python.org/downloads/release/python-375/)

Visual Studio Code - necessário para compilar alguns componenetes e o projeto do Unity.
O instalador do Unity deve fazer o download automaticamente para você. Se não o fizer, baixe a versão mais recente do site oficial.

Baixe também o [Visual Studio Build Tools](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16) e instale.

Na instalação deste, selecione o checkbox C++ Build Tools e clique em "Install".

Reinicie o computador depois de instalar o Unity e os componentes do Visual Studio.

##### Guia de Instalação:
---

Tutorial de como instalar o GDAL no Windows:

1. Baixe o módulo core do GDAL aqui: [64bits](http://download.gisinternals.com/sdk/downloads/release-1900-x64-gdal-3-0-4-mapserver-7-4-3/gdal-300-1900-x64-core.msi) ou [32bits](http://download.gisinternals.com/sdk/downloads/release-1900-gdal-3-0-2-mapserver-7-4-2/gdal-300-1900-core.msi).
2. Instale utilizando a opção "Typical Install".
3. Em seguida é necesário adicionar o GDAL às variáveis de sistema.
3.1. Vá em iniciar e busque por "Environment Variables" ou "Variáveis de ambiente".
3.2. Clique no resultado "Editar variáveis de sistema".
3.3. Na janela que se abrir, clique em "Environment Variables..." próximo ao botão "OK".
3.4. Na nova janela, busque pela variável Path na lista inferior; clique em "Edit...".
3.5. Adicione uma nova linha à variável clicando em "New" e digite "C:\Program Files\GDAL" (OBS: se sua instalação for 32bits lembre-se de colocar 'Program Files (x86)'). Clique OK.
3.6. Na janela anterior, clique em "New..." para adicionar uma nova variável.
3.7. Adicione a variável GDAL_DATA, com caminho "C:\Program Files\GDAL\gdal-data".
3.8. Adicione uma segunda variável GDAL_DRIVER_PATH, com caminho "C:\Program Files\GDAL\gdalplugins".
3.9. Dê OK em tudo.
4. Para confirmar se a instalação foi bem sucedida, abra um prompt de comando do Windows, 
digite ```gdalinfo --version``` e aperte ENTER. A versão do GDAL instalada deve aparecer no console.
5. Baixe e instale o python bindings do GDAL. [64bit](http://download.gisinternals.com/sdk/downloads/release-1900-x64-gdal-3-0-4-mapserver-7-4-3/GDAL-3.0.4.win-amd64-py3.7.msi) [32bit](http://download.gisinternals.com/sdk/downloads/release-1900-gdal-3-0-4-mapserver-7-4-3/GDAL-3.0.4.win32-py3.7.msi)

Em seguida, precisamos instalar algumas bibliotecas para o Python.

```
python -m pip install numpy
python -m pip install GDAL
python -m pip install geopandas
python -m pip install rasterio
```

##### Como rodar o ImmMaps
---
1. Clone o repositório inteiro para seu computador
2. Abra a pasta MapPlot no Unity como um projeto
3. Compile, se desejar
4. Troque o caminho de output do dataset no arquivo main.py para a pasta interna da aplicacão do Unity
5. Utilize o python para rodar o main.py
6. Selecione a imagem e o *shapefile*
7. Ao clicar em Plot, o arquivo com o dataset é salvo na pasta do Unity
8. Inicie a aplicação Unity