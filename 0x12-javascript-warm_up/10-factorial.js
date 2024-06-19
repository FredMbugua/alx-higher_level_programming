#!/usr/bin/node
const args = process.argv.slice(2);
const n = parseInt(args[0], 10);
function factorial (num) {
  if (isNaN(num) || num < 0) {
    return 1;
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(n));
