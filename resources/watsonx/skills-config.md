# watsonx Orchestrate Skills Configuration

## Overview

This guide explains how to configure watsonx Orchestrate to use the TechBio Lead Gen & SMYKM external resources hosted at doi.bio.

---

## External Resource URLs

Configure watsonx to access these markdown resources:

| Resource | URL |
|----------|-----|
| Lead Profiles | `https://doi.bio/resources/leads/` |
| Product Catalogs | `https://doi.bio/resources/products/` |
| Outreach Templates | `https://doi.bio/resources/outreach/` |

---

## Skill 1: TechBio Lead Search

### Purpose
Search for leads based on research domain keywords

### Skill Definition

```json
{
  "name": "techbio-lead-search",
  "description": "Find TechBio leads by research domain. Returns leads with names, affiliations, and opportunity scores.",
  "parameters": {
    "domain": {
      "type": "string",
      "description": "Research domain to search (e.g., 'protein design', 'CRISPR', 'mRNA')",
      "required": true
    }
  },
  "returns": {
    "leads": "Array of lead objects with name, affiliation, score"
  }
}
```

### Instructions for AI

```
When the user asks to find leads in a domain:
1. Fetch the lead profiles from https://doi.bio/resources/leads/
2. Filter by research focus matching the domain
3. Return leads ranked by opportunity score
4. Include: name, title, affiliation, key research, score
```

### Example

**User**: Find leads in AI protein design

**Response**:
Found 1 high-value lead:
1. **Alex Rives** - EvolutionaryScale/CZI (Score: 95)
   - Research: ESM3 protein language model
   - Funding: $142M seed round
   - Key need: Structural validation

---

## Skill 2: TechBio Profile Enrich

### Purpose
Build detailed lead profiles with equipment needs and pain points

### Skill Definition

```json
{
  "name": "techbio-profile-enrich",
  "description": "Enrich a lead profile with detailed research, equipment needs, and pain points.",
  "parameters": {
    "lead_name": {
      "type": "string",
      "description": "Name of the lead to profile",
      "required": true
    }
  },
  "returns": {
    "profile": "Detailed lead profile with equipment needs"
  }
}
```

### Instructions for AI

```
When asked to enrich a lead profile:
1. Fetch the lead's profile from https://doi.bio/resources/leads/{lead-name}.md
2. Extract and summarize:
   - Background and current role
   - Key research projects
   - Equipment needs assessment
   - Pain points and bottlenecks
   - Funding status
   - Opportunity score rationale
3. Present in a structured format
```

### Example

**User**: Build a profile for Alex Rives

**Response**:
## Alex Rives - Full Profile

**Current Role**: Head of Science, CZI (formerly CEO, EvolutionaryScale)

**Key Research**: ESM3 - generative AI for protein design
- Trained on 2.78B proteins
- Generated novel proteins equivalent to 500M years of evolution

**Equipment Needs**:
- High-throughput X-ray crystallography
- Automated crystal screening
- Fast data collection systems

**Pain Point**: AI generates proteins in seconds, but validation takes weeks

**Funding**: $142M seed round (Lux Capital, Nat Friedman, AWS, NVIDIA)

**Opportunity Score**: 95/100 (HIGH)

---

## Skill 3: TechBio Product Match

### Purpose
Match products from catalogs to lead's specific needs

### Skill Definition

```json
{
  "name": "techbio-product-match",
  "description": "Match products from vendor catalogs to a lead's equipment needs.",
  "parameters": {
    "lead_name": {
      "type": "string",
      "description": "Name of the lead",
      "required": true
    },
    "vendor": {
      "type": "string",
      "description": "Vendor to match from (e.g., 'rigaku')",
      "required": false
    }
  },
  "returns": {
    "recommendations": "Product recommendations with rationale"
  }
}
```

### Instructions for AI

```
When asked to match products for a lead:
1. Fetch the lead's profile from https://doi.bio/resources/leads/{lead-name}.md
2. Fetch product catalogs from https://doi.bio/resources/products/
3. Match products to their equipment needs
4. For each recommendation, explain:
   - Why this product fits their needs
   - How it addresses their pain points
   - Key features relevant to their research
5. Include ROI considerations if available
```

### Example

**User**: Match Rigaku products for Alex Rives

**Response**:
## Product Recommendations for Alex Rives

### Primary: XtaLAB Synergy-S
**Why it fits**: High-throughput protein crystallography for validating AI-generated proteins

**Key features for ESM3 validation**:
- Hours instead of days per structure
- HPC detectors for weak diffraction
- Dual-source for proteins and ligands

**Addresses pain point**: Closes the validation speed gap

### Add-on: XtalCheck-S
**Why it fits**: Screen 96-well plates to find best crystals before full data collection

**Key benefit**: Don't waste time on poor diffractors

---

## Skill 4: TechBio SMYKM Generate

### Purpose
Generate personalized outreach using Show Me You Know Me methodology

### Skill Definition

```json
{
  "name": "techbio-smykm-generate",
  "description": "Generate personalized outreach email and strategy for a lead.",
  "parameters": {
    "lead_name": {
      "type": "string",
      "description": "Name of the lead",
      "required": true
    },
    "product": {
      "type": "string",
      "description": "Product to pitch",
      "required": false
    }
  },
  "returns": {
    "outreach": "Personalized email, talking points, follow-up strategy"
  }
}
```

### Instructions for AI

```
When asked to generate SMYKM outreach:
1. Fetch the outreach template from https://doi.bio/resources/outreach/{lead-name}-smykm.md
2. Extract:
   - Personalized email draft
   - Key talking points
   - Follow-up strategy
3. Highlight the personalization hooks:
   - Specific papers/achievements referenced
   - Pain points addressed
   - Connection to their work
```

### Example

**User**: Generate outreach for Alex Rives

**Response**:
## SMYKM Outreach: Alex Rives

### Personalized Email

**Subject**: Closing the loop on ESM3 validation

Hi Alex,

Congratulations on the CZI announcement - excited to see ESM3's capabilities expand through Biohub.

I've been thinking about a bottleneck you're likely facing: ESM3 generates novel proteins in seconds, but traditional structural validation takes weeks. That's a 10,000x speed mismatch.

The Rigaku XtaLAB Synergy-S could change that equation...

[Full email in outreach document]

### Key Personalization Hooks
- References "500M years of evolution" paper
- Mentions CZI/Biohub announcement
- Addresses validation bottleneck specifically

### Follow-up Strategy
- Week 1: Initial email + LinkedIn connect
- Week 2: Share relevant case study
- Week 3: Offer virtual demo

---

## Orchestration Flow

### Complete Workflow

```
User: "Help me reach out to AI protein researchers about Rigaku"

watsonx Orchestrate:
1. [techbio-lead-search] → Find leads in "AI protein design"
2. [techbio-profile-enrich] → Build profile for top lead
3. [techbio-product-match] → Match Rigaku products
4. [techbio-smykm-generate] → Generate personalized outreach

Output: Complete outreach package ready to send
```

### Skill Chaining

Skills can be chained automatically:
- Lead search → Profile enrich → Product match → SMYKM generate

Or called individually for specific tasks.

---

## Setting Up in watsonx Orchestrate

### Step 1: Add External Resources

In watsonx Orchestrate settings, configure access to:
- `https://doi.bio/resources/`

### Step 2: Create Custom Skills

For each skill above:
1. Go to Skills → Create Custom Skill
2. Enter the skill definition JSON
3. Add the AI instructions
4. Test with example inputs

### Step 3: Test the Flow

Try the complete workflow:
```
"Find TechBio leads in protein design and generate outreach for Rigaku products"
```

---

## Troubleshooting

### Resource Not Found
- Ensure markdown files are hosted at correct URLs
- Check CORS settings on doi.bio

### Skill Not Triggering
- Verify skill name matches exactly
- Check parameter requirements

### Poor Personalization
- Ensure lead profile has sufficient detail
- Add more personalization hooks to outreach templates
