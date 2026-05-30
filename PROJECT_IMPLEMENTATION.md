# Listing Writer — Standalone Real GUI Implementation

This folder is now its own runnable project app. It does not depend on the root all-project dashboard at runtime.

## Run

```bash
./run_gui.sh
```

Windows:

```powershell
.\run_gui_windows.ps1
```

Default URL: `http://127.0.0.1:9132`

## What is inside this project folder

- `app/` — FastAPI backend for this project.
- `static/` — elegant browser GUI.
- `plugins/listing-writer.json` — this project’s own feature/customization/input schema.
- `project_config.json` — readable copy of the same project-specific configuration.
- `data/` — local SQLite jobs, uploads, exports.
- `tests/` — verifies this project has a registered real local engine.

## Project-specific scope

- Domain: `E-commerce / Product Content`
- Target user: `Domain operator, business owner, analyst, or team member who needs this workflow executed reliably.`
- Core job: Product details → marketplace listing
- Suite: `E-commerce Growth Suite`

## Deep features applied

- SEO title
- bullet benefits
- feature/spec table
- marketplace compliance
- image prompt ideas
- objection handling
- localization
- A/B variants

## Customization controls

- `execution_mode` — Execution mode (select)
- `marketplace` — marketplace (text)
- `category` — category (text)
- `brand_voice` — brand voice (text)
- `target_customer` — target customer (text)
- `keyword_list` — keyword list (text)
- `forbidden_claims` — forbidden claims (textarea)
- `language` — language (select)
- `tone` — tone (text)
- `output_format` — output format (select)
- `privacy_mode` — privacy mode (select)
- `confidence_threshold` — Confidence threshold (slider)

## Input fields

- `product_details` — Product details (text) required
- `work_brief` — Work brief / source text / URL / instructions (textarea) required

## External data policy

The local deterministic core is real and executable. Live external systems are not simulated. If Shopify, ATS, ERP, OCR/STT, maps, SERP, market data, medical databases, tax/customs databases, or other live systems are required, this project reports the missing connector/API requirement instead of inventing data.

---

## Final UX/UI Layer

This project now uses the **Growth Command Center** pattern.

**UX workflow:** Research → positioning → content/ads → launch queue → measurement

**Domain components:**
- Product/offer canvas
- Margin and pricing cards
- Platform preview board
- Creative variant matrix
- Launch checklist

**Quick actions:**
- Build offer matrix
- Generate channel previews
- Check claims/compliance
- Create launch queue

**No fake-data policy:** external/live actions require real connectors or API keys. Missing connectors are reported instead of simulated.
