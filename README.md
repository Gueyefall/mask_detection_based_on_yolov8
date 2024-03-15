# Description
The **mask_detection_based_on_yolov8** project is a comprehensive set of resources designed for mask-wearing detection.  

This GitHub repository is the primary source of Python scripts and associated data, forming an ecosystem dedicated to research and development in the field of computer vision and machine learning.  

For my case, the trainings were conducted with the following hardware :
- CPU Ryzen 5 6500H
- GPU AMD RADEON RX 6600M
# Repository Installation and Virtual Environment Setup
To install this project, start by opening the Terminal or Command Prompt: On Windows, open Command Prompt or PowerShell. On macOS or Linux, open Terminal.

Execute :
`git clone https://github.com/Gueyefall/mask_detection_based_on_yolov8.git`

PS: You will need to log in with your git credentials having access rights to the repo.
Otherwise, just download the zip using the dedicated button in the "Code" dropdown menu above.

Next, first check if python (ideally 3.9 or later) is installed  
`python --version` ou `python3 --version`

* Install Python: Make sure Python is installed on your system. You can download it from the official Python website. Installing Python also includes pip (Python package manager) and venv (module for creating virtual environments).

* Then install pip, the Python package manager. It is necessary to install dependencies. If you do not have pip, install it by following the instructions on the [official pip website](https://pip.pypa.io/en/stable/installation/)

* For more [details on virtual environments](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments)

Create a Virtual Environment: Execute the following command to create a virtual environment. *Replace nom_env* with the name you want to give your virtual environment :  

* On Windows : `python -m venv nom_env`  
* On macOS and Linux : `python3 -m venv nom_env`

Activate the Virtual Environment: Once the virtual environment is created, you need to activate it :  

* On Windows : `.\nom_env\Scripts\activate`
* On macOS and Linux : `source nom_env/bin/activate`

When the virtual environment is activated, you will typically see the name of the virtual environment displayed in your command line (at the beginning, in parentheses).

*PS: Deactivating the Virtual Environment: When you are done working in the virtual environment, you can deactivate it by executing :* `deactivate`

# Dependencies Installation
Execute the following command to install all dependencies listed in requirements.txt :  
`pip install -r requirements.txt`

In addition, you will probably need to install additional packages before running YOLO....

* Manage drivers for the GPU (varies by provider: nvidia, amd, etc.) 
[Drivers NVIDIA CUDNN](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)  
[Drivers AMD ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html#rocm-install-quick)  

* For the essential dependency that is PyTorch (if not installed), refer to : https://pytorch.org/
