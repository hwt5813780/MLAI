const axios = require('axios');
async function callOpenAI() {
  
    const response = await axios.post(
      'https://api.openai.com/v1/chat/completions',
      {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello!"}]
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + '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'
        }
      }
    );
  
    console.log(completion.data.choices[0].message);
  }
  callOpenAI();
  