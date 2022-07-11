from functools import reduce


def alternatingSums(elements):
    a = [team[1] for team in enumerate(elements) if team[0] % 2 == 0]
    b = [team[1] for team in enumerate(elements) if team[0] % 2 == 1]
    team_a = reduce(lambda x, y: x+y, a, 0)
    team_b = reduce(lambda x, y: x+y, b, 0)
    return [team_a, team_b]
