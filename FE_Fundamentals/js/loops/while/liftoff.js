/*
NASA's countdown to launch includes checkpoints(opens in a new tab) where NASA engineers complete certain technical tasks. During the final minute, NASA has 6 tasks to complete:

Orbiter transfers from ground to internal power (T-50 seconds)
Ground launch sequencer is go for auto sequence start (T-31 seconds)
Activate launch pad sound suppression system (T-16 seconds)
Activate main engine hydrogen burnoff system (T-10 seconds)
Main engine start (T-6 seconds)
Solid rocket booster ignition and liftoff! (T-0 seconds)

Directions:
Write a while loop that counts down from 60 seconds and:

If there's a task being completed, it prints out the task
If there is no task being completed, it prints out the time as T-x seconds
Use the task and time descriptions described above.
*/

/*
 * Programming Quiz: Countdown, Liftoff!
 * 
 * Using a while loop, print out the countdown output above.
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should include a `while` loop
 * - Your `while` loop should have a stop condition
 * - Your code should produce the expected output
 */

// your code goes here
let seconds = 60; // Start counting down from 60 seconds

while (seconds >= 0) {
  switch (seconds) {
    case 50:
      console.log(`Orbiter transfers from ground to internal power`)
      break;
    case 31:
      console.log(`Ground launch sequencer is go for auto sequence start `)
      break;
    case 16:
      console.log(`Activate launch pad sound suppression system`)
      break;
    case 10:
      console.log(`Activate main engine hydrogen burnoff system `)
      break;
    case 6:
      console.log(`Main engine start`)
      break;
    case 0:
      console.log(`Solid rocket booster ignition and liftoff! `)
      break;
    default:
      console.log(`T-${seconds} seconds`);
      break;
  }
  
  seconds -= 1;
}
