<h3># horasudc</h3>
<p>Sistema de gestion de horas cátedras de la Universidad del Chubut</p>

Install Git (sino esta instalado)
-> sudo apt-get install git
-> git --version

Desarrollado con:

Python 3.5.2 
--> Install Python 3.5.2 (https://tecadmin.net/install-python-3-5-on-ubuntu/)
	 Step 1 - Install Required Packages
	-> sudo apt-get install build-essential checkinstall
	-> sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

	 Step 2 - Download Python 3.5.2
	-> cd /home/USUARIO/Descargas
	-> wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
	 Extract package
	-> sudo tar xzf Python-3.5.2.tgz

	 Step 3 – Compile Python Source
	-> cd Python-3.5.2
	-> sudo ./configure
	-> sudo make
	-> sudo make install
	-> sudo ln -fs /home/USUARIO/Descargas/Python-3.5.2/python /usr/bin/python

	 Step 4 – Check the Python Version
	-> python -V o python3.5 -V


Pip3 (instalador de repositorios)
--> Install Pip3 (https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04)
	-> sudo apt-get install python3-setuptools
	-> sudo easy_install3 pip


Framework Django
--> Install Django 1.11.3 (with pip3)
	-> sudo pip3 install django
    -> python3 (shell)
        ->>> import django
        ->>> django.VERSION
        ->>> (1, 11, 3, 'final', 0)


Postgresql
--> Install Postgresql Ununtu 16.04
    -> sudo apt-get update
    -> sudo apt-get install postgresql postgresql-contrib
    Create super User
    -> sudo -i -u postgres (password)
    -> CREATE ROLE mysuperuser2 WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD 'mysuperpass2';


Configuración del Sistema:
--> copiar desde el proyecto de desarrollo (local o desarrollo) el settings.py con la información necesaria
para hacer funcionar el sistema (contiene aplicaciones a utilizar + conexión a la base de datos)


Instalar Apache2
    -> sudo apt-get install apache2


Instalar VirtualENV (https://virtualenv.pypa.io/en/stable/)
    -> pip3 install virtualenv
    -> virtualenv ENV (include python3, site-packages, etc.)


Configurar Apache para deploy Django
    ->

  
  
