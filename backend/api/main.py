from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

app = FastAPI(title="Skill Converter API", version="0.1.0")

# CORS
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Anthropic client
claude_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


class ConversionRequest(BaseModel):
    source_content: str
    source_platform: str  # claude, chatgpt, gemini
    target_platform: str
    user_email: Optional[str] = None


class ConversionResponse(BaseModel):
    converted_content: str
    conversion_notes: list[str]
    warnings: list[str]
    incompatible_features: list[str]
    confidence_score: float


@app.get("/")
async def root():
    return {"message": "Skill Converter API", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/convert", response_model=ConversionResponse)
async def convert_skill(request: ConversionRequest):
    """Convert skill between platforms"""

    # Validate platforms
    valid_platforms = ["claude", "chatgpt", "gemini"]
    if request.source_platform not in valid_platforms:
        raise HTTPException(status_code=400, detail=f"Invalid source platform: {request.source_platform}")
    if request.target_platform not in valid_platforms:
        raise HTTPException(status_code=400, detail=f"Invalid target platform: {request.target_platform}")

    # Build conversion prompt
    conversion_prompt = f"""You are an expert at converting AI skills between platforms.

**Task**: Convert this {request.source_platform} skill to {request.target_platform} format.

**Source Skill**:
{request.source_content}

**Target Platform**: {request.target_platform}

**Instructions**:
1. Preserve core functionality
2. Adapt format to target platform conventions
3. Note incompatible features
4. Suggest optimizations

**Output Format** (JSON):
{{
  "converted_content": "Full converted skill text here",
  "conversion_notes": ["Note 1", "Note 2"],
  "warnings": ["Warning if any"],
  "incompatible_features": ["Feature X cannot convert because Y"],
  "confidence_score": 0.85
}}

Respond ONLY with valid JSON, no markdown code blocks.
"""

    try:
        # Call Claude API
        message = claude_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[{
                "role": "user",
                "content": conversion_prompt
            }]
        )

        # Parse response
        import json
        response_text = message.content[0].text

        # Remove markdown code blocks if present
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0].strip()

        result = json.loads(response_text)

        return ConversionResponse(**result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion failed: {str(e)}")


@app.post("/upload-convert")
async def upload_and_convert(
    file: UploadFile = File(...),
    source_platform: str = Form(...),
    target_platform: str = Form(...),
    user_email: Optional[str] = Form(None)
):
    """Upload file and convert"""

    # Read file content
    content = await file.read()
    source_content = content.decode('utf-8')

    # Use existing convert endpoint
    request = ConversionRequest(
        source_content=source_content,
        source_platform=source_platform,
        target_platform=target_platform,
        user_email=user_email
    )

    return await convert_skill(request)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
