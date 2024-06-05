/*
James was creating an array with the colors of the rainbow, and he forgot some colors. The standard rainbow colors are usually listed in this order:

const rainbow = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"];
but James had this:

const rainbow = ["Red", "Orange", "Blackberry", "Blue"];
Using only the splice() method, insert the missing colors into the array, and remove the color "Blackberry" by following these steps:

Remove "Blackberry"
Add "Yellow" and "Green"
Add "Purple"
Running Your 
*/

/*
 * Programming Quiz: Colors of the Rainbow (6-4)
 *
 * Use only the splice() method to modify the rainbow variable:
 *  - remove "Blackberry"
 *  - add "Yellow" and "Green"
 *  - add "Purple"
 */

const rainbow = ['Red', 'Orange', 'Blackberry', 'Blue'];

// your code goes here
rainbow.splice(2,1,'Yellow','Green'); // Removes one item at index 2 (index is zero based), takes no items, adds 'Yellow' and 'Green'.
rainbow.splice(5,0,'Purple'); // Adds 'Purple'.
console.log(rainbow)