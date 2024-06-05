/*
Directions:
Write a loop that prints out the following song. Starting at 99, and ending at 1 bottle.

99 bottles of juice on the wall! 99 bottles of juice! Take one down, pass it around... 98 bottles of juice on the wall!
98 bottles of juice on the wall! 98 bottles of juice! Take one down, pass it around... 97 bottles of juice on the wall!
...
2 bottles of juice on the wall! 2 bottles of juice! Take one down, pass it around... 1 bottle of juice on the wall!
1 bottle of juice on the wall! 1 bottle of juice! Take one down, pass it around... 0 bottles of juice on the wall!
Attention to Detail is Important in Coding!
Pay attention to the pluralization of the word "bottle" when you go from 2 bottles to 1 bottle to 0 bottles.


*/
/*
 * Programming Quiz: 99 Bottles of Juice
 *
 * Use the following `while` loop to write out the song "99 bottles of juice".
 * Log the your lyrics to the console.
 *
 * Note
 *   - Each line of the lyrics needs to be logged to the same line.
 *   - The pluralization of the word "bottle" changes from "2 bottles" to "1 bottle" to "0 bottles".
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should have a variable `num` with a starting value of `99`
 * - Your code should include a `while` loop
 * - Your `while` loop should have a stop condition
 * - Your code should produce the expected output
 */


let num = 99;
let lyric = "";

while (num >= 0) {
  // check pluralization on the last line
  lyric =
  num === 1
  ? `${num} bottle of juice on the wall! ${num} bottle of juice! Take one down, pass it around... ${num - 1} bottles of juice on the wall!`
  : num === 0
  ? "No more bottles of juice on the wall!"
  : num === 2 ? `${num} bottles of juice on the wall! ${num} bottles of juice! Take one down, pass it around... ${num - 1} bottle of juice on the wall!` : `${num} bottles of juice on the wall! ${num} bottles of juice! Take one down, pass it around... ${num - 1} bottles of juice on the wall!`;
  console.log(lyric);
  // decrement num
  num -= 1;
}
