from typing import Tuple, List

def validate_post(post_data: dict) -> Tuple[bool, List[str]]:
    issues = []

    slides = post_data.get("slides", {})
    caption = post_data.get("caption", "")

    if not slides.get("slide_1"):
        issues.append("Missing slide_1 headline")

    if not slides.get("slide_2") or len(slides["slide_2"].split()) < 6:
        issues.append("slide_2 too short or missing")

    if not slides.get("slide_3") or len(slides["slide_3"].split()) < 12:
        issues.append("slide_3 too short or missing")

    if not caption or len(caption.split()) < 8:
        issues.append("Caption too short or missing")

    return len(issues) == 0, issues
