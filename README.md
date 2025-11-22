# TechBio Lead Gen & SMYKM Agent Orchestrator

**IBM watsonx Orchestrate Hackathon Project**

## Overview

An AI agent orchestration system for TechBio sales that:
1. **Discovers leads** by mining academic publications and research
2. **Builds profiles** with equipment needs and pain points
3. **Matches products** from vendor catalogs
4. **Generates personalized outreach** using "Show Me You Know Me" (SMYKM) methodology

## The Problem

TechBio companies publish extensively - papers, preprints, press releases, funding announcements. This publicly available information reveals:
- What equipment they use
- What methodologies they employ
- Where they have bottlenecks
- What they might need next

**We turn this public intelligence into personalized, high-converting sales outreach.**

## Demo: Alex Rives & Rigaku

Our demo showcases the complete pipeline:

| Stage | Input | Output |
|-------|-------|--------|
| Lead Discovery | "AI protein design" | Alex Rives (EvolutionaryScale/CZI) |
| Profile Building | Publications + News | Equipment needs, $142M funding, validation bottleneck |
| Product Matching | Rigaku catalog | XtaLAB Synergy-S + XtalCheck-S |
| SMYKM Outreach | Profile + Products | Personalized email referencing ESM3, CZI |

## Resources

### Lead Profiles
- [`resources/leads/alex-rives.md`](resources/leads/alex-rives.md) - Complete lead profile

### Product Catalogs
- [`resources/products/rigaku-xray-systems.md`](resources/products/rigaku-xray-systems.md) - X-ray crystallography systems

### Personalized Outreach
- [`resources/outreach/alex-rives-smykm.md`](resources/outreach/alex-rives-smykm.md) - SMYKM email and strategy

### Architecture
- [`resources/orchestrator/agent-flow.md`](resources/orchestrator/agent-flow.md) - Agent design and flow

## Agent Architecture

```
┌─────────────────────────────────────────────┐
│          watsonx Orchestrate                │
└──────┬──────────┬──────────┬───────────────┘
       │          │          │
   ┌───▼───┐  ┌───▼───┐  ┌───▼───┐  ┌───────┐
   │ Lead  │  │Profile│  │Product│  │ SMYKM │
   │Discov.│→ │Builder│→ │ Match │→ │Outreach│
   └───────┘  └───────┘  └───────┘  └───────┘
```

## Key Value Propositions

### For Sales Teams
- **10x faster lead research** - AI does the paper mining
- **Personalized at scale** - Every email references their specific work
- **Higher conversion** - Demonstrate you understand their needs

### For This Demo
- **Alex Rives' pain point**: AI generates proteins in seconds, validation takes weeks
- **Our solution**: Rigaku XtaLAB Synergy-S closes that gap
- **The hook**: "Close the validation loop at AI speed"

## External Resources

Host these at doi.bio for watsonx to access:
- `https://doi.bio/resources/leads/alex-rives.md`
- `https://doi.bio/resources/products/rigaku-xray-systems.md`
- `https://doi.bio/resources/outreach/alex-rives-smykm.md`

## watsonx Orchestrate Skills

| Skill | Purpose |
|-------|---------|
| `techbio-lead-search` | Find leads by research domain |
| `techbio-profile-enrich` | Build detailed lead profiles |
| `techbio-product-match` | Match products to needs |
| `techbio-smykm-generate` | Generate personalized outreach |

## Links

- **Hackathon**: https://lablab.ai/event/agentic-ai-hackathon-ibm-watsonx-orchestrate
- **watsonx Orchestrate**: https://eu-gb.watson-orchestrate.cloud.ibm.com/chat

## Future Roadmap

- [ ] Automated paper monitoring with alerts
- [ ] CRM integration (Salesforce/HubSpot)
- [ ] Multi-vendor product catalogs
- [ ] Competitive intelligence tracking
- [ ] Meeting prep document generation

## Team

Built for the IBM watsonx Orchestrate Agentic AI Hackathon
