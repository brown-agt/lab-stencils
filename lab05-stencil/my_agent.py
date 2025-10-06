# from my_rl_lemonade_agent import rl_agent_submission 
import argparse
# from my_lemonade_agent import nrl_agent_submission 
from agt_server.agents.base_agents.lemonade_agent import LemonadeAgent
from agt_server.local_games.lemonade_arena import LemonadeArena
from agt_server.agents.test_agents.lemonade.stick_agent.my_agent import StickAgent
from agt_server.agents.test_agents.lemonade.always_stay.my_agent import ReserveAgent
from agt_server.agents.test_agents.lemonade.decrement_agent.my_agent import DecrementAgent
from agt_server.agents.test_agents.lemonade.increment_agent.my_agent import IncrementAgent

# NOTE: The README will contain helpful methods for implementing your agent, please take a look at it!
class MyAgent(LemonadeAgent):
    def setup(self):
        self.name = ???
        pass

    def get_action(self):
        raise NotImplementedError

    def update(self):
        pass
    

# # TODO: Give your agent a NAME 
# name = ??? # TODO: PLEASE NAME ME D:
# # NOTE: If you want to submit MyAgent please set agent_submission = MyAgent(name)

################### SUBMISSION #####################
# TODO: Set to your RL Agent by default, change it to whatever you want as long as its a agent that inherits LemonadeAgent
# agent_submission = rl_agent_submission
agent_submission = ???
################### SUBMISSION #####################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='My Agent')
    parser.add_argument('--join_server', action='store_true',
                        help='Connects the agent to the server')
    parser.add_argument('--ip', type=str, default='127.0.0.1',
                        help='IP address (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=8080,
                        help='Port number (default: 8080)')
    
    args = parser.parse_args()

    if args.join_server:
        agent_submission.connect(ip=args.ip, port=args.port)
    else:
        arena = LemonadeArena(
        num_rounds=1000,
        timeout=10,
        players=[
            agent_submission,
            StickAgent("Bug1"),
            ReserveAgent("Bug2"),
            DecrementAgent("Bug3"),
            IncrementAgent("Bug4")
        ])
        
        # NOTE: FEEL FREE TO EDIT THE AGENTS HERE TO TEST AGAINST A DIFFERENT DISTRIBUTION OF AGENTS. A COUPLE OF EXAMPLE AGENTS
        #       TO TEST AGAINST ARE IMPORTED FOR YOU. 
        arena.run()
        
    
