from __future__ import annotations
 
from collections import deque
from dataclasses import dataclass
from functools import cached_property
from typing import List, Union, Dict, Optional, Deque
import pathlib
 
 
def read_data():
     with open(f"C:/GitHub/set2/7/input.txt") as raw_data:
         return raw_data.readlines()
 
 
@dataclass
class File:
    size: int
 
    def to_str(self, _):
        return f"{self.size}"
 
 
class Dir:
    def __init__(self, parent: Optional[Dir]):
        self.subtree: Dict[str, Union[Dir, File]] = {}
        self.parent = parent if parent else self
 
    def __setitem__(self, name: str, item: Union[Dir, File]):
        self.subtree[name] = item
 
    def __getitem__(self, name: str) -> Union[Dir, File]:
        return self.subtree[name]
 
    def __contains__(self, item) -> bool:
        return item in self.subtree
 
    def to_str(self, prefix="\t"):
        s = f"{self.size}\n"
        next_prefix = prefix+"\t"
        for name, item in self.subtree.items():
            s += f"{prefix}{name}: {item.to_str(next_prefix)}"
            if isinstance(item, File):
                s += "\n"
        return s
 
    @cached_property
    def size(self):
        return sum((item.size for name, item in self.subtree.items()))
 
 
def parse_cli(output: List[str]) -> Dir:
    filesystem = Dir(None)
    current_dir = filesystem
    idx = -1
 
    def nextline() -> Optional[str]:
        nonlocal idx
        idx += 1
        if idx >= len(output):
            return None
        ln = output[idx]
        return ln
 
    while line := nextline():
        _, cmd, *args = line.strip().split()
        if cmd == "cd":
            target = args[0]
            if target == "/":
                current_dir = filesystem
            elif target == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir[target]
        elif cmd == "ls":
            while line := nextline():
                result: List[str] = line.strip().split()
                if result[0] == "$":
                    break
                elif result[0].isdigit() and result[1] not in current_dir:
                    current_dir[result[1]] = File(int(result[0]))
                elif result[0] == "dir" and result[1] not in current_dir:
                    current_dir[result[1]] = Dir(current_dir)
                else:
                    print("fuckup")
            idx -= 1
 
    return filesystem
 
 
def part1(data: List[str]) -> int:
    size_sum = 0
    filesystem = parse_cli(data)
    fs_queue = deque([filesystem])
    while fs_queue:
        item = fs_queue.popleft()
        if isinstance(item, Dir):
            fs_queue.extend(item.subtree.values())
            if item.size <= 100000:
                size_sum += item.size
 
    return size_sum
 
 
def part2(data: List[str]) -> int:
    filesystem = parse_cli(data)
    space_needed = 30000000 - (70000000 - filesystem.size)
 
    fs_queue = deque([filesystem])
    candidates = []
    while fs_queue:
        item = fs_queue.popleft()
        if isinstance(item, Dir):
            fs_queue.extend(item.subtree.values())
            if item.size >= space_needed:
                candidates.append(item)
 
    return sorted(candidates, key=lambda item: item.size)[0].size
 
 
def main():
    data = read_data()
    print(f"part 1 = {part1(data)}")
    print(f"part 2 = {part2(data)}")
 
 
if __name__ == "__main__":
    main()
