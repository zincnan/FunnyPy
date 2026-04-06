#!/usr/bin/env python3
"""
ASCII Art Generator - 一个有趣的 ASCII 艺术生成器
支持多种字体、颜色和样式
"""

import random
import sys
import pyfiglet

# ANSI 颜色码
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m',
}

# 彩虹颜色
RAINBOW = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

# 艺术字体模板
FONT_TEMPLATES = {
    'block': [
        "██╗     ██╗███████╗███████╗    ██╗    ██╗ █████╗ ███████╗██╗  ██╗",
        "██║     ██║██╔════╝██╔════╝    ██║    ██║██╔══██╗██╔════╝╚██╗██╔╝",
        "██║     ██║█████╗  ███████╗    ██║ █╗ ██║███████║███████╗ ╚███╔╝ ",
        "██║     ██║██╔══╝  ╚════██║    ██║███╗██║██╔══██║╚════██║ ██╔██╗ ",
        "███████╗██║███████╗███████║    ╚███╔███╔╝██║  ██║███████║██╔╝ ██╗",
        "╚══════╝╚═╝╚══════╝╚══════╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝",
    ],
    'bubble': [
        "  .--.      .--.      .--.      .--.      .--.",
        " :::::.  :::::.  :::::.  :::::.  :::::.  :::::.",
        " :::::'  :::::'  :::::'  :::::'  :::::'  :::::'",
        " `;;`    `;;`    `;;`    `;;`    `;;`    `;;`",
    ],
    'banner': [
        "  ██████╗  ██████╗ ████████╗ ██████╗  ██████╗ ██╗     ",
        "  ██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ",
        "  ██████╔╝██║   ██║   ██║   ██║   ██║██║   ██║██║     ",
        "  ██╔═══╝ ██║   ██║   ██║   ██║   ██║██║   ██║██║     ",
        "  ██║     ╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗",
        "  ╚═╝      ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝",
    ],
    'simple': [
        "   ___  ___  ___  ___  ___  ___  ___  ___  ___",
        "  / _ |/ _ |/ _ || __|| __|/ _ || __|| _ |/ _ |",
        " / /_)| /_)| // || _| | _| / /_)|| _| / // /",
        "/___|/___/|___/ |___||___/|___/ |___/|___/|___/",
    ],
}

# 有趣的短语
QUOTES = [
    "Hello, World! 你好，世界！",
    "Keep Calm and Code On 冷静下来，继续编码",
    "Talk is Cheap, Show Me the Code 空谈廉价，给我看代码",
    "First, solve the problem. Then, write the code 首先解决问题，然后写代码",
    "Code is like humor. When you have to explain it, it's bad 代码就像幽默，解释不清就是烂",
    "It's not a bug, it's a feature 这不是bug，这是特性",
    " reboot the universe 重启宇宙",
    "The best error message is the one that never shows up 最好的错误信息是不显示的那个",
    "A good programmer is someone who always looks both ways before crossing a one-way street 好程序员是过单行道前总看两边的人",
]

# 迷你艺术
MINI_ARTS = {
    'cat': r"""
    /\_/\
   ( o.o )
    > ^ <""",
    'dog': r"""
    / \__
   (    @\___
   /         O
  /   (_____/
 /_____/   U""",
    'fish': r"""
   ><(((('>""",
    'owl': r"""
   ,_,(,_,(,
   (  -.-  )
   o_(")(")""",
    'bear': r"""
   / \__/ \
  ( @  @    )
  /(        )/
  \  \____/ /
   \________/""",
    'penguin': r"""
   _\___/_
  /       \
 |  _   _  |
 ( \/ o_o \/ )
  \  \___/  /
   \_______/""",
    'ghost': r"""
   .-.
  (o o)
  | O |
  |   |
  '~~~'""",
    'skull': r"""
   .-.
  (o o)
  | X |
  |   |
  '~~~'""",
    'alien': r"""
    _____
   /     \
  | o   o |
  |   <   |
   \_____/""",
    'robot': r"""
   .===.
  / o o \
 |   ^   |
 |  \_/  |
  \_____/""",
}


def print_colored(text: str, color: str) -> None:
    """打印彩色文本"""
    color_code = COLORS.get(color, list(COLORS.values())[6])  # white is index 6
    print(f"{color_code}{text}{COLORS['reset']}")


def print_rainbow(text: str) -> None:
    """打印彩虹色文本"""
    for i, char in enumerate(text):
        color = COLORS[RAINBOW[i % len(RAINBOW)]]
        print(f"{color}{char}{COLORS['reset']}", end='')
    print()


def display_mini_art(animal: str) -> None:
    """显示迷你动物艺术"""
    art = MINI_ARTS.get(animal.lower(), MINI_ARTS['cat'])
    for line in art.split('\n'):
        print_colored(line, random.choice(RAINBOW))


def display_font(text: str, font: str = 'block') -> None:
    """显示字体艺术"""
    try:
        art = pyfiglet.figlet_format(text, font=font)
        for line in art.split('\n'):
            print_colored(line, random.choice(RAINBOW))
    except pyfiglet.FontNotFound:
        print_colored(f"字体 '{font}' 未找到，使用默认字体", 'yellow')
        art = pyfiglet.figlet_format(text)
        for line in art.split('\n'):
            print_colored(line, random.choice(RAINBOW))


def spinning_loader(duration: int = 3) -> None:
    """旋转加载动画"""
    import time
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in frames:
            print(f"\r{ random.choice(list(COLORS.values()))}{frame} 加载中...{COLORS['reset']}", end='', flush=True)
            time.sleep(0.1)
    print(f"\r{ random.choice(list(COLORS.values()))}✓ 完成!{COLORS['reset']}  ")


def matrix_rain(duration: int = 5) -> None:
    """矩阵雨效果"""
    import time
    import random as r

    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    columns = min(50, shutil.get_terminal_size().columns)

    end_time = time.time() + duration
    while time.time() < end_time:
        col = r.randint(0, columns - 1)
        line = ''.join(r.choice(chars) for _ in range(r.randint(1, 10)))
        print_colored(f"{' ' * col}{line}", random.choice(RAINBOW))
        time.sleep(0.05)


def magic_8_ball() -> None:
    """魔法8球"""
    import time

    responses = [
        "肯定是的！", "很可能！", "也许吧...", "不太确定",
        "问问别人吧", "肯定不会！", "我的水晶球说是！",
        "这不好说...", "当然是！", "100% 确定！",
    ]

    print_colored("\n🔮 魔法8球 🔮", 'magenta')
    print_colored("思考中", 'cyan')

    for i in range(3):
        print(".", end='', flush=True)
        time.sleep(0.3)
    print()

    print_colored(f"✨ {random.choice(responses)} ✨", 'yellow')


def ascii_cow(text: str) -> None:
    """ASCII 奶牛说话"""
    lines = [
        "        \\   ^__^",
        "         \\  (oo)\\_______",
        "            (__)\\       )\\/\\",
        f"                ||----w |",
        f"                ||     ||",
    ]

    # 包裹文本
    max_len = shutil.get_terminal_size().columns - 10
    words = text.split()
    lines_text = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_len:
            current_line += (" " if current_line else "") + word
        else:
            lines_text.append(current_line)
            current_line = word
    if current_line:
        lines_text.append(current_line)

    # 绘制气泡
    bubble_width = max(len(l) for l in lines_text) + 4
    print(" +" + "-" * bubble_width + "+")
    for l in lines_text:
        print(f" | {l}{' ' * (bubble_width - len(l) - 1)} |")
    print(" +" + "-" * bubble_width + "+")

    # 绘制奶牛
    for line in lines:
        print_colored(line, 'white')


def fortune_teller() -> None:
    """算命先生"""
    import time

    fortunes = [
        ("💼", "今天会遇到贵人相助！"),
        ("📚", "最近适合学习新技能！"),
        ("💰", "财务运势上升中！"),
        ("❤️", "爱情运不错哦！"),
        ("🏃", "今天适合运动！"),
        ("🎨", "创造力爆棚的一天！"),
        ("😴", "休息是为了走更远的路！"),
        ("🚀", "事业运极佳，大展拳脚！"),
    ]

    print_colored("\n🔮 东方神秘算命先生 🔮", 'magenta')
    print_colored("正在解读你的命运...", 'cyan')

    for i in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print()

    icon, fortune = random.choice(fortunes)
    print_colored(f"{icon} {fortune} {icon}", 'yellow')


def rps_game() -> None:
    """石头剪刀布游戏"""
    choices = {'r': '石头 🪨', 'p': '布 📄', 's': '剪刀 ✂️'}

    print_colored("\n🎮 石头剪刀布 🎮", 'cyan')
    print_colored("输入 r (石头), p (布), s (剪刀), q 退出", 'white')

    wins = 0
    losses = 0

    while True:
        user = input("\n你的选择: ").lower().strip()
        if user == 'q':
            print_colored(f"\n📊 最终比分: 胜利 {wins} | 失败 {losses}", 'green')
            break
        if user not in choices:
            print_colored("无效选择！请输入 r, p, s 或 q", 'red')
            continue

        computer = random.choice(['r', 'p', 's'])
        print_colored(f"电脑选择: {choices[computer]}", 'magenta')

        if user == computer:
            result = "平局！"
            color = 'yellow'
        elif (user == 'r' and computer == 's') or \
             (user == 'p' and computer == 'r') or \
             (user == 's' and computer == 'p'):
            result = "你赢了！🎉"
            color = 'green'
            wins += 1
        else:
            result = "你输了！😢"
            color = 'red'
            losses += 1

        print_colored(result, color)


def love_calculator() -> None:
    """爱情计算器"""
    print_colored("\n💕 爱情计算器 💕", 'magenta')

    name1 = input("输入第一个人的名字: ").strip()
    name2 = input("输入第二个人的名字: ").strip()

    if not name1 or not name2:
        print_colored("请输入两个名字！", 'red')
        return

    # 生成一个基于名字的"随机"百分比
    seed = sum(ord(c) for c in name1 + name2)
    random.seed(seed)
    percentage = random.randint(50, 99)

    print()
    bar_len = 30
    filled = int(bar_len * percentage / 100)
    bar = '█' * filled + '░' * (bar_len - filled)

    color = 'green' if percentage >= 80 else 'yellow' if percentage >= 50 else 'red'
    print_colored(f"💖 {name1} + {name2} 💖", 'magenta')
    print_colored(f"[{bar}] {percentage}%", color)

    if percentage >= 90:
        msg = "天生一对！"
    elif percentage >= 70:
        msg = "很有缘分！"
    elif percentage >= 50:
        msg = "还需要努力哦~"
    else:
        msg = "加油！缘分天注定~"
    print_colored(f"✨ {msg} ✨", 'yellow')


import shutil


def show_menu() -> None:
    """显示菜单"""
    menu = """
╔══════════════════════════════════════════════════════╗
║           🎨 ASCII Art Generator 菜单 🎨           ║
╠══════════════════════════════════════════════════════╣
║  1.  🎭  显示艺术字体                                ║
║  2.  🐱  迷你动物艺术                                ║
║  3.  🔮  魔法8球                                     ║
║  4.  🔮  算命先生                                     ║
║  5.  🎮  石头剪刀布                                  ║
║  6.  💕  爱情计算器                                  ║
║  7.  🐄  ASCII 奶牛说话                              ║
║  8.  💬  随机语录                                    ║
║  9.  🌈  彩虹文字                                    ║
║  10. ⏳ 旋转加载动画                                 ║
║  0.  🚪 退出                                         ║
╚══════════════════════════════════════════════════════╝
    """
    print_colored(menu, 'cyan')


def main():
    """主函数"""
    print_colored("""
    ╔═══════════════════════════════════════════╗
    ║   🎨 欢迎来到 ASCII Art Generator! 🎨   ║
    ║       让你的一天更有趣！                  ║
    ╚═══════════════════════════════════════════╝
    """, 'cyan')

    while True:
        show_menu()
        choice = input("\n请选择 (0-10): ").strip()

        if choice == '0':
            print_colored("\n👋 再见！祝你今天愉快！\n", 'green')
            break

        elif choice == '1':
            print_colored("\n选择字体风格:", 'yellow')
            print("1. block  2. standard  3. banner  4. small")
            font_choice = input("选择 (1-4): ").strip()
            fonts = ['block', 'standard', 'banner', 'small']
            idx = int(font_choice) - 1 if font_choice in '1234' else 0
            text = input("输入文字: ") or "test"
            display_font(text, fonts[idx])

        elif choice == '2':
            print_colored("\n选择动物:", 'yellow')
            print("cat, dog, fish, owl, bear, penguin, ghost, skull, alien, robot")
            animal = input("选择动物: ").strip() or 'cat'
            display_mini_art(animal)

        elif choice == '3':
            magic_8_ball()

        elif choice == '4':
            fortune_teller()

        elif choice == '5':
            rps_game()

        elif choice == '6':
            love_calculator()

        elif choice == '7':
            text = input("输入想让奶牛说的话: ") or "Moo~ 我是一只快乐的牛！"
            ascii_cow(text)

        elif choice == '8':
            print_colored(f"\n💬 {random.choice(QUOTES)} 💬\n", 'yellow')

        elif choice == '9':
            text = input("输入彩虹文字: ") or "Rainbow World! 彩虹世界！"
            print()
            print_rainbow(text)

        elif choice == '10':
            print_colored("\n⏳ 开始旋转...", 'cyan')
            spinning_loader(3)

        else:
            print_colored("\n❌ 无效选择，请重新输入！", 'red')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_colored("\n\n👋 程序被中断，再见！\n", 'yellow')
        sys.exit(0)
