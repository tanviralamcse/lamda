# setup.sh

#!/bin/bash

# Update package list
sudo apt-get update

# Install Python 3
sudo apt-get install -y python3

# Install pip (Python package installer)
sudo apt-get install -y python3-pip

# Install Selenium dependencies
pip3 install selenium

# Install pytest for running tests
pip3 install pytest
