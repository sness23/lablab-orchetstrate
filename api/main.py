"""
TechBio Lead Gen & SMYKM API
FastAPI backend for watsonx Orchestrate integration
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI(
    title="TechBio Lead Gen & SMYKM API",
    description="AI-powered lead generation and personalized outreach for TechBio sales",
    version="1.0.0"
)

# Enable CORS for watsonx Orchestrate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models ---

class LeadSummary(BaseModel):
    id: str
    name: str
    title: str
    affiliation: str
    research_focus: str
    opportunity_score: int
    funding: str

class LeadContact(BaseModel):
    twitter: Optional[str] = None
    linkedin: Optional[str] = None
    email: Optional[str] = None

class LeadResearch(BaseModel):
    focus: str
    key_projects: list[str]
    recent_publications: list[str]

class LeadFunding(BaseModel):
    amount: str
    investors: list[str]
    date: str

class LeadProfile(BaseModel):
    id: str
    name: str
    title: str
    affiliation: str
    location: str
    contact: LeadContact
    background: str
    research: LeadResearch
    equipment_needs: list[str]
    pain_points: list[str]
    funding: LeadFunding
    opportunity_score: int
    opportunity_rationale: str

class ProductRecommendation(BaseModel):
    product_name: str
    vendor: str
    category: str
    why_it_fits: str
    key_features: list[str]
    addresses_pain_point: str
    estimated_roi: str
    priority: str

class OutreachRequest(BaseModel):
    lead_id: str
    product: Optional[str] = None
    tone: str = "professional"

class EmailContent(BaseModel):
    subject: str
    body: str

class FollowUpAction(BaseModel):
    week: int
    action: str

class OutreachResponse(BaseModel):
    lead_id: str
    email: EmailContent
    personalization_hooks: list[str]
    talking_points: list[str]
    follow_up_strategy: list[FollowUpAction]

# --- Lead Database ---

LEADS_DB = {
    "alex-rives": {
        "id": "alex-rives",
        "name": "Alex Rives",
        "title": "Head of Science, CZI",
        "affiliation": "Chan Zuckerberg Initiative / EvolutionaryScale",
        "location": "New York / San Francisco",
        "contact": {
            "twitter": "@alexrives",
            "linkedin": "alexrives",
            "email": None
        },
        "background": "Founded and led the Evolutionary Scale Modeling (ESM) project at Meta's fundamental AI research lab. After Meta disbanded the AI protein team in August 2023, founded EvolutionaryScale with former colleagues. Recently joined CZI as Head of Science.",
        "research": {
            "focus": "AI protein generation and structure prediction",
            "key_projects": [
                "ESM3 - generative AI model trained on 2.78B proteins",
                "Novel fluorescent protein generation (500M years of evolution equivalent)",
                "Protein language models"
            ],
            "recent_publications": [
                "ESM3: Simulating 500 million years of evolution with a language model",
                "Evolutionary-scale prediction of atomic-level protein structure with a language model"
            ]
        },
        "equipment_needs": [
            "High-throughput X-ray crystallography",
            "Automated crystal screening (96-well plates)",
            "Fast data collection systems",
            "Cryo-EM for larger complexes"
        ],
        "pain_points": [
            "AI generates proteins in seconds, validation takes weeks",
            "Need to validate thousands of AI-generated structures",
            "Synchrotron beamtime is limited and requires travel",
            "Speed mismatch: 10,000x bottleneck between generation and validation"
        ],
        "funding": {
            "amount": "$142M seed round",
            "investors": ["Nat Friedman", "Daniel Gross", "Lux Capital", "AWS", "NVIDIA"],
            "date": "June 2024"
        },
        "opportunity_score": 95,
        "opportunity_rationale": "Well-funded ($142M+), rapidly scaling operations, core need for structural validation, partnerships with AWS/NVIDIA show willingness to invest in cutting-edge tools."
    },
    "david-baker": {
        "id": "david-baker",
        "name": "David Baker",
        "title": "Professor & Director, Institute for Protein Design",
        "affiliation": "University of Washington",
        "location": "Seattle, WA",
        "contact": {
            "twitter": "@davidbaker_uwipd",
            "linkedin": "david-baker-ipd",
            "email": None
        },
        "background": "Pioneer in computational protein design. Developed Rosetta software suite. 2024 Nobel Prize in Chemistry for computational protein design. Founded multiple biotech companies including Cyrus Biotechnology.",
        "research": {
            "focus": "De novo protein design and structure prediction",
            "key_projects": [
                "RoseTTAFold - protein structure prediction",
                "De novo enzyme design",
                "Designed protein therapeutics and vaccines"
            ],
            "recent_publications": [
                "De novo design of protein structure and function with RFdiffusion",
                "Robust deep learning-based protein sequence design"
            ]
        },
        "equipment_needs": [
            "High-throughput crystallography for designed proteins",
            "Automated screening systems",
            "Cryo-EM for complex structures",
            "Mass spectrometry for protein characterization"
        ],
        "pain_points": [
            "Validating hundreds of designed protein variants",
            "Speed of experimental validation vs computational design",
            "Scaling from academic to commercial applications"
        ],
        "funding": {
            "amount": "$100M+ (various grants and companies)",
            "investors": ["HHMI", "NIH", "DARPA", "Gates Foundation"],
            "date": "Ongoing"
        },
        "opportunity_score": 88,
        "opportunity_rationale": "Nobel laureate with massive influence, ongoing need for validation infrastructure, multiple spin-off companies that could purchase equipment."
    },
    "demis-hassabis": {
        "id": "demis-hassabis",
        "name": "Demis Hassabis",
        "title": "CEO & Co-founder",
        "affiliation": "Google DeepMind",
        "location": "London, UK",
        "contact": {
            "twitter": "@demaborlab",
            "linkedin": "demis-hassabis",
            "email": None
        },
        "background": "Co-founded DeepMind in 2010, acquired by Google in 2014. Led development of AlphaFold which solved the 50-year protein folding problem. 2024 Nobel Prize in Chemistry.",
        "research": {
            "focus": "AI for scientific discovery, protein structure prediction",
            "key_projects": [
                "AlphaFold - protein structure prediction",
                "AlphaFold2 - breakthrough accuracy",
                "AlphaFold3 - protein-ligand complexes"
            ],
            "recent_publications": [
                "Accurate structure prediction of biomolecular interactions with AlphaFold 3",
                "AlphaFold Protein Structure Database"
            ]
        },
        "equipment_needs": [
            "Validation of AlphaFold predictions",
            "High-throughput structural biology",
            "Integration with AI prediction pipelines"
        ],
        "pain_points": [
            "Validating AI predictions at scale",
            "Expanding beyond prediction to design",
            "Drug discovery applications need experimental validation"
        ],
        "funding": {
            "amount": "Google-backed (billions in resources)",
            "investors": ["Alphabet/Google"],
            "date": "Ongoing"
        },
        "opportunity_score": 82,
        "opportunity_rationale": "Massive resources but primarily computational focus. Isomorphic Labs spin-off for drug discovery may have more immediate equipment needs."
    },
    "simon-kohl": {
        "id": "simon-kohl",
        "name": "Simon Kohl",
        "title": "Founder & CEO",
        "affiliation": "Latent Labs",
        "location": "London, UK / San Francisco, CA",
        "contact": {
            "twitter": None,
            "linkedin": "simonkohl",
            "email": None
        },
        "background": "Previously co-lead of DeepMind's protein design team and senior research scientist on AlphaFold2. Founded Latent Labs in 2025 to build AI-powered programmable biology platform.",
        "research": {
            "focus": "AI-powered programmable biology",
            "key_projects": [
                "Generative AI for protein design",
                "Programmable biology platform",
                "Therapeutic protein development"
            ],
            "recent_publications": []
        },
        "equipment_needs": [
            "High-throughput X-ray crystallography",
            "Automated screening systems",
            "Biophysical characterization",
            "Expression systems"
        ],
        "pain_points": [
            "Scaling from computation to experimental validation",
            "Building wet lab infrastructure from scratch",
            "Need rapid iteration between design and validation",
            "Competing with established protein design companies"
        ],
        "funding": {
            "amount": "$50M total ($40M Series A)",
            "investors": ["Radical Ventures", "Sofinnova Partners"],
            "date": "February 2025"
        },
        "opportunity_score": 91,
        "opportunity_rationale": "Fresh $50M funding, actively building infrastructure. DeepMind pedigree means high standards. Early stage = opportunity to become preferred vendor."
    },
    "alex-zhavoronkov": {
        "id": "alex-zhavoronkov",
        "name": "Alex Zhavoronkov",
        "title": "Founder & CEO",
        "affiliation": "Insilico Medicine",
        "location": "Hong Kong / New York",
        "contact": {
            "twitter": "@alzhavoronkov",
            "linkedin": "alex-zhavoronkov",
            "email": None
        },
        "background": "Pioneer in applying generative AI to drug discovery. Founded Insilico Medicine in 2014. First AI-designed drug to enter Phase II trials (2024).",
        "research": {
            "focus": "End-to-end generative AI drug discovery",
            "key_projects": [
                "Chemistry42 - generative chemistry",
                "Biology42 - target discovery",
                "INS018_055 - AI-designed drug in Phase II"
            ],
            "recent_publications": [
                "Generative AI for drug discovery"
            ]
        },
        "equipment_needs": [
            "Structural biology for target validation",
            "High-throughput screening",
            "Protein production systems",
            "Biophysical assays"
        ],
        "pain_points": [
            "Validating AI predictions experimentally",
            "Scaling wet lab operations globally",
            "Multiple therapeutic areas = diverse needs",
            "Speed pressure from clinical timelines"
        ],
        "funding": {
            "amount": "$400M+ total",
            "investors": ["Warburg Pincus", "Qiming Venture Partners"],
            "date": "2022"
        },
        "opportunity_score": 85,
        "opportunity_rationale": "Well-funded, multiple clinical programs need structural validation. Global presence = multiple opportunities."
    },
    "daphne-koller": {
        "id": "daphne-koller",
        "name": "Daphne Koller",
        "title": "Founder & CEO",
        "affiliation": "Insitro",
        "location": "South San Francisco, CA",
        "contact": {
            "twitter": "@daborolab",
            "linkedin": "daphne-koller",
            "email": None
        },
        "background": "Stanford CS professor, MacArthur Genius Fellow, co-founder of Coursera. TIME 100 most influential in AI (2024). Founded Insitro to apply ML to drug discovery.",
        "research": {
            "focus": "ML-driven drug discovery with biological data",
            "key_projects": [
                "Human iPSC-derived cell models",
                "High-content imaging + ML",
                "Metabolic and neurological disease programs"
            ],
            "recent_publications": []
        },
        "equipment_needs": [
            "Structural biology for target validation",
            "High-throughput imaging",
            "Automation systems",
            "Protein characterization"
        ],
        "pain_points": [
            "Translating ML insights to drug candidates",
            "Scaling wet lab to match data generation",
            "Validating computationally-identified targets"
        ],
        "funding": {
            "amount": "$700M+ total",
            "investors": ["a16z", "ARCH Venture Partners", "Foresite Capital"],
            "date": "2021"
        },
        "opportunity_score": 83,
        "opportunity_rationale": "Extremely well-funded ($700M+). Data-first approach needs structural validation. Major pharma partnerships validate approach."
    },
    "chris-gibson": {
        "id": "chris-gibson",
        "name": "Chris Gibson",
        "title": "Co-founder & CEO",
        "affiliation": "Recursion Pharmaceuticals",
        "location": "Salt Lake City, UT",
        "contact": {
            "twitter": "@ChrisGibsonPhD",
            "linkedin": "chris-gibson-recursion",
            "email": None
        },
        "background": "Co-founded Recursion in 2013. PhD in genetics. Built one of largest biological datasets. Led IPO and $688M acquisition of Exscientia in 2024.",
        "research": {
            "focus": "AI-driven drug discovery using cellular imaging",
            "key_projects": [
                "Cellular phenotype imaging at scale",
                "Automated labs + ML",
                "Exscientia integration"
            ],
            "recent_publications": []
        },
        "equipment_needs": [
            "Structural biology for target validation",
            "Automated microscopy",
            "Liquid handling systems",
            "Protein production"
        ],
        "pain_points": [
            "Translating phenotypic hits to molecular targets",
            "Structural validation of AI-identified targets",
            "Integration of Exscientia capabilities"
        ],
        "funding": {
            "amount": "Public company (RXRX), $400M+ cash",
            "investors": ["Public market", "Roche", "Bayer"],
            "date": "IPO 2021"
        },
        "opportunity_score": 80,
        "opportunity_rationale": "Public company with strong cash position. Exscientia acquisition = expanded structural biology needs."
    },
    "gevorg-grigoryan": {
        "id": "gevorg-grigoryan",
        "name": "Gevorg Grigoryan",
        "title": "Co-founder & CEO",
        "affiliation": "Generate:Biomedicines",
        "location": "Cambridge, MA",
        "contact": {
            "twitter": None,
            "linkedin": "gevorg-grigoryan",
            "email": None
        },
        "background": "Former Dartmouth CS professor specializing in computational protein design. Co-founded Generate:Biomedicines to create generative AI platform for protein therapeutics.",
        "research": {
            "focus": "Generative AI for protein drug design",
            "key_projects": [
                "De novo protein therapeutic design",
                "Generative models for antibodies",
                "Bispecifics and novel formats"
            ],
            "recent_publications": []
        },
        "equipment_needs": [
            "High-throughput X-ray crystallography",
            "Cryo-EM for complexes",
            "Biophysical characterization",
            "Automated screening"
        ],
        "pain_points": [
            "Speed of validation vs design",
            "Validating truly novel protein structures",
            "Scaling from hits to leads"
        ],
        "funding": {
            "amount": "$450M+ total",
            "investors": ["Flagship Pioneering", "ARCH Venture Partners"],
            "date": "2022"
        },
        "opportunity_score": 89,
        "opportunity_rationale": "Strong funding ($450M+). Core focus on de novo proteins = high crystallography need. Flagship backing = long-term support."
    },
    "chris-bahl": {
        "id": "chris-bahl",
        "name": "Chris Bahl",
        "title": "Co-founder & CEO",
        "affiliation": "AI Proteins",
        "location": "Boston, MA",
        "contact": {
            "twitter": None,
            "linkedin": "chrisbahl",
            "email": None
        },
        "background": "Former researcher at Dana-Farber and MIT. Expert in de novo protein design. Founded AI Proteins to develop miniprotein therapeutics.",
        "research": {
            "focus": "De novo miniprotein therapeutics",
            "key_projects": [
                "Computationally designed miniproteins",
                "Novel scaffolds for therapeutics",
                "Bristol Myers Squibb partnership"
            ],
            "recent_publications": []
        },
        "equipment_needs": [
            "X-ray crystallography for miniproteins",
            "Biophysical characterization",
            "High-throughput screening",
            "Protein production scale-up"
        ],
        "pain_points": [
            "Validating novel miniprotein folds",
            "Demonstrating target engagement",
            "Speed pressure from BMS partnership",
            "Scaling for clinical development"
        ],
        "funding": {
            "amount": "$41.5M Series A + BMS deal up to $400M",
            "investors": ["BMS partnership"],
            "date": "November 2025"
        },
        "opportunity_score": 92,
        "opportunity_rationale": "Fresh Series A ($41.5M), major pharma partnership (BMS $400M potential). De novo proteins = critical need for structural validation. Early stage = opportunity to be primary vendor."
    }
}

# --- Product Database ---

PRODUCTS_DB = {
    "rigaku": {
        "xtalab-synergy-s": {
            "product_name": "XtaLAB Synergy-S",
            "vendor": "Rigaku",
            "category": "X-ray Crystallography",
            "why_it_fits": "High-throughput protein crystallography for validating AI-generated proteins. Hours instead of days per structure.",
            "key_features": [
                "Kappa goniometer with fast motor speeds",
                "HPC hybrid photon counting detectors (HyPix-6000HE, HyPix-Arc 150°)",
                "Dual-source configuration (Cu for proteins, Mo for small molecules)",
                "PhotonJet-S microfocus X-ray sources",
                "Variable divergence slits for large unit cells"
            ],
            "addresses_pain_point": "Closes the validation speed gap - data collection in hours instead of days",
            "estimated_roi": "10x increase in validation throughput, 500+ structures/year vs 50",
            "priority": "primary"
        },
        "xtalcheck-s": {
            "product_name": "XtalCheck-S",
            "vendor": "Rigaku",
            "category": "Crystal Screening",
            "why_it_fits": "In-situ screening of 96-well crystallization plates to identify best diffraction candidates before full data collection.",
            "key_features": [
                "Goniometer-mountable x,y,z stage",
                "96-well SBS format support",
                "In-situ screening without crystal removal",
                "User-friendly rapid screening interface"
            ],
            "addresses_pain_point": "Screen hundreds of AI-generated protein variants quickly, reduce time wasted on poor crystals",
            "estimated_roi": "50% reduction in failed data collections",
            "priority": "secondary"
        }
    }
}

# --- Outreach Templates ---

OUTREACH_DB = {
    "alex-rives": {
        "email": {
            "subject": "Closing the loop on ESM3 validation",
            "body": """Hi Alex,

Congratulations on the CZI announcement - excited to see ESM3's capabilities expand through Biohub.

I've been thinking about a bottleneck you're likely facing: ESM3 generates novel proteins in seconds, but traditional structural validation takes weeks. That's a 10,000x speed mismatch.

The Rigaku XtaLAB Synergy-S could change that equation. It's what leading structural biology labs use for high-throughput protein crystallography, and the XtalCheck-S add-on lets you screen 96-well plates in-situ.

For novel proteins like your 58%-identity fluorescent protein, on-site capability means:
- Days instead of weeks for validation
- 24/7 availability (no synchrotron scheduling)
- Immediate feedback to improve your models

Would a 15-minute call to discuss your validation infrastructure make sense? I can also arrange a virtual demo.

Best,
[Your Name]"""
        },
        "personalization_hooks": [
            "References CZI/Biohub announcement",
            "Mentions '500M years of evolution' achievement",
            "Cites specific 58% sequence identity paper",
            "Addresses validation bottleneck directly"
        ],
        "talking_points": [
            "ESM3 generates proteins faster than they can be validated",
            "On-site crystallography eliminates synchrotron scheduling",
            "XtalCheck-S enables high-throughput screening of variants",
            "ROI: 10x increase in validation throughput"
        ],
        "follow_up_strategy": [
            {"week": 1, "action": "Send initial email + connect on LinkedIn"},
            {"week": 2, "action": "Share case study of AI company using Rigaku"},
            {"week": 3, "action": "Offer virtual demo with application scientist"}
        ]
    },
    "david-baker": {
        "email": {
            "subject": "Validation infrastructure for IPD's designed proteins",
            "body": """Hi David,

Congratulations on the Nobel Prize - a well-deserved recognition of decades of pioneering work in protein design.

As IPD scales its protein design capabilities with RFdiffusion and other tools, I imagine the experimental validation pipeline becomes increasingly important. Designed proteins need structural confirmation, and throughput matters when you're exploring vast design spaces.

The Rigaku XtaLAB Synergy-S with XtalCheck-S could help IPD validate more designs faster:
- Screen 96-well plates in-situ to find best crystals
- Collect complete datasets in hours
- On-site capability for immediate feedback

Many leading structural biology groups have found this combination dramatically increases their validation throughput. Would it be worth a conversation about IPD's current infrastructure and future needs?

Best,
[Your Name]"""
        },
        "personalization_hooks": [
            "Nobel Prize congratulations",
            "References RFdiffusion specifically",
            "Understands design→validation workflow",
            "Acknowledges scale of IPD operations"
        ],
        "talking_points": [
            "Computational design outpaces experimental validation",
            "High-throughput screening essential for design space exploration",
            "On-site capability enables rapid iteration",
            "IPD spin-offs may have separate equipment needs"
        ],
        "follow_up_strategy": [
            {"week": 1, "action": "Send initial email"},
            {"week": 2, "action": "Share publication featuring Rigaku in protein design"},
            {"week": 3, "action": "Reach out to IPD lab managers directly"}
        ]
    }
}

# --- API Endpoints ---

@app.get("/")
def root():
    return {
        "name": "TechBio Lead Gen & SMYKM API",
        "version": "1.0.0",
        "endpoints": [
            "/leads/search",
            "/leads/{lead_id}",
            "/products/match",
            "/outreach/generate",
            "/battlecard/{lead_id}",
            "/meeting-prep/{lead_id}",
            "/objections/{lead_id}",
            "/deal-probability/{lead_id}",
            "/campaign/{lead_id}",
            "/linkedin/{lead_id}"
        ]
    }

@app.get("/leads/search")
def search_leads(
    domain: str = Query(..., description="Research domain to search"),
    limit: int = Query(10, description="Maximum results to return")
):
    """Search for TechBio leads by research domain"""

    # Simple keyword matching for demo
    domain_lower = domain.lower()
    matches = []

    for lead_id, lead in LEADS_DB.items():
        # Check if domain matches research focus or key projects
        research_text = (
            lead["research"]["focus"].lower() + " " +
            " ".join(lead["research"]["key_projects"]).lower()
        )

        if any(word in research_text for word in domain_lower.split()):
            matches.append(LeadSummary(
                id=lead["id"],
                name=lead["name"],
                title=lead["title"],
                affiliation=lead["affiliation"],
                research_focus=lead["research"]["focus"],
                opportunity_score=lead["opportunity_score"],
                funding=lead["funding"]["amount"]
            ))

    # Sort by opportunity score
    matches.sort(key=lambda x: x.opportunity_score, reverse=True)

    return {
        "domain": domain,
        "total": len(matches[:limit]),
        "leads": matches[:limit]
    }

@app.get("/leads/{lead_id}")
def get_lead_profile(lead_id: str):
    """Get detailed lead profile"""

    if lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{lead_id}' not found")

    lead = LEADS_DB[lead_id]
    return LeadProfile(**lead)

@app.get("/products/match")
def match_products(
    lead_id: str = Query(..., description="Lead ID to match products for"),
    vendor: Optional[str] = Query(None, description="Filter by vendor")
):
    """Match products to lead's needs"""

    if lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{lead_id}' not found")

    recommendations = []

    # For demo, always recommend Rigaku products for crystallography needs
    lead = LEADS_DB[lead_id]

    if any("crystallography" in need.lower() or "x-ray" in need.lower()
           for need in lead["equipment_needs"]):

        if vendor is None or vendor.lower() == "rigaku":
            for product_id, product in PRODUCTS_DB["rigaku"].items():
                recommendations.append(ProductRecommendation(**product))

    return {
        "lead_id": lead_id,
        "recommendations": recommendations
    }

@app.post("/outreach/generate")
def generate_outreach(request: OutreachRequest):
    """Generate SMYKM personalized outreach"""

    if request.lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{request.lead_id}' not found")

    if request.lead_id not in OUTREACH_DB:
        raise HTTPException(status_code=404, detail=f"No outreach template for '{request.lead_id}'")

    outreach = OUTREACH_DB[request.lead_id]

    return OutreachResponse(
        lead_id=request.lead_id,
        email=EmailContent(**outreach["email"]),
        personalization_hooks=outreach["personalization_hooks"],
        talking_points=outreach["talking_points"],
        follow_up_strategy=[FollowUpAction(**f) for f in outreach["follow_up_strategy"]]
    )

# --- Battlecard Endpoint ---

@app.get("/battlecard/{lead_id}")
def get_battlecard(lead_id: str):
    """Get competitive battlecard for a lead"""

    if lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{lead_id}' not found")

    lead = LEADS_DB[lead_id]

    # Generate battlecard based on lead type
    battlecard = {
        "lead_id": lead_id,
        "lead_name": lead["name"],
        "current_setup": {
            "primary": "Synchrotron beamtime or CRO services",
            "challenges": [
                "Limited availability and scheduling delays",
                "Travel required for synchrotron",
                "Slow turnaround from CROs",
                "IP concerns with external partners"
            ]
        },
        "why_rigaku_wins": {
            "vs_synchrotron": [
                {"factor": "Availability", "rigaku": "24/7", "competitor": "Weeks to schedule", "winner": "Rigaku"},
                {"factor": "Travel", "rigaku": "None", "competitor": "Required", "winner": "Rigaku"},
                {"factor": "Cost/structure", "rigaku": "~$50 amortized", "competitor": "$500-2000", "winner": "Rigaku"},
                {"factor": "Iteration speed", "rigaku": "Hours", "competitor": "Days-weeks", "winner": "Rigaku"}
            ],
            "killer_argument": f"Your AI generates proteins in seconds. Traditional validation takes weeks. That's a massive bottleneck. On-site crystallography closes that gap for {lead['name']}."
        },
        "competitor_threats": [
            {
                "name": "Bruker D8 VENTURE",
                "threat_level": "Medium",
                "counter": "Rigaku HyPix-Arc 150° has larger coverage, faster data collection"
            },
            {
                "name": "Cryo-EM (Thermo Fisher)",
                "threat_level": "High for some applications",
                "counter": "Cryo-EM is $5M+, X-ray is $300-600K. Complementary, not replacement."
            }
        ],
        "pricing_guidance": {
            "configuration": "XtaLAB Synergy-S + XtalCheck-S",
            "estimated_total": "$450-580K",
            "roi": "10x increase in validation throughput"
        },
        "win_themes": [
            "Speed: Match your AI's velocity",
            "Control: Your data, your schedule",
            "Scale: Validate thousands, not dozens",
            "Integration: Fits design-test-learn cycle"
        ]
    }

    return battlecard

# --- Meeting Prep Endpoint ---

@app.get("/meeting-prep/{lead_id}")
def get_meeting_prep(lead_id: str):
    """Get meeting preparation briefing for a lead"""

    if lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{lead_id}' not found")

    lead = LEADS_DB[lead_id]

    briefing = {
        "lead_id": lead_id,
        "lead_name": lead["name"],
        "thirty_second_background": f"{lead['name']}, {lead['title']} at {lead['affiliation']}. {lead['background'][:200]}...",
        "recent_news_to_reference": [
            f"Recent funding: {lead['funding']['amount']} ({lead['funding']['date']})",
            f"Key focus: {lead['research']['focus']}",
            f"Notable project: {lead['research']['key_projects'][0] if lead['research']['key_projects'] else 'N/A'}"
        ],
        "smart_questions_to_ask": [
            "How are you currently validating your AI-generated/designed structures?",
            "What's your throughput goal for structure validation?",
            "What's the biggest bottleneck in your design-test-learn cycle?",
            "How much time passes between generating a protein and getting structural validation?",
            "If you could validate 10x more structures, how would that change your research?"
        ],
        "topics_to_avoid": [
            "Previous company departures or layoffs",
            "Direct competitor comparisons (unless they bring it up)",
            "Questioning their AI/computational accuracy",
            "Rushing their decision timeline"
        ],
        "communication_style": {
            "technical_depth": "PhD-level, wants details",
            "pace": "Values efficiency, get to the point",
            "decision_style": "Data-driven, show numbers not just claims"
        },
        "likely_objections": [
            {
                "objection": "We have synchrotron access",
                "response": "Synchrotrons are excellent for challenging cases. The question is throughput - can you validate enough to close the feedback loop? On-site handles volume; synchrotron handles edge cases."
            },
            {
                "objection": "We're focused on computational work",
                "response": "Experimental validation makes computational work credible. Every novel structure you validate strengthens your models and publications."
            },
            {
                "objection": "Capital is tight right now",
                "response": f"With {lead['funding']['amount']} in funding, the question is ROI. On-site capability often pays for itself in year one compared to CRO costs and accelerates your timeline to key milestones."
            }
        ],
        "meeting_objectives": {
            "minimum": [
                "Understand current validation workflow",
                "Identify decision-making process",
                "Get agreement for technical follow-up"
            ],
            "target": [
                "Identify specific pain points",
                "Discuss configuration options",
                "Schedule demo or site visit"
            ],
            "best_case": [
                "Introduction to facilities/procurement team",
                "Discuss timeline for decision",
                "Verbal interest in proposal"
            ]
        },
        "quick_stats": {
            "funding": lead["funding"]["amount"],
            "investors": ", ".join(lead["funding"]["investors"][:3]),
            "research_focus": lead["research"]["focus"],
            "opportunity_score": lead["opportunity_score"]
        }
    }

    return briefing

# --- Objection Handler Endpoint ---

@app.get("/objections/{lead_id}")
def get_objection_handlers(lead_id: str):
    """Get objection handlers specific to a lead"""

    if lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{lead_id}' not found")

    lead = LEADS_DB[lead_id]

    # Common objections with lead-specific responses
    objections = {
        "lead_id": lead_id,
        "lead_name": lead["name"],
        "objections": [
            {
                "category": "Budget",
                "objection": "We don't have budget for equipment right now",
                "response": f"I understand budget cycles. With {lead['funding']['amount']} in funding, this might be the right time to plan infrastructure. Equipment lead times can be 3-6 months, so planning now ensures you're ready when budget opens up. Would it help to see an ROI analysis?",
                "follow_up": "Offer to provide ROI calculator and financing options"
            },
            {
                "category": "Existing Solution",
                "objection": "We already have synchrotron access / use CROs",
                "response": f"Those work well for certain use cases. The question for {lead['affiliation']} is throughput: if your AI generates hundreds of candidates, can current validation keep pace? On-site capability handles volume; synchrotron/CRO handles special cases. Most groups find they're complementary.",
                "follow_up": "Ask about their current validation throughput numbers"
            },
            {
                "category": "Technology Choice",
                "objection": "We're investing in cryo-EM instead",
                "response": "Cryo-EM is excellent for large complexes and difficult-to-crystallize proteins. For the rapid iteration cycles of AI-driven design, X-ray often provides faster turnaround at lower cost. Most cutting-edge groups have both - they serve different purposes. Would it help to discuss how they complement each other?",
                "follow_up": "Offer to connect them with a lab that uses both"
            },
            {
                "category": "Expertise",
                "objection": "We don't have structural biology expertise in-house",
                "response": "That's common for AI-native biotechs, and it's solvable. Rigaku provides comprehensive training, method development, and ongoing application support. We've helped several computational biology companies build successful crystallography operations. Would you like to hear how they did it?",
                "follow_up": "Share case study of AI company building structural biology capability"
            },
            {
                "category": "Timing",
                "objection": "We're too early stage for this",
                "response": f"Actually, now might be the ideal time. You're building infrastructure with {lead['funding']['amount']} - the equipment you choose now becomes your standard. Getting it right from the start avoids switching costs later. We can help you plan for current needs with room to scale.",
                "follow_up": "Discuss phased implementation options"
            },
            {
                "category": "Competition",
                "objection": "We're also talking to [Competitor]",
                "response": "That's smart - important to evaluate options. I'd encourage you to compare: detector technology and coverage, data collection speed for protein crystallography, and application support for AI-generated proteins specifically. We're confident in those comparisons. What criteria matter most to you?",
                "follow_up": "Offer head-to-head technical comparison"
            }
        ]
    }

    return objections

# --- Deal Probability Scorer ---

@app.get("/deal-probability/{lead_id}")
def get_deal_probability(lead_id: str):
    """Get deal probability score with AI reasoning breakdown"""

    if lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{lead_id}' not found")

    lead = LEADS_DB[lead_id]

    # Calculate probability factors
    factors = []
    total_score = 0

    # Funding recency (max 20 points)
    funding_date = lead["funding"]["date"]
    if "2025" in funding_date:
        score = 20
        reasoning = "Very recent funding (2025) - actively building infrastructure"
    elif "2024" in funding_date:
        score = 15
        reasoning = "Recent funding (2024) - likely still in growth mode"
    else:
        score = 8
        reasoning = "Older funding - may need to time with next round"
    factors.append({"factor": "Funding Recency", "score": score, "max": 20, "reasoning": reasoning})
    total_score += score

    # Funding amount (max 20 points)
    funding_amt = lead["funding"]["amount"]
    if "700" in funding_amt or "450" in funding_amt or "400" in funding_amt:
        score = 20
        reasoning = "Large funding ($400M+) - significant budget for infrastructure"
    elif "142" in funding_amt or "100" in funding_amt or "50" in funding_amt or "41" in funding_amt:
        score = 15
        reasoning = "Solid funding - budget available for key equipment"
    else:
        score = 10
        reasoning = "Moderate funding - may need ROI justification"
    factors.append({"factor": "Funding Amount", "score": score, "max": 20, "reasoning": reasoning})
    total_score += score

    # Equipment need match (max 25 points)
    needs = " ".join(lead["equipment_needs"]).lower()
    if "crystallography" in needs or "x-ray" in needs:
        score = 25
        reasoning = "Direct crystallography need identified - strong product fit"
    elif "structural" in needs or "validation" in needs:
        score = 18
        reasoning = "Structural validation need - crystallography is likely solution"
    else:
        score = 10
        reasoning = "Indirect need - requires discovery conversation"
    factors.append({"factor": "Equipment Need Match", "score": score, "max": 25, "reasoning": reasoning})
    total_score += score

    # Pain point severity (max 20 points)
    pains = " ".join(lead["pain_points"]).lower()
    if "bottleneck" in pains or "speed" in pains or "throughput" in pains:
        score = 20
        reasoning = "Acute pain point (speed/throughput) - high urgency to solve"
    elif "scale" in pains or "validation" in pains:
        score = 15
        reasoning = "Scaling challenges - growing need for solution"
    else:
        score = 10
        reasoning = "General challenges - need to uncover specific pain"
    factors.append({"factor": "Pain Point Severity", "score": score, "max": 20, "reasoning": reasoning})
    total_score += score

    # Competition/Incumbent (max 15 points)
    # Estimate based on company stage
    if "2025" in funding_date or "Series A" in funding_amt:
        score = 15
        reasoning = "Early stage - no incumbent equipment, greenfield opportunity"
    elif "Public" in funding_amt or "IPO" in funding_date:
        score = 8
        reasoning = "Established company - likely has existing equipment relationships"
    else:
        score = 12
        reasoning = "Growth stage - may be expanding beyond initial equipment"
    factors.append({"factor": "Competitive Landscape", "score": score, "max": 15, "reasoning": reasoning})
    total_score += score

    # Convert to probability
    probability = total_score  # Out of 100

    # Determine recommendation
    if probability >= 80:
        recommendation = "HIGH PRIORITY - Pursue aggressively"
        next_action = "Request meeting this week"
    elif probability >= 65:
        recommendation = "STRONG OPPORTUNITY - Active pursuit"
        next_action = "Send personalized outreach, follow up in 3 days"
    elif probability >= 50:
        recommendation = "MODERATE OPPORTUNITY - Nurture"
        next_action = "Add to campaign sequence, monitor for trigger events"
    else:
        recommendation = "LONG-TERM - Keep warm"
        next_action = "Quarterly check-in, wait for funding or expansion news"

    return {
        "lead_id": lead_id,
        "lead_name": lead["name"],
        "deal_probability": probability,
        "recommendation": recommendation,
        "next_action": next_action,
        "scoring_breakdown": factors,
        "total_points": total_score,
        "max_points": 100,
        "confidence": "High" if probability > 70 else "Medium" if probability > 50 else "Low"
    }

# --- Multi-Touch Campaign Generator ---

@app.get("/campaign/{lead_id}")
def get_campaign_sequence(lead_id: str):
    """Get 6-week multi-touch campaign sequence for a lead"""

    if lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{lead_id}' not found")

    lead = LEADS_DB[lead_id]

    campaign = {
        "lead_id": lead_id,
        "lead_name": lead["name"],
        "campaign_name": f"{lead['name']} - AI Protein Validation Campaign",
        "duration": "6 weeks",
        "touches": [
            {
                "week": 1,
                "day": "Monday",
                "channel": "Email",
                "action": "Send personalized SMYKM email",
                "content_summary": f"Reference {lead['research']['key_projects'][0] if lead['research']['key_projects'] else 'recent work'}, address validation bottleneck",
                "goal": "Get reply or meeting"
            },
            {
                "week": 1,
                "day": "Wednesday",
                "channel": "LinkedIn",
                "action": "Send connection request",
                "content_summary": f"Personalized note referencing their work at {lead['affiliation']}",
                "goal": "Build relationship"
            },
            {
                "week": 2,
                "day": "Tuesday",
                "channel": "Email",
                "action": "Share relevant content",
                "content_summary": "Case study: How [Similar AI Company] built crystallography capability",
                "goal": "Provide value, stay top of mind"
            },
            {
                "week": 2,
                "day": "Friday",
                "channel": "LinkedIn",
                "action": "Engage with their content",
                "content_summary": "Like/comment on recent post or publication share",
                "goal": "Build visibility"
            },
            {
                "week": 3,
                "day": "Monday",
                "channel": "Email",
                "action": "Invite to webinar/event",
                "content_summary": "Rigaku webinar: 'High-Throughput Validation for AI-Designed Proteins'",
                "goal": "Soft engagement, learn interest level"
            },
            {
                "week": 4,
                "day": "Wednesday",
                "channel": "Email",
                "action": "Share technical paper",
                "content_summary": f"Application note relevant to {lead['research']['focus']}",
                "goal": "Demonstrate expertise"
            },
            {
                "week": 4,
                "day": "Friday",
                "channel": "Phone",
                "action": "Call attempt",
                "content_summary": "Brief voicemail if no answer, reference previous emails",
                "goal": "Direct conversation"
            },
            {
                "week": 5,
                "day": "Tuesday",
                "channel": "Email",
                "action": "Demo offer",
                "content_summary": "Offer virtual demo with application scientist, specific to their use case",
                "goal": "Advance to technical evaluation"
            },
            {
                "week": 6,
                "day": "Monday",
                "channel": "Email",
                "action": "Executive touch",
                "content_summary": "Brief note from sales director, express interest in partnership",
                "goal": "Elevate conversation"
            },
            {
                "week": 6,
                "day": "Thursday",
                "channel": "LinkedIn",
                "action": "Final value-add",
                "content_summary": "Share industry news relevant to their work",
                "goal": "Stay connected for future opportunity"
            }
        ],
        "success_metrics": {
            "email_open_rate_target": "40%+",
            "reply_rate_target": "15%+",
            "meeting_conversion_target": "10%+",
            "linkedin_acceptance_target": "50%+"
        },
        "exit_triggers": [
            "Meeting scheduled - move to opportunity stage",
            "Explicit 'not interested' - move to nurture",
            "Bounced email - verify contact info",
            "No engagement after 6 weeks - pause, retry in 3 months"
        ]
    }

    return campaign

# --- LinkedIn Generator ---

@app.get("/linkedin/{lead_id}")
def get_linkedin_content(lead_id: str):
    """Get LinkedIn connection request and engagement content"""

    if lead_id not in LEADS_DB:
        raise HTTPException(status_code=404, detail=f"Lead '{lead_id}' not found")

    lead = LEADS_DB[lead_id]

    # Get first project for personalization
    key_project = lead["research"]["key_projects"][0] if lead["research"]["key_projects"] else "your recent work"

    linkedin = {
        "lead_id": lead_id,
        "lead_name": lead["name"],
        "connection_request": {
            "note": f"Hi {lead['name'].split()[0]}, I've been following {lead['affiliation']}'s work on {lead['research']['focus']}. {key_project} caught my attention - impressive results. Would love to connect and learn more about your validation workflows. - [Your Name]",
            "character_count": 280,
            "note_about_limit": "LinkedIn connection notes limited to 300 characters"
        },
        "inmails": [
            {
                "type": "Initial Outreach",
                "subject": f"Validation infrastructure for {lead['affiliation']}",
                "body": f"Hi {lead['name'].split()[0]},\n\nCongratulations on the recent progress at {lead['affiliation']} - {key_project} represents a significant advance.\n\nI work with AI-driven protein design companies on structural validation infrastructure. The common challenge I hear: computational design outpaces experimental validation by orders of magnitude.\n\nWould you be open to a brief conversation about how you're approaching this at {lead['affiliation']}? I'd value your perspective, and happy to share what's working for similar groups.\n\nBest,\n[Your Name]"
            },
            {
                "type": "Follow-up (if no response)",
                "subject": f"Quick question about validation at {lead['affiliation']}",
                "body": f"Hi {lead['name'].split()[0]},\n\nFollowing up briefly - I know you're busy scaling {lead['affiliation']}'s capabilities.\n\nOne specific question: are you validating structures primarily through synchrotron beamtime, CROs, or building in-house capability?\n\nHappy to share a case study of how a similar AI protein company approached this decision.\n\nBest,\n[Your Name]"
            }
        ],
        "engagement_content": {
            "post_comment_templates": [
                f"Fascinating approach to {lead['research']['focus']}. The throughput implications for validation are significant - would love to hear more about how you're scaling the experimental side.",
                f"Great to see this progress from {lead['affiliation']}. The structural validation of AI-designed proteins is becoming increasingly critical. Impressive work.",
                f"This is exactly why the field needs better validation infrastructure. Computational design is advancing faster than experimental confirmation. Important work."
            ],
            "share_with_commentary": f"Interesting developments from {lead['affiliation']} on {lead['research']['focus']}. As AI-driven design accelerates, the bottleneck increasingly shifts to experimental validation. Worth following their progress."
        },
        "best_times_to_post": {
            "timezone": "Assume US timezone based on location",
            "optimal_days": ["Tuesday", "Wednesday", "Thursday"],
            "optimal_hours": ["8-9 AM", "12-1 PM", "5-6 PM"],
            "avoid": "Weekends and Monday mornings"
        }
    }

    return linkedin

# --- Health Check ---

@app.get("/health")
def health_check():
    return {"status": "healthy", "leads_count": len(LEADS_DB)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
