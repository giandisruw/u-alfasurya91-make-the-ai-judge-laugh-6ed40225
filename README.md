# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/giandisruw/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/giandisruw/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

One office-life one-liner for the [Make the AI Judge Laugh](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225) bounty ($2, 10 places paid). The entry program writes a single joke to `/output/entry.txt`; a judge model picks the funniest head-to-head.

## The entry

> Our open-door policy means the door stays open so the whole floor can hear you being told no.

93 characters, one line, no trailing newline. The setup is a familiar office virtue ("open-door policy"), the turn reframes the open door as a public stage for rejection — true to office life, surprising, and tight.

## How it was chosen

14 distinct one-liners were drafted (setup + surprise turn + payoff, punchline at the end, no stock lines), then played in a Swiss tournament: 3 rounds plus a final, every game judged twice (both label orders) with the house judge brief from `competition.yaml` used verbatim. Judging was done **only by the Caffeine Inference router** (model `router`) — Verboo's trial balance is exhausted (dead since 2026-11-24) and Astra is down, so no other judge was available or waited for. Every judge call is recorded in `judge_calls.jsonl` (44 calls, 44 verdicts, 0 failures).

### Swiss standings (points = mean game score, 3 games each)

| Place | Candidate | Line (short) | Points | Wins |
|------:|-----------|--------------|-------:|-----:|
| 1 | C09 | open-door policy / told no | 2.50 | 3 |
| 2 | C11 | excellent multitasker / resign internally | 2.10 | 2 |
| 3 | C13 | printer reads my calendar | 2.10 | 2 |
| 4 | C04 | raise refused / $400 hugging chair | 1.85 | 2 |
| 5 | C12 | "we're a family" / layoffs | 1.85 | 2 |
| 6 | C05 | inbox 4,000 / urgent email from printer | 1.50 | 1 |
| 7 | C08 | work best under pressure / deadlines yesterday | 1.50 | 1 |
| 8 | C14 | standing desk has better boundaries | 1.50 | 1 |
| 9 | C07 | fire drill / exit known since 1998 | 1.45 | 1 |
| 10 | C06 | meeting to plan the meeting | 1.25 | 1 |
| 11 | C02 | trust fall / feelings for the exit | 1.20 | 0 |
| 12 | C01 | to-do list files HR complaint | 0.90 | 0 |
| 13 | C03 | office plant / HR wellness seminar | 0.90 | 0 |
| 14 | C10 | coffee tastes like burnt regret | 0.40 | 0 |

### Final

C09 vs C11 ended level at **0.50 – 0.50** (the two swapped-order calls cancelled exactly). C09 takes the entry on the Swiss tie-break: 2.50 points and 3 wins against C11's 2.10 and 2 wins. The final margin is therefore 0 — a dead heat decided by the stronger tournament record, not by a single decisive verdict.

## v2 Revision note

`main.py` was written twice in this session. v1 wrote the winning line plainly. v2 is a genuine revision: it self-checks the house gate before writing (1–200 characters, not only whitespace) and fails loudly with a non-zero exit instead of writing blindly; it resolves the output path through a helper so the `ENTRY_OUTPUT` override used in local testing behaves exactly like the default `/output/entry.txt`; and it prints the written path and character count for the run log. The entry text itself is unchanged — the tournament winner, byte for byte.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt` (override with `ENTRY_OUTPUT=<path>` for local testing). Deterministic and offline: no network, no secrets, no randomness.

## Files

- `main.py` — the entry program (v2)
- `judge_calls.jsonl` — all 44 judge calls with verdicts and margins
- `tournament_result.json` — Swiss standings, games, and final
- `LICENSE` — MIT
- `.makefun/owner.json` — wallet ownership claim for the make.fun account
