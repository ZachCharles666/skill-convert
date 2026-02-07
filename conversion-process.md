# Conversion Process Reference

Detailed workflows for converting skills between platforms.

## Core Conversion Workflow

### Step 1: Intake & Analysis

**Receive customer request**:
1. Customer provides source skill (file upload or text paste)
2. Identify source platform (Claude/GPT/Gemini)
3. Identify target platform
4. Classify complexity tier (Simple/Standard/Complex)

**Initial analysis**:
```
Questions to answer:
- What is the core purpose of this skill?
- What are the key features?
- Are there platform-specific elements?
- What might not convert well?
- Estimated time to convert?
```

### Step 2: Core Conversion

**Use Claude API for intelligent conversion**:

```python
def convert_skill(source_content, source_platform, target_platform):
    """
    Main conversion function using Claude API
    """
    
    conversion_prompt = f"""
You are an expert at converting AI skills between platforms.

**Task**: Convert this {source_platform} skill to {target_platform} format.

**Source Skill**:
{source_content}

**Target Platform Requirements**:
{get_platform_requirements(target_platform)}

**Instructions**:
1. Preserve the core functionality and intent
2. Adapt format to target platform conventions
3. Note any features that cannot be directly converted
4. Suggest platform-specific optimizations
5. Maintain professional tone and clarity

**Output Format**:
Provide THREE sections:

## Converted Skill
[Full converted skill in proper target format]

## Conversion Notes
- [Key change 1] and why
- [Key change 2] and why
- [Feature X] could not convert because...

## Optimization Suggestions
- [Suggestion 1] for better performance
- [Suggestion 2] to leverage platform features
"""

    # Call Claude API
    response = call_claude_api(conversion_prompt)
    
    return parse_conversion_response(response)
```

### Step 3: Manual Review

**Quality checks**:

1. **Format Validation**
   - [ ] Proper structure for target platform
   - [ ] All required sections present
   - [ ] Correct syntax and formatting

2. **Content Preservation**
   - [ ] Core instructions intact
   - [ ] Examples included (if present in source)
   - [ ] Tone and style maintained
   - [ ] Technical accuracy preserved

3. **Platform Adaptation**
   - [ ] Uses target platform's conventions
   - [ ] Leverages platform-specific features
   - [ ] Avoids source platform-specific syntax

4. **Completeness**
   - [ ] Nothing critical missing
   - [ ] Clear instructions for user
   - [ ] Limitations clearly noted

### Step 4: Create Delivery Package

**Generate comprehensive output**:

1. **Converted Skill File**
   - Named appropriately for platform
   - Properly formatted
   - Ready to use

2. **Conversion Report**
   ```markdown
   # Conversion Report
   
   **From**: [Source Platform]
   **To**: [Target Platform]
   **Date**: [Date]
   **Complexity**: [Simple/Standard/Complex]
   
   ---
   
   ## Summary
   
   Your [source] skill has been successfully converted to [target] format.
   
   [1-2 sentence overview of what was done]
   
   ---
   
   ## What Changed
   
   ### Major Changes
   - **[Change 1]**: [Explanation and rationale]
   - **[Change 2]**: [Explanation and rationale]
   
   ### Minor Adjustments
   - [Adjustment 1]
   - [Adjustment 2]
   
   ---
   
   ## Features That Could Not Convert
   
   [If none, say "All features converted successfully"]
   
   - **[Feature 1]**: [Why it can't convert] - [Suggested workaround]
   - **[Feature 2]**: [Why it can't convert] - [Alternative approach]
   
   ---
   
   ## Platform-Specific Optimizations
   
   Your converted skill includes these [target]-specific enhancements:
   
   - [Optimization 1]: [Benefit]
   - [Optimization 2]: [Benefit]
   
   ---
   
   ## Setup Instructions
   
   To use your converted skill:
   
   1. [Step 1]
   2. [Step 2]
   3. [Step 3]
   
   ---
   
   ## Testing Recommendations
   
   Please test these scenarios:
   
   - [ ] [Test scenario 1]
   - [ ] [Test scenario 2]
   - [ ] [Test scenario 3]
   
   ---
   
   ## Need Adjustments?
   
   You have 1 free revision. Just reply with what you'd like changed!
   ```

3. **Quick Start Guide** (platform-specific)
   - How to install/use the converted skill
   - Best practices for that platform
   - Common gotchas to avoid

### Step 5: Delivery & Follow-up

**Delivery email**:
```
Subject: Your [Source]→[Target] Conversion is Ready! 🎉

Hi [Name],

Your skill has been successfully converted!

📎 Attached:
- Converted skill (ready to use)
- Conversion report (what changed)
- Setup guide (how to use it)

⏱️ Turnaround: [X hours]

🎯 Key highlights:
- [Highlight 1]
- [Highlight 2]

Please test it out and let me know:
1. Did it work as expected?
2. Any adjustments needed? (1 free revision)
3. Would you be willing to provide a quick testimonial?

Thanks for being an early customer!

Best,
[Your name]

---

P.S. Remember, as an early customer, you get 50% off when 
we launch the automated version!
```

**Follow-up timeline**:
- Day 1: Delivery
- Day 2: "Did you get a chance to test it?"
- Day 7: "How's it working? We'd love your feedback!"
- Day 30: "Update on automated tool progress..."

## Platform-Specific Conversion Guides

### Claude → ChatGPT

**Key differences**:
1. **Format**:
   - Claude: Markdown-based SKILL.md with YAML frontmatter
   - GPT: Plain text instructions in Configure tab

2. **Structure**:
   - Claude: Can include scripts/, references/, assets/
   - GPT: Instructions + Knowledge files (no executable scripts)

3. **Features**:
   - Claude: MCP, slash commands, context loading
   - GPT: Actions (API calls), DALL-E, web browsing

**Conversion strategy**:
```
1. Extract instructions from SKILL.md body
2. Convert YAML metadata to plain text description
3. Scripts → Note that manual execution needed
4. References → Upload as Knowledge files
5. MCP → Suggest Actions as alternative
6. Reformat for GPT's instruction style
```

**Example**:
```
Claude SKILL.md:
---
name: code-reviewer
description: Reviews code for best practices
---

# Code Review Process
When user submits code:
1. Analyze structure
2. Check best practices
3. Suggest improvements

↓ Converts to ↓

GPT Instructions:
You are a code review expert.

When a user submits code:
1. Analyze the code structure
2. Check against best practices
3. Provide specific improvement suggestions

Focus on:
- Code quality
- Performance
- Maintainability
- Security
```

### ChatGPT → Claude

**Key differences**:
1. **Format**: 
   - GPT: Plain text
   - Claude: Structured Markdown with frontmatter

2. **Knowledge files**:
   - GPT: Uploaded in UI
   - Claude: Referenced in skill structure

**Conversion strategy**:
```
1. Wrap instructions in YAML frontmatter
2. Structure content with clear headers
3. Extract examples into separate sections
4. Knowledge files → references/ directory
5. Actions → Note MCP alternative
6. Add progressive disclosure structure
```

**Example**:
```
GPT Instructions:
You are a marketing expert. When users ask for campaign ideas,
provide 3 options with pros/cons for each.

↓ Converts to ↓

Claude SKILL.md:
---
name: marketing-campaign-generator
description: Generates marketing campaign ideas with analysis. 
Use when user needs campaign concepts, strategies, or marketing plans.
---

# Marketing Campaign Generator

## Core Process

When user requests campaign ideas:

1. Understand their:
   - Target audience
   - Budget range
   - Goals/KPIs
   - Industry context

2. Generate 3 campaign options

3. For each option provide:
   - Core concept
   - Pros
   - Cons
   - Estimated budget
   - Expected outcomes

## Output Format

[Example output structure...]
```

### Claude → Gemini

**Key differences**:
1. **Format**:
   - Claude: Complex Markdown structure
   - Gemini: Simplified text instructions

2. **Context**:
   - Claude: Progressive loading
   - Gemini: Everything loaded upfront

**Conversion strategy**:
```
1. Simplify structure (Gemini prefers simpler format)
2. Combine SKILL.md body into single instruction block
3. References → Summarize or provide as context
4. Remove progressive disclosure patterns
5. Adapt examples for Gemini's style
```

### Gemini → Claude

**Conversion strategy**:
```
1. Add YAML frontmatter structure
2. Break single block into organized sections
3. Add progressive disclosure (what to load when)
4. Consider adding reference files for large content
5. Leverage Claude's advanced features
```

### ChatGPT ↔ Gemini

These conversions are more straightforward as both use simpler formats:
- Mostly direct text transfer
- Adjust tone/style slightly
- Note platform capabilities differences

## Quality Assurance Checklist

Before delivering any conversion:

### Format Compliance
- [ ] Correct structure for target platform
- [ ] Proper syntax (YAML, Markdown, etc.)
- [ ] All required sections present
- [ ] No source platform artifacts

### Content Quality
- [ ] Core functionality preserved
- [ ] Instructions clear and actionable
- [ ] Examples included (if appropriate)
- [ ] Tone consistent with source
- [ ] No errors or typos

### Platform Optimization
- [ ] Uses target platform conventions
- [ ] Leverages platform-specific features
- [ ] Avoids non-compatible features
- [ ] Follows target platform best practices

### Documentation
- [ ] Conversion notes comprehensive
- [ ] Limitations clearly stated
- [ ] Setup instructions clear
- [ ] Testing suggestions provided

### User Experience
- [ ] Ready to use immediately
- [ ] Professional presentation
- [ ] Clear next steps
- [ ] Support offer included

## Common Conversion Challenges

### Challenge 1: Platform-Specific Features

**Problem**: Source skill uses features unique to that platform

**Examples**:
- Claude's MCP servers
- GPT's Actions/API calls
- Gemini's Google Workspace integration

**Solutions**:
1. **Document clearly**: Explain what can't convert and why
2. **Suggest alternatives**: Platform-equivalent features
3. **Workaround guide**: How to achieve similar results
4. **Set expectations**: Some features won't have direct equivalents

### Challenge 2: Format Complexity

**Problem**: Source is very complex or poorly structured

**Solutions**:
1. **Simplify where possible**: Remove unnecessary complexity
2. **Reorganize**: Better structure for target platform
3. **Add comments**: Explain organization
4. **Suggest refactoring**: How to improve original

### Challenge 3: Context Length

**Problem**: Source skill is very long

**Solutions**:
1. **Summarize**: Condense without losing key info
2. **Prioritize**: Focus on most important elements
3. **Split**: Suggest multiple skills if appropriate
4. **Reference**: Use external files/links where possible

### Challenge 4: Ambiguous Intent

**Problem**: Not clear what skill is supposed to do

**Solutions**:
1. **Contact customer**: Ask for clarification
2. **Best guess**: Make reasonable assumptions and document
3. **Multiple options**: Provide 2-3 interpretations
4. **Request examples**: Ask for use cases

## Efficiency Tips

**For manual conversions**:

1. **Use templates**: Standard conversion prompts for each direction
2. **Batch processing**: Do similar conversions together
3. **Keyboard shortcuts**: Speed up common actions
4. **Saved responses**: Email templates for common scenarios
5. **Quality over speed**: Better to take time and do it right

**For automated system**:

1. **Caching**: Save common conversion patterns
2. **Parallel processing**: Handle multiple conversions simultaneously
3. **Smart routing**: Different logic for simple vs. complex
4. **Confidence scoring**: Auto-deliver high confidence, review low
5. **Learning loop**: Improve prompts based on corrections

## Time Estimates

**Per conversion**:
- Simple (<500 words): 20-30 minutes
- Standard (500-2000 words): 45-90 minutes
- Complex (>2000 words): 2-3 hours + consultation

**Weekly capacity** (part-time, 10 hours):
- 15-20 simple conversions
- 8-12 standard conversions
- 3-5 complex conversions

**Monthly capacity** (full-time, 160 hours):
- 240-320 simple conversions
- 130-200 standard conversions
- 50-80 complex conversions

## Pricing Strategy

**Current manual pricing**:
- Simple: $10 (30 min = $20/hour)
- Standard: $25 (60 min = $25/hour)
- Complex: $50 (2.5 hours = $20/hour)

**Target pricing** (once automated):
- Free tier: 1 conversion/month
- Basic: $9/month (10 conversions = $0.90 each)
- Pro: $29/month (50 conversions = $0.58 each)
- Enterprise: Custom (volume discounts)

## Next Steps

After delivering conversion:
1. Wait for customer response (24-48 hours)
2. If no response: Send gentle follow-up
3. If issues: Address quickly (within 4 hours)
4. If satisfied: Request testimonial
5. Add to portfolio (with permission)
6. Track metrics for this conversion
7. Update SOP based on learnings
