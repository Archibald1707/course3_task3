class Range:
    def __init__(self, start=0, finish=0):
        if start < finish:
            self._end = [start, finish]
        else:
            self._end = []

    def is_empty(self) -> bool:
        return self._end == []

    def __contains__(self, point) -> bool:
        if self.is_empty():
            return False
        return self.range_min() <= point <= self.range_max()

    def __eq__(self, comparable):
        return self._end == comparable._end

    # do range's intersect?
    def is_intersect(self, comparable):
        if self.is_empty() or comparable.is_empty():
            return False
        elif (
            self.range_min() >= comparable.range_max()
            or comparable.range_min() >= self.range_max()
        ):
            return False
        return True

    def __gt__(self, comparable):
        if self.is_empty():
            return False
        return self & comparable == comparable

    def __lt__(self, comparable):
        if self.is_empty():
            return False
        return self & comparable == self

    # intersection
    def __and__(self, comparable):
        if not self.is_intersect(comparable):
            return []
        return Range(
            max(self.range_min(), comparable.range_min()),
            min(self.range_max(), comparable.range_max()),
        )

    # union
    def __or__(self, comparable):
        if not self.is_intersect(comparable):
            return []
        else:
            return Range(
                min(self.range_min(), comparable.range_min()),
                max(self.range_max(), comparable.range_max()),
            )

    def __iter__(self):
        if self.is_empty():
            return iter([])
        return iter([i for i in range(self.range_min(), self.range_max() + 1)])

    def range_max(self):
        if self.is_empty():
            return None
        return self._end[1]

    def range_min(self):
        if self.is_empty():
            return None
        return self._end[0]

    def __str__(self):
        if self.is_empty():
            return "[]"
        return f"[{self.range_min()}, {self.range_max()}]"
