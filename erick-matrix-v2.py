import curses, random, time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    sh, sw = stdscr.getmaxyx()
    chars = "01ERICKAI01"
    drops = [random.randint(-sh, 0) for _ in range(sw)]

    while True:
        for i in range(sw):
            c = random.choice(chars)
            y = drops[i]
            if 0 <= y < sh-1:
                # rastro verde
                stdscr.addstr(y, i, c, curses.color_pair(1))
                # cabeça branca brilhante
                if y > 0:
                    stdscr.addstr(y-1, i, c, curses.color_pair(2) | curses.A_BOLD)
            drops[i] += 1
            if drops[i] > sh and random.random() > 0.85:
                drops[i] = 0
        stdscr.refresh()
        time.sleep(0.05)
        if stdscr.getch() != -1:
            break

curses.wrapper(main)
