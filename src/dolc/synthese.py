import os


def create_docs(file_structure):
    with open("docs/SUMMARY.md", "w") as summary:
        summary.write("# Summary\n\n")

        summary.write(create_summary(file_structure))


def create_summary(file_structure, indent_level=0, dir=None) -> str:
    indent = "   " * indent_level
    result = ""
    for key, value in file_structure.items():
        result += f"{indent}- [{key}](docs/"
        if isinstance(value, dict):
            result += f"{key})\n"
            os.mkdir(f"docs/{key}")
            result += create_summary(value, indent_level + 1, key)
        else:
            file_name = f"{key[:-3]}"
            result += f"{file_name}.md)\n"
            create_file(f"docs/{f'{dir}/' if dir else ''}{file_name}.md", file_name)
    return result


def create_file(file_name, title):
    with open(file_name, "w+") as f:
        f.write(f"# {title}")
