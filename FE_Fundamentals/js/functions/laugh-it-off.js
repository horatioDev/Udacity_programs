/*
Directions:
Declare a function called laugh() that returns "hahahahahahahahahaha!".

Print the value returned from the laugh() function to the console. It should print:
hahahahahahahahahaha!

*/

/*
 * Programming Quiz: Laugh it Off 1
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should have a `laugh()` function
 * - Your `laugh()` function should return the correct output
 * - Your code should print `\"hahahahahahahahahaha!\"` by calling the `laugh()`
 */

// your code goes here
function laugh() {
  return 'hahahahahahahahahaha!';
}

// test your code by logging out the returned value
console.log(laugh());

/*
Laugh it Off 2

Directions:
Write a function called laugh() that takes one parameter, num.
The function should return a string with num number of "ha"s.
The string should end with an exclamation point "!".
TIP: You might need a loop to solve this!
*/

/*
 * Programming Quiz: Laugh it Off 2
 *
 * QUIZ REQUIREMENTS
 * - Your code should have a `laugh()` function
 * - Your `laugh()` function should have one parameter named `num`
 * - Your `laugh()` function should return a string with `num` number of `"ha"`s.
 * - The string should end with an exclamation point.
 */

// your code goes here
function laugh2(num) {
  let result = '';
  for (let i = 0; i < num; i++) {
    result += 'ha';
  }
  return result;
}


// test code
console.log(laugh2(0)) 
console.log(laugh2(3)) 
console.log(laugh2(4)) 
console.log(laugh2(8)) 

/*
Write an anonymous function expression that:

stores a function in a variable called "laugh"
creates a string with the number of "ha"s that you pass in as an argument
adds an exclamation point at the end of the string
returns the string
laugh(3);
Returns: hahaha!
*/

/*
 * Programming Quiz: Laugh
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should have a variable `laugh`
 * - Your code should include an anonymous function expression stored in the variable `laugh`
 * - Your anonymous function expression should take one argument
 * - Your anonymous function expression should return the correct number of `hahaha`\'s
*/

// your code goes here
const laugh3 = function(num) {
  let sound = '';
  for(let i = 1; i <= num; i++) {
    sound += 'ha';
  }
  return sound + '!'
}


// testing your code
console.log(laugh3(1));
console.log(laugh3(5));
console.log(laugh3(10));

/*
  Write a named function expression that stores the function in a variable called cry and returns "boohoo!". Don't forget to call the function using the variable name, not the function name:

  cry();
  Returns: boohoo!
*/

/*
 * Programming Quiz: Cry
*/

/*
 * QUIZ REQUIREMENTS
 * - Your code should have a variable `cry`
 * - Your code should include a named function expression stored in the variable `cry`
 * - Your code should call the function expression using the variable name, not the function name
 * - Your function expression should return the expected output
*/

// your code goes here
const cry = function booHoo() {
  return "boohoo!"
}

// test your solution
console.log(cry());

/*
Directions:
Call the emotions() function so that it prints the output you see below, but instead of passing the laugh() function as an argument, pass an inline function expression instead.

emotions("happy", laugh(2)); // you can use your laugh function from the previous quizzes
Prints: "I am happy, haha!"
*/

/*
 * Programming Quiz: Inline Functions
 */
 
 /*
 * QUIZ REQUIREMENTS
 * - Your code should have an `emotions()` function
 * - Your code should call the `emotions()` function
 * - Your `emotions()` function call should have an inline function expression passed as the second parameter
 * - Your function expression should return the expected output
 */


// don't change this code
// emotions() function definition
function emotions(myString, myFunc) {
  console.log("I am " + myString + ", " + myFunc(5));
}

// your code goes here
// Call the emotions() function with two arguments
// Argument 1 - "happy" string
// Argument 2 - an inline function expression
emotions("happy", function (numLaughs) {
  let sound = '';
  for(let i = 1; i <= numLaughs; i++) {
    sound += 'ha';
  }
  return sound + '!'
});