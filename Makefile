# Makefile for gmutils

#########################################################################################################################
# CONFIGURE

install_mac1:
	# Suggested version of Python 3 as of this writing:
	brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/ec545d45d4512ace3570782283df4ecda6bb0044/Formula/python3.rb
	wget https://bootstrap.pypa.io/get-pip.py
	sudo python3 get-pip.py
	pip install --upgrade pip
	brew install Graphviz
	brew install graphviz
	brew link graphviz
	# By hand:
	# python3 -m venv ~/envs/sample

install_mac2:
	pip install -r requirements.txt


install1:
	# By hand:
	# sudo apt-get update
	# sudo apt-get install -y build-essential cython python-numpy
	# sudo apt-get install -y zsh
	# sudo chsh -s /usr/bin/zsh ubuntu
	# zsh
	# sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
	# export LC_ALL=C
	mkdir envs
	mkdir downloads
	sudo apt-get install -y mosh
	wget https://bootstrap.pypa.io/get-pip.py
	sudo python3 get-pip.py
	sudo apt-get install -y python3-dev
	sudo apt-get install -y virtualenv
	sudo apt-get install -y emacs
	sudo apt-get install -y python3-tk


install2:
	# source envs/sample/bin/activate
	# Latest Elastic Search as of this writing:
	wget -P downloads https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.1.1.deb
	sudo dpkg -i downloads/elasticsearch-6.1.1.deb
	sudo systemctl enable elasticsearch.service
	pip install requests


#########################################################################################################################
# ADMIN

com:
	git commit -a -m "minor updates"
	git push

clean:
	# Clean up some artifacts created by other software
	find . -name Icon$$'\r' -exec rm -fr {} \;
	find . -name '*.pyc' -exec rm -fr {} \;
	find . -name '__pycache__' -exec rm -fr {} \;
	find . -name '*~' -exec rm -fr {} \;
	find . -name "*\[Conflict\]*" -exec rm -r {} \;
	find . -name "* \(1\)*" -exec rm -r {} \;
	find . -name ".DS_Store" -exec rm -r {} \;

force:

#########################################################################################################################
#########################################################################################################################
