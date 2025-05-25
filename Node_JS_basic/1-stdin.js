process.stdout.write("Welcome to Holberton School, what is your name?\n");

// Listen for user input
process.stdin.on("data", (data) => {
  const input = data.toString().trim(); // Get and trim the input
  process.stdout.write(`Your name is: ${input}\r`); // Display the name
  process.stdin.end(); // Close the input stream
});

// Event handler for process exit
process.on("exit", () => {
  console.log("This important software is now closing");
});