# Demo Script: TechBio Lead Gen & SMYKM

## Setup (Before Demo)

1. Upload resources to doi.bio:
   - `resources/leads/alex-rives.md`
   - `resources/products/rigaku-xray-systems.md`
   - `resources/outreach/alex-rives-smykm.md`

2. Open watsonx Orchestrate: https://eu-gb.watson-orchestrate.cloud.ibm.com/chat

---

## Demo Flow (5 minutes)

### Part 1: The Problem (30 sec)

**Say**: "TechBio researchers publish everything - papers, funding, equipment they use. We can use this public intelligence to generate highly personalized sales outreach."

### Part 2: Lead Discovery (1 min)

**Type in watsonx**:
```
Find leads in AI protein design
```

**Show**: Alex Rives profile appears
- EvolutionaryScale/CZI
- $142M funding
- ESM3 research

**Say**: "We found Alex Rives - he built ESM3, a breakthrough AI for protein design. Well-funded, actively publishing - perfect lead."

### Part 3: Equipment Needs (1 min)

**Type in watsonx**:
```
What equipment does Alex Rives need?
```

**Show**: Equipment needs assessment
- High-throughput crystallography
- Validation bottleneck

**Say**: "His AI generates proteins in seconds, but validating the structures takes weeks. That's a 10,000x speed mismatch. That's his pain point."

### Part 4: Product Match (1 min)

**Type in watsonx**:
```
Match Rigaku products for Alex Rives
```

**Show**: XtaLAB Synergy-S recommendation
- Why it fits his needs
- How it addresses the bottleneck

**Say**: "We matched the Rigaku XtaLAB Synergy-S - it can do in hours what takes days at a synchrotron. Perfect for validating AI-generated proteins at scale."

### Part 5: SMYKM Outreach (1 min)

**Type in watsonx**:
```
Generate personalized outreach for Alex Rives
```

**Show**: Personalized email
- References ESM3
- Mentions CZI announcement
- Addresses specific pain point

**Say**: "This is Show Me You Know Me - we're not sending a generic pitch. We reference his '500 million years of evolution' paper, his CZI move, and his specific validation bottleneck."

### Part 6: Value Prop (30 sec)

**Say**: "This entire flow - from finding the lead to personalized email - takes minutes instead of hours. And every email demonstrates we understand their specific work. That's what drives conversion in TechBio sales."

---

## Key Talking Points

### If Asked About Data Sources
- Academic papers (PubMed, bioRxiv)
- Press releases and funding announcements
- All publicly available information

### If Asked About Accuracy
- AI extracts and synthesizes, human reviews before sending
- References are fact-checkable
- Focus on recent, verifiable information

### If Asked About Scale
- Can profile hundreds of leads in a domain
- Product catalogs can cover multiple vendors
- Outreach templates are customizable

---

## Backup: Manual Demo

If watsonx isn't configured, show the markdown files directly:

1. Open `resources/leads/alex-rives.md` - "Here's the lead profile"
2. Open `resources/products/rigaku-xray-systems.md` - "Here's the product match"
3. Open `resources/outreach/alex-rives-smykm.md` - "Here's the personalized email"

**Say**: "watsonx Orchestrate chains these together automatically, but here's what each agent produces."

---

## Q&A Prep

**Q: How is this different from LinkedIn Sales Navigator?**
A: We go deeper - we read their actual papers and extract equipment needs, not just job changes.

**Q: What about privacy?**
A: We only use publicly available information - papers they chose to publish.

**Q: Can this work for other industries?**
A: Yes - any industry where decision-makers publish (pharma, academic research, tech).

**Q: How long to set up for a new product?**
A: Product catalog markdown takes ~30 minutes. Then AI handles the matching.
