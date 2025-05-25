process.stdout.write('Welcome to Holberton School, what is your name?\n');
// Listen for user input
process.stdin.on('data', (data) => {
  const input = data.toString().trim(); // Get and trim the input
  // Write the output as expected by the test case
  process.stdout.write(`Your name is: ${input}\r`);
  // Gracefully close the input stream
  process.stdin.end();
});
// Event handler for process exit
process.on('exit', () => {
  console.log('This important software is now closing\n');
});
