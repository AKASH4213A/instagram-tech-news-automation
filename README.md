# AI Tech News Instagram Automation

## Overview

This project is an **AI-powered automation pipeline** that collects trending tech news, summarizes it using a local LLM, and generates Instagram-ready carousel content automatically.
The goal is to reduce manual work in creating social media content and move toward a **fully autonomous AI content publishing system**.

The project uses **Ollama running Phi-3** for local AI inference.

---

## Current Features

* **News Fetching** – Collects latest tech news from multiple sources.
* **Deduplication** – Removes duplicate or similar articles.
* **Article Ranking** – Selects the most relevant news.
* **AI Summarization** – Generates concise summaries using Phi-3.
* **Headline Generation** – Creates engaging titles for posts.
* **Carousel Content Generation** – Converts summaries into structured Instagram slides.
* **Caption Generation** – Produces captions with hooks and hashtags.
* **Canva CSV Export** – Exports carousel text for bulk design in **Canva**.
* **Logging & Quality Checks** – Ensures pipeline reliability.

---

## Current Workflow

News Fetch
↓
Deduplicate Articles
↓
Rank Articles
↓
AI Summarization
↓
Headline Generation
↓
Carousel Slide Generation
↓
Caption Generation
↓
Canva CSV Export
↓
Manual Canva Image Rendering

---

## Upcoming Improvements

* **Automatic Carousel Image Generation** using **Pillow**
* **Cloud Image Hosting** via **Cloudinary**
* **Instagram Auto Posting** using **Instagram Graph API**

---

## Future Goals

* Template-based carousel design engine
* Automatic post scheduling
* Multi-platform posting (LinkedIn, X, Threads)
* Engagement analytics and trend detection

---

## Vision

Build a **fully automated AI system** that can:

1. Discover tech news
2. Summarize it using AI
3. Generate carousel content
4. Create images automatically
5. Publish posts on social media

This transforms the project into a **self-operating AI content engine for tech news pages**.


## Tech Stack

- Python
- RSS feeds
- LLM (local via Ollama)
- Canva Bulk Create
- Logging & validation system

## Status

v1.0 – Content automation pipeline complete.

## Setup

Install Python dependencies:

pip install -r requirements.txt

Install Ollama and pull the model:

ollama pull phi3