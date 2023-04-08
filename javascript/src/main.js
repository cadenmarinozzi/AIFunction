const { createCompletion } = require("./modules/web/OpenAI");

async function aiFunction(functionName, description) {
  const code = await createCompletion([
    {
      content:
        "You are an AI code generator. Generate ONLY the javascript code for the given function description, nothing else. The code should include just the function body, without the function statement, and should return just the output, without any other text. The code should take no user input, and should only have a single return statement.",
      role: "system",
    },
    {
      content:
        "Here is an example:\nFunction: time\nDescription: Returns the current time.\n\nlet time = new Date().toLocaleTimeString();\nconsole.log(time);",
      role: "system",
    },
    {
      content: `Function: ${functionName}\nDescription: ${description}`,
      role: "user",
    },
  ]);

  const result = eval("(function() {" + code + "}())");

  return result;
}

module.exports = aiFunction;
