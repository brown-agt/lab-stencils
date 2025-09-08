import sys
import os
import asyncio
from agt_server.core.agents.common.chicken_agent import ChickenAgent

class CompetitionAgent(ChickenAgent):
    """Your competition agent for the Chicken game."""
    
    def __init__(self, name: str = "CompetitionAgent"):
        super().__init__(name)
        # TODO: Initialize any variables you need for your strategy
        self.SWERVE, self.CONTINUE = 0, 1
    
    def setup(self):
        """
        Initializes the agent for each new game they play.
        Called at the beginning of each new game.
        """
        # TODO: Initialize your agent for a new game
        pass
    
    def get_action(self, obs=None):
        """
        Returns your agent's next action for the Chicken game.
        
        Actions:
        0 = Swerve
        1 = Continue
        
        Chicken payoff matrix (row player, column player):
        S\\C  S  C
        S    0  -1
        C    1  -5
        
        Where S = Swerve, C = Continue
        """
        # TODO: Implement your Chicken strategy here
        # You can use any strategy you want, but it should not be uniform random
        raise NotImplementedError
    
    def update(self, obs=None, actions=None, reward=None, done=None, info=None):
        """
        Updates your agent with the current history, namely your opponent's choice 
        and your agent's utility in the last game.
        
        Args:
            obs: Current observation from the game
            actions: Actions taken by all players
            reward: Your agent's utility in the last game
            done: Whether the game is finished
            info: Additional information (may contain opponent's action)
        """
        # TODO: Add any additional state updates your strategy needs
        if reward is not None:
            self.reward_history.append(reward)
        
        # You can access your action history with self.action_history
        # You can access your reward history with self.reward_history


if __name__ == "__main__":
    
    server = False  # Set to True to connect to server, False for local testing
    name = ...  # TODO: Please give your agent a name
    host = "localhost"  # Server host
    port = 8080  # Server port
    verbose = False  # Enable verbose debug output
    game = "chicken"  # Game type (hardcoded for this agent)
    
    if server:
        server_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'server')
        sys.path.insert(0, server_dir)
        
        from agt_server.server.connect_stencil import connect_agent_to_server
        from agt_server.server.adapters import create_adapter
        
        async def main():
            if not name:
                import random
                agent_name = f"CompetitionAgent_{random.randint(1000, 9999)}"
            else:
                agent_name = name
                
            agent = CompetitionAgent(agent_name)
            server_agent = create_adapter(agent, game)
            
            await connect_agent_to_server(server_agent, game, agent_name, host, port, verbose)
        
        asyncio.run(main())
    else:
        print("Testing Chicken Competition Agent locally...")
        print("=" * 50)
        
        from agt_server.core.agents.lab03.swerve_agent import SwerveAgent
        from agt_server.core.agents.lab03.continue_agent import ContinueAgent
        from agt_server.core.agents.lab03.random_chicken_agent import RandomChickenAgent
        from agt_server.core.local_arena import LocalArena
        from agt_server.core.game.ChickenGame import ChickenGame
        
        agent = CompetitionAgent("CompetitionAgent")
        opponent1 = SwerveAgent("SwerveAgent")
        opponent2 = ContinueAgent("ContinueAgent")
        opponent3 = RandomChickenAgent("RandomAgent")
        
        agents = [agent, opponent1, opponent2, opponent3]
        arena = LocalArena(ChickenGame, agents, num_rounds=1000, verbose=True)
        arena.run_tournament()
        
        print("\nLocal test completed!")

agent_submission = CompetitionAgent("CompetitionAgent")
