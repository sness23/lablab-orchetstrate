---
marp: true
theme: gaia
class: invert
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
    background: #16213e !important;
    color: #00d4ff !important;
  }
  pre {
    background: #16213e !important;
    color: #00d4ff !important;
  }
  pre code {
    background: #16213e !important;
    color: #00d4ff !important;
  }
  a {
    color: #4ecdc4;
  }
  table {
    font-size: 0.8em !important;
    background: #16213e !important;
    border-collapse: collapse !important;
    width: 100% !important;
  }
  thead {
    background: #0f1527 !important;
  }
  tbody {
    background: #1a2332 !important;
  }
  th {
    background: #0f1527 !important;
    color: #00d4ff !important;
    padding: 10px !important;
    border: 1px solid #2a3f5f !important;
    font-weight: bold !important;
  }
  td {
    background: #1a2332 !important;
    color: #eaeaea !important;
    padding: 10px !important;
    border: 1px solid #2a3f5f !important;
  }
  tr:nth-child(even) td {
    background: #16213e !important;
  }
  tr:hover td {
    background: #1f2b45 !important;
  }
  /* Force dark theme on all possible SVG containers and elements */
  svg,
  svg:not(:root) {
    background: #16213e !important;
    overflow: visible !important;
  }
  svg foreignObject,
  svg foreignObject > * {
    background: #16213e !important;
    color: #00d4ff !important;
  }
  /* Alternative: Force all SVGs to have dark theme */
  svg,
  svg * {
    background: transparent !important;
  }
  svg {
    color: #eaeaea !important;
  }
  svg text,
  svg tspan {
    fill: #eaeaea !important;
    stroke: none !important;
  }
  svg rect:not([fill="none"]) {
    fill: #16213e !important;
    stroke: #2a3f5f !important;
  }
  svg rect[fill="white"],
  svg rect[fill="#ffffff"],
  svg rect[fill="#FFFFFF"],
  svg rect[fill="rgb(255,255,255)"] {
    fill: #16213e !important;
  }
  svg line,
  svg path:not([fill]) {
    stroke: #00d4ff !important;
    fill: none !important;
  }
  svg circle,
  svg ellipse {
    fill: #00d4ff !important;
    stroke: #2a3f5f !important;
  }
  svg polygon,
  svg polyline {
    fill: #16213e !important;
    stroke: #00d4ff !important;
  }
  /* Override any white backgrounds */
  svg[style*="background: white"],
  svg[style*="background: #fff"],
  svg[style*="background: rgb(255"],
  svg[style*="background-color: white"],
  svg[style*="background-color: #fff"],
  svg[style*="background-color: rgb(255"] {
    background: transparent !important;
  }
  /* Code block SVGs */
  pre svg,
  code svg,
  .language-text svg,
  .hljs svg {
    background: transparent !important;
  }
  pre svg rect,
  code svg rect,
  .language-text svg rect,
  .hljs svg rect {
    fill: #16213e !important;
  }
  pre svg text,
  code svg text,
  .language-text svg text,
  .hljs svg text {
    fill: #00d4ff !important;
  }
  /* Force override any inline styles */
  svg * {
    fill: currentColor !important;
  }
  svg text,
  svg tspan {
    fill: #00d4ff !important;
  }
  svg rect[fill]:not([fill="none"]) {
    fill: #16213e !important;
  }
  /* Target Marp's specific SVG rendering */
  section svg {
    background: transparent !important;
  }
  section svg text {
    fill: #00d4ff !important;
  }
  section svg rect {
    fill: #16213e !important;
  }
  /* Mermaid diagram specific styling */
  .mermaid svg {
    background: transparent !important;
  }
  .mermaid .node rect,
  .mermaid .node circle,
  .mermaid .node ellipse,
  .mermaid .node polygon {
    fill: #16213e !important;
    stroke: #00d4ff !important;
  }
  .mermaid .node text {
    fill: #eaeaea !important;
  }
  .mermaid .edgePath .path {
    stroke: #00d4ff !important;
  }
  .mermaid .edgeLabel {
    background: #1a2332 !important;
    color: #eaeaea !important;
  }
  .mermaid .cluster rect {
    fill: #0f1527 !important;
    stroke: #00d4ff !important;
  }
  blockquote {
    border-left: 4px solid #00d4ff;
    background: #16213e;
    padding: 10px 20px;
    font-style: italic;
  }
  /* Marp-specific overrides for code blocks that might be rendered as SVG */
  [data-marpit-svg],
  [data-marpit-svg] svg {
    background: #16213e !important;
  }
  [data-marpit-svg] foreignObject {
    background: #16213e !important;
  }
  /* Try to catch any element that might contain the SVG */
  .marpit > svg,
  .marpit svg {
    background: #16213e !important;
  }
  /* Override highlight.js if that's being used */
  .hljs {
    background: #16213e !important;
    color: #00d4ff !important;
  }
---

<!-- _paginate: false -->
<!-- _backgroundColor: #0f0f23 -->

# TechBio Lead Gen and SMYKM

## AI-Powered Sales Intelligence

**IBM watsonx Orchestrate Hackathon**

*Turn public research into personalized outreach*

---

# The Problem

## Sales Reps Spend 80% of Time Researching SMYKM

- Show Me You Know Me (SMYKM)
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
└──────┬──────────┬──────────┬────────────────┘
       │          │          │
   ┌───▼───┐  ┌───▼───┐  ┌───▼───┐  ┌────────┐
   │ Lead  │→ │Profile│→ │Product│→ │ SMYKM  │
   │Search │  │Builder│  │ Match │  │Outreach│
   └───────┘  └───────┘  └───────┘  └────────┘
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

