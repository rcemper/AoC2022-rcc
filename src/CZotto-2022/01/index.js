const fs = require('fs');
const dir = "c:\\GitHub\\set1\\1\\" ;
const rawData = fs.readFileSync(dir+'data.txt').toString();
const data = rawData.trim().split('\r\n\r\n');

const sum = (a, b) => a + b;
const totals = data.map(x => x.trim().split('\r\n').map(Number).reduce(sum, 0)).sort((a,b) => b - a);

// Part 1
console.log('part 1 = '+totals[0].toString());

// Part 2
console.log('part 2 = '+((totals.slice(0, 3).reduce(sum)).toString()));
