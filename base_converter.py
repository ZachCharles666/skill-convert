#!/usr/bin/env python3
"""
Base Converter Template for Skill Converter Project

This provides the foundation for converting skills between AI platforms.
"""

import json
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from enum import Enum


class Platform(Enum):
    """Supported AI platforms"""
    CLAUDE = "claude"
    CHATGPT = "chatgpt"
    GEMINI = "gemini"


@dataclass
class SkillContent:
    """Represents a skill's content structure"""
    name: str
    description: str
    instructions: str
    examples: List[str] = None
    metadata: Dict = None
    platform: Platform = None
    
    def __post_init__(self):
        if self.examples is None:
            self.examples = []
        if self.metadata is None:
            self.metadata = {}


@dataclass
class ConversionResult:
    """Result of a skill conversion"""
    converted_skill: SkillContent
    conversion_notes: List[str]
    warnings: List[str]
    incompatible_features: List[str]
    optimization_suggestions: List[str]
    confidence_score: float  # 0.0 to 1.0
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "converted_skill": {
                "name": self.converted_skill.name,
                "description": self.converted_skill.description,
                "instructions": self.converted_skill.instructions,
                "examples": self.converted_skill.examples,
                "metadata": self.converted_skill.metadata,
                "platform": self.converted_skill.platform.value
            },
            "conversion_notes": self.conversion_notes,
            "warnings": self.warnings,
            "incompatible_features": self.incompatible_features,
            "optimization_suggestions": self.optimization_suggestions,
            "confidence_score": self.confidence_score
        }


class BaseConverter(ABC):
    """
    Abstract base class for platform converters
    
    Each converter handles conversion from one platform to another.
    """
    
    def __init__(self, source_platform: Platform, target_platform: Platform):
        self.source_platform = source_platform
        self.target_platform = target_platform
        self.conversion_notes = []
        self.warnings = []
        self.incompatible_features = []
        self.optimization_suggestions = []
    
    @abstractmethod
    def parse_source(self, source_content: str) -> SkillContent:
        """
        Parse source skill content into structured format
        
        Args:
            source_content: Raw skill content as string
            
        Returns:
            SkillContent object with parsed data
        """
        pass
    
    @abstractmethod
    def convert_instructions(self, source_skill: SkillContent) -> str:
        """
        Convert instructions to target platform format
        
        Args:
            source_skill: Parsed source skill
            
        Returns:
            Converted instructions string
        """
        pass
    
    @abstractmethod
    def format_output(self, converted_skill: SkillContent) -> str:
        """
        Format converted skill for target platform
        
        Args:
            converted_skill: Converted skill content
            
        Returns:
            Formatted string ready for target platform
        """
        pass
    
    def convert(self, source_content: str) -> ConversionResult:
        """
        Main conversion method - orchestrates the conversion process
        
        Args:
            source_content: Raw source skill content
            
        Returns:
            ConversionResult with converted skill and metadata
        """
        # Reset state
        self.conversion_notes = []
        self.warnings = []
        self.incompatible_features = []
        self.optimization_suggestions = []
        
        # Parse source
        source_skill = self.parse_source(source_content)
        
        # Convert instructions
        converted_instructions = self.convert_instructions(source_skill)
        
        # Create converted skill object
        converted_skill = SkillContent(
            name=source_skill.name,
            description=source_skill.description,
            instructions=converted_instructions,
            examples=source_skill.examples,
            metadata=self._convert_metadata(source_skill.metadata),
            platform=self.target_platform
        )
        
        # Calculate confidence score
        confidence = self._calculate_confidence(source_skill, converted_skill)
        
        # Return comprehensive result
        return ConversionResult(
            converted_skill=converted_skill,
            conversion_notes=self.conversion_notes,
            warnings=self.warnings,
            incompatible_features=self.incompatible_features,
            optimization_suggestions=self.optimization_suggestions,
            confidence_score=confidence
        )
    
    def _convert_metadata(self, source_metadata: Dict) -> Dict:
        """
        Convert metadata between platforms
        
        Override in subclasses for platform-specific metadata handling
        """
        return source_metadata.copy()
    
    def _calculate_confidence(
        self, 
        source_skill: SkillContent, 
        converted_skill: SkillContent
    ) -> float:
        """
        Calculate confidence score for the conversion
        
        Score based on:
        - Complexity of source skill
        - Number of incompatible features
        - Number of warnings
        """
        score = 1.0
        
        # Reduce score for incompatible features
        score -= len(self.incompatible_features) * 0.1
        
        # Reduce score for warnings
        score -= len(self.warnings) * 0.05
        
        # Reduce score for very long/complex skills
        instruction_length = len(source_skill.instructions)
        if instruction_length > 5000:
            score -= 0.1
        if instruction_length > 10000:
            score -= 0.2
        
        return max(0.0, min(1.0, score))
    
    def add_conversion_note(self, note: str):
        """Add a note about the conversion process"""
        self.conversion_notes.append(note)
    
    def add_warning(self, warning: str):
        """Add a warning about the conversion"""
        self.warnings.append(warning)
    
    def add_incompatible_feature(self, feature: str, reason: str):
        """Note a feature that couldn't be converted"""
        self.incompatible_features.append(f"{feature}: {reason}")
    
    def add_optimization(self, suggestion: str):
        """Add an optimization suggestion"""
        self.optimization_suggestions.append(suggestion)


class ClaudeToGPTConverter(BaseConverter):
    """Converts Claude Skills to ChatGPT Custom GPTs"""
    
    def __init__(self):
        super().__init__(Platform.CLAUDE, Platform.CHATGPT)
    
    def parse_source(self, source_content: str) -> SkillContent:
        """Parse Claude SKILL.md format"""
        # Extract YAML frontmatter
        frontmatter_match = re.search(
            r'^---\s*\n(.*?)\n---\s*\n',
            source_content,
            re.DOTALL | re.MULTILINE
        )
        
        if not frontmatter_match:
            self.add_warning("No YAML frontmatter found")
            name = "Unnamed Skill"
            description = "No description provided"
            instructions = source_content
        else:
            frontmatter = frontmatter_match.group(1)
            instructions = source_content[frontmatter_match.end():]
            
            # Parse YAML (simple parsing, could use yaml library)
            name_match = re.search(r'name:\s*(.+)', frontmatter)
            desc_match = re.search(r'description:\s*(.+)', frontmatter)
            
            name = name_match.group(1).strip() if name_match else "Unnamed Skill"
            description = desc_match.group(1).strip() if desc_match else "No description"
        
        # Note Claude-specific features
        if 'scripts/' in source_content:
            self.add_incompatible_feature(
                "Executable scripts",
                "GPT cannot run Python/Bash scripts directly. Manual execution needed."
            )
        
        if '/mcp' in source_content.lower():
            self.add_incompatible_feature(
                "MCP (Model Context Protocol)",
                "GPT uses Actions instead. Consider creating custom Actions."
            )
        
        return SkillContent(
            name=name,
            description=description,
            instructions=instructions,
            platform=Platform.CLAUDE
        )
    
    def convert_instructions(self, source_skill: SkillContent) -> str:
        """Convert Claude-style instructions to GPT format"""
        instructions = source_skill.instructions
        
        # Add role/purpose section if not present
        converted = f"You are {source_skill.name}.\n\n"
        converted += f"Purpose: {source_skill.description}\n\n"
        
        # Remove Claude-specific syntax
        # Remove YAML-style markers
        instructions = re.sub(r'^---.*?---\s*\n', '', instructions, flags=re.DOTALL)
        
        # Convert references to Knowledge files
        instructions = re.sub(
            r'See `([^`]+)` for',
            r'Refer to uploaded knowledge files for',
            instructions
        )
        
        # Simplify progressive disclosure patterns
        instructions = re.sub(
            r'Claude (should|will|can) read',
            r'Reference the knowledge base when',
            instructions
        )
        
        converted += instructions
        
        self.add_conversion_note(
            "Added role and purpose header for GPT format"
        )
        self.add_optimization(
            "Consider uploading reference files as Knowledge in GPT's Configure tab"
        )
        
        return converted
    
    def format_output(self, converted_skill: SkillContent) -> str:
        """Format for GPT's instruction field"""
        output = f"""# {converted_skill.name}

{converted_skill.instructions}

---
Note: This skill was converted from Claude format. 
Some features may require manual adaptation.
"""
        return output


class GPTToClaudeConverter(BaseConverter):
    """Converts ChatGPT Custom GPTs to Claude Skills"""
    
    def __init__(self):
        super().__init__(Platform.CHATGPT, Platform.CLAUDE)
    
    def parse_source(self, source_content: str) -> SkillContent:
        """Parse GPT instructions format"""
        # GPT format is typically plain text
        # Try to extract name and description from content
        
        lines = source_content.strip().split('\n')
        name = "Converted GPT"
        description = "Converted from ChatGPT Custom GPT"
        
        # Look for title patterns
        if lines[0].startswith('#'):
            name = lines[0].lstrip('#').strip()
            instructions = '\n'.join(lines[1:])
        else:
            instructions = source_content
        
        # Try to extract description
        desc_patterns = [
            r'You are (.+?)\.',
            r'Purpose: (.+)',
            r'Description: (.+)'
        ]
        for pattern in desc_patterns:
            match = re.search(pattern, instructions, re.IGNORECASE)
            if match:
                description = match.group(1).strip()
                break
        
        # Note GPT-specific features
        if 'dalle' in source_content.lower() or 'dall-e' in source_content.lower():
            self.add_incompatible_feature(
                "DALL-E image generation",
                "Claude doesn't have DALL-E. Consider alternative image workflows."
            )
        
        if 'action' in source_content.lower():
            self.add_incompatible_feature(
                "GPT Actions",
                "Claude uses MCP for external integrations."
            )
        
        return SkillContent(
            name=name,
            description=description,
            instructions=instructions,
            platform=Platform.CHATGPT
        )
    
    def convert_instructions(self, source_skill: SkillContent) -> str:
        """Convert GPT instructions to Claude format"""
        instructions = source_skill.instructions
        
        # Add structure with Markdown headers
        converted = "# Overview\n\n"
        converted += f"{source_skill.description}\n\n"
        converted += "# Instructions\n\n"
        converted += instructions
        
        self.add_conversion_note(
            "Added Markdown structure for Claude format"
        )
        self.add_optimization(
            "Consider adding progressive disclosure with references/ folder"
        )
        
        return converted
    
    def format_output(self, converted_skill: SkillContent) -> str:
        """Format as Claude SKILL.md"""
        output = f"""---
name: {converted_skill.name.lower().replace(' ', '-')}
description: {converted_skill.description}
---

{converted_skill.instructions}
"""
        return output


# Example usage
if __name__ == "__main__":
    # Example: Convert Claude skill to GPT
    claude_skill = """---
name: code-reviewer
description: Reviews code for best practices and suggests improvements
---

# Code Review Process

When user submits code:
1. Analyze structure
2. Check best practices
3. Suggest improvements

Focus on:
- Code quality
- Performance
- Security
"""
    
    converter = ClaudeToGPTConverter()
    result = converter.convert(claude_skill)
    
    print("Converted Skill:")
    print(converter.format_output(result.converted_skill))
    print("\n" + "="*50 + "\n")
    print(f"Confidence Score: {result.confidence_score}")
    print(f"\nConversion Notes: {result.conversion_notes}")
    print(f"Warnings: {result.warnings}")
    print(f"Incompatible Features: {result.incompatible_features}")
    print(f"Optimizations: {result.optimization_suggestions}")
