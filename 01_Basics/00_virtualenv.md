Step 1: Install Miniconda or Anaconda
What are Anaconda and Miniconda?

Anaconda is a full package that includes Python and over 1 GB of libraries and tools, including Jupyter Notebook and Spyder.
Miniconda is a lightweight version of Anaconda, suitable for users who only need Python and essential tools.
Why Miniconda?
If you prefer a smaller installation and only need the basics for Python programming, Miniconda is the better choice. It will use less space and be easier to set up.

 

Installation Process
Search for Miniconda: Open your web browser (preferably Google Chrome) and search for “Download Miniconda.”
Download: You’ll be directed to the Miniconda download page. Select the version appropriate for your operating system (Windows, macOS, or Linux).
Start Installation: Once the installer is downloaded, open it and follow the prompts:
Choose Next and Agree to the terms.
Choose the installation location (you can keep the default).
Select the option to Add Miniconda to PATH for easier access.
 

Step 2: Install VS Code
What is VS Code?
VS Code is a free, open-source code editor that makes it easy to write, edit, and run Python code.

Installation Steps:

Download: Go to the Visual Studio Code website and download the installer for your operating system.
Install: Run the downloaded file and follow the prompts to complete the installation.
 

Step 3: Verify Python Installation
Once Miniconda is installed, it’s time to verify that Python is properly installed.

Check Python Version
Open the Anaconda Prompt:
Press the Windows key and type “Anaconda” in the search bar. Select Anaconda Prompt.
In the Anaconda Prompt, type the following command:
bash
CopyEdit
python --version

If Python is installed correctly, you should see a version number (e.g., Python 3.12).
Alternatively, you can use this command to check:
bash
CopyEdit
python --version

 
If you do not see a version number, this means the installation didn’t work, and you may need to reinstall Miniconda or Anaconda.

 

Step 4: Running Your First Python Program
Now that you have everything installed, it's time to run your first Python program.

Open VS Code.
Create a New File: Click on File > New File.
Write Your Program: Type the following simple Python code:
python
CopyEdit
print("Hello, World!")

 
Run the Program:
Save the file with a .py extension (e.g., first_program.py).
In VS Code, click on Terminal > New Terminal and type:
bash
CopyEdit
python first_program.py

You should see "Hello, World!" printed in the terminal.
 
<!-- Create Virtual Environment  -->
conda create -n first_env pyhton=.10

<!-- Activate Environment -->
conda activate first_env

<!-- Deactivate Environment -->
conda deactivate

<!-- For Package Installation (pip & conda) -->
pip install numpay==2.2

<!-- Check all package install -->
conda list

<!-- check the environments information in your system -->
conda info -e

<!-- Delete the enviroment -->
conda remove --name first_env --all
 

Summary of Key Points
Miniconda vs. Anaconda: Miniconda is a lightweight version, whereas Anaconda includes more tools and libraries.
VS Code is a code editor that makes it easy to write and run Python code.
Python Setup: After installing Miniconda and VS Code, always check your Python installation with python --version.
First Program: Running a simple Python program, such as printing "Hello, World!", is the first step in your journey.