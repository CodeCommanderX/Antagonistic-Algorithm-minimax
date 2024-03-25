import numpy as np #thư viện numpy
import pandas as pd #thư viện pandas
from typing import Tuple
player_o = 1
player_x = -1


def phan_khang(player): 
    #hàm phản kháng
    #:param player: người chơi
    #:return: trả lại node đi của người đánh ban đầu
    opponent = player_o if player == player_x else player_x
    return opponent


class State:

    def __init__(self, board, player):
        self.board = board.copy()
        self.player = player

    def __eq__(self, other):
        if (self.board == other.board).all() and self.player == other.player:
            return True
        else:
            return False

    def Kiemtra_node_di_san_co(self): #kiểm tra các node đã đi sẵn
        space = np.where(self.board == 0)
        coordinate = zip(space[0], space[1])
        available_actions = [(i, j) for i, j in coordinate]
        return available_actions

    def nhan_giatri_kq_trangthai(self): #Nhận giá trị về trạng thái
        #Trả về kết quả của tình trạng tương ứng với trạng thái
        #Nếu trò chơi kết thúc is_over = True nếu không có is_over = False, winner = None
        #Nếu trò chơi kết thúc, có ba kết quả: thắng x, thắng o, hòa
        #người chiến thắng có thể lấy [x, o, None] ba trường hợp này
        #:return: trả lại một tuple(is_over, winner)
        board = self.board
        sum_row = np.sum(board, 0)
        sum_col = np.sum(board, 1)
        diag_sum_tl = board.trace()
        diag_sum_tr = np.fliplr(board).trace()

        n = self.board.shape[0]
        if (sum_row == n).any() or (sum_col == n).any() or diag_sum_tl == n or diag_sum_tr == n:
            is_over, winner = True, player_o
        elif (sum_row == -n).any() or (sum_col == -n).any() or diag_sum_tl == -n or diag_sum_tr == -n:
            is_over, winner = True, player_x
        elif (board != 0).all():
            is_over, winner = True, None
        else:
            is_over, winner = False, None

        return is_over, winner

    def trangthai_tieptheo(self, action): #Đưa ra kết quả tiếp theo dựa trên trạng thái hiện tại
        next_board = self.board.copy()
        next_board[action] = self.player
        next_player = phan_khang(self.player)
        next_state = State(next_board, next_player)
        return next_state  #:return: trạng thái mới


class Game:
    start_player = player_o
    game_size = 3

    def __init__(self, state=None):
        if state:
            if state.board.shape[0] != Game.game_size:
                raise Exception("Kích thước bảng được sử dụng để khởi tạo bị sai")

            board = state.board
            player = state.player
        else:
            board = np.zeros((Game.game_size, Game.game_size), dtype=np.int32)
            player = Game.start_player
        self.state = State(board, player)

    def khoitao_vitri(self, state=None):
        #Khởi tạo tình huống trò chơi
        #Nó có thể được khởi tạo theo mặc định hoặc có thể được khởi tạo bằng trạng thái bên ngoài.
        #:param state: Không có nghĩa là khởi tạo mặc định, các trường hợp khác là khởi tạo bằng trạng thái bên ngoài
        if state:
            if state.board.shape[0] != Game.game_size:
                raise Exception("Kích thước bảng được sử dụng để khởi tạo bị sai")
            board = state.board
            player = state.player
            self.state = State(board, player)
        else:
            self.state.board = np.zeros((Game.game_size, Game.game_size), dtype=np.int32)
            self.state.player = Game.start_player
        return self.state

    def capnhat_trangthai_tieptheo(self, action):
        #Thực hiện hành động đối với tình huống, thực hiện hành động này sẽ sửa đổi trạng thái hiện tại của trò chơi
        #:param action: Ở một vị trí mà bạn có thể di chuyển
        #:return: trạng thái mới
        if action:
            self.state = self.state.trangthai_tieptheo(action)
        return self.state

    def trakq_trochoi(self):
        #Trả về kết quả của trò chơi sau khi thực hiện một hành động
        #:return: tuple (is_over, winner)
        return self.state.nhan_giatri_kq_trangthai()

    def xuat_bangtao_moi(self, board=None):
        #Kết xuất tình huống hiện tại và sử dụng các tình huống bên ngoài để kết xuất
        #:param board: Không có nghĩa là sử dụng tình huống của chính nó để hiển thị, trong các trường hợp khác, sử dụng tình huống bên ngoài để hiển thị
        #:return:
        if board:
            if board.shape[0] != Game.game_size:
                raise Exception("Kích thước bảng được sử dụng để khởi tạo bị sai")
        else:
            board = self.state.board

        for i in range(Game.game_size):
            for j in range(Game.game_size):
                if board[i, j] == player_x:
                    print(" X ", end="")
                elif board[i, j] == player_o:
                    print(" O ", end="")
                else:
                    print(" . ", end="")
            print()

class Human:
    def __init__(self):
        pass

    def __str__(self):
        return "Người đánh"

    def take_action(self, current_state):
        #Người chơi của con người thực hiện hành động
        #:param current_state: tình trạng hiện tại
        #:return: hành động tối ưu
        while True:
            while True:
                command = input("Nhập nước đi của bạn ở dạng i, j, i là hàng ngang, j là hàng dọc ,ví dụ: 1,2:")
                try:
                    i, j = [int(index) for index in command.split(",")]
                    break
                except:
                    print("Định dạng đầu vào không chính xác, vui lòng nhập lại")
            action = i, j
            if action not in current_state.Kiemtra_node_di_san_co():
                print("Có sự cố với vị trí nhập, vui lòng nhập lại")
            else:
                break
        return action

class MiniMax:

    def __init__(self):
        pass

    def __str__(self):
        return "MiniMax AI"

    def take_action(self, current_state: State):

        def recurse(state: State) -> Tuple[int, object]:
            #Trả về trạng thái tốt nhất hiện tại và hành động tương ứng dựa trên trạng thái hiện tại
            #:param state: trạng thái hiện tại
            #:return: trả lại một tuple (utility action)
            is_over, winner = state.nhan_giatri_kq_trangthai()
            if is_over:
                if winner == state.player:
                    return 1, None
                elif winner == phan_khang(state.player):
                    return -1, None
                else:
                    return 0, None

            available_actions = state.Kiemtra_node_di_san_co()
            values = [- recurse(state.trangthai_tieptheo(action))[0] for action in available_actions]
            kws = pd.Series(data=values, index=available_actions)
            action = kws.idxmax()
            return kws[action], action

        _, action = recurse(current_state)
        return action



class AlphaBeta:

    def __init__(self):
        pass

    def __str__(self):
        return "Máy đánh sử dụng Minimax và kỹ thuật cắt tỉa alpha-beta"

    def take_action(self, current_state: State):
        self.player = current_state.player
        def recurse(state: State, alpha, beta) -> Tuple[int, object]:
            #Trả về trạng thái tốt nhất hiện tại và hành động tương ứng dựa trên trạng thái hiện tại
            #:param state: trạng thái hiện tại
            #:param alpha: Giới hạn dưới của doanh thu của người chơi cho đến đầu trạng thái hiện tại
            #:param beta:  Giới hạn trên đối với phần thưởng của người chơi đối thủ nhiều nhất ở trạng thái kết thúc
            #:return: trả lại một tuple (utility action)
            is_over, winner = state.nhan_giatri_kq_trangthai()
            if is_over:
                if winner == self.player:
                    return 1, None
                elif winner == phan_khang(self.player):
                    return -1, None
                else:
                    return 0, None

            available_actions = state.Kiemtra_node_di_san_co()
            if state.player == self.player:
                max_value = (float("-inf"), None)
                for action in available_actions:
                    max_value = max(max_value, (recurse(state.trangthai_tieptheo(action), alpha, beta)[0], action), key=lambda x:x[0])
                    alpha = max(alpha, max_value[0])
                    if beta <= alpha:
                        break
                return max_value
            elif state.player == phan_khang(self.player):
                min_value = (float("inf"), None)
                for action in available_actions:
                    min_value = min(min_value, (recurse(state.trangthai_tieptheo(action), alpha, beta)[0], action), key=lambda x:x[0])
                    beta = min(beta, min_value[0])
                    if beta <= alpha:
                        break
                return min_value

        _, action = recurse(current_state, float("-inf"), float("inf"))
        return action


if __name__ == '__main__':
    game = Game()
    human = Human()
    ai = AlphaBeta()
    players = {0: ai, 1: human}

    turn = 1
    while True:
        current_state = game.state
        action = players[turn].take_action(current_state)
        game.capnhat_trangthai_tieptheo(action)
        game.xuat_bangtao_moi()
        print("{0} rơi vào vị trí {1}".format(players[turn], action))

        # kết quả quan trọng
        is_over, winner = game.trakq_trochoi()
        if is_over:
            if winner:
                print("bên thắng : {0}".format(players[turn]))
            else:
                print("không bên nào thắng")
            break

        # Cập nhật trình phát
        turn = (turn + 1) % 2

