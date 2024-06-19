#!/usr/bin/node
const args = process.argv.slice(2);
const firstInt = parseInt(args[0], 10);
const secondInt = parseInt(args[1], 10);
function add (a, b) {
  return a + b;
}
if (isNaN(firstInt) || isNaN(secondInt)) {
  console.log('Both arguments must be numbers');
} else {
  console.log(add(firstInt, secondInt));
}
