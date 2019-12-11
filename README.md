# ImmMaps

Unity Version: 2019.2.8f1
Python Version: 3.7.5

###### Requerimentos para o Python:
---
- Geopandas
- Rasterio
- GDAL

Tutorial de como instalar o GDAL no Windows:
<https://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows>

Após instalar o GDAL, pode-se instalar o módulo GDAL no python utilizando o comando:
```
python -m pip install GDAL
```

###### Como rodar o ImmMaps
---
1. Clone o repositório inteiro para seu computador
2. Abra a pasta MapPlot no Unity como um projeto
3. Compile, se desejar
4. Troque o caminho de output do dataset no arquivo main.py para a pasta interna da aplicacão do Unity
5. Utilize o python para rodar o main.py
6. Selecione a imagem e o *shapefile*
7. Ao clicar em Plot, o arquivo com o dataset é salvo na pasta do Unity
8. Inicie a aplicação Unity