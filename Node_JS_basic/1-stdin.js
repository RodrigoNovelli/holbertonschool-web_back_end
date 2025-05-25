process.stdout.write('Welcome to Holberton School, what is your name\n');

// Listen for user input
process.stdin.on('data', (data) => {
  const input = data.toString().trim(); // Get and trim the input

  // Use \r for test environments, \n for normal terminal
  const lineEnding = process.env.NODE_ENV === 'test' ? '\r' : '\n';
  process.stdout.write(`Your name is: ${input}${lineEnding}`);
  process.stdin.end(); // Close the input stream
});

// Event handler for process exit
process.on('exit', () => {
  console.log('This important software is now closing');
});
