class CRT:
    def __init__(self, height: int, length: int) -> None:
        self.height = height
        self.length = length
        self.display = [' ' for _ in range(self.height * self.length)]
        self.x = 1
        self.cycles = 0
        self.signal_strength = 0
    
    def __repr__(self):
        return f"CRT(height={self.height}, length={self.length})"

    def __str__(self):
        final = ''
        # Set start/end so that we end up with [0:self.length]
        start = -(self.length)
        end = 0
        for row in range(self.height):
            start += self.length
            end += self.length
            final += ''.join(self.display[start:end])
            final += '\n'
        return final
    
    def draw_pixel(self) -> None:
        pos = (self.cycles - 1) % self.length
        if self.x - 1 <= pos <= self.x + 1:
            self.display[self.cycles - 1] = '#'
        
        if self.cycles % self.length == 20:
            self.signal_strength += self.x * self.cycles
    
    def execute(self, instruction: str) -> None:
#        print(instruction)
#        print(instruction.split())
        ins = instruction.split()
#        match instruction.split():

#            case ['addx', x]:
#                self.addx(x)
        if ins[0] == 'addx':
            self.addx(ins[1])#            case ['noop']:
#                self.noop()
        if ins[0] == 'noop':
            self.noop()

    def addx(self, x: int) -> None:
        for _ in range(2):
            self.cycles += 1
            self.draw_pixel()
        self.x += int(x)
    
    def noop(self) -> None:
        self.cycles += 1
        self.draw_pixel()

class Program:
    def __init__(self, height: int, length: int, filename: str):
        self.height = height
        self.length = length
        self.filename = filename
        self.crt = CRT(self.height, self.length)
    
    def __repr__(self):
        return f"Program(height={self.height}, length={self.length}, filename={self.filename}"
    
    def run(self):
        with open(self.filename) as f:
            for instruction in f:
                print(instruction) 
                self.crt.execute(instruction)
        
        print(f"part 1 = {self.crt.signal_strength}")
        print("part 2 =")
        print(self.crt)
        

program = Program(6, 40, "C:/GitHub/set2/10/input.txt")
program.run()