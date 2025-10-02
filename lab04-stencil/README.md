# CS1440/2440 Lab 4: Introduction to Partial Observability

## Introduction
This lab serves as a casual introduction to partial observability. You will need to fill in all the TO-DO blocks only in belief_bayesian_agent.py and belief_q_learning_agent.py.

## Setup and Installation
Follow these steps to set up your environment and install the necessary package for the lab.

### Step 1: Git Clone the Repository 
Open your terminal and navigate to where you want to clone the repository
```bash 
git clone https://github.com/brown-agt/lab-stencils
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

### Step 3: Install the agt server package
```bash
pip install --upgrade pip
pip install --upgrade agt-server
pip install torch
```

## Agent Methods 
For the `Lemonade Agent`s here are a few methods that you may find helpful! 
- `self.calculate_utils(a1, a2, a3)` is a method that takes in player 1's action (`a1`) and player 2's action (`a2`) and player 3's action (`a3`) and returns a list [`u1`, `u2`, `u3`] where `u1` is player1's utility, `u2` is player 2's utility, and `u3` is player 2's utility. 
- `self.get_action_history()` is a method that returns a list of your actions from previous rounds played.
- `self.get_util_history()` is a method that returns a list of your utility from previous rounds played. 
- `self.get_opp1_action_history()` is a method that returns a list of your first opponents's actions from previous rounds played.
- `self.get_opp1_util_history()` is a method that returns a list of your first opponent's utility from previous rounds played.
- `self.get_opp2_action_history()` is a method that returns a list of your second opponents's actions from previous rounds played.
- `self.get_opp2_util_history()` is a method that returns a list of your second opponent's utility from previous rounds played.
- `self.get_last_action()` is a method that returns a your last action from the previous round.
- `self.get_last_util()` is a method that returns a your last utility from the previous round.
- `self.get_opp1_last_action()` is a method that returns a your first opponent's last action from the previous round.
- `self.get_opp1_last_util()` is a method that returns a your first opponent's last utility from the previous round.
- `self.get_opp2_last_action()` is a method that returns a your second opponent's last action from the previous round.
- `self.get_opp2_last_util()` is a method that returns a your second opponent's last utility from the previous round.


PLEASE MAKE SURE TO SUBMIT YOUR AND YOUR PARTNER's CSLOGIN ON SEPERATE LINES IN `cs_login.txt`