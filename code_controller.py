class Code_controller:
    right_codes = [
        'code1',
        'code2',
        'code3',
        'code4',
    ]
    def __init__(self, player):
        self.player = player

    def is_checked(self, code):
        level = self.player.game.num_level
        return code == self.right_codes[level - 1]

    def check_code(self, code):
        level = self.player.game.num_level
        levels_count = len(self.player.game.levels)
        screen = self.player.game.screen

        if not self.is_checked(code):
            return False

        if level < levels_count - 1:
            if level == 1:
                self.player.brumbrum(screen)
                self.player.change_level(screen, 'WHERE ARE YOU?')
            elif level == 2:
                self.player.change_level(screen, '! ! ! ! !  RUN  ! ! ! ! !')
            else:
                self.player.change_level(screen, 'WHERE ARE YOU?')
            self.player.game.num_level += 1
            self.player.game.new_game()

        return True
