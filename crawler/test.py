import random

# unit: fen
MAX_PACKET_MONEY = 20000
MIN_PACKET_MONEY = 1

MAX_PACKET_COUNT = 200
MIN_PACKET_COUNT = 1

class SplitPacket:
    def __init__(self, money, count):
        if not isinstance(money, (int, long)) or \
                money < MIN_PACKET_MONEY * MIN_PACKET_COUNT or \
                money > MAX_PACKET_MONEY * MAX_PACKET_COUNT:
            raise RuntimeError("invalid money")

        if not isinstance(count, (int, long)) or \
                count < MIN_PACKET_COUNT or \
                count > MAX_PACKET_COUNT:
            raise RuntimeError("invalid count")

        if (1.0 * money / count) > MAX_PACKET_MONEY or \
            (1.0 * money / count) < MIN_PACKET_MONEY:
            raise ValueError("unsatisfied parameters")

        self._money = money
        self._count = count

    def get_split_info(self):
        fixed_points = [point for point in
            range(MAX_PACKET_MONEY,
            self._money,
            MAX_PACKET_MONEY)] + [self._money]
        chosen_points = random.sample([point for point in
            range(1, self._money)
            if point not in fixed_points], self._count - len(fixed_points))
        return reduce(lambda init, point: init + [point-sum(init)],
            sorted(fixed_points + chosen_points), [])

print SplitPacket(30000, 4).get_split_info()
