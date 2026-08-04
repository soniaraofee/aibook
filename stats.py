from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, Iterable, List


@dataclass
class StatsCollector:
    """Collects simple numeric statistics for one or more named metrics."""

    counts: Counter = field(default_factory=Counter)
    totals: Dict[str, float] = field(default_factory=dict)
    mins: Dict[str, float] = field(default_factory=dict)
    maxs: Dict[str, float] = field(default_factory=dict)
    values: Dict[str, List[float]] = field(default_factory=dict)

    def record(self, name: str, value: float | int) -> None:
        numeric_value = float(value)
        self.counts[name] += 1
        self.totals[name] = self.totals.get(name, 0.0) + numeric_value
        self.values.setdefault(name, []).append(numeric_value)

        if name not in self.mins or numeric_value < self.mins[name]:
            self.mins[name] = numeric_value
        if name not in self.maxs or numeric_value > self.maxs[name]:
            self.maxs[name] = numeric_value

    def record_many(self, name: str, values: Iterable[float | int]) -> None:
        for value in values:
            self.record(name, value)

    def get_stats(self, name: str) -> Dict[str, float | int]:
        if name not in self.counts:
            raise KeyError(f"No stats recorded for {name!r}")

        count = self.counts[name]
        total = self.totals[name]
        return {
            "count": count,
            "total": total,
            "average": total / count,
            "min": self.mins[name],
            "max": self.maxs[name],
        }

    def snapshot(self) -> Dict[str, Dict[str, float | int]]:
        return {name: self.get_stats(name) for name in self.counts}

    def clear(self) -> None:
        self.counts.clear()
        self.totals.clear()
        self.mins.clear()
        self.maxs.clear()
        self.values.clear()


if __name__ == "__main__":
    collector = StatsCollector()
    collector.record_many("latency_ms", [120, 140, 180, 100])
    collector.record("errors", 1)

    print(collector.get_stats("latency_ms"))
    print(collector.snapshot())
