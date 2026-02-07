---
name: skill-converter-dev
description: Comprehensive guide for developing a cross-platform AI skill/prompt converter service. Use when the user needs guidance on building, launching, or iterating on the SkillSync/PromptPort product that converts skills between Claude, ChatGPT, and Gemini. Covers business validation, manual service operations, technical implementation, marketing strategies, and product development.
---

# Skill Converter Development Guide

A complete skill for building a cross-platform AI skill/prompt converter service from validation to launch.

## Quick Start

When the user wants to work on the skill converter project, first understand where they are:

1. **Pre-launch (Week 0-1)**: Validating demand → Use "Phase 1: Validation"
2. **Manual service (Week 1-4)**: Running manual conversions → Use "Phase 2: Manual Operations"
3. **Building MVP (Month 2)**: Automating the service → Use "Phase 3: Technical Development"
4. **Scaling (Month 3+)**: Growing the business → Use "Phase 4: Growth & Iteration"

## Core Principles

### Business Model

This is a **service-first, product-second** approach:
- Start with manual conversions to validate demand
- Only automate after proving people will pay
- Focus on solving real pain points, not building features
- Monetize through consulting and services, not just software

### Success Metrics

**Week 1-2 (Validation)**:
- 20+ inquiries about the service
- 5+ paying customers
- $50+ revenue
- Positive feedback (4+/5 rating)

**Month 1 (Manual Service)**:
- 50+ conversions completed
- $500+ revenue
- 4.5+ average satisfaction
- Clear understanding of pain points

**Month 2-3 (MVP)**:
- 100+ total conversions
- $1000+ monthly revenue
- Automated core conversion flow
- 20%+ repeat customer rate

### Critical Constraints

**What NOT to do**:
- ❌ Don't build automation before validation
- ❌ Don't target "everyone" (focus niche first)
- ❌ Don't compete on price (compete on quality)
- ❌ Don't over-engineer (start simple)
- ❌ Don't ignore user feedback (they know best)

**What TO do**:
- ✅ Start with manual service (concierge MVP)
- ✅ Focus on power users & enterprises
- ✅ Charge enough to be sustainable
- ✅ Ship fast, iterate faster
- ✅ Talk to every single user

## Phase 1: Demand Validation (Week 0-1)

### Goal
Confirm people will pay for skill conversion before investing development time.

### Steps

#### Day 1-2: Research & Outreach

**Social Media Validation**:
1. Post on X/Twitter:
   ```
   Quick poll: Do you use Custom GPTs, Claude Skills, or Gemini Gems?
   
   Would you pay $10 to convert them between platforms?
   
   Comment why or why not 👇
   ```

2. Post on Reddit (r/ClaudeAI, r/ChatGPT, r/LocalLLaMA):
   ```
   Title: "Question: Cross-platform AI skill management"
   
   Body: I'm exploring building a service to convert Custom GPTs 
   to Claude Skills (and vice versa).
   
   Questions:
   - Do you use multiple AI platforms?
   - Have you tried migrating prompts/skills manually?
   - Would this save you time?
   - What would you pay for this?
   
   Genuinely curious - thanks for any input!
   ```

**Direct Outreach**:
1. Identify 20 people on X/GitHub who have:
   - Published custom GPTs
   - Shared Claude skills
   - Written about AI prompting

2. Send friendly DMs:
   ```
   Hi! Saw your [skill/GPT name]. Really impressive!
   
   Quick question: Have you ever wanted to use the same 
   prompt/skill across multiple AI platforms?
   
   I'm exploring building a conversion service. 
   Would that be useful to you?
   
   (Just doing research, not selling anything!)
   ```

#### Day 3-4: Analyze & Decide

**Review responses and look for**:
- ✅ **Strong signals**: "Yes, I need this now"
- ✅ **Medium signals**: "Interesting, might use"
- ⚠️ **Weak signals**: "Maybe someday"
- ❌ **Red flags**: "I'd just do it myself"

**Decision criteria**:
- **PROCEED** if: 20+ positive responses, 5+ "need now"
- **MAYBE** if: 10-20 responses, interest but hesitation
- **STOP** if: <10 responses, mostly negative

**If PROCEED**: Continue to Phase 2
**If MAYBE**: Do deeper interviews with interested people
**If STOP**: Pivot idea or abandon (you just saved weeks of work!)

## Phase 2: Manual Service Operations (Week 1-4)

### Goal
Validate willingness to pay and learn conversion requirements through manual service.

### Setup (Day 1)

#### 1. Create Service Description

Draft a clear, simple service offering:

```markdown
# AI Skill Converter - Manual Service

I manually convert AI skills between platforms:
- Claude Skills ↔ ChatGPT Custom GPTs
- Claude Skills ↔ Gemini Gems
- ChatGPT GPTs ↔ Gemini Gems

**Pricing**:
- Simple (<500 words): $10
- Standard (500-2000 words): $25
- Complex (>2000 words + consultation): $50

**Turnaround**: 24 hours
**Guarantee**: 1 free revision + full refund if unsatisfied

**Early customer benefits**:
- 50% lifetime discount on future automated tool
- Priority feature requests
- Acknowledged in product launch

Contact: [email] | [X handle]
```

**Publish this on**:
- Google Doc (public link)
- GitHub Gist
- Simple Carrd.co page ($19/year, optional but recommended)

#### 2. Setup Payment Processing

**Option A: Stripe Payment Links** (Recommended)
1. Create Stripe account
2. Create 3 payment links:
   - $10 - Simple Conversion
   - $25 - Standard Conversion
   - $50 - Premium Conversion + Consultation
3. Save links for easy sharing

**Option B: PayPal**
1. Setup PayPal Business
2. Use PayPal.me/[yourname]
3. Or create invoice templates

#### 3. Prepare Conversion Workflow

Create a standard operating procedure (SOP):

**Email Templates** (see references/email-templates.md)
**Conversion Process** (see references/conversion-process.md)
**Quality Checklist** (see references/quality-checklist.md)

### Daily Operations

#### Morning Routine (30 min)
1. Check emails/DMs for new requests
2. Respond to inquiries within 2 hours
3. Send payment links to confirmed customers

#### Conversion Work (1-3 hours per conversion)
1. Read source skill carefully
2. Use Claude to assist conversion (meta!)
3. Manually review and optimize
4. Test in target platform if possible
5. Create delivery package:
   - Converted skill file
   - Conversion notes (what changed)
   - Feature compatibility report
   - Setup instructions

#### Evening Routine (30 min)
1. Deliver completed conversions
2. Follow up on feedback
3. Log metrics in tracking sheet
4. Plan tomorrow's marketing

### Conversion Quality Standards

**Every conversion must include**:

1. **Converted Skill File**
   - Properly formatted for target platform
   - Core functionality preserved
   - Clean, professional presentation

2. **Conversion Notes**
   ```markdown
   # Conversion Report: [Source] → [Target]
   
   ## Changes Made
   - [Change 1]: Reason
   - [Change 2]: Reason
   
   ## Features Not Converted
   - [Feature 1]: Why it can't convert
   - [Feature 2]: Alternative approach suggested
   
   ## Optimization Recommendations
   - [Suggestion 1]
   - [Suggestion 2]
   
   ## Testing Notes
   - [What was tested]
   - [What to verify]
   ```

3. **Quality Checklist** (internal, not sent to customer)
   - [ ] Format correct for target platform
   - [ ] Core instructions preserved
   - [ ] Examples included where helpful
   - [ ] Platform-specific features noted
   - [ ] Limitations clearly documented
   - [ ] Tested (or test instructions provided)

### Marketing & Customer Acquisition

**Daily Marketing Activities** (1 hour):

**X/Twitter** (2-3 posts/day):
- 1 educational thread
- 1-2 engagement posts
- Active replies to relevant discussions

**Example threads**:
```
🧵 I converted 10 Custom GPTs to Claude Skills this week.

Here's what I learned about cross-platform compatibility:

1/ The biggest mistake people make...
[continue with valuable insights]
[end with subtle CTA]
```

**Reddit** (2-3 posts/week):
- Focus on providing value first
- Share learnings and insights
- Mention service naturally in context

**Discord/Slack** (as appropriate):
- Be helpful in AI communities
- Answer questions about skills/prompts
- Offer conversion service when relevant

### Metrics Tracking

Create a Google Sheet with these columns:

| Date | Customer | Source | Target | Tier | Time | Revenue | Rating | Notes | Testimonial |
|------|----------|--------|--------|------|------|---------|--------|-------|-------------|

**Track daily**:
- Inquiries received
- Conversion rate (inquiry → paid)
- Average time per conversion
- Customer satisfaction scores
- Common pain points
- Revenue

**Review weekly**:
- Total conversions
- Revenue vs. time invested
- Most common source/target pairs
- Most requested features
- Customer feedback themes

### Decision Point (End of Week 4)

**Evaluate against success criteria**:

✅ **SUCCESS - Proceed to automation** if:
- 50+ conversions completed
- $500+ revenue
- 4.5+ average rating
- Clear patterns in what users need
- People asking "when will tool be ready?"

⚠️ **MAYBE - Consider pivot** if:
- 20-49 conversions
- $200-500 revenue
- 4.0-4.4 rating
- Mixed feedback
- Need to adjust positioning

❌ **STOP - Abandon or major pivot** if:
- <20 conversions
- <$200 revenue
- <4.0 rating
- Mostly negative feedback
- Not sustainable to continue

## Phase 3: Technical Development (Month 2)

### Pre-Development

**ONLY START AUTOMATION IF**:
- [ ] Manual service validated (50+ conversions)
- [ ] Profitable unit economics ($5+ profit per conversion)
- [ ] Consistent quality (4.5+ rating)
- [ ] Clear understanding of requirements
- [ ] Users actively requesting automation

**If not all checked**: Keep running manual service and iterate.

### Architecture Planning

#### System Design

**Conversion Engine**:
```
Input: Source skill (Claude/GPT/Gemini format)
       + Source platform identifier
       + Target platform identifier

Process:
1. Parse source skill structure
2. Extract core components (instructions, examples, metadata)
3. Map to target platform format
4. Generate target skill
5. Create conversion report

Output: Converted skill file
        + Conversion notes
        + Compatibility report
```

**Tech Stack Recommendation**:

```
Backend:
- Python (conversion logic)
- FastAPI (API server)
- Claude API (for intelligent conversion)

Frontend:
- Next.js + React
- Tailwind CSS
- Vercel (hosting)

Storage:
- Supabase (PostgreSQL)
- S3 (file storage)

Payment:
- Stripe (payment processing)

Monitoring:
- Sentry (error tracking)
- PostHog (analytics)
```

#### File Structure

```
skill-converter/
├── backend/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── convert.py
│   │   │   ├── auth.py
│   │   │   └── webhooks.py
│   │   └── main.py
│   ├── converters/
│   │   ├── base.py
│   │   ├── claude_to_gpt.py
│   │   ├── gpt_to_claude.py
│   │   ├── claude_to_gemini.py
│   │   ├── gemini_to_claude.py
│   │   ├── gpt_to_gemini.py
│   │   └── gemini_to_gpt.py
│   ├── models/
│   │   ├── skill.py
│   │   └── conversion.py
│   └── utils/
│       ├── parser.py
│       ├── formatter.py
│       └── validator.py
├── frontend/
│   ├── app/
│   │   ├── page.tsx (landing)
│   │   ├── convert/page.tsx
│   │   └── dashboard/page.tsx
│   ├── components/
│   │   ├── FileUpload.tsx
│   │   ├── ConversionForm.tsx
│   │   └── ResultDisplay.tsx
│   └── lib/
│       └── api.ts
└── docs/
    ├── API.md
    └── ARCHITECTURE.md
```

### Core Conversion Logic

**Base Converter Interface**:

See `scripts/base_converter.py` for implementation template.

**Conversion Strategy**:

1. **Use Claude API as conversion engine**:
   - Provide source skill + target platform specs
   - Let Claude intelligently convert
   - Post-process for consistency

2. **Manual validation layer**:
   - Flag conversions for human review
   - Learn from corrections
   - Improve prompts over time

3. **Progressive automation**:
   - Week 1-2: Semi-automated (80% auto, 20% manual)
   - Week 3-4: Mostly automated (95% auto, 5% review)
   - Month 2+: Fully automated with spot checks

### Development Phases

#### Phase 3A: MVP Backend (Week 1-2)

**Build core conversion API**:

Day 1-3: Setup & Infrastructure
- [ ] Initialize FastAPI project
- [ ] Setup Supabase database
- [ ] Configure Claude API
- [ ] Implement authentication

Day 4-7: Conversion Engine
- [ ] Build base converter class
- [ ] Implement Claude↔GPT converter
- [ ] Add conversion validation
- [ ] Create API endpoints

Day 8-10: Testing
- [ ] Test with real examples from manual service
- [ ] Compare output quality to manual conversions
- [ ] Fix edge cases
- [ ] Document API

Day 11-14: Integration
- [ ] Add payment processing
- [ ] Setup email notifications
- [ ] Implement file storage
- [ ] Deploy to production

#### Phase 3B: MVP Frontend (Week 3-4)

**Build user interface**:

Day 1-4: Core Pages
- [ ] Landing page with value prop
- [ ] Conversion form (upload/paste)
- [ ] Payment integration
- [ ] Results page

Day 5-7: User Experience
- [ ] Progress indicators
- [ ] Error handling
- [ ] Download functionality
- [ ] Responsive design

Day 8-10: Dashboard
- [ ] User authentication
- [ ] Conversion history
- [ ] Account management
- [ ] Usage analytics

Day 11-14: Polish & Launch
- [ ] Copy editing
- [ ] Final testing
- [ ] SEO optimization
- [ ] Soft launch to waitlist

### Quality Assurance

**Test Suite Requirements**:

1. **Unit Tests**:
   - Parser functions
   - Formatter functions
   - Validator functions

2. **Integration Tests**:
   - Full conversion flows
   - API endpoints
   - Payment processing

3. **E2E Tests**:
   - User flows
   - Edge cases
   - Error scenarios

**Manual Test Checklist**:
- [ ] Upload skill file → conversion works
- [ ] Paste skill text → conversion works
- [ ] Payment flow → completes successfully
- [ ] Download results → file is correct
- [ ] Email notifications → sent properly
- [ ] Error messages → clear and helpful

### Launch Preparation

**Pre-Launch Checklist**:

**Technical**:
- [ ] All tests passing
- [ ] Production environment configured
- [ ] Monitoring/alerts setup
- [ ] Backup systems in place
- [ ] Rate limiting configured

**Business**:
- [ ] Pricing finalized
- [ ] Terms of Service ready
- [ ] Privacy Policy published
- [ ] Refund policy defined
- [ ] Support email setup

**Marketing**:
- [ ] Launch announcement drafted
- [ ] Product Hunt submission prepared
- [ ] Email to waitlist ready
- [ ] Social media posts scheduled
- [ ] Demo video recorded

## Phase 4: Growth & Iteration (Month 3+)

### Launch Strategy

**Week 1: Soft Launch**
- Email waitlist (from manual service customers)
- Post on X/Twitter
- Share in Discord/Slack communities
- Monitor closely, fix issues fast

**Week 2: Public Launch**
- Product Hunt launch
- Hacker News post
- Reddit announcements
- Press outreach

**Week 3-4: Growth**
- Double down on what works
- A/B test pricing
- Improve conversion rate
- Scale marketing

### Growth Levers

**Acquisition Channels**:

1. **Content Marketing**
   - SEO blog posts
   - Tutorial videos
   - Twitter threads
   - Case studies

2. **Partnerships**
   - AI tool builders (white-label)
   - Consultants (referral program)
   - Educators (affiliate program)

3. **Community**
   - Build in public
   - Active in AI communities
   - Share learnings openly

4. **Product-Led Growth**
   - Free tier (limited conversions)
   - Viral features (share results)
   - Referral incentives

### Monetization Evolution

**Initial Pricing** (Month 1-2):
```
Free: 1 conversion/month
Basic: $9/month - 10 conversions
Pro: $29/month - 50 conversions
Enterprise: Custom pricing
```

**Optimized Pricing** (Month 3+):
```
Adjust based on:
- Actual usage patterns
- Customer feedback
- Competitor pricing
- Willingness to pay

Consider:
- Annual discounts
- Volume discounts
- Team plans
- API access tier
```

### Feature Roadmap

**Must-Have (Launch)**:
- Claude ↔ GPT conversion
- Upload or paste input
- Download results
- Conversion notes

**Should-Have (Month 2-3)**:
- Gemini support
- Batch conversions
- Conversion history
- API access

**Nice-to-Have (Month 4+)**:
- Version control
- Team collaboration
- Custom templates
- Analytics dashboard

**Future (Month 6+)**:
- Skill marketplace
- Auto-sync across platforms
- AI-powered optimization
- White-label solution

### Success Metrics (Monthly)

**Acquisition**:
- Website visits
- Signup conversions
- Traffic sources

**Activation**:
- First conversion completion
- Time to first value
- Onboarding completion

**Retention**:
- Monthly active users
- Churn rate
- Repeat usage

**Revenue**:
- MRR (Monthly Recurring Revenue)
- ARPU (Average Revenue Per User)
- LTV (Lifetime Value)

**Referral**:
- NPS score
- Referral rate
- Testimonials collected

### When to Pivot

**Consider pivoting if** (after 3 months):
- MRR < $500
- Churn > 10%/month
- NPS < 30
- No clear product-market fit

**Pivot options**:
1. **Feature pivot**: Different core feature
2. **Customer pivot**: Different target market
3. **Platform pivot**: Different business model
4. **Complete pivot**: New product entirely

### When to Scale

**Ready to scale if**:
- MRR > $2K consistently
- Churn < 5%/month
- NPS > 50
- Clear growth trajectory
- Positive unit economics

**Scaling strategies**:
1. Hire first employee (customer success)
2. Invest in paid marketing
3. Build sales team (for enterprise)
4. Expand feature set
5. Consider fundraising

## Troubleshooting

### Common Issues

**Issue: Not enough conversion requests**
- Review marketing strategy
- Lower price temporarily
- Increase value (add features)
- Target different customer segment
- Improve messaging/positioning

**Issue: Low conversion quality**
- Review failed conversions
- Improve conversion prompts
- Add more validation
- Increase manual review
- Set better expectations

**Issue: High refund rate**
- Understand why (ask for feedback)
- Improve quality checks
- Better expectation setting
- Add revision process
- Consider if product-market fit exists

**Issue: Can't handle volume**
- Prioritize automation
- Hire contractor for conversions
- Increase prices (reduce demand)
- Add wait times
- Focus on higher-value customers

## Resources & Templates

All supporting materials are in the `references/` directory:

- `conversion-process.md` - Detailed conversion workflows
- `email-templates.md` - Customer communication templates
- `quality-checklist.md` - Quality assurance standards
- `marketing-calendar.md` - Marketing plan template
- `metrics-tracking.md` - Analytics spreadsheet template

Scripts in `scripts/` directory:

- `base_converter.py` - Core conversion logic template
- `test_conversion.py` - Testing framework
- `deploy.sh` - Deployment script

## Next Steps

Based on where you are, here's what to do next:

**If just starting**: 
→ Begin Phase 1: Demand Validation

**If validated demand**: 
→ Launch Phase 2: Manual Service

**If running manual service successfully**: 
→ Start Phase 3: Technical Development

**If MVP launched**: 
→ Focus on Phase 4: Growth & Iteration

Ask Claude for specific guidance on any phase or step!
