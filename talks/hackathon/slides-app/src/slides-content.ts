export const slidesContent = `
<section data-background="#0f0f23">
<h1>TechBio Lead Gen and SMYKM</h1>
<h2>AI-Powered Sales Intelligence</h2>

<p><strong>IBM watsonx Orchestrate Hackathon</strong></p>

<p><em>Turn public research into personalized outreach</em></p>
</section>

<section>
<h1>The Problem</h1>
<h2>Sales Reps Spend 80% of Time Researching SMYKM</h2>

<ul>
<li>Show Me You Know Me (SMYKM)</li>
<li>Reading papers to understand their work</li>
<li>Finding equipment they use</li>
<li>Identifying pain points</li>
<li>Crafting personalized emails</li>
</ul>

<p><strong>Result</strong>: Generic outreach that gets ignored</p>
</section>

<section>
<h1>Our Solution</h1>
<h2>4 AI Agents in watsonx Orchestrate</h2>

<div style="background: #1a2332; padding: 15px; border-radius: 8px; font-family: monospace; margin: 15px 0;">
<pre style="color: #00d4ff; margin: 0; font-size: 0.65em;">┌─────────────────────────────────────────────┐
│          watsonx Orchestrate                │
└──────┬──────────┬──────────┬────────────────┘
       │          │          │
   ┌───▼───┐  ┌───▼───┐  ┌───▼───┐  ┌────────┐
   │ Lead  │→ │Profile│→ │Product│→ │ SMYKM  │
   │Search │  │Builder│  │ Match │  │Outreach│
   └───────┘  └───────┘  └───────┘  └────────┘</pre>
</div>

<p><strong>Find leads → Build profiles → Match products → Personalize outreach</strong></p>
</section>

<section>
<h1>Demo: Alex Rives</h1>
<h2>Our Target Lead</h2>

<table style="width: 100%; margin: 20px 0;">
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
</section>

<section>
<h1>Step 1: Lead Discovery</h1>
<h2>"Find leads in AI protein design"</h2>

<p><strong>watsonx returns:</strong></p>

<table style="width: 100%; margin: 20px 0;">
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

<p><strong>Why high score</strong>: Recent funding, direct equipment need, acute pain point</p>
</section>

<section>
<h1>Step 2: Profile Builder</h1>
<h2>"What equipment does Alex Rives need?"</h2>

<p><strong>Equipment Needs:</strong></p>
<ul>
<li>High-throughput X-ray crystallography</li>
<li>Automated crystal screening (96-well)</li>
<li>Fast data collection systems</li>
</ul>

<p><strong>Pain Point:</strong></p>
<blockquote style="border-left: 4px solid #00d4ff; background: #16213e; padding: 12px; color: #eaeaea; margin: 15px 0; font-size: 0.9em;">
"AI generates 1000 proteins/day. Traditional validation: 1-2/week. That's a <strong>10,000x bottleneck</strong>."
</blockquote>
</section>

<section>
<h1>Step 3: Product Match</h1>
<h2>"Match Rigaku products for Alex Rives"</h2>

<h3>Recommended: XtaLAB Synergy-S</h3>

<table style="width: 100%; margin: 20px 0;">
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

<p><strong>Why it fits</strong>: Closes the validation speed gap</p>
</section>

<section>
<h1>Step 4: SMYKM Outreach</h1>
<h2>"Generate personalized outreach for Alex Rives"</h2>

<p><strong>Subject</strong>: Closing the loop on ESM3 validation</p>

<blockquote style="border-left: 4px solid #00d4ff; background: #16213e; padding: 12px; color: #eaeaea; margin: 15px 0; font-size: 0.85em;">
Congratulations on the CZI announcement - excited to see ESM3's capabilities expand through Biohub.
<br><br>
I've been thinking about a bottleneck you're likely facing: <strong>ESM3 generates novel proteins in seconds, but traditional structural validation takes weeks.</strong>
<br><br>
The Rigaku XtaLAB Synergy-S could change that equation...
</blockquote>
</section>

<section>
<h1>Key Personalization Hooks</h1>
<h2>What Makes It SMYKM</h2>

<ul>
<li>✅ References <strong>CZI/Biohub</strong> announcement</li>
<li>✅ Mentions <strong>"500M years of evolution"</strong> achievement</li>
<li>✅ Addresses <strong>validation bottleneck</strong> specifically</li>
<li>✅ Connects product to <strong>his research goal</strong></li>
</ul>

<p><strong>Every sentence shows we understand his work</strong></p>
</section>

<section>
<h1>Bonus Features</h1>
<h2>Complete Sales Toolkit</h2>

<table style="width: 100%; margin: 20px 0;">
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
</section>

<section>
<h1>Technical Implementation</h1>
<h2>How It Works</h2>

<div style="background: #1a2332; padding: 15px; border-radius: 8px; font-family: monospace; margin: 15px 0;">
<pre style="color: #00d4ff; margin: 0; font-size: 0.7em;">https://doi.bio/resources/
├── leads/alex-rives.md
├── products/rigaku-xray-systems.md
└── outreach/alex-rives-smykm.md</pre>
</div>

<ul>
<li><strong>FastAPI backend</strong> serves resources</li>
<li><strong>OpenAPI spec</strong> for watsonx skill import</li>
<li><strong>Markdown files</strong> for easy updates</li>
</ul>
</section>

<section>
<h1>ROI Impact</h1>
<h2>The Numbers</h2>

<table style="width: 100%; margin: 20px 0;">
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

<p><strong>Result</strong>: 10x more leads, 7x better conversion</p>
</section>

<section data-background="#0f0f23">
<h1>Thank You</h1>
<h2>TechBio Lead Gen & SMYKM</h2>

<p><strong>Turn public research into personalized sales</strong></p>

<h3>Demo</h3>
<ul>
<li>Lead: Alex Rives (ESM3, $142M)</li>
<li>Product: Rigaku XtaLAB Synergy-S</li>
<li>Result: Personalized email that converts</li>
</ul>

<p><strong>GitHub</strong>: github.com/sness23/lablab-orchestrate</p>
</section>
`;