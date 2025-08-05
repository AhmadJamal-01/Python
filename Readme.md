#installation
#Anacoda

conda info -e 
#conda environment details

conda list
#conda laibray install list

conda remove --name python_project --all 
#--all (del all installed libraries in environment) 


pip freeze > requirements.txt
#create requirements.txt file in you environment