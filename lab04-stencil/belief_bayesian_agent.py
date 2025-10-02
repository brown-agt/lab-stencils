from agt_server.agents.base_agents.lemonade_agent import LemonadeAgent
from agt_server.local_games.lemonade_arena import LemonadeArena
from agt_server.agents.test_agents.lemonade.stick_agent.my_agent import StickAgent
from agt_server.agents.test_agents.lemonade.always_stay.my_agent import ReserveAgent
from agt_server.agents.test_agents.lemonade.decrement_agent.my_agent import DecrementAgent
from agt_server.agents.test_agents.lemonade.increment_agent.my_agent import IncrementAgent
import random

from mysterious_agents import mysteriousagent, dummyagent


class BeliefAgent(LemonadeAgent):
    def setup(self):
        # Initialize belief vector: state 0 -> type3, state 1 -> type9.
        self.b = [0.5, 0.5]

        # Transition matrix T: since the type never changes, it is the identity.
        self.T = [[1, 0],
                  [0, 1]]
        
        # Observation function O: maps state index to a dict of observation probabilities.
        # For type3 (state 0): P(3)=0.7, P(9)=0.3.
        # For type9 (state 1): P(3)=0.3, P(9)=0.7.
        self.O = {
            0: {3: 0.7, 9: 0.3},
            1: {3: 0.3, 9: 0.7}
        }

    def get_action(self):
        # TODO: Find the optimal policy in expectation given the current belief state.
        # Hint: there are a lot of valid ways to approach this, some simpler than others.

        best_action = None
        return best_action

    def update(self):
        """
        Update the belief vector given an observation from agent1.
        `observation` should be either 3 or 9.
        
        The belief update is:
            b'(s') = O(observation | s') * b(s') / N
        where N = sum_{s''} O(observation | s'') * b(s''). (a normalization constant)
        """
        if not(self.get_opp1_last_action()):
            pass
        observation = self.get_opp1_last_action()

        # TODO: update new_b to be your new belief state based on the observation!
        # Hint: use self.O and self.b
        new_b = [0.0, 0.0]


beliefagent = BeliefAgent("belief")
arena = LemonadeArena(
    num_rounds=500,
    timeout=1, 
    players=[
        beliefagent,
        mysteriousagent,
        dummyagent,
    ]
)
arena.run()