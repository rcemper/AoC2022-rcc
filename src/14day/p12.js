const fs = require("fs")
const { Interface } = require("readline")
const { inflate } = require("zlib")
const performance = require("perf_hooks").performance
const eol = require("os").EOL

let startTime = performance.now()
let part1 = (part2 = 0)
let maxX = -Infinity
let maxY = -Infinity

let input = fs
    .readFileSync("data.txt", "utf8")
    .split(eol)
    .map((r) =>
        r.split(" -> ").map((i) => {
            coord = i.split(",").map(Number)
            maxX = Math.max(coord[0] + 1, maxX)
            maxY = Math.max(coord[1] + 1, maxY)
 		    return coord
        })
    )

class Cave {
    map
    overFlow = false
    constructor(width, height) {
        this.map = Array(height)
            .fill()
            .map(() => Array(width).fill(" "))
    }
    setTile(x, y, value) {
        this.map[y][x] = value
    }
    getTile(x, y) {
        if (this.map[y] === undefined) {
            this.overFlow = true
            return ""
        }
        let state = this.map[y][x]
        if (state === undefined) this.overFlow = true
        return state
    }
    addSand(x, y) {
        this.setTile(x, y, "X")
        while (true) {
            if (this.getTile(x, y + 1) == " ") y += 1
            else if (this.getTile(x - 1, y + 1) == " ") (x -= 1), (y += 1)
            else if (this.getTile(x + 1, y + 1) == " ") (x += 1), (y += 1)
            else break
        }
        !this.overFlow && this.setTile(x, y, "0")
        if ((x == 500) & (y == 0)) this.overFlow = true
        return this.overFlow
    }
    addLine(startX, startY, endX, endY) {
        let [sX, eX] = [startX, endX].sort((a, b) => a - b)
        let [sY, eY] = [startY, endY].sort((a, b) => a - b)
        if (sX == eX)
            for (let y = sY; y <= eY; y++) {
                this.setTile(sX, y, "#")
            }
        if (sY == eY)
            for (let x = sX; x <= eX; x++) {
                this.setTile(x, sY, "#")
            }
    }
}

let cave = new Cave(maxX, maxY)
input.forEach((row) => {
    for (let i = 0; i < row.length - 1; i++) {
        cave.addLine(...row[i], ...row[i + 1])
    }
})
while (!cave.addSand(500, 0)) part1++

let cave2 = new Cave(maxX * 2, maxY + 2)
input.forEach((row) => {
    for (let i = 0; i < row.length - 1; i++) {
        cave2.addLine(...row[i], ...row[i + 1])
    }
})
cave2.addLine(0, maxY + 1, maxX * 2, maxY + 1)
while (!cave2.addSand(500, 0)) part2++
part2++

let time = performance.now() - startTime
console.log(`Part 1: ${part1}\nPart 2: ${part2}\nTimer: ${time} ms`)