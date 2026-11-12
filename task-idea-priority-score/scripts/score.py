"""Priority score: turns per-category answers into a weighted 0-100 score and ranks tasks.

Usage:  python score.py input.json      (prints a markdown ranking)
        python score.py --selftest
Input format is documented in ../reference/brackets.md ("Input for score.py").
"""
import json
import sys

# Benefit categories: higher level = better. Inverse: higher level = worse.
BENEFIT = ["return", "optional", "desire", "urgency", "impact", "career"]
INVERSE = ["cost", "time"]
CATEGORIES = BENEFIT + INVERSE
KNOWN = ("data", "you")  # sources that count toward confidence
NAMES = {"return": "money", "cost": "cost", "optional": "optional", "desire": "important to you",
         "urgency": "urgent", "time": "time", "impact": "impact", "career": "career boost"}


def money_level(amount, big):
    if amount <= 0:
        return 0
    r = amount / big
    return 1 if r <= 0.1 else 2 if r <= 0.5 else 3 if r <= 1 else 4


def time_level(days):
    return 0 if days <= 1 else 1 if days <= 7 else 2 if days <= 31 else 3 if days <= 92 else 4


def value(cat, e, s):
    """Return (value 0..1, level label, source) for one category entry."""
    if not e or e.get("unknown"):
        return 0.5, "unknown", "unknown"
    src = e.get("src", "you")
    if cat == "desire":
        v = max(0, min(10, float(e["value"])))
        return v / 10, f"{v:g}/10", src
    if "level" in e:
        lvl = int(e["level"])
    elif cat == "return":
        lvl = money_level(float(e["amount"]), s["anchors"]["big_return"])
    elif cat == "cost":
        amount = float(e.get("amount", 0))
        if "hours" in e:
            if not s.get("hourly_cost"):
                raise ValueError("cost given in hours but no hourly_cost: set the user's rate or the Eurostat estimate")
            amount += float(e["hours"]) * float(s["hourly_cost"])
        lvl = money_level(amount, s["anchors"]["big_spend"])
    elif cat == "time":
        lvl = time_level(float(e["days"]))
    else:
        raise ValueError(f"{cat}: needs 'level' (0-4)")
    if not 0 <= lvl <= 4:
        raise ValueError(f"{cat}: level {lvl} outside 0-4")
    v = lvl / 4
    return (1 - v if cat in INVERSE else v), f"level {lvl}", src


def score_task(t, s):
    w = s["weights"]
    rows, total, wsum, known = [], 0.0, 0.0, 0.0
    for cat in CATEGORIES:
        wt = float(w.get(cat, 0))
        if wt <= 0:
            continue
        v, label, src = value(cat, t.get("c", {}).get(cat), s)
        total += wt * v
        wsum += wt
        known += wt if src.split(":")[0].strip() in KNOWN else 0
        rows.append((cat, v, wt, label, src))
    if wsum == 0:
        raise ValueError("all weights are 0")
    score = round(100 * total / wsum)
    conf = round(100 * known / wsum)
    push = max(rows, key=lambda r: (r[1] - 0.5) * r[2])
    pull = min(rows, key=lambda r: (r[1] - 0.5) * r[2])
    return {"name": t["name"], "score": score, "confidence": conf,
            "push": NAMES[push[0]] if (push[1] - 0.5) * push[2] > 0 else "-",
            "pull": NAMES[pull[0]] if (pull[1] - 0.5) * pull[2] < 0 else "-",
            "rows": rows}


def rank(s):
    return sorted((score_task(t, s) for t in s["tasks"]), key=lambda r: -r["score"])


def render(results):
    out = ["| # | Task | Score | Confidence | Pushed up by | Pulled down by |",
           "|---|---|---|---|---|---|"]
    for i, r in enumerate(results, 1):
        out.append(f"| {i} | {r['name']} | {r['score']} | {r['confidence']}% | {r['push']} | {r['pull']} |")
    out.append("")
    for r in results:
        out.append(f"**{r['name']}**: " + "; ".join(
            f"{NAMES[c]} {lab} (weight {w:g}, {src})" for c, v, w, lab, src in r["rows"]))
    return "\n".join(out)


def selftest():
    s = {"weights": {"optional": 10, "return": 5, "cost": 5, "time": 0, "desire": 5},
         "anchors": {"big_return": 100000, "big_spend": 10000}, "hourly_cost": 50,
         "tasks": [
             {"name": "A", "c": {"optional": {"level": 4, "src": "you"}, "return": {"amount": 200000, "src": "data"},
                                 "cost": {"hours": 0, "amount": 0, "src": "data"}, "desire": {"value": 10}}},
             {"name": "B", "c": {"optional": {"level": 0, "src": "you"}, "return": {"amount": 0, "src": "data"},
                                 "cost": {"hours": 400, "src": "estimate"}, "desire": {"value": 0}}},
             {"name": "C", "c": {}}]}
    a, c, b = rank(s)
    assert (a["name"], a["score"], a["confidence"]) == ("A", 100, 100), a
    assert (b["name"], b["score"]) == ("B", 0), b  # 400h x 50 = 20000 > big spend
    assert b["confidence"] == 80, b  # cost was an estimate (weight 5 of 25)
    assert (c["score"], c["confidence"]) == (50, 0), c
    assert money_level(5000, 10000) == 2 and time_level(7) == 1 and time_level(200) == 4
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        with open(sys.argv[1], encoding="utf-8") as f:
            print(render(rank(json.load(f))))
