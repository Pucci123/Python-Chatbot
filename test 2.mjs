import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: [remove]
});

const completion = await openai.chat.completions.create({
    model: "gpt-4",
    messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "Write a haiku about recursion in programming." }
    ]
});

console.log(completion.choices[0].message.content);
