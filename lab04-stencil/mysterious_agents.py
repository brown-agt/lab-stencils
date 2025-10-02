from agt_server.agents.base_agents.lemonade_agent import LemonadeAgent
from agt_server.local_games.lemonade_arena import LemonadeArena
from agt_server.agents.test_agents.lemonade.stick_agent.my_agent import StickAgent
from agt_server.agents.test_agents.lemonade.always_stay.my_agent import ReserveAgent
from agt_server.agents.test_agents.lemonade.decrement_agent.my_agent import DecrementAgent
from agt_server.agents.test_agents.lemonade.increment_agent.my_agent import IncrementAgent
import random

class MysteriousBot(LemonadeAgent):
    def setup(self):
        self.agent_type = random.choice(['type3', 'type9'])

        if self.agent_type == 'type3':
            self.probs = {3: 0.7, 9: 0.3}
        else:
            # type9
            self.probs = {3: 0.3, 9: 0.7}

    def get_action(self):
        positions = list(self.probs.keys())
        weights = list(self.probs.values())
        chosen_position = random.choices(positions, weights=weights, k=1)[0]
        return chosen_position
    def update(self):
        pass

# TODO: 
# Task 3: Modify the mysterious agent in various ways.
class MysteriousBot2(LemonadeAgent):
    def setup(self):
        pass
    def get_action(self):
        pass
    def update(self):
        pass

# TODO: 
# Task 5: Fill out this mystery agent to play Tit-for-tat!
# Tit-for-tat is a strategy in which a player begins cooperating but then
# subsequently mirrors their opponent's actions.
class MysteriousBotTitForTat(LemonadeAgent):
    def setup(self):
        pass
    def get_action(self):
        pass
    def update(self):
        pass

# ----------------------------
class DummyBot(LemonadeAgent):
    def setup(self):
        self.spot = 0
    def get_action(self):
        return self.spot
    def update(self):
        pass

class RandomAgent(LemonadeAgent):
    def setup(self):
        pass
    def get_action(self):
        return random.randint(0, 11)
    def update(self):
        pass
# ----------------------------

randomagent = RandomAgent("Random")
dummyagent = DummyBot("Sticky")

# This agent is exported to belief_bayesian_agent.py and belief_q_learning.agent.py.
# To test your mystery agents, you can change the class of mysteriousagent here
# or just import the class definition in the respective files and create a new
# instance of your new mysteryagent.
mysteriousagent = MysteriousBot("Mysterious")

# Run this file to see how these agents compete
arena = LemonadeArena(
    num_rounds=500,
    timeout=1, 
    players=[
        randomagent,
        mysteriousagent,
        dummyagent,
    ]
)
arena.run()