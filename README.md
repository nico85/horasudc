# horasudc
Sistema de gestion de horas cátedras de la Universidad del Chubut

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
	-> sudo make altinstall

	 Step 4 – Check the Python Version
	-> python3.5 -V


Pip3 (instalador de repositorios)
--> Install Pip3 (https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04)
	-> sudo apt-get install python3-setuptools
	-> sudo easy_install3 pip


Framework Django
--> Install Django 1.11.3 (with pip3)
	-> sudo pip3 install django


-> python3 manage.py shell
  ->>> import django
  ->>> django.VERSION
  ->>> (1, 11, 3, 'final', 0)
  
  
