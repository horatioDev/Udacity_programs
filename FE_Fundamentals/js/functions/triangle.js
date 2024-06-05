/*
For this quiz, you're going to create a function called buildTriangle() that will accept an input (the triangle at its widest width) and will return the string representation of a triangle. See the example output below.

* 
* * 
 ***  
 ***  * 
 ***  * * 
 ***   ***  
 ***   ***  * 
 ***   ***  * * 
 ***   ***   ***  
* * * * * * * * * *
*/

function makeLine(length) {
 let line = "";
  for (let j = 1; j <= length; j++) {
    line += "* "
  }
  return line + "\n";
}

// Build triangle
function buildTriangle(height) {
  let triangle = '';
  for (i=1; i<=height; i++){
    triangle += makeLine(i);
  }
  return triangle;
}
console.log(buildTriangle(5))