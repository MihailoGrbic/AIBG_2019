from Bot import Bot
from Bot import actions
from BotWalker import BotWalker
from GameState import GameState
import utils


class BotAttackWithSword(Bot):

    def __init__(self):
        super().__init__()
        self.bot_walker = BotWalker()

    def play_single_turn(self, current_game_state: GameState):
        if utils.dist(current_game_state.self_info.x, current_game_state.self_info.y, current_game_state.other_info.x,
                      current_game_state.other_info.y) == 1:
            if current_game_state.other_info.x == current_game_state.self_info.x + 1:
                return actions["SWORD_RIGHT"]
            if current_game_state.other_info.x == current_game_state.self_info.x - 1:
                return actions["SWORD_LEFT"]
            if current_game_state.other_info.y == current_game_state.self_info.y + 1:
                return actions["SWORD_DOWN"]
            if current_game_state.other_info.y == current_game_state.self_info.y - 1:
                return actions["SWORD_UP"]
        else:
            self.bot_walker.x_sel = current_game_state.other_info.x
            self.bot_walker.y_sel = current_game_state.other_info.y
            return self.bot_walker.play_single_turn(current_game_state)
