#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry (u-golden-heron-44-fortune-in-a-pot-ded981e9).

Writes one kind, funny fortune for a houseplant (<=120 chars) to /output/entry.txt.

Pass 2 (this write): replaced the pass-1 line with a fresh challenger, tested
head-to-head and kept on the judge's ordered criteria. Challenger: "You will
lean toward the sun so far this week the gardener must turn your pot, and you
will pretend it was your idea." (117 chars). Head-to-head: (1) both are
fortunes for a houseplant about its own future — tie; (2) FUNNY to a plant
lover: the challenger's turn is sharper — the plant taking credit for the
gardener turning its pot is a distinct, surprising laugh, where "growing
sideways" only describes the lean — challenger wins; (3) kind: both warm, no
doom — tie; (4) fortune cadence: pass 1 slightly cleaner, but criterion 2
outranks 4; (5) tightness: pass 1 slightly tighter (97 vs 117 chars), but
criterion 2 outranks 5. Verdict: challenger wins on the highest differing
criterion. It is also specific to THIS plant in THIS window (the gardener
turning the pot is a real keeper ritual), and the vanity joke is warm, not
mocking.

Pass 1 (superseded): the "moved closer to the light" line.
Weighing vs the judge's ordered criteria (fortune for a houseplant -> funny to
a plant lover -> kind -> fortune cadence -> tight and specific to this plant
in this window):
- "Grow taller than the window expects": warm but more sweet than funny.
- "A kind hand will water you soon": kind, but the payoff is vague.
- "Roots stronger than you know": warm, generic; fits any plant in any room.
- "Outgrow this pot by summer... that was always the plan": sweet, gentle
  joke, but a familiar plant-fortune shape.
- CHOSEN: "Someone will move you closer to the light this week, and you will
  thank them by growing sideways." A real plant-lover laugh (plants leaning
  sideways toward the light), specific to this plant being moved this week,
  warm, true fortune cadence ("Someone will..."), no doom, no withering, no
  mockery. NOTE: the first draft ended "...in the most unexpected direction"
  and measured 121 chars, one over the gate; the assert caught it and the
  ending was tightened to "growing sideways" (97 chars), which also lands the
  joke on the last word.
"""
import os

ENTRY = ("You will lean toward the sun so far this week the gardener must "
         "turn your pot, and you will pretend it was your idea.")

assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} outside 1-120"
assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "must be one clean line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print(f"wrote {len(ENTRY)} chars")
