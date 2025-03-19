import os

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_page(from_path, template_path, to_path):
    print(f"* {from_path} {template_path} -> {to_path}")

    with open(from_path) as f1, open(template_path) as f2:
        md_file = f1.read()
        template = f2.read()

    title = extract_title(md_file)
    html = markdown_to_html_node(md_file).to_html()

    output = template.replace("{{ Content }}", html).replace("{{ Title }}", title)

    to_dir_path = os.path.dirname(to_path)

    if to_dir_path != "":
        os.makedirs(os.path.dirname(to_path), exist_ok=True)

    with open(to_path, "w") as f3:
        f3.write(output)


def generate_page_recursive(from_path_content, template_path, to_path_content):
    for file in os.listdir(from_path_content):
        from_dir = os.path.join(from_path_content, file)
        to_dir = os.path.join(to_path_content, file)
        extension = os.path.splitext(from_dir)[-1].lower()

        if os.path.isfile(from_dir):
            if extension == ".md":
                to_dir = os.path.splitext(to_dir)[0] + ".html"
                generate_page(from_dir, template_path, to_dir)
        else:
            generate_page_recursive(from_dir, template_path, to_dir)
