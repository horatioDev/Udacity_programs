/*
"Fizzbuzz" is a famous interview question used in programming interviews. It goes something like this:

Loop through the numbers 1 to 100
If the number is divisible by 3, print "Fizz"
If the number is divisible by 5, print "Buzz"
If the number is divisible by both 3 and 5, print "FizzBuzz"
If the number is not divisible by 3 or 5, print the number

let x = 1;

while (x  <= 20) {
    // check divisibility - print Fizz, Buzz, or FizzBuzz
    (x % 3 === 0  && x % 5 === 0) ? console.log('FizzBuzz') : x % 3 === 0 ? console.log('Fizz') : x % 5 === 0 ? console.log('Buzz') : console.log(x)
    // increment x
    x += 1;
}

Write a while loop that:

Loop through the numbers 1 to 20
If the number is divisible by 3, print "Julia"
If the number is divisible by 5, print "James"
If the number is divisible by 3 and 5, print "JuliaJames"
If the number is not divisible by 3 or 5, print the number
*/

/*
 * Programming Quiz: JuliaJames
 */
/*
 * QUIZ REQUIREMENTS
 * - Your code should have a variable `x` with a starting value of `1`
 * - Your code should include a `while` loop
 * - Your `while` loop should have a stop condition
 * - Your code should use a conditional statement
 * - Your code should increment `x` by `1` each time the loop executes
 * - Your code should produce the expected output
 */
 
let x = 1;

while (x  <= 20) {
    // check divisibility - print Julia, James, or JuliaJames
    (x % 3 === 0  && x % 5 === 0) ? console.log('JuliaJames') : x % 3 === 0 ? console.log('Julia') : x % 5 === 0 ? console.log('James') : console.log(x)
    // increment x
    x += 1;
}