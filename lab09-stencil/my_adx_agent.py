import math
from agt_server.core.game.AdxTwoDayGame import TwoDaysBidBundle
from agt_server.core.game.bid_entry import SimpleBidEntry
from agt_server.core.game.market_segment import MarketSegment
from agt_server.core.game.campaign import Campaign
from agt_server.core.agents.common.base_agent import BaseAgent
from agt_server.core.agents.lab09.aggressive_agent import AggressiveAdXAgent
from agt_server.core.agents.lab09.random_agent import RandomAdXAgent
from agt_server.server.connect_stencil import connect_agent_to_server

from agt_server.core.local_arena import LocalArena
from agt_server.core.game.AdxTwoDayGame import AdxTwoDayGame

class MyTwoDaysTwoCampaignsAgent(BaseAgent):
    """
    Your implementation of the AdX Two Day agent.
    
    This agent competes in AdX auctions over two consecutive days.
    The budget for the second day's campaign depends on the quality score achieved on the first day.
    
    Quality Score Formula:
    QC(x) = (2/a) * (arctan(a * (x/R) - b) - arctan(-b)) 
    where a = 4.08577, b = 3.08577, x = impressions achieved, R = campaign reach
    """
    
    def __init__(self, name: str = "MyTwoDaysAdxAgent"):
        super().__init__(name)
        self.campaign_day1 = None  # Will be set by the game environment
        self.campaign_day2 = None  # Will be set by the game environment
        self.quality_score = 1.0  # Quality score from day 1 (affects day 2 budget)
        self.game_title = "adx_twoday"

    def get_action(self, observation: dict = None) -> TwoDaysBidBundle:
        """Get the agent's action based on the current observation."""
        day = observation["day"]
        if day == 1:
            self.campaign_day1 = Campaign.from_dict(observation["campaign_day1"])
        elif day == 2:
            self.campaign_day2 = Campaign.from_dict(observation["campaign_day2"])
        # Check for quality score in both locations
        if "qc" in observation:
            self.quality_score = observation["qc"]
        elif "campaign" in observation and "qc" in observation["campaign"]:
            self.quality_score = observation["campaign"]["qc"]
        else:
            print(f" No qc found, using default: {self.quality_score}")
        return self.get_bid_bundle(day)
    
    def calculate_quality_score(self, impressions_achieved: int, campaign_reach: int) -> float:
        """
        Calculate quality score using the formula from the writeup.
        
        QC(x) = (2/a) * (arctan(a * (x/R) - b) - arctan(-b)) 
        where a = 4.08577, b = 3.08577
        
        Parameters:
        - impressions_achieved: Number of impressions acquired (x)
        - campaign_reach: Campaign's reach goal (R)
        
        Returns:
        - Quality score between 0 and 1.38442
        """
        a = 4.08577
        b = 3.08577
        x = impressions_achieved
        R = campaign_reach 
        if R == 0:
            return 0.0      
        x_over_R = x / R
        quality_score = (2 / a) * (math.atan(a * (x_over_R) - b) - math.atan(-b)) 
        
        return max(0.0, quality_score)  # Ensure non-negative
    
    def get_first_campaign(self) -> Campaign:
        """Get the campaign assigned for the first day."""
        return self.campaign_day1
    
    def get_second_campaign(self) -> Campaign:
        """Get the campaign assigned for the second day."""
        return self.campaign_day2
    
    def get_bid_bundle(self, day: int) -> TwoDaysBidBundle:
        """
        TODO:
        Return a TwoDaysBidBundle for your assigned campaign on the given day (1 and 2).
        
        Parameters:
        - day: The day for which to create bids (1 or 2)
        
        Returns:
        - TwoDaysBidBundle containing all bids for the specified day
        """
        raise NotImplementedError("not implemented")

if __name__ == "__main__":
    # Configuration variables - modify these as needed
    server = False  # Set to True to connect to server, False for local testing
    name = "MyAdXAgent"  # Agent name
    host = "localhost"  # Server host
    port = 8080  # Server port
    verbose = False  # Enable verbose debug output
    game = "adx_twoday"  # Game type (hardcoded for this agent)
    
    if server:
        async def main():
            # Create agent and adapter
            agent = MyTwoDaysTwoCampaignsAgent(name=name)
            # Connect to server
            await connect_agent_to_server(agent, game, name, host, port, verbose)
        # Run the async main function
        import asyncio
        asyncio.run(main())
    else:
        # Test the basic bidding agent locally
        print("Testing MyAdXAgent locally...")
        print("=" * 50)
        # Create all agents for testing
        agent = MyTwoDaysTwoCampaignsAgent(name=name)
        opponent1 = AggressiveAdXAgent()
        random_agents = [RandomAdXAgent(f"RandomAgent_{i}") for i in range(8)]
        
        # Create arena and run tournament
        agents = [agent, opponent1] + random_agents
        arena = LocalArena(
            game_title="adx_twoday",
            game_class=AdxTwoDayGame,
            agents=agents,
            num_agents_per_game=10,
            num_rounds=20,
            timeout=30.0,
            save_results=False,
            verbose=True
        )
        arena.run_tournament()
        
        print("\nLocal test completed!")

# Export for server testing
agent_submission = MyTwoDaysTwoCampaignsAgent()

