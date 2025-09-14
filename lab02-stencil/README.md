# CS1440/2440 Lab 2: Finite State Machines and Games of Incomplete Information

## Introduction

In Lab 2 of the CS1440/2440 course, you will engage with the game theory problem "Battle of the Sexes" using Python. This lab involves both complete and incomplete information scenarios. You'll design agent strategies using finite state machines (FSMs) and test these strategies against both pre-implemented agents and classmates' agents in simulations and competitions.

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
git clone https://github.com/brown-agt/lab02-stencil.git
```

### Step 2: Create a Virtual Environment

Please then navigate to your project directory. Run the following commands to create a Python virtual environment named `.venv`.

If you own a Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

If you own a Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Agent Methods

For the `BOSAgent`s here are a few methods that you may find helpful!

- `self.calculate_utils(a1, a2)` is a method that takes in player 1's action (`a1`) and player 2's action (`a2`) and returns a list [`u1`, `u2`] where `u1` is player1's utility and `u2` is player 2's utility.
- `self.get_action_history()` is a method that returns a list of your actions from previous rounds played.
- `self.get_util_history()` is a method that returns a list of your utility from previous rounds played.
- `self.get_opp_action_history()` is a method that returns a list of your opponent's actions from previous rounds played.
- `self.get_opp_util_history()` is a method that returns a list of your opponent's utility from previous rounds played.
- `self.get_last_action()` is a method that returns a your last action from the previous round.
- `self.get_last_util()` is a method that returns a your last utility from the previous round.
- `self.get_opp_last_action()` is a method that returns a your opponent's last action from the previous round.
- `self.get_opp_last_util()` is a method that returns a your opponent's last utility from the previous round.

In addition to the above methods, for the `BOSIIAgent`s, you also have access to the following methods:

- `self.is_row_player()` is a method that returns true if you are the row player (and thus have incomplete information) and false if you are the column player.
- `self.get_mood()` is a method that returns your current mood: either self.GOOD_MOOD or self.BAD_MOOD provided you are the column player.  The mood determines the payoff matrix. If you are the row player, this method returns None, because your mood does not vary and you do not know the opponent's mood.
- `self.get_last_mood()` is a method that returns your mood in the last round: either self.GOOD_MOOD or self.BAD_MOOD provided you are the column player and that at least 1 round has been played. Otherwise it returns None
- `self.get_mood_history()` is a method that returns your mood over all rounds played in the current matching: either self.GOOD_MOOD or self.BAD_MOOD provided you are the column player and that at least 1 round has been played. Otherwise it returns None
- `self.row_player_calculate_util(row_move, col_move)` is a method that returns the row player's hypothetical reward from the specified action profile.
- `self.col_player_calculate_util(row_move, col_move, mood)` is analogous to this, but returns the column player's hypothetical reward, and depends on their mood
- `self.col_player_good_mood_prob()` is a method that returns the probability that the column player is in a good mood, which is useful in expected value calculations.
