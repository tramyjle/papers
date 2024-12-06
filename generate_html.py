import os

# Define the directory containing the papers
papers_dir = "papers"

# Check if the directory exists or create it if missing
if not os.path.exists(papers_dir):
    os.makedirs(papers_dir)  # Create the directory
    print(f"Created a '{papers_dir}' directory. Add your PDF files there and rerun the script.")
else:
    # List all PDF files in the directory
    papers = [file for file in os.listdir(papers_dir) if file.lower().endswith(".pdf")]

    if len(papers) == 0:
        print(f"No PDF files found in the '{papers_dir}' directory. Add your PDF files and rerun the script.")
    else:
        # Generate HTML content
        html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Papers</title>
</head>
<body>
    <h1>My Research Papers</h1>
    <ul>
"""

        for paper in papers:
            # Replace spaces in filenames with '%20' for proper URL encoding in links
            encoded_paper = paper.replace(" ", "%20")
            html_content += f'        <li><a href="{papers_dir}/{encoded_paper}">{paper}</a></li>\n'

        html_content += """
    </ul>
</body>
</html>
"""

        # Save the HTML content to a file
        with open("index.html", "w") as f:
            f.write(html_content)

        print("HTML file 'index.html' has been successfully generated with links to all your papers.")
