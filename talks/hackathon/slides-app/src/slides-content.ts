export const slidesContent = `
<section data-background="#0f0f23">
<h1>TechBio Lead Gen and SMYKM</h1>
<h2>AI-Powered Sales Intelligence</h2>

<p><strong>IBM watsonx Orchestrate Hackathon</strong></p>

<p><em>Turn public research into personalized outreach</em></p>
</section>

<section>
<h1>The Problem</h1>
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

<div style="background: #1a2332; padding: 20px; border-radius: 8px; font-family: monospace;">
<pre style="color: #00d4ff; margin: 0;">
┌─────────────────────────────────────────────┐
│          watsonx Orchestrate                │
└──────┬──────────┬──────────┬────────────────┘
       │          │          │
   ┌───▼───┐  ┌───▼───┐  ┌───▼───┐  ┌────────┐
   │ Lead  │→ │Profile│→ │Product│→ │ SMYKM  │
   │Search │  │Builder│  │ Match │  │Outreach│
   └───────┘  └───────┘  └───────┘  └────────┘
</pre>
</div>

**Find leads → Build profiles → Match products → Personalize outreach**

---

# Demo: Alex Rives
## Our Target Lead

<table style="width: 100%;">
  <tr>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Attribute</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Value</th>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Name</strong></td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Alex Rives</td>
  </tr>
  <tr>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Role</strong></td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Head of Science, CZI</td>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Research</strong></td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">ESM3 - AI protein generation</td>
  </tr>
  <tr>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Funding</strong></td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">$142M seed round</td>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Pain Point</strong></td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">AI generates proteins in seconds, validation takes weeks</td>
  </tr>
</table>

---

# Step 1: Lead Discovery
## "Find leads in AI protein design"

**watsonx returns:**

<table style="width: 100%;">
  <tr>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Name</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Company</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Score</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Funding</th>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong style="color: #ff6b6b;">Alex Rives</strong></td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">EvolutionaryScale/CZI</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">95</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">$142M</td>
  </tr>
</table>

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

<table style="width: 100%;">
  <tr>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Factor</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Synchrotron</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Rigaku</th>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Availability</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Weeks to schedule</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">24/7</td>
  </tr>
  <tr>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Speed</td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Days per structure</td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Hours</td>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Cost</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">$500-2000/structure</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">~$50</td>
  </tr>
</table>

**Why it fits**: Closes the validation speed gap

---

# Step 4: SMYKM Outreach
## "Generate personalized outreach for Alex Rives"

**Subject**: Closing the loop on ESM3 validation

<blockquote style="border-left: 4px solid #00d4ff; background: #16213e; padding: 15px; color: #eaeaea;">
Congratulations on the CZI announcement - excited to see ESM3's capabilities expand through Biohub.
<br><br>
I've been thinking about a bottleneck you're likely facing: <strong>ESM3 generates novel proteins in seconds, but traditional structural validation takes weeks.</strong>
<br><br>
The Rigaku XtaLAB Synergy-S could change that equation...
</blockquote>

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

<table style="width: 100%;">
  <tr>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Feature</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Purpose</th>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Battlecards</strong></td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Why Rigaku beats synchrotron/CRO</td>
  </tr>
  <tr>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Objection Handlers</strong></td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Pre-built responses to pushback</td>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Meeting Prep</strong></td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">What to say, what to avoid</td>
  </tr>
  <tr>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Deal Probability</strong></td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">AI-scored likelihood with reasoning</td>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>Campaign Sequences</strong></td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">6-week multi-touch plan</td>
  </tr>
  <tr>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;"><strong>LinkedIn Content</strong></td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Social selling messages</td>
  </tr>
</table>

---

# Technical Implementation
## How It Works

<div style="background: #1a2332; padding: 20px; border-radius: 8px; font-family: monospace;">
<pre style="color: #00d4ff; margin: 0;">
https://doi.bio/resources/
├── leads/alex-rives.md
├── products/rigaku-xray-systems.md
└── outreach/alex-rives-smykm.md
</pre>
</div>

- **FastAPI backend** serves resources
- **OpenAPI spec** for watsonx skill import
- **Markdown files** for easy updates

---

# ROI Impact
## The Numbers

<table style="width: 100%;">
  <tr>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Metric</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">Manual</th>
    <th style="background: #0f1527; color: #00d4ff; padding: 10px; border: 1px solid #2a3f5f;">AI-Assisted</th>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Research time</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">3 hours</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">5 minutes</td>
  </tr>
  <tr>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Personalization</td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Surface</td>
    <td style="background: #16213e; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Deep</td>
  </tr>
  <tr>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">Response rate</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">2%</td>
    <td style="background: #1a2332; color: #eaeaea; padding: 10px; border: 1px solid #2a3f5f;">15%+</td>
  </tr>
</table>

**Result**: 10x more leads, 7x better conversion

---

<!-- .slide: data-background="#0f0f23" -->
# Thank You
## TechBio Lead Gen & SMYKM

**Turn public research into personalized sales**

### Demo
- Lead: Alex Rives (ESM3, $142M)
- Product: Rigaku XtaLAB Synergy-S
- Result: Personalized email that converts

**GitHub**: github.com/sness23/lablab-orchestrate
`;