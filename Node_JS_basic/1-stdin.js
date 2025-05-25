process.stdout.write("Welcome to Holberton School, what is your name?\n");

// Listen for user input on stdin
process.stdin.on("data", (data) => {
  const input = data.toString().trim();
  process.stdout.write(`Your name is: ${input}\r`);
  
  // Gracefully close the input stream after handling input
  process.stdin.end();
});

// Event handler for process exit
process.on("exit", () => {
  console.log("This important software is now closing\n");
});

process.stdin.on("end", () => {
  process.exit();
});
