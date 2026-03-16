from carousel_generator import generate_carousel

summary = """
Headline: AWS Revenue Skyrockets
Kya hua?
AWS ne recent quarter me strong revenue growth dikhaya hai.
Kyun important hai?
Ye batata hai ki cloud aur AI services ki demand fast grow kar rahi hai.
"""

slides = generate_carousel(summary)

for k, v in slides.items():
    print(f"{k.upper()}: {v}\n")
