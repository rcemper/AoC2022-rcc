const fs = require('fs');
const dir = "c:\\GitHub\\set1\\4\\" ;
const rawData = fs.readFileSync(dir+'data.txt').toString();
const data = rawData.trim().split('\r\n').map(row => (
  row.split(',').map(range => range.split('-').map(Number))
));

const contains = (r1, r2) => r1[0] <= r2[0] && r1[1] >= r2[1];
const overlap = (r1, r2) => r1[0] >= r2[0] && r1[0] <= r2[1] || r2[0] >= r1[0] && r2[0] <= r1[1];

// Part 1
console.log('part 1 = '+(
  data.filter(([r1, r2]) => contains(r1, r2) || contains(r2, r1)).length
  ).toString()
);

// Part 2
console.log('part 2 = '+(
  data.filter(([r1, r2]) => overlap(r1, r2)).length
  ).toString()
);
