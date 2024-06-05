/*
Expected Output
Flavor	Topping	Vessel	Response
chocolate	bananas	wafer cone	"Please check our menu and try again."
chocolate	peanuts	wafer cone	"Great choice! Your ice cream is at the next window."
chocolate	sprinkles	sugar cone	"Great choice! Your ice cream is at the next window."
chocolate	sprinkles	bowl	"Please check our menu and try again."
strawberry	sprinkles	wafer cone	"Please check our menu and try again."
strawberry	bananas	sugar cone	"Please check our menu and try again."
strawberry	peanuts	bowl	"Please check our menu and try again."
vanilla	sprinkles	wafer cone	"Great choice! Your ice cream is at the next window."
vanilla	peanuts	sugar cone	"Great choice! Your ice cream is at the next window."
vanilla	sprinkles	bowl	"Please check our menu and try again."
*/

/*
 * Programming Quiz: Ice Cream
 *
 * Write a single if statement that logs out the message:
 * 
 * "Great choice! Your ice cream is at the next window."
 * 
 * ...only if:
 *   - flavor is "vanilla" or "chocolate"
 *   - vessel is "sugar cone" or "wafer cone"
 *   - topping is "sprinkles" or "peanuts"
 *
 * Otherwise log out:
 *
 * "Please check our menu and try again."
 */

/*
 * QUIZ REQUIREMENTS
 * 1. Your code should have the variables `flavor`, `vessel`, and `topping`
 * 2. Your code should have an `if` statement
 * 3. Your code should use logical expressions
 * 
 */
 
// change the values of `flavor`, `topping`, and `vessel` to test your code
const flavor = "vanilla";
const topping = "peanuts";
const vessel = "sugar cone";

const availableFlavor = flavor === 'vanilla' || flavor === 'chocolate';
const availableTopping = topping === 'sprinkles' || topping === 'peanuts';
const availableVessel = vessel === 'sugar cone' || vessel === 'wafer cone';

// your code goes here
if (availableFlavor && availableTopping && availableVessel) {
  console.log('Great choice! Your ice cream is at the next window.')
} else {
  console.log('Please check our menu and try again.')
}