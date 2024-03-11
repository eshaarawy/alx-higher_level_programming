#!/usr/bin/node
function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  }
  factorial(a - 1);
}

console.log(factorial(parseInt(process.argv[2])));
