/*
Use the array's forEach() method(opens in a new tab) to loop over the following array and add 100 to each of the values if the value is divisible by 3.

const test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4, 19, 300, 3775, 299, 36, 209, 148, 169, 299, 6, 109, 20, 58, 139, 59, 3, 1, 139];
Log your solution to the console.

Suggestion
You can test your code with a smaller array first like this one:

const miniTest = [12, 29, 11, 3];
When your code runs, you should get this output:

[112, 929, 11, 103, 199, 1000, 7, 1, 124, 37, 4, 19, 400, 3775, 299, 136, 209, 148, 169, 299, 106, 109, 20, 58, 139, 59, 103, 1, 139]
*/

/*
 * Programming Quiz: Another Type of Loop (6-8)
 * QUIZ REQUIREMENTS
 * Use the existing `test` variable and write a `forEach` loop
 * that adds 100 to each number that is divisible by 3.
 *
 * Things to note:
 *  - Inside the loop, you must use an `if` statement to verify code is divisible by 3
 *  - Inside the loop, you can updade an element ONLY by using the arrayName[index]
 *  - Outside the loop, you can use `console.log` to verify the `test` variable 
 */

const test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4,
  19, 300, 3775, 299, 36, 209, 148, 169, 299,
  6, 109, 20, 58, 139, 59, 3, 1, 139
];

const miniTest = [12, 29, 11, 3];

// Write your code here
test.forEach(function(num, idx) {
if(num%3 === 0){
  test[idx] += 100;
} // check if num is divisible by 3
});

console.log(test)