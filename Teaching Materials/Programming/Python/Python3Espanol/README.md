# Curso de Introduccion a Python 3

Este es un curso de introduccion a la programacion usando Python 3 en el marco del procesamiento de una imagen del disco de escombros alrededor de Fomalhaut para encontrar el exoplaneta Fomalhaut b. Este curso esta diseñado para estudiantes de ultimos años de colegio, o estudiantes universitarios/profesionales sin experiencia en programacion.

El material de este notebook fue recopilado para Clubes de Ciencia Colombia 2017 por Luis Henry Quiroga (GitHub: [lhquirogan](https://github.com/lhquirogan/)) y Germán Chaparro (GitHub: [saint-germain](https://github.com/saint-germain/)).

## Contenidos

1. [Introduccion a Python](1_Introduccion)

2. [Python Intermedio](2_Intermedio)

3. [Python Avanzado](3_Avanzado)

4. [Proyectos](Proyectos)

Para un primer curso intensivo de 4-5 días es suficiente con las secciones 1-2. La seccion "Python Avanzado" contiene tutoriales de Numpy y Matplotlib (que son avanzados para alguien que apenas esta empezando a programar).

Hay varias maneras de explorar este curso:

### Usando mybinder.org sobre este repositorio 

Haciendo clic en el siguiente boton se pueden correr los notebooks de la seccion 1 (excepto algunas celdas en los notebooks 1.4 y 1.5). directamente a traves de mybinder.org, que genera una maquina virtual en la nube en donde se puede interactuar con los notebooks. Los notebooks de las secciones 2 y 3 no se pueden correr de esta manera, pues las librerias no existen dentro de la maquina virtual invocada.

[![Binder](https://mybinder.org/badge.svg)]([![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/astro4dev/OAD-Data-Science-Toolkit/master))

### Usando mybinder.org sobre el repositorio original de este curso

Haciendo clic en el siguiente boton se pueden correr todos los notebooks del curso directamente a traves de mybinder.org, que genera una maquina virtual en la nube en donde se puede interactuar con los notebooks. Este enlace funciona sobre el repositorio original del curso en https://github.com/saint-germain/Python3Espanol.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/saint-germain/Python3Espanol/master)

## Corriendo localmente este repositorio

 - Descarga el repositorio completo del OAD Data Science Toolkit en este [enlace](https://github.com/astro4dev/OAD-Data-Science-Toolkit/archive/master.zip). 
 - Instala [Anaconda](https://www.anaconda.com/download/) completo o [Miniconda](https://conda.io/miniconda.html) con minimo las librerias `jupyter numpy matplotlib astropy` (ver abajo para Windows).
 - Corre localmente los notebooks en este directorio.
 
 Nota: Tambien se puede clonar localmente solamente el repositorio original https://github.com/saint-germain/Python3Espanol y se siguen las instrucciones anteriores.

#### Para instalar Anaconda en Windows:

1. Verificar si tu sistema es 32 o 64 bits: http://es.ccm.net/faq/9548-como-saber-si-mi-windows-es-de-32-o-64-bits

2. Descargar y ejecutar la el instalador para Windows correspondiente a 32 o 64 bits según lo que diga la verificación anterior. Es importante que la versión de Python que necesitamos es la 3.6 https://www.continuum.io/downloads#windows

3. Abrir Jupyter Notebook en la carpeta correspondiente del menú Inicio y buscar la ubicación del repositorio (descomprimido) desde el navegador

4. Desde el navegador, abrir el Notebook (.ipynb) que se quiera estudiar.
