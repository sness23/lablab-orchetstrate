---
marp: true
theme: default
paginate: true
backgroundColor: #1a1a2e
color: #eaeaea
style: |
  section {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 28px;
  }
  h1 {
    color: #00d4ff;
    font-size: 2.2em;
    margin-bottom: 0.3em;
  }
  h2 {
    color: #00d4ff;
    font-size: 1.5em;
    margin-bottom: 0.3em;
  }
  h3 {
    margin-top: 0.3em;
    margin-bottom: 0.2em;
  }
  p {
    margin: 0.3em 0;
  }
  ul, ol {
    margin: 0.3em 0;
  }
  strong {
    color: #ff6b6b;
  }
  code {
    background: #16213e;
    color: #00d4ff;
  }
  a {
    color: #4ecdc4;
  }
  table {
    font-size: 0.8em;
  }
  th {
    background: #16213e;
    color: #00d4ff;
  }
  blockquote {
    border-left: 4px solid #00d4ff;
    background: #16213e;
    padding: 10px 20px;
    font-style: italic;
  }
---

<!-- _paginate: false -->
<!-- _backgroundColor: #0f0f23 -->

# TechBio Lead Gen & SMYKM

## AI-Powered Sales Intelligence

**IBM watsonx Orchestrate Hackathon**

*Turn public research into personalized outreach*

---

# The Problem

## Sales Reps Spend 80% of Time Researching

- Reading papers to understand their work
- Finding equipment they use
- Identifying pain points
- Crafting personalized emails

**Result**: Generic outreach that gets ignored

---

# Our Solution

## 4 AI Agents in watsonx Orchestrate

```
┌─────────────────────────────────────────────┐
│          watsonx Orchestrate                │
└──────┬──────────┬──────────┬───────────────┘
       │          │          │
   ┌───▼───┐  ┌───▼───┐  ┌───▼───┐  ┌───────┐
   │ Lead  │→ │Profile│→ │Product│→ │ SMYKM │
   │Search │  │Builder│  │ Match │  │Outreach│
   └───────┘  └───────┘  └───────┘  └───────┘
```

**Find leads → Build profiles → Match products → Personalize outreach**

---

# Demo: Alex Rives

## Our Target Lead

| Attribute | Value |
|-----------|-------|
| **Name** | Alex Rives |
| **Role** | Head of Science, CZI |
| **Research** | ESM3 - AI protein generation |
| **Funding** | $142M seed round |
| **Pain Point** | AI generates proteins in seconds, validation takes weeks |

---

# Step 1: Lead Discovery

## "Find leads in AI protein design"

**watsonx returns:**

| Name | Company | Score | Funding |
|------|---------|-------|---------|
| **Alex Rives** | EvolutionaryScale/CZI | 95 | $142M |

**Why high score**: Recent funding, direct equipment need, acute pain point

---

# Step 2: Profile Builder

## "What equipment does Alex Rives need?"

**Equipment Needs:**
- High-throughput X-ray crystallography
- Automated crystal screening (96-well)
- Fast data collection systems

**Pain Point:**
> "AI generates 1000 proteins/day. Traditional validation: 1-2/week. That's a **10,000x bottleneck**."

---

# Step 3: Product Match

## "Match Rigaku products for Alex Rives"

### Recommended: XtaLAB Synergy-S

| Factor | Synchrotron | Rigaku |
|--------|-------------|--------|
| Availability | Weeks to schedule | 24/7 |
| Speed | Days per structure | Hours |
| Cost | $500-2000/structure | ~$50 |

**Why it fits**: Closes the validation speed gap

---

# Step 4: SMYKM Outreach

## "Generate personalized outreach for Alex Rives"

**Subject**: Closing the loop on ESM3 validation

> Congratulations on the CZI announcement - excited to see ESM3's capabilities expand through Biohub.
>
> I've been thinking about a bottleneck you're likely facing: **ESM3 generates novel proteins in seconds, but traditional structural validation takes weeks.**
>
> The Rigaku XtaLAB Synergy-S could change that equation...

---

# Key Personalization Hooks

## What Makes It SMYKM

- ✅ References **CZI/Biohub** announcement
- ✅ Mentions **"500M years of evolution"** achievement
- ✅ Addresses **validation bottleneck** specifically
- ✅ Connects product to **his research goal**

**Every sentence shows we understand his work**

---

# Bonus Features

## Complete Sales Toolkit

| Feature | Purpose |
|---------|---------|
| **Battlecards** | Why Rigaku beats synchrotron/CRO |
| **Objection Handlers** | Pre-built responses to pushback |
| **Meeting Prep** | What to say, what to avoid |
| **Deal Probability** | AI-scored likelihood with reasoning |
| **Campaign Sequences** | 6-week multi-touch plan |
| **LinkedIn Content** | Social selling messages |

---

# Technical Implementation

## How It Works

```
https://doi.bio/resources/
├── leads/alex-rives.md
├── products/rigaku-xray-systems.md
└── outreach/alex-rives-smykm.md
```

- **FastAPI backend** serves resources
- **OpenAPI spec** for watsonx skill import
- **Markdown files** for easy updates

---

# ROI Impact

## The Numbers

| Metric | Manual | AI-Assisted |
|--------|--------|-------------|
| Research time | 3 hours | 5 minutes |
| Personalization | Surface | Deep |
| Response rate | 2% | 15%+ |

**Result**: 10x more leads, 7x better conversion

---

<!-- _backgroundColor: #0f0f23 -->

# Thank You

## TechBio Lead Gen & SMYKM

**Turn public research into personalized sales**

### Demo
- Lead: Alex Rives (ESM3, $142M)
- Product: Rigaku XtaLAB Synergy-S
- Result: Personalized email that converts

**GitHub**: github.com/sness23/lablab-orchestrate

*Questions?*
