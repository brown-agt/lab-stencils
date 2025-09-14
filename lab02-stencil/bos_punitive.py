from agt_server.agents.base_agents.bos_agent import BOSAgent
from agt_server.local_games.bos_arena import BOSArena


class PunitiveAgent(BOSAgent):
    def setup(self):
        self.COMPROMISE, self.STUBBORN = 0, 1
        self.GOOD_MOOD, self.BAD_MOOD = 0, 1
        self.actions = [self.COMPROMISE, self.STUBBORN]
        self.curr_state = 0

    def get_action(self):
        if self.curr_state in [1, 3]:
            return self.COMPROMISE
        else:
            return self.STUBBORN

    def update(self):
        opp_last_move = self.get_opp_last_action()
        if self.curr_state == 0:
            if opp_last_move == self.STUBBORN:
                self.curr_state = 1
            else:
                self.curr_state = 0
        elif self.curr_state == 1:
            self.curr_state = 2
        elif self.curr_state == 2:
            if opp_last_move == self.STUBBORN:
                self.curr_state = 3
            else:
                self.curr_state = 2
        else:
            self.curr_state = 4

if __name__ == "__main__":
    agent_name = "PunitiveAgent"

    agent = PunitiveAgent(agent_name)
    arena = BOSArena(
        num_rounds=1000,
        timeout=1,
        players=[
            agent,
            PunitiveAgent("Agent_1"),
            PunitiveAgent("Agent_2"),
            PunitiveAgent("Agent_3"),
            PunitiveAgent("Agent_4")
        ]
    )
    arena.run()
