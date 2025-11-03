## Requirements

- Python
- Git repository with separate 'working' branch

## How to use

1. Run `python create-post <file_name> <post_title>` to start writing a new post from a template file.
2. Run `python build.py` to generate the website.
3. Commit changes to working branch.
4. Configure branches in `./deploy.sh`, then run the script to merge with the main branch.
