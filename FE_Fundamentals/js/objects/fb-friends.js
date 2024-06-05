/*
Create an object called facebookProfile. The object should have 3 properties:

your name
the number of friends you have, and
an array of messages you've posted (as strings) -- include at least two messages.
The object should also have 4 methods:

postMessage(message) - adds a new message string to the array
deleteMessage(index) - removes the message corresponding to the index provided
addFriend() - increases the friend count by 1
removeFriend() - decreases the friend count by 1

HINT! Here are some array methods you might want to use:

addition at the end is done using the push() method - MDN: Array.prototype.push()(opens in a new tab)
addition or removal at a specific index is done using the splice() method - Array.prototype.splice()(opens in a new tab)
deletion from the end is done using the pop() method - MDN: Array.prototype.pop()

Name:  Udacian
Messages:  [ 'Message 1', 'Message 2', 'Message 3', 'Message 4' ]
Messages:  [ 'Message 1', 'Message 2', 'Message 3', 'Message 4', 'New message!' ]
Messages:  [ 'Message 1', 'Message 2', 'Message 4', 'New message!' ]
Friends:  25
Friends:  26
Friends:  25
*/
/*
 * Programming Quiz: Facebook Friends
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should have an object `facebookProfile`
 * - The `facebookProfile` object should have the `name` (string), `friends` (number), and `messages` (array of strings) property
 * - Your `facebookProfile` object should have the `postMessage()`, `deleteMessage()`, `addFriend()` and `removeFriend()` method
 * - Carefully implement the desired functionality of each method, as decribed above
 */


// your code goes here
const facebookProfile = {
  "name": "Udacian",
  "friends": 25,
  "messages": ['Message 1', 'Message 2', 'Message 3', 'Message 4'],
  // post a new message
  postMessage: function(message) {
    facebookProfile.messages.push(message);
  },
  // delete a message
  deleteMessage: function(message) {
    return facebookProfile.messages.splice(2,1);
  },
  // add friend 
  addFriend: function() {
    facebookProfile.friends++;
  },
  // delete friend
  removeFriend: function() {
    return facebookProfile.friends > 0 ? facebookProfile.friends-- : console.log("You don't have any friends!");
  }
}


// text code
console.log("Name: ", facebookProfile.name);
console.log("Messages: ", facebookProfile.messages);
facebookProfile.postMessage("New message!");
console.log("Messages: ",  facebookProfile.messages);
facebookProfile.deleteMessage(2);
console.log("Messages: ",  facebookProfile.messages);
console.log("Friends: ", facebookProfile.friends);
facebookProfile.addFriend();
console.log("Friends: ", facebookProfile.friends);
facebookProfile.removeFriend();
console.log("Friends: ", facebookProfile.friends);