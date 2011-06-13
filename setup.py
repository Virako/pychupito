#-*- coding:utf-8 -*-


from distutils.core import setup

setup(name='pychupito',
      version='1.0 Alpha',
      description='Un juego de chupitos',
      long_description='Este juego guarda foto de los borrachos que vayan a \
       jugar y va sacando aleatoriamente a uno de ellos, el cual tendrá que \
       beber. Durante el juego, esta aplicación te hará fotos y al final de \
       la partida creará un gif con tus fotos para que veas la mejoría',
      author='Víctor Ramírez',
      author_email='virako.9@gmail.com',
      url='https://github.com/Virako/pychupito',
      download_url='https://github.com/Virako/pychupito/archives/master',
      license='GPLv3',
      scripts=['pychupito_game'],
      packages=['pychupito',
                'pychupito.gui'
                ]
     )



