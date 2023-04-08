const { Configuration, OpenAIApi } = require("openai");
require("dotenv").config();

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

const openai = new OpenAIApi(configuration);

async function createCompletion(messages, model = "gpt-3.5-turbo") {
  const completion = await openai.createChatCompletion({
    model,
    messages,
  });

  return completion.data.choices[0].message.content;
}

module.exports = {
  createCompletion,
};
