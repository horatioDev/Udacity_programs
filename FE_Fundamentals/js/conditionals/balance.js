/*
Expected Output
Customer	balance	checkBalance	isActive	Expected Output
Customer1	-325	true	true	Your balance is negative. Please contact bank.
Customer2	35	true	true	Your balance is $35.00.
Customer3	35	false	true	Thank you. Have a nice day!
Customer4	35	true	false	Your account is no longer active.
Customer5	0	true	true	Your account is empty.
Customer6	-325	false	true	Thank you. Have a nice day!
Customer7	-325	true	false	Your account is no longer active.
Customer8	35	false	false	Thank you. Have a nice day!
Customer9	0	false	false	Thank you. Have a nice day!
Customer10	0	true	false	Your account is no longer active.
*/

/*
 * Programming Quiz - Checking Your Balance
 */

/*
 * QUIZ REQUIREMENTS
 * 1. Your code should have the variables `balance`, `checkBalance`, `isActive`
 * 2. Your code should include an `if...else` conditional statement
 * 3. Your code should produce the expected output
 * 4. Your code should not be empty
 * 5. BE CAREFUL ABOUT THE PUNCTUATION AND THE EXACT WORDS TO BE PRINTED. 
 */
 
// change the values of `balance`, `checkBalance`, and `isActive` to test your code
const balance = 35.00;
const checkBalance = true;
const isActive = false;

// your code goes here
// Start only if checkBalance === true
if (checkBalance) {
  // Cases when account is active. Now, the balance could be <, =, or > zero
  if (isActive && balance > 0) {
    console.log("Your balance is $" + balance.toFixed(2) + ".");
  }
  else if (isActive && balance === 0) {
    console.log("Your account is empty.");
  }
  else if (isActive  && balance < 0) {
    console.log("Your balance is negative. Please contact bank.");
  }
  // Case when account is NOT active
  else if (!isActive) {
    console.log("Your account is no longer active.");
  }
}
else {
  console.log("Thank you. Have a nice day!");
}

// function
function checkCustomerStatus(customer, balance, checkBalance, isActive) {
  if (!isActive) {
      return "Your account is no longer active.";
  } else if (!checkBalance) {
      return "Thank you. Have a nice day!";
  } else if (balance < 0) {
      return "Your balance is negative. Please contact bank.";
  } else if (balance === 0) {
      return "Your account is empty.";
  } else {
      return "Your balance is $" + balance.toFixed(2) + ".";
  }
}

// Test cases
const customers = [
  ["Customer1", -325, true, true],
  ["Customer2", 35, true, true],
  ["Customer3", 35, false, true],
  ["Customer4", 35, true, false],
  ["Customer5", 0, true, true],
  ["Customer6", -325, false, true],
  ["Customer7", -325, true, false],
  ["Customer8", 35, false, false],
  ["Customer9", 0, false, false],
  ["Customer10", 0, true, false]
];

customers.forEach(([customer, balance, checkBalance, isActive]) => {
  console.log(`${customer}: ${checkCustomerStatus(customer, balance, checkBalance, isActive)}`);
});