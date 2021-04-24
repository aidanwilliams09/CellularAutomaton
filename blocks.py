import onedim.onedim as od
import gui

def main():
    rule = int(input('Enter ruleset (0-255): '))
    max_gens = int(input('Enter the amount of generations: '))
    first_gen = [0 for i in range(100)]
    first_gen[100 // 2] = 1
    ruleset = [int(b) for b in format(rule, 'b').zfill(8)]
    cur_gen = [int(cell) for cell in first_gen]

    print(*cur_gen)
    for i in range(max_gens):
        cur_gen = od.generate_next_gen(cur_gen, ruleset)
        print(*cur_gen)


if __name__ == '__main__':
    #main()
    gui.window()
