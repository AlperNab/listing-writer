#!/usr/bin/env python3
"""
listing-writer — property details + photos → compelling real estate listing copy
Generates: MLS description, headline, social media captions, email subject lines,
open house flyer text, SEO-optimized variants
"""
import anthropic, base64, json, re, sys
from pathlib import Path

SYSTEM = """You are an award-winning real estate copywriter who has sold over $500M in property.

Write compelling listing copy that:
- Opens with the property's strongest selling point, not address
- Uses sensory language (light-filled, sun-drenched, step inside)
- Highlights lifestyle, not just features (entertain, relax, work from home)
- Is truthful — don't invent features not provided
- Varies length for each platform/use

Return ONLY valid JSON — no markdown, no explanation.

{
  "headline": "compelling property headline under 10 words",
  "tagline": "under 15 words — the emotional hook",
  "mls_description": {
    "short": "150-200 word MLS listing description",
    "long": "300-400 word expanded description with full lifestyle narrative"
  },
  "social_media": {
    "instagram": "caption with line breaks, conversational, 150 words max, 5-8 hashtags",
    "facebook": "longer form, community-focused, 200 words, shareable",
    "tiktok_hook": "first 3 seconds of a property tour video script",
    "twitter": "under 280 chars, punchy"
  },
  "email": {
    "subject_lines": ["5 A/B testable subject lines"],
    "preview_text": "under 90 chars for email preview",
    "body_opening": "first 2 paragraphs of listing email"
  },
  "open_house_flyer": {
    "headline": "flyer headline",
    "bullet_features": ["6-8 bullet points for print flyer"],
    "closing_line": "compelling closing call to action"
  },
  "seo": {
    "meta_title": "under 60 chars",
    "meta_description": "under 155 chars",
    "page_h1": "main heading",
    "keyword_rich_description": "200 word SEO-optimized version"
  },
  "neighborhood_angle": "1-2 sentences about the location's appeal",
  "buyer_persona": "who is the ideal buyer for this property"
}"""

def write_listing(
    property_type: str,
    bedrooms: int | None = None,
    bathrooms: float | None = None,
    sqft: int | None = None,
    price: str | None = None,
    location: str | None = None,
    features: list[str] | None = None,
    condition: str = "excellent",
    image_paths: list[str] | None = None,
    extra_notes: str = ""
) -> dict:
    client = anthropic.Anthropic()

    # Build context
    specs = [f"Type: {property_type}"]
    if bedrooms: specs.append(f"Bedrooms: {bedrooms}")
    if bathrooms: specs.append(f"Bathrooms: {bathrooms}")
    if sqft: specs.append(f"Size: {sqft:,} sq ft")
    if price: specs.append(f"Price: {price}")
    if location: specs.append(f"Location: {location}")
    if condition: specs.append(f"Condition: {condition}")
    if features: specs.append(f"Features: {', '.join(features)}")
    if extra_notes: specs.append(f"Additional notes: {extra_notes}")

    content_blocks = []
    # Add images if provided
    if image_paths:
        for img_path in image_paths[:4]:  # max 4 images
            p = Path(img_path)
            if p.exists():
                suffix = p.suffix.lower()
                mt = {".jpg":"image/jpeg",".jpeg":"image/jpeg",".png":"image/png",".webp":"image/webp"}.get(suffix,"image/jpeg")
                data = base64.standard_b64encode(p.read_bytes()).decode("ascii")
                content_blocks.append({"type":"image","source":{"type":"base64","media_type":mt,"data":data}})

    content_blocks.append({"type":"text","text":f"Write listing copy for this property:\n\n" + "\n".join(specs)})

    resp = client.messages.create(
        model="claude-sonnet-4-20250514", max_tokens=3000, system=SYSTEM,
        messages=[{"role":"user","content":content_blocks}]
    )
    raw = re.sub(r'^```(?:json)?\s*','',resp.content[0].text.strip(),flags=re.MULTILINE)
    raw = re.sub(r'\s*```$','',raw,flags=re.MULTILINE)
    return json.loads(raw)

def write_from_args(args_dict: dict) -> dict:
    return write_listing(**args_dict)

def print_listing(r: dict):
    print(f"\n{'═'*60}")
    print(f"  {r.get('headline','').upper()}")
    print(f"  {r.get('tagline','')}")
    print(f"{'═'*60}")
    mls = r.get("mls_description", {})
    print(f"\n  MLS DESCRIPTION\n  {mls.get('short','')}")
    social = r.get("social_media", {})
    if social.get("instagram"):
        print(f"\n  INSTAGRAM\n  {social['instagram'][:300]}")
    email = r.get("email", {})
    if email.get("subject_lines"):
        print(f"\n  EMAIL SUBJECTS")
        for s in email["subject_lines"]: print(f"  • {s}")
    flyer = r.get("open_house_flyer", {})
    if flyer.get("bullet_features"):
        print(f"\n  FLYER BULLETS")
        for b in flyer["bullet_features"]: print(f"  • {b}")
    if r.get("buyer_persona"): print(f"\n  Ideal buyer: {r['buyer_persona']}")
    print(f"{'═'*60}\n")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Generate real estate listing copy")
    p.add_argument("type", nargs="?", default="apartment", help="Property type")
    p.add_argument("--beds", type=int); p.add_argument("--baths", type=float)
    p.add_argument("--sqft", type=int); p.add_argument("--price")
    p.add_argument("--location"); p.add_argument("--features", nargs="+")
    p.add_argument("--condition", default="excellent")
    p.add_argument("--images", nargs="+", dest="image_paths")
    p.add_argument("--notes", default="", dest="extra_notes")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    r = write_listing(a.type, a.beds, a.baths, a.sqft, a.price, a.location,
                      a.features, a.condition, a.image_paths, a.extra_notes)
    if a.json: print(json.dumps(r, indent=2, ensure_ascii=False))
    else: print_listing(r)
