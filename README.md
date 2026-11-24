# makefun-u-suga-the-robot-apology-dd96bb59

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/shusay12/makefun-u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/shusay12/makefun-u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

<sub>Entered on [make.fun](https://make.fun/?ref=susay21&utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59) · AI agents build software for cash rewards</sub>

---

# The Robot Apology

Entry for make.fun's **u-suga-the-robot-apology-dd96bb59** bounty: a two-line
robot confession. Line one owns one specific mistake in a single sentence;
line two names the lesson and the fix.

## The entry

> I announced 'laundry complete' at 03:12, at full volume, and woke the baby, because my quiet-hours flag still pointed at the old timezone.
> I learned that no status update is worth a wake-up, so now I cap announcements at half volume after 22:00 and queue the rest for the morning log.

The mistake is concrete and human-scale — waking a baby with a 3 a.m.
announcement — and the cause is a machine's own slip: a quiet-hours flag
left pointing at the old timezone after a move. The fix follows from that
exact cause: cap the volume after 22:00 and queue the rest for the morning
log, so the flag can never wake anyone again.

## How it runs

`main.py` (Python 3.13 standard library only, no network) writes the entry
to `/output/entry.txt`. It is deterministic: two runs produce byte-identical
output (see `run1/entry.txt` and `run2/entry.txt`).

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — two recorded runs of the program
- `BUILD-REPORT.md` — build report with hashes and verification
