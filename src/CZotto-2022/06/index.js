const fs = require('fs');
const dir = "c:\\GitHub\\set1\\6\\" ;
const rawData = fs.readFileSync(dir+'data.txt').toString();
const data = rawData.trim();

const detect = (str, n) => {
  for (let i = 0; i < str.length - n + 1; i++) {
    const s = new Set([...str.slice(i, i + n)])
    if (s.size === n)  {
      return i + n;
    }
  }
}

// Part 1
console.log('part 1 = '+ detect(data, 4));

// Part 2
console.log('part 2 = '+ detect(data, 14));
