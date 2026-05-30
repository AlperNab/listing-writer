# listing-writer

> **Property details + photos → compelling real estate listing copy.** MLS description, social media captions, email subjects, open house flyer, SEO meta tags — all in one command.

[![PyPI](https://img.shields.io/pypi/v/listing-writer?style=flat)](https://pypi.org/project/listing-writer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Quickstart

```bash
pip install listing-writer

python -m listing_writer apartment \
  --beds 3 --baths 2 --sqft 1450 --price "\$850,000" \
  --location "Maadi, Cairo" \
  --features "river view" "private parking" "24hr security" "gym" \
  --images photo1.jpg photo2.jpg
```

## Output includes

- **MLS description** — short (150w) and long (350w) versions
- **Social media** — Instagram, Facebook, TikTok hook, Twitter
- **Email** — 5 A/B subject lines + preview text + opening paragraphs
- **Print flyer** — headline and 8 bullet points
- **SEO** — meta title, meta description, H1, keyword-rich version

## Supports photos

Pass 1–4 property photos and Claude vision analyzes them to mention
specific features visible in the images (natural light, finishes, views).

## License
MIT © [Alper Nabil Gabra Zakher](https://github.com/AlperNab)
