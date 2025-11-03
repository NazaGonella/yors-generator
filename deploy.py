import subprocess
import sys
from pathlib import Path
from datetime import datetime


# Replaces %DATE% in Markdown and HTML files with the current post date,
# and %DATEHOME% with the current home date, updating only files that contain these placeholders.
def update_dates():
    home_md_file = Path('./home.md')
    home_html_file = Path('./index.html')
    posts_path = Path('./posts')

    if not posts_path.exists() or not posts_path.is_dir():
        print("Warning: './posts' folder does not exist. No post files will be updated.")
        return

    working_markdown_files = list(Path("./posts").rglob("*.md"))
    paired_files = [(md, md.parent / "index.html") for md in working_markdown_files]

    post_date = datetime.now().strftime("%B %d, %Y")
    home_date = datetime.now().strftime("%d/%m/%Y")
    date_updated : bool = False

    print("### FIXING DATE ###")
    # Set homepage post entry date
    if (home_md_file.exists()):
        home_content = home_md_file.read_text(encoding='utf-8')
        if ("%DATE%" in home_content):
            home_content = home_content.replace("%DATE%", home_date)
            home_md_file.write_text(home_content, encoding="utf-8")
            print("-> ", home_md_file)
            date_updated = True
    if (home_html_file.exists()):
        home_content = home_html_file.read_text(encoding='utf-8')
        if ("%DATE%" in home_content):
            home_content = home_content.replace("%DATE%", home_date)
            home_html_file.write_text(home_content, encoding="utf-8")
            print("-> ", home_html_file)
            date_updated = True
    for md, html in paired_files:
        if md.exists():
            md_content = md.read_text(encoding="utf-8")
            date = post_date
            if ("%DATE%" in md_content):
                md_content = md_content.replace("%DATE%", date)
                md.write_text(md_content, encoding="utf-8")
                print("-> ", md)
                date_updated = True
        if html.exists():
            html_content = html.read_text(encoding="utf-8")
            date = post_date
            if ("%DATE%" in html_content):
                html_content = html_content.replace("%DATE%", date)
                html.write_text(html_content, encoding="utf-8")
                print("-> ", html)
                date_updated = True

    if not date_updated:
        print("No %DATE% found.")
    print("")


def push_to_master():
    working_branch = "working"

    try:
        subprocess.run(["git", "checkout", "master"], check=True)
        subprocess.run(["git", "merge", "working"], check=True)
        subprocess.run(["git", "push", "origin", "master"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        sys.exit(1)

    print("Master branch updated")


def main():
    if "--no-date" not in sys.argv:
        update_dates()
    push_to_master()


if __name__ == "__main__":
    main()