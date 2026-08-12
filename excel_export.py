import pandas as pd


def markdown_to_dataframe(markdown_text):
    """
    Converts a Markdown table into a Pandas DataFrame.
    """

    lines = markdown_text.strip().split("\n")

    # Remove empty lines
    lines = [line for line in lines if line.strip()]

    # Keep only table rows
    table_lines = [line for line in lines if line.startswith("|")]

    if len(table_lines) < 3:
        raise ValueError("No valid Markdown table found.")

    # Extract headers
    headers = [h.strip() for h in table_lines[0].split("|")[1:-1]]

    data = []

    # Skip header and separator row
    for line in table_lines[2:]:
        values = [v.strip() for v in line.split("|")[1:-1]]

        if len(values) == len(headers):
            data.append(values)

    df = pd.DataFrame(data, columns=headers)

    return df


def export_to_excel(markdown_text, output_file):
    """
    Converts Markdown table to Excel.
    """

    df = markdown_to_dataframe(markdown_text)

    df.to_excel(output_file, index=False)

    print(f"\nExcel exported successfully to {output_file}")