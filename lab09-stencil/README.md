# Lab 9: TAC AdX Game (Two-Day Variant)

This lab implements a two-day advertising exchange game where agents compete in AdX auctions over two consecutive days. The budget for the second day's campaign depends on the quality score achieved on the first day.

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

### Step 1: Git Pull the Repository

Open your terminal and navigate to where you cloned the lab-stencils repository. Git pull to get the recent changes for lab 08

```bash
git pull
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

### Step 3: Install/Upgrade the agt server package

```bash
pip install --upgrade pip
pip install --upgrade agt-lab-server
```