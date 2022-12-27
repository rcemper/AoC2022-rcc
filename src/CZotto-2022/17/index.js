const fs = require('fs');
const dir = "c:\\GitHub\\set1\\17\\" ;
const rawData = fs.readFileSync(dir+'data.txt').toString();


const ROCKS = [
  new Uint32Array([2, 3, 4, 5]),
  new Uint32Array([3, 9, 10, 11, 17]),
  new Uint32Array([2, 3, 4, 11, 18]),
  new Uint32Array([2, 9, 16, 23]),
  new Uint32Array([2, 3, 9, 10])
]

function rockFall (input, count = 2022) {
  let i = 0
  let j = 0
  const visited = new Map()
  const blocked = new Set([0, 1, 2, 3, 4, 5, 6])
  let highest = 0

  const outcomes = []

  while (count--) {
    const rock = ROCKS[i].map(v => v + (highest + 4) * 7)
    while (true) {
      if (input[j] === '<') {
        if (
          rock.every(v => v % 7 !== 0) &&
          rock.every(v => !blocked.has(v - 1))
        ) {
          rock.forEach((v, i, arr) => {
            arr[i] = v - 1
          })
        }
      } else {
        if (
          rock.every(v => v % 7 !== 6) &&
          rock.every(v => !blocked.has(v + 1))
        ) {
          rock.forEach((v, i, arr) => {
            arr[i] = v + 1
          })
        }
      }
      j++
      if (j >= input.length) j -= input.length
      if (rock.every(v => !blocked.has(v - 7))) {
        rock.forEach((v, i, arr) => {
          arr[i] = v - 7
        })
      } else {
        rock.forEach(v => blocked.add(v))
        const high = Math.floor(rock[rock.length - 1] / 7)
        const increase = Math.max(0, high - highest)
        outcomes.push(increase)
        highest += increase
        const state = j * ROCKS.length + i
        if (visited.has(state)) {
          const pastVisits = visited.get(state)
          pastVisits.push(outcomes.length - 1)
          const cycleLength = findPattern(pastVisits, outcomes)
          if (cycleLength) {
            const q = Math.floor(count / cycleLength)
            const r = count % cycleLength
            return (
              highest +
              q * outcomes.slice(-cycleLength).reduce((sum, v) => sum + v, 0) +
              outcomes
                .slice(-cycleLength, -cycleLength + r)
                .reduce((sum, v) => sum + v, 0)
            )
          }
        } else {
          visited.set(state, [outcomes.length - 1])
        }
        break
      }
    }
    i++
    if (i >= ROCKS.length) i -= ROCKS.length
  }
  return highest
}

function findPattern (pastVisits, outcomes) {
  const lastIndex = pastVisits[pastVisits.length - 1]
  for (let i = 0; i < pastVisits.length - 1; i++) {
    const testIndex = pastVisits[i]
    const cycleLength = lastIndex - testIndex
    if (testIndex + 1 < cycleLength) continue
    let j = 0
    while (j < cycleLength) {
      if (outcomes[lastIndex - j] !== outcomes[testIndex - j]) break
      j++
    }
    if (j === cycleLength) return cycleLength
  }
  return 0
}

console.log('part 1 = '+rockFall(rawData).toString())
console.log('part 2 = '+rockFall(rawData, 1000000000000).toString())