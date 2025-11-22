# Video Demo Script (3-5 minutes)

## Opening (30 seconds)

**[Screen: Title slide]**

"TechBio researchers publish everything - papers, funding announcements, equipment they use. This is public intelligence that sales teams spend hours mining manually.

We built an AI agent orchestrator that turns this public research into personalized, high-converting sales outreach - in minutes instead of hours."

---

## The Problem (30 seconds)

**[Screen: Problem slide]**

"Here's the problem: A sales rep researching a single lead spends 2-3 hours reading papers, understanding their work, and crafting a personalized email.

The result? Generic outreach that gets ignored. Or personalized outreach that doesn't scale.

What if AI could do that research automatically - and generate emails that show you truly understand their work?"

---

## The Solution (30 seconds)

**[Screen: Architecture diagram]**

"We built four AI agents that work together in watsonx Orchestrate:

1. Lead Discovery - finds researchers by domain
2. Profile Builder - extracts equipment needs and pain points
3. Product Matcher - recommends relevant products
4. SMYKM Generator - creates personalized outreach

Let me show you how it works."

---

## Demo Part 1: Find Leads (45 seconds)

**[Screen: watsonx Orchestrate chat]**

**Type**: "Find leads in AI protein design"

"I'm asking watsonx to find leads in AI protein design.

**[Show results]**

It found three leads, ranked by opportunity score:
- Alex Rives from EvolutionaryScale - score 95
- David Baker from UW - score 88
- Demis Hassabis from DeepMind - score 82

Alex Rives is our top lead - he built ESM3, raised $142 million, and just joined CZI. Let's learn more about him."

---

## Demo Part 2: Build Profile (45 seconds)

**[Screen: watsonx Orchestrate chat]**

**Type**: "What equipment does Alex Rives need?"

"Now I'm asking for his equipment needs.

**[Show results]**

The system analyzed his papers and found his core pain point: ESM3 generates novel proteins in seconds, but structural validation takes weeks.

That's a 10,000x speed mismatch. He needs high-throughput crystallography to close that gap."

---

## Demo Part 3: Match Products (30 seconds)

**[Screen: watsonx Orchestrate chat]**

**Type**: "Match Rigaku products for Alex Rives"

"Let's match products to his needs.

**[Show results]**

It recommends the Rigaku XtaLAB Synergy-S as the primary product - high-throughput protein crystallography that can validate structures in hours instead of days.

XtalCheck-S as a secondary product for screening 96-well plates."

---

## Demo Part 4: Generate Outreach (45 seconds)

**[Screen: watsonx Orchestrate chat]**

**Type**: "Generate personalized outreach for Alex Rives"

"Now the magic - generating a Show Me You Know Me email.

**[Show email]**

Look at this personalization:
- References his CZI announcement
- Mentions the '500 million years of evolution' paper
- Directly addresses his validation bottleneck
- Specific: '58% sequence identity' from his paper

This isn't a template. This shows we understand his specific work and pain points."

---

## The Value (30 seconds)

**[Screen: ROI slide]**

"Let's talk numbers:

Before: 3 hours per lead, 10 leads per week, 2% response rate
After: 5 minutes per lead, 100+ leads per week, 15% response rate

That's 10x more leads with 7x better conversion.

For TechBio sales teams, this is a game-changer."

---

## Technical Architecture (30 seconds)

**[Screen: Tech stack slide]**

"Under the hood:
- watsonx Orchestrate chains the four agents
- FastAPI backend serves our knowledge resources
- OpenAPI spec defines the skill interfaces
- All resources are markdown files - easy to update

The system is extensible - add new leads, new products, new vendors."

---

## Closing (30 seconds)

**[Screen: Final slide]**

"TechBio Lead Gen turns public research into personalized sales intelligence.

Every email demonstrates you understand their work. Every pitch addresses their specific pain point.

That's Show Me You Know Me - and that's what converts in TechBio sales.

Thank you."

---

## Recording Tips

1. **Screen recording**: Use OBS or Loom
2. **Resolution**: 1920x1080
3. **Audio**: Use a decent microphone, quiet room
4. **Pacing**: Pause briefly between sections
5. **Practice**: Run through once before recording
6. **Length**: Target 3-4 minutes (judges appreciate brevity)

## Backup Plan

If watsonx demo fails:
- Show the markdown files directly
- Walk through the API responses in browser
- Emphasize the architecture and value prop
