# AI Function

Generate realtime AI Functions!

## What is an AI Function?

Let's say you want to write a function to get the current time in python. All you have to do is:

```python
from AIFunction import aiFunction

print(aiFunction("time", "Returns the current time."));
# --> 12:00:00
```

## How does it work?

AI function uses OpenAI's GPT model to generate the code for the function. It then runs the code and returns the output. If specified, it will also install the required packages for the code.

## Security

AI Functions are not very secure, as they run code without any user testing, and can be used to run malicious code.
