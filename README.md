## Requirements

- Python
- Git repository with separate 'working' branch

## How to use

To start writing a new post, execute `python create-post <file_name> <post_title>`. This will create a `posts` directory that will contain the folders of future posts, each one with its corresponding `.md` template file.

To generate

1. Run `python create-post <file_name> <post_title>` to start writing a new post from a template file.
2. Run `python build.py` to generate the website.
3. Commit changes to working branch.
4. Configure branches in `./deploy.sh`, then run the script to merge with the master branch.
