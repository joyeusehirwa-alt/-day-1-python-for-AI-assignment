# Assignment 2: Titanic Data Wrangling and Analysis

## What question I explored

I explored what factors were associated with passenger survival on the Titanic — 
specifically, how passenger class and fare related to who survived.

## What I found

- **Class mattered a lot.** First-class passengers survived at a rate of 62.6%, 
  compared to just 24.2% for third-class passengers — more than 2.5 times higher 
  (see `a2_chart1.png`).
- **Fare told a similar story.** Passengers who survived paid an average fare of 
  $48.21, compared to $22.12 for those who did not survive — survivors clearly 
  skewed toward higher-fare tickets, regardless of age (see `a2_chart2.png`).
- Using a standardized (z-score) computation on the fare column, I found at least 
  one extreme outlier — a fare roughly 9.7 standard deviations above the mean, 
  suggesting a small number of passengers paid dramatically more than everyone else.

## Limitation

The `deck` column was missing for about 77% of passengers, so I dropped it entirely 
rather than guessing at cabin locations. This means I couldn't explore whether cabin 
location on the ship affected survival, which could have been another meaningful 
factor tied to both class and proximity to lifeboats.


## Reflection

**Which transform took the longest, and why?**
Task 1 — loading the dataset and generating the schema report (checking shape, 
dtypes, nulls, and unique values) — took the longest. This wasn't because the code 
itself was hard, but because I was still learning what each of these commands 
actually meant and why they mattered, on top of getting my environment and 
notebook set up correctly.

**What would I do differently next time?**
Honestly, I'm not sure yet — this was my first time going through the full 
process, and I'm still building a mental model of what each step is for. I'd like 
to get more comfortable with the basics (like what `.isna()` or `groupby()` are 
actually doing) so the next dataset feels more familiar and less like starting 
from scratch.