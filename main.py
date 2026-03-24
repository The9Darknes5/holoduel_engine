from holoduel_engine.engine.game_state import GameState
from holoduel_engine.players.player import Player
from holoduel_engine.cards.monster import Monster


def main():
    game = GameState()

    p1 = Player(1, "Yugi")
    p2 = Player(2, "Kaiba")

    game.add_player(p1)
    game.add_player(p2)

    game.start_game()

    print("Turno actual:", game.turn_player)
    print("Turno número:", game.turn_count)
    print("Zonas totales:", len(game.field.get_all_zones()))

    blue_eyes = Monster("Blue-Eyes White Dragon", 3000, 2500)

    game.summon_monster(1, blue_eyes)

    game.build_chain()

    player_field = game.field.get_player_field(1)

    for i, zone in enumerate(player_field.main_monster_zones):
        if not zone.is_empty():
            print(f"Zona {i}: {zone.card.name}")

    activatables = game.get_activatable_cards(1)

    print("Cartas activables:")
    for card in activatables:
        print(card.name)


if __name__ == "__main__":
    main()