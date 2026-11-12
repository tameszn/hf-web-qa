# GAIA Question-Answering Agent

An AI agent that answers hard, real-world questions by searching the web, reading the results, and replying with one short, exact answer. It was built as the final assignment of the Hugging Face Agents Course (Unit 4) and scored **55%** on its first submission.

**Links:** [Live Space](https://huggingface.co/spaces/pszn/huggingface_final_project) · [GitHub repository](https://github.com/tameszn/huggingface-final-project)


## Overview

The questions come from GAIA, a benchmark that tests whether an AI assistant can handle everyday tasks that need several steps, such as finding a fact on Wikipedia, comparing two sources, or working through a small puzzle. The course supplies 20 of the easiest GAIA questions (Level 1) through a public scoring service.




| Item | Detail |
|------|--------|
| Questions | 20, taken from the GAIA Level 1 validation set |
| Marking | Exact match against the correct answer |





## How It Works

```
Question → Agent → (needs a fact?) → Web search → Read results → Final answer
                         ↓ no
                   Answer directly
```

20 questions are fetched from the course scoring services , For each question, the agent reasons about what it needs. If it needs a fact, it calls the search tool, reads what comes back, and may search again.
Once it has enough information, it writes a short answer. The answers are cleaned and submitted together and the service returns a score.

### Answer rules given to the model

The agent follows a fixed set of instructions designed for exact-match marking:

- Reply with the final answer only, with no explanation and no "FINAL ANSWER" prefix.
- Write numbers as digits, without commas or units, unless the question asks for them.
- Do not end the answer with a full stop.
- If the answer truly cannot be found, reply `unknown`.


## Built With

| Tool | Role |
|------|------|
| Python | Main language |
| Google Gemini | The language model that reasons and writes the answers |
| Tavily | Web search, used as the agent's only tool |
| LangChain | Connects the model to the search tool and runs the reasoning loop |
| Gradio | The web page with the login and submit buttons |
| Hugging Face Spaces | Hosting |








## What I Learned

- **Format decides the score.** A correct answer in the wrong format earns nothing under exact match.
- **Read the trace.** Printing every step the agent takes (each search and each result) is the fastest way to see why an answer went wrong.
- **Test in small pieces.** Getting the model, then the search tool, then the full app working one at a time made errors easy to find.



## Limitations

- The agent cannot open attached files (Excel, Python), audio, images, or videos, so most questions that need them are answered wrongly.
- Web search is its only tool, and it has no calculator.
- Results can differ between runs, because search results and model replies change over time.


## Next Steps

- Add a reader for Excel and Python files
- Add audio transcription for the recording-based questions
- Add a calculator tool for arithmetic questions
- Review each wrong answer in the results table and adjust the instructions or tools to match









---
title: Template Final Assignment
emoji: 🕵🏻‍♂️
colorFrom: indigo
colorTo: indigo
sdk: gradio
sdk_version: 5.25.2
app_file: app.py
pinned: false
hf_oauth: true
# optional, default duration is 8 hours/480 minutes. Max duration is 30 days/43200 minutes.
hf_oauth_expiration_minutes: 480
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
