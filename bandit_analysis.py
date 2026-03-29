"""
================================================================================
BANDIT RUNNING — MARKETING CASE STUDY
W4 — The Deal & Strategy Project
Author: Zama Lopez Linhardt
================================================================================

REFERENCES:
[1] Bandit founded Oct 2020, zero paid ads year one, community-first:
    shopify.com/blog/bandit-community
[2] $14.2M Series A, led by A-Rod Corp and VCP Ventures, Sep 2023:
    inc.com/sydney-sladovnik/how-an-underdog-brand-made-it-to-olympics.html
[3] Member LTV $850 vs $120 non-member, 3.2x spend, 2.3 referrals:
    thedigitalchapter.com/p/how-bandit-running-built-a-14m-brand-without-paid-ads
[4] Unsponsored Project 2023: 9 athletes. 2024: 35+. 2025: 50+:
    banditrunning.com/pages/unsponsored-project-2024
[5] Jordan Rogers video: 3.3M Instagram views, 315K TikTok views:
    inc.com/sydney-sladovnik/how-an-underdog-brand-made-it-to-olympics.html
[6] 6 athletes signed full sponsorships after Unsponsored Project:
    cultureofsport.substack.com/p/bandit-runnings-unsponsored-project-c3f
[7] 100+ people at Saturday community runs, Williamsburg store:
    shopify.com/blog/bandit-community
[8] YouTube series Dialed: 6,000+ subscribers, comments driving membership:
    thedigitalchapter.com/p/how-bandit-running-built-a-14m-brand-without-paid-ads
[9] Run club memberships +59% globally in 2024 (Strava Year in Sport):
    press.strava.com/articles/strava-releases-annual-year-in-sport-trend
[10] 72% of Gen Z join run clubs to meet people, 22% call it new dating app:
    bostonrunandoutdoor.com/2025/07/24/running-clubs-pumping-new-blood-into-retail
[11] Global running apparel market ~$13B:
    brandscape.substack.com/p/how-running-communities-ushered-in
[12] Community-first brand case, edition+partners deep dive:
    edition.partners/articles/bandit-community-creates-performance
[13] How Bandit built underground running brand in 4 years:
    thecaseforbrand.substack.com/p/how-bandit-is-building-the-underground
[14] Bandit NYC Marathon pop-up, annual touring tradition:
    hypebae.com/2025/10/bandit-running-nyc-marathon-pop-up-store-fashion-info
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Style ─────────────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", font="DejaVu Sans")
C = {
    "brand":   "#E8533C",   # Bandit warm red-orange
    "dark":    "#1a1a2e",
    "mid":     "#4a4a6a",
    "light":   "#f5f0eb",
    "green":   "#2ecc71",
    "amber":   "#f39c12",
    "blue":    "#3498db",
    "muted":   "#95a5a6",
}
plt.rcParams.update({
    "figure.facecolor":  "white",
    "axes.facecolor":    "white",
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.titlesize":    13,
    "axes.titleweight":  "bold",
    "axes.labelsize":    11,
    "xtick.labelsize":   9,
    "ytick.labelsize":   9,
    "figure.dpi":        150,
})

import matplotlib.ticker as mticker

def sf(path):
    plt.savefig(path, bbox_inches="tight", dpi=150)
    plt.close()
    print(f"Saved: {path}")

# ══════════════════════════════════════════════════════════════════════════════
# FIG 1 — MEMBERSHIP FLYWHEEL: LTV COMPARISON
# ══════════════════════════════════════════════════════════════════════════════

def fig1_ltv():
    labels   = ["Non-member\n(one-time)", "Paid Member"]
    ltv      = [120, 850]              # [3]
    spend_x  = [1.0, 3.2]             # 3.2x spend [3]
    referrals= [0.0, 2.3]             # avg referrals per member [3]

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.suptitle("Membership Flywheel — Bandit Running Customer Economics [3]",
                 fontsize=14, fontweight="bold", color=C["dark"], y=1.01)

    # LTV bars
    ax = axes[0]
    bars = ax.bar(labels, ltv, color=[C["muted"], C["brand"]],
                  width=0.5, edgecolor="white")
    for bar, val in zip(bars, ltv):
        ax.text(bar.get_x() + bar.get_width()/2,
                val + 12, f"${val}", ha="center", fontsize=11, fontweight="bold",
                color=C["dark"])
    ax.set_title("Customer Lifetime Value")
    ax.set_ylabel("LTV (USD)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.0f}"))
    ax.annotate("7x higher", xy=(1, 850), xytext=(0.5, 600),
                fontsize=10, color=C["brand"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=C["brand"]))

    # Annual spend multiplier
    ax2 = axes[1]
    bars2 = ax2.bar(labels, spend_x, color=[C["muted"], C["brand"]],
                    width=0.5, edgecolor="white")
    for bar, val in zip(bars2, spend_x):
        ax2.text(bar.get_x() + bar.get_width()/2,
                 val + 0.05, f"{val}x", ha="center", fontsize=11,
                 fontweight="bold", color=C["dark"])
    ax2.set_title("Annual Spend Multiplier")
    ax2.set_ylabel("Relative Annual Spend")
    ax2.set_ylim(0, 4)

    # Referrals
    ax3 = axes[2]
    bars3 = ax3.bar(labels, referrals, color=[C["muted"], C["brand"]],
                    width=0.5, edgecolor="white")
    for bar, val in zip(bars3, referrals):
        ax3.text(bar.get_x() + bar.get_width()/2,
                 val + 0.05, f"{val}", ha="center", fontsize=11,
                 fontweight="bold", color=C["dark"])
    ax3.set_title("Avg. New Customers Referred")
    ax3.set_ylabel("Referrals per Customer")
    ax3.set_ylim(0, 3.5)

    plt.tight_layout()
    sf("/home/claude/fig1_ltv_comparison.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIG 2 — MEMBERSHIP FLYWHEEL COMPOUNDING SIMULATION
# ══════════════════════════════════════════════════════════════════════════════

def fig2_flywheel():
    months   = np.arange(0, 49)
    m0       = 500          # starting members
    ref_rate = 2.3          # referrals per member per year [3]
    churn_m  = 0.03         # 3% monthly churn assumption

    def simulate(ref_rate, churn, label):
        members = [m0]
        for _ in months[1:]:
            new = members[-1] * (ref_rate / 12)
            lost = members[-1] * churn
            members.append(members[-1] + new - lost)
        return np.array(members)

    bull = simulate(2.3,  0.02, "Bull")
    base = simulate(2.3,  0.04, "Base")
    bear = simulate(1.0,  0.06, "Bear — diluted community")

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Membership Flywheel Simulation — 48-Month Horizon",
                 fontsize=14, fontweight="bold", color=C["dark"], y=1.01)

    # Trajectory
    ax = axes[0]
    ax.plot(months, bull/1e3, color=C["green"],  lw=2.2, label="Bull (low churn)")
    ax.plot(months, base/1e3, color=C["brand"],  lw=2.2, label="Base case")
    ax.plot(months, bear/1e3, color=C["muted"],  lw=2.2, label="Bear (diluted)",
            ls="--")
    ax.axvline(24, color=C["amber"], ls=":", lw=1.5,
               label="Month 24 — Series A pressure point")
    ax.set_xlabel("Months")
    ax.set_ylabel("Paying Members (thousands)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}K"))
    ax.legend(fontsize=8)
    ax.set_title("Member Growth Trajectory")
    ax.fill_between(months, bear/1e3, bull/1e3, alpha=0.06, color=C["brand"])

    # Revenue impact at checkpoints
    ax2 = axes[1]
    checkpoints = [12, 24, 36, 48]
    avg_spend = 850   # member LTV proxy per year [3]
    bull_rev = [bull[m] * avg_spend / 1e6 for m in checkpoints]
    base_rev = [base[m] * avg_spend / 1e6 for m in checkpoints]
    bear_rev = [bear[m] * avg_spend / 1e6 for m in checkpoints]
    x = np.arange(len(checkpoints))
    w = 0.25
    ax2.bar(x - w,   bull_rev, w, color=C["green"], label="Bull", edgecolor="white")
    ax2.bar(x,       base_rev, w, color=C["brand"], label="Base", edgecolor="white")
    ax2.bar(x + w,   bear_rev, w, color=C["muted"], label="Bear", edgecolor="white",
            alpha=0.8)
    ax2.set_xticks(x)
    ax2.set_xticklabels([f"Month {m}" for m in checkpoints])
    ax2.set_ylabel("Implied Member Revenue (USD millions)")
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.0f}M"))
    ax2.legend(fontsize=8)
    ax2.set_title("Implied Revenue at Key Checkpoints")

    plt.tight_layout()
    sf("/home/claude/fig2_flywheel.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIG 3 — UNSPONSORED PROJECT GROWTH + VIRALITY
# ══════════════════════════════════════════════════════════════════════════════

def fig3_unsponsored():
    years    = [2023, 2024, 2025]
    athletes = [9, 35, 50]            # [4]
    signed   = [1, 5, 6]              # athletes who gained full sponsorships [6]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("The Unsponsored Project — Growth & Impact [4][5][6]",
                 fontsize=14, fontweight="bold", color=C["dark"], y=1.01)

    # Athletes supported
    ax = axes[0]
    bars = ax.bar([str(y) for y in years], athletes,
                  color=C["brand"], width=0.5, edgecolor="white")
    for bar, val in zip(bars, athletes):
        ax.text(bar.get_x() + bar.get_width()/2,
                val + 0.8, str(val), ha="center", fontsize=12,
                fontweight="bold", color=C["dark"])
    ax.set_title("Athletes Supported per Year")
    ax.set_ylabel("Number of Athletes")
    ax.set_xlabel("Year")

    # Viral reach
    ax2 = axes[1]
    channels = ["Instagram\n(Jordan Rogers)", "TikTok\n(Jordan Rogers)",
                "Athletes Gained\nFull Sponsorships"]
    values   = [3.3, 0.315, 6]
    colors   = [C["brand"], C["amber"], C["green"]]
    bars2    = ax2.bar(channels, values, color=colors, width=0.5, edgecolor="white")
    for bar, val in zip(bars2, values):
        label = f"{val}M views" if val > 1 else f"{int(val*1000)}K views" \
                if val < 1 else f"{int(val)} athletes"
        ax2.text(bar.get_x() + bar.get_width()/2,
                 val + 0.05, label, ha="center", fontsize=9,
                 fontweight="bold", color=C["dark"])
    ax2.set_title("Viral Reach & Downstream Impact")
    ax2.set_ylabel("Millions (views) / Count (athletes)")
    ax2.set_ylim(0, 4.2)

    plt.tight_layout()
    sf("/home/claude/fig3_unsponsored.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIG 4 — SCALE RISK HEATMAP
# Community dilution risk as distribution grows
# ══════════════════════════════════════════════════════════════════════════════

def fig4_scale_risk():
    """
    Two dimensions: % of customers acquired via paid/retail (non-community)
    vs referral rate. Shows how LTV and flywheel degrade as brand scales.
    """
    paid_pct  = np.array([0, 10, 20, 30, 40, 50, 60, 70])   # % non-community
    ref_rates = np.array([2.3, 2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.5])

    # Model: blended LTV degrades as non-community % rises
    ltv_matrix = np.zeros((len(ref_rates), len(paid_pct)))
    for i, ref in enumerate(ref_rates):
        for j, paid in enumerate(paid_pct):
            comm_pct = 1 - paid/100
            ltv_blend = (comm_pct * 850) + ((1-comm_pct) * 120)
            ref_factor = ref / 2.3
            ltv_matrix[i, j] = ltv_blend * ref_factor

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(
        ltv_matrix,
        annot=True,
        fmt=".0f",
        cmap="RdYlGn",
        center=400,
        xticklabels=[f"{p}%" for p in paid_pct],
        yticklabels=[f"{r}x" for r in ref_rates],
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"label": "Blended LTV (USD)"},
        ax=ax,
    )
    ax.set_title(
        "Scale Risk — Blended LTV as Non-Community Acquisition % Grows\n"
        "(Row = referral rate, Col = % customers acquired via paid/retail)",
        fontsize=12, fontweight="bold", color=C["dark"]
    )
    ax.set_xlabel("% of Customers Acquired via Paid / Retail Channels")
    ax.set_ylabel("Referral Rate (members per member)")
    plt.tight_layout()
    sf("/home/claude/fig4_scale_risk.png")


# ── Run all ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  BANDIT RUNNING — W4 Deal & Strategy Project")
    print("=" * 60)
    print("\n[1/4] LTV comparison...")
    fig1_ltv()
    print("[2/4] Membership flywheel simulation...")
    fig2_flywheel()
    print("[3/4] Unsponsored Project impact...")
    fig3_unsponsored()
    print("[4/4] Scale risk heatmap...")
    fig4_scale_risk()
    print("\nAll figures saved.")

