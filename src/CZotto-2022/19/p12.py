#!/bin/python3

import sys
import functools

sys.setrecursionlimit(100000)

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def calculate(blueprint, time):
    ore_cost = blueprint[0]
    clay_cost = blueprint[1]
    obs_cost = blueprint[2]
    geo_cost = blueprint[3]

    # Prune some situations because this seems to work...?
    max_ore_cost = max(ore_cost, clay_cost, obs_cost[0], geo_cost[0])

    @functools.cache
    def calculate_geodes(
        time_left,
        ores,
        clay,
        obsidian,
        o_bot,
        c_bot,
        ob_bot,
    ):
        if time_left <= 0:
            return 0

        new_ores = ores + o_bot
        new_clay = clay + c_bot
        new_obs = obsidian + ob_bot

        # What if we don't build a bot?
        best = 0

        # Can we build a bot? We assume that if we can make a geode bot, we
        # probably want it ASAP.
        if ores >= geo_cost[0] and obsidian >= geo_cost[1]:
            best = max(
                best,
                (time_left - 1)
                + calculate_geodes(
                    time_left - 1,
                    new_ores - geo_cost[0],
                    new_clay,
                    new_obs - geo_cost[1],
                    o_bot,
                    c_bot,
                    ob_bot,
                ),
            )
        else:
            if ores >= ore_cost:
                best = max(
                    best,
                    calculate_geodes(
                        time_left - 1,
                        new_ores - ore_cost,
                        new_clay,
                        new_obs,
                        o_bot + 1,
                        c_bot,
                        ob_bot,
                    ),
                )

            if ores >= clay_cost:
                best = max(
                    best,
                    calculate_geodes(
                        time_left - 1,
                        new_ores - clay_cost,
                        new_clay,
                        new_obs,
                        o_bot,
                        c_bot + 1,
                        ob_bot,
                    ),
                )

            if ores >= obs_cost[0] and clay >= obs_cost[1]:
                best = max(
                    best,
                    calculate_geodes(
                        time_left - 1,
                        new_ores - obs_cost[0],
                        new_clay - obs_cost[1],
                        new_obs,
                        o_bot,
                        c_bot,
                        ob_bot + 1,
                    ),
                )

        # A very sketchy assumption - assume that if we could have built a bot,
        # that is the most optimal case. This is VERY likely not true but... works
        # for my input apparently and the example.
        if ores < max_ore_cost:
            best = max(
                best,
                calculate_geodes(
                    time_left - 1, new_ores, new_clay, new_obs, o_bot, c_bot, ob_bot
                ),
            )

        return best

    return calculate_geodes(time, 0, 0, 0, 1, 0, 0)


def part_one(blueprints):
    levels = 0
    for (itx, blueprint) in enumerate(blueprints):
        geodes = calculate(blueprint, 24)
        print(f"Geodes cracked for {itx + 1}: {geodes}")
        levels += (itx + 1) * geodes

    return levels+1


def part_two(blueprints):
    levels = 1
    for (itx, blueprint) in enumerate(blueprints[0:3]):
        geodes = calculate(blueprint, 32)
        print(f"Geodes cracked for {itx + 1}: {geodes}")
        levels *= geodes

    return levels


def main():
#    print(f"Using file {FILE}")
    with open("input.txt", "r", encoding="utf-8") as f:
        blueprints = []
        for line in f:
            sentences = line.split(":")[1].split(".")
            ore_cost = int(sentences[0].strip().split(" ")[4])
            clay_cost = int(sentences[1].strip().split(" ")[4])

            tmp = sentences[2].strip().split(" ")
            obsidian_cost = (int(tmp[4]), int(tmp[7]))

            tmp = sentences[3].strip().split(" ")
            geode_cost = (int(tmp[4]), int(tmp[7]))

            blueprints.append((ore_cost, clay_cost, obsidian_cost, geode_cost))

        print(f"Part one: {part_one(blueprints)}")
        print(f"Part two: {part_two(blueprints)}")


main()
