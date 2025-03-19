import os
import shutil
from pathlib import Path

from html_gen import generate_page_recursive
from recursive_copy import recursive_copy

root = Path(os.getcwd())
public = root / "public"
static = root / "static"
content = root / "content"
template_path = root / "template.html"


def main():
    try:
        print("Deleting public folder....")
        if public.exists():
            shutil.rmtree(public)

        print("Copying static files....")
        recursive_copy(static, public)

        print("Generating pages...")
        generate_page_recursive(content, template_path, public)

    except (OSError, ImportError) as e:
        print(f"Error building site: {e}")
        raise


if __name__ == "__main__":
    main()
