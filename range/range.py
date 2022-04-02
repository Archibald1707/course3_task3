class Range:
    def __init__(self, start=0, end=0):
        if start < end:
            self.unit = [start, end]
        else:
            self.unit = []

    def is_empty(self) -> bool:
        return self.unit == []

    def is_inside(self, point) -> bool:
        if self.unit == []:
            return False
        return self.rmin() <= point <= self.rmax()

    def __eq__(self, comparable):
        return self.unit == comparable.unit

    def __and__(self, comparable):
        if self.is_empty() or comparable.is_empty():
            return False
        elif self.rmin() >= comparable.rmax() or comparable.rmin() >= self.rmax():
            return False
        return True

    def __gt__(self, comparable):
        if self.is_empty():
            return False
        return self * comparable == comparable.unit

    def __lt__(self, comparable):
        if self.is_empty():
            return False
        return self * comparable == self.unit

    # intersection
    def __mul__(self, comparable):
        if not self & comparable:
            return []
        return [
            max(self.rmin(), comparable.rmin()),
            min(self.rmax(), comparable.rmax()),
        ]

    # ingoing
    def __add__(self, comparable):
        if not self & comparable:
            return []
        else:
            return [
                min(self.rmin(), comparable.rmin()),
                max(self.rmax(), comparable.rmax()),
            ]

    def print_range(self):
        output_string = f"{self.rmin()}"
        for i in range(self.rmin() + 1, self.rmax() + 1):
            output_string += f", {i}"
        return output_string

    def rmax(self):
        if self.is_empty():
            return None
        return self.unit[1]

    def rmin(self):
        if self.is_empty():
            return None
        return self.unit[0]

    def to_string(self):
        if self.is_empty():
            return "[]"
        return f"[{self.rmin()}, {self.rmax()}]"
