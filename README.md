# Bandit Running — Marketing Case Study
### The Deal & Strategy Project | Week 4
**By Zama López Linhardt**

> *How does a sock brand with no paid ads, no celebrity endorsements, and no industry background become a cultural staple in one of the most competitive apparel markets in the world in under four years?*

---

## The Argument

Marketing is consistently underestimated in business education. It is treated as soft, intuitive, less rigorous than finance or strategy. This case study exists to challenge that directly.

Bandit Running proves that marketing is not a support function. In the right hands it is the founding architecture of the entire business. The product was socks. The strategy was community. Four years later: $14.2M raised, a membership flywheel with 7x LTV differential, and the most talked-about brand at the US Olympic Trials.

---

## The Decision Problem

Bandit launched in October 2020 with two self-imposed constraints: never push the product on anyone unprompted, and run zero paid ads in the first year. For a marketer, these are almost irrational rules. They worked precisely because of the restraint.

This analysis asks: what was the marketing architecture that made this possible, what do the economics look like, and what happens when institutional capital forces the brand to scale?

---

## Analysis Outputs

| Output | Description |
|--------|-------------|
| Fig 1 | Member vs non-member LTV, spend multiplier, referral rate |
| Fig 2 | Membership flywheel simulation over 48 months |
| Fig 3 | Unsponsored Project growth and viral reach |
| Fig 4 | Scale risk heatmap: LTV degradation as paid acquisition grows |

---

## Key Findings

- Member LTV is $850 vs $120 for non-members — a 7x differential
- Members spend 3.2x more annually and refer an average of 2.3 new customers
- The Unsponsored Project generated 3.3M Instagram views from a single analyst video
- 6 athletes secured full professional sponsorships after participating
- The flywheel compounds without paid acquisition — until it does not
- At 50%+ paid/retail customer acquisition, blended LTV degrades materially

---

## The Risk

The $14.2M Series A creates pressure to scale distribution. Every customer acquired through paid channels rather than community pull slightly dilutes the flywheel. The signal to watch is not revenue growth. It is referral rate. If referrals drop below 1.5x, the flywheel is slowing. And once community loyalty erodes, no ad budget brings it back.

---

## Repo Structure
```
bandit-running-marketing-case-study/
├── README.md
├── bandit_analysis.py          # Python model — all four outputs
├── data/
│   └── sources.md              # Full reference list with exact URLs
├── outputs/
│   ├── fig1_ltv_comparison.png
│   ├── fig2_flywheel.png
│   ├── fig3_unsponsored.png
│   └── fig4_scale_risk.png
└── report/
    └── W4_Bandit_Running_Report.pdf
```

---

## How to Run
```bash
pip install matplotlib seaborn numpy reportlab
python bandit_analysis.py
```

All four figures save to the working directory.

---

## Series Context

The Deal & Strategy Project is a self-directed weekly series testing real business decisions through structured, evidence-based analysis.

| Week | Topic | Core Question |
|------|-------|---------------|
| W1 | Prediction Markets | When does a probability edge survive real-world constraints? |
| W2 | PE Valuation (Adobe) | When does a great company become a bad investment? |
| W3 | M&A — Strava x Runna | Does the acquisition strengthen the IPO story or risk brand dilution? |
| W4 | Marketing — Bandit Running | How does a sock brand with no ad spend become a cultural staple? |

Posts every Tuesday at 11am CEST.

---

## References

Full reference list with exact URLs available in `data/sources.md`.

All sources accessed March 2026.

---

*The Deal & Strategy Project — github.com/ZamaLopezLinhardt*
