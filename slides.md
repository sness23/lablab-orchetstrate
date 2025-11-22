---
marp: true
theme: default
paginate: true
backgroundColor: #1a1a2e
color: #eaeaea
style: |
  section {
    font-family: 'Segoe UI', Arial, sans-serif;
  }
  h1 {
    color: #00d4ff;
    font-size: 2.5em;
  }
  h2 {
    color: #00d4ff;
    font-size: 1.8em;
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
  .highlight {
    background: linear-gradient(90deg, #00d4ff, #4ecdc4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
---

<!-- _paginate: false -->
<!-- _backgroundColor: #0f0f23 -->

# TechBio Lead Gen & SMYKM

## AI-Powered Sales Intelligence for Life Sciences

<br>

**IBM watsonx Orchestrate Hackathon**

<br>

*Turning Public Research into Personalized Outreach*

---

# The Problem

## TechBio Sales is Broken

<br>

### Sales reps spend **80% of time** researching leads

- Reading papers to understand their work
- Finding equipment they use
- Identifying pain points
- Crafting personalized emails

<br>

### Result: **Generic outreach that gets ignored**

---

# The Opportunity

## Researchers Publish Everything

<br>

- **Papers** → Equipment & reagents they use
- **Preprints** → Current research direction
- **Funding** → Budget for new tools
- **News** → Recent achievements to reference

<br>

### This is **public intelligence** waiting to be mined

---

# Our Solution

## AI Agent Orchestrator

<br>

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

<br>

**4 specialized agents** working together

---

# Show Me You Know Me (SMYKM)

## The Key to TechBio Sales

<br>

### Generic Email:
> "Hi, I wanted to reach out about our X-ray systems..."

<br>

### SMYKM Email:
> "Your fluorescent protein paper showed 58% sequence identity - that's exactly the kind of novel structure that needs in-house validation..."

<br>

**Reference their work. Address their pain point.**

---

# Lead Discovery Results

## AI Protein Design Domain - Top 10 Leads

<br>

| Rank | Name | Company | Score | Funding |
|------|------|---------|-------|---------|
| 1 | **Alex Rives** | EvolutionaryScale/CZI | 95 | $142M |
| 2 | **Chris Bahl** | AI Proteins | 92 | $41M + BMS |
| 3 | **Simon Kohl** | Latent Labs | 91 | $50M |
| 4 | **Gevorg Grigoryan** | Generate:Biomedicines | 89 | $450M |
| 5 | **David Baker** | UW IPD | 88 | $100M+ |

<br>

*+ 5 more leads: Insilico, Insitro, Recursion, DeepMind...*

---

# Total Pipeline Value

## 10 Leads = **$2.4B+ in Funding**

<br>

| Company | Funding | Equipment Need |
|---------|---------|----------------|
| Insitro (Koller) | $700M | Structural validation |
| Generate:Bio | $450M | De novo protein validation |
| Insilico | $400M | Drug target structures |
| EvolutionaryScale | $142M | AI protein validation |
| Latent Labs | $50M | Building from scratch |

<br>

### All need crystallography for AI validation

---

# Demo: Alex Rives

## Our Top Lead

<br>

| Attribute | Value |
|-----------|-------|
| **Name** | Alex Rives |
| **Role** | Head of Science, CZI |
| **Company** | EvolutionaryScale → Biohub |
| **Research** | ESM3 protein AI |
| **Funding** | $142M seed round |

---

# ESM3: Why He Matters

## Breakthrough AI for Protein Design

<br>

- Trained on **2.78 billion proteins**
- Generated novel proteins = **500M years of evolution**
- Partners: **AWS, NVIDIA**

<br>

### His need: Validate AI-generated structures at scale

---

# The Pain Point

## Speed Mismatch

<br>

```
AI Protein Generation:     1000 proteins/day
Traditional Validation:    1-2 proteins/week
```

<br>

### That's a **10,000x bottleneck**

<br>

His AI is fast. His validation is slow.

---

# Product Match: Rigaku

## XtaLAB Synergy-S

<br>

### Why it fits:
- **Hours** instead of days per structure
- **HPC detectors** for weak diffraction
- **96-well screening** with XtalCheck-S
- **On-site** - no synchrotron scheduling

<br>

### Close the validation loop at AI speed

---

# The Personalized Pitch

## SMYKM Email

<br>

**Subject**: Closing the loop on ESM3 validation

> Congratulations on the CZI announcement - excited to see ESM3's capabilities expand through Biohub.
>
> I've been thinking about a bottleneck you're likely facing: **ESM3 generates novel proteins in seconds, but traditional structural validation takes weeks.**
>
> The Rigaku XtaLAB Synergy-S could change that equation...

---

# Key Personalization Hooks

## What Makes It SMYKM

<br>

- ✅ References **"500M years of evolution"** paper
- ✅ Mentions **CZI/Biohub** announcement
- ✅ Addresses **validation bottleneck** specifically
- ✅ Connects product to **their research goal**

<br>

**Every sentence shows we understand their work**

---

# Agent Architecture

## How It Works

<br>

### 1. Lead Discovery Agent
Searches publications, extracts researchers

### 2. Profile Builder Agent
Analyzes papers for equipment, pain points

### 3. Product Match Agent
Matches catalog items to needs

### 4. SMYKM Outreach Agent
Generates personalized email + strategy

---

# Beyond Email: Full Sales Toolkit

## 3 Additional Features That Close Deals

<br>

### 1. Competitive Battlecards
- What they use now (synchrotron, CRO)
- Why you win (speed, cost, control)
- Competitor counters (Bruker, cryo-EM)

### 2. Objection Handlers
- Pre-built responses to "no budget", "we use synchrotron"
- Lead-specific context in every response

### 3. Meeting Prep Briefings
- 30-second background
- Smart questions to ask
- Topics to avoid

---

# Battlecard Example: Alex Rives

## Why Rigaku Wins vs. Synchrotron

<br>

| Factor | Synchrotron | Rigaku | Winner |
|--------|-------------|--------|--------|
| Availability | Weeks | 24/7 | **Rigaku** |
| Travel | Required | None | **Rigaku** |
| Cost/structure | $500-2000 | ~$50 | **Rigaku** |
| Speed | Days | Hours | **Rigaku** |

<br>

**Killer argument**: "Your AI generates 1000 proteins/day. Synchrotron validates 2/week. On-site closes that gap."

---

# Objection Handler Example

## "We already have synchrotron access"

<br>

**Response**:

> "Synchrotrons are excellent for challenging cases. The question is throughput - if ESM3 generates 1000 candidates, can you validate enough to close the feedback loop?
>
> On-site capability handles the volume; reserve synchrotron for edge cases."

<br>

*Response auto-personalized with lead's funding, company, and pain points*

---

# Meeting Prep Example

## Before Your Call with Alex Rives

<br>

**30-Second Background**: Head of Science at CZI, built ESM3, $142M funding

**Must Reference**:
- CZI/Biohub announcement
- "500M years of evolution" paper
- AWS/NVIDIA compute partnerships

**Smart Questions**:
- "What's your current validation throughput?"
- "How much time from design to structure?"

**Avoid**: Meta layoffs, AlphaFold comparisons

---

# Deal Probability Scorer

## AI Explains Its Reasoning

<br>

**Alex Rives: 87% Probability**

| Factor | Score | Reasoning |
|--------|-------|-----------|
| Funding Recency | 15/20 | Recent funding (2024) - growth mode |
| Funding Amount | 15/20 | $142M - budget available |
| Equipment Match | 25/25 | Direct crystallography need |
| Pain Severity | 20/20 | Speed bottleneck - high urgency |
| Competition | 12/15 | Growth stage - expanding |

**Recommendation**: STRONG OPPORTUNITY - Active pursuit

---

# Multi-Touch Campaign

## 6-Week Sequence for Alex Rives

<br>

| Week | Channel | Action |
|------|---------|--------|
| 1 | Email | SMYKM personalized email |
| 1 | LinkedIn | Connection request |
| 2 | Email | Share case study |
| 3 | Email | Webinar invite |
| 4 | Phone | Call attempt |
| 5 | Email | Demo offer |
| 6 | Email | Executive touch |

<br>

*10 touches across 3 channels over 6 weeks*

---

# LinkedIn Social Selling

## Multi-Channel Approach

<br>

### Connection Request (300 char limit)
> "Hi Alex, I've been following EvolutionaryScale's work on AI protein generation. ESM3 caught my attention - impressive results. Would love to connect and learn more about your validation workflows."

<br>

### Comment Templates
> "Fascinating approach to AI protein generation. The throughput implications for validation are significant - would love to hear more..."

---

# Complete Platform: 10 Capabilities

<br>

| # | Capability | Purpose |
|---|------------|---------|
| 1 | Lead Search | Find leads by domain |
| 2 | Profile Builder | Equipment needs, pain points |
| 3 | Product Match | Recommend products |
| 4 | SMYKM Outreach | Personalized email |
| 5 | Battlecards | Competitive intelligence |
| 6 | Objection Handlers | Pre-built responses |
| 7 | Meeting Prep | Pre-call briefing |
| 8 | Deal Probability | AI-scored likelihood |
| 9 | Campaigns | 6-week sequences |
| 10 | LinkedIn | Social selling content |

---

# Technical Implementation

## External Resources on doi.bio

<br>

```
https://doi.bio/resources/
├── leads/alex-rives.md
├── products/rigaku-xray-systems.md
└── outreach/alex-rives-smykm.md
```

<br>

### watsonx fetches markdown → AI processes → Response

---

# watsonx Skills

## Custom Skill Definitions

<br>

| Skill | Function |
|-------|----------|
| `techbio-lead-search` | Find leads by domain |
| `techbio-profile-enrich` | Build detailed profiles |
| `techbio-product-match` | Match products to needs |
| `techbio-smykm-generate` | Create personalized outreach |

<br>

Skills chain automatically or run individually

---

# Live Demo

## watsonx Orchestrate Commands

<br>

```
Find leads in AI protein design
```

```
What equipment does Alex Rives need?
```

```
Match Rigaku products for Alex Rives
```

```
Generate personalized outreach for Alex Rives
```

---

# Value Proposition

## For Sales Teams

<br>

### Before (Manual Research)
- 2-3 hours per lead
- Generic outreach
- Low response rates

<br>

### After (AI Orchestrator)
- **Minutes** per lead
- Personalized to their work
- **Higher conversion**

---

# ROI Impact

## The Numbers

<br>

| Metric | Manual | AI-Assisted | Improvement |
|--------|--------|-------------|-------------|
| Research time | 3 hours | 5 minutes | **36x faster** |
| Leads/week | 10 | 100+ | **10x more** |
| Response rate | 2% | 15%+ | **7x higher** |
| Revenue/rep | $500K | $3.5M | **7x more** |

<br>

### Annual Impact (10-person sales team)
**$30M additional revenue potential**

---

# ROI Calculator

## Real Numbers for TechBio Sales

<br>

### Assumptions
- Average deal size: $350K (equipment sale)
- Sales cycle: 6 months
- Current close rate: 5%

### With AI Orchestrator
- More qualified leads → Higher close rate (8%)
- Better personalization → Shorter cycle (4 months)
- **Result: 2.4x more closed deals per rep**

---

# Market Opportunity

## TechBio is Huge

<br>

- **$1.3T** life sciences market
- **Thousands** of equipment vendors
- **Millions** of researchers publishing

<br>

### Every researcher is a potential lead
### Every paper is sales intelligence

---

# Future Roadmap

## What's Next

<br>

- 📡 **Paper monitoring** - Alerts when leads publish
- 🔗 **CRM integration** - Sync with Salesforce
- 🏭 **Multi-vendor** - Add more product catalogs
- 📊 **Analytics** - Track what personalization works

---

# Competitive Advantage

## Why This Wins

<br>

### vs. LinkedIn Sales Navigator
We read their **actual papers**, not just job changes

### vs. Generic AI Emails
We reference **specific research**, not templates

### vs. Manual Research
**10x faster** with deeper personalization

---

# Tech Stack

## Built With

<br>

- **watsonx Orchestrate** - Agent orchestration
- **Markdown** - External knowledge resources
- **doi.bio** - Resource hosting

<br>

### Simple, extensible, maintainable

---

<!-- _backgroundColor: #0f0f23 -->

# Thank You

## TechBio Lead Gen & SMYKM

<br>

**Turn public research into personalized sales**

<br>

### Links
- GitHub: github.com/sness23/lablab-orchestrate
- Resources: doi.bio/resources

<br>

*Questions?*

---

# Appendix: Example Output

## Full Email Generated

<br>

**Subject**: Closing the loop on ESM3 validation

Hi Alex,

Congratulations on the CZI announcement - excited to see ESM3's capabilities expand through Biohub.

I've been thinking about a bottleneck you're likely facing: ESM3 generates novel proteins in seconds, but traditional structural validation takes weeks. That's a 10,000x speed mismatch.

Would a 15-minute call to discuss your validation infrastructure make sense?

---

# Appendix: Agent Flow

## Complete Orchestration

<br>

```
User: "Find TechBio leads and generate outreach"

Step 1: [Lead Search] → Alex Rives (Score: 95)
Step 2: [Profile] → Equipment needs, pain points
Step 3: [Product Match] → XtaLAB Synergy-S
Step 4: [SMYKM] → Personalized email

Output: Ready-to-send outreach package
```
