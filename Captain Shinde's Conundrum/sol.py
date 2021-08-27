def solution(ammo_damage):
    gun_1 = 0
    gun_2 = 0

    num_reloads = 0

    for i in range(len(ammo_damage)):
        if ammo_damage[i] == gun_1 or ammo_damage[i] == gun_2:
            continue
        else:
            picked = False
            for j in ammo_damage[i+1:]:
                if j == gun_1:
                    num_reloads += 1
                    gun_2 = ammo_damage[i]
                    picked = True
                    break
                elif j == gun_2:
                    num_reloads += 1
                    gun_1 = ammo_damage[i]
                    picked = True
                    break
                else:
                    continue

            if not picked:
                num_reloads += 1
                gun_1 = ammo_damage[i]

    return num_reloads


cases = int(input())
for times in range(cases):
    num_levels = int(input())
    ammo_damage = [int(x) for x in input().split()]

    print(solution(ammo_damage))
