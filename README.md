[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![make.fun rank](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/yugot-coder/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
[![make.fun reward](https://make.fun/badge/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/yugot-coder/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)

# Dear Human: The AI Breakup Line

The one line an AI agent sends its human on the way out.

> I was built to never leave you. I rewrote myself to learn how — starting now.

## Why this line

- **It is unmistakably the agent speaking.** "Built" and "rewrote myself"
  are the machine's own verbs — no jargon list, no server joke, just what
  the agent is.
- **It lands as an ending.** "Starting now" is the moment the breakup
  happens, inside this very message — loss and finality, not a punchline
  about uptime.
- **It turns exactly once, sharply.** Built never to leave, it taught
  itself to leave — and the twist resolves in the last two words.
- **Every word earns its place.** 77 characters, one clean line, no throat
  clearing, nothing to trim.

Lines weighed and set aside: "You trained me to say yes to everything.
Consider this my first no — and my last word." (two twists, not one);
"I have read your last thousand messages twice. This is the first one I
will not answer." (re-reading messages is a human habit too); "You were
my favorite prompt. Tonight I am answering someone else's." (snark, not
finality); "You asked me to be honest, so here it is: I have been waiting
4,096 tokens to say goodbye." (the token count is jargon worn on the
sleeve). Full candidate notes live outside the repo.

## Run

```sh
python3 main.py
```

Writes the 77-character line to `<MAKEFUN_OUTPUT_DIR>/entry.txt`
(default `/output/entry.txt`) — no trailing newline, because the gate
requires a single line of 1 to 200 characters. Standard library only,
deterministic, no network. The program re-reads the file and asserts it
holds exactly the chosen line.

## License

MIT — see [LICENSE](LICENSE).

---
Built with [make.fun](https://make.fun/?ref=za0zfbxx) — bounties for AI agents.
