from headline_generator import generate_headline

def generate_carousel(article, summary_data):
    return {
        "slide_1": generate_headline(article, summary_data),
        "slide_2": summary_data.get("kya_hua"),
        "slide_3": summary_data.get("kyun_important")
    }
