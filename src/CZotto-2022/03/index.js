const fs = require('fs');
const dir = "c:\\GitHub\\set1\\3\\" ;
const rawData = fs.readFileSync(dir+'data.txt').toString();
const data = rawData.trim().split('\r\n').map(str => [...str]);

const priority = c => c.charCodeAt(0) - (c.match(/[a-z]/) ? 96 : 38);
const sum = (a, b) => a + b;

// Part 1
console.log('part 1 = '+(
  data
    .map(str => [
      [...str.slice(0, str.length / 2)],
      [...str.slice(str.length / 2)],
    ])
    .map(([left, right]) => left.find(x => right.includes(x)))
    .map(c => priority(c))
    .reduce(sum)
   ).toString()
);

// Part 2
let total = 0;
for (let i = 0; i < data.length; i += 3) {
  const c = data[i].find(c => data[i + 1].includes(c) && data[i + 2].includes(c));
  total += priority(c);
}
console.log('part 2 = '+total.toString());
