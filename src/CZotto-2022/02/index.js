const fs = require('fs');
const dir = "c:\\GitHub\\set1\\2\\" ;
const rawData = fs.readFileSync(dir+'data.txt').toString();
const data = rawData.trim().split('\r\n').map(str => str.split(' '));

const sum = (a, b) => a + b;

// Part 1
const scoreMap1 = {
  A: {X: 4, Y: 8, Z: 3},
  B: {X: 1, Y: 5, Z: 9},
  C: {X: 7, Y: 2, Z: 6}
}
console.log('part 1 = '+(data.map(([i, j]) => scoreMap1[i][j]).reduce(sum)).toString());

// Part 2
const scoreMap2 = {
  A: {X: 3, Y: 4, Z: 8},
  B: {X: 1, Y: 5, Z: 9},
  C: {X: 2, Y: 6, Z: 7}
}
console.log('part 2 = '+(data.map(([i, j]) => scoreMap2[i][j]).reduce(sum)).toString());
