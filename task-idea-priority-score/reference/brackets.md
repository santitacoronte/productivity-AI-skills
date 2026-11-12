# Categories and brackets

Eight categories, worded as in The One Thing app and the 3D Prioritization Map. Always use these names and questions with the user, word for word. The key is only for score.py; never show it.

## Setup: how important is each category?

Ask: "When you choose what to work on, how important is ...?" for each category below. Answer options: "Very important (10)", "Important (7)", "A little important (3)", "Not important (0)". Any number from 0 to 10 is fine.

| Key | Name | Setup question |
|---|---|---|
| return | Money | How important is how much money it can make in a year? |
| cost | Cost | How important is how much it will cost? |
| optional | Optional | How important is whether it's a must-do or optional? |
| desire | Important to you | How important is how much it matters to you personally? |
| urgency | Urgent | How important is how soon you need to start? |
| time | Time | How important is how much time it will take to complete? |
| impact | Impact | How important is who would notice the result? |
| career | Career boost | How important is what it does for your career? |

## Scoring: the question for each task

| Key | Question | Answers (level 0 to 4) |
|---|---|---|
| return | How much money can you make in a year? | 0 none · 1 a little (up to 10% of your big result) · 2 some (10 to 50%) · 3 a lot (50 to 100%) · 4 more than your big result |
| cost | How much will it cost? | 0 nothing · 1 a little (up to 10% of your big spend) · 2 some (10 to 50%) · 3 a lot (50 to 100%) · 4 more than your big spend |
| optional | How optional is this? Ask yourself: if you walked away from this tomorrow, would something break? | 0 nothing breaks · 1 a few things get harder · 2 something breaks, but it can wait · 3 something important breaks · 4 a lot breaks |
| desire | How important is it to you? Some things you don't need to do, but you want to. | 0 to 10 |
| urgency | Is it urgent? How soon do you need to start? Is there a tight deadline? | 0 no rush · 1 this quarter · 2 this month · 3 this week · 4 today, tight deadline |
| time | How much time will it take to complete? | 0 under a day · 1 a week · 2 a month · 3 a quarter · 4 six months or more |
| impact | Who would notice the result? | 0 barely noticed · 1 my team · 2 my manager · 3 my department · 4 the company |
| career | What does it do for your career? | 0 routine work · 1 a new skill · 2 noticed beyond my team · 3 leadership sees it · 4 my next role |

Cost and time count against a task: a high level lowers the score. All the others raise it.

"Big result" and "big spend" are the user's own amounts from setup: "How much money in a year would be a big result for you?" and "How much spending would feel big for you?"

## Filling a category from data

- **Money, cost:** an amount in the user's currency. Cost is money spent plus hours times the hourly cost. If the user gives hours per week, multiply by the weeks until it's done. score.py turns amounts into levels using the user's two amounts.
- **Time:** days until it's done (calendar days).
- **Urgent:** a start date or deadline gives the level directly.
- **Hourly cost:** the user's own figure first. If they give hours but no rate, use Eurostat's 2024 EU average labour cost, €33.50 per hour (full cost to the employer: wages plus non-wage costs), source https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250328-1 , and mark it "estimate". Outside the EU, ask for their country's figure or their own.
- **Important to you, career boost:** only the user can answer these. Always ask, never guess.

## Input for score.py

```json
{
  "weights": {"return": 7, "cost": 5, "optional": 10, "desire": 3, "urgency": 7, "time": 3, "impact": 7, "career": 3},
  "anchors": {"big_return": 50000, "big_spend": 10000},
  "hourly_cost": 33.5,
  "tasks": [
    {"name": "Password help article",
     "c": {
       "return":   {"amount": 12000, "src": "data: 900 tickets x 4 min x EUR 33.50/h"},
       "cost":     {"hours": 6, "src": "estimate"},
       "optional": {"level": 3, "src": "you"},
       "time":     {"days": 2, "src": "you"},
       "desire":   {"value": 6, "src": "you"},
       "impact":   {"unknown": true}
     }}
  ]
}
```

Each entry takes `level` (0 to 4), or the raw form for its category (`amount`, `hours`, `days`, `value`), or `"unknown": true`. `src` starts with `data`, `you`, `estimate` or `unknown`; add the source after a colon. A category left out counts as unknown. A category with weight 0 is ignored.
