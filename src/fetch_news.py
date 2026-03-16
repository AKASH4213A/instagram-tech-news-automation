import feedparser
from datetime import datetime
from deduplicate_news import deduplicate_news
from ranked_articles import pick_top_7_by_topic, score_article, detect_topic 
from llm_client import call_llm
from ai_summarizer import summarize_article
from carousel_generator import generate_carousel
from save_output import save_post
from caption_generator import generate_caption
from quality_check import validate_post
from logger import logger
from canva_export import export_to_canva_csv



# RSS feed URLs
FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index"
}

def fetch_news():
    all_articles = []

    for source, url in FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:  # latest 10 articles
            article = {
                "source": source,
                "title": entry.get("title", "").strip(),
                "summary": entry.get("summary", "").strip(),
                "link": entry.get("link", ""),
                "published": parse_date(entry)
            }
            all_articles.append(article)

    return all_articles


def parse_date(entry):
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
    return "unknown"



if __name__ == "__main__":

    # ---------------- FETCH ----------------
    news = fetch_news()
    print(f"\nFetched: {len(news)} articles")

    unique_news = deduplicate_news(news)
    print(f"After dedup: {len(unique_news)} articles")

    if not unique_news:
        logger.warning("No articles fetched from feeds.")

    ranked = sorted(unique_news, key=score_article, reverse=True)
    top_7 = pick_top_7_by_topic(ranked)

    # ---------------- INIT ----------------
    saved_count = 0
    skipped_count = 0
    canva_posts = []

    logger.info("Pipeline run started")
    print("\n TOP 7 TECH NEWS:")

    # ---------------- MAIN LOOP ----------------
    for i, n in enumerate(top_7, 1):

        logger.info(f"Processing: {n['title']}")
        print(f"\n{i}. [{score_article(n)} | {detect_topic(n)}] {n['title']} ({n['source']})")

        # ---- ONE LLM CALL ----
        summary = summarize_article(n, llm_call=call_llm)
        print(summary)

        # ---- CAROUSEL ----
        carousel = generate_carousel(n, summary)

        print(f"\n--- Final Generated NEWS for Templates {i} ---")
        print("SLIDE 1:", carousel["slide_1"])
        print("SLIDE 2:", carousel["slide_2"])
        print("SLIDE 3:", carousel["slide_3"])

        # ---- POST DATA ----
        post_data = {
            "source": n["source"],
            "topic": detect_topic(n),
            "original_title": n["title"],

            "slides": {
                "slide_1": carousel["slide_1"],
                "slide_2": carousel["slide_2"],
                "slide_3": carousel["slide_3"]
            },

            "caption": generate_caption(
                {**n, "topic": detect_topic(n)},
                summary
            )
        }

        # ---- VALIDATION ----
        is_valid, issues = validate_post(post_data)

        if not is_valid:
            skipped_count += 1
            logger.warning(f"SKIPPED: {n['title']}")
            for issue in issues:
                logger.warning(f"  - {issue}")
            continue

        # ---- SAVE ----
        path = save_post(post_data, i)
        saved_count += 1
        canva_posts.append(post_data)
        logger.info(f"SAVED: {path}")

    # ---------------- RUN SUMMARY ----------------
    logger.info("Pipeline run completed")
    logger.info("--- RUN SUMMARY ---")
    logger.info(f"Saved posts: {saved_count}")
    logger.info(f"Skipped posts: {skipped_count}")

    if saved_count == 0:
        logger.warning("No valid posts generated in this run")

    # ---------------- CANVA EXPORT ----------------
    if canva_posts:
        csv_path = export_to_canva_csv(canva_posts)
        logger.info(f"Canva CSV generated at: {csv_path}")
    else:
        logger.warning("No posts available for Canva export")




    # print("\n📲 INSTAGRAM READY CONTENT:\n")

    # for i, n in enumerate(top_5, 1):
    #     print(f"--- POST {i} ---")
    #     print(summarize_article(n, llm_call=call_llm))
    #     print("\n")



    # for n in unique_news:
    #     print(f"[{n['source']}] {n['title']}")

