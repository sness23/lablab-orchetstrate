# TechBio Lead Gen & SMYKM Agent Orchestrator

## Overview

This system uses watsonx Orchestrate to coordinate AI agents that:
1. **Find leads** in TechBio by mining academic publications
2. **Build profiles** by aggregating research, equipment, and funding data
3. **Match products** to their specific needs
4. **Generate personalized outreach** using SMYKM methodology

---

## Agent Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  watsonx Orchestrate                     │
│                   (Orchestration Layer)                  │
└─────────────────┬───────────────────────┬───────────────┘
                  │                       │
    ┌─────────────▼─────────────┐   ┌────▼────────────────┐
    │    Lead Discovery Agent    │   │  Product Match Agent │
    │    - Paper mining          │   │  - Catalog search    │
    │    - Author extraction     │   │  - Need matching     │
    │    - Institution lookup    │   │  - Competitor analysis│
    └─────────────┬─────────────┘   └────┬────────────────┘
                  │                       │
    ┌─────────────▼─────────────┐   ┌────▼────────────────┐
    │   Profile Builder Agent    │   │   SMYKM Outreach     │
    │   - Research focus         │   │   - Personalization  │
    │   - Equipment needs        │   │   - Value props      │
    │   - Funding status         │   │   - Email generation │
    └───────────────────────────┘   └─────────────────────┘
```

---

## Agent Descriptions

### 1. Lead Discovery Agent

**Purpose**: Find potential customers in TechBio based on research publications

**Inputs**:
- Target domain (e.g., "protein structure prediction")
- Publication sources (PubMed, bioRxiv, arXiv)
- Time range

**Process**:
1. Search for recent papers in target domain
2. Extract author information and affiliations
3. Identify decision-makers (PIs, lab heads, executives)
4. Score based on funding, publication frequency, and relevance

**Outputs**:
- Lead profile with contact info
- Research summary
- Initial opportunity score

**External Resources**:
- `resources/leads/*.md` - Lead profile templates and data

---

### 2. Profile Builder Agent

**Purpose**: Enrich lead profiles with detailed research and equipment information

**Inputs**:
- Basic lead information from Discovery Agent
- Publication list

**Process**:
1. Analyze papers for equipment/reagent mentions
2. Identify research methodologies
3. Look up funding sources (NIH Reporter, Crunchbase)
4. Find pain points and bottlenecks

**Outputs**:
- Detailed equipment needs assessment
- Research focus areas
- Budget indicators
- Pain points

**External Resources**:
- `resources/leads/*.md` - Enriched lead profiles

---

### 3. Product Match Agent

**Purpose**: Match products from catalog to lead's specific needs

**Inputs**:
- Lead's equipment needs
- Research focus areas
- Budget indicators

**Process**:
1. Search product catalog for relevant items
2. Compare to any known existing equipment
3. Identify upgrade opportunities
4. Calculate potential ROI

**Outputs**:
- Recommended products with rationale
- Competitive positioning
- Pricing guidance

**External Resources**:
- `resources/products/*.md` - Product catalogs and specifications

---

### 4. SMYKM Outreach Agent

**Purpose**: Generate personalized outreach that demonstrates deep understanding

**Inputs**:
- Complete lead profile
- Matched products
- Recent news/publications

**Process**:
1. Extract personalization hooks (recent papers, funding, news)
2. Connect their specific work to product benefits
3. Generate tailored value propositions
4. Create email and follow-up sequence

**Outputs**:
- Personalized email draft
- Talking points
- Follow-up strategy

**External Resources**:
- `resources/outreach/*.md` - Outreach templates and examples

---

## Demo Flow

### Input
```
User: "Find leads in AI protein design and match them with Rigaku products"
```

### Step 1: Lead Discovery
```
Orchestrator → Lead Discovery Agent
Agent: Searching bioRxiv for "protein design" + "AI/ML"...
Agent: Found Alex Rives - EvolutionaryScale/CZI
Agent: High-value lead - $142M funding, active publication
Result: resources/leads/alex-rives.md
```

### Step 2: Profile Building
```
Orchestrator → Profile Builder Agent
Agent: Analyzing ESM3 publication...
Agent: Core need: structural validation of AI-generated proteins
Agent: Pain point: validation speed bottleneck
Result: Updated resources/leads/alex-rives.md
```

### Step 3: Product Matching
```
Orchestrator → Product Match Agent
Agent: Searching Rigaku catalog for crystallography solutions...
Agent: Match: XtaLAB Synergy-S + XtalCheck-S
Agent: Rationale: High-throughput validation for novel proteins
Result: resources/products/rigaku-xray-systems.md
```

### Step 4: SMYKM Outreach
```
Orchestrator → SMYKM Outreach Agent
Agent: Personalizing based on ESM3, CZI announcement, funding...
Agent: Key hook: "500 million years of evolution" achievement
Agent: Value prop: Close the validation loop at AI speed
Result: resources/outreach/alex-rives-smykm.md
```

### Output
```
Complete lead package ready:
- Lead Profile: Alex Rives (Opportunity Score: HIGH)
- Recommended Products: XtaLAB Synergy-S, XtalCheck-S
- Personalized Email: Ready to send
- Follow-up Strategy: 3-week sequence
```

---

## watsonx Orchestrate Integration

### Skills to Create

1. **techbio-lead-search**
   - Input: Domain keyword
   - Output: Lead list with scores

2. **techbio-profile-enrich**
   - Input: Lead name/ID
   - Output: Enriched profile

3. **techbio-product-match**
   - Input: Lead profile
   - Output: Product recommendations

4. **techbio-smykm-generate**
   - Input: Lead + Products
   - Output: Personalized outreach

### Conversation Flow

```
User: Find TechBio leads in protein design

watsonx: I'll search for leads in protein design.
         [Calls techbio-lead-search]

         Found 3 high-value leads:
         1. Alex Rives - EvolutionaryScale (Score: 95)
         2. David Baker - UW IPD (Score: 88)
         3. Demis Hassabis - DeepMind (Score: 82)

         Would you like me to build a full profile for any of these?

User: Yes, Alex Rives

watsonx: [Calls techbio-profile-enrich]
         [Calls techbio-product-match]

         Profile complete. Key findings:
         - Research: AI protein generation (ESM3)
         - Need: High-throughput structure validation
         - Recommended: Rigaku XtaLAB Synergy-S

         Should I generate personalized outreach?

User: Yes

watsonx: [Calls techbio-smykm-generate]

         Here's your personalized email:
         [Shows email draft]

         Key personalization points:
         - References their "500M years of evolution" paper
         - Addresses validation bottleneck specifically
         - Mentions CZI/Biohub expansion
```

---

## External Resource URLs

For watsonx Orchestrate to access these resources, host them at:

- `https://doi.bio/resources/leads/alex-rives.md`
- `https://doi.bio/resources/products/rigaku-xray-systems.md`
- `https://doi.bio/resources/outreach/alex-rives-smykm.md`

Configure watsonx skills to fetch these via HTTP and parse the markdown content.

---

## Future Enhancements

1. **Automated paper monitoring** - Alert when leads publish
2. **CRM integration** - Sync with Salesforce/HubSpot
3. **Multi-product catalogs** - Add more vendors
4. **Competitive intelligence** - Track what equipment leads already have
5. **Meeting prep** - Generate briefing docs before calls
