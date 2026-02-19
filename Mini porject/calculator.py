#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║           CALCULUS - Advanced Python Calculator      ║
║   Features: +, -, *, /, %, mean, median, mode, avg  ║
╚══════════════════════════════════════════════════════╝
"""

from statistics import mean, median, mode, multimode, StatisticsError


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

def separator(char="─", width=54):
    print(char * width)

def header(title: str):
    separator("═")
    print(f"  {title}")
    separator("═")

def section(title: str):
    separator()
    print(f"  {title}")
    separator()

def get_number(prompt: str) -> float:
    """Safely get a number from the user with type casting."""
    while True:
        try:
            raw = input(prompt).strip()
            return float(raw)          # type cast: str → float
        except ValueError:
            print(f"  ✘  '{raw}' is not a valid number. Try again.\n")

def get_number_list(prompt: str) -> list[float]:
    """Get a list of numbers from comma/space-separated user input."""
    while True:
        raw = input(prompt).strip()
        try:
            # type cast: str → list[float]
            numbers = [float(x) for x in raw.replace(",", " ").split() if x]
            if not numbers:
                raise ValueError("Empty list")
            return numbers
        except ValueError:
            print("  ✘  Enter valid numbers separated by spaces or commas.\n")

def fmt(n: float) -> str:
    """Format a float: show int if whole number, else up to 8 decimals."""
    return str(int(n)) if n == int(n) else f"{n:.8f}".rstrip("0")


# ─────────────────────────────────────────────
#  BASIC ARITHMETIC
# ─────────────────────────────────────────────

def basic_calculator():
    section("BASIC CALCULATOR  [ +  −  ×  ÷  % ]")

    a = get_number("  Enter first number  : ")
    b = get_number("  Enter second number : ")

    print()
    ops = {
        "1": ("+",  "Addition",       lambda x, y: x + y),
        "2": ("-",  "Subtraction",    lambda x, y: x - y),
        "3": ("*",  "Multiplication", lambda x, y: x * y),
        "4": ("/",  "Division",       lambda x, y: x / y if y != 0 else None),
        "5": ("%",  "Modulus",        lambda x, y: x % y if y != 0 else None),
        "6": ("**", "Power (a^b)",    lambda x, y: x ** y),
    }

    print("  Select operation:")
    for key, (sym, name, _) in ops.items():
        print(f"    [{key}]  {sym}  →  {name}")
    print()

    choice = input("  Your choice: ").strip()

    if choice not in ops:
        print("  ✘  Invalid choice.")
        return

    sym, name, fn = ops[choice]
    result = fn(a, b)

    print()
    separator()
    if result is None:
        print(f"  ✘  Error: Division / Modulus by zero is undefined.")
    else:
        print(f"  {fmt(a)}  {sym}  {fmt(b)}  =  {fmt(result)}")
        print(f"  Operation : {name}")
        print(f"  Result    : {fmt(result)}")
    separator()


# ─────────────────────────────────────────────
#  STATISTICS CALCULATOR
# ─────────────────────────────────────────────

def statistics_calculator():
    section("STATISTICS CALCULATOR  [ mean · median · mode · avg ]")

    numbers: list[float] = get_number_list(
        "  Enter numbers (space or comma separated):\n  > "
    )

    print()
    ops = {
        "1": "Mean (Average)",
        "2": "Median",
        "3": "Mode",
        "4": "All Statistics",
    }

    print("  Select function:")
    for key, name in ops.items():
        print(f"    [{key}]  {name}")
    print()

    choice = input("  Your choice: ").strip()

    print()
    separator()

    if choice == "1":
        result = mean(numbers)          # type cast: list[float] → float
        print(f"  MEAN (Average)")
        print(f"  Numbers : {numbers}")
        print(f"  Sum     : {fmt(sum(numbers))}")
        print(f"  Count   : {len(numbers)}")
        print(f"  Result  : {fmt(result)}")

    elif choice == "2":
        sorted_nums = sorted(numbers)
        result = median(numbers)
        print(f"  MEDIAN")
        print(f"  Sorted  : {sorted_nums}")
        print(f"  Count   : {len(numbers)}")
        print(f"  Result  : {fmt(result)}")

    elif choice == "3":
        try:
            modes = multimode(numbers)
            freq = numbers.count(modes[0])
            print(f"  MODE")
            print(f"  Numbers : {numbers}")
            if len(modes) == 1:
                print(f"  Mode    : {fmt(modes[0])} (appears {freq} time{'s' if freq > 1 else ''})")
            else:
                print(f"  Modes   : {[fmt(m) for m in modes]} (multi-modal, each {freq}×)")
        except StatisticsError:
            print("  ✘  No mode found (all values appear equally).")

    elif choice == "4":
        _show_all_stats(numbers)

    else:
        print("  ✘  Invalid choice.")

    separator()


def _show_all_stats(numbers: list[float]):
    """Display a full statistics report."""
    n = len(numbers)
    total = sum(numbers)                        # type cast accumulation
    avg   = mean(numbers)
    med   = median(numbers)
    mn    = min(numbers)
    mx    = max(numbers)
    rng   = mx - mn

    # Standard deviation (population)
    variance = sum((x - avg) ** 2 for x in numbers) / n
    std_dev  = variance ** 0.5

    try:
        modes = multimode(numbers)
        mode_str = ", ".join(fmt(m) for m in modes)
        freq = numbers.count(modes[0])
        mode_info = f"{mode_str}  (×{freq})"
    except StatisticsError:
        mode_info = "N/A"

    print(f"  ALL STATISTICS REPORT")
    print(f"  Numbers  : {numbers}")
    print()
    print(f"  Count    : {n}")
    print(f"  Sum      : {fmt(total)}")
    print(f"  Mean     : {fmt(avg)}")
    print(f"  Median   : {fmt(med)}")
    print(f"  Mode     : {mode_info}")
    print(f"  Min      : {fmt(mn)}")
    print(f"  Max      : {fmt(mx)}")
    print(f"  Range    : {fmt(rng)}")
    print(f"  Std Dev  : {fmt(std_dev)}")
    print(f"  Variance : {fmt(variance)}")


# ─────────────────────────────────────────────
#  PERCENTAGE CALCULATOR
# ─────────────────────────────────────────────

def percentage_calculator():
    section("PERCENTAGE CALCULATOR  [ % ]")

    ops = {
        "1": "X% of Y            →  e.g. 15% of 200 = 30",
        "2": "Percentage change  →  From A to B",
        "3": "X is what % of Y  →  e.g. 45 out of 300",
        "4": "Add X% to Y        →  e.g. Y + tax",
        "5": "Subtract X% from Y →  e.g. Y - discount",
    }

    print("  Select operation:")
    for key, name in ops.items():
        print(f"    [{key}]  {name}")
    print()

    choice = input("  Your choice: ").strip()
    print()
    separator()

    if choice == "1":
        pct = get_number("  Percentage (X) : ")
        total = get_number("  Total (Y)      : ")
        result = (pct / 100) * total           # type cast: str → float → calc
        print(f"\n  {fmt(pct)}% of {fmt(total)}  =  {fmt(result)}")

    elif choice == "2":
        a = get_number("  From (original) : ")
        b = get_number("  To (new value)  : ")
        if a == 0:
            print("\n  ✘  Original value cannot be zero.")
        else:
            change = ((b - a) / abs(a)) * 100
            direction = "increase ▲" if change >= 0 else "decrease ▼"
            print(f"\n  {fmt(a)}  →  {fmt(b)}")
            print(f"  Change   : {'+' if change >= 0 else ''}{fmt(change)}%  ({direction})")

    elif choice == "3":
        part  = get_number("  Part (X)  : ")
        whole = get_number("  Whole (Y) : ")
        if whole == 0:
            print("\n  ✘  Whole cannot be zero.")
        else:
            pct = (part / whole) * 100
            print(f"\n  {fmt(part)} is {fmt(pct)}% of {fmt(whole)}")

    elif choice == "4":
        pct = get_number("  Add percentage (X%) : ")
        val = get_number("  To value (Y)        : ")
        added  = (pct / 100) * val
        result = val + added
        print(f"\n  {fmt(val)} + {fmt(pct)}%  ({fmt(added)})  =  {fmt(result)}")

    elif choice == "5":
        pct = get_number("  Subtract percentage (X%) : ")
        val = get_number("  From value (Y)           : ")
        removed = (pct / 100) * val
        result  = val - removed
        print(f"\n  {fmt(val)} − {fmt(pct)}%  ({fmt(removed)})  =  {fmt(result)}")

    else:
        print("  ✘  Invalid choice.")

    separator()


# ─────────────────────────────────────────────
#  EXPRESSION EVALUATOR
# ─────────────────────────────────────────────

def expression_evaluator():
    section("EXPRESSION EVALUATOR  [ type a math expression ]")
    print("  Examples:  3 + 4 * 2     100 / 5 - 3     2 ** 8     15 % 4")
    print("  Type 'back' to return.\n")

    while True:
        expr = input("  >> ").strip()
        if expr.lower() in ("back", "b", "exit", "q"):
            break
        if not expr:
            continue
        try:
            # Safe eval: only allow numbers and math operators
            allowed = set("0123456789 .+-*/%()^e")
            sanitized = expr.replace("^", "**")
            if any(c not in allowed and not c.isalpha() for c in sanitized):
                print("  ✘  Unsafe expression.\n")
                continue
            result = eval(sanitized, {"__builtins__": {}})  # type cast: str → numeric result
            print(f"  =  {fmt(float(result))}\n")
        except ZeroDivisionError:
            print("  ✘  Division by zero.\n")
        except Exception:
            print("  ✘  Invalid expression.\n")


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def main():
    header("  CALCULUS — Advanced Python Calculator")
    print("  Type casting · Arithmetic · Statistics · Percentages")
    print()

    menu = {
        "1": ("Basic Calculator     [ +  −  ×  ÷  %  ^ ]",  basic_calculator),
        "2": ("Statistics           [ mean · median · mode · avg ]", statistics_calculator),
        "3": ("Percentage Tool      [ %  change  ratio ]",   percentage_calculator),
        "4": ("Expression Evaluator [ type any expression ]", expression_evaluator),
        "0": ("Exit", None),
    }

    while True:
        print()
        section("MAIN MENU")
        for key, (label, _) in menu.items():
            print(f"  [{key}]  {label}")
        print()

        choice = input("  Select option: ").strip()

        if choice == "0":
            print()
            separator("═")
            print("  Goodbye! 👋")
            separator("═")
            break
        elif choice in menu:
            label, fn = menu[choice]
            print()
            try:
                fn()
            except KeyboardInterrupt:
                print("\n  ↩  Returning to menu...")
        else:
            print("  ✘  Invalid option. Choose 0–4.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Exiting. Goodbye! 👋\n")
