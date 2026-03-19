#!/usr/bin/node

if (process.argv.length <= 3) {
    console.log(0);
  } else {
    let biggest = parseInt(process.argv[2], 10);
    let secondBiggest = parseInt(process.argv[3], 10);
  
    if (secondBiggest > biggest) {
      const temp = biggest;
  
      biggest = secondBiggest;
      secondBiggest = temp;
    }
  
    for (let i = 4; i < process.argv.length; i++) {
      const current = parseInt(process.argv[i], 10);
  
      if (current > biggest) {
        secondBiggest = biggest;
        biggest = current;
      } else if (current > secondBiggest) {
        secondBiggest = current;
      }
    }
  
    console.log(secondBiggest);
  }