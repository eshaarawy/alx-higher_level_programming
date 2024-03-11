#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length > 1) {
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
