def climbing_leaderboard(ranked, player):
    for i in range(len(player)):
        table = ranked.copy()
        inserted = False
        for j in range(len(table)):
            if player[i] >= table[j]:
                table.insert(j, "a")
        if not inserted:
            table.append("a")
        result_arr = []
        for element in table:
            if element not in result_arr:
                result_arr.append(element)
        print(f"{result_arr.index('a') + 1} ")


leaderboard = [100, 100, 50, 40, 40, 20, 10]
p_runs = [5, 25, 50, 120]
climbing_leaderboard(leaderboard, p_runs)
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
