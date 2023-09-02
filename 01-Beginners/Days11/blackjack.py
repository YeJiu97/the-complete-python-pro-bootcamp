import os
import random
import time

"""
项目说明：
1. 去掉Q,J,K,A算作是11或者1
2. 一副牌四个花色，一共四副牌
3. 两个玩家，一个保守策略，一个激进策略
4. 运行多次，从统计上查看结果
"""

GAME_TIMES = 10000
TURN_GAP = 0.01


# 打招呼
def greet():
    """This function will print greet sentence to players"""
    print("""
    ======================Welcome to Black Jack====================
    """)


# 生成卡组
def create_card():
    """This function will create a card list for the game"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4 * 4  # 四色，四副牌，A先算作是11，爆了可以改成1
    random.shuffle(cards)  # 进行一次洗牌
    return cards


# 开始进行抽牌
def send_card(left_cards):
    """This function will randomly select a card from the left cards"""
    select_card = left_cards.pop(
        random.randint(1, len(left_cards) - 1))  # random select a card but not the first or last
    return select_card, left_cards


# 计算手上的牌的分数
def calculate_score(hand_cards):
    """This function will calculate the score of cards on hand"""

    # swift A from 11 to 1 if over 21
    if sum(hand_cards) > 21 and 11 in hand_cards:
        hand_cards.remove(11)
        hand_cards.append(1)

    return sum(hand_cards)


# 展示手牌
def display_cards(player_1, player_2, dealer):
    """This function will show all cards on hand"""
    print(f"Player 1's cards is {player_1}, the total score is {calculate_score(player_1)}")
    print(f"Player 2's cards is {player_2}, the total score is {calculate_score(player_2)}")
    print(f"Dealer's cards is {dealer}, the total score is {calculate_score(dealer)}")


# 比较大小
def compare_score(player_1_score, player_2_score, dealer_score):
    """This function will compare scores and return a result"""

    # 有一方是21点的情况
    if dealer_score == 21:
        return "Dealer Win!"  # 因为相同分数dealer取胜
    if player_1_score == 21 or player_2_score == 21:
        return "Players Win!"  # 由于Python从上往下按照顺序来进行执行

    # 玩家1小于21点的情况
    if player_1_score < 21:
        # 如果玩家2也小于21
        if player_2_score < 21:
            # 如果庄家高于了21
            if dealer_score > 21:
                return "Players Win!"
            # 如果庄家没有高于21
            else:
                # 此时三者都小于了21，当两个玩家没有任意一者高于庄家的时候，庄家取得胜利
                if player_1_score <= dealer_score and player_2_score <= dealer_score:
                    return "Dealer Win!"
                else:
                    # 其他情况，也就是有至少一者高于了庄家，但是小于21点
                    return "Players Win!"
        # 接着开始考虑玩家2大于21点的情况
        else:
            # 只需要比较player_1和dealer
            if player_1_score <= dealer_score:  # 持平或者小于，则庄家胜利
                return "Dealer Win!"
            else:  # 否则玩家胜利
                return "Players Win!"
    # 考虑玩家1大于了21点的情况
    else:
        # 考虑玩家2超过21点的情况
        if player_2_score > 21:
            return "Dealer Win!"  # 无论庄家是否超过21点，只要都超过21点，就算做是庄家的胜利，此时两位玩家已经失败
        # 考虑玩家2没有超过21点的情况
        else:
            if player_2_score <= dealer_score:  # 小于或者持平都是庄家获胜
                return "Dealer Win!"
            else:  # 否则则是玩家获胜
                return "Players Win!"


# 游戏运行函数
def run_game():
    """This function will run the black jack game"""

    greet()  # 先打个招呼
    new_cards = create_card()  # 给出一副打乱的卡组

    # 三方开始的时候手里都是空牌
    player_1 = []
    player_2 = []
    dealer = []

    # 开始发牌, 一人两张
    for _ in range(2):
        card_got, new_cards = send_card(new_cards)
        player_1.append(card_got)

    for _ in range(2):
        card_got, new_cards = send_card(new_cards)
        player_2.append(card_got)

    for _ in range(2):
        card_got, new_cards = send_card(new_cards)
        dealer.append(card_got)

    # 展示一下大家的手牌
    print("Current Situation:")
    display_cards(player_1, player_2, dealer)

    # 计算一下分数
    player_1_score = calculate_score(player_1)
    player_2_score = calculate_score(player_2)
    dealer_score = calculate_score(dealer)

    # 判断游戏是否继续
    # 如果庄家21点，庄家直接胜利
    if dealer_score == 21:
        print("Dealer Win!")
        return "Dealer Win!"
    # 如果玩家21点，但是庄家没有21点，则玩家直接胜利
    elif player_1_score == 21 or player_2_score == 21:
        print("Player Win!")
        return "Players Win!"
    # 否则继续游戏
    else:
        # 玩家一先开始，采取较为激进的策略
        # 计算剩余的牌的平均值，将其作为抽牌的预期，高于这个值的20%作为可以接受的范围
        while player_1_score + sum(new_cards) / len(new_cards) < 21 * 1.2:
            card_got, new_cards = send_card(new_cards)
            player_1.append(card_got)
            player_1_score = calculate_score(player_1)

        # 玩家二则采取更加保守的路测，因为玩家一出现问题的可能性比较大，所以玩家二进行兜底
        while player_2_score + sum(new_cards) / len(new_cards) < 21 * 0.8:
            card_got, new_cards = send_card(new_cards)
            player_2.append(card_got)
            player_2_score = calculate_score(player_2)

        # 庄家在总分低于17的时候必须再抽一张牌
        while dealer_score < 17:
            card_got, new_cards = send_card(new_cards)
            dealer.append(card_got)
            dealer_score = calculate_score(dealer)

        # 开始进行比较用来判断结果
        result = compare_score(player_1_score, player_2_score, dealer_score)
        print(result)
        display_cards(player_1, player_2, dealer)
        return result


def result_statistics():
    """This function will run the game for a large number times"""
    dealer_win = 0
    players_win = 0

    for _ in range(GAME_TIMES):
        os.system("cls")
        result = run_game()
        if result == "Players Win!":
            players_win += 1
        else:
            dealer_win += 1

        print(f"Current Outcome: Players Win: {players_win}, Dealer Win: {dealer_win}")
        print(f"")
        time.sleep(TURN_GAP)

    if players_win > dealer_win:
        print("Players take a good strategy to win the black jack game")
    else:
        print("The strategy of players may not be a good one")


if __name__ == '__main__':
    result_statistics()