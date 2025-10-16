# CS1440/2440 Lab 6: Simultaneous Auctions (Part 1)

## Introduction
Very chill lab this time introducing you to the idea of marginal values and utilizing them to optimize your bids in a simple Simultaneous Sealed Bid Auction. Later labs will build off of these ideas so please make sure to toy around with and understand this well. 
The idea of price prediction using self-confirming price prediction is also introduced.

## Setup and Installation
Follow these steps to set up your environment and install the necessary package for the lab.

**IMPORTANT: Please install/use a version of `Python >= 3.10`**
To check which version of Python you're using please run
```bash
python --version
```

If you installed Python 3.11 but your computer defaults to Python 3.9 you can initialize the virtual environment below to use 
Python 3.11 instead by running:

If you own a Mac 
```bash
python3.11 -m venv .venv
```
Instead of 
```bash
python3 -m venv .venv
```

If you own a Windows 
```bash
py -3.11 -m venv .venv
```

### Step 1: Git Clone the Repository 
Open your terminal and navigate to where you want to clone the repository
```bash 
git clone https://github.com/brown-agt/lab06-stencil.git
```

### Step 2: Create a Virtual Environment
Please then navigate to your project directory. Run the following commands to create a Python virtual environment named `.venv`.

If you own a Mac 
```bash
python3 -m venv .venv
source .venv/bin/activate
```

If you own a Windows 
```bash 
python3 -m venv .venv
.venv\Scripts\activate
```

**Note:** There will be no live competition for this lab! 
