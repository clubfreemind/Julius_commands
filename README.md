    Clone the project
    Install julius, julius-voxforge
    Install  voice file : cd /usr/share/festival/voices/english/ 
	            sudo wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2 
		    sudo tar jxf cmu_us_clb_arctic-0.95-release.tar.bz2 
		    sudo ln -s cmu_us_slt_arctic cmu_us_slt_arctic_clunits 
		    sudo cp /etc/festival.scm /etc/festival.scm.backup 
		    sudo echo "(set! voice_default 'voice_cmu_us_slt_arctic_clunits)" >> /etc/festival.scm
    Install festival
    Install festlex-cmu
    Install Tornado
    Install python-numpy
    Install lxml
    Install python-dev
    Command for running julius : padsp julius -C julian.jconf | ./getcommand.py
    
