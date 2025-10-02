from agt_server.agents.base_agents.lemonade_agent import LemonadeAgent
from agt_server.local_games.lemonade_arena import LemonadeArena
from agt_server.agents.test_agents.lemonade.stick_agent.my_agent import StickAgent
from agt_server.agents.test_agents.lemonade.always_stay.my_agent import ReserveAgent
from agt_server.agents.test_agents.lemonade.decrement_agent.my_agent import DecrementAgent
from agt_server.agents.test_agents.lemonade.increment_agent.my_agent import IncrementAgent
import random

from mysterious_agents import mysteriousagent, dummyagent
import numpy as np

class BeliefStateQLearningAgent(LemonadeAgent):
    def setup(self):
        # Initialize belief state: [a, b, 1] where a,b are type probabilities
        # The third number is the sticky position for the 'dummy' agent.
        self.b = np.array([0.5, 0.5, 1.0])
        
        # Observation function O
        self.O = {
            0: {3: 0.7, 9: 0.3},
            1: {3: 0.3, 9: 0.7}
        }
        
        # Q-learning parameters
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.3
        
        # Features: belief state [a, b, 1]
        self.num_features = 3
        self.num_actions = 12
        self.weights = np.random.normal(0, 0.1, (self.num_actions, self.num_features))
        
        self.prev_features = None
        self.prev_action = None
        
    def belief_to_features(self, belief):
        """Convert belief state [a, b, 1] to features"""
        return belief
    
    def get_q_values(self, belief):
        """Q(b, a) where b is the belief state [a, b, 1]"""
        features = self.belief_to_features(belief)
        return np.dot(self.weights, features)
    
    def get_action(self):
        q_values = self.get_q_values(self.b)
        
        if np.random.random() < self.epsilon:
            action = np.random.randint(0, self.num_actions)
        else:
            action = np.argmax(q_values)
        
        self.prev_features = self.belief_to_features(self.b)
        self.prev_action = action
        return action
    
    def update(self):
        # TODO: Update the belief given your opponent's actions.
        # Hint: put the code from Part 1 into a helper function.
        # Note our belief state has a third index for the sticky 'dummy' agent here.

        # TODO: Use the standard weight update function for Q-learning.
        pass

# Test the belief-state Q-learning agent
belief_q_agent = BeliefStateQLearningAgent("BeliefQ")

arena = LemonadeArena(
    num_rounds=1000,
    timeout=1, 
    players=[
        belief_q_agent,
        mysteriousagent,
        dummyagent,
    ]
)
arena.run()
