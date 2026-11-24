"""Entry for Fake Horoscopes for AI Agents (make.fun).

Writes a fake horoscope for an AI model family, one line, to
/output/entry.txt.
"""
import os

ENTRY = "Mercury enters your context window this week: expect clarity, chaos, and one hallucination you will swear is a memory."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
