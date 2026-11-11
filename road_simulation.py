"""
road_simulation.py
Full Self Driving Simulation mode in Kigali: ALU Rwanda -> Convention Center

Your job: complete TODO 1 to TODO 10 below (replace each `pass`).
Do NOT edit engine.py, index.html or transit_program.py.
Run with:   python road_simulation.py or python3 road_simulation.py
"""

SEGMENT_M = 100
ZEBRA_WAIT = 5
ACCELERATION = 5
BRAKING = 20
START_NAME = "ALU Rwanda"
END_NAME = "Convention Center"

# Each item in the road list is ONE segment of road. On the screen each segment is 100 m long
road = [
    "60", "road", "road", "road", "zebra", "road", "road",
    "80", "road", "road", "road", "road", "road", "road",
    "bus", "road", "road", "bus", "road", "road","road",
    "60", "road", "road", "road", "road","80", "road", 
    "road","zebra", "road", "road","road", "road",
]


# ==================== PART 1: CHECK THE SIGN ====================

# TODO 1: Return True only if sign is text AND is "bus", "zebra",
# or a number from 20 to 100 written as text (e.g. "80"). Otherwise False.
def is_valid_sign(sign):
    if not isinstance(sign, str):
        return False
    if sign in ("bus", "zebra"):
        return True
    if not sign.isascii() or not sign.isdecimal():
        return False
    number_text = sign.lstrip("0") or "0"
    if len(number_text) > 3:
        return False
    return 20 <= int(number_text) <= 100


# TODO 2: Return "bus", "zebra", "speed" (a number) or "road" (anything else).
def get_sign_type(sign):
    if sign == "bus":
        return "bus"
    if sign == "zebra":
        return "zebra"
    if is_valid_sign(sign):
        return "speed"
    return "road"


# ==================== PART 2: TAKE ACTION ====================

# TODO 3: If the sign is a speed sign, return its number as an int. Else return current_limit.
def get_speed_limit(sign, current_limit):
    if get_sign_type(sign) == "speed":
        return int(sign.lstrip("0") or "0")
    return current_limit


# TODO 4: Return 0 while stop_timer is above 0, otherwise return limit.
def get_target_speed(limit, stop_timer):
    if stop_timer > 0:
        return 0
    return limit


# TODO 5: Move speed ONE step towards target and return it.
# Below target: add ACCELERATION (never go above target).
# Above target: subtract BRAKING (never go below target).
def adjust_speed(speed, target):
    if speed < target:
        return min(speed + ACCELERATION, target)
    if speed > target:
        return max(speed - BRAKING, target)
    return speed


# TODO 6: Use a loop. Return (speed_signs, zebras, buses).
def count_signs(road_list):
    speed_signs = 0
    zebras = 0
    buses = 0
    for sign in road_list:
        sign_type = get_sign_type(sign)
        if sign_type == "speed":
            speed_signs += 1
        elif sign_type == "zebra":
            zebras += 1
        elif sign_type == "bus":
            buses += 1
    return speed_signs, zebras, buses


# ==================== PART 3: SAFE INPUT AND JOURNEY SUMMARY ====================

# TODO 7: Keep asking until the user types a whole number from low to high.
# Use try/except for text that is not a number. Return the number as an int.
def ask_for_number(question, low, high):
    while True:
        try:
            number = int(input(question))
        except ValueError:
            print(f"  Please enter a whole number from {low} to {high}.")
            continue
        if low <= number <= high:
            return number
        print(f"  Please enter a whole number from {low} to {high}.")


# TODO 8: Insert sign at position. Return False if position is not from 0 to len(road_list).
# Otherwise insert and return True.
def insert_sign(road_list, sign, position):
    if not is_valid_sign(sign) or not isinstance(position, int):
        return False
    if not 0 <= position <= len(road_list):
        return False
    road_list.insert(position, sign)
    return True


# TODO 9: Replace the sign at index with a new sign. Return False if index is not
# from 0 to len(road_list) - 1. Otherwise replace it and return True.
def replace_sign(road_list, sign, index):
    if not is_valid_sign(sign) or not isinstance(index, int):
        return False
    if not 0 <= index < len(road_list):
        return False
    road_list[index] = sign
    return True


# TODO 10: Summarise the journey. Use a loop to count the signs we pass
# (every segment that is not "road"). Return four values:
# (signs_passed, length_m, START_NAME, END_NAME)
# length_m is the number of segments times SEGMENT_M.
def get_journey_summary(road_list):
    signs_passed = 0
    for sign in road_list:
        if sign != "road":
            signs_passed += 1
    length_m = len(road_list) * SEGMENT_M
    return signs_passed, length_m, START_NAME, END_NAME


if __name__ == "__main__":
    import sys
    import transit_program
    transit_program.run(sys.modules[__name__])
